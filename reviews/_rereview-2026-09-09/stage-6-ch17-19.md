# 阶段 6 复审：第 17、18、19 章

- 日期：2026-09-09
- 范围：`chapters/17-automation-overview.md`、`18-performance-testing.md`、`19-minishop-project.md`；`project/minishop/` 抽查；`practice/19-project-pack/`；`chapters/quizzes/stage-6-project.md`
- 依据：Quality Standard v1.0、冻结口径、PRD v1.0。旧 `reviews/` 与 v1.2.1 复评分不当成成绩。
- 复跑：本机 `python3 project/minishop/run.py test` 与 `python3 practice/19-project-pack/main.py` 均为 **37 passed, 1 xfailed**（pytest 9.1.1 / requests 2.34.2）。`run.py test` 会改写 `evidence/pytest-output.txt`，审查后已还原该证据文件。

---

## 总判

三章冻结口径整体守住：**没有**把接口 ROI 写成永远最高；**没有**把 Playwright 写成 UI 回归套件；UI 示例 `goto` 是 `/` 不是 `/login`；第 18 章有 `.jmx` 骨架和步骤，正文反复写明未安装、未跑 GUI、未加压、未冻结 SLA；第 19 章第一次把 `/api/`、qty=10 允许 / 11 拒绝、订单无 `status` 写成项目基线；pytest 基线 37/1、BUG-001 仍开放；MiniShop 只作个人实践。超库存在计划与用例里都是 **P0**，没有「计划 P1、用例 P0」。下一章预告为 18 → 19 → 20。

第 17 章是地图，不是空泛工具清单，也没有把未实现的 CI/UI 套件写成仓库已有。第 18 章**没有**把未跑压测写成结论，不应当因为「作者没点 JMeter GUI」卡在发布线 90。第 19 章仓库能跑、数字 37/1 能对上，但正文仍写 Postman「**9 个请求**」，集合实际是 **15** 个——这正好踩中冻结句「覆盖矩阵、Postman 请求数、pytest 覆盖范围必须与正文数字一致」。核心章目标 95 **未达到**，不要继承旧分 96。

实操 19-1 **能**检查「37/1」：它真的在 `project/minishop` 跑 pytest，并同时要求 BUG-001 仍开放。它不检查 Postman 个数。

| 章 | 本轮 | 旧分（不继承） | 目标 | DoD | 发布 |
| ---: | ---: | ---: | ---: | --- | --- |
| 17 | **92** | 91 | 90 | 20/20（有低优先级备注） | 可维持 |
| 18 | **92** | 90 | 90 | 19/20 | 可维持；未踩「假压测结论」线 |
| 19 | **93** | 96 | **95** | 18/20 | 可维持 90 线；**未达 95**，须改过时数字 |

---

## 各章评分

### 第 17 章《自动化测试进阶概览》— 92/100

一句话核心与冻结一致：越靠近 UI 的观察越贵。接口优势全部带场景；错误 1 与练习 9 明确打掉「ROI 永远最高」。Playwright/Selenium 标「示例结构」，`page.goto(".../")`，审查声明未装驱动。CI YAML 标明不是本仓库流水线（仓库无 `.github/workflows`）。pytest-html 声明已在独立 venv 跑过。实战是书面分层地图，不是交 UI 套件。

| 项目 | 满分 | 得分 | 说明 |
| --- | ---: | ---: | --- |
| 技术准确性 | 25 | 24 | 分层/金字塔/等待/CI 正确；面试示例「六种输入」与仓库 8 条购物车 parametrize 不完全同口径 |
| 知识完整性 | 15 | 13 | 地图章该有的都有；Allure/Cypress 点到为止，符合第三梯队 |
| 初学者友好 | 15 | 14 | 生活类比 + MiniShop 对照表清楚 |
| 实战价值 | 15 | 13 | 书面地图能练判定；本章本来就不该变成第二套框架课 |
| 示例质量 | 10 | 9 | `goto /`、选择器与 `frontend/index.html` 的 `#login-btn` / 按钮文案「登录」对得上 |
| 项目一致性 | 5 | 4 | 场景仍用教学路径 `POST /cart/items`（第 19 章前允许），但库存 10 / qty=11→400 已是 v1.0 行为，标签可再硬一点 |
| 面试价值 | 5 | 5 | 金字塔、ROI、初级边界都有反例 |
| 练习质量 | 5 | 5 | 10 题覆盖分层与禁止绝对化 |
| 结构与表达 | 5 | 5 | 13 块齐全，下一章 18 |
| **合计** | **100** | **92** | |

DoD 20/20。备注：章内实战未写 `📖` 徽章（`practice/README.md` 有）。`practice/STATUS.md` 把 17-1 写成「Playwright 回归 Incomplete」，容易让人以为仓库缺一套 UI 套件；**正文没有这个暗示**。

### 第 18 章《性能测试基础》— 92/100

旧分 90 的理由是「未安装、未跑 JMeter」。这是诚实证据，不是知识错误。正文多次写：审查未装 GUI、骨架 1 用户 1 循环不是负载、教学毫秒数不是 MiniShop SLA、pytest/CI 绿不是性能结论。`.jmx` 存在且与步骤一致：`GET http://127.0.0.1:8765/api/products`，1 线程 1 循环，注释写明 Not an SLA。

| 项目 | 满分 | 得分 | 说明 |
| --- | ---: | ---: | --- |
| 技术准确性 | 25 | 24 | 百分位、并发≠TPS、负载/压力/耐久、授权纪律正确；练习 10 答案写成 `GET /products`，与同章 `.jmx` 的 `/api/products` 不一致 |
| 知识完整性 | 15 | 14 | 初级地图完整；不假装容量规划 |
| 初学者友好 | 15 | 14 | 五个样本算平均值/中位数/最大值已核：266.0 / 120 / 800 |
| 实战价值 | 15 | 13 | 交付是问题清单，类型 🚧，符合「未加压」 |
| 示例质量 | 10 | 9 | `.jmx` 可打开；上面的示例树仍是教学路径 `POST /login`（已标示例结构） |
| 项目一致性 | 5 | 4 | 骨架已走 `/api/products`，练习答案却回到 `/products` |
| 面试价值 | 5 | 5 | 含 GET/POST 安全神话干扰项 |
| 练习质量 | 5 | 4 | 第 10 题要求 MiniShop 目标草稿，答案路径应写成 v1.0 前缀或明确「教学路径」 |
| 结构与表达 | 5 | 5 | 下一章 19 |
| **合计** | **100** | **92** | |

DoD 19/20：第 10 项 MiniShop 一致未满。不阻断发布。

### 第 19 章《MiniShop 完整测试项目》— 93/100

核心冻结点在仓库里是真的：`/api/`、qty=10 允许 11 拒绝且不落库、订单 Body 无 `status`、37/1、BUG-001 开放、个人实践、Playwright 只在 `run.py evidence` 截图、`tests/` 里没有 UI 套件。本机复跑与 `evidence/pytest-output.txt` 摘要一致。

扣分不来自「没点 Postman GUI / 没加压」（那是应披露的剩余风险），而来自**正文数字过时**和覆盖叙述不完整。

| 项目 | 满分 | 得分 | 说明 |
| --- | ---: | ---: | --- |
| 技术准确性 | 25 | 24 | 规则、401/403、Cookie+Bearer 同时下发都对；「9 个请求」是错的事实数字 |
| 知识完整性 | 15 | 14 | 项目包文件都在；19.8 覆盖句未点出注册（11/38 条） |
| 初学者友好 | 15 | 14 | 能指着目录走；独立阅读要来回跳文件 |
| 实战价值 | 15 | 15 | 可启动、可测、有缺陷、有证据 |
| 示例质量 | 10 | 9 | HTTP/SQL/截图/pytest 对得上；章内截图列表跳过已存在的 `06-register.png` |
| 项目一致性 | 5 | 3 | Postman 9≠15；计划写「商品列表」P0，用例表无对应 TC |
| 面试价值 | 5 | 5 | 个人项目 / 无状态机 / 绿≠无缺陷 |
| 练习质量 | 5 | 5 | 含 37/1 与禁止公司名 |
| 结构与表达 | 5 | 4 | 目录表未列 `jmeter/`；实战类型徽章在 practice 目录不在章内 |
| **合计** | **100** | **93** | |

DoD 18/20：第 4 项（未过时）、第 10 项（MiniShop 一致）不通过。按标准属「修正后发布」。核心章 95 **未达到**。

---

## Issues

级别：高 = 冻结数字/契约与仓库不符；中 = 会误导执行或简历口径；低 = 表达/目录/徽章。

| ID | 章 | 级 | 问题 | 证据 | 建议（审查不改正文） |
| --- | ---: | --- | --- | --- | --- |
| S6-01 | 19 | **高** | 正文写 Postman「9 个请求」 | `chapters/19-minishop-project.md` 约 L214。集合 `item` 实测 **15**：注册合法/占用/非法、搜索、空搜索、登录 A/B/管理员、qty=1/10/11、下单、无凭证、越权他人、越权管理员。第 14 章 14.6.1 导入顺序已经按这 15 个写。环境文件 password/token 初始值确为空。 | 改成 15，或写「15 个请求（含…）」并与 14.6.1 对齐。 |
| S6-02 | 19 | 中 | 19.8 pytest 覆盖句对不上 38 条收集结果 | 收集 38 = 37 passed + 1 xfailed。覆盖句只提登录、商品、qty=1/10/11 与四态、未认证、下单、越权、管理员、纯函数。`test_register.py` 11 条、首页表单、qty=11 不落库未写。面试区「1、10、11、缺字段、null、空串、字符串、0」是对的。 | 用一张「收集数分解」或至少补「注册 11」。 |
| S6-03 | 19 | 中 | 计划 P0 含「商品列表」，用例表没有商品列表 TC | `docs/test-plan.md` P0 含商品列表。`test-cases.md` 无 TC-PRODUCT-*；pytest 有 `test_products_list` / `test_products_catalog_without_keyword`。超库存计划/用例均为 P0，**此项冻结已对齐**。 | 补 TC，或把计划里的「商品列表」改成「由 pytest 覆盖、用例表不单列」。 |
| S6-04 | 18 | 中 | 练习 10 答案路径不是 MiniShop v1.0 | 题干要 MiniShop 搜索/改数量目标。答案写 `GET /products`。同章 `.jmx` 与步骤是 `GET /api/products`。第 19 章才冻结 `/api/`，但骨架已经用 v1.0 路径。 | 答案改为 `/api/products`，或明确「若仍用第 13 章教学服务则 `/products`」。 |
| S6-05 | 17 | 低 | 面试「六种输入」 | 仓库购物车是 8 组 parametrize（ok/eq_stock/over_stock/missing/null/empty_str/wrong_type/zero）。 | 改成「八种」或「边界 + 四态」。 |
| S6-06 | 19 | 低 | 目录表未列 `jmeter/` | 第 18 章指向 `project/minishop/jmeter/minishop-get-products.jmx`，第 19 章 19.1 表无此行。 | 加一行「第 18 章骨架，未加压」。 |
| S6-07 | 17/18/19 | 低 | 章内实战未写类型徽章 | 质量标准要求写清 ✅/📖/🚧。徽章在 `practice/README.md`（17-1 📖、18-1 🚧、19-1 ✅）。 | 章内补一行类型。 |
| S6-08 | 仓库 | 低 | `practice/STATUS.md` 把 17-1 写成 Playwright 回归未完成 | 第 17 章实战是分层地图；Playwright 只在 `run.py evidence`。 | 改 STATUS，避免暗示「缺 UI 套件」。 |

未列为缺陷（抽查通过）：

- qty=10 允许、11 拒绝、不落库：`server.qty_allowed(10,10) is True`，`qty_allowed(11,10) is False`；`evidence/http/04` 200 / `05` 400 `qty exceeds stock`；SQL 第二节鼠标 qty=10 不是 11。
- 订单无 `status`：`evidence/http/06-order-create.txt` Body 仅 `id`；pytest 断言 `"status" not in body`；OpenAPI 写明 no status。
- 空搜索 BUG-001：空白 keyword 200 且三件商品；xfail `strict=True`；`bugs/BUG-001.md` 含「不在报告里写成已修复」（19-1 用这句判开放）。
- Playwright：`tests/` 只有 api/qty/register；截图来自 `run.py` 的 Chrome channel。
- 个人实践、无公司名、无「已测通支付/全部订单状态」：PRD、README、总结、简历证据、第 19 章常见错误均有。
- 阶段测验 6：37/1、无 status、个人项目、ROI 不能取消 Web 冒烟、未授权不加压；干扰项 B「22 passed 仍是仓库数字」已标过时。

### MiniShop 声明文件抽查

| 第 19 章指向 | 在不在 | 抽查 |
| --- | --- | --- |
| `docs/PRD.md` | 是 | R-CART-10、R-SEARCH、R-ORDER 无 status、`/api/` |
| `docs/requirement-review.md` | 是 | 状态机裁进非范围 |
| `docs/test-plan.md` / `test-cases.md` / `prd-coverage-matrix.md` | 是 | 超库存 P0；空搜索 P1 失败 |
| `docs/test-points.md` / `sql-check.md` / `test-report.md` | 是 | 报告 37/1；种子 JOIN 两行 |
| `docs/openapi.json` | 是 | OpenAPI 3.0.3，路径均 `/api/` |
| `postman/*.json` | 是 | v2.1，15 请求，密码空 |
| `tests/` + `evidence/pytest-output.txt` | 是 | 38 collected；摘要 37 passed, 1 xfailed |
| `bugs/BUG-001.md` | 是 | 开放 |
| `automation/` | 是 | 只指向 `tests/` |
| `jmeter/*.jmx` | 是（章 19 目录表未列） | 1 用户 1 循环 |
| `docs/project-summary.md` / `resume-evidence.md` | 是 | 个人项目；37/1 |

### 实操 19-1 是否真检查 37/1

是。`practice/19-project-pack/main.py` 在 MiniShop 目录执行 `python -m pytest -q`，用输出是否含 `37 passed` 且含 `1 xfailed`/`1 xfail` 决定退出码。本机复跑：文件检查全 OK，`passed_37` / `xfailed_1` / `bug_still_open` 均为 true。unittest 通过 `code == 0` 间接锁住 xfail，不只锁 37。不检查 Postman 个数，故 S6-01 不会被 19-1 拦住。

---

## 结构简化机会

1. **第 17 章**：金字塔、ROI、两种浏览器工具、报告、CI、初级边界已经够一张地图。Allure/Cypress「了解」可收成一句，把篇幅留给「接口绿了页面仍可能坏」的 MiniShop 对照。
2. **第 18 章**：18.7 步骤 4～7 与随后「两条纪律」重复讲 GUI 不适合加压。保留 `.jmx` 逐步打开 + 一条纪律即可。
3. **第 19 章**：19.1 目录表、19.8 覆盖句、覆盖矩阵三处都在数「测了什么」。用「38 collected 分解」一处说清，正文不再用散文枚举。目录表补 `jmeter/`，避免和第 18 章各说各的。
4. **阶段测验 6**：已能卡住冻结点，不必加题；若改 Postman 个数，测验不必跟 9/15，避免再写死一个易过时的请求数。

---

## 可接受风险

- 作者未点 Postman GUI / Collection Runner；集合 JSON 与 `pm.test` 在仓库里。第 14、19 章已披露。
- 未安装、未跑 JMeter GUI；`.jmx` 不是压测报告。第 18 章已披露。不要用这个把第 18 章按到 90。
- Playwright 只取证，不是回归套件。页面逐控件未用无头套件点完。
- 默认 `MINISHOP_RESET=1`，不适合当长期共享环境。
- 第 13～18 章教学服务仍是 `/login` 且常只让 qty=1（已标明）；第 19 章才冻结。
- 第 17、18 章实战是书面产出，仓库没有学习者填好的 `exercises/chapter-17-*.md` / `chapter-18-*.md`。
- 本机复跑时 MiniShop 目录没有 `.venv`，系统 Python 3.14.3 + pytest 9.1.1 仍能跑通；教材要求 `run.py setup` 仍然合理。

---

## 交接

1. **不要继承第 19 章旧分 96。** 本轮 93。要冲 95，先改 S6-01（Postman 9→15），并补 19.8 覆盖句 / 计划「商品列表」口径（S6-02、S6-03）。
2. **不要把第 18 章因「没跑 GUI」打回发布线。** 本章没有假结论。优先改练习 10 路径（S6-04）。
3. 第 17 章可维持 92；低优先级改「六种输入」和 STATUS 17-1 措辞，防止读者以为缺 Playwright 套件。
4. pytest 基线以仓库 `evidence/pytest-output.txt` 与本机复跑为准：**37 passed, 1 xfailed**，xfail = BUG-001。19-1 能锁住这个数字。
5. 下一章（第 20 章）项目口述必须用 37/1、开放缺陷、无订单状态、个人实践；不要再引用审查初稿里的 22 passed。
6. 本文件只写审查。正文、PRD、集合、测试均未改。
