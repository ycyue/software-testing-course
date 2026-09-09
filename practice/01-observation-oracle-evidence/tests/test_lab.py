from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
PRACTICE = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PRACTICE))

import main as lab  # noqa: E402
from _minishop import MiniShopLab  # noqa: E402


class Practice11Tests(unittest.TestCase):
    def test_observe_has_no_verdict(self):
        buf = io.StringIO()
        with MiniShopLab() as shop, redirect_stdout(buf):
            result = lab.arm_observe(shop.base_url)
        text = buf.getvalue()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["item_count"], 3)
        self.assertNotIn("BUG-001", text)
        self.assertNotIn("不符合", text)

    def test_oracle_sends_no_request(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            result = lab.arm_oracle()
        text = buf.getvalue()
        self.assertFalse(result["request_sent"])
        self.assertIn("R-SEARCH", text)
        self.assertNotIn("HTTP ", text)

    def test_full_writes_evidence_and_flags_bug(self):
        buf = io.StringIO()
        with MiniShopLab() as shop, redirect_stdout(buf):
            observe = lab.arm_observe(shop.base_url)
            payload = lab.arm_full(shop.base_url, observe)
        self.assertTrue(payload["violates_r_search"])
        path = HERE / "validation" / "latest.json"
        self.assertTrue(path.is_file())
        saved = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(saved["bug"], "BUG-001")
        self.assertEqual(saved["observe"]["item_count"], 3)


if __name__ == "__main__":
    unittest.main()
