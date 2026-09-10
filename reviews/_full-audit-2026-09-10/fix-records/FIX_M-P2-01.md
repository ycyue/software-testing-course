# FIX RECORD
Audit ID：M-P2-01（RT03-0001）
原问题：`PRAGMA foreign_keys` 按连接生效、不写入 sqlite 文件。12.4 脚本只在同一次会话打开约束；学生第二天重开 `sqlite3 ~/minishop-sql-lab.sqlite` 默认 OFF，`user_id=99` 能插进去。12.12 审查句「FOREIGN KEY constraint failed」只在同连接 ON 时成立，可复制块里既没有 99 那一行，也没有「每次打开都要再 ON」。
修改文件：
- `chapters/12a-sql-query.md`（12.3、12.4 跟做、12.6 重开）
- `chapters/12b-sql-write-and-minishop.md`（12.12、工作实战）
- `chapters/assets/diagrams/ch12-pk-fk.html` / `.png`（脚注同步）
修改位置：12.3 外键段；12.4 跟做；12.6 打开命令后；12.12 审查句与失败 INSERT；12B 工作实战进入后第一句。
原内容：（摘录）
`SQLite 默认不强制外键，需要 PRAGMA foreign_keys = ON;`
`审查中在 PRAGMA foreign_keys = ON 下插入不存在的用户，SQLite 报 FOREIGN KEY constraint failed。`
修复后内容：（摘录）
- 12.3：开关按**当前连接**生效，**不会写入** sqlite 文件；关掉终端再打开必须再执行一次。
- 12.4 / 12.6 / 12B 工作实战：每次打开教学文件先 `PRAGMA foreign_keys = ON;`。
- 12.12 可复制失败句：
```sql
PRAGMA foreign_keys = ON;
INSERT INTO cart_items (user_id, product_id, qty)
VALUES (99, 1, 1);
-- 期望：FOREIGN KEY constraint failed
```
  并写明：没报错说明这次连接没打开外键，先 `DELETE … WHERE user_id = 99` 再 ON 后重试。
为什么这样修：SQLite 外键默认关闭是连接级设置，不是库文件属性。只在 12.4 建库围栏写一次 ON，学生会以为「文件已经强制外键」，重开后幽灵用户插进去，审查句与引擎表现打架。
依据：SQLite 文档 Foreign Key Support：foreign key constraints must be enabled separately for each database connection；`PRAGMA foreign_keys` 不持久化到文件。本机 CLI 3.43.2：新连接 `PRAGMA foreign_keys` 返回 0，`VALUES (99,1,1)` 成功 id=4；同连接 `ON` 后再插 99 → `FOREIGN KEY constraint failed (19)`。MiniShop `server.connect()` 每次都会 `PRAGMA foreign_keys = ON;`，与教学 CLI 不是同一纪律。
是否影响其他章节：否。未改 `server.py`。教学 CLI 与应用连接的差异只写在第 12 章。
验证结果：
- 新 `sqlite3` 进程、不写 PRAGMA：`foreign_keys=0`，`user_id=99` 插入成功。
- 新进程先 `PRAGMA foreign_keys = ON`：返回 1，再插 99 失败。
- 12.12 耳机事务 `ROLLBACK` 后 99 失败句不污染 `cart_items`（3 行）。
状态：FIXED
