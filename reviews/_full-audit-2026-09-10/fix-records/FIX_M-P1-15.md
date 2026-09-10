# FIX RECORD
Audit ID：M-P1-15（CH12-0001 / CH12-0002 / CH12-0003 / CH12-0004；G05-0002 / G05-0003 / G03-0009）
原问题：
1. `ch12-tables` 自称 MiniShop 种子，却只画 2 用户 / 2 商品 / Tester A 两行车，caption 抄邻图「主键 / 先 SELECT」。
2. `ch12-pk-fk` 把 `products.sku` 写成主键，外键只画 `user_id`。
3. 12A 承诺本机 `sqlite3` 完成，第一条可复制 SELECT 前没有打开教学库的命令。
4. 12.12 INSERT 耳机没有 `BEGIN…ROLLBACK`，抄完会永久污染 LEFT JOIN / 练习 7。
修改文件：
- `chapters/assets/diagrams/ch12-tables.html`
- `chapters/assets/diagrams/ch12-tables.png`（已重截）
- `chapters/assets/diagrams/ch12-pk-fk.html`
- `chapters/assets/diagrams/ch12-pk-fk.png`（已重截）
- `chapters/12a-sql-query.md`（12.4 跟做命令、12.6 第一条 SELECT 前、工作实战）
- `chapters/12b-sql-write-and-minishop.md`（12.12 INSERT）
修改位置：12.4 示意图与跟做；12.3 主键图；12.6 第一条 SELECT 前；12.12 INSERT 代码块。
原内容：（摘录）
- 图 lead：`MiniShop 种子数据如下。` users/products/cart 各 2 行。caption：`主键认出一行，外键把行连起来。改数前先 SELECT…`
- 主键卡：`users.id、products.sku（唯一）。` 外键只写 `cart_items.user_id → users.id`
- 12A 仅前置句「可在本机 sqlite3 完成」，第一条 `sqlite3` 命令原在 12B
- 12.12 裸 `INSERT … VALUES (1, 3, 1);`，散文才说应放进事务
修复后内容：（摘录）
- 图标明「12.4 教学库，不是 MiniShop v1.0 种子」；users 3 行（`13800138002` / `NULL`，不是 admin）；products 3 行含耳机；cart_items 3 行（含 Tester B）；caption 只讲三表会合。
- 主键：`users.id`、`products.id`、`cart_items.id`；sku 标 UNIQUE 不是 PK；外键两条：`user_id→users.id` 且 `product_id→products.id`。
- 12.4 表后与 12.6 第一条 SELECT 前均给出 `sqlite3 ~/minishop-sql-lab.sqlite`；禁止打开 `project/minishop/data/minishop.sqlite`。
- 12.12 耳机 INSERT 包进 `BEGIN; … ROLLBACK;`，并写误插后用主键 `DELETE`。
为什么这样修：图插在 12.4 教学 INSERT 之前，必须画教学库全表，否则 `COUNT(*)=3`、LEFT JOIN 耳机空行、SKU-DEMO-001 两行都对不上。主键图画 sku 会教错 JOIN 键。12A 没有打开命令就要求写出 SELECT。可复制 INSERT 必须与 12.13 同构，否则练习 7 的「003 qty 为空」被自己污染。
依据：12.4 DDL（`id INTEGER PRIMARY KEY`，`sku TEXT NOT NULL UNIQUE`）；独立 CLI 3.43.2：教学库 `COUNT(*)=3` / `COUNT(display_name)=2`；`BEGIN` 插耳机后 LEFT JOIN 003 的 qty=1，`ROLLBACK` 后恢复为空。SQLite PRIMARY KEY ≠ UNIQUE。
是否影响其他章节：否。v1.0 主库与实操 12-1 临时库未改。12B 练习 7 答案在回滚后仍然成立。
验证结果：
- 图：users 3 / products 3（含耳机 stock=3）/ cart 3；caption 不再抄主键课；PK 卡不再写 sku。
- Chrome headless `--window-size=1320,780` 已重截 `ch12-tables.png`、`ch12-pk-fk.png`。
- CLI：`ROLLBACK` 后 `cart_items` 仍 3 行；LEFT JOIN 第四行 `SKU-DEMO-003` qty 空。
状态：FIXED
需重截 PNG：已由本 Agent 按 `chapters/assets/diagrams/README.md` 用本机 Chrome 无头截过；Coordinator 统一过一遍亦可。
