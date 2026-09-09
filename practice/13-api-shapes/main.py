#!/usr/bin/env python3
"""Practice 13-1: missing / null / empty string / wrong type are four different observations."""

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

CASES = [
    ("missing", {"sku": SKU}, 400, "missing qty"),
    ("null", {"sku": SKU, "qty": None}, 400, "null qty"),
    ("empty_str", {"sku": SKU, "qty": ""}, 400, "wrong type qty"),
    ("wrong_type", {"sku": SKU, "qty": "1"}, 400, "wrong type qty"),
]


def main() -> int:
    print("实操 13-1  缺字段、null、空字符串、错误类型不是同一类")
    print("判定：购物车 Body 这四种形状都应 400，且错误信息能区分缺失和类型。\n")

    rows = []
    with MiniShopLab() as shop:
        status, _h, raw, parsed = request(
            "POST",
            f"{shop.base_url}/api/login",
            json_body={"phone": PHONE, "password": PASSWORD},
        )
        token = parsed["token"]
        headers = {"Authorization": f"Bearer {token}"}
        for name, body, expect_status, expect_error in CASES:
            got_status, _ch, got_raw, got_parsed = request(
                "POST",
                f"{shop.base_url}/api/cart/items",
                json_body=body,
                headers=headers,
            )
            error = (got_parsed or {}).get("error") if isinstance(got_parsed, dict) else None
            ok = got_status == expect_status and error == expect_error
            print(f"{name:11} body={json.dumps(body, ensure_ascii=False)}")
            print(f"            HTTP {got_status} error={error}  预期 {expect_status}/{expect_error}  {'OK' if ok else 'FAIL'}")
            rows.append(
                {
                    "name": name,
                    "status": got_status,
                    "error": error,
                    "expect_status": expect_status,
                    "expect_error": expect_error,
                    "ok": ok,
                }
            )

    all_ok = all(r["ok"] for r in rows)
    if all_ok:
        verdict = (
            "四种形状都是 400，但 missing 和 null 的错误信息不同；"
            "空字符串和 \"1\" 在本实现里都走 wrong type。"
            "不要把它们写成「都是异常输入，测一条就行」。"
        )
        code = 0
    else:
        verdict = "有形状未按预期返回。对照 server.py 购物车校验。"
        code = 2

    print(f"\n结论：{verdict}")
    payload = {
        "lab": "13-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "rows": rows,
        "verdict": verdict,
    }
    out = HERE / "validation"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "latest.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"证据：{path.relative_to(PRACTICE.parent)}")
    print("\n读完请回答：为什么缺 qty 和 qty=null 要分成两条，而不是一条「异常」？")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
