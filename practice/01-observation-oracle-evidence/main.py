#!/usr/bin/env python3
"""Practice 1-1: Testing = Observation + Oracle + Evidence.

You do not need to read this file line by line. Run it, then answer:
which arm is actually testing?
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
PRACTICE = HERE.parent
sys.path.insert(0, str(PRACTICE))

from _http import request  # noqa: E402
from _minishop import MiniShopLab  # noqa: E402

ORACLE = (
    "R-SEARCH：关键字为空或仅空白时，不应把全量商品当成搜索结果"
    "（当前实现不符合，见 BUG-001）。"
)
def arm_observe(base_url: str) -> dict:
    url = f"{base_url}/api/products?keyword={quote('   ')}"
    status, _headers, raw, parsed = request("GET", url)
    items = (parsed or {}).get("items") if isinstance(parsed, dict) else None
    count = len(items) if isinstance(items, list) else None
    print("=== 臂 A：只有观察（不读需求）===")
    print(f"GET {url}")
    print(f"HTTP {status}")
    print(f"items 数量：{count}")
    print("你现在只知道「系统返回了这些商品」。这算通过还是失败？")
    print("没有判定标准，你说不准。\n")
    return {"status": status, "item_count": count, "body": raw}


def arm_oracle() -> dict:
    print("=== 臂 B：只有判定（不发请求）===")
    print(ORACLE)
    print("出处：project/minishop/docs/PRD.md")
    print("你现在只知道「需求怎么写」。实现有没有违反？不跑系统，你说不准。\n")
    return {"oracle": ORACLE, "request_sent": False}


def arm_full(base_url: str, observe: dict) -> dict:
    count = observe["item_count"]
    violates = observe["status"] == 200 and count == 3
    print("=== 臂 C：观察 + 判定 + 证据 ===")
    print(f"判定：{ORACLE}")
    print(f"观察：HTTP {observe['status']}，{count} 件商品")
    if violates:
        verdict = (
            "不符合 R-SEARCH：空/空白关键字返回了全量 3 件商品。"
            "这就是仓库里的 BUG-001。v1.0 保持开放，不要写成已修复。"
        )
    else:
        verdict = (
            "本次运行没有复现「空白关键字返回 3 件」。"
            "不要把一次未复现写成缺陷已修复；对照 bugs/BUG-001.md。"
        )
    print(f"结论：{verdict}")
    payload = {
        "lab": "1-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "oracle": ORACLE,
        "observe": {"status": observe["status"], "item_count": count},
        "violates_r_search": violates,
        "verdict": verdict,
        "bug": "BUG-001" if violates else None,
    }
    out_dir = HERE / "validation"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "latest.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"证据已写入：{path.relative_to(PRACTICE.parent)}\n")
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Practice 1-1 observation / oracle / evidence")
    parser.add_argument(
        "--arm",
        choices=("observe", "oracle", "full", "all"),
        default="all",
        help="which arm to run (default: all three)",
    )
    args = parser.parse_args(argv)

    print("实操 1-1  测试 = 观察 + 判定 + 证据")
    print("会在临时目录启动 MiniShop，不改 project/minishop/data/，也不占用 8765。\n")

    if args.arm == "oracle":
        arm_oracle()
        return 0

    with MiniShopLab() as shop:
        observe = arm_observe(shop.base_url)
        if args.arm == "observe":
            return 0
        arm_oracle()
        result = arm_full(shop.base_url, observe)

    print("读完三段输出，用自己的话回答：")
    print("  去掉观察、去掉判定、去掉证据，分别还叫不叫测试？为什么？")
    return 0 if result.get("violates_r_search") else 2


if __name__ == "__main__":
    raise SystemExit(main())
