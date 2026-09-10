# VERIFY_IMAGES

审计员：Verification-Agent-04（图片）  
日期：2026-09-10  
范围：FIX_PLAN 点名七组示意图（html + png）对照对应章正文  
方法：`read_file` 打开每张 PNG 与同名 HTML；对照插入点正文、12.4 DDL / 13.8 表、`server.py` `_cart_items` 校验顺序。  
禁止改教材。本文件只写 KEEP / FAIL。

---

## 总表

| 资产 | 核验口径 | HTML | PNG | 正文 | 结论 |
| --- | --- | --- | --- | --- | --- |
| `ch13-four-shapes` | 四格带 sku | 四格均含 `"sku":"SKU-DEMO-001"` | 与 HTML 同文 | 13.8 表同行 | **KEEP** |
| `ch12-pk-fk` | `products.id` 主键 | 主键卡写 `products.id`；sku 标 UNIQUE 不是 PK | 与 HTML 同文 | 12.3 ASCII + 12.4 `id INTEGER PRIMARY KEY` | **KEEP** |
| `ch12-tables` | 教学库 3 商品 | products 三行含耳机；kicker「不是 MiniShop v1.0 种子」 | 与 HTML 同文 | 12.4 INSERT 三行 | **KEEP** |
| `ch15-venv` | 无立刻 `pip install -r` | 中列 `pip list`；全文无 `-r` | 与 HTML 同文 | 15.9 本章不装 requests/pytest | **KEEP** |
| `ch18-p95` | caption 不是并发≠TPS | caption 讲五样本 / 最近秩 P95=800 | 与 HTML 同文 | 18.2 同一组数；并发在 18.4 邻图 | **KEEP** |
| `ch09-get-post` | `keyword=鼠标` 或非 mouse 空列表 | `GET /api/products?keyword=鼠标`；无 `mouse` | 与 HTML 同文 | 9.8 图下解绑句 | **KEEP** |
| `ch05-decision-table` | caption 不是超库存 | caption 409/400，无「超库存」 | 与 HTML 同文 | 5.9 注册占用表 | **KEEP** |

**总裁决：7 / 7 KEEP。无 FAIL。**

七组 PNG 均为 1320×780；mtime 均晚于同名 HTML（2026-09-10 13:25–13:26 截于 13:15–13:17 的 HTML）。未发现「改了 HTML 忘重截」。

---

## 1. `ch13-four-shapes` — KEEP

文件：`chapters/assets/diagrams/ch13-four-shapes.html` / `.png`  
出现位置：`chapters/13-api-testing.md` 13.8 L250

**口径：** 四格带 sku。旧图 2–4 格裸 `{"qty":null}` 等，会先被 `_cart_items` 打成 `missing sku`。

**HTML（四格 Body + oracle）：**

| 格 | Body | 图上错误串 |
| --- | --- | --- |
| 缺字段 | `{"sku":"SKU-DEMO-001"}` | 400 missing qty |
| null | `{"sku":"SKU-DEMO-001","qty":null}` | 400 null qty |
| 空串 | `{"sku":"SKU-DEMO-001","qty":""}` | 400 wrong type qty |
| 错误类型 | `{"sku":"SKU-DEMO-001","qty":"1"}` | 400 wrong type qty |

lead：「一次只破坏 qty，四格都带 sku。」caption：「缺 sku 会先变成 missing sku，不要画成 null qty。」

**PNG：** `read_file` 目视四卡均含 `SKU-DEMO-001`；无裸 `{"qty":…}`。caption 与 HTML 同句。

**正文 13.8 表 L253–260：** 缺字段 / null / 空字符串 / 错误类型四行与图逐字节相同。`server.py` L366–382：先 `"sku" not in data` → `missing sku`，再 `missing qty` / `null qty` / `wrong type qty`。图与实现、表一致。

---

## 2. `ch12-pk-fk` — KEEP

文件：`chapters/assets/diagrams/ch12-pk-fk.html` / `.png`  
出现位置：`chapters/12a-sql-query.md` 12.3 L62

**口径：** `products.id` 主键。旧图把 `products.sku（唯一）` 写成「这一行的身份证」。

**HTML：** 主键卡「users.id、products.id、cart_items.id。……sku 是 UNIQUE 不是 PK：JOIN 购物车时连的是 products.id」。外键卡「cart_items.user_id → users.id，且 cart_items.product_id → products.id」。caption：「主键是三张表的 id；sku 是 UNIQUE 不是主键。」

**PNG：** `read_file` 目视主键卡含 `products.id`，sku 标 UNIQUE 不是 PK；外键两条都在。无 `products.sku` 当主键。

**正文：** 12.3 ASCII（L69–72）`products.id <----- cart_items.product_id`。12.4 DDL（L93–97）`id INTEGER PRIMARY KEY`，`sku TEXT NOT NULL UNIQUE`。图与 DDL / ASCII 同口径。

---

## 3. `ch12-tables` — KEEP

文件：`chapters/assets/diagrams/ch12-tables.html` / `.png`  
出现位置：`chapters/12a-sql-query.md` 12.4 L82

**口径：** 教学库 3 商品。旧图自称 MiniShop 种子，只画 2 商品。

**HTML products 表：**

| id | sku | name | stock |
| --- | --- | --- | ---: |
| 1 | SKU-DEMO-001 | 无线鼠标 | 10 |
| 2 | SKU-DEMO-002 | 键盘 | 5 |
| 3 | SKU-DEMO-003 | 耳机 | 3 |

kicker：「12.4 教学库（不是 MiniShop v1.0 种子）」。users 三行含 `13800138002` / `NULL`；cart_items 三行（A 鼠标 1、A 键盘 2、B 鼠标 1）。黄条：v1.0 用户 3 是 `13800138099` Admin，禁止拿本图对 `seed-join.txt` 做 COUNT。无「MiniShop 种子数据如下」。

**PNG：** `read_file` 目视 `products（3 行，含耳机）`、三件商品、教学库标题与对照条均在。

**正文 12.4 INSERT L114–117：** 三行商品与图逐字段相同。L125 明文「不要把教学库用户 3 当成项目管理员」。

---

## 4. `ch15-venv` — KEEP

文件：`chapters/assets/diagrams/ch15-venv.html` / `.png`  
出现位置：`chapters/15b-python-files-json.md` 15.9 L30

**口径：** 无立刻 `pip install -r`。旧图中列 `pip install -r requirements.txt`、右列 `run.py setup`。

**HTML 检索：** `pip install -r`、`run.py setup`、「审查未点击」均为 0 命中。中列：「python3 -m venv .venv 后 python3 -m pip list，本章只该看到 pip」。右列：「本章不要在仓库里装包。」caption：「`.venv` 不要进 Git。」

**PNG：** `read_file` 目视三列与 HTML 同文；画面无 `pip install -r`、无 `requirements.txt`、无 `run.py`。

**正文 15.9 L61–79：** 练习目录建 `.venv`；`python3 -m pip list`；「本章**不要**安装 `requests` / `pytest`」。图不再把学生赶到立刻装包。

---

## 5. `ch18-p95` — KEEP

文件：`chapters/assets/diagrams/ch18-p95.html` / `.png`  
出现位置：`chapters/18-performance-testing.md` 18.2 L112

**口径：** caption 不是并发≠TPS。旧 caption 整段抄 18.4「并发人数 ≠ TPS。50 线程共用一个教学账号」。

**HTML caption：**「五个样本 100 / 110 / 120 / 200 / 800 ms。平均 266 ms 藏不住尾部。最近秩：n=5 时 5×0.95=4.75，向上取整取第 5 个，P95=800 ms；P50=120 ms。800 ms 不是 MiniShop SLA。」全文无「并发人数」、无「TPS」。柱下标 `P50=120`、`尾部 · P95=800`。

**PNG：** `read_file` 目视 caption 为五样本 / 最近秩，不是并发≠TPS。五柱 100/110/120/200/800，红柱旁「尾部 · P95=800」。

**正文 18.2 L93–110：** 同组样本平均 266.0、中间 120、最大 800；最近秩 P50=120、P95=800。并发≠TPS 在 18.4 与邻图 `ch18-tps-concurrency`（caption 讲 50 线程单账号），未串回本图。

---

## 6. `ch09-get-post` — KEEP

文件：`chapters/assets/diagrams/ch09-get-post.html` / `.png`  
出现位置：`chapters/09a-network-http-semantics.md` 9.8 L275

**口径：** `keyword=鼠标`，或非 mouse 且标明空列表。旧图 `keyword=mouse` 打仓库得空 `items`。

**HTML：** `GET /api/products?keyword=鼠标`。`mouse` 0 命中。

**PNG：** `read_file` 目视 GET 卡 monospace 为 `GET /api/products?keyword=鼠标`。无 `mouse`。

**正文 L277：**「示意图路径是 MiniShop 的 `GET /api/products?keyword=鼠标`。……不要抄成 `/api/products?keyword=mouse`（种子商品名是中文，会得到空列表）。」`server.py` L271 对 `name`/`sku` 小写包含匹配，「鼠标」能命中「无线鼠标」。满足「keyword=鼠标」支。

---

## 7. `ch05-decision-table` — KEEP

文件：`chapters/assets/diagrams/ch05-decision-table.html` / `.png`  
出现位置：`chapters/05-test-case-design.md` 5.9 L264

**口径：** caption 不是超库存。旧 caption「不要把『否』和『超库存』叠在同一条里」，表却是注册。

**HTML caption：**「每列一条规则。占用失败是 409，格式或密码失败是 400，不要叠在同一格。」`超库存` 0 命中。表：手机号合法 / 密码合法 / 号码未占用 → 201 有 phone、无 token / 400 / 400 / 409。lead：「失败后『保持原值』PRD 未写，不要画进动作。」

**PNG：** `read_file` 目视 caption 为 409/400，无「超库存」。四列动作与 HTML 同。

**正文 5.9 L266–277：**「图和下面这张 Markdown 是同一张业务：MiniShop v1.0 注册占用表」。章内 `超库存` 0 命中。图注不再串库存课。

---

## 残余（不构成 FAIL）

本任务只裁七条口径。下列不改裁决：

- `ch18-p95` 柱高仍非线性比例（100 画成约 28% 高、200 约 50%、800 为 100%）。caption 已不串台。
- `ch05-decision-table` 规则 1 因「201 有 phone、无 token」把 2–4 列挤窄。caption 已无超库存。
- `ch15-venv` 右列「第 19 章再装」相对 15.9「第 16 章再用 pytest/requests」偏后；任务口径是禁止立刻 `pip install -r`，图已满足。
- 09A L298 / 练习仍用教学 URL 的 `keyword=mouse`，正文 L277 已解绑；**图**已改为 `鼠标`。

未改任何教材文件。
