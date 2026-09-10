# VERIFY P0 / P1

- 角色：独立 Verification Agent（修复者 ≠ 验收者）
- 日期：2026-09-10
- 范围：`MASTER_AUDIT.md` 的 **MASTER-P0-001** 与 **M-P1-02…36**（M-P1-01 已升 P0，不单列）
- 方法：对照 `FIX_PLAN.md` / 若干 `fix-records/`，**打开修复后正文、图、集合、测试**取证；不采信 FIX RECORD 单独结案
- 硬约束：未改 `chapters/`
- 本机 pytest（2026-09-10）：`cd project/minishop && .venv/bin/python -m pytest -q` → **38 passed, 1 xfailed**（xfail = `test_empty_keyword_should_not_return_all` / BUG-001）

## 0. 结论

P0/P1 **没有 FAIL、没有 REGRESSION**。  
**34 PASS / 2 PARTIAL**（M-P1-32、M-P1-34）。  
主线（假登录缺陷、冒烟动词、Cookie 401、四态 sku、disableCookies、`lastOrderId`、`get_by_role`、所属者 200）已在学生会抄的正文/资产里落地。未关账的是：所属者用例加上之后，**学生可见截图/口播仍写 37**；以及 M-P1-34 的 **缺陷工具点击** 未做（Git PR 已做）。

## 1. 总表

| ID | 主题 | 裁决 | 一句话 |
| --- | --- | --- | --- |
| MASTER-P0-001 | 种子账号演登录失败 | **PASS** | Test1234 成功；失败用 Test1234x；开放缺陷钉 BUG-001 空搜索 |
| M-P1-02 | 冒烟「加入购物车」 | **PASS** | 3.6 / 答案 4 已是更新数量 / 创建订单 |
| M-P1-03 | 3.8 空格「异常提示」 | **PASS** | 改为返回全量 + BUG-001；无「异常提示」 |
| M-P1-04 | 第 4 章作业三套规格 | **PASS** | 只指向一份 `template.md`；矩阵「不落库」标实现观察 |
| M-P1-05 | 判定表图文；状态机过星 | **PASS** | 正文+PNG 注册 201/400/409；锁定/优惠券降星且不算过关 |
| M-P1-06 | 06B 练习 10 答成 qty=11 | **PASS** | 确认/回归对象改回 BUG-001 空搜索 |
| M-P1-07 | test-plan 出口混三套 P0 | **PASS** | 出口只写用例 P0～P3 + 缺陷 S1/S2 |
| M-P1-08 | example.test 写成 MiniShop 网址 | **PASS** | 教学 URL 标明不是仓库地址 |
| M-P1-09 | 不带 Bearer ≠ 401 | **PASS** | 401 = 无 Bearer **且** 无 Cookie |
| M-P1-10 | GET /api/orders 无 id → 表写 401 | **PASS** | 正文写 404；`server.py` 无集合 GET |
| M-P1-11 | 空搜索截图 ≈ 目录 | **PASS** | caption 禁止当证据；主证据改 HTTP `keyword=` |
| M-P1-12 | 「数量保持合法值」 | **PASS** | 列表 qty=1；输入框可仍 11（落在 08A，非 08B） |
| M-P1-13 | keyword=mouse 空列表 | **PASS** | 图/11/14 改为无 query 或 `keyword=鼠标`；PNG 已重截 |
| M-P1-14 | Preserve log / Timing / 限速 | **PASS** | 登录是 hidden；Timing 现名；localhost 限速已写 |
| M-P1-15 | 种子图 / sku 当 PK / sqlite 第一帧 / INSERT 无事务 | **PASS** | HTML+PNG 主键是 id；12A 有 sqlite3；12.12 包 BEGIN/ROLLBACK |
| M-P1-16 | 四态图缺 sku | **PASS** | HTML 与 PNG 四格均含 `SKU-DEMO-001` |
| M-P1-17 | 纸面无 Content-Length；实装 HTTP/1.0 | **PASS** | 登录报文 CL=45；注明 curl 会加、实装 HTTP/1.0 |
| M-P1-18 | Cookie jar 把 401 打成 201 | **PASS** | 「无凭证创建」`disableCookies: true`；正文同步 |
| M-P1-19 | orderId vs lastOrderId | **PASS** | 14 章无环境变量名 `orderId`；集合/env 为 `lastOrderId` |
| M-P1-20 | 先手建、第 6 步、只断言数组 | **PASS** | 先导入；无「第 6 步再创建订单」；列表断言 sku |
| M-P1-21 | venv 图立刻 pip install -r | **PASS** | 图只留 venv + pip list；第 19 章再装 |
| M-P1-22 | getByRole 非 Python | **PASS** | 表与示例均为 `get_by_role` |
| M-P1-23 | P95 图注串台；无算例 | **PASS** | 五样本最近秩 P95=800；caption 不再串并发 |
| M-P1-24 | 教学服务 qty=1 现在时 | **PASS** | 19/20/22/测验 6 均为过去时「已删除」 |
| M-P1-25 | 可背范文 + 测验 Q8 互斥 | **PASS** | 20.4–20.14 改提纲；Q8 改回五段 |
| M-P1-26 | 简历可抄；未禁独立开发 | **PASS** | 强制仓库路径槽；禁「独立开发教材」 |
| M-P1-27 | 分层命名打架 | **PASS** | 22.2 五套名字对照表 |
| M-P1-28 | 自检空表可抄 37 passed | **PASS** | 有 `cd` 命令；禁止抄 37 |
| M-P1-29 | 2-1 与 run.py 不同构 | **PASS** | 表标 📖；`run.py 2-1` 提示书面、不启动 |
| M-P1-30 | 08A 验证码进优先检查 | **PASS** | 优先 6 条无验证码；标明仅草案 |
| M-P1-31 | run.py 无工作目录 | **PASS** | 16 索引 / 16A/B / 测验 5 Q9 / 18.7 均有 `cd project/minishop` |
| M-P1-32 | 缺所属者 GET 200 | **PARTIAL** | 用例已加且本机 38/1；学生可见 PNG/口播仍写 37 |
| M-P1-33 | 默认能使用 Postman/DevTools | **PASS** | 绑 exercises GUI 产物；否则了解/用过 |
| M-P1-34 | Git 无 PR；缺陷工具无点击 | **PARTIAL** | 2.9 + 22.2 已有 fork/branch/PR；禅道/Jira 仍无点击 |
| M-P1-35 | 测验 3 Q5 无 token=401 | **PASS** | 401=无 Bearer 且无 Cookie；仅缺 Authorization 可能 201 |
| M-P1-36 | 登录慢改 session | **PASS** | 已删「改成 session」建议；改为清库下禁止改 session |

计数：PASS 34 · PARTIAL 2 · FAIL 0 · REGRESSION 0。

---

## 2. 必抽核（任务指定）

### 2.1 第 1 章场景（MASTER-P0-001）→ PASS

打开 `chapters/01-software-testing-intro.md` L39–46：

- 正确密码 **Test1234**：「这组凭证在仓库里**会登录成功**，不是开放缺陷」
- 失败观察用错误密码 **`Test1234x`**
- 「仓库里真正仍开放……是空搜索返回全量商品（BUG-001）」

`chapters/assets/diagrams/ch01-static-dynamic.png` 已与 HTML 对齐（目视）：动态卡写错误密码 Test1234x → 登录失败；正确密码 Test1234 会成功；开放缺陷是空搜索 BUG-001。FIX RECORD 写「PNG 未重截」**已被现状推翻**。

对照：`tests/test_api.py` `test_login_ok` 用 Test1234 → 200；`test_login_wrong_password` → 401。

### 2.2 第 3 章冒烟 + 3.8（M-P1-02 / 03）→ PASS

`chapters/03-software-testing-classification.md`：

- L218 冒烟：首页打开、登录、商品加载、**能更新合法数量、能创建订单**
- L413 答案 4：同上，并写「不要写加入购物车/结算」
- L238 3.8：连续空格后**仍返回全量商品**（BUG-001 仍开放），**不是**「异常提示」
- 章内「加入购物车」仅余工作实战禁止句（L304）

第 7 章 combo 教学页仍有「加入购物车」，正文已声明不代表 MiniShop，**不在本条范围**（属 combo HTML 示例）。

### 2.3 Cookie 401 + GET /api/orders 404（M-P1-09 / 10）→ PASS

`chapters/08b-web-auth-permission.md` L176 / L183：

- 401：无 Bearer **且** 无 Cookie `minishop_session`
- 只去掉 Authorization、Cookie 还在 → 仍可能 200/201
- **没有** `GET /api/orders` 列表接口，打它是 **404**，不是 401

`project/minishop/server.py` L232–242：仅 `path.startswith("/api/orders/") and path != "/api/orders/"` 进 `_get_order`；`/api/orders` 与 `/api/orders/` 走 404。

### 2.4 测验 3 Q5（M-P1-35）→ PASS

`chapters/quizzes/stage-3-web.md` L22：

> 401：……无 Bearer **且** 无 Cookie `minishop_session`……仅缺 `Authorization`、浏览器仍带着 Cookie 时，MiniShop 仍可能 201。

与 08B / R-AUTH Cookie 回退同口径。

### 2.5 四态图每格有 sku（M-P1-16）→ PASS

`chapters/assets/diagrams/ch13-four-shapes.html` 四格：

1. `{"sku":"SKU-DEMO-001"}` → missing qty  
2. `{"sku":"SKU-DEMO-001","qty":null}` → null qty  
3. `{"sku":"SKU-DEMO-001","qty":""}` → wrong type qty  
4. `{"sku":"SKU-DEMO-001","qty":"1"}` → wrong type qty  

对应 PNG 目视四格均含 `SKU-DEMO-001`，无裸 `{"qty":null}`。

### 2.6 disableCookies + lastOrderId（M-P1-18 / 19）→ PASS

- `MiniShop.postman_collection.json` L200：「无凭证创建」`"protocolProfileBehavior": {"disableCookies": true}`，无 Authorization
- `chapters/14-postman.md` L117：无凭证 = 不要 Authorization **且**关 cookie jar
- `chapters/14-postman.md` 全文检索 **无** 环境变量名 `orderId`
- env JSON 仅 `lastOrderId`；越权 URL `{{baseUrl}}/api/orders/{{lastOrderId}}`

### 2.7 第 16 章无「改成 session」（M-P1-36）→ PASS

`chapters/16b-pytest-fixtures.md` L60：**禁止**在 autouse 清库下把 `token_a` 改成 `scope="session"`。  
已删除原建议「登录很慢时再改为 session」。练习 5 答案同步禁令。仓库 `conftest.py` 未改 `token_a` 为 session。

（正文仍出现「不要改成 session」禁令句，这是修复本身，不是原问题复现。）

### 2.8 get_by_role（M-P1-22）→ PASS

`chapters/17-automation-overview.md` L135 表：Python `get_by_role` / `get_by_label` / `get_by_test_id`；注明 JS 文档才是 `getByRole`。L147 示例 `page.get_by_role("button", name="登录")`。

### 2.9 pytest 38/1（本轮加所属者）→ 代码 PASS，资产 PARTIAL（见 M-P1-32）

本机：

```
XFAIL tests/test_api.py::test_empty_keyword_should_not_return_all
38 passed, 1 xfailed in 1.52s
```

`test_owner_can_read_own_order`：所属者 `GET /api/orders/{id}` → 200，有 id/items，**无 status**。  
`practice/16-pytest-regression/main.py` / `19-project-pack/main.py` 门闩已改为 `"38 passed"`。  
`evidence/pytest-output.txt` 末行 `38 passed, 1 xfailed`。

未关账：`chapters/assets/09-pytest-report.png` 汇总仍是 **37 Passed / 1 Expected failures / 38 tests**；`20-interview.md` L91 口播仍写「pytest 有 **37 通过**」；`ch19-workbench.html` caption 仍写 37。

---

## 3. 逐条证据（其余 P1）

### M-P1-04 PASS

- `04b` L159：只复制 `practice/04-requirement-review/template.md`，不要另做第二套表；已无「四份内容」
- `template.md` 有「已确认规则」三列，禁止把不落库/验证码抄进该表
- `prd-coverage-matrix.md` L13：qty=11 拒绝（PRD）；不落库为实现观察

### M-P1-05 PASS

- 5.9 Markdown 与 `ch05-decision-table.png` 同为注册占用：201 有 phone 无 token / 400 / 409
- 5.10 / 5.15 标 ⭐⭐ 加分，**不是** MiniShop 过关
- 完成标准 L562：状态迁移/锁定不算过关
- 5.14 方法节仍 ⭐⭐⭐，但正文写明锁定模型不算过关、v1.0 无状态机——符合「降星倒逼」原修复，不判 PARTIAL

### M-P1-06 / 07 PASS

- 06B 答案 10：对象是 6-1 / BUG-001 空搜索，不是 qty=11
- `project/minishop/docs/test-plan.md` L28–33：出口只写**用例**优先级 + 缺陷严重程度；不要把「P0 缺陷」写进同一句
- 06B L108 同步

### M-P1-08 PASS

`07-web-basics.md` L45–48：`shop.example.test` 是**教学 URL**，**不是**仓库地址，本机通常打不开。L211 再次声明不是仓库测试环境。本机地址是 `http://127.0.0.1:8765/`。

### M-P1-11 PASS

FIX_PLAN 允许「正文改指 HTTP；caption 不假装」。08A L319、第 10 章 L410、第 19 章 L181 均写：`04-search-empty-bug001.png` 几乎等于目录，**不能**当空搜索证据；主证据 `evidence/http/03-products-empty-keyword.txt`（`keyword=%20%20%20`）。图未 REPLACE，但原 P1 的「假装已提交空关键字」已拆掉。

### M-P1-12 PASS

FIX_PLAN 写 08b，实际落点 08A L320 / L399：列表/接口保持提交前 `qty=1`；输入框可仍 11。08B 无该练习。内容正确，不因路径笔误降级。

### M-P1-13 PASS

- `ch09-get-post.html` / PNG：`GET /api/products?keyword=鼠标`（目视 PNG 已重截，FIX_LOG「PNG 待重截」过时）
- 09A L277：教学 `keyword=mouse` 解绑 `/api/`
- 11.13：无 query 预期 3 件；明确不要 `keyword=mouse`
- 14.2 / 14.5：`keyword=鼠标` + 断言 `items[0].sku == SKU-DEMO-001`

07/08A 教学 URL 仍含 `keyword=mouse`，已标明非仓库 MiniShop，不构成本条失败。

### M-P1-14 PASS

第 10 章：登录是同页 `hidden` 切换，Preserve log 不是登录必选项；清空演示用「后台」`/admin.html`。Timing 现名 **Waiting for server response**。localhost 限速下接口 Waiting 常常仍短。

### M-P1-15 PASS

- `ch12-tables.html`+PNG：教学库三表；用户 3 是 002/NULL，禁止当 v1.0 Admin
- `ch12-pk-fk.html`+PNG：主键是 `id`；sku 是 UNIQUE 不是 PK
- 12A L153：`sqlite3 ~/minishop-sql-lab.sqlite` 第一帧
- 12B 12.12：INSERT 耳机包在 `BEGIN`…`ROLLBACK`

### M-P1-17 PASS

13.12 纸面请求含 `Content-Length: 45`（Body `{"phone":"13800138000","password":"Test1234"}`）；注明 `curl -d` 会自动加。响应说明实装 `HTTP/1.0`。09B 同步。

### M-P1-20 PASS

14.2：「先按 14.6.1 导入……不要新建一套 `/api/login`」。章内无「新建 Request」动作、无「第 6 步再创建订单」。14.7：集合只有一条创建订单，不幂等用**复制**该请求。列表脚本断言 sku。  
（14.6.1 逐步操作第 6 步是「打开 Collection」，不是旧教案的「再创建订单」。）

### M-P1-21 PASS

`ch15-venv.html`+PNG：中间格 `python3 -m venv .venv` 后 `pip list`，本章只该看到 pip；右格「第 19 章再装」。无立刻 `pip install -r`。

### M-P1-23 PASS

`ch18-p95.png`：五柱 100/110/120/200/800，标 P50=120、尾部 P95=800。18.2 最近秩算例与练习 2 答案一致。不再把 P95 图注接到并发≠TPS。

### M-P1-24 PASS

- 19 错误 2 / 练习 2：教学桩**已删除**，不要另找服务器
- 20.3 边界 / 错误 8：过去时
- 22.1 / 错误 2：过去时
- 测验 6 Q5：qty=10 允许、11 拒绝；不要找第二台服务器
- `ch19-qty-rule.html` caption：曾经有过 `/login`+qty=1，现行已删

### M-P1-25 PASS

20.4 节首：「答题提纲，不是背稿」。各域改为五行关键词。测验 7 Q8 改回五段并映射 STAR。工作实战加非 MiniShop 90 秒现场测、禁连续粘贴。  
残留：20.2 自我介绍仍有一段可抄口播，且数字是 37——记入 M-P1-32，不把本条打回 FAIL（原 P1 核心是 20.4–20.14 满分段 + Q8 结构）。

### M-P1-26 / 33 PASS

21.3：Postman/DevTools **不要默认写会做**；绑 `exercises/` Runner/Network，否则了解或用过作者集合。对照 `STATUS` 10-1/14-1 Incomplete。  
21.4：四行必须指向仓库路径；禁止「独立开发 MiniShop 前后端」。作业模板有「路径：」槽，完成标准含该禁止句。

### M-P1-27 / 28 PASS

22.2 对照表五行：大纲三梯队 / 必须掌握 / 高频使用 / 了解即可 / 星级。22.3 标题标明「不是第二梯队」。  
结课自检：`cd project/minishop && python3 run.py test`；「不要抄……包括 37 passed」。

### M-P1-29 PASS

根 README 2-1 标 📖「章内作业，无脚本」。`practice/run.py` 将 2-1 列入书面 ID，命令打印「没有可运行脚本」且不启动程序（FIX RECORD 称退出码 2）。`docs/LEARNING.md` / `practice/README.md` 同步。

### M-P1-30 PASS

08A 8.10 MiniShop 优先检查 6 条无验证码。L289：验证码只在第 4 章草案，**不是**优先检查项。

### M-P1-31 PASS

- `chapters/16-pytest.md` L10：`cd project/minishop && python3 run.py test`
- 16A L163–164、L261–263：setup/serve/test 前有 `cd project/minishop`
- 16B 工作实战 bash 块同样有 cd
- 测验 5 Q9：`cd project/minishop && python3 run.py setup && python3 run.py test`
- 18.7：先 `cd project/minishop` 再 `python3 run.py serve`

### M-P1-32 PARTIAL

已修好：

- `test_owner_can_read_own_order` 存在且断言 200 / 无 status
- 本机与 `evidence/pytest-output.txt`：**38 passed, 1 xfailed**（收集 39）
- 16-1 / 19-1 门闩、第 16/19/21 章审查数字、根 README 已改 38/1

未关账（学生会看见）：

| 落点 | 现状 |
| --- | --- |
| `chapters/assets/09-pytest-report.png` | 38 tests，**37 Passed**，1 Expected failure |
| `chapters/20-interview.md` L91 | 「pytest 有 **37 通过**」 |
| `chapters/assets/diagrams/ch19-workbench.html` caption | 「**37 passed** / 1 xfailed」 |

FIX RECORD 已承认 PNG 需重截、第 20 章未改数字。所属者正例本身成立，故不是 FAIL；基线宣传未收口，故 **PARTIAL**。

### M-P1-34 PARTIAL

已修好（G08-0004）：

- 2.9：fork/空仓 → `git switch -c` → 一次 commit → **自己仓 PR**；警告 fork 后默认指向上游
- 22.2 必须掌握表增加「Git 协作（branch / PR）」行，指向 2.9

未修（G08-0005，MASTER 同行「缺陷工具无点击」）：

- 06A 6.9 仍写「不讲解容易过时的按钮路径」
- 无 Jira 免费云 / 禅道一次建单+流转练习
- FIX_PLAN 本行只排了 Git；「可选免费云工单」未落地

Git 半页已够初级 JD 的 clone/PR；缺陷工具仍是对照表口头课。故 **PARTIAL**，不是 FAIL。

---

## 4. 与 FIX_PLAN / FIX RECORD 的差异

| FIX 声称 | 独立核验 |
| --- | --- |
| 若干 PNG「待 Coordinator 重截」 | ch01 / ch05 / ch09 / ch12×2 / ch13 / ch15 / ch18 **已经**与 HTML 同文，按现状 PASS |
| M-P1-32 FIXED | 测试与 38/1 真；PNG/口播未收口 → **PARTIAL** |
| M-P1-34 FIXED | 只关 Git；缺陷工具点击未做 → **PARTIAL** |
| M-P1-12 文件 08b | 实际在 08A，内容对 |
| M-P1-36「删改成 session」 | 建议已删；禁令句仍含该短语（合格） |

无发现把已修内容改回错误口径的 REGRESSION。

## 5. 不在本轮 P0/P1、不升格

- 第 7 章 combo「加入购物车」（教学页，已声明非 MiniShop）
- 04B 教学草案里的「加入购物车」（故意的坏需求）
- 06B「加购」动词（MASTER 记 M-P2-08）
- 09-pytest-report 裁掉 Environment 明细（M-P2-10）；本报告只因与 38/1 数字冲突记入 M-P1-32
- 越权 Postman 断言 `json.id` 空转（RT03，非本表）

## 6. 发布建议

P0 已关。P1 主尺子（oracle / Cookie / sku / 变量名 / 冒烟动词）已关。  
发布前若只补两处：**重截 `09-pytest-report.png` 并扫掉正文 37 通过**；**决定 M-P1-34 缺陷工具是做一次云工单还是从 MASTER 行里删掉 G08-0005**。其余 P1 可标 VERIFIED。
