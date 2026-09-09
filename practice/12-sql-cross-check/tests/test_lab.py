from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import main as lab  # noqa: E402


class Practice121Tests(unittest.TestCase):
    def test_api_matches_sql(self):
        self.assertEqual(lab.main(), 0)
        saved = json.loads((HERE / "validation" / "latest.json").read_text(encoding="utf-8"))
        self.assertTrue(saved["match"])
        self.assertEqual(saved["api_qty"], 2)
        self.assertEqual(saved["sql_qty"], 2)


if __name__ == "__main__":
    unittest.main()
