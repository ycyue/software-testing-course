#!/usr/bin/env python3
"""Practice 11-1: page error is not enough — grep the server log."""

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


def main() -> int:
    print("实操 11-1  页面报错之后，日志里有没有一行？")
    print("判定：qty=11 被拒时，应用日志应出现 inventory reject。这是页面上看不到的观察通道。\n")

    with MiniShopLab() as shop:
        status, _h, raw, parsed = request(
            "POST",
            f"{shop.base_url}/api/login",
            json_body={"phone": PHONE, "password": PASSWORD},
        )
        token = parsed["token"]
        cart_status, _ch, cart_raw, _cp = request(
            "POST",
            f"{shop.base_url}/api/cart/items",
            json_body={"sku": "SKU-DEMO-001", "qty": 11},
            headers={"Authorization": f"Bearer {token}"},
        )
        log_text = shop.log_path.read_text(encoding="utf-8")
        hits = [line for line in log_text.splitlines() if "inventory reject" in line]

    print(f"HTTP 观察：POST /api/cart/items qty=11 → {cart_status} {cart_raw}")
    print("日志观察：grep inventory reject")
    if hits:
        for line in hits:
            print(f"  {line}")
    else:
        print("  （没有命中）")

    ok = cart_status == 400 and len(hits) >= 1 and "qty=11" in hits[0]
    if ok:
        verdict = (
            "HTTP 400 和日志 inventory reject 对上了。"
            "只看页面「操作失败」你不知道服务端是否按库存规则拒绝。"
        )
        code = 0
    else:
        verdict = "日志未出现 inventory reject，或 HTTP 不是 400。"
        code = 2

    print(f"\n结论：{verdict}")
    payload = {
        "lab": "11-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "http_status": cart_status,
        "log_hits": hits,
        "verdict": verdict,
    }
    out = HERE / "validation"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "latest.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"证据：{path.relative_to(PRACTICE.parent)}")
    print("\n读完请回答：为什么 curl 失败之后还要 grep 日志，而不是只截一张页面？")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
