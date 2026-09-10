# Chapter 16 Audit

审计角色：Chapter-Audit-Agent-16  
范围：第 16 章全部（索引 + 16A + 16B）及指定相关文件。未审其他章正文。  
日期：2026-09-10  
权威：pytest 9.x 官方文档、requests 官方文档、MiniShop PRD v1.0 / OpenAPI、Quality Standard v1.0  
核验环境：Python 3.14.3，pytest 9.1.1，requests 2.34.2

## 1. Coverage

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 索引页小节/标题 | 1 | 1 | 0 |
| 16A 标题（含错误/面试/练习） | 31 | 31 | 0 |
| 16B 标题（含错误/面试/练习；模板内 4 个标题算代码块内容） | 34+4 | 38 | 0 |
| 正文段落（去围栏后非列表/非表散文行） | 16=3，16A=65，16B=67，实操 README=3 | 138 | 0 |
| 表格块 | 16A 3 + 16B 1 = 4 | 4 | 0 |
| 代码围栏 | 16A 11 + 16B 10 + 实操 README 2 = 23 | 23 | 0 |
| 其中 Python 块 | 9（16A 5 + 16B 4） | 9 | 0 |
| Shell/bash 命令块 | 8 | 8 | 0 |
| SQL 示例 | 0（仅散文提到授权库 `SELECT`） | 0 | 0 |
| HTTP 示例（表+可抄请求） | 16.4 行为表 8 行 + GET 片段 1 + 登录 2 + token 登录 1 + 下单 1 + 购物车 8 = 21 | 21 | 0 |
| 章内测试函数/参数化行 | 14（qty 2 + fail demo 1 + login 2 + order 1 + cart 8） | 14 | 0 |
| 仓库套件收集项 | 38（37 passed + 1 xfailed） | 38 | 0 |
| Bug 示例 | BUG-001（正文/实操/xfail/缺陷单） | 1 | 0 |
| 小练习 | 16A 1–4，16B 5–10 = 10 | 10 | 0 |
| 章内标准答案 | 10 | 10 | 0 |
| 阶段测验 5 题（全文件 10 题；第 16 章相关 6–10，全卷均独立作答） | 10 | 10 | 0 |
| 图片 PNG（引用） | 5 | 5 | 0 |
| 示意图 HTML | 4 | 4 | 0 |
| Markdown 链接 | 16=4，16A=5，16B=4，实操=3 = 16 | 16 | 0 |
| 相关代码文件 | practice `main.py`/`test_lab.py`；`pytest.ini`；`conftest.py`；`test_api.py`；`test_qty_rule.py`；`test_register.py` | 7 | 0 |
| 全局/线索文件（必读，不作本章正文） | brief/inventory/标准/大纲/既有审查 | 全部已读 | 0 |

Coverage：**100%**。未检查 = 0。

### 1.1 内容单元清单（按文件）

**`chapters/16-pytest.md`（索引）**  
一句话核心；拆章说明；链 16A/16B；作业（读 `tests/`、`run.py test` 37/1、实操 16-1）；阶段测验 5；读完第二节进第 17 章。

**`chapters/16a-pytest-basics.md`**  
解决的问题、学习目标、前置、场景导入、16.1 ROI、16.2 安装、16.3 收集/`assert`、16.4 requests、16.5 登录、16.5 后无标题的仓库命令+HTML 截图、常见错误 1–5、面试 3 题、练习 1–4 与答案、检查清单、总结、可运行性、参考资料、下一节预告。

**`chapters/16b-pytest-fixtures.md`**  
解决的问题、学习目标、前置、场景导入、16.6 fixture/scope、16.7 conftest、16.8 token、16.9 parametrize、16.10 目录与 ini、实操 16-1 入口、MiniShop 工作实战、记录模板、仓库结果、常见错误 1–4、面试 3 题、练习 5–10 与答案、检查清单、总结、阶段测验、可运行性、参考资料、第 17 章预告。

**实操 / 仓库 / 测验 / 图**  
见第 8–11、18 节。每张 PNG/HTML 均用 `read_file` 打开。

## 2. 总评分

核心章，按 brief 从严；90 是作者发布线，不是本审计下限。

| 维度 | 分数 | 依据 |
| --- | ---: | --- |
| 技术准确性 | 8/10 | 可抄示例与 pytest 9 / requests / PRD 一致，37/1 本机复现；扣在 session-scope 建议与 `reset_seed_db` 冲突、图「永远测不到 401」过绝对、`test_*` 与官方前缀 `test` 不完全等同 |
| 岗位实用性 | 8/10 | ROI 有边界、timeout、401 不 autouse、xfail 诚实口径都对岗位有用；缺 `@pytest.mark.xfail`/`strict`、两扇门、403 阅读指针 |
| 完整性 | 7/10 | 大纲条目都在；xfail 语法、临时端口实现、pytest-html 来源未讲清 |
| 初学者友好度 | 7/10 | qty 纯函数闭环好；工作实战跳到未教的 `ThreadingHTTPServer`/`tmp_path_factory`；16A 图 caption 提前讲 autouse |
| 教学顺序 | 8/10 | 16A→16B 坡度对；装饰器与 xfail 面试略提前 |
| 代码质量 | 9/10 | 9 个 Python 块 `ast.parse` 全过；对 live MiniShop 与仓库套件均跑通 |
| 实操质量 | 9/10 | `python3 practice/run.py 16-1` 与 `--check` 均为 37 passed / 1 xfailed |
| 练习质量 | 8/10 | 1–7、9–10 与答案一致；练习 8 弱于同章面试口径 |
| 图片质量 | 7/10 | ROI/八组 parametrize 对齐正文；collect 图 lead/caption 错位；no-autouse 标题过绝对 |
| 结构与 MiniShop 一致性 | 8/10 | `/api/login`、`qty=10→200`、Bearer、订单无 `status`、无第二套 `teach_server`；16A 缺「工作实战」标题 |
| **总体** | **79/100** | 无 P0/P1；P2 为教学缺口而非把学生教到错误契约 |

## 3. P0

无。可抄示例已是 `POST /api/login`、`qty=10`→200、购物车 Bearer、订单 201/`id`/无 `status`。未把「接口自动化 ROI 永远最高」「GET 比 POST 安全」「Cookie/Session/Token 三选一」「全绿=无缺陷」写成正课。BUG-001 仍开放，与 xfail 对齐。

## 4. P1

无。旧审查（教学服务 `/login`、qty=1-only、16.5 依赖未教的 `base_url`、16.4 未写先 `serve`、正文「六个」vs 八组）在现行正文中已修好，本轮独立复核确认。

## 5. P2

见下方 ISSUE CH16-0001 … CH16-0009。

## 6. P3

见 ISSUE CH16-0010 … CH16-0021。

## 7. 逐段问题

### 索引 `chapters/16-pytest.md`

| 单元 | 结论 |
| --- | --- |
| 一句话核心 | 通过。与 16A 一致，能过滤 `assert True` /「绿了=没缺陷」。 |
| 拆章列表与作业句 | 通过。作业钉在 16B + 实操 16-1 + `37 passed / 1 xfailed`。命令未写 `cd`，被 16B 工作实战补上。 |
| 链接 16A/16B/16-1/测验 5 | 通过。目标文件均存在。 |

### 16A 开篇（解决的问题 → 场景导入）

| 单元 | 结论 |
| --- | --- |
| 一句话核心 / 星级 / 核心章目标 | 通过。 |
| 解决的问题：Runner vs pytest | 通过。未宣称淘汰 Postman。 |
| 学习目标 | 通过。与 16.1–16.5 对应。未把 fixture 写进上半章必会，正确。 |
| 前置「已完成第 15 章」 | 通过（不展开第 15 章正文）。 |
| 场景导入 | 通过。 |

### 16.1 ROI

通过。生活类比→适合/不适合→三问 ROI→「接口往往更便宜但不是永远」→绿条只证明写过的断言→Postman 互补。未绝对化。图见 IMG-CH16-001。

### 16.2 安装

通过。`python3 -m venv`、`python3 -m pytest`、禁止 `sudo pip`、密码不入库、`.venv` 不进 Git，与仓库 `.gitignore` 一致。本机 `python3 -m pytest --version` = `pytest 9.1.1`，与正文「审查机器」一致。双路径（自己目录 pip / `run.py setup`）见 CH16-0019。

### 16.3 收集与 assert

收集规则对文件名准确（官方默认 `python_files = test_*.py *_test.py`）。函数名写成 `test_*`，官方默认是前缀 `test`，见 CH16-0010。  
`qty_allowed` 与 `server.qty_allowed` 逻辑相同，本机 2 passed。  
fail demo 失败改写输出确为 `assert 11 <= 10`。  
「不要 `assert True`、不要用 print 代替断言」正确；与 16.4 用 print 的张力见 CH16-0015。  
装饰器段见 CH16-0001。图见 IMG-CH16-002。

### 16.4 requests

「先 `run.py serve`、第一帧 `MINISHOP_BASE_URL=http://127.0.0.1:8765`」本机复现。未启动会 `ConnectionError` 的说明正确。  
GET `keyword=鼠标` → 200，命中 `SKU-DEMO-001` 无线鼠标。  
`timeout`、`json=` → `Content-Type: application/json`、`data=` 字典为表单、`raise_for_status` 把 4xx 变成 `HTTPError`：均按 requests 官方行为复现。  
行为表 8 行对照 PRD / 本机：登录 200+token+Set-Cookie、错密码 401、`qty=10` 200、`qty=11` 400、无 Bearer 下单 401、下单 201 无 `status`、两次下单不同 `id`。`POST /login` 无前缀 → 404。  
GET+print 仍不是可收集测试，见 CH16-0015。

### 16.5 登录

硬编码 `BASE = "http://127.0.0.1:8765"`，不再吃 16B fixture。对刚启动的 serve：**2 passed**。  
`Set-Cookie` 在 `response.headers` 中，且含 HttpOnly（PRD R-AUTH；16.5 未断言 HttpOnly，属简化，可接受）。  
「不要写 `base_url` 参数否则 fixture not found」正确。  
作业命令指向 `run.py test` 正确。  
16.5 之后无「工作实战」标题，见 CH16-0011。截图见 IMG-CH16-005。

### 16A 常见错误 / 面试 / 练习 / 清单 / 总结

错误 1–5 均正确，且对准禁止绝对化清单。  
面试「xfail 是失败还是已修复」口径正确，但出现在 16A 尚未讲标记语法之时，见 CH16-0006。  
练习 1–4 与答案一致（先独立作答再对照）。  
检查清单未含 xfail，见 CH16-0018。  
可运行性 37/1 与本机一致。  
`https://docs.pytest.org/` 为官方入口（web_search 确认；本环境 `web_fetch` 因 SSRF 解析到 198.18.0.0/15 失败，不构成链接错误）。

### 16B 开篇 → 16.6

一句话核心可当过滤器。场景导入区分 `token_a` 非 autouse 与 `reset_seed_db` autouse，正确。  
scope 表与官方 `@pytest.fixture(scope=...)` 五档一致；默认 `function` 正确；`yield` 收尾正确；fixture 里 `assert` 失败为 setup ERROR，正确。  
16.6 片段读环境默认 8765，仓库 `base_url` 是 session + 临时端口，见 CH16-0003、CH16-0004。

### 16.7 conftest

「不会被当成测试模块收集」：本机把 `test_foo` 放进 `conftest.py`，`--collect-only` 未收集。机制是文件名不匹配 `python_files`。  
「同名覆盖更外层」符合官方 fixture 就近覆盖。  
「项目根放一份」与仓库 `tests/conftest.py` 不完全同句，见 CH16-0012。

### 16.8 Token fixture

片段 + 下单示例对 serve：**通过**（201，有 `id`，无 `status`）。  
「无凭证不要声明 `token_a`」正确。Cookie/Bearer 可同时出现，登录响应已复现。图见 IMG-CH16-004。

### 16.9 parametrize

八组 ids 与仓库 `test_cart_qty_cases` 逐行相同。对 serve：**8 passed**。  
`qty=10`→200、`qty=11`→400、四态与 `0`/`"1"` 均为 400，与 `server._cart_items` 分支一致。  
「一次只变一个主要无效条件」「无凭证另条 401」正确。  
默认 id 写成 `[body0]` 不精确，见 CH16-0016。

### 16.10 配置

`pytest.ini` 与仓库逐字相同。`testpaths`、`-ra` 官方语义正确。  
pytest 9 认识 `pytest.toml`（9.0 新增，且空文件也抢配置）正确；`pyproject.toml` 的 `[tool.pytest.ini_options]` 仍可用，9.0 另加原生 `[tool.pytest]`，入门不提可接受。  
空 `pytest.ini` 仍是配置源：官方「even when empty」——对，但 pytest 9 里空 `pytest.toml` 优先级更高。  
命令未钉 `cd project/minishop`，仓库根目录 `pytest --collect-only` 因 practice 下多个 `test_lab.py` 同名 **9 errors**，见 CH16-0009。  
`-ra`「本章用得少」低估其对 xfail 摘要的作用，见 CH16-0013。  
`pythonpath = .` 官方存在，本章说不必先上，正确。

### 工作实战 / 常见错误 / 面试 / 练习 5–10

工作实战命令、37/1、读三个文件、不另造 `/login`：通过。完成标准第 4 条要 403，阅读清单未指向对应测试，见 CH16-0008。  
错误 1–4 与冻结契约一致。  
面试三次下单断言（201、不同 id、无 status）正确且强于练习 8 答案，见 CH16-0007。  
练习 5–7、9–10 通过。练习 9 正确选项 C，A/B/D 分别打 ROI 绝对化、认证层次、GET/POST 神话。

## 8. 代码问题

### 8.1 章内 Python 块（逐块重新推导）

| # | 位置 | 推导 | 本机 |
| --- | --- | --- | --- |
| A1 | 16A L101 `qty_allowed` + `test_qty_one_allowed` | 语法正确；`type is int` 会拒绝 `bool`（比 `isinstance` 更严，与 `server.qty_allowed` 相同）；`1<=10` → True | 与 A2 同文件 **2 passed** |
| A2 | 16A L124 超库存 | 须与 A1 同文件（正文已标明）；`11<=10` → False | 同上 |
| A3 | 16A L139 fail demo | 故意失败；pytest 改写输出 `assert 11 <= 10` | **1 failed**，信息匹配正文 |
| A4 | 16A L171 GET products | 片段非 test；依赖 serve；`params` 会编码中文 | serve 上 **200**，items=`SKU-DEMO-001` |
| A5 | 16A L222 登录两测 | 无 fixture 依赖；错密码不断言 Body，也不 `raise_for_status` | serve 上 **2 passed** |
| B1 | 16B L35 `base_url` | 片段；默认 8765；仓库实现不同 | 作片段对 serve 可用 |
| B2 | 16B L85 `token_a` | 依赖 `base_url`；`.get("token")` 与仓库 `["token"]` 等价于成功路径 | 注入后可用 |
| B3 | 16B L107 下单 | SKU-DEMO-003 stock=3，qty=1 → 201；Body 无 status | **passed**；重复打常驻 serve 会耗库存（CH16-0003） |
| B4 | 16B L129 购物车 8 组 | 与仓库表一致；`None`→JSON `null` | **8 passed** |

隐藏依赖：A4/A5/B* 需要对端 MiniShop；B* 须由 pytest 收集 fixture。正文已标「片段」。未教授概念：装饰器（16A 有一句定义）、`tmp_path_factory`/`ThreadingHTTPServer`（工作实战会撞上）。

### 8.2 仓库套件（声称 37/1）

收集 38 项：`test_api` 23（含 8 组 parametrize + 1 xfail）+ `test_qty_rule` 4 + `test_register` 11。  
`python3 -m pytest -q`（`project/minishop`）：**37 passed, 1 xfailed**。  
xfail 节点：`test_empty_keyword_should_not_return_all`，`strict=True`，reason=`BUG-001 empty keyword returns full catalog`。空格关键字本机仍返回三件商品，与 `bugs/BUG-001.md`、PRD R-SEARCH 一致。

`token_a` 无 `autouse`；`reset_seed_db` 有 `autouse=True`；`base_url` `scope="session"` 且 `yield` 临时端口。与 16B 文字声明一致。

### 8.3 实操 16-1

`main.py` 优先 MiniShop `.venv`，否则 `sys.executable`；在 `project/minishop` 跑 `python3 -m pytest -q`；用输出是否含 `37 passed` 与 `1 xfailed`/`1 xfail` 判定。缺 pytest 时提示 `run.py setup`。  
本机：`python3 practice/run.py 16-1` → exit 0，写出 `validation/latest.json`（`passed_37=true`，`xfailed_1=true`）。  
`python3 practice/run.py 16-1 --check` → unittest **ok**（会再跑一遍套件）。

无 CODE 级不可运行缺陷。CH16-0004 是正文建议与仓库实现的冲突，不是片段语法错误。

## 9. 图片问题

详见第 9 节 IMG 记录（下）。MODIFY：IMG-CH16-002、IMG-CH16-004。其余 KEEP。

## 10. 表格问题

| 表 | 结论 |
| --- | --- |
| 16A 第三方库 | 通过。 |
| 16A requests 属性 | 通过。`json=` 会设 `Content-Type: application/json`（已复现）；`timeout` 不写可挂起（官方：默认不等待超时）。 |
| 16A MiniShop 行为 | 通过。与 PRD R-AUTH/R-CART-10/R-ORDER 及本机一致。未写 HttpOnly、未写注册，上半章可接受。 |
| 16B fixture scope | 通过。五档官方齐全；class 标明本章不用；package 标 ⭐。 |

## 11. 练习与答案问题

### 11.1 小练习：先独立作答，再对照

**练习 1**  
独立：适合——购物车 `qty=10/11` 与缺字段四态，每次回归都跑；不适合先自动——全新结算页还在改文案。依据：重复次数、界面稳定性、漏测损失。  
教材：同向。通过。

**练习 2**  
独立：`-m` 走当前解释器（通常 venv）里的 pytest，避免 PATH 上另一个副本。  
教材：一致。通过。

**练习 3**  
独立：默认不会被收集。改为 `test_login.py`（或 `login_test.py`）且 `def test_login_ok():`。  
教材：只给 `test_login.py` + `test_login_ok`。正确但不完整（`*_test.py` 也行）。不升 ISSUE，属答案取最小改法。

**练习 4**  
独立：`raise_for_status()` 在断言前把 400 变成 `HTTPError`，分不清实现是 400 还是 500。  
教材：一致。通过。本机对 401 调用 `raise_for_status()` 得到 `HTTPError: 401 Client Error`。

**练习 5**  
独立：默认 `function`。`autouse` 会让无凭证测试也先登录；若再共用 Session/Cookie，401 测脏。  
教材：一致。通过。

**练习 6**  
独立：不会收集。公共 `base_url` 放 `conftest.py`（项目根或 `tests/`）。  
教材：一致。通过。

**练习 7**  
独立：fixture 准备环境，parametrize 展开数据。购物车 qty/四态用 parametrize。  
教材：一致。通过。

**练习 8**  
独立：两次均 **201**、两个不同 **`id`**、Body **没有 `status`**。不要写待支付/已发货等状态名。  
教材：只写「两次都成功创建且 id 不同」。**【ANSWER VERIFICATION FAILED】** 见 CH16-0007。

**练习 9**  
独立：C。A ROI 绝对化；B 认证层次≠插件；D GET/POST 安全神话。  
教材：C。通过。

**练习 10**  
独立：200、`result=ok`、token 非空字符串、错密码 401。密码用教学账号 `Test1234`，只许本机。成功路径也可加 Set-Cookie（16.5 有）。  
教材：四项与密码口径一致，「合理四项即可」。通过。题干多出「不要写订单状态名」见 CH16-0017。

### 11.2 阶段测验 5（先独立作答）

覆盖 13–16 章。第 16 章直接相关为 6–10；按任务对全卷作答。

| # | 独立答案 | 教材 | 结果 |
| --- | --- | --- | --- |
| 1 | 接口擅长规则、状态码、权限、数据形状；UI 擅长按钮、跳转、文案。页面挂了接口绿仍可能失败，不能互相取消 | 同向 | 通过 |
| 2 | 缺字段/`null`/`""`/错误类型在 JSON 里不是同一回事，常走不同分支 | 同向 | 通过 |
| 3 | 以 PRD + OpenAPI 为准。`POST /login` 无 `/api` → 404 | 同向；本机 404 | 通过 |
| 4 | 课程口径：Environment 覆盖 Collection | 同向 | 通过（Postman 细节不在本章展开） |
| 5 | 会带着已登录态，测不到 401。无凭证不要 autouse token，不要共用已登录 Session | 同向 | 通过 |
| 6 | `-m` 用当前解释器里的 pytest | 同向 | 通过 |
| 7 | fixture 准备环境，parametrize 展开数据；多种 Body 用 parametrize | 同向 | 通过 |
| 8 | 不是永远最高。例：天天改文案的全新页面先手工 | 同向 | 通过 |
| 9 | `project/minishop/requirements.txt`；`python3 run.py setup` 然后 `python3 run.py test` | 同向 | 通过 |
| 10 | B | B | 通过 |

无测验级 【ANSWER VERIFICATION FAILED】。必过题 2/5/8 独立答案与教材同向。

## 12. 初学者理解障碍

【Beginner Friction】

1. 工作实战问「`base_url` 怎样起临时端口」，`conftest.py` 使用 `tmp_path_factory`、`ThreadingHTTPServer`、`port=0`、`yield` 停服务——16B 只教了读环境变量的片段（CH16-0003）。
2. 16A `ch16-collect` 图 caption 出现 autouse，读者还没到 16B（CH16-0002）。
3. 16A 16.3 解释装饰器，但上半章代码没有 `@`（CH16-0001）。
4. 自己目录 `pip install` 与 `run.py setup` 两套入口，没有「作业用哪一套」对照表（CH16-0019）。
5. 从仓库根打 `python3 -m pytest` 会因多个 `test_lab.py` 收集失败，报错像 pytest 坏了（CH16-0009）。
6. 16.4 用 `print`，16.3 又说不要用 print 代替断言（CH16-0015）。

## 13. 岗位能力缺口

【Job Reality Gap】

1. 以 xfail 为本章诚实证据的核心，却不教 `@pytest.mark.xfail` 与 `strict=True` / XPASS。仓库一旦修好 BUG-001，strict xfail 会让套件变红——这正是岗位上该发生的事，正文没说（CH16-0006）。
2. 「登录很慢就改 `scope=session`」在有 autouse 清库时会拿到失效 token（CH16-0004）。岗位上 session-scoped auth + 每测重置库是常见坑。
3. 完成标准要能讲他人订单 403，但阅读清单不指向那条测试（CH16-0008）。
4. pytest-html 截图未说明插件与 `--html`（第 17 章才到 Allure/pytest-html，可接受为了解，但仍造成「这张图怎么来的」）（CH16-0020）。
5. 常驻 `serve` 不 reset 时，注册号与库存会脏——作业路径用临时端口所以规定命令能绿，抄片段打 8765 则不一定（CH16-0003）。

## 14. 建议删除内容

- 不删主题。将 16A 16.3 末段装饰器说明**移到** 16B 16.6 首个 `@pytest.fixture` 之前（CH16-0001），16A 只留「下节才会用到 `@`」。
- `ch16-collect` caption 中「401 用例不要 autouse」删掉或移到 `ch16-no-autouse`（CH16-0002）。
- 16B 16.6「登录很慢再改为 `scope=session`」若保留，必须加 reset_db 警告；否则删掉这句（CH16-0004）。

## 15. 建议新增内容

1. **两扇门**（16.6 后）：抄片段 → 已启动的 `run.py serve`（8765，不自动回种）；仓库作业 → 只 `python3 run.py test`（临时端口 + `reset_seed_db`）。点明：不必会写线程，但要能指着 `yield f"http://127.0.0.1:{port}"`。
2. **xfail 最小语法**（16B 工作实战或 16.10 后）：从 `test_api.py` 摘 3 行 `@pytest.mark.xfail(..., strict=True)`，解释 XFAIL ≠ 失败 ≠ 已修复，XPASS+strict 会让套件变红。
3. 工作实战阅读清单加一条：`test_order_forbidden_other_user`（他人 403；管理员也不走 `/api/orders/{id}`，与 R-PERM 一致）。
4. 16.6：`token_a` 保持 function 的原因之一是 `reset_seed_db` 会删 `sessions` 表，session-scoped token 会 401。

## 16. 建议重写内容

- `ch16-collect.html` 的 `.lead` / `.caption`（CH16-0002），改完按 `diagrams/README.md` 重截 PNG。
- `ch16-no-autouse.html` 标题去掉「永远」（CH16-0005）。
- 练习 8 标准答案，与面试三段对齐（CH16-0007）。
- 16.10 命令块补 `cd project/minishop` 且说明用 venv/`run.py test`（CH16-0009）。

## 17. 本章结论

**B 小修**

理由：无 P0/P1；可抄 HTTP/pytest 示例全部跑通；仓库基线 37 passed / 1 xfailed 本机复现；ROI 未绝对化；MiniShop 契约与 PRD 一致。剩余是核心章不该留下的教学缺口（两扇门、xfail 语法、图与正文口径、练习 8 答案），改完即可，不需要部分重写或重新设计。

未达作者核心章 95 分目标，也未达 90 发布线——这是本审计的独立分数，不是对旧 99/95 分的继承。

## 18. 执行记录

### 18.1 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`
- `README.md`、`docs/COURSE_CONTROL.md`、`docs/COURSE_OUTLINE_v1.2.md`、`docs/LEARNING.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`、`practice/STATUS.md`、`practice/run.py`
- `exercises/README.md`
- `project/minishop/README.md`、`docs/PRD.md`（规则表与教学数据）、`requirements.txt`、`run.py`、`server.py`（qty/login/cart/order/search/reset_db）、`bugs/BUG-001.md`
- `chapters/16-pytest.md`、`16a-pytest-basics.md`、`16b-pytest-fixtures.md`
- `practice/16-pytest-regression/README.md`、`main.py`、`tests/test_lab.py`
- `project/minishop/pytest.ini`、`tests/conftest.py`、`test_api.py`、`test_qty_rule.py`、`test_register.py`
- `chapters/quizzes/README.md`、`stage-5-api.md`
- `reviews/chapter-16-review.md`、`reviews/_pedagogy-2026-09-10/ch16.md`、`RUBRIC.md`（线索，未照抄）
- `reviews/_rereview-2026-09-09/stage-5-ch13-16.md`、`reviews/v1.2.1-rescore.md`、`reviews/full-course-audit-v1.2.md`（线索：旧双基线问题在现行正文已消失）
- `chapters/assets/diagrams/ch16-collect.{html,png}`、`ch16-fixture.{html,png}`、`ch16-no-autouse.{html,png}`、`ch16-roi.{html,png}`
- `chapters/assets/09-pytest-report.png`
- `project/minishop/evidence/pytest-output.txt`、`evidence/http/01-login-ok.txt`、`03-products-empty-keyword.txt`
- `chapters/assets/diagrams/README.md`

未读其他章正文。

### 18.2 实际跑过的命令与结果摘要

| 命令/实验 | 结果 |
| --- | --- |
| `python3 -m pytest --version` | pytest 9.1.1 |
| `python3 -c "import requests; print(requests.__version__)"` | 2.34.2 |
| 16A `qty_allowed` 两测 | 2 passed |
| 16A fail demo | failed，`E assert 11 <= 10` |
| 收集：`login.py`/`login_ok` vs `test_login.py`/`test_login_ok` | 前者 0，后者收集 |
| `def testok()` 是否收集 | **会收集**（官方前缀 `test`） |
| `conftest.py` 内 `test_foo` | **不收集** |
| MiniShop `--collect-only -q` | 38 tests collected |
| MiniShop `pytest -q` | **37 passed, 1 xfailed**（BUG-001） |
| `python3 project/minishop/server.py` | 打印 `MINISHOP_BASE_URL=http://127.0.0.1:8765` |
| 16.4 GET `keyword=鼠标` | 200，无线鼠标 |
| 16.5 登录两测 vs serve | 2 passed |
| 16.6+16.8+16.9 拼装 vs serve | 9 passed |
| `POST /login` | 404 `{"error":"not found"}` |
| 购物车/下单无 Bearer | 401 |
| `raise_for_status()` on 401 | `HTTPError` |
| `json=` Content-Type | `application/json` |
| `data=` 字典 Content-Type | `application/x-www-form-urlencoded` |
| 两次 `POST /api/orders` | 201，不同 id，无 `status` |
| 注册 `13900001111` | 201 无 token；第二次 **409**（脏 serve） |
| session token + `reset_db` 后再带 Bearer | **401** |
| 仓库根目录 `pytest --collect-only` | **9 collection errors**（practice 下重复 `test_lab.py` 模块名） |
| `-k login`（minishop cwd） | 4/38 collected |
| `python3 practice/run.py 16-1` | exit 0，37/1，写出 `validation/latest.json` |
| `python3 practice/run.py 16-1 --check` | unittest ok |

未执行：`python3 run.py setup`（以免改 project；`--check` 时目录中已出现 `.venv`，疑为并行 agent 所建）、`python3 run.py test`（会改写 `evidence/pytest-output.txt` / html，禁止改 project）。等价命令 `python3 -m pytest -q` 在 `project/minishop` 已跑。

Windows 激活 / `Activate.ps1`：本机 macOS，未点。【External Verification Required】仅此项 GUI。

### 18.3 外部核查

| 条目 | 来源 | 结论 |
| --- | --- | --- |
| 收集 `python_files` 默认 | pytest 9 API Reference | `["test_*.py", "*_test.py"]`，与正文一致 |
| 收集 `python_functions` 默认 | 同上 | `["test"]` **前缀**，正文写成 `test_*`（CH16-0010） |
| fixture scope / 默认 function / autouse / yield | pytest fixture API | 与正文一致 |
| conftest 共享、就近覆盖 | fixtures reference | 与正文一致 |
| xfail / XPASS / `strict=True` | skipping.html | 仓库用法正确；正文未教语法（CH16-0006） |
| `pytest.toml` 9.0 新增、空文件也抢配置 | customize.html | 正文「pytest 9 还认识 pytest.toml」正确 |
| `pytest.ini` even when empty | 同上 | 正确；9.0 起 toml 优先于 ini |
| `pythonpath` | 配置参考 | 存在，正文「不必先上」正确 |
| `-k`、`--collect-only`、`-ra`（a=all except passed） | usage / output | 与正文一致 |
| assert 改写打印中间值 | how-to/assert | 与 fail demo 输出一致 |
| `requests` `json=` / `timeout` / `raise_for_status` | requests 2.34.2 docs | 与正文一致 |

docs.pytest.org 的 `web_fetch` 被 SSRF 拦截（解析到 198.18.x）；改用 `web_search` 摘官方页片段。链接本身有效。

---

## ISSUE

ID：CH16-0001  
文件：`chapters/16a-pytest-basics.md`  
章节：16A  
小节：16.3 测试函数与 assert  
精确位置：16.3 末段「`@` 是装饰器…」  
原文：`@` 是装饰器：写在函数上一行，把函数交给别人处理。本章只要求会用 pytest 提供的两个：`@pytest.fixture` 和 `@pytest.mark.parametrize`。  
问题等级：P2  
问题类别：PRE / PED / SEQ  
问题说明：上半章没有任何 `@` 代码，却要求建立装饰器心智模型，并点名 16B 才出现的两个装饰器。与质量标准「不得无提示引入未学习的装饰器」相比，提示有了，但放错册。  
为什么有问题：零基础读者在刚学会 `assert` 时被拉去记 16B API，16A 的闭环（qty 纯函数）被打断。  
依据：Quality Standard §六；教学审查尺「后文不调用尚未教的技能」。  
建议修改：整段移到 16B 16.6 第一个代码块前；16A 改一句「下节才会看到函数上一行的 `@`，现在不必会写」。  
推荐替换文本：16A 删除该段。16B 16.6 代码前插入：`@` 是装饰器：写在函数上一行，把函数交给别人处理。本节只用 pytest 提供的 `@pytest.fixture`；下一节再用 `@pytest.mark.parametrize`。不要自己实现装饰器，也不要展开 class 测试。

## ISSUE

ID：CH16-0002  
文件：`chapters/assets/diagrams/ch16-collect.html`（及 `ch16-collect.png`）；出现在 `chapters/16a-pytest-basics.md` 16.3  
章节：16A  
小节：16.3  
精确位置：示意图 `.lead` 与 `.caption`  
原文：lead「python3 -m pytest 用的是当前解释器里的 pytest…」；caption「…401 用例不要 autouse 已登录 token。」  
问题等级：P2  
问题类别：IMG / SEQ / PED  
问题说明：图插在「按文件名收集」旁，主句却在讲 `-m pytest`；脚注把 16B 的 autouse 提前倒给 16A 读者。  
为什么有问题：16A 练习 3 考的是收集规则，图没有帮这一刀；autouse 无上下文，只能当生词跳过或记错时机。  
依据：教学审查尺「图讲的是难点」；pytest 收集约定官方页。  
建议修改：lead 改回收规则；caption 只留 conftest 不被收集 + `-m` 用当前解释器。autouse 只留在 `ch16-no-autouse`。改 HTML 后按 `diagrams/README.md` 重截 PNG。  
推荐替换文本：lead：`文件要叫 test_*.py 或 *_test.py，函数名以 test 开头。名字不像约定，pytest 会当没看见。` caption：`示意图：conftest.py 放公共 fixture，自己不会当测试收集。python3 -m pytest 用的是当前解释器里的那一份。`

## ISSUE

ID：CH16-0003  
文件：`chapters/16b-pytest-fixtures.md`  
章节：16B  
小节：16.6、工作实战  
精确位置：16.6 `base_url` 片段之后「仓库套件自己起临时端口，见 `tests/conftest.py`」；工作实战第 1 问  
原文：仓库套件自己起临时端口，见 `tests/conftest.py`。 / `base_url` 怎样起临时端口  
问题等级：P2  
问题类别：PED / JOB  
问题说明：作业问临时端口，正文可抄 fixture 却是 `MINISHOP_BASE_URL` 默认 8765。`conftest.py` 用 `tmp_path_factory`、`ThreadingHTTPServer(("127.0.0.1", 0), …)`、`yield` 停服务——均未教。抄 16.8 打常驻 serve 会扣 `SKU-DEMO-003` 库存（stock=3）；本机对脏 serve 第二次注册 `13900001111` 已得 409。  
为什么有问题：规定命令 `run.py test` 能绿，抄片段打 8765 则不一定；读者无法只靠 16.6 回答工作实战第 1 问，打开 conftest 又看不懂。  
依据：本机对照实验；`server.reset_db` / 下单扣库存。  
建议修改：写死两扇门；明确「现在不必会写 class/线程，但要能指着 yield 的随机端口」；警告常驻 serve 不回种。  
推荐替换文本：这里有两扇门，不要混：① 抄上面片段到自己练习目录：对端是已经启动的 `python3 run.py serve`（8765）。serve 不重启则库不回种，注册过的手机、卖完的 SKU 再跑会红。② 仓库作业不要设 8765、不要另写 conftest。命令只有：`cd project/minishop && python3 run.py setup && python3 run.py test`。`tests/conftest.py` 的 `base_url` 起临时端口，`reset_seed_db` 是 autouse 回种，不是拿来测 401 的。

## ISSUE

ID：CH16-0004  
文件：`chapters/16b-pytest-fixtures.md`  
章节：16B  
小节：16.6  
精确位置：`token_a` 用默认 `function` 最稳…登录很慢时再改为 `scope="session"`  
原文：登录很慢时再改为 `scope="session"`。  
问题等级：P2  
问题类别：ACC / CODE / JOB  
问题说明：MiniShop token 存在 `sessions` 表。`reset_seed_db` 每测 `unlink` 数据库。session-scoped `token_a` 会在 reset 之后变成 401。本机：登录拿到 token → `reset_db` → 再带 Bearer 访问购物车 → **401**。  
为什么有问题：读者按「最稳是 function，慢了再改 session」去改仓库 `token_a`，会看到认证用例集体红，误判 pytest/fixture 坏了。  
依据：pytest「更高 scope 先执行」；`server.reset_db`；本机复现。  
建议修改：删掉「再改为 session」，或明确「只要还有 autouse 清库，token 就不能 session」。  
推荐替换文本：`token_a` 必须保持默认 `function`：每个需要它的测试在 `reset_seed_db` 之后自己登录一次。不要改成 `scope="session"`——仓库每次测试都会把库打回种子，`sessions` 表里的旧 token 会立刻失效（本课程已复现为 401）。登录成本用 session 去摊，只适用于**不**每测清库的项目。

## ISSUE

ID：CH16-0005  
文件：`chapters/assets/diagrams/ch16-no-autouse.html`（及 png）；`chapters/16b-pytest-fixtures.md` 16.8  
章节：16B  
小节：16.8  
精确位置：示意图 `<h1>`  
原文：测「没带通行证」时，夹具若自动登录，你永远测不到 401  
问题等级：P2  
问题类别：IMG / ACC  
问题说明：标题用「永远」。同章正文写：`token_a` 只 `return` 字符串，不会自动粘到未声明参数的请求上；要 Session/Cookie 才会测脏。autouse 单独的效果是「多打一次登录」，401 用例仍可能绿。  
为什么有问题：图把已经修过的绝对化又画回去，和错误 1、练习 5 的细口径打架。  
依据：16B 16.6 末段；rereview 已纠正「单 autouse ≠ 测不到 401」。  
建议修改：标题改为条件句。  
推荐替换文本：测「没带通行证」时，不要 autouse 登录夹具；若再共用 Session 或 Cookie，你就测不到 401。

## ISSUE

ID：CH16-0006  
文件：`chapters/16a-pytest-basics.md`、`chapters/16b-pytest-fixtures.md`  
章节：16A 面试 / 16B 工作实战  
小节：面试「xfail 是失败还是已修复」；工作实战完成标准 2  
精确位置：16A 面试第三题；16B 全文搜索 `@pytest.mark.xfail` **零处**  
原文：仓库 37 passed、1 xfailed，对应 BUG-001 仍开放。  
问题等级：P2  
问题类别：PED / JOB  
问题说明：一句话核心、实操 16-1、面试都围着 xfail，正文从不展示 `@pytest.mark.xfail(reason="…", strict=True)`，也不提 XPASS。仓库该标记是 `strict=True`：BUG-001 一旦修好，套件会因 XPASS 变红。  
为什么有问题：学生能背「xfail 不是失败也不是已修复」，却不会在代码里认出它，也无法解释「修了为什么还红」。  
依据：pytest skipping.html `strict` 参数；`tests/test_api.py` L222。  
建议修改：16B 工作实战增加 8 行摘录 + XFAIL/XPASS 对照。  
推荐替换文本：仓库里那 1 条长这样（不要改它）：

```python
@pytest.mark.xfail(reason="BUG-001 empty keyword returns full catalog", strict=True)
def test_empty_keyword_should_not_return_all(base_url):
    ...
```

失败且被标记 → 摘要里 `xfailed`，套件仍返回 0。若有一天空搜索不再返回全量，`strict=True` 会把它变成失败（XPASS），提醒你去掉 xfail 并关缺陷。这不是「测试写坏了」。

## ISSUE

ID：CH16-0007  
文件：`chapters/16b-pytest-fixtures.md`  
章节：16B  
小节：练习 8 / 练习答案 8  
精确位置：练习 8 题干与答案第 8 条  
原文：答案「两次都成功创建且 `id` 不同（v1.0 默认不幂等）。」  
问题等级：P2  
问题类别：ANS / EX  
问题说明：【ANSWER VERIFICATION FAILED】独立答案为：两次都 **201**、两个不同 **id**、Body **没有 `status`**。同章面试第三题已是这三项。练习答案漏掉状态码和冻结字段。题干「不要写订单状态名」容易让作者把「断言没有 `status` 字段」也删掉。  
为什么有问题：学生按答案写自动化，可能不断言 201、不断言无 `status`，与 R-ORDER 和 16.8 示例不一致。  
依据：PRD R-ORDER；16B 面试「两次都 201、两个不同 id、Body 没有 status」；本机两次下单复现。  
建议修改：答案与面试对齐。  
推荐替换文本：8. 两次都返回 201、两个不同的 `id`、Body 里没有 `status` 字段（v1.0 默认不幂等，也没有订单状态机）。不要写「待支付/已发货」这类状态名。若正式需求改成幂等，再按正式文档改期望。

## ISSUE

ID：CH16-0008  
文件：`chapters/16b-pytest-fixtures.md`  
章节：16B  
小节：MiniShop 工作实战 完成标准 4  
精确位置：完成标准第 4 条 vs 「打开三个文件」清单  
原文：能说明无 Bearer 下单是 401、他人订单是 403。 / 打开：conftest、`test_cart_qty_cases`、`test_register.py`  
问题等级：P2  
问题类别：EX / PED  
问题说明：401 在 16.4 表里有；403 只存在于 `test_order_forbidden_other_user`（且管理员走 `/api/orders/{id}` 也是 403，R-PERM）。阅读清单不指向该测试。  
为什么有问题：完成标准无法用工作实战指定的三处读后回答，除非自己把 `test_api.py` 读完。  
依据：PRD R-PERM；`tests/test_api.py` `test_order_forbidden_other_user`。  
建议修改：清单加第 4 个指针。  
推荐替换文本：4. `tests/test_api.py` 的 `test_create_order_unauthorized` 与 `test_order_forbidden_other_user`：无 Bearer 下单 401；他人订单 403。管理员也不走 `GET /api/orders/{id}` 看别人的单（R-PERM）。

## ISSUE

ID：CH16-0009  
文件：`chapters/16b-pytest-fixtures.md`  
章节：16B  
小节：16.10 常用命令  
精确位置：`python3 -m pytest` 等五条，无 `cd`  
原文：

```bash
python3 -m pytest
python3 -m pytest -q
...
```

问题等级：P2  
问题类别：SEQ / PED / CODE  
问题说明：16A 刚警告不要用系统 pytest 打没 venv 的空环境。16.10 又给出无 cwd、无 venv 的 `python3 -m pytest`。本机在**仓库根**执行 `pytest --collect-only`：因 `practice/*/tests/test_lab.py` 模块同名，**9 errors during collection**。  
为什么有问题：初学者从 README 克隆后在根目录模仿 16.10，会得到与「pytest 坏了」无法区分的报错，而规定作业 `cd project/minishop && python3 run.py test` 是绿的。  
依据：本机收集错误；pytest 默认把同名测试模块当冲突。  
建议修改：命令全部带 cwd，并指向 `run.py test`。  
推荐替换文本：

```bash
cd project/minishop
python3 run.py test          # 推荐：venv + 临时端口
python3 -m pytest -q         # 须已 setup，且当前目录是 project/minishop
python3 -m pytest --collect-only -q
python3 -m pytest -k login
python3 -m pytest tests/test_api.py
```

不要在课程仓库根目录直接打 `pytest`：`practice/` 里有多份 `test_lab.py`，收集会报模块同名错误。

## ISSUE

ID：CH16-0010  
文件：`chapters/16a-pytest-basics.md`  
章节：16A  
小节：16.3  
精确位置：pytest 默认收集 · 函数名 `test_*`  
原文：函数名 `test_*`。  
问题等级：P3  
问题类别：TERM / ACC  
问题说明：官方 `python_functions` 默认 `["test"]`，是前缀不是 glob。本机 `def testok():` 会被收集。正文 `test_*` 是常见写法，作为「推荐命名」对，作为「默认收集规则」略窄。  
为什么有问题：较真的学生用 `testok` 会发现「书上说不会收集，实际上会」。  
依据：pytest 9 API Reference `python_functions` Default `["test"]`；本机收集。  
建议修改：改成「函数名以 `test` 开头（习惯写成 `test_` + 下划线）」。  
推荐替换文本：函数名以 `test` 开头（请写成 `test_login_ok` 这种带下划线的名字，不要叫 `login_ok`）。

## ISSUE

ID：CH16-0011  
文件：`chapters/16a-pytest-basics.md`  
章节：16A  
小节：16.5 之后至「常见错误」之前  
精确位置：L256 起「安装请优先使用仓库依赖」无标题  
原文：安装请优先使用仓库依赖：… HTML 报告截图 …  
问题等级：P3  
问题类别：PED  
问题说明：质量标准要求每章有 MiniShop 工作实战。拆章后作业在 16B 合理，但 16A 这段命令+截图像掉了标题的工作实战。  
为什么有问题：读者不知道这是「上半章可跑的最小验收」还是 16.5 的附录。  
依据：Quality Standard §七。  
建议修改：加标题「上半章可运行验收（完整套件在 16B）」或并入 16.5。  
推荐替换文本：`## 上半章可运行验收`（其余命令保持，并写明完整 37/1 到 16B / 实操 16-1）。

## ISSUE

ID：CH16-0012  
文件：`chapters/16b-pytest-fixtures.md`  
章节：16B  
小节：16.7 vs 练习 6 vs 16.10 目录  
精确位置：16.7「项目根目录放一份即可」  
原文：项目根目录放一份即可。  
问题等级：P3  
问题类别：TERM  
问题说明：仓库实际是 `tests/conftest.py`；练习 6 答案是「项目或 tests 目录」。三处不完全同句。  
为什么有问题：学生可能在 `project/minishop/conftest.py` 和 `tests/conftest.py` 各放一份，同名 fixture 打架。  
依据：pytest conftest 就近覆盖；仓库布局。  
建议修改：16.7 与目录树对齐。  
推荐替换文本：入门在 `tests/conftest.py` 放一份即可（本仓库就是这样）。项目根也可以放，pytest 会向上找；不要两层写同名 fixture。

## ISSUE

ID：CH16-0013  
文件：`chapters/16b-pytest-fixtures.md`  
章节：16B  
小节：16.10  
精确位置：`-ra` 解释  
原文：`-ra` 在结束时多打印跳过等原因（本章用得少，但报告更完整）。  
问题等级：P3  
问题类别：PED  
问题说明：仓库 `addopts = -ra` 正是为了在摘要里打出 `XFAIL … BUG-001`。说「本章用得少」低估了它和 37/1 的关系。  
为什么有问题：学生可能删掉 `-ra` 还觉得「反正用得少」。  
依据：pytest `-r` 字符表，`a` = all except passed；本机摘要含 XFAIL 行。  
建议修改：把 `-ra` 和 xfail 摘要连起来。  
推荐替换文本：`-ra` 会在结束时多打一行摘要。本章靠它看见 `XFAIL tests/test_api.py::test_empty_keyword_should_not_return_all - BUG-001 …`，不要删。

## ISSUE

ID：CH16-0014  
文件：`chapters/assets/diagrams/ch16-no-autouse.html`；`chapters/assets/09-pytest-report.png`  
章节：16A/16B  
小节：16.8 图标题；16A 截图  
精确位置：h1「夹具」；图片路径 `assets/09-pytest-report.png`  
原文：夹具若自动登录；`![pytest-html …](assets/09-pytest-report.png)`  
问题等级：P3  
问题类别：TERM / IMG  
问题说明：全书与本章正文用 fixture，图标题用「夹具」；报告截图文件名像第 9 章。  
为什么有问题：检索「fixture」找不到图标题；`09-` 让人以为图走错章。  
依据：本章其余图/正文用 fixture。  
建议修改：标题改回 fixture；截图可复制为 `assets/16-pytest-report.png` 再引用（不必强改 evidence 原名）。  
推荐替换文本：图标题用「fixture」；16A 引用 `assets/16-pytest-report.png`（内容可与现图相同）。

## ISSUE

ID：CH16-0015  
文件：`chapters/16a-pytest-basics.md`  
章节：16A  
小节：16.3 vs 16.4  
精确位置：16.3「也不要用 `print` 代替断言」；16.4 `print(response.status_code)`  
原文：不要用 `print` 代替断言。 / `print(response.status_code)`  
问题等级：P3  
问题类别：PED / CODE  
问题说明：16.4 已标明片段，但仍是上半章第一条 HTTP 代码。学习目标写「发 JSON」，示例却是 GET+print；带 assert 的 HTTP 要到 16.5。  
为什么有问题：照 16.4 保存成 `test_*.py` 会收集到 0 条，以为 pytest 没跑。  
依据：本机把 print 片段当脚本可跑，当测试则无用例。  
建议修改：16.4 加一句「这不是测试函数，不要指望 pytest 收集它」；或改成带 `assert` 的 `test_products_keyword_mouse`。  
推荐替换文本：这是普通脚本片段，用来确认 serve 已开。pytest 只收集 `test_` 函数；下一节的登录示例才是测试。

## ISSUE

ID：CH16-0016  
文件：`chapters/16b-pytest-fixtures.md`  
章节：16B  
小节：16.9  
精确位置：`ids` 解释  
原文：比默认的 `[body0]` 好读。  
问题等级：P3  
问题类别：TERM  
问题说明：parametrize 默认 id 一般是参数值的 saferepr，不是 `[body0]`。`ids=` 仍然值得教。  
为什么有问题：学生 `--collect-only` 看不到 `[body0]`，会怀疑自己用法不对。  
依据：pytest parametrize 默认 id 规则。  
建议修改：改成「比默认把整个 dict 塞进节点名更好读」。  
推荐替换文本：`ids` 出现在收集列表和失败报告里，比默认把一整坨 `{'sku': …}` 塞进节点名更好读。

## ISSUE

ID：CH16-0017  
文件：`chapters/16b-pytest-fixtures.md`  
章节：16B  
小节：练习 10  
精确位置：题干末句  
原文：列出 MiniShop 登录测试最少要断言的 4 项（含一项失败密码）。密码如何提供？不要写订单状态名。  
问题等级：P3  
问题类别：EX  
问题说明：「不要写订单状态名」是练习 8 的约束，登录题不需要。像复制残留。  
为什么有问题：干扰审题。  
依据：题干与 16.5 登录断言无关订单。  
建议修改：删掉该句。  
推荐替换文本：列出 MiniShop 登录测试最少要断言的 4 项（含一项失败密码）。密码如何提供？

## ISSUE

ID：CH16-0018  
文件：`chapters/16a-pytest-basics.md`  
章节：16A  
小节：本章检查清单  
精确位置：四条 checklist  
原文：ROI / 运行 pytest / requests JSON / 不对 400 先 raise_for_status  
问题等级：P3  
问题类别：PED  
问题说明：16A 面试已考 xfail，清单没有「我能解释 xfailed ≠ 失败 ≠ 已修复」。  
为什么有问题：检查清单应能验证面试刚问过的能力。  
依据：Quality Standard §七 检查清单可验证能力。  
建议修改：加一条，或写「xfail 的含义见 16B，上半章能指着 HTML 报告的 Expected failures」。  
推荐替换文本：`- [ ] 我能指着 37 passed / 1 expected failure 说：那 1 条不是挂了，也不是已修复`

## ISSUE

ID：CH16-0019  
文件：`chapters/16a-pytest-basics.md`  
章节：16A  
小节：16.2 与 16.5 后命令  
精确位置：16.2「在自己的练习目录建虚拟环境，不要拿课程仓库当安装实验场」vs 随后 `cd project/minishop && python3 run.py setup`  
原文：见上。  
问题等级：P3  
问题类别：PED  
问题说明：两条安装路径都对，但没有「作业/实操 16-1 用 minishop venv；自己玩 qty 纯函数用练习目录」对照。  
为什么有问题：有人在仓库根 `pip install`，有人两套都不做然后怪 16-1。  
依据：practice README「16-1 需要先 setup」。  
建议修改：加三行对照。  
推荐替换文本：作业和实操 16-1：只在 `project/minishop` 里 `python3 run.py setup`（它会建 `.venv`，不要手搓到仓库根）。16.3 的 qty 纯函数：可以在**自己的练习目录**另建 venv。不要 `sudo pip`，不要把 `.venv` 提交进 Git。

## ISSUE

ID：CH16-0020  
文件：`chapters/16a-pytest-basics.md`  
章节：16A  
小节：16.5 后截图  
精确位置：`![pytest-html 37 passed / 1 expected failure](assets/09-pytest-report.png)`  
原文：HTML 报告截图  
问题等级：P3  
问题类别：PED / JOB  
问题说明：截图来自 pytest-html 4.2.0（与 `requirements.txt` 一致），由 `run.py test` 的 `--html` 生成。16.2 只装 `pytest requests`，个人 venv 得不到这张图。第 17 章才点名 pytest-html，可接受推迟，但此处应一句交代来源。  
为什么有问题：读者 `pip install pytest requests` 后找不到 pytest-report.html，以为自己没跑对。  
依据：`project/minishop/run.py` `run_pytest`；截图 Environment 行 pytest-html v4.2.0。  
建议修改：标明来源，并说自己练习目录不必生成 HTML。  
推荐替换文本：这张图是仓库 `python3 run.py test` 用插件 `pytest-html` 生成的（`requirements.txt` 里有）。上半章自己的 venv 不必装它；看终端里的 `.` 和 `passed` 即可。

## ISSUE

ID：CH16-0021  
文件：`practice/16-pytest-regression/README.md`  
章节：实操 16-1  
小节：标题  
精确位置：H1  
原文：实操 16-1 ★★：37 绿、1 条 xfail 是什么意思？  
问题等级：P3  
问题类别：TERM / PED  
问题说明：正文立刻澄清 xfail 不是全绿，但标题「37 绿」仍可被扫成「全绿」。  
为什么有问题：与全书「不要把 37/1 说成全绿」的纪律略冲。  
依据：16B 错误 2；实操正文第 17–18 行其实是对的。  
建议修改：标题改「37 passed + 1 xfailed 是什么意思？」。  
推荐替换文本：`# 实操 16-1 ★★：37 passed、1 条 xfailed 是什么意思？`

---

### 图片记录

IMG-CH16-001  
文件：`chapters/assets/diagrams/ch16-roi.png` + `ch16-roi.html`  
出现位置：16A 16.1  
图片主要内容：左「适合先自动」（稳定重复能判断），右「不要当第一步」（不稳、没预期、一次性）；lead 写接口往往更便宜但不是永远。  
技术准确性：正确，未把 ROI 绝对化。  
与正文一致性：与 16.1 列表一致。  
文字是否正确：是。  
UI 是否过时：否（概念图）。  
教学价值：高，对准本章禁止的绝对化。  
可读性：好；PNG 下方大片留白，不影响阅读。  
是否需要修改：否  
修改建议：—  
最终结论：KEEP

IMG-CH16-002  
文件：`chapters/assets/diagrams/ch16-collect.png` + `ch16-collect.html`  
出现位置：16A 16.3  
图片主要内容：左会收集 `test_login.py`/`test_login_ok`，右不会收集 `login.py`/`login_ok`。  
技术准确性：盒子内容正确；lead/caption 与收集主题错位（见 CH16-0002）。  
与正文一致性：盒子与 16.3 一致；caption 提前讲 autouse，与 16A 不一致。  
文字是否正确：盒子正确；脚注超范围。  
UI 是否过时：否。  
教学价值：中（被 lead/caption 稀释）。  
可读性：好。  
是否需要修改：是  
修改建议：见 CH16-0002。  
最终结论：MODIFY

IMG-CH16-003  
文件：`chapters/assets/diagrams/ch16-fixture.png` + `ch16-fixture.html`  
出现位置：16B 16.6  
图片主要内容：左 fixture 准备环境，右 parametrize 八组 Body（qty=1/10/11/缺/null/""/"1"/0）。  
技术准确性：八组与代码一致（旧「六种」已不在）。左卡「先启动 MiniShop」对抄片段成立，对 `run.py test` 不完全成立，被 CH16-0003 覆盖，不单开图 ISSUE。  
与正文一致性：与 16.9「八个」一致。  
文字是否正确：是。  
UI 是否过时：否。  
教学价值：高。  
可读性：好。  
是否需要修改：否（两扇门用正文补，不必为这句话换图）  
修改建议：若改两扇门图可另增，非必须。  
最终结论：KEEP

IMG-CH16-004  
文件：`chapters/assets/diagrams/ch16-no-autouse.png` + `ch16-no-autouse.html`  
出现位置：16B 16.8  
图片主要内容：需要 token 的测试显式写参数；401 用例不要 autouse。  
技术准确性：盒子正确；h1「永远测不到 401」过绝对（CH16-0005）。  
与正文一致性：与错误 1 的细口径不完全一致。  
文字是否正确：盒子正确，标题过强。  
UI 是否过时：否。  
教学价值：高（401 是本章难点）。  
可读性：好。「夹具」用词见 CH16-0014。  
是否需要修改：是  
修改建议：见 CH16-0005、CH16-0014。  
最终结论：MODIFY

IMG-CH16-005  
文件：`chapters/assets/09-pytest-report.png`  
出现位置：16A 16.5 后  
图片主要内容：pytest-html 报告，09-Sep-2026，pytest-html v4.2.0，38 tests，37 Passed，1 Expected failures，0 Failed。  
技术准确性：与基线 37/1 一致，与 `requirements.txt` 的 pytest-html==4.2.0 一致。  
与正文一致性：一致。  
文字是否正确：是。  
UI 是否过时：否（就是本仓库产物）。  
教学价值：中高（证明 Expected failures ≠ Failed）；未展示 xfail 用例名，需靠终端 `-ra`。  
可读性：摘要区清楚，细节表为空（未展开）。  
是否需要修改：文件名 `09-` 易误导（CH16-0014），内容可留。  
修改建议：复制为 `16-pytest-report.png` 再引用；或正文注明「文件名沿用 evidence 截图编号」。  
最终结论：KEEP（命名 P3，不强制换图）
