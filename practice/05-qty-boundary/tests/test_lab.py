from __future__ import annotations

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import main as lab  # noqa: E402
from _minishop import MiniShopLab  # noqa: E402


class Practice51Tests(unittest.TestCase):
    def test_both_sides_of_cut(self):
        buf = io.StringIO()
        with MiniShopLab() as shop, redirect_stdout(buf):
            token = lab.login(shop.base_url)
            left_status, _a, left_parsed = lab.set_qty(shop.base_url, token, 10)
            right_status, _b, _right = lab.set_qty(shop.base_url, token, 11)
        self.assertEqual(left_status, 200)
        self.assertEqual((left_parsed or {}).get("qty"), 10)
        self.assertEqual(right_status, 400)

    def test_script_exit_zero(self):
        self.assertEqual(lab.main(), 0)


if __name__ == "__main__":
    unittest.main()
