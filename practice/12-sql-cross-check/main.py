#!/usr/bin/env python3
"""Practice 12-1: UI/API qty must match SQL. Cross-check, not UI-only."""

from __future__ import annotations

import json
import sqlite3
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
QTY = 2

JOIN_SQL = """
SELECT u.phone, p.sku, p.name, c.qty, p.stock
FROM cart_items c
JOIN users u ON u.id = c.user_id
JOIN products p ON p.id = c.product_id
WHERE u.phone = ? AND p.sku = ?
"""


def main() -> int:
    print("实操 12-1  页面说 2 件，库里是不是 2 件？")
    print("判定：API 写入的 qty 必须与 JOIN 查询一致。UI 对了库不对，仍是缺陷。\n")

    with MiniShopLab() as shop:
        status, _h, _raw, parsed = request(
            "POST",
            f"{shop.base_url}/api/login",
            json_body={"phone": PHONE, "password": PASSWORD},
        )
        token = parsed["token"]
        cart_status, _ch, cart_raw, cart_parsed = request(
            "POST",
            f"{shop.base_url}/api/cart/items",
            json_body={"sku": SKU, "qty": QTY},
            headers={"Authorization": f"Bearer {token}"},
        )
        conn = sqlite3.connect(str(shop.db_path))
        conn.row_factory = sqlite3.Row
        row = conn.execute(JOIN_SQL, (PHONE, SKU)).fetchone()
        conn.close()

    print("API 观察")
    print(f"  POST /api/cart/items HTTP {cart_status}  {cart_raw}")
    print("SQL 观察")
    print("  " + " ".join(JOIN_SQL.split()))
    if row:
        print(f"  phone={row['phone']} sku={row['sku']} qty={row['qty']} stock={row['stock']}")
    else:
        print("  JOIN 没有返回行")

    api_qty = (cart_parsed or {}).get("qty") if cart_status == 200 else None
    sql_qty = row["qty"] if row else None
    match = api_qty == sql_qty == QTY
    if match:
        verdict = (
            f"交叉验证通过：API 与 SQL 都是 qty={QTY}。"
            "如果只看页面数字，你发现不了「页面显示 2、库里仍是旧值」这类缺陷。"
        )
        code = 0
    else:
        verdict = f"不一致：API qty={api_qty} SQL qty={sql_qty}。这在真实项目里应开缺陷。"
        code = 2

    print(f"\n结论：{verdict}")
    payload = {
        "lab": "12-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "api_qty": api_qty,
        "sql_qty": sql_qty,
        "match": match,
        "verdict": verdict,
    }
    out = HERE / "validation"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "latest.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"证据：{path.relative_to(PRACTICE.parent)}")
    print("\n读完请回答：为什么 UPDATE 之前要先 SELECT？这次实操有没有改生产库？")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
