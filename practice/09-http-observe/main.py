#!/usr/bin/env python3
"""Practice 9-1: one HTTP exchange is four slots — method, path, headers, body."""

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
    print("实操 9-1  HTTP 观察的四格")
    print("一次登录不是「点按钮」，而是方法 + 路径 + 头 + 体。\n")

    path = "/api/login"
    body = {"phone": PHONE, "password": PASSWORD}
    with MiniShopLab() as shop:
        url = shop.base_url + path
        status, headers, raw, parsed = request("POST", url, json_body=body)

    cookie = headers.get("Set-Cookie") or headers.get("set-cookie")
    token = (parsed or {}).get("token") if isinstance(parsed, dict) else None

    print("请求")
    print(f"  方法：POST")
    print(f"  路径：{path}")
    print("  头  ：Content-Type: application/json")
    print(f"  体  ：phone={PHONE}  password=<teaching>")
    print("响应")
    print(f"  状态：{status}")
    print(f"  头  ：Set-Cookie {'有' if cookie else '无'}")
    print(f"  体  ：token {'有' if token else '无'}  keys={list((parsed or {}).keys()) if isinstance(parsed, dict) else None}")
    print()

    slots_ok = status == 200 and bool(token) and bool(cookie)
    if slots_ok:
        verdict = (
            "登录成功同时给了 JSON token 和 Set-Cookie。"
            "按 R-AUTH，后续接口以 Authorization: Bearer 为准；"
            "Cookie 与 Token 不是两种互相替代的登录产品。"
        )
        code = 0
    else:
        verdict = "登录响应缺少 token 或 Set-Cookie，对照 PRD R-AUTH。"
        code = 2

    print(f"结论：{verdict}")
    payload = {
        "lab": "9-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "request": {"method": "POST", "path": path, "header": "Content-Type", "body_keys": ["phone", "password"]},
        "response": {
            "status": status,
            "has_set_cookie": bool(cookie),
            "has_token": bool(token),
            "body_keys": list((parsed or {}).keys()) if isinstance(parsed, dict) else [],
        },
        "verdict": verdict,
    }
    out = HERE / "validation"
    out.mkdir(parents=True, exist_ok=True)
    path_out = out / "latest.json"
    path_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"证据：{path_out.relative_to(PRACTICE.parent)}")
    print("\n读完请回答：为什么不能说「GET 不安全、POST 安全」？这次请求里真正决定成败的是哪一格？")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
