"""Minimal JSON HTTP helper. Stdlib only."""

from __future__ import annotations

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def request(method: str, url: str, json_body=None, headers=None, timeout: int = 5):
    data = None
    hdrs = {"Accept": "application/json"}
    if json_body is not None:
        data = json.dumps(json_body).encode()
        hdrs["Content-Type"] = "application/json"
    if headers:
        hdrs.update(headers)
    req = Request(url, data=data, headers=hdrs, method=method)
    try:
        with urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode()
            parsed = json.loads(body) if body else None
            return resp.status, dict(resp.headers), body, parsed
    except HTTPError as exc:
        try:
            body = exc.read().decode()
            try:
                parsed = json.loads(body) if body else None
            except json.JSONDecodeError:
                parsed = None
            return exc.code, dict(exc.headers), body, parsed
        finally:
            exc.close()
    except URLError as exc:
        raise SystemExit(
            f"无法连接 {url}：{exc.reason}\n"
            "实操会自己启动 MiniShop。若你改过代码，先确认 project/minishop/server.py 仍能 import。"
        ) from exc
