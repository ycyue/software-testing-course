# Chapter 19 Audit

- 审计员：Chapter-Audit-Agent-19
- 日期：2026-09-10
- 范围：`chapters/19-minishop-project.md` 及其声称的项目产物（`practice/19-project-pack/`、`project/minishop/`、阶段测验 6 中第 19 章题、示意图与截图）
- 不扩审：第 1–18、20–22 章正文（仅在本章声称「13–16 已打 v1.0」时对照本章内部口径）
- 依据：`AUDIT_AGENT_BRIEF.md`、Quality Standard v1.0、PRD v1.0 / OpenAPI、ISTQB 口径仅用于「不要绝对化」检查、RFC 9110（401/403/201/409）
- 旧审查（`chapter-19-review.md` 99→96、`_rereview` 93、`_pedagogy/ch19.md` 22/30）只作线索，分数不继承

## 1. Coverage

本章及「它声称的项目产物」全量阅读；未检查必须为 0。生成物 `evidence/pytest-report.html` 只核摘要数字与 38 条收集名单，不把 HTML/JSON blob 当作者正文逐字节审。

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 章内 H2 小节 | 24 | 24 | 0 |
| 章内 H3 小节 | 26 | 26 | 0 |
| 正文段落 / 列表项（章内） | 全部 | 全部 | 0 |
| 章内表格 | 2（目录、种子 JOIN） | 2 | 0 |
| 章内代码围栏 | 9 | 9 | 0 |
| 章内图片引用 | 10 | 10 | 0 |
| 章内 Markdown 链接 | 6 | 6 | 0 |
| 学习目标条目 | 8 | 8 | 0 |
| 常见错误 | 10 | 10 | 0 |
| 面试问答 | 5 | 5 | 0 |
| 小练习 + 答案 | 10 + 10 | 20 | 0 |
| 检查清单 + 门槛 | 9 + 4 | 13 | 0 |
| 阶段测验 6 题 + 答案 | 10 + 10 | 20 | 0 |
| Practice 19-1（README / main.py / test_lab.py） | 3 | 3 | 0 |
| MiniShop 文档（README、PRD、OpenAPI、计划/点/用例/矩阵/评审/报告/SQL/总结/简历） | 12 | 12 | 0 |
| MiniShop 测试（conftest + 3 个 test_*.py） | 4 文件 / 38 collected | 38 | 0 |
| MiniShop 实现（server.py / run.py / frontend×4 / pytest.ini / requirements / run.sh / run.bat） | 11 | 11 | 0 |
| Postman 集合 + 环境 | 15 请求 + 10 变量 | 全部 | 0 |
| BUG-001 | 1 | 1 | 0 |
| HTTP 证据 txt | 9 | 9 | 0 |
| SQL / 日志 / linux 证据 | seed-join、app-sample、pwd-ls、grep、df、curl 头、network-log.html | 全部 | 0 |
| 截图 PNG（assets = evidence，9 张） | 9 | 9 | 0 |
| 示意图 HTML+PNG（workbench / qty-rule / cross-check） | 6 | 6 | 0 |
| JMeter 骨架 | 1 | 1 | 0 |
| automation/README | 1 | 1 | 0 |
| 可运行命令（setup / 19-1 / venv pytest / 进程内 HTTP） | 见 §18 | 已跑 | 0 |

**Coverage：100%。** 未检查 = 0。

冻结口径现场核对（不是抽样结论）：

| 冻结点 | 结果 |
| --- | --- |
| 路径 `/api/` | server / OpenAPI / Postman / pytest / 证据一致 |
| qty=10 允许、qty=11 拒绝且不落库 | `qty_allowed(10,10) is True`；`qty_allowed(11,10) is False`；HTTP 200/400；购物车仍为 10 |
| 订单成功 201 仅 `id`、无 `status` | 实现、OpenAPI、pytest、Postman、`06-order-create.txt` 一致 |
| BUG-001 仍开放 | 空白 keyword 仍回三件商品；xfail `strict=True`；缺陷单含「保持开放 / 不在报告里写成已修复」 |
| pytest 基线 37 passed / 1 xfailed | 本机系统 Python 与 `.venv` 各跑一次，均为 37/1；收集 38 |
| MiniShop 只作个人实践 | 章、PRD、README、总结、简历证据均约束；未见公司名 |
| v1.0 不做支付/物流/优惠券/状态机/HTTPS/生产部署 | PRD 非范围 + 实现无对应接口 |
| Cookie + Bearer 同时下发，后续以 Bearer 为准 | 登录 `Set-Cookie HttpOnly` + JSON `token`；前端带 Bearer；服务端两者都能认 |
| 401 / 403 分开 | 无凭证 401；他人订单与非管理员 403（RFC 9110） |
| P0/P1 标明课程约定 | 计划、用例、缺陷单均有 |
| 未把 pytest 绿写成性能结论 | 错误 8、可运行性说明、计划「未加压」 |
| 未使用 GET/POST 安全神话、Cookie/Session/Token 三选一 | 错误 7、练习 9C |

## 2. 总评分

核心章从严。仓库能跑、数字能对上，不等于正文已达 95。

| 项 | 分 |
| --- | ---: |
| 技术准确性 | 8/10 |
| 岗位实用性 | 8/10 |
| 完整性 | 8/10 |
| 初学者友好度 | 7/10 |
| 教学顺序 | 8/10 |
| 代码质量 | 8/10 |
| 实操质量 | 8/10 |
| 练习质量 | 9/10 |
| 图片质量 | 7/10 |
| **总体** | **81/100** |

对照 Quality Standard：核心章目标 95 **未达到**；发布线 90 **未达到**。DoD 约 18/20（前置跳转、非范围/示意图口径、空搜索截图证明力不足）。结论见 §17。

扣分主要来自：章内「13–16 已打 v1.0」与示意图/错误 2 的 qty=1 叙事对打；19.3 仍是指针；空搜索截图几乎等于商品目录页；所属者读自己订单未落用例；Postman 空搜索会红、pytest 用 xfail，章内未对齐。

## 3. P0

无。未发现会把学生教错的冻结契约错误，未发现把 MiniShop 写成公司项目，未发现把 BUG-001 写成已修复，未发现伪造 37/1。

## 4. P1

无。上一轮 rereview 的 S6-01（Postman 9≠15）现行正文已改为 15，本机集合 `item` 恰好 15。S6-02/S6-03（覆盖句缺注册、计划商品列表无 TC）现行正文已补。pytest 命令已改为 `run.py test`。这些不再记为现行债。

仍有多项 P2 会卡住「打开文件后第一眼看什么」和「这张图到底证明了什么」，但还不到「会把学生教错」。

## 5. P2

见 CH19-0001～CH19-0010、CH19-0017。

## 6. P3

见 CH19-0011～CH19-0016。

## 7. 逐段问题

### 标题 / 一句话核心 / 重要级别

一句话核心「把观察、判定、证据收成一套能指给人看的项目」能当过滤器，挡住再讲一遍接口、编公司名/状态机。全章 ⭐⭐⭐ 作为收成章诚实；把 Linux/SQL/Postman 也标必须掌握，与「11 与 12 并列、互不为硬前置」不对称，见 CH19-0004。

### 这一章解决什么问题

收口定位正确。声明个人实践、不要把第 4/5 章验证码/优惠券/支付写进本项目，符合冻结口径。

**问题：** 同段写「第 13～16 章可运行示例已经打本仓库 MiniShop：路径带 `/api/`，`qty=10` 允许、`qty=11` 拒绝」，与 19.2 示意图标题、错误 2、练习 2 的「教学服务只让 qty=1」对打。见 CH19-0001。

### 学习目标

8 条覆盖启动、PRD、裁剪、计划、四通道、Postman/pytest、BUG-001、简历。后 3 条在正文和仓库里有锚点；「解释为什么裁掉状态机」「按计划执行 P0/P1」在 19.3/19.4 几乎只有路径。见 CH19-0003。

### 前置知识

仍是「已完成第 1～18 章中与本项目相关的技能」，没有已做/没做跳转。见 CH19-0004。

### 场景导入 + mermaid

面试官要看的五件东西与仓库一一可指。mermaid：PRD → 评审计划 → 用例执行 → 四通道 → pytest/Postman → 缺陷报告 → 总结简历，顺序合理。教学密码纪律正确。

### 19.1 项目声明与目录

目录表现行已含 `jmeter/`（上一轮 S6-06 已修）。启动命令与 README 一致。`MINISHOP_RESET=1` 与 `serve()` 默认一致。

「边看仓库边做」五步已插入，19-1 被明确写成只锁基线——上一轮 P19-02/P19-03 的一半已落地。`docs/` 一行仍把评审/矩阵/SQL/总结/简历挤没了，见 CH19-0013。

`python3 run.py test` 会**改写**仓库内 `evidence/pytest-output.txt`。见 CH19-0008。

### 19.2 PRD v1.0

已确认规则与 PRD 表一致（手机号、密码、R-CART-10、R-AUTH、R-ORDER、R-PERM、R-SEARCH）。qty 示意图数字 10/11 正确。

非范围句短于 PRD。见 CH19-0002。示意图 caption 见 CH19-0001。

### 19.3 需求评审

只有两句散文 + 一个文件路径。评审记录本身写得好（状态机进非范围、空搜索→BUG-001、注册不自动登录、已补注册表单），但章内没告诉读者打开后先看哪三格。见 CH19-0003。

### 19.4 计划 / 风险 / 测试点 / 用例

出口标准、P0/P1 课程约定、超库存 P0、空搜索 P1、商品列表由 pytest 覆盖且用例表不单列——与 `test-plan.md` / `test-cases.md` 现行文本一致（S6-03 已修）。

仍缺「打开计划看优先级和出口、打开用例看 TC-SEARCH-001 失败」的第一眼锚点。见 CH19-0003。

覆盖矩阵把无凭证 401 挂在 R-PERM 下，见 CH19-0012。R-PERM「所属者可读自己的订单」没有对应 TC。见 CH19-0006。

### 19.5 Web 功能与后台

`GET /` 含登录/注册表单、`GET /admin.html` 200：实现与截图 01 支持。qty=11 页（05）证明力强。

问题：

- `GET /admin.html` 未登录也是 200（静态页），权限在 `/api/admin/*`。章未拆开，学生容易把页面 200 当成已授权。见 CH19-0009。
- 07-admin 订单「暂无」，alt 却写「只列出订单 id」。见 CH19-0007。
- 截图列表跳过已存在的 `06-register.png`、`08-network-log.png`。06 与 01 字节相同，不挂反而合理；08 是诚实的非 DevTools 表格，19.6 本可挂。见 CH19-0011、CH19-0014。

### 19.6 DevTools、Linux、SQL

四通道图与实现/证据一致：页面拒绝、400 `qty exceeds stock`、SQL 不得为 11、日志 `inventory reject ... qty=11`。种子 JOIN 两行与 `seed-join.txt`、03-shop 购物车列表一致。警告不要用 macOS `free`、只查教学库，正确。

未挂 `08-network-log.png`，而 19.6 正文在讲 DevTools 看 `POST /api/login`。见 CH19-0014。

### 19.7 接口、OpenAPI、Postman

OpenAPI 3.0.3、前缀 `/api/`、15 请求拆解与集合 `item` 完全一致；环境 password/token 初始空。审查未点 GUI 的披露正确。

空搜索那条 `pm.test` 按 R-SEARCH 断言，**现行实现下会失败**（集合 description 写了，章 19.7 没写）。pytest 对同一事实用 xfail，Runner 会红。见 CH19-0005。

OpenAPI 偏稀、登录 200 描述写成 “no order status field”。见 CH19-0015。

### 19.8 pytest

命令与 19.1 对齐。本机 `.venv` 与系统 Python 均为 37 passed / 1 xfailed。xfail 名称、`strict=True`、收集 38、不要 autouse 登录到 401——与 `conftest.py` / `test_api.py` 一致。覆盖句已点注册 11 条、首页表单、qty=11 不落库（S6-02 已修）。「四态」未点名 qty=0，面试区却写了 0。见 CH19-0016。

「pytest 绿不等于页面按钮可用，也不等于性能达标」正确。

### 19.9 缺陷、回归、报告

BUG-001 步骤/预期/实际/证据与实现、curl、xfail 一致。报告数字与仓库 pytest 输出一致。未假装关闭。正确。

### 19.10 总结与简历

可写/不可写清单与 `resume-evidence.md` 一致，没有写成公司项目。见 §13 岗位缺口（教学实现不等于生产范本，章未点明）。

### 工作实战 / 19-1

五步必做、执行记录模板、完成标准齐全。类型徽章仍未写在章内。19-1 已披露「过关不等于能面试讲解」，但可运行验收仍然一次浏览器都不用开。见 CH19-0010、CH19-0011。

### 常见错误 / 面试 / 练习

错误 1/3/4/5/6/7/8/9/10 都打在正确的坑上。错误 2 与章首口径摩擦，见 CH19-0001。面试五段结构符合全书约定，示例能指到仓库。练习与答案见 §11。

### 检查清单 / 总结 / 可运行性 / 参考资料 / 下一章

清单可验证。总结七件事与核心公式一致。可运行性说明与本机结果相符（Python 3.14.3、37/1、未点 GUI、未加压、Playwright 只取证）。链接全部可解析。下一章预告第 20 章，先做阶段测验 6，正确。

## 8. 代码问题

实现整体是合格的教学服务器：参数化 SQL、`type(qty) is not int`（拒绝 `True` 冒充 1）、下单用 `BEGIN`+条件 UPDATE 防超卖、403 体不含他人 id、注册 201 不签发 token。测试 isolation：session 级临时库 + autouse `reset_db`。

问题：

- CH19-0006：所属者 `GET /api/orders/{id}` 200 无自动化；`test_admin_products_ok` 在种子无订单时对空列表 `all(...)` 恒真。
- CH19-0008：`run.py test` 把 stdout 写入 `evidence/pytest-output.txt`（教材证据被本机跑脏）。
- CH19-0009：`/admin.html` 无鉴权（静态），鉴权只在 API。
- 下单不经过购物车、不改 `cart_items`，可能出现页面 qty>stock。见 CH19-0017。
- OpenAPI 未描述 `role`、登录缺字段 400、订单 404/409 无测试（P3，并入 CH19-0015）。

未把这些当成学生作业去「修产品」；它们是教材声称「完整项目闭环」时的测试缺口。

## 9. 图片问题

见下方 IMG-CH19-00N。结论摘要：

| ID | 文件 | 结论 |
| --- | --- | --- |
| IMG-CH19-001 | ch19-workbench.png/.html | KEEP |
| IMG-CH19-002 | ch19-qty-rule.png/.html | MODIFY |
| IMG-CH19-003 | ch19-cross-check.png/.html | KEEP |
| IMG-CH19-004 | 01-login.png | KEEP |
| IMG-CH19-005 | 02-login-fail.png | KEEP |
| IMG-CH19-006 | 03-shop.png | KEEP |
| IMG-CH19-007 | 04-search-empty-bug001.png | MODIFY |
| IMG-CH19-008 | 05-cart-qty-11.png | KEEP |
| IMG-CH19-009 | 06-register.png | DELETE（与 01 字节相同，章内未挂） |
| IMG-CH19-010 | 07-admin.png | MODIFY |
| IMG-CH19-011 | 08-network-log.png | KEEP（可挂进 19.6；不是 DevTools 面板） |
| IMG-CH19-012 | 09-pytest-report.png | KEEP |

assets 与 evidence/screenshots 九张 PNG **sha256 全相同**。

## 10. 表格问题

- 章内目录表 `docs/` 一行过粗：CH19-0013。
- 章内种子 JOIN 表与 `sql-check.md`、`seed-join.txt`、页面购物车一致，无错。
- `test-cases.md` 摘要 18 条：超库存 P0、空搜索失败/BUG-001、无状态名，正确。证据路径有的带 `evidence/` 有的不带：CH19-0013 类 P3。
- `prd-coverage-matrix.md`：R-SEARCH 失败、非范围明确留下，正确；401 挂 R-PERM：CH19-0012。
- `test-plan.md` P0 含商品列表并注明 pytest 覆盖、用例表不单列，与用例表不再冲突。

## 11. 练习与答案问题

### 章内练习 1–10（先独立作答，再对答案）

| 题 | 独立答案 | 教材答案 | 判定 |
| --- | --- | --- | --- |
| 1 | 材料来自课程仓库和个人练习；写成公司经历是诚信问题，深挖必穿 | 同 | 一致 |
| 2 | 以 `project/minishop/docs/PRD.md` 为准 | 同 | 一致；题干「第 16 章教学服务」与章首摩擦，见 CH19-0001 |
| 3 | 不能。xfail=BUG-001，未覆盖处仍可能有缺陷 | 同 | 一致 |
| 4 | 与 v1.0 契约不符的多余字段；开缺陷或先改 PRD，不能当成状态机合法 | 同 | 一致 |
| 5 | R-SEARCH；BUG-001 | 同 | 一致 |
| 6 | 401 未认证；403 已认证无权限 | 同 | 一致 |
| 7 | SKU-DEMO-001 qty 1 stock 10；SKU-DEMO-002 qty 2 stock 5 | 同 | 一致 |
| 8 | 集合会把初始值复制走；token 只留本机当前值 | 同 | 一致 |
| 9 | D。A 冒充企业；B 无状态机；C ROI 绝对化 | 同 | 一致 |
| 10 | 须含个人项目、库存规则、pytest、已知缺陷；禁公司名与状态名 | 示例合理 | 一致（开放题） |

无 `【ANSWER VERIFICATION FAILED】`。

### 阶段测验 6（覆盖 17–19；先独立作答）

必过题 3、6、9。独立答案：

1. 金字塔：下层更快更稳，上层更贵。接口 ROI 高 **不等于** 可以取消 Web 冒烟。
2. 没有约定负载、百分位和资源证据；功能断言不是负载模型。
3. 未授权对公网/生产加压可能造成事故或违法；只在自有或书面授权环境，本课不要求打高并发。
4. 没有 `status`。不能写「测通全部订单状态」。
5. qty=10 允许，qty=11 拒绝。早期教学服务可能只让 qty=1；测 v1.0 跟 PRD。
6. 本机 2026-09-10 复跑：**37 passed, 1 xfailed**。xfail = BUG-001。
7. 把每条 PRD 规则对到用例和证据。R-SEARCH = 失败 / BUG-001。
8. 不会自动登录。R-REG：201 无 token。
9. 材料来自课程仓库和个人练习。冒充企业经历是诚信问题。
10. D。B「22 passed 仍是仓库数字」已过时。

与文末答案一致。Q6 教材写「2026-09-09 审查为 37/1，以本机 evidence 为准」——本机即时 pytest 与该文件摘要相同。无答案错误。

### 19-1

`python3 practice/run.py 19-1` 与 `--check` 均为退出码 0：PRD 含 R-SEARCH/R-CART-10，BUG-001 仍开放，OpenAPI/Postman 文件存在，输出含 `37 passed` 与 `1 xfailed`。unittest 通过 `code == 0` 间接锁住 xfail。不检查 Postman 个数、不打开浏览器。见 CH19-0010、CH19-0016。

## 12. 初学者理解障碍

【Beginner Friction】

- 读完 19.1 启动命令后，19.2–19.10 仍主要是仓库导览；「打开评审看哪三格」没有。会逛目录 ≠ 会讲裁剪。
- 前置把 1–18 当已做完。没做 12-1 的人在 19.6 会以为必须手写 JOIN；已做 16-1 的人会以为 37/1 还要当第一次跑。
- 04 截图与 03 几乎一样，搜索框空格看不见，空搜索 Bug 在页面上不像 Bug。
- `/admin.html` 200 vs `/api/admin/*` 403 未拆开。
- 19-1 绿灯后以为「项目做完了」，章内虽有一句披露，可运行层仍不强制五步。
- `run.py test` 会改教材里的 `evidence/pytest-output.txt`，git status 变脏，学生不知道该不该提交。
- Postman 若按第 14 章 Runner 跑，空搜索那条会失败，而 pytest 是 xfail「绿」。

## 13. 岗位能力缺口

【Job Reality Gap】

- 闭环在仓库里是真的：需求→计划→用例→证据→缺陷→报告→简历。这正是初级岗位要能指给人看的东西。
- 缺口：所属者读自己的订单没有正例（CH19-0006）；管理员订单列表自动化在空表上真空通过；下单与购物车是两条互不更新的路径，章未标明教学简化（CH19-0017）。
- 教学实现细节（HTTP/1.0、SHA256+固定盐、Session 不过期、Cookie 无 SameSite）不得被学生写进简历当「我设计了安全架构」。章强调了个人项目，未强调「不要抄这套哈希上生产」。
- 简历证据本身不越界：无公司名、无「已测通支付/全部订单状态」、无精通 JMeter/独立 CI。此项通过。

## 14. 建议删除内容

- `chapters/assets/06-register.png` 与 `evidence/screenshots/06-register.png`（与 01-login.png 字节相同，文件名误导）。若要保留「注册入口」证据，用 01 即可。
- 错误 2 / 练习 2 / qty-rule 图题若 13–16 可运行示例确已打 v1.0，应删掉「现在还只让 qty=1」的现在时，改成「若你仍拿旧教学片段」。

## 15. 建议新增内容

- 前置「已做 / 没做」跳转表（教学审查补丁 1 仍适用）。
- 19.3 打开评审的三格：状态机→非范围；空搜索→R-SEARCH/BUG-001；注册不自动登录。
- pytest：所属者 `GET /api/orders/{id}` 200 且无 `status`；管理员列表先下单再断言只有 `id`。
- 19.7 一句：Postman「空搜索-BUG-001」现行会失败，这是缺陷仍开放，不是你没导入对。
- 19.5 一句：`/admin.html` 人人 200，权限看接口 401/403。
- 取证顺序：先下单再截后台，让 07 里出现订单 id。
- 空搜索截图：关键字框用可见占位（例如把空格换成选中态，或在页上留「本次 keyword="   "」）。

## 16. 建议重写内容

- 19.2 非范围改成「以 PRD 非范围为准」，点名支付、退款、物流、优惠券、评价、状态机、正式域名/HTTPS、短信验证码。
- ch19-qty-rule 标题/caption：不要再写「第 13–16 章教学服务常只让 qty=1」的现在时。
- 04-search-empty-bug001.png：重拍，让「提交了空白关键字」看得见。
- 07-admin.png：带至少一条订单 id 的列表。

## 17. 本章结论

**B 小修**

仓库是真的能跑的个人测试实践项目：契约、开放缺陷、37/1、简历口径都守住。作为核心收成章，正文仍有几处「指针代替第一眼」和「图证明不了它声称的那件事」。不需要重写章节，需要按 §14–16 做小修后再冲 90/95。

不可选 A：核心章目标 95 未到，空搜索截图与 19.3 厚度不够发布线。不可选 C：没有 P0/P1 教错冻结契约，上一轮数字类硬伤（Postman 9、pytest 命令）已修。

## 18. 执行记录

### 读过的文件

全局：`reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`、`REPOSITORY_INVENTORY.md`、`MASTER_AUDIT.md`、`AUDIT_PROGRESS.md`；`README.md`；`docs/COURSE_CONTROL.md`、`COURSE_OUTLINE_v1.2.md`、`LEARNING.md`；`standards/QUALITY_STANDARD_v1.0.md`；`practice/README.md`、`STATUS.md`；`exercises/README.md`；`reviews/_pedagogy-2026-09-10/RUBRIC.md`、`ch19.md`；`reviews/chapter-19-review.md`；`reviews/_rereview-2026-09-09/stage-6-ch17-19.md`（线索）；`reviews/v1.2.1-rescore.md`、`full-course-audit-v1.2.md` 中第 19 章相关句（线索）。

本章：`chapters/19-minishop-project.md`；`chapters/quizzes/stage-6-project.md`、`quizzes/README.md`；`chapters/assets/diagrams/README.md`（ch19 条目）。

Practice：`practice/19-project-pack/README.md`、`main.py`、`tests/test_lab.py`、`validation/latest.json`；`practice/run.py`。

项目：`project/README.md`；`project/minishop/README.md`、`server.py`、`run.py`、`run.sh`、`run.bat`、`pytest.ini`、`requirements.txt`；`tests/conftest.py`、`test_api.py`、`test_qty_rule.py`、`test_register.py`；`frontend/index.html`、`app.js`、`admin.html`、`styles.css`；`docs/PRD.md`、`openapi.json`、`test-plan.md`、`test-cases.md`、`test-points.md`、`test-report.md`、`requirement-review.md`、`prd-coverage-matrix.md`、`sql-check.md`、`project-summary.md`、`resume-evidence.md`；`bugs/BUG-001.md`；`postman/MiniShop.postman_collection.json`、`MiniShop.postman_environment.json`；`automation/README.md`；`jmeter/minishop-get-products.jmx`；`evidence/README.md`、`pytest-output.txt`、`pytest-report.html`（摘要）、`http/*.txt`、`http/network-log.html`、`sql/seed-join.txt`、`logs/app-sample.log`、`linux/*`；`logs/app.log`（抽样）。

图片：`chapters/assets/diagrams/ch19-{workbench,qty-rule,cross-check}.{html,png}`；`chapters/assets/0{1-9}-*.png`；`project/minishop/evidence/screenshots/` 九张（哈希对照）。

### 实际跑过的命令与结果

| 命令 | 结果 |
| --- | --- |
| `python3 --version` | Python 3.14.3 |
| `python3 -c "import pytest,requests"` | pytest 9.1.1，requests 2.34.2 |
| `python3 project/minishop/run.py setup` | 创建 `.venv`，安装 pytest==9.1.1、pytest-html==4.2.0、requests==2.34.2 |
| `python3 practice/run.py 19-1` | 退出 0；文件检查全 OK；`37 passed, 1 xfailed`；BUG-001 仍开放 |
| `python3 practice/run.py 19-1 --check` | unittest `test_project_pack` ok（内部再次调用 main） |
| `project/minishop/.venv/bin/python -m pytest -q` | **37 passed, 1 xfailed**（未走 `run.py test`，未改写 evidence） |
| `pytest --collect-only -q` | **38 tests collected**，名单与 19.8 覆盖句相符（test_api 23 含 8 组 qty + 1 xfail，test_register 11，test_qty_rule 4） |
| 进程内 ThreadingHTTPServer 对 `MiniShopHandler` 的登录/qty/空搜索/下单/越权/注册/日志 | 与 PRD 一致；空白 keyword 仍 3 件；owner GET 200 且无 status（**此条无 pytest**） |
| `python3 server.py` `MINISHOP_PORT=8769` | 打印 `MINISHOP_BASE_URL=http://127.0.0.1:8769` 后因前台超时被收进程；HTTP 行为已由进程内客户端覆盖 |
| 未执行 | `run.py test` / `run.py evidence`（会改写 `evidence/pytest-output.txt` 与截图）；未点 Postman GUI；未装/未跑 JMeter；未开浏览器手工点页面（截图与 API 已核） |

### 外部核查

| 条目 | 来源 | 结论 |
| --- | --- | --- |
| pytest 9.1.1 | PyPI / GitHub release 2026-06-19 | 现行最新稳定版，教材钉死版本成立 |
| requests 2.34.2 | PyPI 2026-05-14 | 现行最新，成立 |
| pytest-html 4.2.0 | PyPI 2026-01-19 | 成立 |
| OpenAPI 3.0.3 | OpenAPI Initiative | 成立 |
| Postman Collection v2.1 schema URL | schema.getpostman.com | 集合声明成立 |
| HTTP 201 / 401 / 403 / 409 | RFC 9110 §15.3.2、§15.5.2、§15.5.4、§15.5.10 | 本章用法正确：创建、缺认证、已认证无权限、手机号占用/库存冲突 |
| 禁止绝对化六条 | Quality Standard §四 | 本章均作为错误项或反例出现，未当成正说 |

---

# ISSUE 清单

## ISSUE
ID：CH19-0001
文件：`chapters/19-minishop-project.md`；`chapters/assets/diagrams/ch19-qty-rule.html`
章节：19
小节：开篇「这一章解决什么问题」；19.2 示意图；错误 2；练习 2
精确位置：约 L15；示意图 h1/caption；L327–329；L405
原文：章首「第 13～16 章可运行示例已经打本仓库 MiniShop：路径带 `/api/`，`qty=10` 允许、`qty=11` 拒绝。」示意图「教学服务可能只让 qty=1」「第 13～16 章教学服务常只让 qty=1 成功」。
问题等级：P2
问题类别：SEQ / PED / TERM
问题说明：同一章对「13–16 现在测的是哪把尺子」给了现在时的两种说法。
为什么有问题：读者会以为 5-1/13-1/16-1 仍是 qty=1 唯一成功，或反过来以为错误 2 过时。冻结口径要求第 19 章前的教学约定必须标明，不能和「已经打 v1.0」混成现在时事实。
依据：本章开篇 vs 示意图 caption；Quality Standard §五。是否仍属 13–16 正文事实，交 Global-06 / 对应章 Agent 对照，不在本章扩审。
建议修改：示意图改成「测 MiniShop v1.0 必须以 PRD 为准；若你还拿着旧教学片段（只让 qty=1），不要用它当本项目期望。」错误 2 同步。
推荐替换文本：见 §16。

## ISSUE
ID：CH19-0002
文件：`chapters/19-minishop-project.md` vs `project/minishop/docs/PRD.md`
章节：19
小节：19.2
精确位置：L138
原文：`非范围：支付、物流、优惠券、订单状态机、生产 HTTPS。`
问题等级：P2
问题类别：TEST / PED
问题说明：短于 PRD 非范围（退款、评价、短信验证码、正式域名）。
为什么有问题：学习目标要求说明非范围；面试对照 PRD 时会问「章里没写能不能写进简历」。验证码是第 4/5 章教学约定，本章必须点名不要写进本项目。
依据：PRD「非范围」节；教学审查 P19-06（现行正文仍未改）。
建议修改：非范围以 PRD 为准并点名验证码。
推荐替换文本：`非范围以 docs/PRD.md 为准：支付、退款、物流、优惠券、评价、订单状态机、正式域名/HTTPS、短信验证码。第 4、5 章用验证码练设计，不要写进本项目用例或简历。`

## ISSUE
ID：CH19-0003
文件：`chapters/19-minishop-project.md`
章节：19
小节：19.3、19.4
精确位置：L143–160
原文：19.3 仅「记录：docs/requirement-review.md」加两句散文；19.4 仅文件路径列表。
问题等级：P2
问题类别：PED
问题说明：学习目标要求「解释为什么裁掉状态机」「按计划执行 P0/P1」，正文没有「打开文件后第一眼看哪几行」。
为什么有问题：收成章若只指路，零基础读者会复制目录交差，讲不出裁剪。评审文件里其实已有三格结论。
依据：学习目标 L22–L23；`docs/requirement-review.md` 表。
建议修改：19.3 写三格锚点；19.4 写「优先级节 P0 含 qty=10/11 与注册，空搜索是 P1；TC-SEARCH-001 结果失败/BUG-001」。
推荐替换文本：教学审查补丁 3 仍适用。

## ISSUE
ID：CH19-0004
文件：`chapters/19-minishop-project.md`
章节：19
小节：前置知识；19.6–19.8 星级
精确位置：L30–34
原文：`已完成第 1～18 章中与本项目相关的技能`
问题等级：P2
问题类别：PRE / SEQ
问题说明：没有已做/没做跳转；Linux/SQL/Postman 与章标题同为 ⭐⭐⭐。
为什么有问题：11 与 12 互不为硬前置；16-1 已跑过 37/1 的人被当成第一次。未做 SQL 的人会在 JOIN 处卡住。
依据：`docs/LEARNING.md` 学习顺序；教学审查 P19-01。
建议修改：加跳转表；已跑 16-1 只解释 xfail；没做 12-1 对照种子表即可。
推荐替换文本：教学审查补丁 1。

## ISSUE
ID：CH19-0005
文件：`chapters/19-minishop-project.md`；`project/minishop/postman/MiniShop.postman_collection.json`
章节：19
小节：19.7
精确位置：章 L227；集合「空搜索-BUG-001」的 `pm.test`
原文：章只说 15 个请求并带 `pm.test`，未说空搜索这条现行会失败。
问题等级：P2
问题类别：TEST / PED
问题说明：同一缺陷，pytest 用 xfail（套件仍「绿」），Postman 用硬断言（Runner 会红）。
为什么有问题：学生按 14.6.1 跑 Runner 会以为导入错了。集合 description 有警告，章 19.7 没有。
依据：集合 test 脚本 `closed = code===400 || items.length===0`；实现空白 keyword 仍全量。
建议修改：19.7 加一句：空搜索请求按 R-SEARCH 断言，现在失败 = BUG-001 仍开放，不要为了全绿改断言。
推荐替换文本：`空搜索那条 pm.test 现行会失败，对应 BUG-001；pytest 用 xfail 跟踪同一事实。审查未点 GUI。`

## ISSUE
ID：CH19-0006
文件：`project/minishop/tests/test_api.py`；`docs/prd-coverage-matrix.md`；`docs/test-cases.md`
章节：19（项目产物）
小节：R-PERM / 19.8 覆盖句
精确位置：`test_order_forbidden_other_user`、`test_admin_products_ok`；矩阵 R-PERM 行
原文：PRD R-PERM「`GET /api/orders/{id}` 仅订单所属者可看明细」；用例只有 B 读 A → 403。
问题等级：P2
问题类别：TEST
问题说明：无「所属者 200 且无 status」正例。管理员订单列表在种子无订单时 `all(set(keys)=={"id"})` 对空列表恒真。本机手工：owner GET 200 `{'id','items'}`，无 status。
为什么有问题：若实现改成「谁都 403」，现有越权测试仍绿。覆盖矩阵声称 R-PERM 已通过。
依据：PRD R-PERM；ISTQB 权限测试应有允许与拒绝成对。
建议修改：补 `test_owner_can_read_own_order`；管理员用例先下单再断言 items 非空且只有 id。
推荐替换文本：用例预期 `200，body 有 id 与 items，无 status`。

## ISSUE
ID：CH19-0007
文件：`chapters/assets/04-search-empty-bug001.png`；`07-admin.png`
章节：19
小节：19.5
精确位置：L179、L183
原文：alt「空搜索 BUG-001」；「管理员后台只列出订单 id」
问题等级：P2
问题类别：IMG
问题说明：04 与 03-shop 都是「共 3 件」三件商品，关键字框空格不可见，截图证明不了「提交了空白搜索」。07 订单为「暂无」，证明不了「只列出 id」（取证脚本先截后台、后才 HTTP 下单）。
为什么有问题：学生看图对不上 BUG-001 步骤；alt 承诺的内容图上没有。HTTP 证据是够的，图是弱证据。
依据：`run.py` `capture_screenshots` 顺序；BUG-001「搜索框为空格提交后页面共 3 件」。
建议修改：重拍 04（让 keyword 提交可见）；07 先下单再截。
推荐替换文本：无正文替换，换图。

## ISSUE
ID：CH19-0008
文件：`project/minishop/run.py`；`chapters/19-minishop-project.md` 19.1/19.8
章节：19
小节：19.1 一键运行
精确位置：`run_pytest()` 写入 `EVIDENCE / "pytest-output.txt"`
原文：`python3 run.py test       # pytest`
问题等级：P2
问题类别：CODE / PED
问题说明：教材命令会覆盖仓库已提交的审查证据。19-1 直接 `python -m pytest` 不会覆盖。
为什么有问题：学习者 git status 变脏，可能把本机输出当教材证据提交，或以为自己把课程改坏了。上一轮复审已踩过「跑完要还原 evidence」。
依据：`run.py` L61–74；`practice/19-project-pack/main.py` 不写该文件。
建议修改：`run.py test` 默认写到临时路径或 `evidence/local-pytest-output.txt`（gitignore）；只有 `evidence` 子命令才更新教材证据。或章内写明「会改写 evidence，不要提交」。
推荐替换文本：章内加 `这条命令会覆盖 evidence/pytest-output.txt，那是你本机证据，不要当教材原件提交。`

## ISSUE
ID：CH19-0009
文件：`chapters/19-minishop-project.md`；`server.py` `do_GET`；`frontend/admin.html`
章节：19
小节：19.5
精确位置：L168–169、L187
原文：`GET /admin.html → 200`；`普通用户调 /api/admin/products 为 403`
问题等级：P2
问题类别：PED / TEST
问题说明：未区分静态页 200 与接口 401/403。`test_admin_page_ok` 只断言页面 200 含「只列出 id」。
为什么有问题：权限测试的典型坑：页面能打开 ≠ 有数据权限。本章学习目标含权限，却把关键观察留给学生自己撞。
依据：RFC 9110 403 针对的是资源请求被拒绝，不是 HTML 文件是否存在。
建议修改：写明「后台页未登录也 200；库存/订单 id 来自 `/api/admin/*`，普通用户 403、未登录 401。」
推荐替换文本：同上。

## ISSUE
ID：CH19-0010
文件：`practice/19-project-pack/README.md`；`chapters/19-minishop-project.md` 工作实战
章节：19
小节：MiniShop 工作实战；实操 19-1
精确位置：README 验收条件；章 L282–317
原文：19-1 验收「文件在 + 37/1」；章内五步才要求启动首页、复现 BUG-001。
问题等级：P2
问题类别：EX / PED
问题说明：一句话核心是「能指给人看」。可运行层仍可不开浏览器拿到 ✅。README 已有「过关不等于能面试讲解」，章 19.1 也有一句，但工作实战节仍无类型徽章、未把 19-1 与五步的关系写在必做之前。
为什么有问题：只跑 19-1 的读者会以为收成完成。
依据：Quality Standard §七 实操要练会该章那句话。
建议修改：工作实战必做前加类型行；保持 19-1 只锁基线（这是对的），但检查清单把五步标成进入下一章硬门槛（门槛 1–4 其实已写，需在 19-1 README 再指回去——已有，章内补徽章即可）。
推荐替换文本：`类型：✅ 基线检查 + 📖 执行记录。python3 practice/run.py 19-1 不代替下面 5 步。`

## ISSUE
ID：CH19-0011
文件：`chapters/assets/06-register.png`（及 evidence 副本）
章节：19
小节：未挂入正文；覆盖矩阵引用 `06-register.png`
精确位置：矩阵最后一行「页面」
原文：文件名暗示注册页；内容与 `01-login.png` sha256 相同。
问题等级：P3
问题类别：IMG
问题说明：`run.py` 在 `goto /` 后再 snap 06，未登录态首页与 01 相同。覆盖矩阵把它当注册入口证据，实际就是登录页全页。
为什么有问题：文件名骗人；占证据位。01 已含注册表单。
依据：本机 `01-login.png` 与 `06-register.png` sha256 均为 `910f31b0…` 前缀相同的同一哈希。
建议修改：删除 06，矩阵改引用 01。
推荐替换文本：矩阵证据列改为 `01-login.png`。

## ISSUE
ID：CH19-0012
文件：`project/minishop/docs/prd-coverage-matrix.md`
章节：19
小节：覆盖矩阵 R-PERM 行
精确位置：矩阵「R-PERM | 无凭证 401」
原文：把 TC-AUTH-001 无凭证 401 映射到 R-PERM
问题等级：P3
问题类别：TERM
问题说明：R-PERM 是越权与管理员；未认证更接近 R-AUTH。
为什么有问题：401/403 刚在学习目标里要求分开，矩阵又把 401 塞进权限规则。
依据：PRD R-AUTH / R-PERM 分列；RFC 9110 401 vs 403。
建议修改：无凭证行改挂 R-AUTH，或单列「认证」。
推荐替换文本：`R-AUTH | 无凭证改购物车/下单 401 | TP-AUTH-401 | TC-AUTH-001`

## ISSUE
ID：CH19-0013
文件：`chapters/19-minishop-project.md` 19.1 表；`docs/test-cases.md` 证据列
章节：19
小节：19.1；用例摘要
精确位置：L74；用例表「证据」列
原文：`docs/` = 「PRD、OpenAPI、计划、用例、报告」；证据路径有的 `evidence/http/01-…` 有的 `04-search-empty-bug001.png` 有的 `sql/seed-join.txt`
问题等级：P3
问题类别：PED
问题说明：目录表漏评审/矩阵/SQL/总结/简历；证据前缀不统一。
为什么有问题：学生按表找文件会以为没有 `requirement-review.md`。
依据：`project/minishop/docs/` 实际文件列表。
建议修改：docs 行改为「PRD、OpenAPI、评审、计划、用例、矩阵、SQL、报告、总结、简历」。证据列统一 `evidence/…`。
推荐替换文本：如上。

## ISSUE
ID：CH19-0014
文件：`chapters/19-minishop-project.md` 19.6；`chapters/assets/08-network-log.png`
章节：19
小节：19.6
精确位置：L195；未引用 08
原文：正文要看 `POST /api/login` 的状态码、Set-Cookie、token；仓库有诚实的非 DevTools 表格图未挂。
问题等级：P3
问题类别：IMG
问题说明：STATUS 说没有 DevTools 面板截图，08 自己也写「不是 Chrome DevTools 面板截图」。挂上可以当 HTTP 证据墙，不挂也不算断链。
为什么有问题：19.6 的 DevTools 句没有第一帧可看。
依据：`evidence/http/network-log.html` 与 08 PNG 内容一致。
建议修改：19.6 挂 08，并写明这是整理表不是面板。
推荐替换文本：`![本机请求记录（非 DevTools 面板）](assets/08-network-log.png)`

## ISSUE
ID：CH19-0015
文件：`project/minishop/docs/openapi.json`
章节：19
小节：19.7
精确位置：`/api/login` 200 description
原文：`"200": {"description": "OK with token; no order status field"}`
问题等级：P3
问题类别：HTTP
问题说明：登录响应描述在说订单字段；未写 `role`、缺字段 400。契约作为教学 OpenAPI 可稀，但这句会让人以为登录 body 跟订单有关。
为什么有问题：学生对照 OpenAPI 写用例时会被带跑。
依据：实际登录 body 为 `result/token/role`，无 status；缺字段返回 400 `missing field`。
建议修改：`200: token + role + Set-Cookie HttpOnly；body 无 status。400 缺字段；401 密码/用户错误。`
推荐替换文本：如上。

## ISSUE
ID：CH19-0016
文件：`chapters/19-minishop-project.md` 19.8；`practice/19-project-pack/main.py`
章节：19
小节：19.8 覆盖句；19-1
精确位置：L252；main.py 对 OpenAPI/Postman 只 `is_file()`
原文：覆盖「qty=1/10/11 与四态」；面试区写了 0。19-1 不解析 JSON、不数 15 请求。
问题等级：P3
问题类别：TEST / EX
问题说明：八组 parametrize 含 zero；「四态」通常指缺/null/空串/错类型，0 被漏写。19-1 用空文件也能过 OpenAPI 存在性检查（PRD/BUG 有内容检查）。
为什么有问题：覆盖句与面试口述差一组；19-1 锁不住上一轮那种「请求数写错」。
依据：`test_cart_qty_cases` ids；main.py L32–36。
建议修改：覆盖句写成「1/10/11 + 缺/null/空串/字符串/0」。19-1 可选：`json.load` OpenAPI 且 `len(collection['item'])==15`（注意不要再把 15 写成永不改的魔法数而不在失败信息里指文件）。
推荐替换文本：`购物车 8 组：1、10、11、缺字段、null、空串、字符串、0。`

## ISSUE
ID：CH19-0017
文件：`project/minishop/server.py`；`frontend/index.html`；`chapters/19-minishop-project.md`
章节：19
小节：19.2 / 19.5 购物车与下单
精确位置：`_create_order` 不读、不改 `cart_items`；首页购物车表单与下单表单并列
原文：PRD 范围并列「购物车数量、创建订单」；页面上两套 SKU/qty 表单。
问题等级：P2
问题类别：JOB / PED
问题说明：创建订单按 sku+qty 直接扣库存，不经过购物车，也不把购物车数量改掉。用户可先把购物车写成 10，再下单 1 件后页面仍显示 qty=10、stock=9。
为什么有问题：真实电商几乎都是「从购物车结算」。本章把它当完整项目收成，却不标明这是教学简化，学生可能把「下单与购物车无关」写进简历或面试。PRD 也没写清订单是否来自购物车。
依据：`_create_order` 只 UPDATE `products.stock`；`refreshCart` 读当前 stock。本机 03-shop 与下单证据走的是两条路径。
建议修改：PRD R-ORDER 加一句「v1.0 下单不读取购物车，是教学简化，不是结算流程」；章 19.2/19.5 复述。不必改实现。
推荐替换文本：`创建订单（R-ORDER）：直接 POST sku+qty，不经过购物车、不修改 cart_items。这是教学简化，简历不要写成「完成了购物车结算」。`

---

# 图片记录

IMG-CH19-001
文件：`chapters/assets/diagrams/ch19-workbench.png` + `.html`
出现位置：19.1
图片主要内容：能跑 / 契约 / 怎么测 / 证据 / 缺陷 / 诚实边界 六块；个人实践、无 status、37/1+BUG-001。
技术准确性：正确。
与正文一致性：与一句话核心一致。
文字是否正确：是。
UI 是否过时：不适用（概念图）。
教学价值：高，对准本章过滤器。
可读性：好。
是否需要修改：否。
修改建议：—
最终结论：KEEP

IMG-CH19-002
文件：`chapters/assets/diagrams/ch19-qty-rule.png` + `.html`
出现位置：19.2
图片主要内容：10 绿允许 / 11 红拒绝；标题强调教学服务 qty=1 vs PRD。
技术准确性：10/11 数字正确；标题现在时与章首冲突（CH19-0001）。
与正文一致性：与 R-CART-10 一致，与开篇 13–16 已打 v1.0 不一致。
文字是否正确：10/11 正确；「常只让 qty=1」作为现在时不稳。
UI 是否过时：否。
教学价值：中（尺子必要，但是第 5/16 章已练过）。
可读性：好。
是否需要修改：是。
修改建议：改标题为「v1.0 尺子：等于库存允许」。
最终结论：MODIFY

IMG-CH19-003
文件：`chapters/assets/diagrams/ch19-cross-check.png` + `.html`
出现位置：19.6
图片主要内容：页面 / POST /api/cart/items / SQL / app.log 四通道对 qty=11。
技术准确性：与实现和证据一致。
与正文一致性：对准学习目标「交叉核对」。
文字是否正确：是。
UI 是否过时：否。
教学价值：高，本章新难点。
可读性：好。
是否需要修改：否。
修改建议：—
最终结论：KEEP

IMG-CH19-004
文件：`chapters/assets/01-login.png`（= evidence 副本）
出现位置：19.5 alt「登录与注册」
图片主要内容：登录表单 + 注册表单；个人实践声明；密码规则与「不自动签发 token」。
技术准确性：与 `index.html` 一致。
与正文一致性：支持「页面含登录与注册」。
文字是否正确：是。
UI 是否过时：教学页，可接受。
教学价值：高。
可读性：好。
是否需要修改：否。
修改建议：—
最终结论：KEEP

IMG-CH19-005
文件：`chapters/assets/02-login-fail.png`
出现位置：19.5
图片主要内容：手机号 13800138000，密码已填，文案「登录失败」；注册区仍在。
技术准确性：错误密码不进商品区，正确。
与正文一致性：是。
文字是否正确：是。
UI 是否过时：否。
教学价值：中（正常失败例）。
可读性：好。
是否需要修改：否。
修改建议：—
最终结论：KEEP

IMG-CH19-006
文件：`chapters/assets/03-shop.png`
出现位置：19.5
图片主要内容：用户 13800138000 (user)；三件商品库存 10/5/3；购物车鼠标 1 / 键盘 2；下单表单。
技术准确性：与种子数据、SQL 一致。
与正文一致性：是。
文字是否正确：是。
UI 是否过时：否。
教学价值：高（种子可视化）。
可读性：好。
是否需要修改：否。
修改建议：—
最终结论：KEEP

IMG-CH19-007
文件：`chapters/assets/04-search-empty-bug001.png`
出现位置：19.5
图片主要内容：登录后商品区「共 3 件」三件商品；关键字框看起来是空的。
技术准确性：空白搜索确回全量，但图上看不出发生了搜索。
与正文一致性：alt 声称 BUG-001，视觉上几乎是 03 的副本（哈希不同，空格不可见）。
文字是否正确：无错误字，缺「本次 keyword 为空白」的可见标记。
UI 是否过时：否。
教学价值：低（证明力不足）。
可读性：好但无信息增量。
是否需要修改：是。
修改建议：重拍，露出已提交的空白/空格，或叠加「keyword='   ' → 仍 3 件」。
最终结论：MODIFY

IMG-CH19-008
文件：`chapters/assets/05-cart-qty-11.png`
出现位置：19.5
图片主要内容：数量框 11，提示 `qty exceeds stock`，列表仍 qty=1。
技术准确性：正确，且同时证明拒绝与不落库。
与正文一致性：是。
文字是否正确：是。
UI 是否过时：否。
教学价值：高。
可读性：好。
是否需要修改：否。
修改建议：—
最终结论：KEEP

IMG-CH19-009
文件：`chapters/assets/06-register.png`（章内未引用）
出现位置：覆盖矩阵；run.py 取证
图片主要内容：与 01-login.png 像素级相同。
技术准确性：作为「注册页」不成立。
与正文一致性：正文未挂，矩阵误用。
文字是否正确：同 01。
UI 是否过时：否。
教学价值：无（重复）。
可读性：—
是否需要修改：删除或停止当独立证据。
修改建议：DELETE 文件或矩阵改指 01。
最终结论：DELETE

IMG-CH19-010
文件：`chapters/assets/07-admin.png`
出现位置：19.5
图片主要内容：库存 10/5/3；订单 id 区「暂无」；注记「v1.0 只列出 id」。
技术准确性：库存正确；订单空是取证顺序造成，不是后台会显示状态名。
与正文一致性：alt「只列出订单 id」与画面「暂无」不匹配。
文字是否正确：注记正确。
UI 是否过时：否。
教学价值：中（能看库存与注记，不能看 id 列表形态）。
可读性：好。
是否需要修改：是。
修改建议：先创建订单再截。
最终结论：MODIFY

IMG-CH19-011
文件：`chapters/assets/08-network-log.png`（章内未引用）
出现位置：evidence/screenshots；network-log.html 的截图
图片主要内容：本机请求表；登录 200 HttpOnly、空搜索 BUG-001、qty 10/11、下单无 status、注册 201/409；自报不是 DevTools 面板。
技术准确性：与 HTTP 证据一致。诚实披露。
与正文一致性：19.6 需要一帧 HTTP 观察，却没挂。
文字是否正确：是。
UI 是否过时：否。
教学价值：中高。
可读性：好。
是否需要修改：建议挂进 19.6，不必改图。
修改建议：正文引用。
最终结论：KEEP

IMG-CH19-012
文件：`chapters/assets/09-pytest-report.png`
出现位置：19.8
图片主要内容：pytest-html 4.2.0；38 tests；37 Passed；1 Expected failures；0 Failed。
技术准确性：与本机复跑、`pytest-report.html` 摘要一致。
与正文一致性：alt 用 expected failure，与插件 UI 一致。
文字是否正确：是。日期 09-Sep-2026。
UI 是否过时：否。
教学价值：高（绿 ≠ 无缺陷的可视化）。
可读性：未展开 xfail 名称，正文有补。
是否需要修改：否（可选：截到能看见 `test_empty_keyword_should_not_return_all`）。
修改建议：—
最终结论：KEEP
