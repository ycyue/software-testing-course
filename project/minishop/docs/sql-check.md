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

预期两行：鼠标 qty 1 stock 10；键盘 qty 2 stock 5。

超库存请求被拒绝后，不应出现 `qty=11` 的购物车行。修改数据仅限本机教学库。
