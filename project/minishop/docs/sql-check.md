# SQL 核对（授权教学库）

种子库在每次 `MINISHOP_RESET=1` 启动时重建。核对 Tester A 购物车：

```sql
PRAGMA foreign_keys = ON;
SELECT u.phone, p.sku, c.qty, p.stock
FROM cart_items AS c
INNER JOIN users AS u ON c.user_id = u.id
INNER JOIN products AS p ON c.product_id = p.id
WHERE u.phone = '13800138000';
```

预期两行（**v1.0 初始种子**，尚未改数量）：鼠标 qty 1 stock 10；键盘 qty 2 stock 5。

本机输出见 `evidence/sql/seed-join.txt`：

- 第一节「种子」应对上上面两行；
- 第二节是证据会话里 `qty=10` 允许、`qty=11` 拒绝之后的库；鼠标可为 10，但不得为 11。

这是 MiniShop v1.0 种子，不是第 12 章 12.4 那套教学 INSERT（用户 3 为 `13800138002`、`display_name` 为 `NULL`）。

`test_cart_qty_11_does_not_persist` 用接口再读购物车交叉验证。修改数据仅限本机教学库。
