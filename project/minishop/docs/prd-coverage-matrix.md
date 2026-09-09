# MiniShop v1.0 PRD 覆盖矩阵

日期：2026-09-09。个人实践，非正式公司度量。P0～P3 为课程用例约定。

| 规则 | 要点 | 测试点 | 用例 | 层 | 优先级 | 结果 | 证据 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-PHONE | 11 位数字且以 1 开头，按字符串存 | TP-REG-PHONE | TC-REG-002 | 接口 | P0 | 通过 | `tests/test_register.py` |
| R-PASS | 8～16 位，字母+数字 | TP-REG-PASS | TC-REG-003 | 接口 | P0 | 通过 | `tests/test_register.py` |
| R-REG | 合法注册 201、无 token；占用 409 | TP-REG-OK / TP-REG-DUP | TC-REG-001 / TC-REG-004 | 接口/Web | P0 | 通过 | `evidence/http/07-register-ok.txt`、`08-register-duplicate.txt` |
| R-AUTH | 登录 JSON token + HttpOnly Cookie；后续 Bearer | TP-LOGIN-OK | TC-LOGIN-001 | 接口/Web | P0 | 通过 | `evidence/http/01-login-ok.txt`、`evidence/screenshots/03-shop.png` |
| R-AUTH | 错误密码 401 | TP-LOGIN-BAD | TC-LOGIN-002 | 接口/Web | P0 | 通过 | `evidence/http/02-login-bad.txt`、`02-login-fail.png` |
| R-CART / R-CART-10 | qty=1、qty=10 允许 | TP-CART-1 / TP-CART-10 | TC-CART-001 / TC-CART-002 | 接口 | P0 | 通过 | `evidence/http/04-cart-qty-10.txt` |
| R-CART / R-CART-10 | qty=11 拒绝且不落库 | TP-CART-11 | TC-CART-003 | 接口/SQL | P0 | 通过 | `05-cart-qty-11.txt`、`sql/seed-join.txt`、`05-cart-qty-11.png` |
| R-CART | 缺 qty / null / "" / "1" / 0 | TP-CART-NULL | TC-CART-004 | 接口 | P1 | 通过 | pytest parametrize |
| R-ORDER | 201 + id，无 status | TP-ORDER-ID | TC-ORDER-001 | 接口 | P0 | 通过 | `evidence/http/06-order-create.txt` |
| R-ORDER | 两次 POST 两个 id | TP-ORDER-2 | TC-ORDER-002 | 接口 | P1 | 通过 | pytest |
| R-PERM | 无凭证 401 | TP-AUTH-401 | TC-AUTH-001 | 接口 | P0 | 通过 | pytest |
| R-PERM | B 读 A 订单 403 | TP-PERM-403 | TC-PERM-001 | 接口 | P1 | 通过 | pytest |
| R-PERM | 普通用户 `/api/admin/*` 403；管理员 200；管理员 `GET /api/orders/{他人}` 亦 403 | TP-ADMIN | TC-ADMIN-001 / TC-ADMIN-002 | 接口/Web | P1 | 通过 | pytest、`07-admin.png` |
| R-SEARCH | 空/空白关键字不应全量 | TP-SEARCH-EMPTY | TC-SEARCH-001 | 接口/Web | P1 | **失败** BUG-001 | `03-products-empty-keyword.txt`、`04-search-empty-bug001.png` |
| （页面） | 首页含登录/注册表单 | TP-WEB-HOME | TC-WEB-001 | Web | P2 | 通过 | `01-login.png`、`06-register.png` |

未覆盖（明确留下，不假装通过）：

- 支付、物流、优惠券、订单状态机：PRD 非范围。
- Postman GUI Collection Runner：本机未点击；集合 JSON 与脚本已入库。
- 无头 UI 逐控件套件：截图为 Playwright + 本机 Chrome 的手工等价路径，不是回归套件。
