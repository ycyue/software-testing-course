from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import main as lab  # noqa: E402


class Practice81Tests(unittest.TestCase):
    def test_privilege_matrix(self):
        self.assertEqual(lab.main(), 0)
        saved = json.loads((HERE / "validation" / "latest.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["b_reads_a"], 403)
        self.assertEqual(saved["a_reads_own"], 200)
        self.assertEqual(saved["user_admin"], 403)
        self.assertEqual(saved["admin_admin"], 200)


if __name__ == "__main__":
    unittest.main()
