#!/usr/bin/env python3
"""Practice 19-1: the project pack is files you can point to, plus pytest baseline."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MINISHOP = ROOT / "project" / "minishop"


def _python() -> str:
    if os.name == "nt":
        candidate = MINISHOP / ".venv" / "Scripts" / "python.exe"
    else:
        candidate = MINISHOP / ".venv" / "bin" / "python"
    if candidate.exists():
        return str(candidate)
    return sys.executable


def main() -> int:
    print("实操 19-1  MiniShop 项目包：文件在不在、pytest 是不是 38/1")
    print("判定：能指着 PRD、BUG-001、OpenAPI，并且自动化基线仍是 38 passed / 1 xfailed。\n")

    checks = {
        "prd": (MINISHOP / "docs" / "PRD.md").is_file(),
        "bug001": (MINISHOP / "bugs" / "BUG-001.md").is_file(),
        "openapi": (MINISHOP / "docs" / "openapi.json").is_file(),
        "postman": (MINISHOP / "postman" / "MiniShop.postman_collection.json").is_file(),
    }
    prd = (MINISHOP / "docs" / "PRD.md").read_text(encoding="utf-8") if checks["prd"] else ""
    bug = (MINISHOP / "bugs" / "BUG-001.md").read_text(encoding="utf-8") if checks["bug001"] else ""
    checks["prd_has_r_search"] = "R-SEARCH" in prd and "R-CART-10" in prd
    checks["bug_still_open"] = "保持开放" in bug or "不在报告里写成已修复" in bug

    for key, ok in checks.items():
        print(f"  文件检查 {key}: {'OK' if ok else 'MISSING'}")

    py = _python()
    cmd = [py, "-m", "pytest", "-q"]
    print("运行：", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=str(MINISHOP), capture_output=True, text=True)
    text = (proc.stdout or "") + (proc.stderr or "")
    print(text, end="" if text.endswith("\n") else "\n")

    pytest_missing = "No module named pytest" in text
    if pytest_missing:
        print("还没有 pytest。先执行：cd project/minishop && python3 run.py setup")
        checks["passed_38"] = False
        checks["xfailed_1"] = False
        verdict = "还没有 pytest。先执行：cd project/minishop && python3 run.py setup"
        code = 2
    else:
        checks["passed_38"] = "38 passed" in text
        checks["xfailed_1"] = "1 xfailed" in text or "1 xfail" in text
        all_ok = all(checks.values())
        if all_ok:
            verdict = (
                "项目包齐全，pytest 仍是 38 passed / 1 xfailed。"
                "xfail 是 BUG-001 仍开放。不要把本项目写成公司电商，也不要写已测通支付。"
            )
            code = 0
        else:
            verdict = "项目包或缺文件，或 pytest 基线变了。对照 project/minishop/README.md。"
            code = 2

    print(f"结论：{verdict}")
    payload = {
        "lab": "19-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "pytest_missing": pytest_missing,
        "checks": checks,
        "verdict": verdict,
    }
    out = HERE / "validation"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "latest.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"证据：{path.relative_to(ROOT)}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
