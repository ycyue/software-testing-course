#!/usr/bin/env python3
"""Practice 15-1: JSON is list-of-dict; read it as data, not as a screenshot."""

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


def main() -> int:
    print("实操 15-1  把商品列表当成数据读，不要当截图看")
    print("判定：响应是对象，items 是列表，每件有 sku/name/stock；库存 10 的鼠标能被脚本找出来。\n")

    out = HERE / "validation"
    out.mkdir(parents=True, exist_ok=True)
    json_path = out / "products.json"

    with MiniShopLab() as shop:
        status, _h, raw, parsed = request("GET", f"{shop.base_url}/api/products")

    json_path.write_text(raw + ("" if raw.endswith("\n") else "\n"), encoding="utf-8")
    loaded = json.loads(json_path.read_text(encoding="utf-8"))
    items = loaded.get("items") if isinstance(loaded, dict) else None

    print(f"HTTP {status}")
    print(f"顶层类型：{type(loaded).__name__}  keys={list(loaded) if isinstance(loaded, dict) else None}")
    print(f"items 类型：{type(items).__name__}  长度：{len(items) if isinstance(items, list) else None}")
    mouse = None
    if isinstance(items, list):
        for it in items:
            print(f"  sku={it.get('sku')} name={it.get('name')} stock={it.get('stock')}")
            if it.get("sku") == "SKU-DEMO-001":
                mouse = it

    ok = (
        status == 200
        and isinstance(loaded, dict)
        and isinstance(items, list)
        and len(items) == 3
        and mouse is not None
        and mouse.get("stock") == 10
    )
    if ok:
        verdict = (
            "JSON 已落盘再读回：三件商品，鼠标库存 10。"
            "测试用 Python 是为了处理观察结果，不是为了成为开发。"
        )
        code = 0
    else:
        verdict = "商品 JSON 形状或鼠标库存与教学数据不符。"
        code = 2

    print(f"\n结论：{verdict}")
    payload = {
        "lab": "15-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": status,
        "item_count": len(items) if isinstance(items, list) else None,
        "mouse_stock": mouse.get("stock") if mouse else None,
        "products_file": str(json_path.relative_to(PRACTICE.parent)),
        "verdict": verdict,
    }
    path = out / "latest.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"证据：{path.relative_to(PRACTICE.parent)}")
    print("第 15 章工作实战仍要你自己写 cart_cases.json；这次只练「读懂接口 JSON」。")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
