from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import main as lab  # noqa: E402


class Practice151Tests(unittest.TestCase):
    def test_reads_products_json(self):
        self.assertEqual(lab.main(), 0)
        saved = json.loads((HERE / "validation" / "latest.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["item_count"], 3)
        self.assertEqual(saved["mouse_stock"], 10)
        self.assertTrue((HERE / "validation" / "products.json").is_file())


if __name__ == "__main__":
    unittest.main()
