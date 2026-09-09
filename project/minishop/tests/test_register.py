import pytest
import requests

TIMEOUT = 5


def test_register_ok_then_login(base_url):
    phone = "13900001111"
    created = requests.post(
        f"{base_url}/api/register",
        json={"phone": phone, "password": "Test1234", "display_name": "New User"},
        timeout=TIMEOUT,
    )
    assert created.status_code == 201
    body = created.json()
    assert body["result"] == "ok"
    assert body["phone"] == phone
    assert "token" not in body
    login = requests.post(
        f"{base_url}/api/login",
        json={"phone": phone, "password": "Test1234"},
        timeout=TIMEOUT,
    )
    assert login.status_code == 200
    assert login.json()["token"]


def test_register_duplicate_phone(base_url):
    response = requests.post(
        f"{base_url}/api/register",
        json={"phone": "13800138000", "password": "Test1234"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 409
    assert response.json()["error"] == "phone taken"


@pytest.mark.parametrize(
    "phone",
    ["1380013800", "23800138000", "1380013800a", ""],
    ids=["ten_digits", "not_start_1", "non_digit", "empty"],
)
def test_register_invalid_phone(base_url, phone):
    response = requests.post(
        f"{base_url}/api/register",
        json={"phone": phone, "password": "Test1234"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 400
    assert response.json()["error"] == "invalid phone"


@pytest.mark.parametrize(
    "password",
    ["Test12", "abcdefgh", "12345678", "Test1234Test12345"],
    ids=["too_short", "letters_only", "digits_only", "too_long"],
)
def test_register_invalid_password(base_url, password):
    response = requests.post(
        f"{base_url}/api/register",
        json={"phone": "13900002222", "password": password},
        timeout=TIMEOUT,
    )
    assert response.status_code == 400
    assert response.json()["error"] == "invalid password"


def test_register_phone_number_type_rejected(base_url):
    response = requests.post(
        f"{base_url}/api/register",
        json={"phone": 13900003333, "password": "Test1234"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 400
