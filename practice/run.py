#!/usr/bin/env python3
"""Run a course practice drill by id.

Examples:
  python3 practice/run.py --list
  python3 practice/run.py 1-1
  python3 practice/run.py 5-1 --check
  python3 practice/run.py 1-1 -- --arm observe
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRACTICE = Path(__file__).resolve().parent

PRACTICE_DIRS = {
    "1-1": PRACTICE / "01-observation-oracle-evidence",
    "5-1": PRACTICE / "05-qty-boundary",
    "8-1": PRACTICE / "08-privilege",
    "9-1": PRACTICE / "09-http-observe",
    "11-1": PRACTICE / "11-log-grep",
    "12-1": PRACTICE / "12-sql-cross-check",
    "13-1": PRACTICE / "13-api-shapes",
    "15-1": PRACTICE / "15-json-check",
    "16-1": PRACTICE / "16-pytest-regression",
    "19-1": PRACTICE / "19-project-pack",
}

WRITTEN_DIRS = {
    "4-1": PRACTICE / "04-requirement-review",
    "6-1": PRACTICE / "06-bug-report",
}


def list_practice() -> None:
    print("可运行实操（✅）。书面实操见 practice/README.md。")
    print()
    rows = [
        ("1-1", "观察 / 判定 / 证据 对照", "第 1 章"),
        ("5-1", "qty=10 与 qty=11 成对看边界", "第 5 章"),
        ("8-1", "他人订单 403、非管理员进不了后台", "第 8 章"),
        ("9-1", "登录请求的方法、路径、头、体", "第 9 章"),
        ("11-1", "qty=11 之后 grep 日志", "第 11 章"),
        ("12-1", "购物车 API 与 SQL JOIN 交叉验证", "第 12 章"),
        ("13-1", "缺字段 / null / 空串 / 错误类型", "第 13 章"),
        ("15-1", "把商品列表当成 JSON 读", "第 15 章"),
        ("16-1", "pytest 37 passed / 1 xfailed", "第 16 章"),
        ("19-1", "项目包文件 + pytest 基线", "第 19 章"),
    ]
    for practice_id, title, chapter in rows:
        print(f"  {practice_id:5}  {title}  ({chapter})")
    print()
    print("书面：4-1 需求评审  6-1 缺陷报告")
    print("python3 practice/run.py 1-1")


def run_practice(practice_id: str, check: bool, extra: list[str]) -> int:
    written = WRITTEN_DIRS.get(practice_id)
    if written is not None:
        readme = written / "README.md"
        print(f"{practice_id} 是书面实操，没有一条命令能代替你写。")
        print(f"打开：{readme.relative_to(ROOT)}")
        return 0
    folder = PRACTICE_DIRS.get(practice_id)
    if folder is None:
        print(f"没有编号 {practice_id}。先 python3 practice/run.py --list")
        print("完整清单（含 📖/🚧）见 practice/README.md。")
        return 2
    if check:
        tests = folder / "tests"
        if not tests.is_dir():
            print(f"{folder} 没有 tests/，请直接做这次实操。")
            return 2
        cmd = [sys.executable, "-m", "unittest", "discover", "-s", str(tests), "-v"]
        print(" ".join(cmd), flush=True)
        return subprocess.call(cmd, cwd=str(folder))
    main = folder / "main.py"
    cmd = [sys.executable, str(main), *extra]
    print(" ".join(cmd), flush=True)
    return subprocess.call(cmd, cwd=str(folder))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run MiniShop course practice drills")
    parser.add_argument("practice_id", nargs="?", help="例如 1-1")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--check", action="store_true", help="跑该实操的 unittest")
    args, extra = parser.parse_known_args()
    if extra and extra[0] == "--":
        extra = extra[1:]
    if args.list or not args.practice_id:
        list_practice()
        return 0
    return run_practice(args.practice_id, args.check, extra)


if __name__ == "__main__":
    raise SystemExit(main())
