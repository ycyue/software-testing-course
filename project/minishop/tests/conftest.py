import sys
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import server

TIMEOUT = 5
PASSWORD = "Test1234"


@pytest.fixture(scope="session")
def base_url(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("minishop")
    db = tmp / "minishop.sqlite"
    log = tmp / "app.log"
    server.reset_db(db)
    server.configure_logging(log)
    server.MiniShopHandler.db_path = db
    server.MiniShopHandler.log_path = log
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), server.MiniShopHandler)
    port = httpd.server_address[1]
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{port}"
    httpd.shutdown()


@pytest.fixture(autouse=True)
def reset_seed_db(base_url):
    server.reset_db(server.MiniShopHandler.db_path)


@pytest.fixture
def token_a(base_url):
    response = requests.post(
        f"{base_url}/api/login",
        json={"phone": "13800138000", "password": PASSWORD},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture
def token_b(base_url):
    response = requests.post(
        f"{base_url}/api/login",
        json={"phone": "13800138001", "password": PASSWORD},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture
def token_admin(base_url):
    response = requests.post(
        f"{base_url}/api/login",
        json={"phone": "13800138099", "password": PASSWORD},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    return response.json()["token"]
