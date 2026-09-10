# RT_03 SQL / CODE / QUIZ（Second Pass Red Team）

- Agent：SECOND PASS Red Team（SQL 重推导 + 代码盲区 + 练习答案）
- 日期：2026-09-10
- 约束：不改教材。不采信 GLOBAL_03/04 数字，全部独立取证。12.12 INSERT 无事务第一轮已报，本文件不把它当主单。
- 引擎：sqlite3 CLI **3.43.2**；Python `sqlite3` 绑定 **3.50.4**；教学库 `/tmp/rt03/teach.sqlite` 与 `/tmp/rt03/cli.sqlite` 均按 12.4 正文自建，未打开 `project/minishop/data/minishop.sqlite` 当教学库。
- MiniShop：`server.reset_db` 临时库 + `ThreadingHTTPServer`；Postman 15 条用集合 JSON 原请求重放（query 按 Postman 对非 ASCII 编码）。
- mermaid：`mermaid@11` + jsdom，`mermaid.parse` 23/23。

---

## 0. 结论先写

12A/12B **围栏内审查数字全部能复现**，没有 COUNT/SUM/AVG/JOIN/NULL 算错，也没有 INNER/LEFT JOIN 写错连接键。新问题不在「3 与 2 算成 4」，而在三处第一轮 MASTER 总表没收或没写完的副作用：

1. **SQLite `PRAGMA foreign_keys` 按连接生效、不进文件**。12.12 审查句依赖 ON；学生第二天重开 `sqlite3 ~/minishop-sql-lab.sqlite` 默认 OFF，`user_id=99` 能插进去。
2. **下单扣库存、不读不改购物车**。12.16「`qty > stock` 应零行」只对静态教学种子成立。按仓库集合默认 Cookie 罐跑完 15 条后，教学 SKU-DEMO-001 会出现 **cart qty=10 / stock=9**。MASTER 收了「无凭证 401 被 Cookie 打成 201」，没收这条脏库。
3. **搜索对 ASCII 做 `lower()` 包含匹配**；注册路径 **确实不自动登录**（与 PRD/前端一致）。

阶段测验 70 题：与标准答案整题冲突仍是测验 7 第 8 题（G04-0004，本轮独立确认）。G04 **漏网**：测验 3 第 5 题把 MiniShop「无 token 下单」写成 401，未区分无凭证 vs 无 Bearer。

章内 213 题：没有发现 G04-0001～0006 之外的新 【ANSWER VERIFICATION FAILED】。

mermaid 23 张语法全部合法。G03 覆盖表写了 252 围栏，但 mermaid 没有 parse。

---

## 1. Coverage（本轮实际做了什么）

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 12A ` ```sql ` 围栏 | 13 | 13（建库 + 每条 SELECT/聚合/JOIN/NULL） | 0 |
| 12B ` ```sql ` 围栏 | 6 | 6（INSERT / UPDATE / DELETE / 事务模板 / qty>stock / qty=11 对照） | 0 |
| 正文「审查结果」数字句 | 见 §2 表 | 全部用 CLI + Python 各跑一遍 | 0 |
| `practice/_http.py` `_minishop.py` | 2 | 通读；Lab 起临时库打行为矩阵 | 0 |
| `project/minishop/server.py` 注册/搜索/购物车/下单 | 4 个 handler | HTTP 实打 | 0 |
| `frontend/app.js` + `index.html` 下单/注册/搜索表单 | 全文件 | 读 + 对照 handler | 0 |
| Postman 集合请求 | **15** | 逐条重放 + 逐条对照 `pm.expect` 与 `server.py` | 0 |
| 阶段测验 | 70 | 先读题独立作答，再对文末答案 | 0 |
| 章内小练习 | 213 | 抽核 G04 已判 FAIL 的 6 道 + 12/13/14/16/19 相关；未发现新整题写反 | 未把 213 道解答全文贴进本文件 |
| mermaid 围栏 | 23 | `mermaid.parse` 全过 | 0 |

未做：Postman GUI Runner、Newman 二进制、浏览器真实点击（前端行为按源码 + 同等 HTTP 推断）。

---

## 2. SQL 重跑：声称 vs 实测

教学库按 12.4 原文插入：用户 3 行（用户 3 `display_name` NULL）、商品 3、购物车 3（A: 鼠标 1 / 键盘 2；B: 鼠标 1）。

| 正文位置 | 声称 | sqlite3 CLI / Python | 判定 |
| --- | --- | --- | --- |
| 12.6 `WHERE phone` | `id=1`，Tester A | 1 行，相同 | MATCH |
| 12.7 `BETWEEN 3 AND 5` | 键盘 stock=5、耳机 stock=3 | 2 行，001 不在 | MATCH |
| 12.8 `ORDER BY stock DESC, sku ASC LIMIT 2` | 先 001（10）再 002（5） | 相同 | MATCH |
| 12.8 `DISTINCT user_id` | 1 和 2 | `(1),(2)` | MATCH |
| 12.9 `COUNT(*)` / `COUNT(display_name)` | 3 / 2 | 3 / 2 | MATCH |
| 12.9 `SUM(qty)` | 4 | 4（1+2+1） | MATCH |
| 12.9 `AVG(stock)` | 6.0 | 6.0（(10+5+3)/3） | MATCH |
| 12.9 MIN/MAX | 3 / 10 | 3 / 10 | MATCH |
| 12.9 `GROUP BY product_id` | 商品 1：2 行合计 qty 2；商品 2：1 行合计 qty 2 | `(1,2,2),(2,1,2)` | MATCH |
| 12.9 `HAVING COUNT(*)>1` | 只留商品 1 | 1 行 `product_id=1` | MATCH |
| 12.10 INNER JOIN Tester A | 001 qty1 stock10；002 qty2 stock5 | 2 行，连接键 `c.product_id=p.id` 正确 | MATCH |
| 12.10 LEFT JOIN | 001 出现两次；003 的 qty 为空 | **4 行**：001/1，001/1，002/2，003/NULL | 数字不反；总行数正文没写（第一轮 CH12-0025 P3） |
| 12.11 `= NULL` | 零行 | 0 | MATCH |
| 12.11 `IS NULL` | 用户 3，`13800138002` | 1 行 | MATCH |
| 12.16 `qty > stock`（种子） | 零行 | 0 | MATCH（仅静态种子） |
| 12.13 UPDATE stock=9 + ROLLBACK | 事务内 9，回滚 10 | 相同 | MATCH |
| 12.13 DELETE id=2 + ROLLBACK | 回滚后 id=2 qty=2 仍在 | 相同 | MATCH |
| 12.16 事务内 qty=11 | `qty=11, stock=10` | `id=1` 正是鼠标行 | MATCH |
| 12.14 `TRUNCATE` | SQLite 无此语句 | `near "TRUNCATE": syntax error` | MATCH |
| 同连接 `PRAGMA foreign_keys=ON` 插 `user_id=99` | `FOREIGN KEY constraint failed` | IntegrityError | MATCH |
| **新连接、不写 PRAGMA** 再插 99 | 正文未声称 | CLI `PRAGMA foreign_keys` = **0**，插入成功 id=4 | 见 RT03-0001 |
| 抄 12.12 INSERT 耳机、无 ROLLBACK | 第一轮已报 | LEFT JOIN 003 的 qty 变为 1 | 独立复现；**不新开主单** |

12.7 其余 WHERE（AND / OR / LIKE / IN）正文没有给行数。实测：AND 两行（001 与 002）；OR 两行（001 与 003，键盘 stock=5 不满足 `< 5`）；LIKE `%鼠标%` 一行；IN 两行。无算错。

JOIN 条件：`c.user_id = u.id` 且 `c.product_id = p.id`，**没有**把 `product_id` 对 `sku`。SQL 正文本身是对的。

---

## 3. ISSUE

### ISSUE

ID：RT03-0001  
文件：`chapters/12b-sql-write-and-minishop.md`；`chapters/12a-sql-query.md`  
章节：第 12 章  
小节：12.3 / 12.4 / 12.12  
精确位置：12a L75–76「SQLite 默认不强制外键，需要 `PRAGMA foreign_keys = ON;`」；12.4 建库围栏第一句 PRAGMA；12b L41「审查中在 PRAGMA foreign_keys = ON 下插入不存在的用户」  
原文：审查中 FK ON 时报 `FOREIGN KEY constraint failed`。  
问题等级：P2  
问题类别：SQL / PRE / PED  
问题说明：`PRAGMA foreign_keys` **按连接**有效，不写入 sqlite 文件。12.4 脚本在**同一次** `sqlite3` 会话里打开约束；12B 工作实战是「进入后执行 12.4」，但学生按「昨天建好的 `~/minishop-sql-lab.sqlite`」直接打开时，默认是 OFF。本轮：新 `sqlite3 /tmp/rt03/cli.sqlite` → `PRAGMA foreign_keys` 返回 0 → `INSERT … user_id=99` **成功**，行 id=4。  
为什么有问题：12.12 把外键失败写成审查事实，可复制块却没有 99 那一行，也没有「每次打开都要 PRAGMA」。学生会看到幽灵用户插进去，以为外键「课上说的和引擎不一样」。第一轮 CH12-0014 只报「没有可复制失败句」；**连接级不持久**是本轮新证据。  
依据：SQLite 文档：foreign_keys setting is not persistent；本机 CLI 3.43.2 重开实验。MiniShop `server.connect()` 每次 `PRAGMA foreign_keys=ON`，与教学 CLI 不是同一纪律。  
建议修改：12.4 / 12.12 / 工作实战都写「每次打开教学文件先 `PRAGMA foreign_keys=ON;`」；给出 `VALUES (99,1,1)` 失败句。  
推荐替换文本：`SQLite 的外键开关不保存在文件里。每次 sqlite3 打开教学库先执行 PRAGMA foreign_keys=ON; 再测 user_id=99。`

---

### ISSUE

ID：RT03-0002  
文件：`chapters/12b-sql-write-and-minishop.md`；`project/minishop/server.py`；`project/minishop/frontend/app.js`；`project/minishop/postman/MiniShop.postman_collection.json`；`project/minishop/docs/PRD.md`  
章节：第 12 / 14 / 19 章 + MiniShop  
小节：12.16 验证清单；R-ORDER；集合「改数量-等于库存」→「创建订单」→「无凭证创建」  
精确位置：12b L189–192「接口成功后库存有没有少、购物车有没有多」；`server.py` `_cart_items` 不改 `products.stock`；`_create_order` L454–470 扣库存、不读 `cart_items`；`app.js` L97–112 下单表单独立 sku/qty，成功后不 `refreshCart`/`refreshProducts`；集合无凭证 Body `{"sku":"SKU-DEMO-001","qty":1}`  
原文：12.16「当前示例数据应**零行**」；14.7「无凭证创建 → 401」；PRD 范围并列购物车数量与创建订单，R-ORDER 不写订单是否来自购物车。  
问题等级：P1  
问题类别：SQL / MiniShop / CODE / TEST  
问题说明：独立 HTTP（临时库）：

| 步骤 | 观察 |
| --- | --- |
| `POST /api/cart/items` sku=001 qty=2 | 200；`products.stock` **仍为 10** |
| `POST /api/orders` sku=001 qty=1 | 201；stock **变为 9**；购物车仍 qty=2，**不被清空** |
| 用户 B 购物车只有 001，却 `POST /api/orders` sku=002 qty=1 | **201**（下单不读购物车） |
| 注册 201 | Body 仅 `result`+`phone`，**无 token、无 Set-Cookie**；随后无凭证 `GET /api/cart` → 401 |
| 集合顺序 + **默认 Cookie 罐** | 改数量把 001 写成 qty=10 后，「无凭证创建」001 qty=1 变成 Tester A 的 **201**；SQL `qty>stock` 得到 **(10, 9, SKU-DEMO-001)** |
| 集合 + `disableCookies` | 无凭证 401；001 库存仍 10；003 因「创建订单」变为 2；`qty>stock` 仍 0 |

前端：购物车表单与下单表单并列，默认都是 `SKU-DEMO-001` / 1。下单成功只写 `订单 id=`，商品列表和购物车 DOM 不刷新。页面仍可能显示 qty=10、库存 10，库里已经 9。  
为什么有问题：12.16 把「零行」写成当前数据的巡检结论。学生若按第 14 章导入集合跑 Runner（正文允许的 Cookie 默认行为），再把 12.16 的 JOIN 打到同一 MiniShop 库，会看到超卖行，并误报「页面把 11 写进库了」——实际是 **下单扣库存、购物车仍 10**。MASTER 有 M-P1-18（401→201），没有这条脏库；CH12-0010 / CH19-0017 / G06-0004 第一轮写过「购物车不扣库存 / 下单不经过购物车」，总表未收，且没有把官方 15 条跑完后的 `qty>stock=(10,9)` 测出来。  
依据：本轮临时库 HTTP + 集合重放；`server.py` L400–413 vs L452–470；`app.js` L83–112；集合 L188–207。  
建议修改：R-ORDER 写明「v1.0 直接 POST sku+qty，不读取、不修改 cart_items，这是教学简化」；12.16 清单拆成「改购物车：stock 不变、qty≤stock」「下单成功：stock 减少、购物车行仍在」；无凭证请求 `disableCookies`，Body 不要用刚写成 qty=10 的 SKU。  
推荐替换文本：`改购物车成功只改 cart_items.qty，products.stock 不变。创建订单按 Body 的 sku/qty 扣库存，不读购物车。种子上 qty>stock 为零行；若先把购物车写成 10 再下单 1 件，巡检会变成有行，这不是 qty=11 缺陷。`

【对照第一轮】CH12-0010 P2、CH19-0017 P2、G06-0004 P2、G03-0001 P1。本单升级理由：官方集合在默认 Cookie 罐下会**制造** 12.16 反例，不只是文案不精确。

---

### ISSUE

ID：RT03-0003  
文件：`project/minishop/postman/MiniShop.postman_collection.json`；`chapters/14-postman.md`  
章节：第 14 章 + MiniShop 资产  
小节：集合 15 条 Tests；14.5 正文脚本；14.7 对照表  
精确位置：集合 L11–16、L131–133、L145–147、L178–186、L199–207、L211–217  
原文：14.7「共 15 个请求」；无凭证 401；越权 403；qty=1/10 → 200。  
问题等级：P2  
问题类别：CODE / TEST / HTTP  
问题说明：G03 覆盖写了集合 15 条 JSON 合法，但执行矩阵没有把 **15 条 `pm.expect` 逐条对上 server**。本轮逐条（密码当前值 `Test1234`，query `鼠标` 按客户端编码）：

| # | 名称 | 集合断言 | 与 server（无 Cookie 罐） | 与默认 Cookie 罐 |
| --- | --- | --- | --- | --- |
| 1 | 注册-合法 | 201；`phone==newPhone`；无 `token` | PASS；也无 Set-Cookie | 同 |
| 2 | 注册-占用 | 409 | PASS（`phone taken`，脚本不断言字符串） | 同 |
| 3 | 注册-非法 | 400；`invalid phone` | PASS（`1380013800` 十位） | 同 |
| 4 | 搜索商品 | 200；`items` 数组；`items[0].sku==SKU-DEMO-001` | PASS（`keyword=鼠标` 命中一件） | 同 |
| 5 | 空搜索-BUG-001 | 400 或 `items.length===0` | **FAIL**（200 / 3 件，BUG-001，正文已声明） | 同 |
| 6–8 | 三登录 | 200 + 写 token；管理员 `role==admin`；登录-正确无 `status` | PASS | 同 |
| 9 | 改数量-合法 | **只** `status==200` | 实际 Body `{sku,qty:1}`，脚本不断言 qty | 同 |
| 10 | 改数量-等于库存 | 只 200 | 200 `{qty:10}` | 同 |
| 11 | 改数量-超库存 | 400；`qty exceeds stock` | PASS | 同 |
| 12 | 创建订单 | 201；`id` 为字符串；无 `status`；`set lastOrderId` | PASS（sku=003 qty=1，stock 3→2） | 同 |
| 13 | 无凭证创建 | 401 | PASS（401 `unauthorized`） | **HTTP 201**（G03-0001）且扣 001 库存（RT03-0002） |
| 14 | 越权-他人订单 | 403；**另** `json.id not.eql lastOrderId` | 403 `{"error":"forbidden"}`，**没有 `id`**。Chai 里 `undefined !== "ord-…"` 为真，断言**空转通过** | 同 |
| 15 | 越权-管理员 | 403 | PASS | 同 |

14.5 正文「超过库存」脚本只 `to.have.property("error")`，集合才 `eql('qty exceeds stock')`。14.5 列表脚本只断言数组（mouse 空数组也会绿）第一轮已报，此处不重复当主因。  
注册-合法**不断言**无 `Set-Cookie`：R-REG「不自动登录」若被改成发会话 Cookie、仍不回 token，这条集合仍然绿。当前实现确实不发 Cookie（本轮确认），缺口在断言而不是实现。  
为什么有问题：第 14 章完成标准是「导入并跑通仓库集合」。学生看到越权绿，会以为已经断言「响应里不是那张订单」；其实只证明了 403，`id` 检查对当前 Body 是空操作。改数量两条在服务端误返回 200 但 qty 不是 1/10 时也会绿。  
依据：集合 JSON Tests；本轮 15 条重放；`_get_order` L492–494 他人 403 只回 `{"error":"forbidden"}`。  
建议修改：越权改为 `pm.expect(json).to.not.have.property('id')` 且 `error === 'forbidden'`；改数量断言 Body `qty`；注册断言无 `token` **且** 响应头无 `Set-Cookie`；无凭证 `disableCookies`。  
推荐替换文本：`403 的 Body 是 {"error":"forbidden"}，不要用 json.id 去比较订单号——没有这个字段时 Chai 也会绿。`

【对照第一轮】G03-0001 覆盖第 13 条 Cookie；**未**覆盖第 14 条空转、第 9/10 条弱断言、第 1 条不检查 Cookie。

---

### ISSUE

ID：RT03-0004  
文件：`project/minishop/server.py`；`chapters/08a-web-page-testing.md`；`project/minishop/docs/PRD.md`；`chapters/13-api-testing.md`  
章节：第 8 / 12 / 13 章 + MiniShop  
小节：8.6 搜索表；R-SEARCH；`_get_products`  
精确位置：`server.py` L269–271 `key = keyword.lower()` 后对 `name.lower()` / `sku.lower()` 做包含匹配；08a L211「大小写与中英文：按需求，不要假设一定忽略大小写」；R-SEARCH 只冻结空/空白关键字  
原文：见上。13.4 已写搜 `mouse` 会空（中英文，不是大小写）。  
问题等级：P2  
问题类别：MiniShop / TEST / PED  
问题说明：本轮 `GET /api/products?keyword=`：

| keyword | n | 命中 |
| --- | ---: | --- |
| `鼠标` / `无线` | 1 | 001 |
| `mouse` / `MOUSE` | 0 | 与「无线鼠标」无公共子串 |
| `SKU-DEMO-001` / `sku-demo-001` / `Sku-Demo-001` | 1 | ASCII **忽略大小写** |
| 空白 / 缺省 | 3 | BUG-001 |

教材 08.6 正确警告「不要假设」；PRD **没有**冻结大小写。实现已经是大小写不敏感的包含匹配。学生按 08.6 设计「SKU-demo-001 应无结果」会得到 1 件，不知该报缺陷还是记实际行为。SQL `LIKE '%sku-demo-001%'` 在 SQLite 对 ASCII 也不敏感（本轮 1 行），与 12.7「查询部分下面通用」是另一条方言（G02-0003 已报 LIKE；**搜索 API 的 lower()** 第一轮 MASTER 未列）。  
为什么有问题：搜索是主路径。大小写是测试点表里有、契约里无、实现里有的第三套口径。  
依据：HTTP 矩阵；`app.js` L59–66 会 `encodeURIComponent`，大小写原样送出。  
建议修改：R-SEARCH 补一句「当前实现对 name/sku 做大小写不敏感包含匹配；空/空白仍按 BUG-001」；或 8.6 MiniShop 行写「测到 `sku-demo-001` 能命中，记实际行为，不要当缺陷」。  
推荐替换文本：`MiniShop 搜索：非空关键字对商品名和 SKU 做小写包含。mouse 不是鼠标。SKU 的大小写都能命中。空/空白仍返回全量（BUG-001）。`

---

### ISSUE

ID：RT03-0005  
文件：`chapters/quizzes/stage-3-web.md`  
章节：阶段测验 3  
小节：第 5 题（401 vs 403）  
精确位置：答案「401 未通过认证（无 token 下单）；403 … `/api/admin/*`」  
原文：见上。  
问题等级：P2  
问题类别：ANS / MiniShop / HTTP  
问题说明：【ANSWER VERIFICATION FAILED】（相对 MiniShop 实现，不是相对 RFC 定义）。独立答案：401 = 没有可接受的凭证；403 = 已识别但无权限。MiniShop 例应写成：**无 Bearer 且无 Cookie** 下单 → 401；仅缺 Authorization、浏览器/Postman 仍带 `minishop_session` → **201**；用户 B 读 A 的订单、普通用户打 `/api/admin/*` → 403。教材把「无 token 下单」直接钉成 401。G04 矩阵该题「过 / server.py 印证」，只核了无任何凭证的路径。  
为什么有问题：同卷 Q1/Q2 刚强调 Cookie 会自动带上、不能三选一。Q5 例题又用「无 token」等价 401，和第 8/14 章 Cookie 回退同一把尺子。学生按标准答案设计「去掉 Authorization 就该 401」会在 Runner 里看到 201。  
依据：本轮仅 Cookie `POST /api/orders` → 201；无凭证 → 401；`_token()` 先 Bearer 再 Cookie。测验 5 第 5 题只谈 Session/autouse，同样没提 Cookie 罐（口径缺口，不升本单）。  
建议修改：例改为「不带 Authorization **也不带** Cookie 时下单 401」。  
推荐替换文本：`401：没有任何凭证（无 Bearer、无会话 Cookie）时下单。403：已登录的用户 B 读 A 的订单，或普通用户打 /api/admin/orders。不要把「请求里没写 Bearer」当成 401——Cookie 罐会让它变成 201。`

【对照第一轮】G04-0004 是测验 7 Q8 结构冲突，本轮独立确认仍成立（见 §5）。G04 **未**把测验 3 Q5 标成答案问题。

---

### ISSUE

ID：RT03-0006  
文件：`chapters/12a-sql-query.md`  
章节：第 12 章（上）  
小节：12.9  
精确位置：L289「出现在 SELECT 中的非聚合列，一般必须出现在 GROUP BY 中。MySQL 在某些模式下较松，不要依赖这种宽松行为。」  
原文：见上。  
问题等级：P2  
问题类别：SQL / PRE  
问题说明：动手引擎是 SQLite。本轮：

```sql
SELECT sku, stock, COUNT(*) FROM products GROUP BY stock;
-- 3 行，非法标准 SQL，SQLite 接受
SELECT product_id, qty, COUNT(*) FROM cart_items GROUP BY product_id;
-- 商品 1 的 qty 取组内任意值（本种子两行都是 1，看不出「任意」）
```

正文只点名 MySQL。学生在 sqlite3 里「跑通」非标准 GROUP BY，带到 PostgreSQL / `ONLY_FULL_GROUP_BY` 才爆。12.9 示例本身只 SELECT 了分组列和聚合，**示例不依赖宽松模式**；缺口是声明。  
为什么有问题：用户明确要求查「GROUP BY 与 SQLite 宽松模式未声明」。数字没有算错，但方言警告写错对象。  
依据：CLI 3.43.2 上述两条成功返回；SQLite 文档 GROUP BY 可比标准宽松。  
建议修改：改成「SQLite 和旧 MySQL 都可能让非聚合列不进 GROUP BY 就跑通，返回值不确定。练习仍按标准写。」  
推荐替换文本：`教学库是 SQLite：非法标准的 GROUP BY 常常仍有结果。不要用「能跑」证明写法可移植。`

【对照第一轮】CH12-0012 已写 SQLite 宽松 + MiniShop `UNIQUE(user_id,product_id)`。MASTER P1 总表未收。本轮独立复现成立，另开 RT03 号供第二轮合并，不升 P1。

---

## 4. 行为核对（教材声称 vs 实现）— 第一轮 MASTER 未列的四问

| 问 | 实现 | 教材主要声称 | MASTER 总表 | 本轮 |
| --- | --- | --- | --- | --- |
| 下单是否扣库存 | `_create_order` `stock = stock - ?`，成功则减 | 12.16 清单把「库存有没有少」写成接口成功后的通用检查，未钉死是订单接口 | 未列 | **扣**；购物车接口**不扣**（RT03-0002） |
| 下单是否读购物车 | 只读 Body `sku`+`qty`；不读、不改 `cart_items` | PRD 范围并列两功能；页面两套表单；未写「不是结算」 | 未列（章 19 / G06 有 P2） | **不读**（RT03-0002） |
| 注册是否自动登录 | 201 无 token、无 Set-Cookie；`app.js`「未自动登录」且不写 `sessionStorage` | R-REG、测验 6 Q8、多章一致 | 未当问题（声称与实现一致） | **核对通过** |
| 搜索大小写 | `keyword.lower() in name/sku.lower()` | 08.6 不要假设；R-SEARCH 不提；`mouse` 空是中英文 | 只收了 `keyword=mouse` 空列表（M-P1-13） | ASCII SKU 忽略大小写（RT03-0004） |

`practice/_http.py`：标准库 `urlopen`，**没有** Cookie 罐。practice 的 401/403 不会被会话 Cookie 污染。这与集合默认行为不同，不是缺陷。  
`practice/_minishop.py`：临时库 + `reset_db`，不碰教学 `data/`。与 12-1 隔离声称一致。

---

## 5. 测验 70 + 章内 213

方法：先读 `chapters/quizzes/stage-*.md` 题干作答，再对文末答案。不把 G04 矩阵当答案。

### 5.1 阶段测验：只报冲突或 G04 漏网

| 卷 | 题 | 独立答案要点 | 教材答案 | 本轮 |
| --- | --- | --- | --- | --- |
| 1 Q4 | V 模型对应 | 系统需求↔系统测试；系统设计/架构↔集成（第 2 章 L132–141 同句） | 同 | 过 |
| 3 Q5 | 401/403 MiniShop 例 | 无任何凭证 401；Cookie 回退 201；他人订单/admin 403 | 「无 token 下单」=401 | **RT03-0005** G04 漏 |
| 3 Q9 | 登录两类凭证 | token + Set-Cookie；后续 Cookie 可并存 | 「后续以 Bearer 为准」 | 与 PRD R-AUTH 字面同向；实现仍认 Cookie。不升整题 FAIL |
| 4 Q7 | JOIN 两行 | 001 qty1 stock10；002 qty2 stock5（v1.0 种子） | 同 | 过；与 12.4 用户 3 不是同一库 |
| 5 Q5 | 401 夹在已登录 Session | 测不到 401；也不要共用 Cookie 罐 | 只写 Session/token | 方向对，漏 Cookie。不升 FAIL |
| 6 Q5 | qty=10/11 vs「第 16 章教学服务」 | 以 PRD 为准 10 允许 11 拒绝 | 「早期教学服务往往只让 qty=1」 | G04-0010 已报题干过时，不重复 |
| 6 Q8 | 注册自动登录？ | 不会。201 无 token、无 Cookie | R-REG 201 无 token | **过**（实现印证） |
| 7 Q1 | 五段 | 结论→原理→场景→示例→边界 | 同 | 过 |
| 7 Q8 | 争执用什么结构 | 应回五段（与 Q1、第 20 章强制结构同一把尺子） | 「结论-场景-你做了什么-结果-你学到什么」 | **独立确认 G04-0004**：【ANSWER VERIFICATION FAILED】。不新开 RT03 号 |

其余 70−9 题：独立方向与教材同向，不把 G04 已列的口径/难度项再写一遍。

未发现「GET 不安全 POST 安全」「三选一」「P0 全球统一」「没 Bug=没 Bug」「测试必须等开发写完」「ROI 永远最高」被写成正确答案。

### 5.2 章内 213：G04 漏网检查

抽核并重做与 SQL/代码相关的 12A 1–5、12B 6–10、13、14、16B 8、19。结论：

| 已有 G04 | 本轮 |
| --- | --- |
| G04-0001 第 3 章冒烟「加入购物车」 | 独立仍判教材答案错；不重复开单 |
| G04-0002 06B 练习 10 对象写成 qty=11 | 独立仍判对象错 |
| G04-0003 第 20 章「库存 11」用词 | 独立仍判用词错 |
| G04-0005 12A 练习 4 答案没写出 SQL | 独立 JOIN 两行数字对，答案不完整 |
| G04-0006 16B 练习 8 漏 201 / 无 status | 独立仍判漏项 |

**没有**发现第 7 条整题/关键对象写反。12B 练习 7 依赖「003 qty 为空」：若学生先执行了 12.12 无事务 INSERT，该答案在**同一文件库**上不成立——这是 INSERT 污染的后果（CH12-0004），不是练习答案本身写错种子。

---

## 6. mermaid（第一轮未 parse）

`chapters/*.md` 共 23 个 ` ```mermaid ` 围栏（与 UNIT_INVENTORY 一致）。G03 执行矩阵 E56 是 `node --check` 对 **javascript** 围栏；mermaid 不在 JS 语法检查范围内。

本轮 `mermaid@11` `parse`：

| 文件 | 结果 |
| --- | --- |
| 01 / 02×2 / 03 / 05×2（含 `stateDiagram-v2` 中文状态名、`D{AND}`）/ 06a / 07×3 / 08b / 09a×2 / 09b / 10 / 13 / 14 / 17（`flowchart BT` 链式 `UNIT --> API --> UI`）/ 18 / 19 / 20 / 21 / 22 | **23 OK / 0 FAIL** |

无语法非法。02 的 `D -.每日检查进展并调整计划.-> D` 自环虚线合法。不因此开 ISSUE。

---

## 7. 独立复现、不新开主单

| 现象 | 本轮 | 第一轮 | 处理 |
| --- | --- | --- | --- |
| 12.12 INSERT 耳机无 ROLLBACK，LEFT JOIN 003 不再空 | 复现 qty=1 | CH12-0004、G03-0009、M-P1-15 | 按任务要求不重复当主单 |
| 无凭证 + Cookie 罐 → 201 | 复现 | G03-0001、M-P1-18 | 本轮只追加脏库（RT03-0002） |
| `keyword=mouse` 空数组 | 复现 | M-P1-13 | 不重复；大小写另开 RT03-0004 |
| 测验 7 Q8 五段 vs STAR 变体 | 独立仍冲突 | G04-0004 | §5 确认 |
| MiniShop `UNIQUE(user_id,product_id)` vs 12.4 教学表无 UNIQUE | 对照 DDL 属实 | CH12-0012 后半 | 并入 RT03-0006 的方言项，不再拆单 |

---

## 8. 建议总控怎么收

- **P1 只收 RT03-0002**（下单扣库存 / 不读购物车 / 官方集合默认跑完后 `qty>stock` 不再是零行）。不要再单独升 PRAGMA 或 GROUP BY。
- RT03-0001、0003、0004、0005、0006 → P2。0005 是 G04 漏网，测验卷与 Cookie 回退同一把尺子。
- mermaid 无单。注册不自动登录无单。
- 12A/12B 审查数字 **不必因「SQL 算错」返工**；要返工的是 12.16 巡检前提、12.12 外键开关、以及集合无凭证请求。
