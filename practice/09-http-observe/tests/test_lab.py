from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import main as lab  # noqa: E402


class Practice91Tests(unittest.TestCase):
    def test_four_slots_and_auth(self):
        self.assertEqual(lab.main(), 0)
        saved = json.loads((HERE / "validation" / "latest.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["request"]["method"], "POST")
        self.assertEqual(saved["request"]["path"], "/api/login")
        self.assertTrue(saved["response"]["has_token"])
        self.assertTrue(saved["response"]["has_set_cookie"])
        text = (HERE / "validation" / "latest.json").read_text(encoding="utf-8")
        self.assertNotIn("Test1234", text)


if __name__ == "__main__":
    unittest.main()
