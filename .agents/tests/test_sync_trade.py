"""Unit test harness for Ultraviolet Grasslands trade synchronisation pipeline.

Validates:
1. Header column alignment and column shift detection.
2. Base price parsing, fallbacks, split formats, and multiplier calculations.
3. Market condition text categorisation.
4. Route maximisation and trade route optimisation logic.
5. Complete trade data JSON schema and dictionary indexing.
"""

import csv
import io
import sys
import unittest
from pathlib import Path

# Add scripts directory to module search path
REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / ".agents" / "scripts"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import sync_trade


class TestHeaderValidation(unittest.TestCase):
    """Test spreadsheet header alignment and column-shift detection."""

    def setUp(self):
        self.canonical_header = [
            "Ref", "Trade Good", "Size", "€",
            "1 Violet City", "2 Low R High", "3 Steppe Lime", "4 Porcelain C",
            "5 Potsherd Cr", "6 T Vomish Dr", "", "8 Last Serai",
            "9 Way Stone", "10 Death Fac P", "11 South Fac P"
        ]

    def test_valid_canonical_header(self):
        """Ensure canonical 15-column header passes validation."""
        self.assertTrue(sync_trade.validate_header_columns(self.canonical_header))

    def test_header_too_short(self):
        """Ensure header with fewer than 15 columns raises ValueError."""
        short_header = self.canonical_header[:14]
        with self.assertRaises(ValueError) as ctx:
            sync_trade.validate_header_columns(short_header)
        self.assertIn("expected at least 15 columns", str(ctx.exception))

    def test_shifted_columns_detected(self):
        """Ensure column shift (e.g. inserted column) is caught immediately."""
        shifted_file = FIXTURES_DIR / "shifted_columns.csv"
        with open(shifted_file, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))
        with self.assertRaises(ValueError) as ctx:
            sync_trade.validate_header_columns(reader[0])
        self.assertIn("Header column shift detected", str(ctx.exception))

    def test_misnamed_station_column(self):
        """Ensure an unexpected station column header name raises ValueError."""
        corrupted = list(self.canonical_header)
        corrupted[4] = "1 Metropolis"
        with self.assertRaises(ValueError) as ctx:
            sync_trade.validate_header_columns(corrupted)
        self.assertIn("Violet City", str(ctx.exception))


class TestPriceAndConditionParsing(unittest.TestCase):
    """Test price calculation formulas, fallback values, and condition mapping."""

    def test_fallback_base_price(self):
        """Ensure blank base price falls back to canonical UVG base price dictionary."""
        rows = [
            ["Ref", "Trade Good", "Size", "€", "1 Violet City", "2 Low R High", "3 Steppe Lime", "4 Porcelain C", "5 Potsherd Cr", "6 T Vomish Dr", "", "8 Last Serai", "9 Way Stone", "10 Death Fac P", "11 South Fac P"],
            ["TG01", "Alchemical lubricants", "Sack", "", "x1", "", "", "", "", "", "", "", "", "", ""]
        ]
        items = sync_trade.parse_trade_items(rows)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["base_price"], "€100")
        vc_loc = next(l for l in items[0]["locations"] if l["location"] == "Violet City")
        self.assertEqual(vc_loc["price_str"], "€100")

    def test_explicit_base_price_and_multiplier(self):
        """Ensure explicit base price with multiplier produces exact cash calculations."""
        rows = [
            ["Ref", "Trade Good", "Size", "€", "1 Violet City", "2 Low R High", "3 Steppe Lime", "4 Porcelain C", "5 Potsherd Cr", "6 T Vomish Dr", "", "8 Last Serai", "9 Way Stone", "10 Death Fac P", "11 South Fac P"],
            ["TG04", "Chitin cap", "Sack", "100", "", "x0, no market", "", "x0.5, low market", "", "", "", "x3 market bubble!", "", "", ""]
        ]
        items = sync_trade.parse_trade_items(rows)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["base_price"], "€100")

        locs = {l["location"]: l for l in items[0]["locations"]}
        self.assertEqual(locs["Low Road / High Road"]["price_str"], "€0")
        self.assertEqual(locs["Porcelain Citadel"]["price_str"], "€50")
        self.assertEqual(locs["The Last Serai"]["price_str"], "€300")

    def test_split_base_price_and_multiplier(self):
        """Ensure split base price format (€10/40) scales both components correctly."""
        rows = [
            ["Ref", "Trade Good", "Size", "€", "1 Violet City", "2 Low R High", "3 Steppe Lime", "4 Porcelain C", "5 Potsherd Cr", "6 T Vomish Dr", "", "8 Last Serai", "9 Way Stone", "10 Death Fac P", "11 South Fac P"],
            ["", "Crystal shards/spheres", "Sack", "10/40", "x1", "x2", "", "", "", "", "", "", "", "", ""]
        ]
        items = sync_trade.parse_trade_items(rows)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["base_price"], "€10/40")

        locs = {l["location"]: l for l in items[0]["locations"]}
        self.assertEqual(locs["Violet City"]["price_str"], "€10/40")
        self.assertEqual(locs["Low Road / High Road"]["price_str"], "€20/80")

    def test_market_condition_parsing(self):
        """Ensure market condition notes map to formatted British English descriptions."""
        cond_taboo = sync_trade.parse_market_condition("x0, taboo", 0.0)
        self.assertIn("**Taboo:**", cond_taboo)

        cond_bubble = sync_trade.parse_market_condition("x3 market bubble!", 3.0)
        self.assertIn("**Market Bubble:**", cond_bubble)

        cond_crisis = sync_trade.parse_market_condition("x4, crisis demand", 4.0)
        self.assertIn("**Crisis Demand:**", cond_crisis)

        cond_illicit = sync_trade.parse_market_condition("x2, popular & illegal", 2.0)
        self.assertIn("**Illicit Contraband:**", cond_illicit)

        cond_source = sync_trade.parse_market_condition("x0.5 source", 0.5)
        self.assertIn("**Domestic Source:**", cond_source)

        cond_soft = sync_trade.parse_market_condition("x0.5, low demand", 0.5)
        self.assertIn("**Soft Market:**", cond_soft)

        cond_normal = sync_trade.parse_market_condition("x1, normal", 1.0)
        self.assertEqual(cond_normal, "Standard open-market demand.")


class TestRouteOptimisation(unittest.TestCase):
    """Test trade route optimisation and arbitrage calculation logic."""

    def test_global_best_trade_route(self):
        """Ensure global route identifies highest margin between source/low and bubble/high."""
        rows = [
            ["Ref", "Trade Good", "Size", "€", "1 Violet City", "2 Low R High", "3 Steppe Lime", "4 Porcelain C", "5 Potsherd Cr", "6 T Vomish Dr", "", "8 Last Serai", "9 Way Stone", "10 Death Fac P", "11 South Fac P"],
            ["", "Fine tubers", "Sack", "100", "x1", "x1", "x1", "x3, market bubble", "", "", "", "x1", "x1", "x0.5, low demand", "x1"]
        ]
        items = sync_trade.parse_trade_items(rows)
        trade_data = sync_trade.build_trade_data(items)
        item_entry = trade_data["items"][0]

        expected_route = "Death-Facing Passage (€50) --> Porcelain Citadel (€300)"
        self.assertEqual(item_entry["best_trade"], expected_route)

    def test_flat_pricing_no_arbitrage(self):
        """Ensure identical prices across stations return no great trade identified message."""
        rows = [
            ["Ref", "Trade Good", "Size", "€", "1 Violet City", "2 Low R High", "3 Steppe Lime", "4 Porcelain C", "5 Potsherd Cr", "6 T Vomish Dr", "", "8 Last Serai", "9 Way Stone", "10 Death Fac P", "11 South Fac P"],
            ["TG05", "Common intoxicants", "Sack", "2000", "x1", "x1", "", "", "", "", "", "x1", "", "", ""]
        ]
        items = sync_trade.parse_trade_items(rows)
        trade_data = sync_trade.build_trade_data(items)
        item_entry = trade_data["items"][0]

        self.assertIn("No great trade identified", item_entry["best_trade"])

    def test_station_export_and_import_routes(self):
        """Ensure location trade summary computes correct directional arrows for import/export."""
        rows = [
            ["Ref", "Trade Good", "Size", "€", "1 Violet City", "2 Low R High", "3 Steppe Lime", "4 Porcelain C", "5 Potsherd Cr", "6 T Vomish Dr", "", "8 Last Serai", "9 Way Stone", "10 Death Fac P", "11 South Fac P"],
            ["TG01", "Alchemical lubricants", "Sack", "100", "", "x2", "x1", "x1", "x0.5, low demand", "", "", "", "", "", ""]
        ]
        items = sync_trade.parse_trade_items(rows)
        trade_data = sync_trade.build_trade_data(items)

        # For Low Road / High Road (price €200, max on trail): best import is Potsherd Crater -> Low Road / High Road
        lrh_row = trade_data["locations"]["Low Road / High Road"][0]
        self.assertEqual(lrh_row["price_str"], "€200")
        self.assertIn("Potsherd Crater (€50) --> Low Road / High Road (€200)", lrh_row["best_trade"])

        # For Potsherd Crater (price €50, min on trail): best export is Potsherd Crater -> Low Road / High Road
        pc_row = trade_data["locations"]["Potsherd Crater"][0]
        self.assertEqual(pc_row["price_str"], "€50")
        self.assertIn("Potsherd Crater (€50) --> Low Road / High Road (€200)", pc_row["best_trade"])


class TestTradeDataSchema(unittest.TestCase):
    """Test compiled JSON structure and lookup indexing."""

    def setUp(self):
        fixture_path = FIXTURES_DIR / "sample_market_research.csv"
        with open(fixture_path, "r", encoding="utf-8") as f:
            rows = list(csv.reader(f))
        items = sync_trade.parse_trade_items(rows)
        self.trade_data = sync_trade.build_trade_data(items)

    def test_root_keys_present(self):
        """Ensure required top-level keys exist in trade_data dictionary."""
        required_keys = {"stations", "items", "locations"}
        self.assertTrue(required_keys.issubset(self.trade_data.keys()))

    def test_stations_schema(self):
        """Ensure stations list contains all 10 canonical trail stations."""
        self.assertEqual(len(self.trade_data["stations"]), 10)
        for st in self.trade_data["stations"]:
            self.assertIn("name", st)
            self.assertIn("slug", st)
            self.assertIn("dir_path", st)

    def test_items_schema(self):
        """Ensure items list contains expected schema attributes."""
        items = self.trade_data["items"]
        self.assertGreater(len(items), 0)
        for it in items:
            self.assertIn("ref", it)
            self.assertIn("name", it)
            self.assertIn("slug", it)
            self.assertIn("category", it)
            self.assertIn("size", it)
            self.assertIn("base_price", it)
            self.assertIn("best_trade", it)
            self.assertIn("locations", it)
            self.assertEqual(len(it["locations"]), 10)
            for loc in it["locations"]:
                self.assertIn("name", loc)
                self.assertIn("dir_path", loc)
                self.assertIn("price_str", loc)
                self.assertIn("condition_html", loc)

    def test_locations_map_all_stations(self):
        """Ensure every station has an item pricing table in locations dictionary."""
        for st in self.trade_data["stations"]:
            st_name = st["name"]
            self.assertIn(st_name, self.trade_data["locations"])
            loc_items = self.trade_data["locations"][st_name]
            self.assertEqual(len(loc_items), len(self.trade_data["items"]))
            for entry in loc_items:
                self.assertIn("ref", entry)
                self.assertIn("name", entry)
                self.assertIn("slug", entry)
                self.assertIn("price_str", entry)
                self.assertIn("best_trade", entry)


if __name__ == "__main__":
    unittest.main()
