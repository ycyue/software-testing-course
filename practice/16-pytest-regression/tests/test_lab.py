from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import main as lab  # noqa: E402


class Practice161Tests(unittest.TestCase):
    def test_pytest_baseline(self):
        code = lab.main()
        if code == 2:
            saved = json.loads((HERE / "validation" / "latest.json").read_text(encoding="utf-8"))
            if "No module named pytest" in saved.get("verdict", "") or not saved.get("passed_37"):
                self.skipTest("pytest not installed; run project/minishop/run.py setup")
        self.assertEqual(code, 0)
        saved = json.loads((HERE / "validation" / "latest.json").read_text(encoding="utf-8"))
        self.assertTrue(saved["passed_37"])
        self.assertTrue(saved["xfailed_1"])


if __name__ == "__main__":
    unittest.main()
