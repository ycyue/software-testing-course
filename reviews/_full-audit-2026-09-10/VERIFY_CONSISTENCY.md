# VERIFY_CONSISTENCY

日期：2026-09-10  
Agent：Verification-Agent-05 跨章节一致性  
抽核对象：FIX 后学习者正文 / 测验 / MiniShop 可抄资产（**未改教材**）  
对照台账：`FIX_PLAN.md`、`FIX_LOG.md`、对应 `fix-records/FIX_*.md`  
本机复跑：`cd project/minishop && python3 -m pytest -q` → **38 passed, 1 xfailed**（xfail = `test_empty_keyword_should_not_return_all` / BUG-001）

---

## 0. 结论先说

六条抽核里，**登录、Cookie/401（第 8/14/测验 3）、lastOrderId、qty=10/11 过去时、第 3 章 vs 06B 加购** 已对齐，**没有新的 P0**。

仍有两处 **修复后可见的新张力**（都不是原 P0 回潮）：

| ID | 等级 | 是否新冲突 | 摘要 |
| --- | --- | --- | --- |
| V05-0001 | P2 | 是：M-P1-32 把基线改成 38 之后，图/反抄例句没跟上 | 学习者主文写 **38 passed / 1 xfailed**，`09-pytest-report.png` 与 `ch19-workbench` 图注仍写 **37** |
| V05-0002 | P2 | 是：M-P1-09/18/35 把 8/14/测验 3 钉成「401=无 Bearer **且** 无 Cookie」之后，9/13/16/20 仍用「无 token/无 Bearer → 401」省略句 | 指定的 8/14/测验 3 三者彼此一致；省略句在 curl/pytest 无 Cookie 时碰巧成立，浏览器/Postman 会打成 201 |

第 3 章与 06B 加购已对齐。06A §6.3 仍写「加购」是**相邻残留**，不判本条失败（见 §7）。

---

## 1. 抽核表

| # | 抽核点 | 原修复 | 现行判定 |
| --- | --- | --- | --- |
| 1 | 登录：第 1 章错误密码 vs 10/13 正确密码成功 | MASTER-P0-001 | **PASS**，无新冲突 |
| 2 | Cookie/401：第 8 / 14 / 测验 3 | M-P1-09、M-P1-18、M-P1-35 | **三者 PASS**；第 9/13/16/20 省略句 = V05-0002 |
| 3 | lastOrderId：第 14 章 vs 集合 | M-P1-19 | **PASS** |
| 4 | qty=10/11 第 13–22 vs 现在时教学服务 qty=1 | M-P1-24 | **PASS**（qty=1 仅作合法数量或已删除历史） |
| 5 | pytest 38 vs 仍写 37 的学习者正文 | M-P1-32、M-P1-28 | **主文 PASS；图/反抄未收口** = V05-0001 |
| 6 | 加入购物车：第 3 章 vs 06B | M-P1-02、M-P2-08 | **PASS** |

---

## 2. 登录：第 1 章错误密码 vs 第 10/13 章正确密码成功

**判定：PASS。** 开篇不再把种子账号写成开放缺陷。

### 第 1 章（现行）

`chapters/01-software-testing-intro.md` 场景导入：

- 教学账号 `13800138000` / **正确密码 `Test1234`**「在仓库里**会登录成功**，不是开放缺陷」
- 失败观察改用错误密码 **`Test1234x`**，判定后失败是预期，不是缺陷
- 开放缺陷钉在空搜索 **BUG-001**
- 工作场景块（约 L361）同口径

示意图 HTML 与 PNG 已对齐（FIX 记录曾写 PNG 待重截，现行 `ch01-static-dynamic.png` 已是 `Test1234x` 失败 + `Test1234` 成功）：

- `chapters/assets/diagrams/ch01-static-dynamic.html`
- `chapters/assets/diagrams/ch01-static-dynamic.png`

### 第 10 / 13 章

`10-chrome-devtools.md` MiniShop 逐步操作：

4. 错误密码 → `POST /api/login` **401**（图 `02-login-fail.png`）
5. 改成密码 **`Test1234`** → **200**，JSON 有 `token`，`Set-Cookie` 含 `HttpOnly`（图 `03-shop.png`）

`13-api-testing.md` 可抄报文 / curl：

- Body `{"phone":"13800138000","password":"Test1234"}`
- 成功形状 **200** + `token` + `Set-Cookie`
- 检查清单：错误密码 → 401；正确密码成功

仓库契约：`tests/test_api.py::test_login_ok`（`Test1234` → 200 + token + Set-Cookie）；`test_login_wrong_password` → 401。

**无新冲突。** 第 1 章「失败」是明确的错误密码演示，第 10/13 章「成功」是同一组种子凭证。学生按第 1 章用 `Test1234` 去跑 MiniShop，会登录成功，与后文一致。

---

## 3. Cookie / 401：第 8 章、第 14 章、测验 3

**判定：指定三者 PASS，口径同一把尺子。**

尺子：MiniShop `401` = **无 Bearer 且无 Cookie `minishop_session`**。只去掉 `Authorization`、Cookie 还在 → 仍可能 200/201。仓库「无凭证创建」必须 `disableCookies`。

| 落点 | 现行原文（摘） | 与尺子 |
| --- | --- | --- |
| 08B 8.14 表 | 「无 Bearer **且** 无 Cookie `minishop_session` … → 401」；「只去掉 Authorization、Cookie 还在 → 仍可能 200/201」 | 一致 |
| 08B 8.12 | 「没有 Bearer 时，服务端仍会读 Cookie `minishop_session`」 | 一致 |
| `ch08-privilege.html` / `.png` | 「无 Bearer 且无 Cookie … 只去掉 Authorization、Cookie 还在，MiniShop 仍会认人」 | 图已跟上（本轮打开 PNG 确认） |
| 14.2 / 14.4 / 14.5 / 14.7 | 无凭证 = 不要 Authorization **且**关掉 cookie jar；集合已 `protocolProfileBehavior.disableCookies`；cookie jar 代发会变成 **201** | 一致 |
| 集合 JSON | 「无凭证创建」`disableCookies: true`，无 `Authorization` 头，断言 401 | 与正文一致 |
| 测验 3 Q5 / Q9 | 401 = 无 Bearer **且** 无 Cookie；仅缺 Authorization 仍可能 201；没有 Bearer 时 Cookie 仍能认人 | 一致 |
| 实操 8-1 README | 未认证 401 要**同时去掉** Bearer 和 Cookie；只去 Bearer 会仍是 200 | 一致 |
| 第 22 章能力表 | 「401=无 Bearer **且** 无 Cookie」 | 与 8/14 同向 |

集合与环境抽核：

- `project/minishop/postman/MiniShop.postman_collection.json`：「无凭证创建」有 `disableCookies`；「创建订单」`set('lastOrderId')`；越权 URL `{{baseUrl}}/api/orders/{{lastOrderId}}`
- pytest `test_cart_unauthorized` / `test_create_order_unauthorized` 不带 Cookie 头，401 在该通道成立

**指定三者没有互相打脸。** 修复后新张力见 V05-0002。

---

## 4. lastOrderId：第 14 章 vs 集合

**判定：PASS。**

| 资产 | 变量名 |
| --- | --- |
| `MiniShop.postman_environment.json` | 仅 `lastOrderId`，无 `orderId` |
| 集合「创建订单」脚本 | `pm.environment.set('lastOrderId', json.id)` |
| 集合「越权-他人订单 / 管理员读明细」 | `GET {{baseUrl}}/api/orders/{{lastOrderId}}` |
| 14.2 | 「仓库越权请求的 URL 是 `{{baseUrl}}/api/orders/{{lastOrderId}}`」 |
| 14.3 表 | 行名 `lastOrderId` |
| 14.5 脚本 | `pm.environment.set("lastOrderId", body.id)` |
| 14.7 对照表 | `GET /api/orders/{{lastOrderId}}` |
| 练习 8 答案 | `pm.environment.get("lastOrderId")` |
| `chapters/14-postman.md` 全文 | **零处** `orderId` 字符串 |

按正文 `set("lastOrderId")` 再跑仓库越权请求，Path 能替换，不会再打成 `GET /api/orders/` → 404。

（集合越权脚本对 403 Body 做 `json.id not.eql lastOrderId` 在无 `id` 时会空转通过，属 RT03 旧账，不是 lastOrderId **命名**冲突，本条不升级。）

---

## 5. qty=10/11 第 13–22 vs 现在时「教学服务 qty=1」

**判定：PASS。** 收口层已改过去时；第 13–16 章可抄示例就是 `/api/` + qty=10 允许 / qty=11 拒绝。

### 现行第 13–16 章（不是 qty=1-only 桩）

- 13 开篇：「路径带 `/api/`，购物车 `qty=10` 允许、`qty=11` 拒绝」
- 13.8 表：`qty=1` 是**正常合法值** 200（种子购物车本来就是 1），旁边有 `qty=10` → 200、`qty=11` → 400。这是 v1.0 允许的正整数，**不是**「只让 qty=1 成功」
- 14.7：qty=1 与 qty=10 → 200；qty=11 → 400
- 16A 表：`qty=1` 或 `qty=10` → 200；`qty=11` → 400；路径 `/api/login`
- 16B：「不要另写一台 `/login` 教学服务」；基线 38/1 对端是 `project/minishop`

### 收口层（过去时）

| 文件 | 现行 |
| --- | --- |
| 19 错误 2 / 练习 2 / 总结 | 「仓库曾经有过 `/login` + 只让 qty=1 成功的桩，**现行教材已删除**」 |
| 测验 6 Q5 | 「曾经有过 qty=1 教学桩，现在还要去第 16 章找第二台服务器吗？」答案：不要，现行 13–16 已是 `/api/` 与 10/11 |
| 20.3 / 错误 8 | 「旧 `/login` + qty=1 教学桩已删除」；「不要去找第二台教学服务」 |
| 22.1 / 错误 5 | 同过去时 |
| `ch19-qty-rule.html` / `.png` | 标题 qty=10/11；caption「仓库曾经有过 /login + qty=1 教学桩，现行第 13～16 章已删除」（PNG 已跟上） |

### 不要误报的现在时「教学服务」

- 18.7「启动教学服务」= `cd project/minishop && python3 run.py serve`，打 `/api/products`，不是 qty=1 桩
- 17 练习里 `TEACH_BASE_URL` 指已关机 CI 假想，未写成 MiniShop 现行契约

**无现在时「第 13/16 章教学服务只让 qty=1 成功」。** 学生按 13–16 可抄示例跑仓库，得到的是 10 允许、11 拒绝。

---

## 6. pytest 38 vs 仍写 37 的学习者正文

**判定：主文已改 38；图与反抄例句仍写 37 → V05-0001。**

本机与仓库证据：

| 来源 | 数字 |
| --- | --- |
| 本轮 `pytest -q` | **38 passed, 1 xfailed** |
| `evidence/pytest-output.txt` | 38 passed, 1 xfailed |
| `evidence/pytest-report.html` | **39 tests**，**38 Passed**，1 Expected failure |
| `project/minishop/README.md`、`docs/test-report.md`、`resume-evidence.md` | 38/1（test-report 把 37 标成 2026-09-09 **历史**） |
| practice 16-1 / 19-1 | 验收串 `38 passed` |
| `practice/STATUS.md` 16-1 | 38 passed / 1 xfailed |

学习者**章节正文 / 测验**已写 38 的：

- `16-pytest.md`、`16a`、`16b`
- `19-minishop-project.md`（含「收集 39 = 38 passed + 1 xfailed」）
- `20-interview.md`、`21-job-hunting.md`
- 测验 6 Q6、测验 7 Q5
- 根 `README.md`：`python3 run.py test  # 基线：38 passed, 1 xfailed`

### 仍写 37 的学习者可见处

1. **`chapters/assets/09-pytest-report.png`**（第 14 / 16A / 19 章引用）  
   打开截图：日期 **09-Sep-2026**；**38 tests**；筛选条 **37 Passed** + 1 Expected failure。  
   这是 M-P1-32 **之前**的收集数（38 = 37 + 1 xfail）。现行 evidence HTML 已是 39 tests / 38 Passed。  
   图注已改成「passed + 1 expected failure（以本机 pytest 为准）」，**像素里仍是 37**。学生本机 38/1 会对着这张旧图怀疑多跑出一条。

2. **`chapters/assets/diagrams/ch19-workbench.html` 与 `.png`**  
   caption：「示意图：**37 passed / 1 xfailed** 仍带着 BUG-001。数字以本机最近一次 pytest 为准。」  
   同章正文（19.1/19.8/总结）写 38。**章内图文打架。** PNG 与 HTML 一致，都还是 37（本轮打开 PNG 确认）。

3. **第 22 章 + `practice/README.md` 22-1**  
   结课自检反复写「不要抄 **37 passed**」。禁抄意图仍对，但示例数字已过时；现行可抄正文里的审查数字是 38。学生可能以为「37 不能抄、38 可以抄」，或以为仓库基线还是 37。

非学习者正文、不升为本条失败：

- `docs/COURSE_CONTROL.md` L17：2026-09-09 复评句仍写 `37 passed, 1 xfailed`（作者主控历史）
- `reviews/` 审计报告里的 37（禁止改审计原文）

**这是 M-P1-32 把基线 +1 之后的新残留，不是 37/1 时代的旧账回潮。** 主文与 practice 门闩已锁 38，故不升 P0/P1。

---

## 7. 加入购物车：第 3 章 vs 06B

**判定：PASS。** MiniShop 页面按钮是「更新数量」「创建订单」（`frontend/index.html` L68 / L78），没有独立「加入购物车」。

### 第 3 章（M-P1-02 后）

- 3.6 冒烟：「首页能打开、用户能登录、商品列表能加载、**能更新合法数量、能创建订单**」
- 工作实战：「登录、更新购物车数量或创建订单（**不要写加入购物车/结算/下架**）」
- 练习 4 答案：「首页打开、登录、商品加载、**更新合法数量、创建订单**。不要写加入购物车/结算」
- 章内「加入购物车」只出现在**禁止句**

### 06B（M-P1-06 + M-P2-08 后）

- 全文 **无「加购」/「加入购物车」**
- 练习 10 答案：确认对象是 BUG-001 空搜索；回归是「有关键字搜索、登录、**qty=10**、**创建订单**」

二者动词与页面控件一致，不再互抄「加入购物车」。

### 相邻残留（不判本条失败）

`06a-bug-management.md` §6.3 仍写回归「是否影响**加购**、改数量、创建订单」。FIX_M-P2-08 已声明不在该 ID 范围。第 7 章 combo 教学页的「加入购物车」按钮有正文声明「不代表真实 MiniShop」。04B 引用的是 v0.1 **草案**反例。

---

## 8. 修复后新冲突（本轮要记的）

### ISSUE V05-0001

ID：V05-0001  
文件：`chapters/assets/09-pytest-report.png`；`chapters/assets/diagrams/ch19-workbench.html` + `ch19-workbench.png`；`chapters/22-learning-path.md`；`practice/README.md`  
对照：`chapters/16a-pytest-basics.md` L266、`19-minishop-project.md` L245/L254、`evidence/pytest-report.html`（39 tests / 38 Passed）  
问题等级：P2  
问题类别：SEQ / IMG / MiniShop  
问题说明：M-P1-32 新增所属者 GET 200 后，可跑基线与章节主文是 **38 passed / 1 xfailed（收集 39）**。学习者仍会在第 19 章工作台图注读到 **37 passed**，在 pytest-html 截图筛选项读到 **37 Passed / 38 tests**，在结课自检读到「不要抄 37 passed」。  
为什么有问题：同一章（19）正文 38、图 37；同一张 `09-pytest-report.png` 被 14/16/19 引用。线性读者会问「我是不是多跑了一条」或把 37 抄进简历。22 章反抄例句未改成现行数字，禁抄纪律还在，示例过期。  
依据：本机 pytest 38/1；evidence HTML 38 Passed；FIX_M-P1-32「`09-pytest-report.png` 仍是旧截图，需 Coordinator 重截」——**至今未重截**（像素日期 09-Sep-2026，37 Passed）。  
建议修改：按现行 `evidence/pytest-report.html` 重截 `09-pytest-report.png`；`ch19-workbench` caption 改 38 或只写「passed + 1 xfailed，以本机为准」不要写死 37；22 章 / practice 22-1 反抄句改成「不要抄正文或 evidence 里的数字（包括 38 passed）」。  
是否挡发布：否。主文、practice 16-1/19-1、test-report 已锁 38。

### ISSUE V05-0002

ID：V05-0002  
文件：`chapters/assets/diagrams/ch09-status.html` + `ch09-status.png`；`chapters/13-api-testing.md` L263；`chapters/16a-pytest-basics.md` L208；`chapters/16b-pytest-fixtures.md` L242；`chapters/20-interview.md` L241  
对照：08B 8.14、14.2、测验 3 Q5（401 = 无 Bearer **且** 无 Cookie）  
问题等级：P2  
问题类别：HTTP / SEQ / MiniShop  
问题说明：第 8/14/测验 3 已写清 Cookie 回退。修复后，第 9 章状态码图仍写「无 token 下单」；第 13 章 13.8「无 Bearer 时购物车是 401」；16A 表「`POST /api/orders` 无 Bearer | 401」；16B 门槛「无 Bearer 下单是 401」；第 20 章面试示例「无 token 下单 401」。FIX_M-P1-35 已点名第 9 图与第 20 章「不在本 ID 范围」，故是**修复后未扩散的省略句**，不是 8/14/测验 3 回潮。  
为什么有问题：已登录浏览器或 Postman cookie jar 下，只去掉 Bearer 是 **201** 不是 401。测验 3 会抓 Cookie，第 9/20 章口头仍说「无 token 下单 401」。13.9 表其实已经写对（「不带 Cookie / Bearer」→ 401），与 13.8 一句打架。16A/pytest 通道不带 Cookie，省略句在该通道成立，学生换到 Postman 会踩 M-P1-18 刚修掉的坑。  
依据：`server.py` `_token()` Bearer 优先、Cookie 回退；FIX_M-P1-09 MiniShopLab：Cookie-only POST `/api/orders` → 201，两者都无 → 401。  
建议修改：第 9 图 / 第 20 章示例改成「无 Bearer **且** 无 Cookie 下单 401」；13.8 与 16A/16B 补半句「本通道请求未带 Cookie；浏览器/Postman 还要关 cookie jar」。  
是否挡发布：否。指定抽核的 8/14/测验 3 已一致；curl/pytest 无 Cookie 时数字仍对。

### 不升格

- 06A §6.3「加购」：第 3 章 vs 06B 已对齐；06A 是同章上册残留，P3，非本条失败。
- 14 越权断言 `json.id` 空转：旧 P2，与 lastOrderId 命名无关。
- `docs/COURSE_CONTROL.md` 37：作者主控历史句，不是章节正文。

---

## 9. 覆盖与方法

| 抽核 | 打开 / 检索 |
| --- | --- |
| 登录 | `01-software-testing-intro.md`；`ch01-static-dynamic.html/png`；`10-chrome-devtools.md` L392–408；`13-api-testing.md` L340–384；`test_api.py` login |
| Cookie/401 | `08b` 8.12–8.14；`ch08-privilege.html/png`；`14-postman.md` 14.2/14.4/14.5/14.7；集合 JSON；`quizzes/stage-3-web.md`；`practice/08-privilege/README.md` |
| lastOrderId | `14-postman.md` 全文 `orderId` 检索（0 命中）；环境 JSON；集合 set/URL |
| qty=1 现在时 | `chapters/13`–`22` + 测验 6：`教学服务` / `qty=1 唯一` / `只让 qty=1`；`ch19-qty-rule.html/png` |
| pytest 37/38 | `chapters/**/*.md`、`practice/`、`project/minishop/`、`docs/`；打开 `09-pytest-report.png`、`ch19-workbench.png`；本机 pytest |
| 加购 | `03` 3.6 / 工作实战 / 答案 4；`06b` 全文；`index.html` 按钮文案 |

未改 `chapters/`、`practice/`、`project/`。练习 10（06B）、测验 3 Q5 按现行答案独立核对，与正文同向。

---

## 10. 总判

| 问题 | 修复后是否新冲突 |
| --- | --- |
| 第 1 章错误密码 vs 10/13 正确密码成功 | **否** |
| Cookie/401 第 8 / 14 / 测验 3 | **三者否**；9/13/16/20 省略句为 V05-0002 |
| lastOrderId 第 14 vs 集合 | **否** |
| qty=10/11 第 13–22 vs 现在时教学服务 qty=1 | **否** |
| pytest 38 vs 学习者仍写 37 | **是（图/反抄）** V05-0001；章节主文已是 38 |
| 加入购物车 第 3 vs 06B | **否** |

**抽核六条无 P0 回潮、无指定三者互相打脸。** 发布前建议 Coordinator 只做两件小事：重截 `09-pytest-report.png` 与改 `ch19-workbench` caption；Cookie 省略句可随下一轮 P2 收。
