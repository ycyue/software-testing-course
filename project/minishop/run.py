#!/usr/bin/env python3
"""MiniShop v1.0 one-click setup / serve / test / evidence.

Examples:
  python3 run.py              # same as serve
  python3 run.py setup        # create .venv and install requirements.txt
  python3 run.py serve        # start http://127.0.0.1:8765
  python3 run.py test         # pytest (uses .venv if present)
  python3 run.py evidence     # pytest + curl/SQL/log capture; screenshots if Playwright+Chrome exist
  python3 run.py all          # setup + evidence
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import time
import venv
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
VENV = ROOT / ".venv"
REQ = ROOT / "requirements.txt"
EVIDENCE = ROOT / "evidence"


def venv_python() -> Path:
    if os.name == "nt":
        return VENV / "Scripts" / "python.exe"
    return VENV / "bin" / "python"


def py() -> str:
    candidate = venv_python()
    if candidate.exists():
        return str(candidate)
    return sys.executable


def setup() -> None:
    if not VENV.exists():
        print("creating", VENV)
        venv.create(VENV, with_pip=True)
    cmd = [str(venv_python()), "-m", "pip", "install", "-r", str(REQ)]
    print(" ".join(cmd))
    subprocess.check_call(cmd)


def serve() -> None:
    os.chdir(ROOT)
    server = ROOT / "server.py"
    os.execv(sys.executable, [sys.executable, str(server)])


def run_pytest(extra: list[str] | None = None) -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    out = EVIDENCE / "pytest-output.txt"
    html = EVIDENCE / "pytest-report.html"
    cmd = [py(), "-m", "pytest", "-q"]
    if extra:
        cmd.extend(extra)
    print(" ".join(cmd))
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, env=env)
    text = (proc.stdout or "") + (proc.stderr or "")
    out.write_text(text, encoding="utf-8")
    print(text, end="" if text.endswith("\n") else "\n")
    # HTML report is optional; do not fail the course run if plugin missing.
    html_cmd = [py(), "-m", "pytest", "-q", f"--html={html}", "--self-contained-html"]
    html_proc = subprocess.run(html_cmd, cwd=ROOT, capture_output=True, text=True)
    if html_proc.returncode not in (0, 1) and "unrecognized arguments" in (html_proc.stderr or ""):
        print("pytest-html not installed; skipped HTML report (optional).")
    elif html.exists():
        print("wrote", html)
    return proc.returncode


def _http(method: str, url: str, body: dict | None = None, headers: dict | None = None):
    data = None
    hdrs = {"Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    if body is not None:
        data = json.dumps(body).encode()
        hdrs["Content-Type"] = "application/json"
    req = Request(url, data=data, headers=hdrs, method=method)
    try:
        with urlopen(req, timeout=5) as resp:
            raw = resp.read()
            return resp.status, dict(resp.headers), raw
    except HTTPError as err:
        raw = err.read()
        return err.code, dict(err.headers), raw


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def capture_http_sql_log(base: str) -> None:
    http_dir = EVIDENCE / "http"
    http_dir.mkdir(parents=True, exist_ok=True)

    def dump(name: str, method: str, path: str, body=None, headers=None) -> tuple[int, dict, bytes]:
        status, hdrs, raw = _http(method, base + path, body, headers)
        cookie = hdrs.get("Set-Cookie") or hdrs.get("set-cookie") or ""
        cookie_note = "Set-Cookie: present HttpOnly" if "HttpOnly" in cookie else (
            "Set-Cookie: present" if cookie else "Set-Cookie: absent"
        )
        preview = raw.decode("utf-8", errors="replace")
        if "token" in preview:
            try:
                obj = json.loads(preview)
                if isinstance(obj, dict) and obj.get("token"):
                    obj["token"] = "<redacted>"
                    preview = json.dumps(obj, ensure_ascii=False)
            except json.JSONDecodeError:
                pass
        text = (
            f"{method} {path}\n"
            f"HTTP {status}\n"
            f"{cookie_note}\n"
            f"Body:\n{preview}\n"
        )
        _write(http_dir / name, text)
        return status, hdrs, raw

    dump("02-login-bad.txt", "POST", "/api/login", {"phone": "13800138000", "password": "wrong-password"})
    status, hdrs, raw = dump(
        "01-login-ok.txt",
        "POST",
        "/api/login",
        {"phone": "13800138000", "password": "Test1234"},
    )
    token = json.loads(raw.decode()).get("token", "")
    auth = {"Authorization": f"Bearer {token}"}
    dump("03-products-empty-keyword.txt", "GET", "/api/products?keyword=%20%20%20")
    dump("04-cart-qty-10.txt", "POST", "/api/cart/items", {"sku": "SKU-DEMO-001", "qty": 10}, auth)
    dump("05-cart-qty-11.txt", "POST", "/api/cart/items", {"sku": "SKU-DEMO-001", "qty": 11}, auth)
    dump("06-order-create.txt", "POST", "/api/orders", {"sku": "SKU-DEMO-003", "qty": 1}, auth)
    dump("07-register-ok.txt", "POST", "/api/register", {
        "phone": "13900001111",
        "password": "Test1234",
        "display_name": "Evidence User",
    })
    dump("08-register-duplicate.txt", "POST", "/api/register", {
        "phone": "13800138000",
        "password": "Test1234",
    })
    dump("09-register-bad-phone.txt", "POST", "/api/register", {
        "phone": "1380013800",
        "password": "Test1234",
    })

    log_src = ROOT / "logs" / "app.log"
    log_dst = EVIDENCE / "logs" / "app-sample.log"
    if log_src.exists():
        sample = []
        for line in log_src.read_text(encoding="utf-8").splitlines():
            if "token=" in line.lower():
                continue
            sample.append(line)
        log_dst.parent.mkdir(parents=True, exist_ok=True)
        log_dst.write_text("\n".join(sample[-40:]) + ("\n" if sample else ""), encoding="utf-8")


def cart_join_snapshot(db: Path) -> tuple[list[str], object]:
    if not db.exists():
        return ["database missing"], None
    conn = sqlite3.connect(str(db))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT u.phone, p.sku, c.qty, p.stock
        FROM cart_items AS c
        INNER JOIN users AS u ON c.user_id = u.id
        INNER JOIN products AS p ON c.product_id = p.id
        WHERE u.phone = '13800138000'
        ORDER BY p.id
        """
    ).fetchall()
    over = conn.execute(
        """
        SELECT qty FROM cart_items c
        JOIN products p ON p.id = c.product_id
        JOIN users u ON u.id = c.user_id
        WHERE u.phone = '13800138000' AND p.sku = 'SKU-DEMO-001'
        """
    ).fetchone()
    conn.close()
    lines = ["phone\tsku\tqty\tstock"]
    for row in rows:
        lines.append(f"{row['phone']}\t{row['sku']}\t{row['qty']}\t{row['stock']}")
    qty = over["qty"] if over else None
    return lines, qty


def write_seed_join(seed_lines: list[str], after_lines: list[str], after_qty) -> None:
    text = (
        "# 种子（启动后、改购物车前）\n"
        + "\n".join(seed_lines)
        + "\n\n# qty=10 允许、qty=11 拒绝之后\n"
        + "\n".join(after_lines)
        + f"\n\nSKU-DEMO-001 qty after qty=11 reject: {after_qty} (must not be 11)\n"
    )
    _write(EVIDENCE / "sql" / "seed-join.txt", text)


def capture_screenshots(base: str) -> None:
    shot_dir = EVIDENCE / "screenshots"
    shot_dir.mkdir(parents=True, exist_ok=True)
    assets = ROOT.parents[1] / "chapters" / "assets"
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright not installed; skipped UI screenshots.")
        _write(shot_dir / "README.txt", "Playwright unavailable in this environment.\n")
        return

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(channel="chrome", headless=True)
        except Exception as err:
            print("chrome channel unavailable:", err)
            _write(shot_dir / "README.txt", f"Chrome channel unavailable: {err}\n")
            return
        page = browser.new_page(viewport={"width": 1280, "height": 900})

        def snap(name: str) -> None:
            target = shot_dir / name
            page.screenshot(path=str(target), full_page=True)
            if assets.exists() or True:
                assets.mkdir(parents=True, exist_ok=True)
                (assets / name).write_bytes(target.read_bytes())

        page.goto(base + "/", wait_until="networkidle")
        snap("01-login.png")
        page.fill("#phone", "13800138000")
        page.fill("#password", "wrong-password")
        page.click("#login-btn")
        page.wait_for_timeout(400)
        snap("02-login-fail.png")
        page.fill("#password", "Test1234")
        page.click("#login-btn")
        page.wait_for_selector("#shop-panel")
        snap("03-shop.png")
        page.fill("#keyword", "   ")
        page.click("#search-form button[type=submit]")
        page.wait_for_timeout(400)
        snap("04-search-empty-bug001.png")
        page.fill("#cart-qty", "11")
        page.click("#cart-form button[type=submit]")
        page.wait_for_timeout(400)
        snap("05-cart-qty-11.png")
        page.goto(base + "/", wait_until="networkidle")
        snap("06-register.png")
        page.fill("#phone", "13800138099")
        page.fill("#password", "Test1234")
        page.click("#login-btn")
        page.wait_for_selector("#shop-panel")
        page.goto(base + "/admin.html", wait_until="networkidle")
        page.wait_for_timeout(400)
        snap("07-admin.png")
        browser.close()
    print("wrote screenshots under", shot_dir)


def start_server_process() -> tuple[subprocess.Popen, str]:
    env = os.environ.copy()
    env["MINISHOP_RESET"] = "1"
    env["PYTHONUNBUFFERED"] = "1"
    proc = subprocess.Popen(
        [sys.executable, str(ROOT / "server.py")],
        cwd=ROOT,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    assert proc.stdout is not None
    base = None
    deadline = time.time() + 8
    lines = []
    while time.time() < deadline:
        line = proc.stdout.readline()
        if not line and proc.poll() is not None:
            break
        lines.append(line)
        if "MINISHOP_BASE_URL=" in line:
            base = line.strip().split("=", 1)[1]
            break
    if not base:
        proc.kill()
        raise RuntimeError("server did not print MINISHOP_BASE_URL: " + "".join(lines))
    return proc, base


def evidence() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    linux_dir = EVIDENCE / "linux"
    linux_dir.mkdir(parents=True, exist_ok=True)
    pwd = subprocess.check_output(["pwd"], cwd=ROOT, text=True)
    ls_env = os.environ.copy()
    ls_env["CLICOLOR"] = "0"
    ls = subprocess.check_output(["/bin/ls"], cwd=ROOT, text=True, env=ls_env)
    _write(linux_dir / "pwd-ls.txt", f"$ pwd\n{pwd}\n$ ls\n{ls}")
    df = subprocess.check_output(["df", "-h", "."], cwd=ROOT, text=True)
    _write(linux_dir / "df.txt", df)

    proc, base = start_server_process()
    try:
        db = ROOT / "data" / "minishop.sqlite"
        seed_lines, _seed_qty = cart_join_snapshot(db)
        capture_screenshots(base)
        capture_http_sql_log(base)
        after_lines, after_qty = cart_join_snapshot(db)
        write_seed_join(seed_lines, after_lines, after_qty)
        log_src = ROOT / "logs" / "app.log"
        if log_src.exists():
            grep = subprocess.check_output(
                ["grep", "-E", "login ok|inventory reject", str(log_src)],
                text=True,
            )
            _write(linux_dir / "grep-app-log.txt", grep)
        body_path = linux_dir / "login-body.json"
        curl_login = subprocess.check_output(
            [
                "curl", "-sS", "-D", "-", "-o", str(body_path),
                "-H", "Content-Type: application/json",
                "-d", '{"phone":"13800138000","password":"Test1234"}',
                f"{base}/api/login",
            ],
            text=True,
        )
        body_path.unlink(missing_ok=True)
        redacted = []
        for line in curl_login.splitlines():
            if line.lower().startswith("set-cookie:"):
                redacted.append("Set-Cookie: minishop_session=<redacted>; HttpOnly; Path=/")
            else:
                redacted.append(line)
        _write(linux_dir / "curl-login-headers.txt", "\n".join(redacted) + "\n")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
    return run_pytest()


def main() -> int:
    parser = argparse.ArgumentParser(description="MiniShop v1.0 one-click runner")
    parser.add_argument(
        "cmd",
        nargs="?",
        default="serve",
        choices=["setup", "serve", "test", "evidence", "all"],
    )
    args = parser.parse_args()
    if args.cmd == "setup":
        setup()
        return 0
    if args.cmd == "serve":
        serve()
        return 0
    if args.cmd == "test":
        return run_pytest()
    if args.cmd == "evidence":
        return evidence()
    if args.cmd == "all":
        setup()
        code = evidence()
        print("Next: python3 run.py serve")
        return code
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
