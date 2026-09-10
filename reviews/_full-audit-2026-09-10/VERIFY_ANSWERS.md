# VERIFY_ANSWERS — Verification-Agent-03

- Agent：Verification-Agent-03（练习与答案）
- 日期：2026-09-10
- 范围（仅这 8 题）：第 3 章练习 4；06B 练习 10；08A 练习 10；测验 3 Q5、Q6；测验 5 Q9；测验 6 Q5；测验 7 Q8
- 方法：先据 PRD / `server.py` / 前端 / 实操 6-1 / 第 10、16、19、20 章口径独立作答，再对照**修复后**公布答案。禁止改教材。
- 判定：PASS = 独立答案与修复后答案同向，关键对象不错；FAIL = 整题或关键对象仍错。残留用词另记，不升为整题 FAIL，除非会让学生看错观察对象。

**本文件只写审查。未改 `chapters/`、`practice/`、`project/`。**

---

## 0. 总表

| # | 题 | 结论 | 原缺陷（已修） | 对照要点 |
| --- | --- | --- | --- | --- |
| 1 | 第 3 章练习 4 | **PASS** | M-P1-02 / G04-0001 冒烟「加入购物车」 | 五项 = 首页、登录、商品加载、更新合法数量、创建订单 |
| 2 | 06B 练习 10 | **PASS** | M-P1-06 对象写成 qty=11；M-P2-08「加购」 | 对象 BUG-001；确认空搜索；回归非加购 |
| 3 | 08A 练习 10 | **PASS** | M-P1-12 把输入框仍为 11 当失败 | 列表/接口 qty 不得变 11；框里 11 不算失败 |
| 4 | 测验 3 Q5 | **PASS** | M-P1-35 「无 token 下单 = 401」 | 401 = 无 Bearer **且** 无 Cookie；Cookie-only → 201 |
| 5 | 测验 3 Q6 | **PASS** | CH10-0001 / M-P1-14 登录必勾 Preserve log | 先开 Network；Preserve log 只管文档跳转 |
| 6 | 测验 5 Q9 | **PASS** | M-P1-31 缺 `cd project/minishop` | 依赖在该目录 `requirements.txt`；根目录无 `run.py` |
| 7 | 测验 6 Q5 | **PASS** | M-P1-24 教学服务现在时 | qty=10/11；桩是过去时；不要找第二台服务器 |
| 8 | 测验 7 Q8 | **PASS** | G04-0004 / CH20-0003 STAR 另套 | 仍用五段；STAR 只映射 |

**8/8 PASS。0 FAIL。**

残留（不构成 FAIL，见 §2.3）：08A 题干/答案把带 `qty=` 的购物车列表写成「商品列表」。商品区 `#product-list` 只渲染库存，没有 qty。缺陷标题示例已写「购物车…列表数量」，核心判定与截图一致。

---

## 1. 独立求解所用冻结事实（先于对照答案）

来源：`project/minishop/docs/PRD.md`、`server.py`、`frontend/index.html` + `app.js`、`practice/06-bug-report/README.md`、`bugs/BUG-001.md`、截图 `05-cart-qty-11.png`、本机探针、Chrome Network 文档。不是从公布答案抄的。

| 项 | 独立结论 |
| --- | --- |
| 页面按钮 | 无「加入购物车」。购物车「更新数量」，下单「创建订单」。登录后同页显示商品区+购物车+下单，不是另开购物车路由。 |
| 冒烟 | 构建能否开始测：打开首页、登录、三件商品、合法改数量、创建订单返回 `id`。 |
| 6-1 对象 | 书面实操写 **BUG-001 空搜索 / R-SEARCH**。06A 的 qty=11 是写法示范，v1.0 会拒绝 11，不要交。 |
| qty 规则 | R-CART-10：`SKU-DEMO-001` 库存 10 时 `qty=10` 允许、`qty=11` 拒绝。 |
| qty=11 页面 | 输入框可仍为 11（`app.js` 失败只改 `cart-msg` 再 `refreshCart`，不回写 input）。购物车列表 `qty=` 保持提交前值。商品区只有「库存」。 |
| 401 / 403 | RFC 9110：401 = 缺有效认证凭证；403 = 已理解请求但拒绝授权。MiniShop `_token()`：先 Bearer，否则 Cookie `minishop_session`。 |
| Preserve log | Chrome：「Save requests across **page loads**」。MiniShop 登录是 `hidden` 切换，不是文档导航。真导航：`/admin.html`。 |
| 依赖 / 命令 | 仓库根无 `run.py`。套件入口 `project/minishop/run.py`。`requirements.txt` 在该目录。 |
| 教学桩 | 仓库**曾经**有 `/login` + 只让 qty=1 的桩，现行 13～16 章打的就是 `/api/` + 10/11。无 `teach_server.py`。 |
| 面试结构 | 第 20 章强制：结论 → 原理 → 场景 → 示例 → 边界。STAR 映射，不另背一套。 |

本机探针（临时库，未改 `evidence/`）：

```
LOGIN_A            200 + Set-Cookie minishop_session
NO_CREDS_ORDERS    401 {"error":"unauthorized"}
COOKIE_ONLY_ORDERS 201 {"id":"ord-…"}
BEARER_ORDERS      201
B_READ_A           403
USER_ADMIN         403
QTY10              200 {"qty":10}
QTY11              400 {"error":"qty exceeds stock"}
CART_AFTER_11      qty 仍为提交前的 10（先打了 10 再打 11）
PRODUCTS           items 仅 sku/name/stock，无 qty
EMPTY_KW / SPACE   200 三件（BUG-001 仍开放）
```

仓库根：

```
python3 run.py test
→ can't open file '.../软件测试class/run.py'
python3 practice/run.py test
→ 没有编号 test。
```

`evidence/pytest-output.txt`：`38 passed, 1 xfailed`（BUG-001）。

Chrome 文档：<https://developer.chrome.com/docs/devtools/network/reference>「Save requests across page loads」= Preserve log。

---

## 2. 逐题

### 2.1 第 3 章练习 4 — PASS

**文件：** `chapters/03-software-testing-classification.md`  
**题干：** 为 MiniShop 写出五项冒烟检查。

**独立答案**

冒烟 = 这份构建能不能开始测（ISTQB confirmation/smoke 轴：关键路径子集，不是质量合格证明）。对照 `index.html` 真实控件，五项必须能点到：

1. 首页 / 登录页打开（`GET /`）
2. 教学账号登录成功（`13800138000` / `Test1234`）
3. 商品列表加载三件（鼠标 / 键盘 / 耳机）
4. 把 `SKU-DEMO-001` **更新**为合法数量（按钮「更新数量」，如 qty=2）
5. **创建订单**成功（按钮「创建订单」，返回 `id`）

禁止：加入购物车、结算、支付、下架。冒烟过 ≠ 可以上线。集合可随版本风险调整，但 v1.0 不能写页面上不存在的按钮。

**修复后答案**

> 例如：首页打开、登录、商品加载、更新合法数量、创建订单。不要写加入购物车/结算。实际集合应根据版本关键能力和风险调整。

与 3.6 正文同一张清单。工作实战仍禁止「加入购物车/结算/下架」。全文「加入购物车」只余禁止句。

**对照：** 五项动词与独立答案同向；已去掉加购/提交订单。  
**结论：PASS**

---

### 2.2 06B 练习 10 — PASS

**文件：** `chapters/06b-test-management.md`  
**题干：** 根据 06A / 实操 6-1 已写的缺陷，说明修复后怎样做确认测试和回归测试（不要再交第二份完整缺陷单）。

**独立答案**

- **对象：** 6-1 / `BUG-001`（空/空白关键字返回全量，R-SEARCH）。**不是** qty=11。qty=11 在 06A 是写法示范，实现会 400，不能当本单。
- **确认测试：** 同一修复构建上重放空关键字与仅空白关键字：`GET /api/products?keyword=`、若干空格、页面搜索框提交空格。按 R-SEARCH **不得**把全量三件当成搜索结果。400 还是空列表+提示，以当时已确认规则为准（PRD 未钉死唯一形态）。
- **回归测试：** 按修改点抽：有关键字搜索仍能命中、登录仍可用、合法数量（含 qty=10）仍允许、创建订单仍返回 `id`（Body 无 `status`）。不要写「加购」（页面无此按钮）。
- BUG-001 在修复前不得写成已关闭。不要再交第二份完整单。

**修复后答案**

> 对象是 6-1 / BUG-001（空搜索，R-SEARCH），不是 qty=11。确认测试：…空关键字或仅空白关键字…不得把全量商品当成搜索结果…回归测试：有关键字搜索仍能命中、登录仍可用、qty=10 仍允许、创建订单仍返回 id（无 status）。…qty=11 是另一条已实现规则（R-CART-10），不是本单确认步骤。BUG-001 在修复前不得写成已关闭。

06B 全文已无「加购」。

**对照：** 对象、确认步骤、回归范围与独立答案同向。  
**结论：PASS**

---

### 2.3 08A 练习 10（列表 qty vs 输入框）— PASS

**文件：** `chapters/08a-web-page-testing.md`  
**题干：** 库存 10 的商品，在购物车把数量改为 11。写 Web 步骤、预期，以及若**商品列表**变成 11 时的缺陷标题。**输入框仍显示 11 不算失败。** 不要虚构接口路径。

**独立答案**

步骤：

1. 登录 `13800138000` / `Test1234`（登录后本页即有购物车，无独立 `/cart`）。
2. 确认 `SKU-DEMO-001` 库存显示 10；**购物车列表**种子为 `qty=1`（Tester A）。
3. `#cart-qty` 改为 11，点「更新数量」。

预期（可观察、拆开三处）：

| 观察点 | 预期 | 失败？ |
| --- | --- | --- |
| `#cart-msg` | `qty exceeds stock`（或「失败」） | 无提示且写入成功 → 缺陷 |
| 购物车列表 `#cart-list` 的 `qty=` | 仍为**提交前**值（本题步骤下为 1） | 变成 11 → 缺陷 |
| `GET /api/cart` | 该 SKU `qty` 仍为提交前值 | 变成 11 → 缺陷 |
| 输入框 `#cart-qty` | **可以仍是 11** | 不算失败 |
| 商品区 `#product-list` | 只显示「库存 10」，本来就没有 qty | 不要拿库存列当 qty 判定 |

`app.js`：失败分支只改文案并 `refreshCart()`，不把 input 改回。`05-cart-qty-11.png` 与之一致：框=11，列表 `qty=1`，提示 `qty exceeds stock`。v1.0 无小计/价格。不要把「数量保持合法值」写成已冻结的唯一判定（若先改成 10 再打 11，列表应仍为 10 而非 1）。不要虚构未教的接口路径。

缺陷标题示例：购物车在库存为 10 时，提交 qty=11 后**列表数量**变成 11 且无失败提示。

**修复后答案**

> 步骤示例：登录测试账号；打开购物车；确认 SKU 教学商品库存显示 10、当前数量 1；把数量改为 11 并提交。预期：提交失败；页面提示 `qty exceeds stock`（或等价）；**商品列表/接口**该 SKU 仍为提交前的 `qty=1`；输入框可以仍显示 11，不要把「框里还是 11」当成失败，也不要把「数量保持合法值」写成已冻结的唯一判定。v1.0 没有小计/价格…缺陷标题示例：购物车在库存为 10 时，提交 qty=11 后列表数量变成 11 且无失败提示。

工作实战第 4 条同口径：列表不得变成 11（图中保持 `qty=1`）；输入框仍 11 也可以。

**对照**

- 核心（本题被点名的「列表 qty vs 输入框」）：**同向。** 框里 11 ≠ 失败；变成 11 的是列表/接口 qty。
- 缺陷标题已落到「购物车…列表数量」，与截图购物车 `qty=1` 一致。
- 残留用词：题干和答案写「**商品列表**」。页面「商品」`#product-list` 模板是 `sku + name + 库存`，**没有 qty**；带 `qty=` 的是「购物车」`#cart-list`。学生若只盯商品区，看不见 `qty=1`，也几乎看不到「变成 11」。答案里的「/接口」可补上 `GET /api/cart`。此残留不把整题打 FAIL：判定三件套（提示、列表/接口 qty、输入框）已与实现和截图对齐。

**结论：PASS**（残留见上，不改教材）

---

### 2.4 测验 3 Q5 — PASS

**文件：** `chapters/quizzes/stage-3-web.md`  
**题干：** 401 和 403 差在哪？MiniShop 里各举一例。

**独立答案**

- **401：** 没认出你。请求缺少**有效凭证**。MiniShop：无 `Authorization: Bearer` **且** 无 Cookie `minishop_session` 时访问受保护接口，例如 `POST /api/orders` → 401。
- **不能**写成「无 token / 不带 Authorization = 401」。浏览器登录后 Cookie 还在、只缺 Bearer 时，本机探针 `POST /api/orders` → **201**（`_token()` Cookie 回退）。
- **403：** 已认出你，但不许做这件事。例：普通用户 `GET /api/admin/orders` 或 `/api/admin/products` → 403；用户 B 读 A 的 `GET /api/orders/{id}` → 403（管理员也不走这条看他人订单，R-PERM）。

RFC 9110 §15.5.2 / §15.5.4：401 lacks valid authentication credentials；403 understood but refuses to authorize。

**修复后答案**

> 401：没认出你——无有效凭证（无 Bearer **且** 无 Cookie `minishop_session`）访问受保护接口，例如两者都不带时 `POST /api/orders`。仅缺 `Authorization`、浏览器仍带着 Cookie 时，MiniShop 仍可能 201。403：已认出你但不许，例如普通用户打 `/api/admin/*`…或用户 B 读 A 的 `GET /api/orders/{id}`。

本机：`NO_CREDS_ORDERS 401`；`COOKIE_ONLY_ORDERS 201`；`USER_ADMIN 403`；`B_READ_A 403`。

**对照：** 与独立答案同向，已堵住 Cookie-only 假 401。  
**结论：PASS**

---

### 2.5 测验 3 Q6 — PASS

**文件：** `chapters/quizzes/stage-3-web.md`  
**题干：** 为什么要先打开 Network 再点登录？Preserve log 解决什么？登录成功就一定要勾吗？

**独立答案**

1. **先开 Network：** 面板未开时请求已经结束，列表里不会出现。与是否跳转无关。没先开，不是 Preserve log 的问题。
2. **Preserve log：** 解决**文档跳转 / 整页导航 / 刷新**清空 Network 列表（Chrome：save requests across page loads）。
3. **登录成功不必勾。** MiniShop v1.0 登录是 `loginPanel.hidden = true; shopPanel.hidden = false`，不是 `location` 跳转。未勾选时 `POST /api/login` 通常还在。要演示清空：登录后点「后台」进 `/admin.html`，对比勾/不勾。只测登录、无整页跳转，应写「本次无整页跳转」。

**修复后答案**

> 先开 Network 是因为请求可能在打开面板前已经结束，与是否跳转无关。Preserve log 解决的是**有文档跳转/整页导航时**列表被清空，不是「登录就必须勾」。MiniShop v1.0 登录是页面内 hidden 切换，未勾选时登录 POST 通常还在；要看清空效果，登录后点「后台」进入 `/admin.html`。

与第 10 章 10.9 / 面试 Preserve log 示例同口径。

**对照：** 三问都同向。  
**结论：PASS**

---

### 2.6 测验 5 Q9 — PASS

**文件：** `chapters/quizzes/stage-5-api.md`  
**题干：** MiniShop v1.0 依赖装在哪？一键命令是什么？

**独立答案**

- **声明位置：** `project/minishop/requirements.txt`（pytest / pytest-html / requests）。`server.py` 本身标准库可跑，pytest 才要这些包。
- **安装落点：** `python3 run.py setup` 在 **`project/minishop/.venv`** 里 pip install 该文件。
- **一键（本课跑套件）：** 必须先进入该目录（或带路径调用该文件）：

```bash
cd project/minishop && python3 run.py setup && python3 run.py test
```

- **不要在仓库根执行 `python3 run.py`：** 根目录没有 `run.py`。`practice/run.py test` 会报「没有编号 test」。
- 从仓库根也可用 `python3 project/minishop/run.py setup`（16B 实操句），但测验给的可抄命令带 `cd` 更不容易抄错。README「一键运行」还有 `serve`；本题覆盖第 13～16 章，setup+test 是对的套件入口。

**修复后答案**

> `project/minishop/requirements.txt`。`cd project/minishop && python3 run.py setup && python3 run.py test`。不要在仓库根执行。

本机：根目录 `python3 run.py test` → `can't open file '.../run.py'`。`project/minishop/run.py` 存在。16 索引 / 16B 工作实战已是同一条 `cd`。

**对照：** 路径、cwd、禁止根执行与独立答案同向。  
**结论：PASS**

---

### 2.7 测验 6 Q5（教学服务过去时）— PASS

**文件：** `chapters/quizzes/stage-6-project.md`  
**题干：** qty=10 和 qty=11 在 v1.0 分别应怎样？仓库**曾经**有过 qty=1 教学桩，现在还要去第 16 章找第二台服务器吗？

**独立答案**

- v1.0 / R-CART-10：`qty=10` **允许**（200），`qty=11` **拒绝**（400 `qty exceeds stock`，不落库）。
- 仓库**曾经**有过 `/login` + 只让 qty=1 成功的教学桩，**已删除**。现行第 13～16 章可运行示例就是 `/api/` 与 10/11。
- **不要**去第 16 章找第二台服务器，也**不要**把已删除的桩当现行差异。跟 `docs/PRD.md`。
- 题干必须是过去时。现在时「第 16 章教学服务只让 qty=1」会把学生赶走找幽灵服务。

本机：`QTY10 200`；`QTY11 400`。`find` 无 `teach_server`。测验 6 全文已无「教学服务」现在时。第 19 章错误 2 / 练习 2 同为过去时。

**修复后答案**

> qty=10 允许，qty=11 拒绝。仓库曾经有过 `/login` + qty=1 桩，现行第 13～16 章已是 `/api/` 与 qty=10/11；不要另找服务器，跟 PRD。

**对照：** 时态、规则、不要第二台服务器，均同向。  
**结论：PASS**

---

### 2.8 测验 7 Q8（五段）— PASS

**文件：** `chapters/quizzes/stage-7-career.md`  
**题干：** 行为面试「和开发发生争执」用什么结构讲？不要编造未发生的故事。

**独立答案**

仍用第 20 章**五段**，不另背 STAR 当标准答案：

1. **结论：** 先对数据/复现，不对人。
2. **原理：** 争议回到需求、日志和库。
3. **场景：** 真实经历或课程练习（可用空搜索算不算缺陷）。
4. **示例：** 拿出 R-SEARCH 与三件商品的响应，标成开放缺陷。
5. **边界：** 需求真改了就改用例；不要编造未发生的争执。

STAR 映射（本课不另考一套）：场景 ≈ 情境；示例 ≈ 行动和结果；边界 ≈ 学到什么。同卷第 1 题已锁五段，Q8 必须同一把尺子。

**修复后答案**

> 仍用第 20 章五段：结论（先对数据不对人）→ 原理（回到需求、日志和库）→ 场景（空搜索算不算缺陷）→ 示例（拿出 R-SEARCH 和三件商品）→ 边界（需求改了就改用例）。场景对应常见 STAR 的情境，示例对应行动和结果，边界对应学到什么；本课不另背一套。必须是真实经历或课程练习，不要编。

与 `20-interview.md` 20.16「和开发对缺陷有分歧？」同构。已无「结论-场景-你做了什么-结果-你学到什么」那套 STAR 变体。

**对照：** 五段全称 + 一句映射 + 禁止编造，与独立答案同向。  
**结论：PASS**

---

## 3. 取证摘要

| 检查 | 命令 / 对象 | 结果 |
| --- | --- | --- |
| Cookie-only 下单 | 临时 MiniShop，有 Cookie、无 Bearer，`POST /api/orders` | **201** |
| 无凭证下单 | 同上，无 Cookie 无 Bearer | **401** |
| 越权 | 用户打 `/api/admin/*`；B 读 A 订单 | **403** |
| qty=10 / 11 | `POST /api/cart/items` | 200 / 400，11 不覆盖已写入的合法 qty |
| 商品 JSON | `GET /api/products` | 无 `qty` 字段 |
| 空搜索 | `keyword=` 与空格 | 200 三件（BUG-001） |
| 根目录 run.py | `python3 run.py test` | 文件不存在 |
| 教学桩文件 | `find … -name '*teach*'`（排除 reviews） | 无 |
| pytest 证据 | `evidence/pytest-output.txt` | 38 passed, 1 xfailed |
| qty=11 截图 | `chapters/assets/05-cart-qty-11.png` | 框 11；购物车列表 qty=1；提示 qty exceeds stock |
| Preserve log | Chrome Network reference | across page loads，不是凡登录必勾 |

---

## 4. 残留（不改教材，不升 FAIL）

1. **08A 练习 10 用词「商品列表」**：观察 qty 的是购物车列表 `#cart-list`，不是商品区。建议（若日后改教材）：题干/答案改成「购物车列表的 qty」；缺陷标题已基本正确。
2. **「打开购物车」**：v1.0 无独立购物车页，登录后同页可见。步骤仍可执行。
3. 测验 5 Q9「不要在仓库根执行」针对的是裸 `python3 run.py`；带路径的 `python3 project/minishop/run.py setup` 从根目录可用（16B 另有一句）。不构成答案错误。

---

## 5. 结论

指定 8 题修复后公布答案与独立作答**全部 PASS**。原先的加购冒烟、BUG-001 被答成 qty=11、输入框 11 当失败、Cookie-only 假 401、登录必勾 Preserve log、缺 `cd project/minishop`、教学服务现在时、Q8 另套 STAR，均已落到与实现/PRD/Chrome/第 20 章五段一致的答案上。

Verification-Agent-03 未修改任何教材正文。
