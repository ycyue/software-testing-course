#!/usr/bin/env python3
"""Practice 16-1: pytest is automated evidence. 37 passed / 1 xfailed is BUG-001 still open."""

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
    print("实操 16-1  pytest 绿条是证据，xfail 不是失败也不是已修复")
    print("判定：仓库自动化应保持 37 passed, 1 xfailed（BUG-001）。\n")

    py = _python()
    cmd = [py, "-m", "pytest", "-q"]
    print("运行：", " ".join(cmd))
    print("目录：", MINISHOP)
    proc = subprocess.run(cmd, cwd=str(MINISHOP), capture_output=True, text=True)
    text = (proc.stdout or "") + (proc.stderr or "")
    print(text, end="" if text.endswith("\n") else "\n")

    if "No module named pytest" in text or proc.returncode == 2 and "pytest" in text.lower():
        print("还没有 pytest。先执行：")
        print("  cd project/minishop && python3 run.py setup")
        return 2

    passed = "37 passed" in text
    xfailed = "1 xfailed" in text or "1 xfail" in text
    if passed and xfailed:
        verdict = (
            "37 passed, 1 xfailed。"
            "xfail 对应 BUG-001：空搜索仍返回全量，PRD 要求不应如此。"
            "不要把 xfail 说成「测试挂了」，也不要说成「已经修了」。"
        )
        code = 0
    else:
        verdict = "输出与基线 37 passed / 1 xfailed 不一致。对照 evidence/pytest-output.txt。"
        code = 2

    print(f"结论：{verdict}")
    payload = {
        "lab": "16-1",
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "returncode": proc.returncode,
        "passed_37": passed,
        "xfailed_1": xfailed,
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
