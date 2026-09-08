# MiniShop v1.0 测试点

| ID | 点 | 层 | 优先级 |
| --- | --- | --- | --- |
| TP-LOGIN-OK | 正确手机号密码登录 | 接口/Web | P0 |
| TP-LOGIN-BAD | 错误密码 | 接口 | P0 |
| TP-CART-1 | qty=1 | 接口 | P0 |
| TP-CART-10 | qty=10 等于库存 | 接口 | P0 |
| TP-CART-11 | qty=11 超库存 | 接口/SQL | P0 |
| TP-CART-NULL | qty 缺 / null / "" / 字符串 | 接口 | P1 |
| TP-ORDER-ID | 创建订单返回 id 且无 status | 接口 | P0 |
| TP-ORDER-2 | 两次 POST 两个 id | 接口 | P1 |
| TP-AUTH-401 | 无凭证改购物车/下单 | 接口 | P0 |
| TP-PERM-403 | 用户 B 读用户 A 订单 | 接口 | P1 |
| TP-ADMIN | 普通用户 403，管理员 200 | 接口/Web | P1 |
| TP-SEARCH-EMPTY | 空关键字 | 接口/Web | P1 |
| TP-SQL-JOIN | Tester A 购物车与库存 | SQL | P1 |
