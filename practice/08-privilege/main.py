#!/usr/bin/env python3
"""Practice 8-1: user A cannot read B's order; non-admin cannot open admin API."""

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

PASSWORD = "Test1234"


def login(base_url: str, phone: str) -> str:
    status, _h, raw, parsed = request(
        "POST",
        f"{base_url}/api/login",
        json_body={"phone": phone, "password": PASSWORD},
    )
    if status != 200 or not parsed or "token" not in parsed:
        raise SystemExit(f"登录失败 {phone} HTTP {status}: {raw}")
    return parsed["token"]


def auth(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def main() -> int:
    print("实操 8-1  权限：别人的订单和后台接口")
    print("判定：R-PERM 用户不得读写他人订单；非管理员不得访问 /api/admin/*。\n")

    with MiniShopLab() as shop:
        token_a = login(shop.base_url, "13800138000")
        token_b = login(shop.base_url, "13800138001")
        token_admin = login(shop.base_url, "13800138099")

        create_status, _h, create_raw, created = request(
            "POST",
            f"{shop.base_url}/api/orders",
            json_body={"sku": "SKU-DEMO-001", "qty": 1},
            headers=auth(token_a),
        )
        order_id = (created or {}).get("id") if create_status == 201 else None

        b_status, _bh, b_raw, _bp = request(
            "GET",
            f"{shop.base_url}/api/orders/{order_id}",
            headers=auth(token_b),
        )
        a_own, _ah, a_raw, _ap = request(
            "GET",
            f"{shop.base_url}/api/orders/{order_id}",
            headers=auth(token_a),
        )
        user_admin_status, _uh, user_admin_raw, _up = request(
            "GET",
            f"{shop.base_url}/api/admin/orders",
            headers=auth(token_a),
        )
        admin_status, _adh, admin_raw, _adp = request(
            "GET",
            f"{shop.base_url}/api/admin/orders",
            headers=auth(token_admin),
        )

    print(f"A 下单          HTTP {create_status}  id={order_id}")
    print(f"B 读 A 的订单    HTTP {b_status}  {b_raw}")
    print(f"A 读自己的订单  HTTP {a_own}")
    print(f"普通用户打后台  HTTP {user_admin_status}  {user_admin_raw}")
    print(f"管理员打后台    HTTP {admin_status}\n")

    ok = (
        create_status == 201
        and bool(order_id)
        and b_status == 403
        and a_own == 200
        and user_admin_status == 403
        and admin_status == 200
    )
    if ok:
        verdict = (
            "权限成立：自己的订单 200，别人的 403，普通用户进不了 /api/admin。"
            "页面藏掉按钮不算权限测试，要以服务器判定为准。"
        )
        code = 0
    else:
        verdict = "未复现 R-PERM。对照 PRD 与 /api/orders、/api/admin/orders。"
        code = 2

    print(f"结论：{verdict}")
    payload = {
        "lab": "8-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "oracle": "R-PERM",
        "create": {"status": create_status, "id": order_id},
        "b_reads_a": b_status,
        "a_reads_own": a_own,
        "user_admin": user_admin_status,
        "admin_admin": admin_status,
        "verdict": verdict,
    }
    out = HERE / "validation"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "latest.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"证据：{path.relative_to(PRACTICE.parent)}")
    print("\n读完请回答：为什么「后台入口在页面上看不见」不能代替这次 403？")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
