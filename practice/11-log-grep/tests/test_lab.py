from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import main as lab  # noqa: E402


class Practice111Tests(unittest.TestCase):
    def test_log_has_reject(self):
        self.assertEqual(lab.main(), 0)
        saved = json.loads((HERE / "validation" / "latest.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["http_status"], 400)
        self.assertTrue(any("inventory reject" in line for line in saved["log_hits"]))


if __name__ == "__main__":
    unittest.main()
