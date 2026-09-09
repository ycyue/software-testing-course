import pytest
import requests

TIMEOUT = 5


def test_login_ok(base_url):
    response = requests.post(
        f"{base_url}/api/login",
        json={"phone": "13800138000", "password": "Test1234"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    body = response.json()
    assert body["result"] == "ok"
    assert type(body["token"]) is str and body["token"] != ""
    assert "Set-Cookie" in response.headers
    assert "HttpOnly" in response.headers["Set-Cookie"]
    assert "status" not in body
    cookie_cart = requests.get(
        f"{base_url}/api/cart",
        headers={"Cookie": f"minishop_session={body['token']}"},
        timeout=TIMEOUT,
    )
    assert cookie_cart.status_code == 200


def test_login_wrong_password(base_url):
    response = requests.post(
        f"{base_url}/api/login",
        json={"phone": "13800138000", "password": "wrong-password"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 401


def test_products_list(base_url):
    response = requests.get(f"{base_url}/api/products", params={"keyword": "鼠标"}, timeout=TIMEOUT)
    assert response.status_code == 200
    items = response.json()["items"]
    assert type(items) is list
    assert [it["sku"] for it in items] == ["SKU-DEMO-001"]


def test_products_catalog_without_keyword(base_url):
    response = requests.get(f"{base_url}/api/products", timeout=TIMEOUT)
    assert response.status_code == 200
    items = response.json()["items"]
    assert [it["sku"] for it in items] == ["SKU-DEMO-001", "SKU-DEMO-002", "SKU-DEMO-003"]


def test_home_has_login_and_register_form(base_url):
    response = requests.get(f"{base_url}/", timeout=TIMEOUT)
    assert response.status_code == 200
    html = response.text
    assert 'id="login-form"' in html
    assert 'for="password"' in html
    assert 'type="password"' in html
    assert 'id="register-form"' in html
    js = requests.get(f"{base_url}/app.js", timeout=TIMEOUT).text
    assert "await refreshProducts();" in js
    assert "await refreshProducts(\"\");" not in js


def test_admin_page_ok(base_url):
    response = requests.get(f"{base_url}/admin.html", timeout=TIMEOUT)
    assert response.status_code == 200
    assert "只列出 id" in response.text


@pytest.mark.parametrize(
    "body, status",
    [
        ({"sku": "SKU-DEMO-001", "qty": 1}, 200),
        ({"sku": "SKU-DEMO-001", "qty": 10}, 200),
        ({"sku": "SKU-DEMO-001", "qty": 11}, 400),
        ({"sku": "SKU-DEMO-001"}, 400),
        ({"sku": "SKU-DEMO-001", "qty": None}, 400),
        ({"sku": "SKU-DEMO-001", "qty": ""}, 400),
        ({"sku": "SKU-DEMO-001", "qty": "1"}, 400),
        ({"sku": "SKU-DEMO-001", "qty": 0}, 400),
    ],
    ids=["ok", "eq_stock", "over_stock", "missing", "null", "empty_str", "wrong_type", "zero"],
)
def test_cart_qty_cases(base_url, token_a, body, status):
    response = requests.post(
        f"{base_url}/api/cart/items",
        json=body,
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=TIMEOUT,
    )
    assert response.status_code == status


def test_cart_qty_11_does_not_persist(base_url, token_a):
    before = requests.get(
        f"{base_url}/api/cart",
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=TIMEOUT,
    )
    assert before.status_code == 200
    before_qty = next(it["qty"] for it in before.json()["items"] if it["sku"] == "SKU-DEMO-001")
    rejected = requests.post(
        f"{base_url}/api/cart/items",
        json={"sku": "SKU-DEMO-001", "qty": 11},
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=TIMEOUT,
    )
    assert rejected.status_code == 400
    after = requests.get(
        f"{base_url}/api/cart",
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=TIMEOUT,
    )
    after_qty = next(it["qty"] for it in after.json()["items"] if it["sku"] == "SKU-DEMO-001")
    assert after_qty == before_qty
    assert after_qty != 11


def test_cart_unauthorized(base_url):
    response = requests.post(
        f"{base_url}/api/cart/items",
        json={"sku": "SKU-DEMO-001", "qty": 1},
        timeout=TIMEOUT,
    )
    assert response.status_code == 401


def test_create_order_returns_id(base_url, token_a):
    response = requests.post(
        f"{base_url}/api/orders",
        json={"sku": "SKU-DEMO-003", "qty": 1},
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 201
    body = response.json()
    assert "id" in body
    assert type(body["id"]) is str
    assert "status" not in body


def test_create_order_twice_not_idempotent(base_url, token_a):
    payload = {"sku": "SKU-DEMO-002", "qty": 1}
    headers = {"Authorization": f"Bearer {token_a}"}
    first = requests.post(f"{base_url}/api/orders", json=payload, headers=headers, timeout=TIMEOUT)
    second = requests.post(f"{base_url}/api/orders", json=payload, headers=headers, timeout=TIMEOUT)
    assert first.status_code == 201
    assert second.status_code == 201
    assert first.json()["id"] != second.json()["id"]
    assert "status" not in first.json()
    assert "status" not in second.json()


def test_create_order_unauthorized(base_url):
    response = requests.post(
        f"{base_url}/api/orders",
        json={"sku": "SKU-DEMO-001", "qty": 1},
        timeout=TIMEOUT,
    )
    assert response.status_code == 401


def test_order_forbidden_other_user(base_url, token_a, token_b, token_admin):
    created = requests.post(
        f"{base_url}/api/orders",
        json={"sku": "SKU-DEMO-003", "qty": 1},
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=TIMEOUT,
    )
    assert created.status_code == 201
    order_id = created.json()["id"]
    other = requests.get(
        f"{base_url}/api/orders/{order_id}",
        headers={"Authorization": f"Bearer {token_b}"},
        timeout=TIMEOUT,
    )
    assert other.status_code == 403
    assert "id" not in other.json() or other.json().get("id") != order_id
    admin = requests.get(
        f"{base_url}/api/orders/{order_id}",
        headers={"Authorization": f"Bearer {token_admin}"},
        timeout=TIMEOUT,
    )
    assert admin.status_code == 403


def test_admin_products_forbidden_to_user(base_url, token_a):
    products = requests.get(
        f"{base_url}/api/admin/products",
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=TIMEOUT,
    )
    orders = requests.get(
        f"{base_url}/api/admin/orders",
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=TIMEOUT,
    )
    assert products.status_code == 403
    assert orders.status_code == 403


def test_admin_products_ok(base_url, token_admin):
    products = requests.get(
        f"{base_url}/api/admin/products",
        headers={"Authorization": f"Bearer {token_admin}"},
        timeout=TIMEOUT,
    )
    assert products.status_code == 200
    assert type(products.json()["items"]) is list
    orders = requests.get(
        f"{base_url}/api/admin/orders",
        headers={"Authorization": f"Bearer {token_admin}"},
        timeout=TIMEOUT,
    )
    assert orders.status_code == 200
    items = orders.json()["items"]
    assert type(items) is list
    assert all(set(it.keys()) == {"id"} for it in items)


@pytest.mark.xfail(reason="BUG-001 empty keyword returns full catalog", strict=True)
def test_empty_keyword_should_not_return_all(base_url):
    response = requests.get(f"{base_url}/api/products", params={"keyword": "   "}, timeout=TIMEOUT)
    body = response.json()
    assert response.status_code == 400 or body.get("items") == []
