# VERIFY MiniShop

- 验证员：Verification-Agent-07 MiniShop
- 日期：2026-09-10
- 范围：修复后五项（PRD R-ORDER 下单不读购物车；所属者 GET 测试；Postman `disableCookies`；BUG-001 仍开放；38 passed / 1 xfailed）
- 对照：`GLOBAL_06_MINISHOP.md`、`FIX_PLAN.md`（G06-0004 / M-P1-32 / M-P1-18）、`fix-records/FIX_G06-0004.md`、`FIX_M-P1-32.md`、`FIX_M-P1-18.md`
- 禁止：未改教材、未改项目；未跑 `python3 run.py test` / `run.py evidence`（会覆盖仓库证据）

验收结论：**VERIFIED**。五项现场成立。残留项见 §5，均不在本轮五项内，不挡签章。

---

## 1. 五项清单

| # | 检查项 | Audit ID | 结论 | 现场证据 |
| --- | --- | --- | --- | --- |
| 1 | PRD R-ORDER 下单不读购物车 | G06-0004 | **PASS** | PRD 已冻结；`_create_order` 不碰 `cart_items`；探针下单后购物车 qty 不变 |
| 2 | 所属者 GET 测试存在 | M-P1-32 / G06-0001 | **PASS** | `test_owner_can_read_own_order` 收集并 Passed；TC-PERM-002 在用例/矩阵 |
| 3 | Postman `disableCookies` | M-P1-18 | **PASS** | 「无凭证创建」`protocolProfileBehavior.disableCookies=true`，无 Authorization；集合仍 15 条 |
| 4 | BUG-001 仍开放 | 冻结口径 | **PASS** | 缺陷单「保持开放」；空白 keyword 仍 200/三件；xfail `strict=True` 仍 XFAIL |
| 5 | 38 passed, 1 xfailed | M-P1-32 基线 | **PASS** | 本机收集 39；`.venv` pytest **38 passed, 1 xfailed**；仓库 `evidence/pytest-output.txt` / `pytest-report.html` 同数字 |

---

## 2. 逐项取证

### 2.1 G06-0004 — R-ORDER 下单不读购物车

**文档**

`project/minishop/docs/PRD.md` R-ORDER：

> `POST /api/orders` 成功返回 201 与 `id`，Body **不含** `status`。默认不幂等：两次成功 POST 得到两个 id。v1.0 下单直接 POST sku+qty，不读取、不修改购物车

覆盖矩阵同句：「直接 POST sku+qty，不读购物车」。第 19 章 19.2 已复述「不读取购物车」。实现未改，符合 FIX RECORD「不必改 server」。

**实现**

`server.py` `_create_order`（约 L415–478）：只 `SELECT`/`UPDATE products`、`INSERT orders` / `order_items`。全文件 `cart_items` 出现在建表、种子、GET 购物车、POST 改数量；**不在** `_create_order`。

**本机探针**（隔离 sqlite，端口 `63808`，未写仓库）：

1. Tester A 把 `SKU-DEMO-001` 购物车改为 qty=10；
2. `POST /api/orders` `{"sku":"SKU-DEMO-003","qty":1}` → **201** `{"id":"ord-f3e06af0f9ea"}`，无 `status`；
3. 再 `GET /api/cart`：鼠标仍 qty=10、键盘仍 qty=2（与下单前相同）；
4. SQL：`cart_items` 仍 `(1,1,10),(1,2,2),(2,1,1)`；`SKU-DEMO-003.stock` 3→2（只扣库存）；`orders` 列仍为 `id, user_id, created_at`，无 `status`。

结论：契约已写明教学简化；行为与契约一致。没有「购物车结算」。

缺口（不挡本项）：没有单独 pytest 断言「下单后 cart_items 不变」。G06-0004 的修复方式是写进 PRD，不是补测。OpenAPI `POST /api/orders` summary 仍是 “Create order; not idempotent; body has id only”，未写不读车——属原 G06-0007 薄文档，本轮未修。

### 2.2 M-P1-32 — 所属者 GET 测试存在

`tests/test_api.py::test_owner_can_read_own_order`（L188–207）：A 下单 → A `GET /api/orders/{id}` → **200**；`id` 匹配；`items == [{"sku":"SKU-DEMO-003","qty":1}]`；`"status" not in body`。

配套文档：

- `docs/test-cases.md` TC-PERM-002「所属者读自己的订单 | 200，body 有 id 与 items，无 status | 通过 | pytest」
- `docs/test-points.md` TP-PERM-OWNER
- `docs/prd-coverage-matrix.md` R-PERM 所属者行「通过 | pytest」
- OpenAPI `GET /api/orders/{id}` 200：「id and items, no status」

本机：收集列表含该名；`pytest -q` 该条在 38 passed 内；`evidence/pytest-report.html` 记 **Passed**。隔离探针所属者 GET：`200 {'id': 'ord-f3e06af0f9ea', 'items': [{'sku': 'SKU-DEMO-003', 'qty': 1}]}`，无 `status`。拒绝路径 `test_order_forbidden_other_user` 仍在（B / 管理员 403）。允许/拒绝成对。

未改 `server.py`。xfail 仍只一条。

残留（原 G06-0001 后半，**不在** M-P1-32「加一条所属者 GET 200」范围内）：`test_admin_products_ok` 仍对管理员订单空列表做 `all(set(keys)=={"id"})`，空表恒真。种子 0 单时绿灯不能证明「列表元素只有 id」。

### 2.3 M-P1-18 — Postman `disableCookies`

`postman/MiniShop.postman_collection.json`：

- `json.loads` 合法；Collection v2.1；**15** 个 `item`；路径均为 `/api/`。
- 仅「无凭证创建」带 `"protocolProfileBehavior": {"disableCookies": true}`（全文 1 处）。
- 该请求 header 只有 `Content-Type`，**无** `Authorization`；Body `SKU-DEMO-001` qty=1；断言 401。

HTTP 等价（证明 Cookie 半边仍生效，故必须关 jar）：

| 请求 | 结果 |
| --- | --- |
| 无 Cookie、无 Bearer `POST /api/orders` | **401** `unauthorized` |
| 仅 `minishop_session` Cookie、无 Bearer | **201** 含 `id` |

本机无 Newman / Postman GUI，未点 Runner。请求级字段已写入 JSON，不依赖学生勾「Run collection without using stored cookies」。

残留（原 G06-0002 其余，本轮只验 `disableCookies`）：登录脚本仍无 `Set-Cookie`/`HttpOnly` 断言；后续请求仍只带 Bearer。空搜索-BUG-001 仍按 R-SEARCH 硬断言，Runner 会红（G06-0003，计划已披露）。

### 2.4 BUG-001 仍开放

| 通道 | 现场 |
| --- | --- |
| `bugs/BUG-001.md` | 「v1.0 保持开放，不在报告里写成已修复」 |
| 实现 | `GET /api/products?keyword=   ` → **200**，sku 三件全量 |
| pytest | `@pytest.mark.xfail(..., strict=True)`；本机 **XFAIL** `test_empty_keyword_should_not_return_all`；未 xpass |
| 用例/矩阵 | TC-SEARCH-001 / R-SEARCH 结果「**失败** BUG-001」 |
| HTTP 证据 | `evidence/http/03-products-empty-keyword.txt` 仍是主证据 |

未把缺陷写成已修复。`strict=True`：若有人改断言让空搜索「绿」，会 xpass 变红。

### 2.5 38 passed, 1 xfailed

命令（故意不走 `run.py test`）：

```text
cd project/minishop && .venv/bin/python -m pytest --collect-only -q
# 39 tests collected

.venv/bin/python -m pytest -q
# 38 passed, 1 xfailed in 0.77s
# XFAIL tests/test_api.py::test_empty_keyword_should_not_return_all
```

拆分：`test_api` 24（含 8 组 qty + 1 owner + 1 xfail）、`test_register` 11、`test_qty_rule` 4 → 39 = 38 passed + 1 xfailed。

仓库证据：

- `evidence/pytest-output.txt`：`38 passed, 1 xfailed in 0.92s`（时长与本机 0.77s 不同跑次，数字相同）
- `evidence/pytest-report.html`：2026-09-10 13:22:15；**38 Passed / 1 Expected failures**；`test_owner_can_read_own_order` Passed

项目 README、`docs/test-report.md`、实操 16-1 / 19-1 判定串均为 38/1。

---

## 3. 冻结口径抽查（未列入五项，顺带确认未回退）

| 冻结点 | 现场 |
| --- | --- |
| `/api/` | 一致 |
| qty=10 允许 / 11 拒绝 | 未改；本轮未复跑 qty 专测，但 38 passed 含 `test_cart_qty_cases` / `test_cart_qty_11_does_not_persist` |
| 订单成功无 `status` | 探针 201 仅 `id`；所属者 200 无 `status` |
| 个人实践 | PRD 首行仍是个人测试实践 |
| 密码 `Test1234` 登录成功 | 探针 200 + HttpOnly Cookie |

---

## 4. 本轮未跑 / 未改

- `python3 run.py test`、`run.py evidence`（会覆盖 `evidence/`）
- Postman GUI / Newman / JMeter
- 浏览器手工（空搜索/所属者已用 HTTP 探针）
- 教材正文（Verification 只写本文件）

---

## 5. 残留（不挡五项 VERIFIED；本轮 FIX_PLAN 未收）

| 残留 | 说明 | 原单 |
| --- | --- | --- |
| `evidence/screenshots/09-pytest-report.png` | 仍是 09-Sep 10:17、**37 Passed** / 38 tests。html 已是 10-Sep 38 Passed。FIX_PLAN 已列「需重截」 | M-P1-32 记录；Coordinator |
| `test_admin_products_ok` 空表恒真 | 管理员订单列表未先下单 | G06-0001 后半 |
| 矩阵「R-PERM \| 无凭证 401」 | 401 仍挂权限规则 | G06-0009 P2 |
| Postman 无 Cookie 契约断言 | 只有 `disableCookies`，无 Set-Cookie | G06-0002 其余 |
| `run.py test` 仍覆盖仓库 `pytest-output.txt` | 本验证故意绕开 | G06-0006 |
| OpenAPI 登录 200 文案仍写订单字段；无 securitySchemes | 薄于实现 | G06-0007 |
| pytest-html `CI: true` | 本机报告指纹 | G06-0010 |
| `docs/COURSE_CONTROL.md` | 仍写审查数字 `37 passed, 1 xfailed`（控制文档，非项目包） | 库存漂移 |

`09-pytest-report.png` 与现行 38/1 **不一致**。自动化数字以本机 pytest 与 `pytest-output.txt` / html 为准，不以该 PNG 为准。不把五项改成 Conditional。

---

## 6. 对 FIX_PLAN 的建议（本 Agent 未改台账）

| Audit ID | 修复状态 | 验证建议 |
| --- | --- | --- |
| G06-0004 | FIXED | **VERIFIED** |
| M-P1-32 | FIXED | **VERIFIED**（所属者 GET；PNG 仍待重截） |
| M-P1-18 | FIXED | **VERIFIED**（JSON 字段；GUI 未点） |

---

## 7. 执行记录

读过：`GLOBAL_06_MINISHOP.md`、`FIX_PLAN.md`、`FIX_LOG.md`、`FIX_G06-0004.md`、`FIX_M-P1-32.md`、`FIX_M-P1-18.md`、`PRD.md`、`prd-coverage-matrix.md`、`test-cases.md`、`test-report.md`、`openapi.json`、`bugs/BUG-001.md`、`tests/test_api.py`、`tests/conftest.py`、`server.py` `_create_order`、`postman/MiniShop.postman_collection.json`、`evidence/pytest-output.txt`、`evidence/pytest-report.html`、`09-pytest-report.png`、`practice/19-project-pack/main.py`。

跑过：

- `.venv/bin/python -m pytest --collect-only -q` → 39 collected
- `.venv/bin/python -m pytest -q` → **38 passed, 1 xfailed**
- `json.loads` 集合；item=15；`disableCookies` 仅无凭证创建
- 隔离 `ThreadingHTTPServer`：空搜索三件；下单不改购物车；所属者 200；无凭证 401；仅 Cookie 201

未跑：`run.py test` / `evidence`、Newman、浏览器。

---

## 8. 结论

作为本轮五项回归：**通过**。

- R-ORDER 已写明 v1.0 直接 POST sku+qty、不读不改购物车，实现与探针一致。
- 所属者 `GET /api/orders/{id}` 200 且无 `status` 已有 pytest + TC-PERM-002。
- Postman「无凭证创建」已 `disableCookies: true`。
- BUG-001 仍开放，xfail 未变成 xpass。
- 自动化基线 **38 passed, 1 xfailed**（收集 39）。

不要根据本文件去改空搜索断言、不要把 MiniShop 写成公司项目、不要把 38 passed 说成没有缺陷。
