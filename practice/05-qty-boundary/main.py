#!/usr/bin/env python3
"""Practice 5-1: both sides of the stock cut. qty=10 allowed, qty=11 rejected."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PRACTICE = HERE.parent
sys.path.insert(0, str(PRACTICE))

from _http import request  # noqa: E402
from _minishop import MiniShopLab  # noqa: E402

PHONE = "13800138000"
PASSWORD = "Test1234"
SKU = "SKU-DEMO-001"


def login(base_url: str) -> str:
    status, _h, _raw, parsed = request(
        "POST",
        f"{base_url}/api/login",
        json_body={"phone": PHONE, "password": PASSWORD},
    )
    if status != 200 or not parsed or "token" not in parsed:
        raise SystemExit(f"登录失败 HTTP {status}: {_raw}")
    return parsed["token"]


def set_qty(base_url: str, token: str, qty: int):
    status, _h, raw, parsed = request(
        "POST",
        f"{base_url}/api/cart/items",
        json_body={"sku": SKU, "qty": qty},
        headers={"Authorization": f"Bearer {token}"},
    )
    return status, raw, parsed


def main() -> int:
    print("实操 5-1  边界值：尺子切在库存 10 上")
    print("判定：R-CART-10，SKU-DEMO-001 库存为 10 时，qty=10 允许，qty=11 拒绝。\n")

    with MiniShopLab() as shop:
        token = login(shop.base_url)
        left_status, left_raw, left_parsed = set_qty(shop.base_url, token, 10)
        right_status, right_raw, right_parsed = set_qty(shop.base_url, token, 11)

    print("=== 切点左侧 qty=10（有效边界）===")
    print(f"HTTP {left_status}  body={left_raw}")
    print("=== 切点右侧 qty=11（无效边界）===")
    print(f"HTTP {right_status}  body={right_raw}\n")

    left_ok = left_status == 200 and (left_parsed or {}).get("qty") == 10
    right_ok = right_status == 400
    if left_ok and right_ok:
        verdict = (
            "边界成立：等于库存通过，超过库存拒绝。"
            "只测 10 或只测 11，都不够说明切点在哪。"
        )
        code = 0
    else:
        verdict = "未复现 R-CART-10。对照 PRD 与 tests/test_api.py 的 qty 参数化。"
        code = 2

    print(f"结论：{verdict}")
    payload = {
        "lab": "5-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "oracle": "R-CART-10",
        "qty_10": {"status": left_status, "body": left_parsed},
        "qty_11": {"status": right_status, "body": right_parsed},
        "both_sides_required": True,
        "verdict": verdict,
    }
    out = HERE / "validation"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "latest.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"证据：{path.relative_to(PRACTICE.parent)}")
    print("\n读完请回答：为什么「测一个正常数量 2」不能代替边界值？")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
