# MiniShop v1.0 测试用例

P0～P3 为课程约定。完整自动化名称见 `tests/`。执行记录见 `evidence/`。

## 摘要

| ID | 标题 | 优先级 | 预期要点 | 结果 | 证据 |
| --- | --- | --- | --- | --- | --- |
| TC-REG-001 | 合法新手机号注册 | P0 | 201，`result=ok`，有 phone，无 token | 通过 | `tests/test_register.py`、`evidence/http/07-register-ok.txt` |
| TC-REG-002 | 非法手机号 | P0 | 10 位 / 非 1 开头 / 含字母 / 空串 → 400 | 通过 | pytest parametrize |
| TC-REG-003 | 非法密码 | P0 | 过短 / 无数字 / 无字母 / 过长 → 400 | 通过 | pytest parametrize |
| TC-REG-004 | 已占用手机号 | P0 | 409 `phone taken` | 通过 | `evidence/http/08-register-duplicate.txt` |
| TC-LOGIN-001 | 正确密码登录 | P0 | 200，`result=ok`，非空 token，Set-Cookie HttpOnly | 通过 | `evidence/http/01-login-ok.txt` |
| TC-LOGIN-002 | 错误密码 | P0 | 401 | 通过 | `evidence/http/02-login-bad.txt` |
| TC-WEB-001 | 首页含登录与注册表单 | P2 | 200，含 label/password/register-form | 通过 | `evidence/screenshots/01-login.png` |
| TC-CART-001 | qty=1 | P0 | 200 | 通过 | pytest |
| TC-CART-002 | qty=10 | P0 | 200 | 通过 | `evidence/http/04-cart-qty-10.txt` |
| TC-CART-003 | qty=11 | P0 | 400，购物车不得写成 11 | 通过 | `evidence/http/05-cart-qty-11.txt`、`sql/seed-join.txt` |
| TC-CART-004 | 缺 qty / null / "" / "1" / 0 | P1 | 均为 400 | 通过 | pytest |
| TC-ORDER-001 | 创建订单 | P0 | 201，有 id，无 status | 通过 | `evidence/http/06-order-create.txt` |
| TC-ORDER-002 | 连续两次创建 | P1 | 两个不同 id | 通过 | pytest |
| TC-AUTH-001 | 无凭证下单 | P0 | 401 | 通过 | pytest |
| TC-PERM-001 | B 访问 A 的订单 | P1 | 403，Body 不含该 id | 通过 | pytest |
| TC-PERM-002 | 所属者读自己的订单 | P1 | 200，body 有 id 与 items，无 status | 通过 | pytest |
| TC-ADMIN-001 | 普通用户访问后台库存接口 | P1 | 403 | 通过 | pytest |
| TC-ADMIN-002 | 管理员打开后台页 | P1 | 200，列出库存，订单只有 id | 通过 | `evidence/screenshots/07-admin.png` |
| TC-SEARCH-001 | keyword 为空白 | P1 | 按 PRD 不应全量 | **失败** BUG-001 | `evidence/http/03-products-empty-keyword.txt`（主证据；页面截图不能单独证明提交了空关键字） |

## 详细步骤（P0 抽样，可手工复现）

### TC-REG-001 合法注册

- 前置：服务已启动，教学库已重置；手机号 `13900001111` 不在种子用户中。
- 步骤：`POST /api/register`，Body `{"phone":"13900001111","password":"Test1234","display_name":"New User"}`。
- 预期：HTTP 201；JSON 含 `result=ok` 与 `phone`；**没有** `token`。随后用同一手机号登录应得 200。
- 实际（2026-09-09 本机）：与预期一致。

### TC-LOGIN-001 正确密码登录

- 前置：种子账号 `13800138000` / `Test1234`。
- 步骤：打开 `http://127.0.0.1:8765/`，输入手机号和密码，点「登录」。同时可抓 `POST /api/login`。
- 预期：页面进入商品区；接口 200；JSON 有 token；响应头 `Set-Cookie` 含 `HttpOnly`。
- 实际：通过。截图 `evidence/screenshots/03-shop.png`。

### TC-CART-003 qty=11

- 前置：已登录 Tester A；`SKU-DEMO-001` 库存 10。
- 步骤：购物车数量填 11 并提交；或 `POST /api/cart/items` `{"sku":"SKU-DEMO-001","qty":11}`。
- 预期：400 `qty exceeds stock`；再查购物车 / SQL，该 SKU 数量不是 11。
- 实际：通过。

### TC-SEARCH-001 空白关键字

- 步骤：搜索框输入三个空格，或 `GET /api/products?keyword=   `。
- 预期（R-SEARCH）：不应把三件商品当搜索结果。
- 实际：200，三件商品都在。开放缺陷 BUG-001。
