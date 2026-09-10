# Chapter 12 Audit

审计角色：Chapter-Audit-Agent-12（技术审计 / 事实核查 / 初学者体验 / 岗位视角）  
范围：第 12 章全部（索引 + 12A 查询 + 12B 写操作），不含其他章正文。  
日期：2026-09-10  
引擎实跑：SQLite CLI 3.43.2；Python `sqlite3` 模块绑定 3.50.4。

## 1. Coverage

禁止抽样。下表分母为本章范围内全部内容单元；未检查必须为 0。

| 类型 | 数量 | 已检查 | 未检查 | 备注 |
| --- | ---: | ---: | ---: | --- |
| 索引页标题/段落 | 1 标题 + 6 散文块 | 7 | 0 | `chapters/12-database-and-sql.md` |
| 12A 标题（含 # / ## / ###） | 40 | 40 | 0 | 12.1–12.11 + 模板块 |
| 12B 标题（围栏外） | 36 | 36 | 0 | 12.12–12.16 + 模板块；围栏内作业模板标题不另计 |
| 12A 散文块 | 92 | 92 | 0 | 跳过代码围栏与表格 |
| 12B 散文块 | 71 | 71 | 0 | 同上 |
| 表格 | 9 | 9 | 0 | 12A×8，12B×1 |
| 代码围栏 | 24 | 24 | 0 | 12A 14（1 text + 13 sql）；12B 9（6 sql + text/bash/markdown）；practice README 1 bash |
| SQL 语句（围栏内可执行句） | 49 | 49 | 0 | 12A 27；12B 19；`sql-check.md` 2；practice `JOIN_SQL` 1。每条独立重跑 |
| 行内危险/对照 SQL | 6 | 6 | 0 | 无 WHERE 的 UPDATE、DROP、TRUNCATE、`SELECT * … = NULL`、`START TRANSACTION`、`user_id=99` |
| Linux/Shell 命令 | 2 | 2 | 0 | `sqlite3 ~/minishop-sql-lab.sqlite`；`python3 practice/run.py 12-1` |
| HTTP 示例 | 2 | 2 | 0 | 仅 practice：`POST /api/login`、`POST /api/cart/items`（正文无 HTTP 报文） |
| 测试用例 / 验收 | 6 | 6 | 0 | 12-1 验收 3 条；12B 验证清单 4 条中与库相关者；pytest 名 `test_cart_qty_11_does_not_persist` |
| Bug / 缺陷示例 | 4 | 4 | 0 | 无 WHERE 整表清零；UI 对库不对；qty=11 教学对照；接口 400 仍要查库 |
| 章内练习题 | 10 | 10 | 0 | 12A 1–5；12B 6–10。先独立作答再对答案 |
| 章内练习答案 | 10 | 10 | 0 | |
| 阶段测验第 12 章题 | 6 | 6 | 0 | `stage-4-ops.md` Q5–Q10。Q1–Q4 属第 11 章，不纳入本章分母 |
| 阶段测验第 12 章答案 | 6 | 6 | 0 | |
| PNG 示意图 | 5 | 5 | 0 | `read_file` 打开像素图 |
| HTML 示意图源 | 5 | 5 | 0 | 与 PNG 文案一致 |
| Markdown 链接 | 16 | 16 | 0 | 全部可解析；无外链 URL |
| 图注 / alt | 5 | 5 | 0 | |
| Practice 源码 | 2 文件 | 2 | 0 | `main.py`、`tests/test_lab.py` |
| MiniShop SQL 文档与证据 | 2 | 2 | 0 | `sql-check.md`、`seed-join.txt` |
| MiniShop schema / 种子（只读副本） | 1 库 | 1 | 0 | 复制后查询，未改原库 |

**Coverage：100%。未检查 = 0。**

大纲 v1.2 第 12 章主题对照（数据库、PK/FK、关系/非关系、CRUD、SELECT、WHERE、逻辑运算、排序/限制/去重、聚合、GROUP BY/HAVING、JOIN、NULL、INSERT/UPDATE/DELETE、事务、COMMIT/ROLLBACK、MiniShop 数据验证、授权库 + 先 SELECT）：正文均有对应小节。缺口不在「没写」，在图、动手第一帧、写示例污染查询练习。

## 2. 总评分

核心章，按严评分。九项各 /10；总体按 90 分母折算为百分制。质量标准发布线 90、核心章目标 95 是作者目标，不是本审计下限。

| 项 | 分 | 依据 |
| --- | ---: | --- |
| 技术准确性 | 8 | 围栏内 SQL 与审查数字全部独立复现；示意图把 `products.sku` 写成主键；12.16 清单把「库存减少」套到购物车接口 |
| 岗位实用性 | 8 | 先 SELECT、授权库、无 WHERE=事故、事务回滚、UI/库交叉验证是初级岗位真技能；缺客户端工具、PII、只读账号、备份命令 |
| 完整性 | 8 | 大纲主题齐；SQLite 无 TRUNCATE、FK 默认关闭、方言差异大体写清；缺 SQLite 自身 GROUP BY 宽松、教学库 vs MiniShop UNIQUE 对照表 |
| 初学者友好度 | 7 | 查询坡度合理；两套（实则三套）库反复口头区分，但 12A 没有 `sqlite3` 第一帧，图还把种子画错 |
| 教学顺序 | 8 | 先 SELECT 再 DELETE 的拆章正确；12.12 INSERT 不带事务，会破坏后面 LEFT JOIN / 练习 7 |
| 代码质量 | 8 | 教学 SQL 可运行、practice 使用 `?` 绑定；INSERT 示例在 sqlite3 默认 autocommit 下会永久插入 |
| 实操质量 | 7 | 12-1 绿路径 API=SQL=2 可跑且隔离临时库；不观察 UI，也没有「对不上」的失败样本 |
| 练习质量 | 7 | 10 题答案与独立推导一致；12A 偏解释、练习 4 答案没写出 SQL |
| 图片质量 | 5 | 五张里两张事实错误（表数据、主键），两张跑题（NULL→第 13 章；先 SELECT→qty=11/TRUNCATE） |
| **总体** | **73/100** | 九项合计 66/90 → 73。核心章目标 95 **未达到** |

Definition of Done（质量标准 20 项）独立判断：**16/20**。未过：3 无知识性错误（图）、6 术语（图中主键）、13 图表帮助理解、17 练习覆盖目标（12A 动手弱）。不得按核心章直接发布。

## 3. P0

无。

未把 GET/POST 安全神话、Cookie/Session/Token 三选一、P0 等级全国统一等禁止项写进本章。  
无 WHERE 的 `UPDATE`/`DELETE` **已充分警告**（12.13 点名整表清零是事故、错误 1、面试、检查清单、练习 6/10）。按任务要求：此项不作为问题开单。  
未教「SQLite 有 TRUNCATE」。未鼓励在生产库写。未把教学库 `13800138002` 写成管理员。

## 4. P1

## ISSUE
ID：CH12-0001
文件：`chapters/12a-sql-query.md`；`chapters/assets/diagrams/ch12-tables.html`；`chapters/assets/diagrams/ch12-tables.png`
章节：第 12 章（上）
小节：12.4 教学库：三张表
精确位置：12a 第 82 行插图；HTML 第 16 行 lead「MiniShop 种子数据如下。」
原文：`MiniShop 种子数据如下。` 图中 users 仅 2 行、products 仅 2 行、cart_items 仅 Tester A 两行。
问题等级：P1
问题类别：IMG / SEQ / PED
问题说明：图插在 12.4 **教学 INSERT 之前**，却自称 MiniShop 种子，数据既对不上 12.4（缺 `13800138002`/NULL、缺耳机、缺 Tester B 购物车），也对不上 v1.0 种子（缺管理员 `13800138099`、缺 `SKU-DEMO-003`、缺 `user_id=2` 的购物车）。PNG 与 HTML 一致。
为什么有问题：读者若用图做练习 5 的 `COUNT(*)` 会得到 2 而不是 3；做 12.10 LEFT JOIN 看不到耳机空行，也看不到「SKU-DEMO-001 出现两行」。12.4 正文表格是对的，图在表格之前，先入为主。
依据：独立查询 12.4 教学库 `COUNT(*)=3`；只读副本 `minishop.sqlite` 用户 3 为 `13800138099` Admin；PRD 教学数据三条用户、三件商品。
建议修改：图改画 12.4 全表，标题写明「12.4 教学库，不是 MiniShop v1.0 种子」，脚注 `002 ≠ 099`。
推荐替换文本：见第 16 节补丁 1。

## ISSUE
ID：CH12-0002
文件：`chapters/assets/diagrams/ch12-pk-fk.html`；`chapters/assets/diagrams/ch12-pk-fk.png`；出现于 `chapters/12a-sql-query.md` 12.3
章节：第 12 章（上）
小节：12.3 主键与外键
精确位置：HTML 主键卡片「users.id、products.sku（唯一）。没有它，两行鼠标会分不清。」
原文：`users.id、products.sku（唯一）。`
问题等级：P1
问题类别：IMG / TERM / SQL
问题说明：12.4 `CREATE TABLE products ( id INTEGER PRIMARY KEY, sku TEXT NOT NULL UNIQUE, …)`。正文 ASCII 图也写 `products.id <----- cart_items.product_id`。示意图把 UNIQUE 列当成「这一行的身份证」。
为什么有问题：初学者会按 sku 去 JOIN `cart_items.product_id`（整数 1）对 `products.sku`（文本 `SKU-DEMO-001`），结果空。主键定义在核心章图上写错，属于会教错。
依据：12.4 DDL；SQL 标准 PRIMARY KEY ≠ UNIQUE；独立 `PRAGMA table_info` 等价物即 DDL。
建议修改：主键写 `users.id`、`products.id`、`cart_items.id`；sku/phone 标 UNIQUE。
推荐替换文本：见第 16 节补丁 2。

## ISSUE
ID：CH12-0003
文件：`chapters/12a-sql-query.md`
章节：第 12 章（上）
小节：前置知识；12.4；MiniShop 工作实战（上）
精确位置：第 23 行「本章可在本机 `sqlite3` 完成」；第 366–368 行工作实战
原文：`会用终端更方便，但本章可在本机 sqlite3 完成。` / `最小动作：打开 project/minishop/docs/sql-check.md 里的 JOIN，对照 … seed-join.txt 第一节。`
问题等级：P1
问题类别：SEQ / PRE / PED
问题说明：学习目标要求「写出带 WHERE 的 SELECT」，12.4 起所有审查结果都假设学生有一份教学库，但 12A **没有任何一条** `sqlite3 …` 第一帧。第一条 sqlite 命令出现在 12B 第 211 行 `sqlite3 ~/minishop-sql-lab.sqlite`。12A 工作实战的「最小动作」是打开 Markdown/TXT，不是执行 SQL。
为什么有问题：练习 3/5 的答案（`IS NULL`、`COUNT(*)=3` / `COUNT(display_name)=2`）只对 12.4 教学库成立。若学生按工作实战去碰 v1.0 库：`display_name` 全非空，`COUNT(display_name)=3`，`IS NULL` 零行。对 `project/minishop/data/minishop.sqlite` 粘贴 12.4 INSERT 会因缺少 `password_hash`/`role` 失败。
依据：12A 全文检索仅「sqlite3」一词在第 23 行；12B 第 211 行才有命令；副本库用户 3 为 Admin 而非 NULL。
建议修改：12.4 表后立刻给出独立教学文件命令，并写「不要打开 MiniShop 主库」；工作实战补产出路径。
推荐替换文本：见第 16 节补丁 3。

## ISSUE
ID：CH12-0004
文件：`chapters/12b-sql-write-and-minishop.md`
章节：第 12 章（下）
小节：12.12 INSERT；练习 7
精确位置：第 32–39 行代码块；第 43 行散文警告；第 307–328 行练习 7
原文：
```sql
INSERT INTO cart_items (user_id, product_id, qty)
VALUES (1, 3, 1);
```
`这会给 Tester A 加一行耳机。` 练习 7：`SKU-DEMO-003 的数量为空`
问题等级：P1
问题类别：SQL / SEQ / EX
问题说明：12.13 的 UPDATE/DELETE 都包在 `BEGIN`…`ROLLBACK` 里。12.12 的 INSERT **没有**。sqlite3 CLI 默认 autocommit，抄这段会永久插入耳机行。散文虽然说「应放在事务里回滚」，学生复制的是代码块。
为什么有问题：独立复现：INSERT 后 LEFT JOIN 中 `SKU-DEMO-003` 的 `qty` 变为 `1`，不再为空。练习 7 标准答案「空数量：没有匹配的购物车行」在已执行 12.12 的库上不成立。数据独立性写在段落里，没有写进可复制 SQL。
依据：本机 INSERT 后 `LEFT JOIN … ORDER BY p.sku` 第四行 `(SKU-DEMO-003, 1)`；练习 7 答案第 328 行。
建议修改：INSERT 示例改为 `BEGIN; … ROLLBACK;`，与 12.13 同构；另给一条 `user_id=99` 的可复制失败句。
推荐替换文本：见第 16 节补丁 4。

## 5. P2

## ISSUE
ID：CH12-0005
文件：`chapters/assets/diagrams/ch12-null.html` / `ch12-null.png`；`chapters/12a-sql-query.md` 12.11
章节：第 12 章（上）
小节：12.11 NULL
精确位置：图 lead「JSON 的 null 进 Python 是 None」；脚注「第 13 章四态」
原文：`JSON 的 null 进 Python 是 None，进 SQL 常是 NULL。` / `第 13 章四态（缺 / null / 空串 / 错误类型）和这里是同一套纪律。`
问题等级：P2
问题类别：IMG / PED / SEQ
问题说明：12.11 正文用教学库用户 3 的 `display_name` 讲 `IS NULL`。图不出现用户 3，改讲 JSON 缺字段、Python `None`、第 13 章四态。Python 在第 15 章，接口四态在第 13 章。
为什么有问题：零基础在第 12 章被拖去未学语言与未学接口课；本章真正难点（`= NULL` 得不出真、`COUNT(列)` 跳过 NULL）图上没有。
依据：学习顺序 12 → 13 → 15；12.11 审查结果是用户 3 / `13800138002`。
建议修改：图改回用户 3 的 `IS NULL` / `= NULL` / `COUNT(display_name)`。JSON 四态留给第 13 章。
推荐替换文本：三格改为「NULL 缺失」「空字符串 ''」「0 是有值」；脚注写用户 3。

## ISSUE
ID：CH12-0006
文件：`chapters/assets/diagrams/ch12-join.html` / `ch12-join.png`；`12a` 12.10
章节：第 12 章（上）
小节：12.10 JOIN
精确位置：图只演示 INNER JOIN 拼出 Tester A 的鼠标一行
原文：`拼完：13800138000 · SKU-DEMO-001 · qty 1 · stock 10`
问题等级：P2
问题类别：IMG / PED
问题说明：12.10 真正难点是 LEFT JOIN 把 `SKU-DEMO-001` 复制成两行、`SKU-DEMO-003` qty 为空、结果行数 ≠ 商品数。图只画幸福路径一行。
为什么有问题：练习 7 完全依赖这个难点，图帮不上。
依据：独立 LEFT JOIN 结果四行：001/1、001/1、002/2、003/NULL。
建议修改：补 LEFT JOIN 图，或把现图第三格改成「一行变两行 / 空着的是没匹配」。
推荐替换文本：见第 16 节补丁 5。

## ISSUE
ID：CH12-0007
文件：`chapters/assets/diagrams/ch12-select-first.html` / `ch12-select-first.png`；`12b` 12.13
章节：第 12 章（下）
小节：12.13 UPDATE 与 DELETE
精确位置：第三步「超库存被接口拒绝后，这里不得出现 11。」；脚注「SQLite 没有 TRUNCATE」
原文：同上
问题等级：P2
问题类别：IMG / PED
问题说明：图命题是「先数清楚会切到几行」。第三步应是「同一 WHERE 再 SELECT，不对就 ROLLBACK」。qty=11 属于 12.16，TRUNCATE 属于 12.14。
为什么有问题：一张图塞三个难点，削弱「先数行」这一句。
依据：12.13 安全流程第 6–7 步；12.16 才是 qty=11 对照。
建议修改：第三步改回核对行数/内容；脚注只留授权库 + 无 WHERE 会切整表。
推荐替换文本：`同一 WHERE 再查一次：行数和内容是不是你要的。不对就 ROLLBACK。`

## ISSUE
ID：CH12-0008
文件：`practice/12-sql-cross-check/main.py`；`practice/12-sql-cross-check/README.md`；`chapters/12b-sql-write-and-minishop.md` 场景导入
章节：第 12 章（下）+ 实操 12-1
小节：场景导入；实操打印
精确位置：`main.py` 第 34 行；第 91 行提问
原文：`实操 12-1  页面说 2 件，库里是不是 2 件？` / `读完请回答：为什么 UPDATE 之前要先 SELECT？`
问题等级：P2
问题类别：PED / EX / JOB
问题说明：脚本从未打开浏览器，只打 `POST /api/cart/items`。一句话核心是「UI 对了库不对，仍是缺陷」，12-1 只证明绿路径 API=SQL=2，不制造「页面对、库不对」。结尾问 UPDATE 前为何 SELECT，但本次没有手写 SQL UPDATE。
为什么有问题：学生可能把「页面说 2 件」写进证据/简历。旧问题「12-1 绑 qty=11」已修好（索引与 12B 已声明 qty=2），但绿路径被说成验证了 UI。
依据：等价脚本实跑 `POST` 200 `{"sku":"SKU-DEMO-001","qty":2}`，JOIN `qty=2`；无 UI 代码。
建议修改：打印改为「接口返回 2，库里是不是 2」；正文写明失败样本在 12.16 事务对照；末问改为「两条通道对不上为什么仍是缺陷」。
推荐替换文本：`实操 12-1  接口返回 qty=2，JOIN 是不是也是 2？脚本不打开浏览器。`

## ISSUE
ID：CH12-0009
文件：`chapters/12b-sql-write-and-minishop.md`；`project/minishop/tests/test_api.py`
章节：第 12 章（下）
小节：场景导入；本章可运行性说明
精确位置：12b 第 24、255、356 行
原文：`qty=11 不落库看 evidence/sql/seed-join.txt 和 pytest test_cart_qty_11_does_not_persist` / `qty=11 不落库由 pytest 与 SQL 交叉验证`
问题等级：P2
问题类别：TEST / SQL
问题说明：`test_cart_qty_11_does_not_persist` 只 `GET /api/cart` 比较接口 qty，**不执行 SQL**。SQL 证据是静态 `seed-join.txt` 第二节。
为什么有问题：学生打开该测试会以为「pytest 已经查过库」。本章核心是库通道，命名与表述夸大了交叉验证。
依据：`test_api.py` 第 95–117 行无 `sqlite3`；本审计用临时库独立跑：qty=10 允许、qty=11 返回 400，JOIN 鼠标 qty=10 不是 11——结论对，但那是审计补做的 SQL，不是该测试做的。
建议修改：写明 pytest 核的是接口再读；库核对着 `seed-join.txt` 或自己 JOIN。或给测试加一条 SQL 断言。
推荐替换文本：`pytest 用 GET /api/cart 确认仍不是 11；库状态见 evidence/sql/seed-join.txt 第二节。两者一起才叫交叉验证。`

## ISSUE
ID：CH12-0010
文件：`chapters/12b-sql-write-and-minishop.md`
章节：第 12 章（下）
小节：12.16 MiniShop 数据验证
精确位置：第 192 行验证清单第 3 条
原文：`接口成功后库存有没有少、购物车有没有多`
问题等级：P2
问题类别：TEST / JOB
问题说明：MiniShop `POST /api/cart/items` 是按 sku **覆盖 qty**（已有行 UPDATE，无行 INSERT），**不减少** `products.stock`。库存减少发生在 `POST /api/orders`。独立验证：cart qty=2 前后 `stock` 均为 10。
为什么有问题：学生按清单去查购物车接口，会把「库存没少」误报成缺陷，或把「行数没多」（upsert）误报成缺陷。
依据：`server.py` `_cart_items` 第 400–413 行；`_create_order` 第 454–456 行 `stock = stock - ?`。
建议修改：拆成两条：改购物车后 qty 与 stock 比较（qty≤stock，stock 本身不变）；下单成功后 stock 减少。标明这是 MiniShop v1.0 行为，第 19 章前可写「以当前实现为准」。
推荐替换文本：`改购物车成功：同一用户同一 SKU 的 qty 被更新为请求值，products.stock 不变。下单成功：stock 减少，订单表多一行 id。`

## ISSUE
ID：CH12-0011
文件：`chapters/12a-sql-query.md`
章节：第 12 章（上）
小节：练习 4 / 练习答案
精确位置：第 430–432 行题干；第 445 行答案
原文：`写出查询 Tester A（13800138000）购物车 sku、数量和库存的 JOIN。` / `使用 12.10 的 INNER JOIN 三表查询，…`
问题等级：P2
问题类别：EX / ANS
问题说明：题干要求「写出」，答案只指向 12.10，不给出语句。
为什么有问题：学生无法对照自己的 SQL；与「答案与练习对应」的 DoD 不完全吻合。
依据：质量标准第 18 项；题干动词「写出」。
建议修改：答案贴出完整 SQL + 两行预期。
推荐替换文本：
```sql
SELECT u.phone, p.sku, c.qty, p.stock
FROM cart_items AS c
INNER JOIN users AS u ON c.user_id = u.id
INNER JOIN products AS p ON c.product_id = p.id
WHERE u.phone = '13800138000';
```
预期：鼠标 qty 1 stock 10；键盘 qty 2 stock 5（无 ORDER BY 时行序不保证）。

## ISSUE
ID：CH12-0012
文件：`chapters/12a-sql-query.md` 12.4 / 12.9；对比 `project/minishop/server.py`
章节：第 12 章（上）
小节：12.4；12.9
精确位置：12.4 `CREATE TABLE cart_items` 无 `UNIQUE(user_id, product_id)`；12.9 第 289 行只写 MySQL GROUP BY 较松
原文：`MySQL 在某些模式下较松，不要依赖这种宽松行为。`
问题等级：P2
问题类别：SQL / PRE
问题说明：两处方言/模型差异未对准动手引擎。(1) MiniShop 有 `UNIQUE(user_id, product_id)`，12.12 才能「避免再插一条」在 MiniShop 上变成 UNIQUE 失败，教学库则允许重复行。(2) **SQLite 同样允许 SELECT 非聚合列不出现在 GROUP BY**，并返回组内任意值。本章动手引擎是 SQLite，只点名 MySQL。
为什么有问题：学生在 sqlite3 里写非法标准 GROUP BY 会「跑通」，带到公司 PostgreSQL/MySQL ONLY_FULL_GROUP_BY 才爆。
依据：独立 `SELECT sku, stock, COUNT(*) … GROUP BY product_id` 在 SQLite 成功返回三行；`server.py` cart_items DDL 含 UNIQUE。
建议修改：12.9 补一句「SQLite 也宽松，教学上仍按标准写」；12.4 或 12B 补 MiniShop UNIQUE 对照。
推荐替换文本：`SQLite 和旧 MySQL 都可能让非聚合列不出现在 GROUP BY 里『跑通』，返回值不确定。练习里非聚合列必须进入 GROUP BY。MiniShop 购物车还有 UNIQUE(user_id, product_id)，同一用户同一商品不会有第二行。`

## ISSUE
ID：CH12-0013
文件：`chapters/12a-sql-query.md` 小练习；`chapters/12b-sql-write-and-minishop.md` 练习 7–8
章节：第 12 章
小节：小练习
精确位置：12A 练习 1–5；12B 练习 7–8
原文：练习 1–2 为识别/解释；练习 7「（查询含义见 12A 的 LEFT JOIN）」；练习 8「（无 ORDER BY 的 LIMIT 见 12A）」
问题等级：P2
问题类别：EX / PED
问题说明：12A 学习目标是写出 SELECT/JOIN，练习却停在解释，动手闭环要到 12B 书面包。12B 7–8 是 12A 知识点的延期作业，不是写操作题。
为什么有问题：拆章本为「避免还没学会 SELECT 就 DELETE」，上册练习没有强迫学生执行任何 SQL。
依据：练习 1–5 题干无「在 sqlite3 执行」；12B 工作实战才要求三条 SELECT。
建议修改：12A 至少一题要求贴出自己跑过的 JOIN 输出；把 7–8 收回 12A，12B 换事务/无 WHERE 的改输入题。
推荐替换文本：练习 4 改为「在教学库执行该 JOIN，把两行结果贴进 exercises/…」。

## ISSUE
ID：CH12-0014
文件：`chapters/12b-sql-write-and-minishop.md`
章节：第 12 章（下）
小节：12.12 INSERT
精确位置：第 41 行
原文：`审查中在 PRAGMA foreign_keys = ON 下插入不存在的用户，SQLite 报 FOREIGN KEY constraint failed。`
问题等级：P2
问题类别：SQL / PED
问题说明：外键失败是本章要学生亲眼看的结果，但没有可复制的 `INSERT … VALUES (99, …)`。
为什么有问题：「审查中」三字把证据留在作者机器上；学生只能背报错原文。
依据：独立执行 `INSERT INTO cart_items (user_id, product_id, qty) VALUES (99, 1, 1)`，FK ON 时 `IntegrityError: FOREIGN KEY constraint failed`；FK OFF（默认）时插入成功。
建议修改：给出完整失败句，并提醒关闭 FK 时幽灵用户能写进去。
推荐替换文本：
```sql
PRAGMA foreign_keys = ON;
INSERT INTO cart_items (user_id, product_id, qty) VALUES (99, 1, 1);
-- 期望：FOREIGN KEY constraint failed
```

## ISSUE
ID：CH12-0015
文件：`chapters/12a-sql-query.md`；`chapters/12b-sql-write-and-minishop.md`；`practice/12-sql-cross-check/`
章节：第 12 章全套
小节：跨节
精确位置：12.4 教学库；12A 工作实战 v1.0 证据；12-1 临时库
原文：多处分别警告「不要把教学库用户 3 当成管理员」，但从未用一张表收口三套环境。
问题等级：P2
问题类别：PED / PRE
问题说明：学生实际面对：(1) 12.4 自建文件，用户 3=`13800138002` NULL；(2) `project/minishop/data/minishop.sqlite`，用户 3=`13800138099` Admin，另有 `password_hash`/`role`/`orders`；(3) 实操 12-1 的临时库，schema 同 (2)，退出即删。
为什么有问题：【Beginner Friction】口头警告挡不住「旁边就有一个 sqlite 文件」。CH12-0003 是第一帧缺失，本条是环境地图缺失。
依据：副本 schema 与 12.4 DDL 对照；`practice/_minishop.py` 使用 `tempfile` + `server.reset_db`。
建议修改：12.4 后加「三套库对照」四行表。
推荐替换文本：见第 15 节。

## ISSUE
ID：CH12-0016
文件：`chapters/12a-sql-query.md`；`chapters/12b-sql-write-and-minishop.md`
章节：第 12 章
小节：岗位/完整性
精确位置：全章未出现 DBeaver/客户端、脱敏、只读账号、`.backup`/`mysqldump`
原文：（缺失）
问题等级：P2
问题类别：JOB
问题说明：【Job Reality Gap】初级测试入职后通常拿只读账号 + GUI 客户端查测试库，生产只读也要审批，手机号是 PII。本章安全纪律（授权、WHERE、事务）是对的，但没有「怎么连上、看见什么、不能复制什么」。
为什么有问题：面试能答「先 SELECT」，入职第一天不会装客户端、不会申请权限、可能把手机号贴进缺陷单。
依据：质量标准「工作中可用」；12B 只写「确认当前连接的是测试库」没有 how。
建议修改：12B 加一小节「了解」：只读账号、禁止把手机号完整贴到缺陷、备份优先于练习写。不必展开 GUI 截图。
推荐替换文本：`连库前问三句：这是测试库吗？我是只读还是可写？结果里有没有手机号要脱敏？sqlite3 练习文件可用 .backup 备份。`

## ISSUE
ID：CH12-0017
文件：`chapters/12b-sql-write-and-minishop.md`
章节：第 12 章（下）
小节：下一章预告
精确位置：第 365 行
原文：`第 13 章《接口测试》。`
问题等级：P2
问题类别：SEQ / PED
问题说明：拆章后 12B 对第 13 章零交接。NULL 图已经把第 13 章四态画完（CH12-0005），预告却不把「JOIN 核对交出去、JSON 四态下一章才主讲」说清。
为什么有问题：学生不知道第 13 章要用本章的 JOIN 去对接口 body，也不知道四态不该在本章找完整答案。
依据：质量标准第 20 项「能自然衔接下一章」。
建议修改：预告写一句：下一章用接口观察同一条购物车规则，SQL 仍是最终状态；缺字段/null/空串到第 13 章再拆。
推荐替换文本：`第 13 章《接口测试》：同一条 qty 规则改从 HTTP 看。JOIN 已经会了，下一章只多一条观察通道，不换业务规则。`

## 6. P3

## ISSUE
ID：CH12-0018
文件：`chapters/12a-sql-query.md` 12.1；`chapters/12b-sql-write-and-minishop.md` 工作实战
章节：第 12 章
小节：12.1；MiniShop 工作实战
精确位置：12a 第 44 行 `教学库 minishop_lab`；12b 第 211 行 `sqlite3 ~/minishop-sql-lab.sqlite`
原文：同上
问题等级：P3
问题类别：TERM
问题说明：库名/文件名两套。SQLite 也没有独立的 `CREATE DATABASE minishop_lab`。
建议修改：统一为 `~/minishop_lab.sqlite`，并写明「SQLite 一份文件就是一个库」。

## ISSUE
ID：CH12-0019
文件：`chapters/12a-sql-query.md`
章节：第 12 章（上）
小节：12.10 INNER JOIN 审查结果表
精确位置：第 302–315 行查询无 `ORDER BY`，结果表固定 001 再 002
原文：审查结果表行序
问题等级：P3
问题类别：SQL / PED
问题说明：12.8 刚教「没有 ORDER BY 的 LIMIT 不保证同一行」，INNER JOIN 又给固定行序。本次 SQLite 按 `cart_items` 插入序返回，属于巧合。
建议修改：查询加 `ORDER BY p.sku`，或注明行序不保证。

## ISSUE
ID：CH12-0020
文件：`chapters/12a-sql-query.md`
章节：第 12 章（上）
小节：参考资料
精确位置：第 467 行
原文：`- SQLite 文档`
问题等级：P3
问题类别：LINK
问题说明：无 URL。本章无任何 `http(s)://` 外链。
建议修改：给出 `https://www.sqlite.org/lang.html`（SELECT/DELETE/NULL）。

## ISSUE
ID：CH12-0021
文件：`chapters/12b-sql-write-and-minishop.md`
章节：第 12 章（下）
小节：12.13
精确位置：第 75–89 行 `AND stock >= 1`；第 89 行「把不要把库存改成离谱值写进条件」
原文：`UPDATE products SET stock = 9 WHERE sku = 'SKU-DEMO-001' AND stock >= 1;`
问题等级：P3
问题类别：SQL / PED
问题说明：条件只挡住当前 stock=0。若当前 stock=1，仍会把库存改成 9（变多）。独立复现：键盘 stock 先改为 1，再执行该模式，得到 9。
建议修改：改成 `SET stock = stock - 1 WHERE sku=… AND stock >= 1`，或删掉「离谱值」这句，只说「条件不能替代 SELECT」。

## ISSUE
ID：CH12-0022
文件：`chapters/12b-sql-write-and-minishop.md`
章节：第 12 章（下）
小节：12.14
精确位置：第 121 行
原文：`MySQL 上常是 DDL、难以当普通 DELETE 回滚`
问题等级：P3
问题类别：TERM / SQL
问题说明：MySQL 官方：TRUNCATE 是 DDL，**implicit commit，cannot be rolled back**。「难以」偏软。PostgreSQL「可放进事务 ROLLBACK」正确（官方：transaction-safe, rolled back if surrounding transaction does not commit）。
建议修改：MySQL 写成「会隐式提交，不能 ROLLBACK」。

## ISSUE
ID：CH12-0023
文件：`chapters/12a-sql-query.md`
章节：第 12 章（上）
小节：12.4 示例数据表
精确位置：第 143–147 行
原文：表头 `| cart_items | user_id | product_id | qty |`，第一列实际是 id。
问题等级：P3
问题类别：PED
问题说明：users 表头是 `users.id`，products 表头从 sku 起、不写 id，cart 表头用表名占 id 列。三张表示例格式不统一。
建议修改：第一列改为 `id`。

## ISSUE
ID：CH12-0024
文件：`chapters/12a-sql-query.md`
章节：第 12 章（上）
小节：12.3
精确位置：第 65 行「主键不能重复，也不能为 NULL」
原文：同上
问题等级：P3
问题类别：TERM
问题说明：对 SQL 标准与本章 `INTEGER PRIMARY KEY` 成立。SQLite 历史缺陷：非 INTEGER 的 PRIMARY KEY 允许 NULL；INTEGER PRIMARY KEY 插入 NULL 会自动生成 id（独立复现得到 id=4）。不必展开成长文，可加半句以免较真学生去试。
建议修改：`标准主键不能为 NULL。本章用 INTEGER PRIMARY KEY：插入 NULL 会自动生成 id，库里仍不会留下空主键。`

## ISSUE
ID：CH12-0025
文件：`chapters/12a-sql-query.md`；`chapters/12b-sql-write-and-minishop.md`
章节：第 12 章
小节：练习 10；12.10 LEFT JOIN 审查句
精确位置：练习 10 答案「回滚后应为 10」；12.10「SKU-DEMO-001 出现两次…SKU-DEMO-003 的 qty 为空」（未点名 002）
原文：同上
问题等级：P3
问题类别：ANS / PED
问题说明：练习 10 默认 12.4 种子且 12.13 已 ROLLBACK。若有人把 `stock=9` COMMIT 了，回滚一次 SET 9 仍是 9。LEFT JOIN 审查句省略键盘一行，不算错，但初学者会以为结果只有「两行 001 + 空 003」。
建议修改：答案写「若改前是 10，回滚后仍是 10」；LEFT JOIN 补「键盘一行 qty=2」。

## 7. 逐段问题

| 位置 | 结论 | 关联 |
| --- | --- | --- |
| 索引页 | 通过。qty=2 与 12-1 对齐；链接可解析 | |
| 12A 一句话核心 / 目标 / 前置 / 场景 | 通过。Linux 非硬前置正确 | CH12-0003 前置承诺 sqlite3 却无命令 |
| 12.1 数据库是什么 | 通过。表/行/列清楚；引擎列表恰当 | CH12-0018 库名 |
| 12.2 关系/非关系 | 通过。拒绝「关系型过时 / NoSQL 更快」 | |
| 12.3 主键外键 | 正文正确（含 SQLite PRAGMA、InnoDB、PG 默认强制） | CH12-0002 图；CH12-0024 NULL 细节 |
| 12.4 教学库 | DDL/INSERT/三张表数字自洽；002≠099 已写 | CH12-0001 图；CH12-0003 无第一帧；CH12-0023 表头 |
| 12.5 CRUD | 通过。Read 最多；写须授权。上册点名写操作名字可接受 | |
| 12.6 SELECT | 通过。单引号、少用 `*` | 独立：id=1 Tester A |
| 12.7 WHERE | 通过。AND/OR/LIKE/IN/BETWEEN 闭区间；注入仅了解且无载荷 | 独立结果见 §8 |
| 12.8 排序限制去重 | 通过。无 ORDER BY 的 LIMIT 警告正确 | |
| 12.9 聚合 GROUP BY HAVING | 数字全对 | CH12-0012 SQLite 也宽松 |
| 12.10 JOIN | 正文 INNER/LEFT、ON vs WHERE 正确 | CH12-0006 图；CH12-0019 行序 |
| 12.11 NULL | 正文正确 | CH12-0005 图跑题 |
| 12A 工作实战 | 验收行数字对，但是「打开文件」不是跑 SQL | CH12-0003 |
| 12A 常见错误 / 面试 / 清单 / 总结 | 通过。错误 3 把两套库分开 | |
| 12A 练习 1–5 | 答案与独立推导一致；4 未给 SQL | CH12-0011、CH12-0013 |
| 12B 场景导入 | 已区分 12-1=qty=2 与 qty=11 证据（旧错已修） | CH12-0008、CH12-0009 |
| 12.12 INSERT | 先 SELECT、授权库有 | CH12-0004、CH12-0014 |
| 12.13 UPDATE/DELETE | 安全流程 7 步完整；无 WHERE=事故 | CH12-0007 图；CH12-0021 |
| 12.14 DROP/TRUNCATE | SQLite 无 TRUNCATE 正确；PG 可回滚正确 | CH12-0022 MySQL 措辞 |
| 12.15 事务 | autocommit、不能替代权限、不能撤销已 COMMIT：正确 | |
| 12.16 MiniShop 验证 | qty>stock 零行正确；教学对照标明非简历缺陷 | CH12-0010 |
| 12B 工作实战书面包 | 结构好，完成标准可验证 | 依赖 12.4 库，见 CH12-0003 |
| 12B 常见错误 / 面试 / 清单 | 通过。无 WHERE、TRUNCATE、接口拒绝仍查库、未授权库 | |
| 12B 练习 6–10 | 独立答案一致 | CH12-0004 会让 7 在脏库上对不上 |
| 12B 预告 | 过薄 | CH12-0017 |
| sql-check.md / seed-join.txt | 与 v1.0 种子 JOIN 一致；第二节与 qty=10/11 独立复现一致 | CH12-0009 |
| practice 12-1 | 可跑、临时库、参数化 JOIN、验收 qty=2 | CH12-0008 |
| 测验 Q5–10 | 【ANSWER VERIFICATION】通过 | |

无 P0 级绝对化。未教授订单 status。未把 MiniShop 写成企业项目。

## 8. 代码问题

### 8.1 独立重跑：12.4 教学库（全部围栏 SQL）

建库语句按 12.4 原文执行。下列「教材声称」来自正文「审查结果」；「独立结果」来自本次 SQLite。

| # | 语句意图 | 独立结果 | 与教材 |
| --- | --- | --- | --- |
| 1 | `WHERE phone='13800138000'` | `(1, 13800138000, Tester A)` | 一致 |
| 2 | `stock>=5 AND stock<=10` | 001/10，002/5 | 正文未列全表，与数据一致 |
| 3 | `stock<5 OR sku='SKU-DEMO-001'` | 001/10，003/3 | 一致（推导） |
| 4 | `LIKE '%鼠标%'` | 无线鼠标 | 一致 |
| 5 | `IN ('001','002')` | 两行 | 一致 |
| 6 | `BETWEEN 3 AND 5` | 键盘 5、耳机 3 | 一致 |
| 7 | `ORDER BY stock DESC, sku ASC LIMIT 2` | 001/10，002/5 | 一致 |
| 8 | `DISTINCT user_id` | 1，2 | 一致 |
| 9 | `COUNT(*)` | 3 | 一致 |
| 10 | `COUNT(display_name)` | 2 | 一致 |
| 11 | `SUM(qty)` | 4 | 一致 |
| 12 | `AVG(stock)` | 6.0 | 一致 |
| 13 | `MIN/MAX(stock)` | 3 / 10 | 一致 |
| 14 | `GROUP BY product_id` | 商品1：2 行 qty 和 2；商品2：1 行 qty 和 2 | 一致 |
| 15 | `HAVING COUNT(*)>1` | 仅 product_id=1 | 一致 |
| 16 | INNER JOIN Tester A | 001 qty1 stock10；002 qty2 stock5 | 一致 |
| 17 | LEFT JOIN ORDER BY sku | 001/1，001/1，002/2，003/NULL | 一致 |
| 18 | `display_name = NULL` | 0 行 | 一致 |
| 19 | `display_name IS NULL` | 用户 3，`13800138002` | 一致 |
| 20 | `qty > stock` 种子 | 0 行 | 一致 |
| 21 | UPDATE stock=9 + ROLLBACK | 事务内 9，回滚后 10 | 一致 |
| 22 | DELETE id=2 + ROLLBACK | 事务内 0 行，回滚后 `(2,1,2)` | 一致 |
| 23 | UPDATE qty=11 + ROLLBACK | 事务内 11/10，回滚后 1/10 | 一致 |
| 24 | `INSERT user_id=99` FK ON | `FOREIGN KEY constraint failed` | 一致 |
| 25 | 同上 FK OFF（默认） | 插入成功，幽灵用户 | 正文警告正确 |
| 26 | `TRUNCATE TABLE products` | CLI 3.43.2 与 Python 3.50.4 均为 `near "TRUNCATE": syntax error` | 一致 |
| 27 | 无 WHERE `UPDATE products SET stock=0` | 三行库存全 0；ROLLBACK 恢复 | 正文「事故」判断正确 |

12.12 INSERT 无事务：见 CH12-0004。  
12.15 模板含注释，不作为可执行脚本，可接受。  
practice `JOIN_SQL` 使用 `?` 绑定，等价 INNER JOIN，独立跑 API=SQL=2。

### 8.2 MiniShop 只读副本

复制 `project/minishop/data/minishop.sqlite` 后查询（未写原库）：

- 用户：`13800138000` Tester A / `13800138001` Tester B / `13800138099` Admin
- 商品：鼠标 10、键盘 5、耳机 3
- 购物车：A 鼠标 1、A 键盘 2、B 鼠标 1
- Tester A JOIN：与 `sql-check.md`、`seed-join.txt` 第一节、12.10 审查表同构
- `qty>stock`：0 行
- schema 比 12.4 多 `password_hash`、`role`、`UNIQUE(user_id,product_id)`、`orders` 等

连接默认 `PRAGMA foreign_keys=0`，与正文「SQLite 默认不强制」一致。MiniShop `connect()` 会打开 FK。

### 8.3 实操 12-1（等价脚本，未写 practice 目录）

| 项 | 结果 |
| --- | --- |
| `POST /api/login` | 200，含 `token` |
| `POST /api/cart/items` qty=2 | 200 `{"sku":"SKU-DEMO-001","qty":2}` |
| JOIN | qty=2 stock=10 |
| match | True |
| 库路径 | 系统临时目录，非 `project/minishop/data/` |
| MiniShopLab 是否改教学库 | 对照实验：教学文件哈希不变 |

qty=10 允许、qty=11 拒绝后 JOIN：鼠标 10/10，键盘 2/5，不是 11。与 `seed-join.txt` 第二节一致。

### 8.4 语法/坏习惯（非 P0）

- 12.12 INSERT 无 BEGIN：CH12-0004
- INNER JOIN 无 ORDER BY：CH12-0019
- practice 使用 `?` 而 12A 未教占位符：可接受（学生只运行脚本），建议在 12.7 了解框加半句「应用应绑定变量，不要拼接」已有，可补 `?` 示例
- `JOIN` 与 `INNER JOIN` 在 SQLite 等价，practice 未写 INNER：P3 风格，不开独立单

## 9. 图片问题

五张 PNG 均用 `read_file` 打开；五张 HTML 源均读过。PNG 文案与 HTML 一致，不存在「源对图错」。

### IMG-CH12-001
文件：`chapters/assets/diagrams/ch12-pk-fk.png`（源 `ch12-pk-fk.html`）  
出现位置：12A 12.3  
图片主要内容：主键 vs 外键两卡片  
技术准确性：错误。`products.sku` 不是主键。外键只画了 `user_id→users.id`，缺 `product_id→products.id`  
与正文一致性：与 12.3 ASCII 图、12.4 DDL 冲突  
文字是否正确：否  
UI 是否过时：否（自制图）  
教学价值：命题句好（「认出哪一行 / 属于谁」），内容写错  
可读性：标题清晰，下方大片留白  
是否需要修改：是  
修改建议：主键改为三表 `id`；sku 标 UNIQUE  
最终结论：**REPLACE**（至少 MODIFY 主键句）

### IMG-CH12-002
文件：`ch12-tables.png` / `.html`  
出现位置：12A 12.4  
图片主要内容：三张表示意  
技术准确性：数据不完整且自称 MiniShop 种子  
与正文一致性：与紧随其后的 12.4 三表冲突  
文字是否正确：「MiniShop 种子数据如下」不正确  
教学价值：本应是全章最有用的图，当前会带错 COUNT/JOIN  
可读性：表格可读  
是否需要修改：是  
修改建议：改画 12.4 全量三表  
最终结论：**REPLACE**

### IMG-CH12-003
文件：`ch12-join.png` / `.html`  
出现位置：12A 12.10  
图片主要内容：三表碎片拼回一行  
技术准确性：这一行 INNER JOIN 正确  
与正文一致性：只覆盖 12.10 前半；不覆盖 LEFT JOIN  
文字是否正确：是  
教学价值：入门有用，难点缺席  
可读性：好  
是否需要修改：是（补 LEFT JOIN 或改现图）  
最终结论：**MODIFY**

### IMG-CH12-004
文件：`ch12-null.png` / `.html`  
出现位置：12A 12.11  
图片主要内容：NULL / 空串 / 缺字段  
技术准确性：JSON/SQL/Python 对照本身大体对；「字段存在但值为空」把 NULL 说成「空」易混  
与正文一致性：正文是用户 3 的 SQL NULL，图是第 13 章四态  
文字是否正确：提前引入 Python/JSON  
教学价值：对第 12 章低  
可读性：好  
是否需要修改：是  
最终结论：**REPLACE**

### IMG-CH12-005
文件：`ch12-select-first.png` / `.html`  
出现位置：12B 12.13  
图片主要内容：SELECT → 改数 → 再 SELECT  
技术准确性：授权库、带 WHERE 正确；第三步改讲 qty=11，脚注讲 TRUNCATE  
与正文一致性：与 12.13 安全流程不完全同构  
文字是否正确：第三步跑题  
教学价值：结构（三步）有价值  
可读性：好  
是否需要修改：是  
最终结论：**MODIFY**

缺图（最多记 2 个具体缺口）：LEFT JOIN 行复制；12.4 教学库全貌（现 `ch12-tables` 不能承担）。

## 10. 表格问题

| 表 | 位置 | 结论 |
| --- | --- | --- |
| 12.1 表/行/列/模式 | 12a | 通过。Schema/Database 对 SQLite 略简化，CH12-0018 |
| 12.4 users | 12a | 通过。NULL 用户 3 正确 |
| 12.4 products | 12a | 通过。无 id 列，与 cart 表头不统一，CH12-0023 |
| 12.4 cart_items | 12a | 表头第一列误标 `cart_items`，CH12-0023 |
| 12.5 CRUD | 12a | 通过 |
| 12.7 运算符 | 12a | 通过。BETWEEN 闭区间正确 |
| 12.10 JOIN 审查 | 12a | 数字对；无 ORDER BY，CH12-0019 |
| 12.11 NULL 写法 | 12a | 通过 |
| 12.14 DROP/TRUNCATE | 12b | 通过。SQLite 无 TRUNCATE 正确；MySQL 回滚措辞 CH12-0022 |

无表格数字与独立查询冲突（图不算表格）。

## 11. 练习与答案问题

方法：先按 12.4 数据与 SQL 语义独立作答，再读教材答案。

### 12A / 12B 小练习

| 题 | 独立答案 | 教材答案 | 判定 |
| --- | --- | --- | --- |
| 1 | 表如 `products`；行如一条商品；列如 `stock`。主键要唯一标识一行，NULL 无法标识 | 同 | 通过 |
| 2 | 共同问题：数据在哪、怎么读、怎么证明写入、怎么隔离。电商/后端测试仍大量用 SQL | 同 | 通过 |
| 3 | `= NULL` 为 UNKNOWN，WHERE 当假。应 `IS NULL` | 同 | 通过 |
| 4 | 三表 INNER JOIN，`WHERE u.phone='13800138000'`，鼠标 1/10、键盘 2/5 | 指向 12.10，未给 SQL | **答案不完整** CH12-0011，不是算错 |
| 5 | 3 与 2，用户 3 的 display_name 为 NULL | 同 | 通过 |
| 6 | B | B | 通过 |
| 7 | 两行=两个购物车行 JOIN 复制商品侧；空 qty=LEFT JOIN 无匹配；不能按两行删商品 | 同 | 通过；但若已跑 12.12，观察会变 CH12-0004 |
| 8 | 无 ORDER BY 的 LIMIT 行不确定，拿去写会改错行 | 同 | 通过 |
| 9 | 只能说明持久化没有 qty>stock；不能说明页面/接口没出现 11 | 同 | 通过 |
| 10 | 回滚后 10（前提改前是 10）；无 WHERE 更新整表，应 ROLLBACK 并汇报 | 同 | 通过；前提 CH12-0025 |

【ANSWER VERIFICATION FAILED】：无整题算错。练习 4 答案未满足「写出」。

### 阶段测验 4（仅第 12 章题 Q5–Q10）

独立作答（在对答案之前按本章与 MiniShop 种子推导）：

5. 主键唯一标识一行；外键引用另一表主键。`cart_items` 依赖 `users` 与 `products`。  
6. 先 SELECT 看影响范围。只在授权教学库改；未授权库连查也要谨慎。  
7. `SKU-DEMO-001` qty 1 stock 10；`SKU-DEMO-002` qty 2 stock 5。  
8. SQLite 无 TRUNCATE。回滚语义因引擎而异。  
9. SQL 里该 SKU 的 qty 不可以是 11。这不是实操 12-1（12-1 是合法 qty=2 的 JOIN）。  
10. C。

教材答案与上述一致。【ANSWER VERIFICATION】Q5–Q10 通过。  
Q1–Q4 为 Linux，非本章分母。

通过线「≥8/10 且 3、6、8 必过」对第 12 章意味着 Q6、Q8 必过，设计合理。

## 12. 初学者理解障碍

标记 【Beginner Friction】：

1. 三套库（教学文件 / MiniShop 主文件 / 12-1 临时库）只靠散文区分，12A 还把人领到 v1.0 证据文件旁边。CH12-0003、CH12-0015。
2. 12.4 第一张图少一行用户、少一件商品，和练习数字打架。CH12-0001。
3. 主键图写 sku，正文写 id。CH12-0002。
4. 12A 没有「打开 sqlite3 → 提示符变成 sqlite>」的第一帧，却要求会写 SELECT。
5. LEFT JOIN 空 qty 出现在系统讲 NULL 之前，靠一句「为空」过渡；图还不画复制行。
6. NULL 图突然出现 Python/JSON。CH12-0005。
7. 12.12 抄完 INSERT，练习 7 的「耳机为空」就没了。CH12-0004。
8. GROUP BY/HAVING 标 ⭐⭐⭐，对第一遍初级略重，但例子足够小，不单开 P1。

## 13. 岗位能力缺口

标记 【Job Reality Gap】：

1. 先 SELECT、授权库、事务、交叉验证：岗位对齐，是本章最大优点。
2. 缺：如何申请只读账号、GUI 客户端、执行计划/慢查询（了解即可）、PII 脱敏、备份后再练写。CH12-0016。
3. 购物车接口不减库存、下单才减：清单写混会误报缺陷。CH12-0010。
4. 12-1 只练绿路径，简历上容易写成「我用 SQL 发现了 UI 不一致」，实际没有这条证据。CH12-0008。
5. pytest 名被说成 SQL 交叉验证，入职后会高估自动化已经覆盖的通道。CH12-0009。

## 14. 建议删除内容

- `ch12-tables` 中「MiniShop 种子数据如下」这句（改，不删整图）。
- `ch12-null` 中第 13 章四态脚注与 Python `None` 主讲（改回 SQL）。
- `ch12-select-first` 第三步的 qty=11 与脚注 TRUNCATE（改回「再 SELECT」）。
- 12.12 不带事务的 INSERT 代码块（替换，不删 INSERT 节）。

不必删 GROUP BY/HAVING、不必删 12.2 NoSQL 了解段。

## 15. 建议新增内容

1. 12.4 后 `sqlite3` 第一帧 + 「不要打开 `project/minishop/data/minishop.sqlite`」。
2. 三套库对照表：

| 环境 | 用户 3 | 用途 |
| --- | --- | --- |
| 12.4 教学文件 | `13800138002` NULL | COUNT / IS NULL / 章内 SQL |
| MiniShop v1.0 主库 | `13800138099` Admin | 只读对照 `sql-check.md` |
| 实操 12-1 临时库 | 同 v1.0 schema | API=SQL=2，退出即删 |

3. LEFT JOIN 行复制图。
4. 可复制的 FK 失败 INSERT。
5. 12B 预告把 JOIN 交给第 13 章。
6. （了解）只读账号 / 手机号脱敏 / `.backup`。

## 16. 建议重写内容

### 补丁 1 — `ch12-tables`（对应 CH12-0001）

命题：「这是 12.4 教学库，不是 MiniShop v1.0 种子。」  
盒子：users 三行（含 `13800138002` display_name=NULL）；products 三行（耳机 stock 3）；cart_items 三行（A 鼠标 1、A 键盘 2、B 鼠标 1）。  
对照条：v1.0 用户 3 是 `13800138099` Admin。禁止拿本图对 `seed-join.txt` 做 COUNT。

### 补丁 2 — `ch12-pk-fk`（对应 CH12-0002）

主键：`users.id`、`products.id`、`cart_items.id`。`phone`/`sku` 是 UNIQUE。  
外键：`cart_items.user_id → users.id`，`cart_items.product_id → products.id`。

### 补丁 3 — 12A 第一帧（对应 CH12-0003）

插在 12.4 示例表之后：

```markdown
本机跟做（教学库，不要打开 MiniShop 主库）：

```bash
sqlite3 ~/minishop_lab.sqlite
```

提示符变成 `sqlite>` 后，把本节 `PRAGMA`～`INSERT` 整段贴进去。`.tables` 应看到 `users` `products` `cart_items`。

不要对 `project/minishop/data/minishop.sqlite` 跑这段 INSERT：那套表有 `password_hash`、`role`，用户 3 是 `13800138099`。后面的 `COUNT(*)` / `IS NULL` 只对这份教学库成立。
```

工作实战产出改为 `exercises/chapter-12a-join.md`，动作仍只读 `seed-join.txt` 第一节，并写明与教学库用户 3 不能对答案。

### 补丁 4 — INSERT 包进事务（对应 CH12-0004）

```sql
BEGIN;

SELECT id, user_id, product_id, qty
FROM cart_items
WHERE user_id = 1 AND product_id = 3;

INSERT INTO cart_items (user_id, product_id, qty)
VALUES (1, 3, 1);

SELECT id, user_id, product_id, qty
FROM cart_items
WHERE user_id = 1 AND product_id = 3;

ROLLBACK;
```

另附 FK 失败句（CH12-0014）。

### 补丁 5 — LEFT JOIN 图（对应 CH12-0006）

命题：「LEFT JOIN 可能把左表一行变成多行；空着的是没匹配，不是商品不存在。」  
结果：`SKU-DEMO-001` 两行、`SKU-DEMO-003` qty 空。禁止按「两行」DELETE 商品。

### 补丁 6 — 12-1 打印（对应 CH12-0008）

`页面说 2 件` → `接口返回 2，库里是不是 2？`  
末问 → `这两条通道对不上为什么仍是缺陷？这次有没有改生产库？`

## 17. 本章结论

**C 明显需要修改**

不能选 A/B：两张核心示意图事实错误（主键、种子表），12A 作为「写出 SELECT」的半章没有 sqlite 第一帧，INSERT 示例会污染后续 LEFT JOIN 练习。这些不是润色。

不能选 D/E：围栏内 SQL 经独立重跑全部成立；无 WHERE 警告充分；SQLite vs MySQL/PostgreSQL 的 TRUNCATE、FK、LIMIT、建表方言大体讲清；12-1 绿路径可跑且隔离临时库；002≠099、不编订单 status、不把 qty=11 教学对照当简历缺陷——这些已经是核心章该有的骨架。

发布建议：先改四张图（或两张 REPLACE + 一张 LEFT JOIN 新图 + select-first/null MODIFY）、补 12A 第一帧、把 INSERT 推进事务，再复评。目标 95 目前 73，差距主要在图和动手闭环，不在 SQL 算错。

旧审查分数（初审 97/99、v1.2.1 复评 93、教学审查 23/30）只作线索。旧单「12-1 绑 qty=11」「INSERT 节完全无先 SELECT」现行正文已修，本审计不重复开单。现行仍未修的是图与 12A 第一帧（与 2026-09-10 教学审查 P12-01/02 方向一致，结论由本次独立复跑支撑）。

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `README.md`（第 12 章行）
- `docs/COURSE_CONTROL.md`
- `docs/COURSE_OUTLINE_v1.2.md`（第 12 章主题）
- `docs/LEARNING.md`（Linux∥SQL）
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`、`practice/STATUS.md`、`practice/run.py`、`practice/_minishop.py`、`practice/_http.py`
- `exercises/README.md`
- `project/minishop/docs/PRD.md`（R-CART / 教学数据）
- `project/minishop/docs/sql-check.md`
- `project/minishop/evidence/sql/seed-join.txt`
- `project/minishop/server.py`（schema、cart、order 减库存）
- `project/minishop/tests/test_api.py`（`test_cart_qty_11_does_not_persist`）
- `project/minishop/docs/openapi.json`（`/api/login`、`/api/cart/items` 路径存在）
- `chapters/12-database-and-sql.md`
- `chapters/12a-sql-query.md`
- `chapters/12b-sql-write-and-minishop.md`
- `chapters/quizzes/README.md`、`chapters/quizzes/stage-4-ops.md`（第 12 章题）
- `practice/12-sql-cross-check/README.md`、`main.py`、`tests/test_lab.py`、`validation/latest.json`（只读）
- `chapters/assets/diagrams/ch12-{join,null,pk-fk,select-first,tables}.{png,html}`
- 线索（未照抄）：`reviews/chapter-12-review.md`、`reviews/_pedagogy-2026-09-10/ch12.md`、`reviews/_rereview-2026-09-09/stage-4-ch09-11-12.md`

未读其他章正文。

### 实际跑过的命令与结果摘要

- 复制 `project/minishop/data/minishop.sqlite` → `/tmp/minishop-audit-copy.sqlite` 后查询 schema/种子/JOIN（不写原库）。
- 按 12.4 在 `/tmp/ch12-teaching-lab*.sqlite` 重建教学库，逐条执行 SELECT/JOIN/聚合/NULL/事务/FK/无 WHERE UPDATE。
- `sqlite3` CLI：`TRUNCATE TABLE t;` → `near "TRUNCATE": syntax error`。
- 等价于 12-1 的 Python（`MiniShopLab` + `JOIN_SQL`）：API qty=2 且 SQL qty=2。**未**执行 `python3 practice/run.py 12-1`，以免写入 `practice/12-sql-cross-check/validation/latest.json`。
- 临时库 qty=10 允许、qty=11 拒绝后 JOIN 鼠标=10≠11。
- cart POST 前后 `products.stock` 仍为 10。
- MiniShopLab 隔离对照：教学主库哈希在 Lab 会话前后不变。
- 审计期间主库文件曾被**其他进程**改写（并行 Agent/本机服务），故种子结论一律以启动时副本与 MiniShopLab 临时库为准，不以审计结束时的主库文件为准。

### 外部核查

| 条目 | 来源 | 结论 |
| --- | --- | --- |
| SQLite 无 `TRUNCATE TABLE` | 本机 CLI 3.43.2 / Python 3.50.4 语法错误；database.guide 转述 SQLite DELETE truncate optimizer | 教材正确 |
| SQLite FK 默认关闭 | 本机默认 `PRAGMA foreign_keys=0`；sqlite.org/quirks.html「Foreign Key Enforcement Is Off By Default」 | 教材正确 |
| MySQL TRUNCATE 不能当普通 DML 回滚 | dev.mysql.com TRUNCATE TABLE：DDL、implicit commit、cannot be rolled back | 教材「难以回滚」偏软，CH12-0022 |
| PostgreSQL TRUNCATE 可 ROLLBACK | postgresql.org/docs/current/sql-truncate.html「transaction-safe…rolled back if the surrounding transaction does not commit」 | 教材正确 |
| SQLite PRIMARY KEY 可空的历史缺陷 | sqlite.org/quirks.html | 本章 INTEGER PK 不受害；CH12-0024 |
| sqlite.org 页面直接抓取 | `web_fetch` SSRF 拦截（解析到 198.18.1.186） | 改用 web_search 摘要 + 本机实验 |

无条目需要长期悬挂为【External Verification Required】。
