from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import main as lab  # noqa: E402


class Practice131Tests(unittest.TestCase):
    def test_four_shapes(self):
        self.assertEqual(lab.main(), 0)
        saved = json.loads((HERE / "validation" / "latest.json").read_text(encoding="utf-8"))
        names = [r["name"] for r in saved["rows"]]
        self.assertEqual(names, ["missing", "null", "empty_str", "wrong_type"])
        self.assertTrue(all(r["ok"] for r in saved["rows"]))


if __name__ == "__main__":
    unittest.main()
