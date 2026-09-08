# MiniShop v1.0 用例摘要

P0～P3 为课程约定。

| ID | 标题 | 优先级 | 预期要点 | 结果 |
| --- | --- | --- | --- | --- |
| TC-LOGIN-001 | 正确密码登录 | P0 | 200，`result=ok`，非空 token，Set-Cookie | 通过 |
| TC-LOGIN-002 | 错误密码 | P0 | 401 | 通过 |
| TC-CART-001 | qty=1 | P0 | 200 | 通过 |
| TC-CART-002 | qty=10 | P0 | 200 | 通过 |
| TC-CART-003 | qty=11 | P0 | 400，库中不得把该次写成 11 | 通过 |
| TC-CART-004 | 缺 qty / null / "" / "1" / 0 | P1 | 均为 400 | 通过 |
| TC-ORDER-001 | 创建订单 | P0 | 201，有 id，无 status | 通过 |
| TC-ORDER-002 | 连续两次创建 | P1 | 两个不同 id | 通过 |
| TC-AUTH-001 | 无凭证下单 | P0 | 401 | 通过 |
| TC-PERM-001 | B 访问 A 的订单 | P1 | 403 | 通过 |
| TC-ADMIN-001 | 普通用户访问后台库存接口 | P1 | 403 | 通过 |
| TC-SEARCH-001 | keyword 为空白 | P1 | 按 PRD 不应全量 | **失败** BUG-001 |

完整步骤见 pytest 名称与 BUG-001。未列出的注册、页面文案为 P2 手工冒烟：登录页含 label/password，后台页可打开。
