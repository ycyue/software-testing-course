#!/usr/bin/env python3
"""Run a course practice drill by id.

Examples:
  python3 practice/run.py --list
  python3 practice/run.py 1-1
  python3 practice/run.py 5-1 --check
  python3 practice/run.py 1-1 -- --arm observe

Written ids such as 2-1 have no script. The command only prints where to open.
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

# Chapter-only drills: recognized so `run.py 2-1` is not "没有编号".
# kind: written (📖) or skeleton (🚧). None of these have main.py.
WRITTEN_CHAPTERS = {
    "2-1": (
        "written",
        "chapters/02-software-development-process.md",
        "2.8 MiniShop 工作实战",
        "在 MiniShop 上标出需求→提测→冒烟会落在哪",
        "第 2 章",
    ),
    "3-1": (
        "written",
        "chapters/03-software-testing-classification.md",
        "MiniShop 工作实战",
        "给登录、搜索、购物车贴分类坐标，不要互斥单选",
        "第 3 章",
    ),
    "7-1": (
        "written",
        "chapters/07-web-basics.md",
        "MiniShop 工作实战：建立页面观察记录",
        "打开页面，记录 URL 与 HTML",
        "第 7 章",
    ),
    "10-1": (
        "written",
        "chapters/10-chrome-devtools.md",
        "MiniShop 工作实战：DevTools 取证包",
        "DevTools 取证（仓库没有面板截图）",
        "第 10 章",
    ),
    "14-1": (
        "written",
        "chapters/14-postman.md",
        "MiniShop 工作实战：Postman 集合包",
        "导入 Postman 集合（作者未点 GUI Runner）",
        "第 14 章",
    ),
    "17-1": (
        "written",
        "chapters/17-automation-overview.md",
        "MiniShop 工作实战：自动化分层地图",
        "画 MiniShop 自动化分层，不写 Playwright 套件",
        "第 17 章",
    ),
    "18-1": (
        "skeleton",
        "chapters/18-performance-testing.md",
        "MiniShop 工作实战：性能问题清单",
        "有 .jmx 骨架和步骤，作者未安装、未跑 JMeter GUI",
        "第 18 章",
    ),
    "20-1": (
        "written",
        "chapters/20-interview.md",
        "MiniShop 工作实战：面试口述稿",
        "用项目证据写一页面试口述",
        "第 20 章",
    ),
    "21-1": (
        "written",
        "chapters/21-job-hunting.md",
        "MiniShop 工作实战：一页简历草稿",
        "一页诚实简历草稿",
        "第 21 章",
    ),
    "22-1": (
        "written",
        "chapters/22-learning-path.md",
        "MiniShop 工作实战：结课自检",
        "对照三梯队做结课自检",
        "第 22 章",
    ),
}


def list_practice() -> None:
    print("可运行实操（✅）。只有这些编号能 python3 practice/run.py <id> 跑起来。")
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
        ("16-1", "pytest 38 passed / 1 xfailed", "第 16 章"),
        ("19-1", "项目包文件 + pytest 基线", "第 19 章"),
    ]
    for practice_id, title, chapter in rows:
        print(f"  {practice_id:5}  {title}  ({chapter})")
    print()
    print("书面实操（📖）。没有脚本。python3 practice/run.py 2-1 不会启动程序。")
    print()
    print("  2-1    生命周期落点  （第 2 章）")
    print("  3-1    分类坐标      （第 3 章）")
    print("  7-1    页面观察记录  （第 7 章）")
    print("  4-1    需求评审      （第 4 章 · practice/04-requirement-review/）")
    print("  6-1    缺陷报告      （第 6 章 · practice/06-bug-report/）")
    print("  10-1   DevTools 取证 （第 10 章）")
    print("  14-1   Postman 集合  （第 14 章）")
    print("  17-1   自动化分层图  （第 17 章）")
    print("  20-1   面试口述      （第 20 章）")
    print("  21-1   简历草稿      （第 21 章）")
    print("  22-1   结课自检      （第 22 章）")
    print()
    print("骨架（🚧）：18-1 有 .jmx 步骤，作者未跑 JMeter GUI，同样没有脚本。")
    print("python3 practice/run.py 1-1")


def print_no_script(practice_id: str, kind: str, open_path: str, section: str) -> int:
    if kind == "skeleton":
        label = "骨架实操（🚧）"
    else:
        label = "书面实操（📖）"
    print(f"{practice_id} 是{label}，没有可运行脚本。")
    print(f"python3 practice/run.py {practice_id} 不会启动任何程序，也不能代替你写或点 GUI。")
    print(f"打开：{open_path}")
    print(f"小节：{section}")
    print("产出写入 exercises/。完整清单见 practice/README.md。")
    return 2


def run_practice(practice_id: str, check: bool, extra: list[str]) -> int:
    written = WRITTEN_DIRS.get(practice_id)
    if written is not None:
        readme = written / "README.md"
        print(f"{practice_id} 是书面实操（📖），没有可运行脚本，没有一条命令能代替你写。")
        print(f"python3 practice/run.py {practice_id} 不会启动任何程序。")
        print(f"打开：{readme.relative_to(ROOT)}")
        return 0
    chapter = WRITTEN_CHAPTERS.get(practice_id)
    if chapter is not None:
        kind, open_path, section, _title, _ch = chapter
        return print_no_script(practice_id, kind, open_path, section)
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
    parser.add_argument(
        "practice_id",
        nargs="?",
        help="例如 1-1（可运行）。2-1 等书面编号没有脚本，只会提示打开哪一章。",
    )
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
