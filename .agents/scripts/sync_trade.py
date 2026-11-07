#!/usr/bin/env python3
"""
Sync UVG trade multiplier spreadsheet with the Charged campaign website.
Pulls the live Google Sheet CSV, calculates real Cash prices (€),
and generates _data/trade.json consumed dynamically by Jekyll Liquid includes.

Usage:
  python3 .agents/scripts/sync_trade.py
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
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
TRADING_DIR = REPO_ROOT / "trading"
DATA_DIR = REPO_ROOT / "_data"
TRADE_DATA_FILE = DATA_DIR / "trade.json"


def write_if_changed(path: Path, new_content: str) -> bool:
    """Write content to path only if the file does not exist or content differs."""
    if path.exists():
        try:
            if path.read_text(encoding="utf-8") == new_content:
                return False
        except Exception:
            pass
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(new_content, encoding="utf-8")
    return True

SPREADSHEET_CSV_URL = (
    "https://docs.google.com/spreadsheets/d/1TEx8ZmBq90Tyms3u5eVlM2OqpUIemsj6c04rmNXxg94/"
    "export?format=csv&gid=1457428661"
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
        "header_match": "violet",
        "dir_path": "directory/VioletCity/index.md",
    },
    {
        "col_idx": 5,
        "name": "Low Road / High Road",
        "slug": "LowRoadHigh",
        "header_match": "low r",
        "dir_path": "directory/LowRoadHigh/index.md",
    },
    {
        "col_idx": 6,
        "name": "Steppe of Lime Nomads",
        "slug": "LimeNomads",
        "header_match": "steppe lime",
        "dir_path": "directory/LimeNomads/index.md",
    },
    {
        "col_idx": 7,
        "name": "Porcelain Citadel",
        "slug": "PorcelainCitadel",
        "header_match": "porcelain",
        "dir_path": "directory/PorcelainCitadel/index.md",
    },
    {
        "col_idx": 8,
        "name": "Potsherd Crater",
        "slug": "PotsherdCrater",
        "header_match": "potsherd",
        "dir_path": "directory/PotsherdCrater/index.md",
    },
    {
        "col_idx": 9,
        "name": "Trail of Vomish Dreams",
        "slug": "TrailOfVomishDreams",
        "header_match": "vomish",
        "dir_path": None,
    },
    {
        "col_idx": 11,
        "name": "The Last Serai",
        "slug": "LastSerai",
        "header_match": "last serai",
        "dir_path": "directory/LastSerai/index.md",
    },
    {
        "col_idx": 12,
        "name": "Way Stone Graveyard",
        "slug": "WayStoneGraveyard",
        "header_match": "way stone",
        "dir_path": "directory/WayStoneGraveyard/index.md",
    },
    {
        "col_idx": 13,
        "name": "Death-Facing Passage",
        "slug": "DeathFacingPassage",
        "header_match": "death fac",
        "dir_path": "directory/DeathFacingPassage/index.md",
    },
    {
        "col_idx": 14,
        "name": "South-Facing Passage",
        "slug": "SouthFacingPassage",
        "header_match": "south fac",
        "dir_path": None,
    },
]


def validate_header_columns(header_row: list[str]) -> bool:
    """Validate that spreadsheet header row aligns with LOCATION_COLUMNS.

    Raises:
        ValueError: If header row lacks required columns or any expected
                    station header does not match its designated column.
    """
    min_required_cols = max(loc["col_idx"] for loc in LOCATION_COLUMNS) + 1 if LOCATION_COLUMNS else 4
    if len(header_row) < min_required_cols:
        raise ValueError(
            f"Header row has {len(header_row)} columns; expected at least {min_required_cols} columns."
        )

    for loc in LOCATION_COLUMNS:
        col_idx = loc["col_idx"]
        expected_match = loc.get("header_match", "").lower()
        if not expected_match:
            continue

        actual_header = header_row[col_idx].strip().lower()
        if expected_match not in actual_header:
            raise ValueError(
                f"Header column shift detected at index {col_idx}: "
                f"expected '{expected_match}' for station '{loc['name']}', "
                f"but found '{header_row[col_idx]}'."
            )
    return True


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


def fetch_csv() -> Optional[list[list[str]]]:
    """Fetch live CSV matrix directly from the Google Sheets workbook.

    Returns:
        List of row strings if successful, or None if network fetch fails.
    """
    try:
        req = urllib.request.Request(
            SPREADSHEET_CSV_URL,
            headers={"User-Agent": "Charged-Trade-Sync/1.0"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8")
            reader = csv.reader(io.StringIO(content))
            return list(reader)
    except Exception as e:
        print(f"[WARN] Live Google Sheets fetch failed: {e}. Preserving existing trade data.", file=sys.stderr)
        return None


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


def build_trade_data(items: list[dict]) -> dict:
    stations = [
        {"name": loc["name"], "slug": loc["slug"], "dir_path": loc["dir_path"]}
        for loc in LOCATION_COLUMNS
    ]

    items_list = []
    items_by_name = {}
    items_by_slug = {}

    for it in items:
        # Determine most profitable trade route across all stations
        valid_locs = [
            l
            for l in it["locations"]
            if l["has_data"] and l["multiplier"] is not None and l["multiplier"] > 0
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
                best_trade = f"{low_loc['location']} ({low_loc['price_str']}) --> {high_loc['location']} ({high_loc['price_str']})"
            else:
                best_trade = '<em style="color: #888;">No great trade identified.</em>'
        else:
            best_trade = '<em style="color: #888;">No great trade identified.</em>'

        item_locations = []
        for loc in it["locations"]:
            if not loc["has_data"]:
                cond_html = ""
            elif loc["multiplier"] == 1.0 and "standard open-market demand" in loc["condition"].lower():
                cond_html = f'<em style="color: #888;">{loc["condition"]}</em>'
            else:
                cond_html = loc["condition"]

            item_locations.append(
                {
                    "name": loc["location"],
                    "slug": loc["slug"],
                    "dir_path": loc["dir_path"],
                    "price_str": loc["price_str"],
                    "has_data": loc["has_data"],
                    "multiplier": loc["multiplier"],
                    "condition": loc["condition"],
                    "condition_html": cond_html,
                }
            )

        item_dict = {
            "ref": it["ref"],
            "name": it["name"],
            "slug": it["slug"],
            "category": it["category"],
            "size": it["size"],
            "base_price": it["base_price"],
            "best_trade": best_trade,
            "locations": item_locations,
        }
        items_list.append(item_dict)
        items_by_name[it["name"]] = item_dict
        items_by_slug[it["slug"]] = item_dict

    # Build per-location trade summaries
    locations_data = {}
    for st in LOCATION_COLUMNS:
        st_name = st["name"]
        loc_rows = []
        for it in items:
            st_loc = next((l for l in it["locations"] if l["location"] == st_name), None)
            local_price = st_loc["price_str"] if (st_loc and st_loc["has_data"]) else "—"

            valid = [
                l
                for l in it["locations"]
                if l["has_data"] and l["multiplier"] is not None and l["multiplier"] > 0
            ]
            route_str = None

            if st_loc and st_loc["has_data"] and st_loc["multiplier"] and st_loc["multiplier"] > 0:
                st_m = st_loc["multiplier"]
                other_valid = [l for l in valid if l["location"] != st_name]
                if other_valid:
                    max_other = max(l["multiplier"] for l in other_valid)
                    min_other = min(l["multiplier"] for l in other_valid)
                    export_p = max_other - st_m
                    import_p = st_m - min_other

                    if max(export_p, import_p) > 0:
                        if export_p >= import_p:
                            highs = [l for l in other_valid if l["multiplier"] == max_other]
                            high_loc = next(
                                (
                                    l
                                    for l in highs
                                    if any(k in l.get("condition", "").lower() for k in ["bubble", "demand", "crisis"])
                                ),
                                highs[0],
                            )
                            route_str = f"{st_name} ({st_loc['price_str']}) --> {high_loc['location']} ({high_loc['price_str']})"
                        else:
                            lows = [l for l in other_valid if l["multiplier"] == min_other]
                            low_loc = next(
                                (l for l in lows if "source" in l.get("condition", "").lower()),
                                lows[0],
                            )
                            route_str = f"{low_loc['location']} ({low_loc['price_str']}) --> {st_name} ({st_loc['price_str']})"

            display_route = route_str if route_str else '<em style="color: #888;">No great trade identified.</em>'
            loc_rows.append(
                {
                    "ref": it["ref"],
                    "name": it["name"],
                    "slug": it["slug"],
                    "price_str": local_price,
                    "best_trade": display_route,
                }
            )
        locations_data[st_name] = loc_rows

    return {
        "stations": stations,
        "items": items_list,
        "items_by_name": items_by_name,
        "items_by_slug": items_by_slug,
        "locations": locations_data,
    }


def save_trade_data(trade_data: dict) -> bool:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    content = json.dumps(trade_data, indent=2, ensure_ascii=False) + "\n"
    return write_if_changed(TRADE_DATA_FILE, content)


def ensure_item_pages(items: list[dict]) -> int:
    changed = 0
    for it in items:
        out_file = TRADING_DIR / f"{it['slug']}.md"
        page_md = (
            "---\n"
            "layout: default\n"
            f"title: \"{it['name']}\"\n"
            "parent: Trading\n"
            "nav_exclude: false\n"
            "---\n"
            "\n"
            "# {{ page.title }}\n"
            "\n"
            "{% include trade_item.html %}\n"
        )
        if write_if_changed(out_file, page_md):
            changed += 1
    return changed


def ensure_index_page() -> bool:
    index_file = TRADING_DIR / "index.md"
    index_md = (
        "---\n"
        "layout: default\n"
        "title: Trading\n"
        "has_children: true\n"
        "has_toc: false\n"
        "nav_order: 40\n"
        "---\n"
        "\n"
        "# Ultraviolet Grasslands Commerce & Trade\n"
        "\n"
        "Live trade prices and market conditions along the Great Road across the Vastlands. Synchronised with the caravan ledger.\n"
        "\n"
        "## Trade Goods Summary\n"
        "\n"
        "{% include trade_summary.html %}\n"
    )
    return write_if_changed(index_file, index_md)


PUBLISHED_LOCATIONS = [
    {"name": "Violet City", "file": REPO_ROOT / "directory/VioletCity/index.md"},
    {"name": "Low Road / High Road", "file": REPO_ROOT / "directory/LowRoadHigh/index.md"},
    {"name": "Steppe of Lime Nomads", "file": REPO_ROOT / "directory/LimeNomads/index.md"},
    {"name": "Porcelain Citadel", "file": REPO_ROOT / "directory/PorcelainCitadel/index.md"},
    {"name": "The Last Serai", "file": REPO_ROOT / "directory/LastSerai/index.md"},
]


def ensure_location_pages() -> int:
    changed = 0
    for loc_info in PUBLISHED_LOCATIONS:
        file_path = loc_info["file"]
        if not file_path.exists():
            continue

        content = file_path.read_text(encoding="utf-8")
        heading_match = re.search(r"\n## Trade & Commerce\b", content)
        if heading_match:
            base_content = content[: heading_match.start()].rstrip()
        else:
            base_content = content.rstrip()

        # If it already includes the dynamic template, do not rewrite
        if "{% include trade_location.html %}" in base_content:
            continue

        new_content = f"{base_content}\n\n{{% include trade_location.html %}}\n"
        if write_if_changed(file_path, new_content):
            print(f"[LOCATION] Updated {file_path.relative_to(REPO_ROOT)} to dynamic Liquid include.")
            changed += 1
    return changed


def main():
    parser = argparse.ArgumentParser(description="Sync UVG trade sheet with website.")
    parser.parse_args()

    TRADING_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    rows = fetch_csv()
    if rows is None:
        print("[INFO] Could not fetch live trade sheet; existing _data/trade.json was preserved.")
        return

    if not rows:
        sys.exit("[ERROR] CSV data is empty.")

    try:
        validate_header_columns(rows[0])
    except ValueError as err:
        sys.exit(f"[ERROR] Spreadsheet validation failed: {err}")

    items = parse_trade_items(rows)

    # 1. Build and save backend JSON data
    trade_data = build_trade_data(items)
    if save_trade_data(trade_data):
        print(f"[DATA] Wrote backend trade data to {TRADE_DATA_FILE.relative_to(REPO_ROOT)}")
    else:
        print(f"[DATA] {TRADE_DATA_FILE.relative_to(REPO_ROOT)} is up to date.")

    # 2. Ensure master trading hub index uses dynamic Liquid include
    if ensure_index_page():
        print(f"[INDEX] Updated {TRADING_DIR.relative_to(REPO_ROOT)}/index.md to dynamic Liquid include.")
    else:
        print(f"[INDEX] {TRADING_DIR.relative_to(REPO_ROOT)}/index.md is up to date.")

    # 3. Ensure each trade item page uses dynamic Liquid include
    updated_items = ensure_item_pages(items)
    if updated_items > 0:
        print(f"[ITEMS] Synchronised {updated_items} item pages in {TRADING_DIR.relative_to(REPO_ROOT)}/ to Liquid include.")
    else:
        print(f"[ITEMS] All {len(items)} trade items in {TRADING_DIR.relative_to(REPO_ROOT)}/ are up to date.")

    # 4. Ensure published location pages use dynamic Liquid include
    updated_locations = ensure_location_pages()
    if updated_locations == 0:
        print("[LOCATION] All published location pages are up to date.")


if __name__ == "__main__":
    main()
