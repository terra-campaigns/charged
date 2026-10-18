#!/usr/bin/env python3
"""
Sync UVG trade multiplier spreadsheet with the Charged campaign website.
Pulls the live Google Sheet CSV, calculates real Cash prices (€),
and generates:
  - trading/index.md (Top-level master commerce hub)
  - trading/<item>.md (Individual child notes for each active trade good, mount, or tool)

Usage:
  python3 .agents/scripts/sync_trade.py
  python3 .agents/scripts/sync_trade.py --offline  # Use cached CSV without fetching
"""

import argparse
import csv
import io
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TRADING_DIR = REPO_ROOT / "trading"
CACHE_FILE = REPO_ROOT / ".agents" / "context" / "trade_sheet_cache.csv"

SPREADSHEET_CSV_URL = (
    "https://docs.google.com/spreadsheets/d/1jzVvpxaQsuevjKaFAHmi2KpHFvdh9q9F6tG8ZeVBTMw/"
    "export?format=csv&gid=35129677"
)

# Standard UVG 2E fallback prices for items if blank in the spreadsheet
UVG_FALLBACK_BASE_PRICES = {
    "TG01": 100,    # Alchemical lubricants
    "TG02": 100,    # Beast egg masses
    "TG03": 50,     # Bone-work
    "TG04": 100,    # Chitin cap
    "TG05": 2000,   # Common intoxicants
    "TG06": 1000,   # Cosmic scales
    "TG07": 200,    # Dryland coral seeds
    "TG08": 1000,   # Gems and jewels
    "TG09": 1000,   # Gold
    "TG10": 500,    # Indigo ivories
    "TG11": 500,    # Joy worms
    "TG12": 200,    # Karma dust
    "TG13": 500,    # Last steel
    "TG14": 100,    # Livingstone bricks
    "TG15": 50,     # Marrow-beet
    "TG16": 1000,   # Medimagicals
    "TG18": 100,    # Odd fruits
    "TG19": 50,     # Rediothermal fuel
    "TG20": 500,    # Rainbow silks
    "TG21": 10000,  # Rare drugs
    "TG22": 2000,   # Replacement bodies
    "TG23": 1000,   # Saffron
    "TG24": 500,    # Sanguine porcelains
    "TG25": 500,    # Silver
    "TG26": 2000,   # Soul-stones
    "TG27": 200,    # Ultra jay needles
    "TG28": 500,    # Vampire wines
    "TG29": 500,    # Vidy crystals
    "TG30": 200,    # Weapons and armours
    "VM07": 70,     # Mules
    "VM08": 200,    # Combat steed
    "VM18": 6000,   # Prismatic Walker
    "TK12": 100,    # Navigator's suitcase
    "TK15": 50,     # Prospector Kit
    "TK19": 100,    # Veterinarian Kit
}

LOCATION_COLUMNS = [
    {
        "col_idx": 4,
        "name": "Violet City",
        "slug": "VioletCity",
        "dir_path": "directory/VioletCity/index.md",
    },
    {
        "col_idx": 5,
        "name": "Low Road / High Road",
        "slug": "LowRoadHigh",
        "dir_path": "directory/LowRoadHigh/index.md",
    },
    {
        "col_idx": 6,
        "name": "Steppe of Lime Nomads",
        "slug": "LimeNomads",
        "dir_path": "directory/LimeNomads/index.md",
    },
    {
        "col_idx": 7,
        "name": "Porcelain Citadel",
        "slug": "PorcelainCitadel",
        "dir_path": "directory/PorcelainCitadel/index.md",
    },
    {
        "col_idx": 8,
        "name": "Potsherd Crater",
        "slug": "PotsherdCrater",
        "dir_path": None,
    },
    {
        "col_idx": 9,
        "name": "Trail of Vomish Dreams",
        "slug": "TrailOfVomishDreams",
        "dir_path": None,
    },
    {
        "col_idx": 11,
        "name": "The Last Serai",
        "slug": "LastSerai",
        "dir_path": "directory/LastSerai/index.md",
    },
]


def clean_slug(name: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", name).strip()
    return re.sub(r"[\s_-]+", "_", cleaned)


def parse_market_condition(note: str, mult: float) -> str:
    lower = note.lower().strip()
    if "taboo" in lower:
        return "**Taboo:** Possession or trade strictly forbidden by local edicts."
    if "bubble" in lower:
        return "**Market Bubble:** Wild speculative surge in local purchasing price."
    if "crisis" in lower:
        return "**Crisis Demand:** Severe critical shortage; merchants pay emergency premiums."
    if "illegal" in lower or "ilegal" in lower:
        return "**Illicit Contraband:** High black-market demand; carries confiscation or arrest risk."
    if "source" in lower:
        return "**Domestic Source:** Locally harvested or produced; steady supply."
    if "no market" in lower or "useless" in lower:
        return "**No Market:** Completely unwanted or useless to local buyers."
    if "low demand" in lower or "low market" in lower:
        return "**Soft Market:** Saturated or low interest; buyers demand discounts."
    if "high demand" in lower:
        return "**High Demand:** Eager buyers offering premium margins."
    if "haggle" in lower:
        return f"**Controlled Trade:** Regulated guild monopoly; difficult negotiation ({note})."
    if "equivalent material" in lower:
        return f"**Local Substitute:** Similar regional goods available ({note})."
    if "close" in lower:
        return "**Proximate Supply:** Close to production origin; prices slightly depressed."
    if "old caravans" in lower:
        return "**Caravan Glut:** Influx from abandoned or broken caravans depressing value."
    if "normal" in lower:
        return "Standard open-market demand."
    if note:
        return f"**Local Condition:** {note.capitalize()}."
    if mult == 1.0:
        return "Standard open-market demand."
    if mult > 1.0:
        return f"Elevated regional demand (price factor $\\times {mult:g}$)."
    if mult == 0.0:
        return "Zero market demand."
    return f"Discounted regional market (price factor $\\times {mult:g}$)."


def fetch_csv(use_cache: bool = False) -> list[list[str]]:
    if not use_cache:
        try:
            req = urllib.request.Request(
                SPREADSHEET_CSV_URL,
                headers={"User-Agent": "Charged-Trade-Sync/1.0"},
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read().decode("utf-8")
                CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
                CACHE_FILE.write_text(content, encoding="utf-8")
                reader = csv.reader(io.StringIO(content))
                return list(reader)
        except Exception as e:
            print(f"[WARN] Live fetch failed ({e}). Falling back to local cache.", file=sys.stderr)

    if CACHE_FILE.exists():
        content = CACHE_FILE.read_text(encoding="utf-8")
        reader = csv.reader(io.StringIO(content))
        return list(reader)

    sys.exit("Error: Could not fetch Google Sheet CSV and no local cache was found.")


def parse_trade_items(rows: list[list[str]]) -> list[dict]:
    items = []

    for idx, row in enumerate(rows[1:], start=2):
        if not row or not any(c.strip() for c in row):
            continue

        ref = row[0].strip() if len(row) > 0 else ""
        name = row[1].strip() if len(row) > 1 else ""
        size = row[2].strip() if len(row) > 2 else "Sack"
        base_price_raw = row[3].strip() if len(row) > 3 else ""

        if not name:
            if ref.startswith("VM"):
                name = f"Vehicle / Mount {ref}"
            elif ref.startswith("TK"):
                name = f"Toolkit {ref}"
            elif ref.startswith("TG"):
                name = f"Trade Good {ref}"
            else:
                continue

        # Determine category
        if ref.startswith("TG"):
            category = "Trade Goods"
        elif ref.startswith("VM"):
            category = "Vehicles & Mounts"
        elif ref.startswith("TK"):
            category = "Toolkits"
        else:
            category = "Speciality Cargo"

        # Determine base price
        base_price_display = "—"
        base_price_val = None
        if base_price_raw:
            if "/" in base_price_raw:
                cleaned = re.sub(r"[^\d/]", "", base_price_raw)
                base_price_display = f"€{cleaned}"
                base_price_val = cleaned  # split format
            else:
                try:
                    num = float(re.sub(r"[^\d.]", "", base_price_raw))
                    base_price_val = num
                    formatted = int(num) if num.is_integer() else num
                    base_price_display = f"€{formatted}"
                except ValueError:
                    base_price_display = f"€{base_price_raw}"
        elif ref in UVG_FALLBACK_BASE_PRICES:
            num = UVG_FALLBACK_BASE_PRICES[ref]
            base_price_val = float(num)
            base_price_display = f"€{num}"
        else:
            base_price_display = "—"

        # Parse locations
        location_data = []
        has_active_market = False

        for loc_cfg in LOCATION_COLUMNS:
            col_idx = loc_cfg["col_idx"]
            cell_val = row[col_idx].strip() if len(row) > col_idx else ""

            if not cell_val:
                location_data.append(
                    {
                        "location": loc_cfg["name"],
                        "slug": loc_cfg["slug"],
                        "dir_path": loc_cfg["dir_path"],
                        "has_data": False,
                        "multiplier": None,
                        "price_str": "—",
                        "condition": "No recorded market data.",
                    }
                )
                continue

            has_active_market = True
            m = re.match(r"x([0-9]+(?:\.[0-9]+)?)[,\.\s]*(.*)", cell_val, re.I)
            if m:
                mult = float(m.group(1))
                note = m.group(2).strip(" ,.")
            else:
                mult = 1.0
                note = cell_val

            # Calculate price
            if mult == 0.0:
                price_str = "€0"
            elif base_price_val is not None:
                if isinstance(base_price_val, str) and "/" in base_price_val:
                    parts = base_price_val.split("/")
                    calc_parts = []
                    for p in parts:
                        try:
                            v = float(p.strip()) * mult
                            calc_parts.append(str(int(v) if v.is_integer() else f"{v:.1f}"))
                        except ValueError:
                            calc_parts.append(p)
                    price_str = f"€{'/'.join(calc_parts)}"
                else:
                    calc = base_price_val * mult
                    formatted_calc = int(calc) if calc.is_integer() else f"{calc:.1f}"
                    price_str = f"€{formatted_calc}"
            else:
                price_str = f"Base $\\times {mult:g}$"

            condition = parse_market_condition(note, mult)

            location_data.append(
                {
                    "location": loc_cfg["name"],
                    "slug": loc_cfg["slug"],
                    "dir_path": loc_cfg["dir_path"],
                    "has_data": True,
                    "multiplier": mult,
                    "price_str": price_str,
                    "condition": condition,
                }
            )

        # Include if it has base price or at least one active market entry
        if has_active_market or (base_price_val is not None):
            slug = f"{ref}_{clean_slug(name)}" if ref else clean_slug(name)
            items.append(
                {
                    "ref": ref,
                    "name": name,
                    "category": category,
                    "size": size or "Sack",
                    "base_price": base_price_display,
                    "locations": location_data,
                    "slug": slug,
                }
            )

    return items


def generate_item_page(item: dict) -> str:
    ref_display = item["ref"] or "Custom / Local"
    base_price_display = item["base_price"]

    lines = [
        "---",
        "layout: default",
        f"title: \"{item['name']}\"",
        "parent: Trading",
        "nav_exclude: false",
        "---",
        "",
        f"# {item['name']}",
        "",
        "| | | | |",
        "| :--- | :--- | :--- | :--- |",
        "| **Reference Code** | **Category** | **Standard Unit** | **Base Value** |",
        f"| {ref_display} | {item['category']} | {item['size']} | {base_price_display} |",
        "",
        "## Trail Prices & Market Conditions",
        "",
        "Prices reflect actual caravan transaction rates in Cash (€) across the trade corridor.",
        "",
        "| | | |",
        "| :--- | :--- | :--- |",
        "| **Trail Station** | **Local Price** | **Market Situation** |",
    ]

    for loc in item["locations"]:
        if loc["dir_path"]:
            loc_label = f"**[{loc['location']}](../{loc['dir_path']})**"
        else:
            loc_label = f"**{loc['location']}**"

        if not loc["has_data"]:
            cond_str = ""
        elif loc["multiplier"] == 1.0 and "standard open-market demand" in loc["condition"].lower():
            cond_str = f'<em style="color: #888;">{loc["condition"]}</em>'
        else:
            cond_str = loc["condition"]

        lines.append(f"| {loc_label} | {loc['price_str']} | {cond_str} |")

    lines.append("")
    return "\n".join(lines)


def generate_index_page(items: list[dict]) -> str:
    # Format month and day (MM:DD) so it appears in-world as a timestamp (e.g. 10:18 of yesterday)
    time_sim_str = datetime.now(timezone.utc).astimezone().strftime("%m:%d")
    lines = [
        "---",
        "layout: default",
        "title: Trading",
        "has_children: true",
        "has_toc: false",
        "nav_order: 40",
        "---",
        "",
        "# Ultraviolet Grasslands Commerce & Trade",
        "",
        f"Live trade prices and market conditions along the Great Road from the **Violet City** to **The Last Serai**. Synchronised with the caravan ledger at {time_sim_str} of yesterday.",
        "",
        "## Trade Goods Summary",
        "",
        "| | | | |",
        "| :--- | :--- | :--- | :--- |",
        "| **Ref** | **Item** | **Base** | **Most profitable trade on the Grasslands** |",
    ]

    for it in items:
        # Determine most profitable trade route (lowest known price -> highest known price)
        valid_locs = [
            loc
            for loc in it["locations"]
            if loc["has_data"] and loc["multiplier"] is not None and loc["multiplier"] > 0
        ]

        if len(valid_locs) >= 2:
            min_mult = min(l["multiplier"] for l in valid_locs)
            max_mult = max(l["multiplier"] for l in valid_locs)
            if min_mult < max_mult:
                lows = [l for l in valid_locs if l["multiplier"] == min_mult]
                highs = [l for l in valid_locs if l["multiplier"] == max_mult]
                low_loc = next((l for l in lows if "source" in l.get("condition", "").lower()), lows[0])
                high_loc = next(
                    (
                        l
                        for l in highs
                        if any(k in l.get("condition", "").lower() for k in ["bubble", "demand", "crisis"])
                    ),
                    highs[0],
                )
                route_str = f"{low_loc['location']} ({low_loc['price_str']}) --> {high_loc['location']} ({high_loc['price_str']})"
            else:
                route_str = '<em style="color: #888;">No great trade identified.</em>'
        else:
            route_str = '<em style="color: #888;">No great trade identified.</em>'

        lines.append(
            f"| {it['ref'] or '—'} | **[{it['name']}]({it['slug']}.md)** | {it['base_price']} | {route_str} |"
        )

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Sync UVG trade sheet with website.")
    parser.add_argument("--offline", action="store_true", help="Use local cached CSV without web request.")
    args = parser.parse_args()

    TRADING_DIR.mkdir(parents=True, exist_ok=True)
    rows = fetch_csv(use_cache=args.offline)
    items = parse_trade_items(rows)

    # Write trading/index.md
    index_md = generate_index_page(items)
    (TRADING_DIR / "index.md").write_text(index_md, encoding="utf-8")
    print(f"[INDEX] Wrote {TRADING_DIR / 'index.md'}")

    # Write each item note
    written_count = 0
    for it in items:
        page_md = generate_item_page(it)
        out_file = TRADING_DIR / f"{it['slug']}.md"
        out_file.write_text(page_md, encoding="utf-8")
        written_count += 1

    print(f"[ITEMS] Synchronized {written_count} trade items into {TRADING_DIR.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()
