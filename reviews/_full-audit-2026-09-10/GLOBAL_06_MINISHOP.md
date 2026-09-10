# Global-06 MiniShop Project Audit

- 审计员：Global-Agent-06（MiniShop Project Agent）
- 日期：2026-09-10
- 范围：仅 `project/minishop/`，按**真实测试项目验收**，不审第 19 章教学文笔
- 对照：`AUDIT_AGENT_BRIEF.md` MiniShop 冻结口径、`docs/PRD.md`、OpenAPI、Chapter-19 审计（独立取证，不照抄）
- 禁止：未改教材、未改项目；本机 pytest 曾把 `evidence/pytest-output.txt` 时间从 0.61s 写成 0.68s，已 `git checkout` 还原

验收结论：**有条件通过（Conditional Pass）**。契约主路径、37/1、BUG-001 开放、订单无 `status`、qty=10/11、个人项目口径均成立。不能按岗位标准签章「权限已测完」和「空搜索 Web 证据充分」。

---

## 1. 产物覆盖（未检查 = 0）

| 产物 | 路径 | 已检查 | 现场结论 |
| --- | --- | --- | --- |
| README | `README.md`、`project/README.md` | 是 | 个人实践；setup/serve/test；非范围含无 status |
| 启动 | `run.py` / `run.sh` / `run.bat` / `server.py` | 是 | `setup` 成功；`server.py` 打印 `MINISHOP_BASE_URL`；未跑 `run.py test`（会改写证据） |
| 前端 | `frontend/index.html` `app.js` `admin.html` `styles.css` | 是 | 登录+注册；搜索/购物车/下单分表单；后台静态页 |
| PRD | `docs/PRD.md` | 是 | R-PHONE/PASS/REG/CART/CART-10/AUTH/ORDER/PERM/SEARCH |
| OpenAPI | `docs/openapi.json` | 是 | 3.0.3；9 条 `/api/*` 与 `server.py` 路由集合一致 |
| 计划/点/用例/矩阵 | `test-plan.md` `test-points.md` `test-cases.md` `prd-coverage-matrix.md` | 是 | 18 条用例摘要；空搜索失败；401 挂错规则 |
| 评审/SQL/报告/总结/简历 | `requirement-review.md` `sql-check.md` `test-report.md` `project-summary.md` `resume-evidence.md` | 是 | 口径诚实；权限正例缺口 |
| BUG | `bugs/BUG-001.md` | 是 | 仍开放；未写成已修复 |
| 测试代码 | `tests/conftest.py` `test_api.py` `test_qty_rule.py` `test_register.py` `pytest.ini` | 是 | 收集 38；本机 **37 passed, 1 xfailed** |
| Postman | `postman/*.json` | 是 | 15 请求；密码空；Bearer；无 Cookie 断言；空搜索会红 |
| JMeter | `jmeter/minishop-get-products.jmx` | 是 | 1 用户 1 循环；无 Response Assertion；本机无 jmeter 二进制 |
| 自动化说明 | `automation/README.md` | 是 | 指向 `../tests/`，不是第二套框架 |
| HTTP 证据 | `evidence/http/*.txt` `network-log.html` | 是 | 登录 Cookie 打码；空搜索三件；qty 10/11；订单仅 id |
| SQL/日志/Linux | `evidence/sql/` `logs/` `linux/` `logs/app.log` | 是 | JOIN 与种子一致；qty=11 未落库；日志无 `token=` |
| 截图 | `evidence/screenshots/*.png`（9） | 是 | 01=06 字节相同；04 弱；07 订单「暂无」 |
| pytest 证据 | `evidence/pytest-output.txt` `pytest-report.html` `09-pytest-report.png` | 是 | 数字 37/1 真；时间戳跨跑次 |
| 数据 | `data/minishop.sqlite` | 是 | 种子态：3 用户、3 商品、购物车 3 行、0 订单、无 status 列 |
| 依赖 | `requirements.txt` | 是 | pytest 9.1.1 / pytest-html 4.2.0 / requests 2.34.2 |

Coverage：**100%**。未检查 = 0。Newman / Postman GUI / JMeter GUI / Chrome 手工点页面：环境无 GUI 与 jmeter/newman 二进制，已用 HTTP 等价与截图核验，见 §8。

---

## 2. 闭环覆盖表

判断标准：该环节是否有**独立产物**、是否能指到**可复核证据**、是否与冻结口径一致。

| 环节 | 产物 | 状态 | 验收说明 |
| --- | --- | --- | --- |
| 需求 | `docs/PRD.md` | 有 | 范围/非范围/九条规则清楚。缺口：未写「下单是否来自购物车」 |
| 测试分析 | `requirement-review.md` `test-points.md` | 有 | 状态机进非范围、空搜索→BUG-001、注册不自动登录。TP-SQL-JOIN 无对应 TC |
| 测试计划 | `test-plan.md` | 有 | 入口/出口/风险；P0～P3 标明课程约定；性能明确未加压 |
| 测试用例 | `test-cases.md`（18 条）+ pytest 38 | 有 | P0 主路径有步骤；缺所属者 200、订单超库存、admin 未登录 401 |
| 环境 | README + `run.py setup/serve` | 有 | 本机 `setup` 成功；默认 `MINISHOP_RESET=1` 已披露 |
| 数据 | `server.seed` + sqlite | 有 | 教学账号/库存与 PRD 一致；`data/` 是种子，不是 qty=10 会话后快照（未假装） |
| 功能测试（Web） | 截图 01–07 | 弱 | 登录失败、qty=11 页面证明力强；空搜索图几乎等于商品目录；注册图=登录图 |
| API | pytest + Postman + `evidence/http/` | 有 | pytest 覆盖主契约；Postman 15 条；Cookie 只在 pytest 登录用例，不在集合 |
| SQL | `sql-check.md` + `seed-join.txt` | 有 | 种子 qty 1/2；qty=11 后仍为 10。本机隔离库复现 |
| Bug | `BUG-001.md` | 有 | 步骤/预期/实际/证据齐全；保持开放 |
| 回归 | pytest `xfail(strict=True)` | 有 | 无独立回归计划文档；无已关闭缺陷再测记录（只有 1 条开放缺陷，可接受） |
| 自动化 | `tests/` + `automation/README.md` | 有 | 基线可重复。JMeter 只是骨架 |
| 报告 | `test-report.md` | 有 | 37/1 与仓库输出、本机复跑一致；不声称支付/状态机/性能 |
| 简历表达 | `resume-evidence.md` `project-summary.md` | 有 | 可写/不可写清单正确，未见公司名冒充 |

**闭环完整性：结构 14/14 有产物；深度上权限正例、空搜索 Web 证据、Postman Cookie 未达岗位签章线。**

---

## 3. 契约一致性

### 3.1 OpenAPI ↔ `server.py` 路由

OpenAPI `paths` 与实现 JSON API **一一对应**（9/9）：

`/api/login` POST、`/api/register` POST、`/api/products` GET、`/api/cart` GET、`/api/cart/items` POST、`/api/orders` POST、`/api/orders/{id}` GET、`/api/admin/products` GET、`/api/admin/orders` GET。

未知 `/api/*` 实现 404。静态 `/` `/admin.html` `/app.js` `/styles.css` 不进 OpenAPI，合理。

### 3.2 本机 HTTP（`MINISHOP_PORT=18765` 隔离库）与 PRD

| 冻结点 | 现场 |
| --- | --- |
| 路径 `/api/` | 一致 |
| 登录 200 + JSON `token` + `Set-Cookie: minishop_session=…; HttpOnly; Path=/` | 一致；body 无 `status` |
| 后续 Bearer **与** Cookie 都能取购物车 | 均 200 |
| 错密码 401、无 `Set-Cookie` | 一致 |
| 无凭证：GET/POST cart、POST orders、GET admin、GET order | **全部 401** |
| qty=10 → 200；qty=11 → 400 `qty exceeds stock` 且不落库 | 购物车仍 10 |
| `GET /api/products?keyword=   ` → 三件全量 | **BUG-001 仍开放** |
| 无 keyword → 目录三件；`keyword=鼠标` → 仅 SKU-DEMO-001 | 一致 |
| `POST /api/orders` 201，body **仅** `id` | `{'id': 'ord-…'}`，无 status |
| 所属者 GET 订单 200，`id`+`items`，无 status | **实现有，pytest 无** |
| 用户 B / 管理员读他人明细 | 403，`{"error":"forbidden"}`，不回 id |
| `/api/admin/orders` 元素只有 `id` | 下单后 `{"items":[{"id":"ord-…"}]}` |
| 注册 201 有 phone 无 token；占用 409；非法手机号 400 | 一致 |
| `orders` 表列 | `id, user_id, created_at`，**无 status** |
| v1.0 不做支付/物流/优惠券/状态机/HTTPS | 无对应接口 |

OpenAPI 薄于实现（见 G06-0007）：登录未写 400/Cookie；购物车未写 404 unknown sku；无 `securitySchemes`；`/api/login` 200 描述写成 “no order status field”；R-SEARCH 在 OpenAPI 里只是 200 items，与 PRD 冲突靠 BUG-001 跟踪。

### 3.3 Postman 与 Cookie/401

集合 `item` **恰好 15**。环境 `password`/`token*` 初始为空，仓库无密钥。鉴权头只有 `Authorization: Bearer {{token}}`。

| 检查 | 结果 |
| --- | --- |
| 断言 `Set-Cookie` / `HttpOnly` | **无**（全文无这两个字符串） |
| Cookie 头后续请求 | **无** |
| 401 | 仅「无凭证创建」`POST /api/orders`；本机该条会绿 |
| 空搜索-BUG-001 | 按 R-SEARCH 要求 400 或 `items.length===0`；本机 **会失败**（200 / 3 件） |
| 缺的 OpenAPI 路径 | GET `/api/cart`、GET `/api/admin/*`、所属者 GET `/api/orders/{id}` |
| Newman | 本机无 `newman`；用 requests 按脚本逻辑复现 |

R-AUTH 的 Cookie 半边只在 `test_login_ok` 里测到，**集合不能当 Cookie 契约证据**。

### 3.4 qty=10/11、订单无 status、BUG-001

四处独立证据一致：实现、pytest、HTTP txt、SQL、日志 `inventory reject … qty=11`、截图 05。订单成功响应与表结构都没有 `status`。空搜索仍全量，xfail 名称与缺陷单一致。

---

## 4. 证据诚实性

**数字不假。** 仓库 `evidence/pytest-output.txt`：`37 passed, 1 xfailed in 0.61s`，xfail = `test_empty_keyword_should_not_return_all`。本机 `.venv` pytest（不写 evidence）：收集 38，**37 passed, 1 xfailed**。`pytest-report.html`：37 Passed / 1 Expected failures。截图 09 同数字。

**未把 BUG-001 写成已修复。** 报告、矩阵、缺陷单、Postman description、代码注释一致。

**HTTP 证据像真跑的：** token 打码、空搜索三件、qty=11 400、订单 `{"id":"ord-59b7e410b85d"}` 无其它字段、注册 201 无 token。`curl-login-headers.txt` 为 HTTP/1.0 + HttpOnly Cookie 打码，与 `BaseHTTPRequestHandler` 相符。

**有问题的证据（不够构成造假，但证明力不足或文件名骗人）：**

| 项 | 问题 |
| --- | --- |
| `01-login.png` 与 `06-register.png` | sha256 全同 `910f31b0…`；矩阵把 06 当注册入口证据，实际是未登录首页 |
| `04-search-empty-bug001.png` | 与 03 仅差 12 字节；关键字框空格不可见，「共 3 件」看起来就是目录 |
| `07-admin.png` | 订单「暂无」。根因：`run.py` `capture_screenshots()` **先于** `capture_http_sql_log()` 里的下单 |
| `network-log.html` / `08-network-log.png` | **`run.py` 不生成**；自报「整理表不是 DevTools」，诚实，但不能当自动取证管道产物 |
| `09-pytest-report.png` vs html | 图 09-Sep 10:17:20（607ms）；html 09-Sep 15:36:40。同日不同次，数字相同 |
| html `environment.CI = true` | 声称本机证据，报告指纹像 CI |
| `run.py test` | 把 stdout 写进仓库 `evidence/pytest-output.txt`（CH19 已踩；本审计差点再踩，已还原） |

JMeter / Postman GUI：计划与矩阵写明未点、未加压。骨架存在且未假装有 SLA。诚实。

---

## 5. 简历风险

**未写成公司项目。** 全目录「公司/企业」只出现在禁止句和「非正式公司评审/度量」。无「某某科技」「电商部门核心系统」作为自称。`resume-evidence.md` 不可写清单正确。

仍可能被学生抄进简历的**教学实现细节**（项目未禁止写，但岗位上危险）：

- 密码 `SHA256(固定盐|明文)`，盐写在源码 `minishop-lab-v1`
- Session 无过期、无登出
- Cookie 无 `Secure` / `SameSite`（本机 HTTP 可解释）
- HTTP/1.0
- 下单不走购物车结算

可写模板（与仓库一致，建议保留）：个人项目 MiniShop；PRD/矩阵/pytest；qty=10/11；订单无 status；37 passed / 1 xfailed；BUG-001 开放。不可写：已测通全部订单状态、生产压测、精通 JMeter、独立 CI、加密架构。

---

## 6. 现场执行（2026-09-10）

| 命令 | 结果 |
| --- | --- |
| `python3 --version` | 3.14.3 |
| `cd project/minishop && python3 run.py setup` | `.venv` 已有；pytest 9.1.1 / pytest-html 4.2.0 / requests 2.34.2 |
| `.venv/bin/python -m pytest --collect-only -q` | **38 tests collected**（test_api 23 含 8 组 qty + 1 xfail；register 11；qty_rule 4） |
| `.venv/bin/python -m pytest -q` | **37 passed, 1 xfailed**（未走 `run.py test`） |
| `MINISHOP_PORT=18765` + 隔离 sqlite/log 的 `python3 server.py` | `MINISHOP_BASE_URL=http://127.0.0.1:18765` |
| 进程内 69 项契约探针 | 行为断言 0 FAIL；Postman「无 Cookie 断言」「空搜索会红」为观察项 |
| `sqlite3 data/minishop.sqlite` | 种子；0 订单 |
| newman / jmeter / postman CLI | **未安装** |
| `run.py test` / `run.py evidence` | **故意未跑**（会改仓库证据） |

---

## 7. P0 / P1 / P2 / P3

### P0

无。未发现：把 MiniShop 写成公司项目、把 BUG-001 标已修复、伪造 37/1、订单成功带 `status`、qty=10/11 与 PRD 相反、OpenAPI 路径与实现对不上。

### P1

G06-0001。

### P2

G06-0002～G06-0009。

### P3

G06-0010～G06-0013。

---

## 8. ISSUE 清单

## ISSUE
ID：G06-0001
文件：`project/minishop/tests/test_api.py`；`docs/prd-coverage-matrix.md`；`docs/test-cases.md`
章节：MiniShop v1.0（非教材章）
小节：R-PERM
精确位置：`test_order_forbidden_other_user`、`test_admin_products_ok`；矩阵 R-PERM 三行；用例仅 TC-PERM-001
原文：PRD「`GET /api/orders/{id}` 仅订单所属者可看明细」；矩阵结果「通过」；用例只有 B 读 A → 403
问题等级：P1
问题类别：TEST
问题说明：权限规则只有拒绝路径自动化。所属者 200 且无 `status` 本机手工成立（`{'id','items'}`），但无 pytest / 无 TC。管理员订单列表在种子 0 单时 `all(set(keys)=={"id"})` 对 `[]` 恒真。
为什么有问题：若实现改成「谁都 403」或管理员列表漏出 `status`/`user_id` 却一直空表，现网绿灯仍亮。把 R-PERM 标「通过」作为测试项目验收不成立。ISTQB 访问控制应允许/拒绝成对。
依据：PRD R-PERM；本机 owner GET 200；`test_admin_products_ok` 空列表。
建议修改：补 `test_owner_can_read_own_order`（200，有 id/items，无 status）；管理员用例先下单再断言 items 非空且只有 id。矩阵在补测前不要写「通过」。
推荐替换文本：`TC-PERM-002 所属者读自己的订单 | 200，body={id,items}，无 status`

【Agent Disagreement】Chapter-19 将同一缺口记为 CH19-0006 **P2**（教学缺口）。本 Agent 按项目验收记 **P1**（关键遗漏 + 矩阵结论不准确）。总控裁决：若只评教材是否教错契约 → 可维持 P2；若评「这套测试资产能否签字」→ P1。

## ISSUE
ID：G06-0002
文件：`project/minishop/postman/MiniShop.postman_collection.json`；`MiniShop.postman_environment.json`
章节：MiniShop v1.0
小节：R-AUTH / 401
精确位置：集合 15 条；「登录-正确」脚本；「无凭证创建」
原文：登录只 `pm.expect(json.token)`；后续 `Authorization: Bearer {{token}}`；401 仅 POST `/api/orders`
问题等级：P2
问题类别：TEST / HTTP
问题说明：R-AUTH 要求 JSON token **与** HttpOnly Cookie。pytest `test_login_ok` 测了 Set-Cookie 和纯 Cookie 拉购物车。Postman 全文无 `Set-Cookie`/`HttpOnly`/`Cookie` 头。无凭证 401 未覆盖 GET `/api/cart`、POST `/api/cart/items`、GET `/api/admin/*`、GET `/api/orders/{id}`（实现均为 401）。
为什么有问题：学生若只跑集合，会以为认证=Bearer-only，与「不是三选一」的课程纪律相反。集合不能作为 Cookie 契约或 401 矩阵的充分证据。
依据：集合 JSON 检索；本机 Cookie 购物车 200、无凭证全 401。
建议修改：登录断言 `Set-Cookie` 含 `HttpOnly`；加一条只带 Cookie、不带 Bearer 的 GET `/api/cart`；401 至少再加购物车与 admin。
推荐替换文本：登录脚本增加 `pm.expect(pm.response.headers.get('Set-Cookie')).to.include('HttpOnly')`

## ISSUE
ID：G06-0003
文件：`postman/MiniShop.postman_collection.json`；`tests/test_api.py`；`docs/test-plan.md`
章节：MiniShop v1.0
小节：BUG-001 跟踪策略
精确位置：集合「空搜索-BUG-001」`pm.test`；pytest `@pytest.mark.xfail(..., strict=True)`
原文：Postman `closed = code===400 || items.length===0`；pytest 期望失败
问题等级：P2
问题类别：TEST
问题说明：同一开放缺陷，pytest 套件仍「绿」，Postman Runner 必红。集合 description 有警告，计划只写「GUI 未点」，未写「这条脚本现行失败是缺陷仍开放」。
为什么有问题：用第 14 章方式跑 Runner 会被理解成导入错误。不是造假，是双工具政策未在测试计划里对齐。
依据：本机空搜索 200/3 件；xfail 名称匹配 BUG-001。
建议修改：`test-plan.md` 风险表加一行：Postman 空搜索失败 = BUG-001，不要改断言求绿。
推荐替换文本：`空搜索：pytest xfail 跟踪；Postman 按 R-SEARCH 硬断言，现行失败。`

## ISSUE
ID：G06-0004
文件：`server.py` `_create_order`；`frontend/app.js`；`docs/PRD.md`
章节：MiniShop v1.0
小节：购物车 vs 下单
精确位置：`_create_order` 只扣 `products.stock`，不读不改 `cart_items`；`order-form` submit 后不 `refreshCart`/`refreshProducts`
原文：PRD 范围并列「购物车数量、创建订单」，未写订单来源
问题等级：P2
问题类别：TEST / JOB
问题说明：本机：购物车 SKU-001 qty=10 后下单耳机，购物车仍 qty=10；下单鼠标 11 件接口 400，但合法下单后页面列表库存不刷新。真实电商几乎从购物车结算。
为什么有问题：当完整项目收成却不标明教学简化，面试/简历可能写成「完成购物车结算」。PRD 也没冻结「下单是否必须来自购物车」。
依据：现场 SQL/HTTP；`app.js` 下单成功只写 `订单 id=`。
建议修改：PRD R-ORDER 加「v1.0 直接 POST sku+qty，不经过购物车」。不必改实现。前端可选下单后刷新，属体验非冻结缺陷。
推荐替换文本：`创建订单：直接 POST sku+qty，不读取、不修改 cart_items。教学简化，不是结算流程。`

## ISSUE
ID：G06-0005
文件：`evidence/screenshots/04-search-empty-bug001.png` `06-register.png` `07-admin.png`；`run.py` `evidence()`；`prd-coverage-matrix.md`
章节：MiniShop v1.0
小节：Web 证据
精确位置：`capture_screenshots` 在 `capture_http_sql_log` 之前；矩阵引用 06、07、04
原文：06 当注册证据；07「订单只有 id」；04「空搜索 BUG-001」
问题等级：P2
问题类别：IMG / TEST
问题说明：01 与 06 像素级相同。04 与 03 视觉上同为「共 3 件」、空格看不见。07 订单「暂无」，因为先截后台、后才 HTTP 下单。HTTP txt 足够支撑 BUG-001 和 qty=11；这三张图不能支撑文件名/矩阵声称的事实。
为什么有问题：测试项目的证据链要求「图能证明步骤发生过」。当前 Web 层对空搜索、注册、订单 id 列表是弱证据或错贴标签。
依据：sha256；`run.py` 顺序；本机读图。
建议修改：04 让 keyword 提交可见；07 先下单再截；删 06 或矩阵改指 01；`evidence()` 调整顺序。
推荐替换文本：矩阵页面行改为 `01-login.png`（含注册表单）。

## ISSUE
ID：G06-0006
文件：`run.py` `run_pytest()`；`README.md` 一键 `python3 run.py test`
章节：MiniShop v1.0
小节：环境/证据管道
精确位置：`out = EVIDENCE / "pytest-output.txt"` 无条件覆盖
原文：`python3 run.py test       # pytest`
问题等级：P2
问题类别：CODE
问题说明：教材一键测试会改写已提交的审查证据。本审计用 `python -m pytest` 仍曾看到工作区 0.68s vs 仓库 0.61s（已还原）。`evidence()` 同样重写 http/sql/截图。
为什么有问题：学习者 git status 变脏，可能把本机输出当课程原件提交，或以为自己改坏了仓库。证据目录自称「本机真实跑出来」，与「仓库基线」角色冲突。
依据：`run.py` L61–81；git diff 仅时长/时间戳。
建议修改：默认写 `evidence/local-pytest-output.txt`（gitignore）；只有显式 `evidence --commit-baseline` 才更新仓库文件。README 写明不要提交。
推荐替换文本：`python3 run.py test  # 写到本地临时输出，不覆盖仓库 evidence/`

## ISSUE
ID：G06-0007
文件：`docs/openapi.json`
章节：MiniShop v1.0
小节：冻结契约
精确位置：`/api/login` 200 description；无 `components.securitySchemes`；cart/login 响应码
原文：`"200": {"description": "OK with token; no order status field"}`
问题等级：P2
问题类别：HTTP
问题说明：质量标准冻结「PRD + OpenAPI」。OpenAPI：登录描述在说订单字段；不写 `role`、缺字段 400、Set-Cookie；购物车/订单 unknown sku 404 实现有、文档无；R-SEARCH 只文档 200 items。
为什么有问题：对照 OpenAPI 写用例的人会漏 Cookie/400/404，并可能以为空搜索 200 全量是契约而非缺陷。教学 OpenAPI 可以薄，但这句会把登录和订单搅在一起。
依据：本机登录 400 `missing field`；cart 404 `unknown sku`；PRD R-AUTH/R-SEARCH。
建议修改：登录 200 = token+role+Set-Cookie HttpOnly，body 无 status；补 400；cart 补 404；products 注明空白 keyword 现行全量=BUG-001。
推荐替换文本：见上。

## ISSUE
ID：G06-0008
文件：`server.py` `do_GET`；`frontend/admin.html`；`tests/test_api.py` `test_admin_page_ok`；`test-cases.md` TC-ADMIN-002
章节：MiniShop v1.0
小节：管理员权限
精确位置：`GET /admin.html` 无鉴权；pytest 只断言页面 200 含「只列出 id」
原文：TC-ADMIN-002「管理员打开后台页 | 200，列出库存，订单只有 id | 通过」
问题等级：P2
问题类别：TEST / PED
问题说明：未登录 GET `/admin.html` 仍 200（静态）。数据在 `/api/admin/*`：无凭证 401、普通用户 403。pytest 页面用例不登录。截图 07 是已登录管理员。三者混成一条「通过」。
为什么有问题：权限测试经典坑：页面能打开 ≠ 有数据权限。本机已确认静态 200 + API 401/403 分离。
依据：RFC 9110 403 针对资源请求；现场探针。
建议修改：拆 TC：静态页匿名 200；API 401/403/200。pytest 页面用例不要当成授权通过。
推荐替换文本：`TC-ADMIN-000 匿名 GET /admin.html → 200，接口仍 401`

## ISSUE
ID：G06-0009
文件：`docs/prd-coverage-matrix.md`
章节：MiniShop v1.0
小节：R-PERM 行
精确位置：`R-PERM | 无凭证 401 | TP-AUTH-401 | TC-AUTH-001`
原文：把未认证映射到权限规则
问题等级：P2
问题类别：TERM
问题说明：R-PERM 是越权与管理员；未认证是 R-AUTH。学习目标刚要求 401/403 分开，矩阵把 401 塞进 R-PERM。TC-AUTH-001 标题还只写「无凭证下单」，pytest 另有购物车 401 未进用例表。
为什么有问题：覆盖矩阵是闭环的索引。索引把认证算进权限「通过」，会高估 R-PERM、低估 R-AUTH 的 GET 401 缺口。
依据：PRD 分列；RFC 9110 401 vs 403。
建议修改：无凭证行改挂 R-AUTH；R-PERM 只保留 403 与所属者 200。
推荐替换文本：`R-AUTH | 无凭证改购物车/下单/admin 401 | TP-AUTH-401 | TC-AUTH-001（补 cart/admin）`

## ISSUE
ID：G06-0010
文件：`jmeter/minishop-get-products.jmx`；`evidence/http/network-log.html`；`evidence/pytest-report.html`；`evidence/screenshots/09-pytest-report.png`
章节：MiniShop v1.0
小节：性能骨架与证据指纹
精确位置：JMX 无 `ResponseAssertion`；html `CI: true`；09.png 10:17 vs html 15:36
原文：JMeter comments「Not an SLA」；报告「本机」
问题等级：P3
问题类别：TEST
问题说明：JMeter 1 线程 1 循环打 GET `/api/products`，无断言，本机无 jmeter 可跑。network-log 手整理且 HTML 空格折叠，关键字三个空格在表格里看不见。pytest-html 环境 CI=true；截图与 html 非同一次生成。
为什么有问题：不构成造假（计划写了未加压、08 自报非 DevTools），但「本机证据包」内部时间戳/CI 指纹不一致。
依据：JMX 文本；html 环境块；截图 OCR 时间。
建议修改：JMeter 加 200 断言即可保持骨架；证据包固定一次 `evidence()` 的时间戳；CI 环境变量不要污染本机报告。
推荐替换文本：无强制。

## ISSUE
ID：G06-0011
文件：`docs/test-points.md`；`tests/test_api.py`；`tests/test_qty_rule.py`
章节：MiniShop v1.0
小节：用例完整性
精确位置：TP-SQL-JOIN 无 TC；qty 参数无负数；无 `qty is True`
原文：四态列出缺/null/""/"1"/0
问题等级：P3
问题类别：TEST
问题说明：SQL 核对只有文档+证据文件，没有用例 ID。`qty_allowed` 用 `type is int` 能拒绝 `True`，无测试。PUT/DELETE `/api/products` 本机 501 HTML，OpenAPI 不列，可接受。订单超库存实现 400，无 TC（并入缺口，严重性低于所属者 200）。
为什么有问题：闭环表「测试点→用例」在 SQL 这一行断开。
依据：test-points 18 行 vs test-cases 18 条不对齐 SQL；现场 order qty=11 → 400。
建议修改：TP-SQL-JOIN → TC-SQL-001 指向 `seed-join.txt`；可选补 qty=-1。
推荐替换文本：`TC-SQL-001 Tester A 购物车 JOIN | 鼠标 1/10 键盘 2/5 | 通过 | evidence/sql/seed-join.txt`

## ISSUE
ID：G06-0012
文件：`server.py` `SALT` / `sessions`；`docs/resume-evidence.md`
章节：MiniShop v1.0
小节：简历与安全教学实现
精确位置：`SALT = "minishop-lab-v1"`；sessions 无 expiry
原文：简历可写 pytest/边界；未写「不要把这套哈希当安全设计」
问题等级：P3
问题类别：JOB
问题说明：项目已禁止写成公司系统，未禁止把 SHA256+固定盐、不过期 Session 写成「我做了安全认证」。Cookie 无 SameSite。
为什么有问题：初级简历常见夸大。实现作为教学服务器合格，作为安全范本不合格。
依据：源码；OWASP 密码存储不应用单次 SHA256 固定盐。
建议修改：`resume-evidence.md` 不可写再加「加密架构 / Session 安全设计」。
推荐替换文本：`- 使用 SHA256 固定盐作为「生产级加密」`

## ISSUE
ID：G06-0013
文件：`postman/MiniShop.postman_collection.json`（第一条「注册-合法」）
章节：MiniShop v1.0
小节：集合可重复性
精确位置：`newPhone=13900004444` 固定；注册在集合最前
原文：201 created
问题等级：P3
问题类别：TEST
问题说明：服务默认每次启动重置，单次 Runner 可以绿（除空搜索）。不重置时第二次 409。环境 password 为空是正确的防泄密，但未填则三条登录全 401，description 已提示。
为什么有问题：小摩擦，不破坏基线。
依据：集合顺序；`MINISHOP_RESET` 默认 1。
建议修改：注册用时间戳手机号，或注明必须重置库。
推荐替换文本：集合 description 加「跑 Runner 前重启 serve（RESET=1）」。

---

## 9. 与 Chapter-19 分歧

Chapter-19 审的是**教材第 19 章 + 它声称的项目产物**；本报告只验收**项目仓库**。重叠处独立复跑，结论如下。

| 主题 | Chapter-19 | Global-06 | 裁决建议（总控） |
| --- | --- | --- | --- |
| 37 passed / 1 xfailed | 本机成立 | 本机成立；仓库 txt 0.61s | **同意**，数字真 |
| BUG-001 仍开放 | 同意 | 同意；HTTP/SQL/xfail/Postman 四通道 | **同意** |
| 订单无 status | 同意 | 同意；表也无 status 列 | **同意** |
| qty=10/11 不落库 | 同意 | 同意 | **同意** |
| 非公司项目 | 同意 | 同意 | **同意** |
| Postman 15 条 | 同意 | 同意 | **同意** |
| 所属者 GET 无自动化 | CH19-0006 **P2** | G06-0001 **P1** | **分歧**：项目签字用 P1，教材用 P2。建议总控保留 P1 在项目债、P2 在章内文笔债 |
| 06=01 截图 | CH19-0011 **P3** | G06-0005 **P2**（矩阵当注册证据） | **部分分歧**：文件重复是 P3；当作独立证据是 P2 |
| 07 空订单 / 04 弱图 | CH19-0007 P2 | 并入 G06-0005 P2 | **同意** |
| 401 挂 R-PERM | CH19-0012 **P3** | G06-0009 **P2** | **轻微升级**：矩阵是闭环索引，错挂会错估覆盖 |
| 下单≠购物车 | CH19-0017 P2 | G06-0004 P2，并补「前端不刷新库存」 | **同意并补充** |
| `run.py test` 改证据 | CH19-0008 P2 | G06-0006 P2 | **同意**；本审计已还原误写 |
| Postman 空搜索会红 | CH19-0005 P2（章 19.7 没写） | G06-0003 P2（计划未对齐双工具） | **同意**，落点在项目计划而非课文 |
| Postman 缺 Cookie | 未单列（只写后续 Bearer） | **G06-0002 新问题** | 采纳为项目债 |
| OpenAPI login 文案 | CH19-0015 P3 | G06-0007 P2（冻结双契约） | 可维持 P3 若认定 OpenAPI 仅为索引；项目验收偏 P2 |
| 订单超库存无 TC | 未单列 | G06-0011 提及 | 新缺口，P3 |
| pytest-html CI=true、09.png≠html 时刻 | 未报 | G06-0010 | 新问题，P3 |
| network-log 非 run.py 生成 | 未报（当诚实整理表） | G06-0010 | 同意「不假」，补管道缺口 |
| CH19-0001 qty=1 现在时 | 章内文笔 | **不审** | 交章 Agent / Global-01 |
| CH19 无 P0/P1 | 「不会教错冻结契约」 | 项目有 **1 个 P1** | 不矛盾：教错 ≠ 测试资产签章 |

Chapter-19 结论「B 小修 / 81 分」针对课文。对仓库本身：主契约可跑、数字诚实；**测试资产不能声称 R-PERM 已完整通过**。

---

## 10. 实现与测试质量（非 ISSUE 的观察）

合格处（验收加分，不另开单）：

- 参数化 SQL；`type(qty) is not int` 拒绝 bool 冒充
- 下单 `BEGIN` + `UPDATE … AND stock >= ?`，冲突 409
- 403 体不含他人 id
- 注册 201 不签发 token
- pytest：session 临时库 + autouse `reset_db`，隔离干净
- xfail `strict=True`：BUG-001 若被悄悄「修掉断言」会 xpass 变红
- 前端登录刷新商品调用 `refreshProducts()` 不传空串，避免登录即触发 BUG-001（`test_home_has_login_and_register_form` 锁住）

教学简化（已在非范围或可接受）：无支付、无状态机、无 HTTPS、HTTP/1.0、单机 SQLite、每次启动重置。

---

## 11. 建议（只建议，未改仓库）

1. 补所属者读单与管理员非空订单列表自动化，矩阵在此之前不要写 R-PERM 通过。
2. Postman 补 Cookie/401；计划写明空搜索 Runner 红 = BUG-001。
3. PRD 写明下单不走购物车。
4. 重拍 04/07，去掉 06 或改引用；`evidence()` 先下单再截后台；`run.py test` 不要覆盖仓库基线。
5. OpenAPI 补 Cookie/400/404 与 BUG-001 注释。
6. 简历不可写再加「安全架构」。

不建议：为了集合全绿去改空搜索断言；把 JMeter 1 循环写成性能结论；把 MiniShop 写成公司项目。

---

## 12. 项目结论

作为**课程个人测试实践项目**：通过。能跑、能指、数字真、缺陷真、范围真、简历口径真。

作为**初级测试工程师交付的项目包**：有条件通过。缺权限允许路径、Web 空搜索/注册/后台订单图证明力不足、Postman 未落实 Cookie 契约、一键 test 会污染证据。这些不够构成 P0 教错，但够挡住「测试已覆盖 R-PERM / 证据链完整」的签字。

---

## 13. 执行记录

读过：`reviews/_full-audit-2026-09-10/GLOBAL_AGENT_BRIEF.md`、`AUDIT_AGENT_BRIEF.md`、`AGENT_MAP.md`、`AUDIT_PROGRESS.md`、`CHAPTER_19_AUDIT.md`、`REPOSITORY_INVENTORY.md`、`standards/QUALITY_STANDARD_v1.0.md`、`docs/COURSE_CONTROL.md`、`docs/LEARNING.md`（MiniShop 句）、`project/README.md`。

项目：`project/minishop/` 下 README、`run.py`、`run.sh`、`run.bat`、`server.py`、`pytest.ini`、`requirements.txt`、`frontend/*`、`docs/*`（PRD、OpenAPI、计划/点/用例/矩阵/评审/SQL/报告/总结/简历）、`bugs/BUG-001.md`、`tests/*`、`postman/*`、`jmeter/*`、`automation/README.md`、`evidence/**`、`logs/app.log`、`data/minishop.sqlite`。

截图 9 张均用 `read_file` 打开。

跑过：`run.py setup`；venv pytest collect + `-q`；隔离端口 `server.py`；OpenAPI/Postman/SQL/HTTP 探针脚本；`sqlite3` schema；sha256；git diff 后 **checkout 还原** evidence。

未跑：`run.py test`、`run.py evidence`、Postman GUI、Newman、JMeter、浏览器手工（截图+API 已核）。

外部：RFC 9110 401/403/201/409 用法与实现一致；pytest-html 4.2.0 / pytest 9.1.1 与 requirements 钉死版本一致。未把 GET/POST 安全神话、Cookie/Session/Token 三选一写进本项目正说。
