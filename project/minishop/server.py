#!/usr/bin/env python3
"""MiniShop v1.0 local teaching app. Personal software-testing practice project."""

from __future__ import annotations

import hashlib
import json
import logging
import os
import sqlite3
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent
DEFAULT_DB = ROOT / "data" / "minishop.sqlite"
DEFAULT_LOG = ROOT / "logs" / "app.log"
SALT = "minishop-lab-v1"
STATIC = ROOT / "frontend"

STOCK_MOUSE = 10


def hash_password(password: str) -> str:
    return hashlib.sha256(f"{SALT}|{password}".encode()).hexdigest()


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        PRAGMA foreign_keys = ON;
        CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY,
          phone TEXT NOT NULL UNIQUE,
          password_hash TEXT NOT NULL,
          display_name TEXT,
          role TEXT NOT NULL DEFAULT 'user'
        );
        CREATE TABLE IF NOT EXISTS products (
          id INTEGER PRIMARY KEY,
          sku TEXT NOT NULL UNIQUE,
          name TEXT NOT NULL,
          stock INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS cart_items (
          id INTEGER PRIMARY KEY,
          user_id INTEGER NOT NULL,
          product_id INTEGER NOT NULL,
          qty INTEGER NOT NULL,
          UNIQUE(user_id, product_id),
          FOREIGN KEY (user_id) REFERENCES users(id),
          FOREIGN KEY (product_id) REFERENCES products(id)
        );
        CREATE TABLE IF NOT EXISTS orders (
          id TEXT PRIMARY KEY,
          user_id INTEGER NOT NULL,
          created_at TEXT NOT NULL,
          FOREIGN KEY (user_id) REFERENCES users(id)
        );
        CREATE TABLE IF NOT EXISTS order_items (
          id INTEGER PRIMARY KEY,
          order_id TEXT NOT NULL,
          sku TEXT NOT NULL,
          qty INTEGER NOT NULL,
          FOREIGN KEY (order_id) REFERENCES orders(id)
        );
        CREATE TABLE IF NOT EXISTS sessions (
          token TEXT PRIMARY KEY,
          user_id INTEGER NOT NULL,
          created_at TEXT NOT NULL,
          FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """
    )
    conn.commit()


def seed(conn: sqlite3.Connection) -> None:
    pw = hash_password("Test1234")
    users = [
        (1, "13800138000", pw, "Tester A", "user"),
        (2, "13800138001", pw, "Tester B", "user"),
        (3, "13800138099", pw, "Admin", "admin"),
    ]
    conn.executemany(
        "INSERT OR REPLACE INTO users(id, phone, password_hash, display_name, role) VALUES (?,?,?,?,?)",
        users,
    )
    products = [
        (1, "SKU-DEMO-001", "无线鼠标", STOCK_MOUSE),
        (2, "SKU-DEMO-002", "键盘", 5),
        (3, "SKU-DEMO-003", "耳机", 3),
    ]
    conn.executemany(
        "INSERT OR REPLACE INTO products(id, sku, name, stock) VALUES (?,?,?,?)",
        products,
    )
    conn.execute("DELETE FROM cart_items")
    conn.execute(
        "INSERT INTO cart_items(user_id, product_id, qty) VALUES (1, 1, 1), (1, 2, 2), (2, 1, 1)"
    )
    conn.commit()


def reset_db(db_path: Path) -> None:
    if db_path.exists():
        db_path.unlink()
    conn = connect(db_path)
    init_schema(conn)
    seed(conn)
    conn.close()


def valid_phone(phone: str) -> bool:
    return isinstance(phone, str) and len(phone) == 11 and phone.isdigit() and phone.startswith("1")


def valid_password(password: str) -> bool:
    if type(password) is not str or not (8 <= len(password) <= 16):
        return False
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_letter and has_digit


class MiniShopHandler(BaseHTTPRequestHandler):
    db_path = DEFAULT_DB
    log_path = DEFAULT_LOG

    def log_message(self, format, *args):
        return

    def _app_log(self, message: str) -> None:
        logging.getLogger("minishop").info(message)

    def _json(self, code: int, obj, extra_headers=None) -> None:
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Connection", "close")
        if extra_headers:
            for key, value in extra_headers:
                self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)

    def _bytes(self, code: int, payload: bytes, content_type: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(payload)

    def _read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b""
        if not raw:
            return {}
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return None
        if type(data) is not dict:
            return None
        return data

    def _conn(self) -> sqlite3.Connection:
        return connect(Path(self.db_path))

    def _token(self):
        auth = self.headers.get("Authorization", "")
        if auth.startswith("Bearer "):
            return auth[7:].strip() or None
        cookie = self.headers.get("Cookie", "")
        for part in cookie.split(";"):
            part = part.strip()
            if part.startswith("minishop_session="):
                return part.split("=", 1)[1] or None
        return None

    def _user(self, conn):
        token = self._token()
        if not token:
            return None
        row = conn.execute(
            "SELECT u.* FROM sessions s JOIN users u ON u.id = s.user_id WHERE s.token = ?",
            (token,),
        ).fetchone()
        return row

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path in ("/", "/index.html"):
            self._bytes(200, (STATIC / "index.html").read_bytes(), "text/html; charset=utf-8")
            return
        if path == "/admin.html":
            self._bytes(200, (STATIC / "admin.html").read_bytes(), "text/html; charset=utf-8")
            return
        if path == "/app.js":
            self._bytes(200, (STATIC / "app.js").read_bytes(), "application/javascript; charset=utf-8")
            return
        if path == "/styles.css":
            self._bytes(200, (STATIC / "styles.css").read_bytes(), "text/css; charset=utf-8")
            return
        if path == "/api/products":
            self._get_products(parse_qs(parsed.query))
            return
        if path == "/api/cart":
            self._get_cart()
            return
        if path.startswith("/api/orders/") and path != "/api/orders/":
            self._get_order(path.rsplit("/", 1)[-1])
            return
        if path == "/api/admin/products":
            self._admin_products()
            return
        if path == "/api/admin/orders":
            self._admin_orders()
            return
        if path.startswith("/api/"):
            self._json(404, {"error": "not found"})
            return
        self._json(404, {"error": "not found"})

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/login":
            self._login()
            return
        if path == "/api/register":
            self._register()
            return
        if path == "/api/cart/items":
            self._cart_items()
            return
        if path == "/api/orders":
            self._create_order()
            return
        self._json(404, {"error": "not found"})

    def _get_products(self, qs):
        keyword = qs.get("keyword", [None])[0]
        conn = self._conn()
        rows = conn.execute("SELECT sku, name, stock FROM products ORDER BY id").fetchall()
        conn.close()
        items = [{"sku": r["sku"], "name": r["name"], "stock": r["stock"]} for r in rows]
        # BUG-001: empty / whitespace keyword still returns the full list.
        if keyword is not None and keyword.strip() != "":
            key = keyword.lower()
            items = [it for it in items if key in it["name"].lower() or key in it["sku"].lower()]
        self._json(200, {"items": items})

    def _login(self):
        data = self._read_json()
        if data is None:
            self._json(400, {"error": "invalid json"})
            return
        phone = data.get("phone")
        password = data.get("password")
        if "phone" not in data or "password" not in data:
            self._json(400, {"error": "missing field"})
            return
        conn = self._conn()
        row = conn.execute("SELECT * FROM users WHERE phone = ?", (phone,)).fetchone()
        if row is None or row["password_hash"] != hash_password(str(password) if password is not None else ""):
            self._app_log(f"login fail phone={phone}")
            conn.close()
            self._json(401, {"result": "fail"})
            return
        token = uuid.uuid4().hex
        conn.execute(
            "INSERT INTO sessions(token, user_id, created_at) VALUES (?,?,?)",
            (token, row["id"], time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())),
        )
        conn.commit()
        conn.close()
        self._app_log(f"login ok user={row['phone']}")
        cookie = f"minishop_session={token}; HttpOnly; Path=/"
        self._json(
            200,
            {"result": "ok", "token": token, "role": row["role"]},
            [("Set-Cookie", cookie)],
        )

    def _register(self):
        data = self._read_json()
        if data is None:
            self._json(400, {"error": "invalid json"})
            return
        phone = data.get("phone")
        password = data.get("password")
        name = data.get("display_name")
        if not valid_phone(phone if type(phone) is str else ""):
            self._json(400, {"error": "invalid phone"})
            return
        if not valid_password(password if type(password) is str else ""):
            self._json(400, {"error": "invalid password"})
            return
        conn = self._conn()
        exists = conn.execute("SELECT id FROM users WHERE phone = ?", (phone,)).fetchone()
        if exists:
            conn.close()
            self._json(409, {"error": "phone taken"})
            return
        conn.execute(
            "INSERT INTO users(phone, password_hash, display_name, role) VALUES (?,?,?,?)",
            (phone, hash_password(password), name, "user"),
        )
        conn.commit()
        conn.close()
        self._json(201, {"result": "ok", "phone": phone})

    def _get_cart(self):
        conn = self._conn()
        user = self._user(conn)
        if user is None:
            conn.close()
            self._json(401, {"error": "unauthorized"})
            return
        rows = conn.execute(
            """
            SELECT p.sku, p.name, c.qty, p.stock
            FROM cart_items c
            JOIN products p ON p.id = c.product_id
            WHERE c.user_id = ?
            ORDER BY c.id
            """,
            (user["id"],),
        ).fetchall()
        conn.close()
        items = [{"sku": r["sku"], "name": r["name"], "qty": r["qty"], "stock": r["stock"]} for r in rows]
        self._json(200, {"items": items})

    def _cart_items(self):
        data = self._read_json()
        if data is None:
            self._json(400, {"error": "invalid json"})
            return
        conn = self._conn()
        user = self._user(conn)
        if user is None:
            conn.close()
            self._json(401, {"error": "unauthorized"})
            return
        if "sku" not in data:
            conn.close()
            self._json(400, {"error": "missing sku"})
            return
        if "qty" not in data:
            conn.close()
            self._json(400, {"error": "missing qty"})
            return
        sku = data.get("sku")
        qty = data.get("qty")
        if qty is None:
            conn.close()
            self._json(400, {"error": "null qty"})
            return
        if type(qty) is not int:
            conn.close()
            self._json(400, {"error": "wrong type qty"})
            return
        product = conn.execute("SELECT * FROM products WHERE sku = ?", (sku,)).fetchone()
        if product is None:
            conn.close()
            self._json(404, {"error": "unknown sku"})
            return
        if qty < 1:
            conn.close()
            self._json(400, {"error": "qty not positive"})
            return
        if qty > product["stock"]:
            self._app_log(
                f"inventory reject sku={sku} stock={product['stock']} qty={qty}"
            )
            conn.close()
            self._json(400, {"error": "qty exceeds stock"})
            return
        existing = conn.execute(
            "SELECT id FROM cart_items WHERE user_id = ? AND product_id = ?",
            (user["id"], product["id"]),
        ).fetchone()
        if existing:
            conn.execute("UPDATE cart_items SET qty = ? WHERE id = ?", (qty, existing["id"]))
        else:
            conn.execute(
                "INSERT INTO cart_items(user_id, product_id, qty) VALUES (?,?,?)",
                (user["id"], product["id"], qty),
            )
        conn.commit()
        conn.close()
        self._json(200, {"sku": sku, "qty": qty})

    def _create_order(self):
        data = self._read_json()
        if data is None:
            self._json(400, {"error": "invalid json"})
            return
        conn = self._conn()
        user = self._user(conn)
        if user is None:
            conn.close()
            self._json(401, {"error": "unauthorized"})
            return
        if "sku" not in data or "qty" not in data:
            conn.close()
            self._json(400, {"error": "missing field"})
            return
        sku = data.get("sku")
        qty = data.get("qty")
        if type(qty) is not int:
            conn.close()
            self._json(400, {"error": "wrong type qty"})
            return
        product = conn.execute("SELECT * FROM products WHERE sku = ?", (sku,)).fetchone()
        if product is None:
            conn.close()
            self._json(404, {"error": "unknown sku"})
            return
        if qty < 1:
            conn.close()
            self._json(400, {"error": "qty not positive"})
            return
        if qty > product["stock"]:
            self._app_log(f"inventory reject sku={sku} stock={product['stock']} qty={qty}")
            conn.close()
            self._json(400, {"error": "qty exceeds stock"})
            return
        order_id = f"ord-{uuid.uuid4().hex[:12]}"
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        try:
            conn.execute("BEGIN")
            updated = conn.execute(
                "UPDATE products SET stock = stock - ? WHERE sku = ? AND stock >= ?",
                (qty, sku, qty),
            )
            if updated.rowcount != 1:
                conn.execute("ROLLBACK")
                conn.close()
                self._json(409, {"error": "stock changed"})
                return
            conn.execute(
                "INSERT INTO orders(id, user_id, created_at) VALUES (?,?,?)",
                (order_id, user["id"], now),
            )
            conn.execute(
                "INSERT INTO order_items(order_id, sku, qty) VALUES (?,?,?)",
                (order_id, sku, qty),
            )
            conn.commit()
        except sqlite3.Error:
            conn.execute("ROLLBACK")
            conn.close()
            self._json(500, {"error": "db"})
            return
        conn.close()
        self._json(201, {"id": order_id})

    def _get_order(self, order_id: str):
        conn = self._conn()
        user = self._user(conn)
        if user is None:
            conn.close()
            self._json(401, {"error": "unauthorized"})
            return
        row = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
        if row is None:
            conn.close()
            self._json(404, {"error": "not found"})
            return
        if row["user_id"] != user["id"]:
            conn.close()
            self._json(403, {"error": "forbidden"})
            return
        items = conn.execute(
            "SELECT sku, qty FROM order_items WHERE order_id = ?",
            (order_id,),
        ).fetchall()
        conn.close()
        body = {"id": row["id"], "items": [{"sku": i["sku"], "qty": i["qty"]} for i in items]}
        self._json(200, body)

    def _admin_products(self):
        conn = self._conn()
        user = self._user(conn)
        if user is None:
            conn.close()
            self._json(401, {"error": "unauthorized"})
            return
        if user["role"] != "admin":
            conn.close()
            self._json(403, {"error": "forbidden"})
            return
        rows = conn.execute("SELECT sku, name, stock FROM products ORDER BY id").fetchall()
        conn.close()
        self._json(200, {"items": [dict(r) for r in rows]})

    def _admin_orders(self):
        conn = self._conn()
        user = self._user(conn)
        if user is None:
            conn.close()
            self._json(401, {"error": "unauthorized"})
            return
        if user["role"] != "admin":
            conn.close()
            self._json(403, {"error": "forbidden"})
            return
        rows = conn.execute("SELECT id, user_id, created_at FROM orders ORDER BY created_at").fetchall()
        conn.close()
        self._json(200, {"items": [{"id": r["id"]} for r in rows]})


def configure_logging(log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("minishop")
    logger.handlers.clear()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_path, encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s INFO  %(message)s"))
    logger.addHandler(handler)


def serve(host="127.0.0.1", port=8765, db_path=None, log_path=None):
    db = Path(db_path or os.environ.get("MINISHOP_DB") or DEFAULT_DB)
    log = Path(log_path or os.environ.get("MINISHOP_LOG") or DEFAULT_LOG)
    if os.environ.get("MINISHOP_RESET", "1") == "1" or not db.exists():
        reset_db(db)
    else:
        conn = connect(db)
        init_schema(conn)
        conn.close()
    configure_logging(log)
    MiniShopHandler.db_path = db
    MiniShopHandler.log_path = log
    httpd = ThreadingHTTPServer((host, int(os.environ.get("MINISHOP_PORT", port))), MiniShopHandler)
    bound = httpd.server_address[1]
    print(f"MINISHOP_BASE_URL=http://{host}:{bound}", flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    serve()
