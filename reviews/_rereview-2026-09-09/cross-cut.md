# 横切一致性审计（会让学生按错尺子）

- 日期：2026-09-09
- 范围：正文 / 测验 / 实操 / MiniShop v1.0 / 入口文档
- 方法：grep + 抽读；已有 `reviews/full-course-audit-v1.2.md`、`reviews/v1.2.1-rescore.md` 当待核实主张
- 纪律：已标明的教学约定不打成 bug，除非练习/答案会让人抄进项目或对着跑着的 v1.0 打

## 总判

全书官方学习顺序和「下一章预告」**自洽**；可运行实操**一律打 v1.0 `/api/`**；`Test123456`、正文里的「99 分」、把 `22 passed` 写成当前基线，**已经不在教材里**。质量标准禁止的绝对化（GET/POST 安全神话、Cookie/Session/Token 三选一、P0 全球统一、没 Bug 等于没 Bug、测试必须等开发完成、接口 ROI 永远最高）检索结果都落在「错误 / 选择题干扰项 / 不要说」，**没有当成正说**。

会让学生按错尺子的，不是「忘了写免责声明」这种已经修过的面，而是 **两把尺子并排还要学生自己换**：

1. **第 5 章教学尺（密码 8～20、验证码、锁定/禁用、R-REG-01）vs 测验/PRD 尺（8～16、无短信、无状态机）**——同一周学、同一份作业。
2. **第 10 章已经在真 MiniShop 上看到 `POST /api/login`，第 13～16 章又把可运行示例换回 `/login` + `qty=1` 才成功**——实操 9-1/13-1/16-1 打 v1.0，章内工作实战却允许/鼓励打教学服务。
3. **入口三套话 + 拆章索引 12 行不挂练习**——不是知识错误，但学生会跑 `practice/run.py 2-1` 或在索引页宣布「这章没作业」。

`full-course-audit-v1.2.md` 里「预告与大纲一致」「禁止绝对化未当正说」抽查成立。该审计「概念复核把第 20 章改成 22 passed」是**过期主张**：现行第 20/21/19 章和测验 6 已是 37/1。`v1.2.1-rescore.md` 留下的双基线、第 5 章验证码教学，**标签在，抄进项目的口仍开着**。

## 横切 Issues（Severity + 出现文件:line 列表，不要只说「多处」）

### HIGH — 练习/答案/数字会让人抄进 MiniShop 或对错端口

| ID | 问题 | 文件:line |
| --- | --- | --- |
| H1 | 第 5 章第一张可抄用例卡：种子号写成「未注册」+ 验证码。抄进 v1.0 会 409，且项目无验证码。后文 5.17 才标明教学，但学生先抄这张卡。 | `chapters/05-test-case-design.md:105-107`（`13800138000` 未注册；验证码有效；密码 `Test1234`） |
| H2 | 第 5 章工作实战追踪表用 `R-REG-01` / `R-REG-05`（隐私政策）。PRD 只有 `R-REG` / `R-PHONE` / `R-PASS`，无隐私政策、无验证码。完成标准写了「不要冒充正式规则」，但示例 ID 就是正式规则长这样。 | `chapters/05-test-case-design.md:509-510`；对照 `project/minishop/docs/PRD.md:20-22` |
| H3 | 阶段测验 2 问「MiniShop 密码长度应测哪些边界」，答案是 **8 和 16 / 7 和 17**。第 5 章主讲边界表和示意图是 **8～20 / 7、8、20、21**。测验口径对（v1.0），正文主例子会让认真做 5.8 的人答错；反过来，把测验答案当「第 5 章教的」也会和 5.8 打架。5.17:422 有对照，但测验题干没写「跟 PRD 不是跟 5.8」。 | `chapters/quizzes/stage-2-analysis.md:7,20`；`chapters/05-test-case-design.md:214,228-238,422`；`chapters/assets/diagrams/ch05-boundary.html:23-35` |
| H4 | 练习 5 点名「为 **MiniShop** 登录」画正常/锁定/禁用。5.14:360 写了「教学用」，练习题和答案没有再说 v1.0 无锁定。PRD 无锁定/禁用。 | `chapters/05-test-case-design.md:562,575`；`project/minishop/docs/PRD.md` 无「锁定」「禁用」 |
| H5 | 08A 把验证码、锁定、下架、小计写进「一轮 **MiniShop** Web 功能测试」表，表内无教学标签。8.10:274 才说注册需求是草案；练习 10:398 才说 v1.0 没有小计。先读表的人会按这些测首页。 | `chapters/08a-web-page-testing.md:35-43` |
| H6 | 第 19 章把 Postman 集合写成「**9 个请求**」。集合 JSON 有 **15** 个 `item`（3 注册 + 2 搜索 + 3 登录 + 3 改数量 + 4 订单/越权）。面试口述「集合 9 个请求」会对不上仓库。第 14 章 14.6.1 逐步操作已经按 15 个名字列顺序，两章数字不一致。 | `chapters/19-minishop-project.md:214`；`project/minishop/postman/MiniShop.postman_collection.json:8-237`；`chapters/14-postman.md:281` |
| H7 | 双基线会打到正在跑的 8765：第 10 章已写死「v1.0 登录路径是 `/api/login`，不是 `/login`」；第 13 章工作实战仍「对教学服务或授权测试环境」+「可用本章 OpenAPI 片段」（`paths./login`）；第 16 章可运行教学服务 `POST /login` 且 **只有 `qty=1` 成功**。把章内 curl 打到 `python3 run.py serve` → 404；把 `qty=10` 期望套到教学服务 → 400。实操 13-1/16-1 打的是 v1.0，和章内作业不是同一把尺子。 | `chapters/10-chrome-devtools.md:48`；`chapters/13-api-testing.md:15,183,405-417,635-640`；`chapters/16a-pytest-basics.md:190-205`；`chapters/16b-pytest-fixtures.md:265-284`；对照 `project/minishop/server.py:248`（只认 `/api/login`） |
| H8 | README 学习顺序表给 2-1/3-1/7-1/10-1/14-1/17-1/18-1/20-1/21-1/22-1 都挂了编号，`practice/run.py` 只认识 1-1/5-1/8-1/9-1/11-1/12-1/13-1/15-1/16-1/19-1（书面另加 4-1/6-1）。学生照表跑 `python3 practice/run.py 2-1` 得到「没有编号」。 | `README.md:48-68`；`practice/run.py:21-37,70-72`；`practice/README.md:61-82` 有完整表，但根 README 捷径不指向章内工作实战 |

### MEDIUM — 标签在别处，当前句仍会换尺

| ID | 问题 | 文件:line |
| --- | --- | --- |
| M1 | 04A 练习 3 把「PRD：密码 8～20 位」当矛盾题材料。04A 开头免责清单有验证码/优惠券/支付/订单状态，**没有密码长度**。04B:23 才对比草案 8～20 vs v1.0 8～16。先做 04A 练习的人会以为 MiniShop PRD 是 8～20。 | `chapters/04a-requirements-static-testing.md:12,465-466,488-490`；`chapters/04b-minishop-requirement-review.md:23-42` |
| M2 | 第 9 章「MiniShop 服务端」序列图正下方，登录路径例子是 `/login`，此处无教学标签。9.13:466 才说教学示例；练习 10 答案:746 才补「教学示例」。实操 9-1 断言路径必须是 `/api/login`。 | `chapters/09-computer-network-and-http.md:248-257,746`；`practice/09-http-observe/tests/test_lab.py:19` |
| M3 | 第 9 章插图 alt 与 HTML 把 **8765 叫「教学服务」又叫「MiniShop v1.0」**。第 11/13/14 章教学占位是 `PORT`/`8080` + `/login`。同一词「教学服务」两套端口。 | `chapters/09-computer-network-and-http.md:107`；`chapters/assets/diagrams/ch09-ip-port.html:28,43`；`chapters/11-linux.md:435-441`；`chapters/14-postman.md:119` |
| M4 | 第 14 章 14.6.1 导入 v1.0 集合（`/api/`、8765、`Test1234`），紧接着 14.7「MiniShop 教学全流程」又建 `POST /login`、`GET /products`、qty=1。同章两套 Collection。14.6.1:285 有「不要混」一句，14.7 表头仍叫 MiniShop。 | `chapters/14-postman.md:273-285,295-307` |
| M5 | 第 18 章示例结构是 `POST /login` + `POST /cart/items`；仓库 `.jmx` 是 `GET /api/products`、端口 8765、1 用户 1 循环。学生若「按正文搭」会对着 v1.0 打不存在的 `/login`。正文标了示例结构，但没写「和仓库 jmx 不是同一份」。 | `chapters/18-performance-testing.md:214-224`；`project/minishop/jmeter/minishop-get-products.jmx:4-27` |
| M6 | 教学服务密码是字面量 `<redacted>`；v1.0 是 `Test1234`。第 11 章 curl 示例把 `<redacted>` 放进 JSON。对着 8765 重放 = 401，学生会以为登录坏了。11:435 有对照句，示例本身仍是错密码形状。 | `chapters/16a-pytest-basics.md:205`；`chapters/11-linux.md:435-441`；`README.md:36` |
| M7 | 拆章索引 12 行：只分流 A/B + 一句「读完第二节后进入第 N 章」，**不链实操、不链工作实战**。练习入口在 B（或 06A）。从 README 点「读」进索引的人会以为这章没有作业。 | `chapters/04-requirements-analysis-and-static-testing.md:1-12`；`chapters/06-bug-and-test-management.md:1-12`；`chapters/08-web-functional-testing.md:1-12`；`chapters/12-database-and-sql.md:1-12`；`chapters/15-python-basics.md:1-12`；`chapters/16-pytest.md:1-12`。实操实际在：`04b:151`、`06a:402`、`08b:256`、`12b:189`、`15b:307`、`16b:210` |
| M8 | 起步实操三套名单不一致（作者主控 vs 学习者学习建议 vs 根 README「当天」）。 | `docs/COURSE_CONTROL.md:17`（1-1/5-1/9-1/12-1/16-1）；`docs/LEARNING.md:70-78`（1-1/5-1/8-1/9-1/13-1，另列 11-1/12-1/15-1/16-1/19-1）；`README.md:19`（只推 1-1） |
| M9 | `STATUS.md` 把 17-1 同时标成 Incomplete（Playwright 回归）和 Reader exercise（画分层）。10-1/14-1 也在 Incomplete 表又出现在「其余书面」括号里。学生不知道交分层图还是交 Playwright。 | `practice/STATUS.md:33-39` |
| M10 | 集合 `info.name` 为 `MiniShop v1.0 Teaching`。v1.0 契约 + Teaching 一词，和第 13～16 章「教学服务」撞名。 | `project/minishop/postman/MiniShop.postman_collection.json:3` |
| M11 | 15A 正文「下一章用 pytest 调这些函数」——正式预告是 15B。会跳过文件/JSON。 | `chapters/15a-python-syntax.md:44` vs `:707-709` |

### LOW / 已核实不是现行教材 bug

| 项 | 结论 |
| --- | --- |
| `Test123456` | 仅 `reviews/full-course-audit-v1.2.md:31` 历史记录。正文现为 `Test1234`（`chapters/01-software-testing-intro.md:38` 等）。 |
| 正文「99 分」 | `chapters/` 无匹配。只在 reviews / README 作者工作台「取消 99 分」。 |
| `22 passed` 当现行基线 | 正文已是 37/1。残留：`chapters/quizzes/stage-6-project.md:14` 作为**错误选项 B**；`project/minishop/docs/test-report.md:21` 写明是 2026-09-08 历史。审计 `full-course-audit-v1.2.md:88`「第 20 章改为 22 passed」**已过期**。 |
| `13800138002` | 仅 12A 教学库用户 3，且 `chapters/12a-sql-query.md:125,382` 写明不是管理员 `…099`。v1.0 种子是 00/01/99（`server.py:91-93`）。 |
| 第 1/3/5/6 章优惠券、支付、待支付 | 抽查均有「不是 v1.0 / 教学示例」标签（如 `01:129,348`、`03:104,113`、`05:249 起及 332-349`、`06a:31,164`）。**不打 bug**。会抄进项目的是上面 H1–H5 那种**没贴在当场**的。 |
| 禁止绝对化当正说 | 未发现。均在「错误 N」或测验干扰项。 |
| 图表断链 | 正文 `assets/diagrams/*.png` 引用 82 个，缺失 0。 |
| 可运行实操是否打 v1.0 | 是。`practice/_minishop.py:13-32` import `project/minishop/server.py`；登录路径全是 `/api/login`（05/08/09/11/12/13 的 `main.py`）。16-1/19-1 直接跑仓库 pytest。 |

## 数字与路径对照表

| 尺子 | 现行 v1.0 / 仓库 | 仍会出现的另一把尺 | 学生若抄错 |
| --- | --- | --- | --- |
| pytest | `37 passed, 1 xfailed`（`evidence/pytest-output.txt:4`；函数+parametrize=38 条=37+1 xfail） | 历史 22 passed（test-report:21；旧审计；测验 6 错误项 B） | 面试报 22；或把 xfail 说成全绿 |
| 密码 | `Test1234`，8～16 且字母+数字（PRD `R-PASS`；`README.md:36`） | 教学 8～20（05:229）；教学服务密码字面量 `<redacted>`（16a:205）；已删除的 `Test123456` 只在旧审计 | 测 20 位当合法；或用 `<redacted>` 打 8765 |
| 登录 API | `POST /api/login`（`server.py:248`；OpenAPI:9；前端 `app.js` fetch `/api/login`） | 教学 `POST /login`（09:257；13:339；14:91,155；16a:194；16b:265；18:217） | 对 serve 打 `/login` → 404 |
| 登录页 | `GET /`（PRD:38；17:146 已改，无 `/login` 路由） | 无现行正文再 `goto /login`（审计主张「已改」成立） | — |
| 购物车成功 | `qty=10` 允许、`qty=11` 拒绝（PRD `R-CART-10`；pytest `test_cart_qty_cases` ids `eq_stock`/`over_stock`；实操 5-1） | 教学服务仅 `qty=1` 成功（13:259；16a:197-203；16b:279-284） | 把 qty=10 写成 v1.0 失败，或反过来 |
| 订单 | 201 + `id`，无 `status`；不幂等 | 第 5 章场景表支付/优惠券行（已标明）；待支付只作为「不要写」 | 简历写状态机 |
| 账号 | `13800138000` / `…001` / 管理员 `…099` | 12A 教学库 `…002` + NULL（已标明） | JOIN 对答案对不上 evidence |
| Postman | 15 个请求，路径全 `/api/`，含 qty=1/10/11、注册、越权 | 第 19 章写「9 个」；第 14 章 14.7 另有 7 步教学 `/login` | 口述条数错；混跑两套集合 |
| OpenAPI vs server | 前缀 `/api/`；login/register/products/cart/cart/items/orders/orders/{id}/admin/* 对齐。页面 `/`、`/admin.html` 不进 OpenAPI（合理） | 第 13 章教学 OpenAPI `paths./login` | 对照错文档 |

## 下一章预告偏差表

正式学习顺序：`01 → 02 → 03 → 07 → 04 → 05 → 06 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20 → 21 → 22`。

| 文件 | 「下一章预告」指向 | 是否符合顺序 | 拆章是否跳过下册 |
| --- | --- | --- | --- |
| `01:497` | 研发流程（第 2 章） | 是 | — |
| `02:434` | 分类地图（第 3 章） | 是 | — |
| `03:468` | 第 7 章 Web | 是（故意不按文件名 04） | — |
| `07:640` | 第 4 章，先读 04A | 是 | 不跳 04B（点名 04A） |
| `04a:528` | 04B | 是 | 否 |
| `04b:308` | 第 5 章 | 是 | — |
| `04` 索引:12 | 读完第二节后第 5 章 | 是 | 索引本身不链 04B 练习 |
| `05:625` | 06A | 是 | 否 |
| `06a:574` | 06B | 是 | 否 |
| `06b:338` | 08A | 是（07 已读过） | — |
| `08a:423` | 08B | 是 | 否 |
| `08b:420` | 第 9 章 | 是 | — |
| `09:804` | 第 10 章 | 是 | — |
| `10:687` | 第 11 章 | 是 | — |
| `11:731` | 12A | 是 | 否 |
| `12a:467` | 12B | 是 | 否 |
| `12b:353` | 第 13 章 | 是 | — |
| `13:652` | 第 14 章 | 是 | — |
| `14:564` | 15A | 是 | 否 |
| `15a:707` | 15B | 是 | 否（但 15a:44 非正式「下一章 pytest」会跳 15B） |
| `15b:582` | 16A | 是 | — |
| `16a:354` | 16B | 是 | 否 |
| `16b:636` | 第 17 章 | 是 | — |
| `17:524` | 第 18 章 | 是 | — |
| `18:504` | 第 19 章 | 是 | — |
| `19:490` | 第 20 章 | 是 | — |
| `20:545` | 第 21 章 | 是 | — |
| `21:411` | 第 22 章 | 是 | — |
| `22:396` | 没有第 23 章 | 是 | — |

**结论：** 审计「预告与大纲一致」对 **`## 下一章预告` 成立**。拆章上册**没有**预告到下一整章而跳过下册。唯一非正式跳章句：15A:44。

## 实操/测验/图表断链

### 实操 22 项 vs 目录 vs run.py

| 编号 | practice/ 目录 | run.py | 类型（practice/README） |
| --- | --- | --- | --- |
| 1-1, 5-1, 8-1, 9-1, 11-1, 12-1, 13-1, 15-1, 16-1, 19-1 | 有 | 有 | ✅ 可运行；脚本打 v1.0 |
| 4-1, 6-1 | 有（模板） | 有（打印书面说明，exit 0） | 📖 |
| 2-1, 3-1, 7-1, 10-1, 14-1, 17-1, 18-1, 20-1, 21-1, 22-1 | **无目录** | **无编号** | 📖/🚧，入口在对应章「工作实战」 |

不是「声称 22 个文件夹」——`practice/README.md:55-82` 写清了。断链发生在 **根 README 实操列** 把书面项链到 `practice/README.md` 而不是章内锚点，且 `run.py` 对书面编号除 4-1/6-1 外直接失败（H8）。

### 测验 vs 正文（必过题抽查）

| 测验 | 必过 | 与正文 |
| --- | --- | --- |
| 阶段 1 Q4 V 模型 | 系统需求↔系统测试；系统设计↔集成测试 | 与审计已回写的第 2 章一致 |
| 阶段 1 Q1/Q9 | 没发现 ≠ 没 Bug；C 正确 | 与第 1/2 章禁止绝对化一致 |
| 阶段 2 Q2 购物车可测性 | 已登录、正整数、≤库存、失败保持原值 | 与 PRD `R-CART` 一致 |
| 阶段 2 Q3 密码边界 | **8/16** | **与 5.8 教学尺 8/20 冲突（H3）** |
| 阶段 2 Q9 验证码/优惠券 | 不能进 v1.0，跟 PRD | 与 5.17 标签一致；但 H1 示例卡仍会让人抄 |
| 阶段 3 Q1/Q4 Cookie 分层、GET/POST | 禁止三选一、禁止安全神话 | 与 08B/09 错误节一致 |
| 阶段 3 Q9 登录两类凭证 | token + Set-Cookie | 与 PRD `R-AUTH`、第 10 章一致 |
| 阶段 4 Q7 JOIN 种子 | 鼠标 qty 1 / 键盘 qty 2 | 与 `evidence/sql/seed-join.txt` 第一节一致 |
| 阶段 4 Q8 SQLite 无 TRUNCATE | 是 | 与 12B 一致 |
| 阶段 5 Q3 `/login` vs `/api/login` | 测 v1.0 跟 PRD/OpenAPI | 测验正确；章内作业仍可走教学服务（H7） |
| 阶段 5 Q4 变量覆盖 | Environment 覆盖 Collection | 与 14:143 一致（审计已改） |
| 阶段 6 Q6/Q10 pytest 数字 | 37/1；B「22 passed 仍是仓库数字」为错 | 与现行仓库一致 |
| 阶段 6 Q5 qty=10/11 | v1.0 允许/拒绝；教学服务常只让 qty=1 | 明确教换尺，与 H7 同源 |
| 阶段 7 Q1 五段口述 | 结论→原理→场景→示例→边界 | 与第 20 章一致 |
| 阶段 7 Q9 | D 测试不能证明无缺陷 | 禁止绝对化未当正说 |

### 图表

正文引用的 `chapters/assets/diagrams/*.png` **全部存在**（82/82）。第 7 章组合页 `assets/07-html-combo.html` 在仓库（审计「组合页不在仓库」已过期）。

内容尺风险（不是断链）：`ch05-boundary` 主视觉是 8～20，caption 末行才写 v1.0 为 8～16（`ch05-boundary.html:35`）。`ch09-ip-port` 8765 门牌同时写「v1.0」和「教学服务」（M3）。

### MiniShop 代码抽查（不必读完）

| 层 | 抽查结果 |
| --- | --- |
| server 路由 | `/api/login|register|products|cart|cart/items|orders` + `/api/orders/{id}` + `/api/admin/products|orders` + 页面 `/` `/admin.html`。无 `/login`。 |
| OpenAPI | 上述 JSON API 均在；订单 409 stock changed 与 `server.py:461` 一致。 |
| pytest | 37 passed + 1 xfail（BUG-001 空关键字）。qty=1/10/11、注册 201/409/400、越权 403、订单无 status：与 PRD 对齐。 |
| Postman | 请求全 `/api/`；有 qty=10；空搜索按 R-SEARCH 断言（当前应失败）。缺 GET `/api/cart`、admin 列表——不是错误，但第 19 章「9 个请求」计数错（H6）。 |
| 前端 | 登录在 `/`，API 走 `/api/login`。 |

## 结构简化建议

1. **消灭双基线，而不是再加标签。** 第 13～16 章可运行示例直接打 `project/minishop`（实操已经这么做了）。教学若需要「只有 qty=1 成功」来讲「期望跟被测系统走」，用**一段对照表**即可，不要再维护一套 `TeachHTTPServer` + `/login` + 密码 `<redacted>`。现在的标签学生看到了仍会对着 8765 粘 curl。
2. **第 5 章技术练习不要用 MiniShop 当壳。** 验证码/8～20/锁定/优惠券改称「通用练习系统」，MiniShop 名字只留给 PRD 已有规则。测验 2 Q3 与 5.8 才能同一把尺。
3. **拆章策略要么按长度，要么按练习节奏，不要两套。** 现行：09=806、11=733、13=654、05=627、10=691 **未拆**；15A=709、16B=638 **拆了**。09/11/13 比 15/16 更需要中场练习，却整章灌完。
4. **索引页不要只有 12 行。** 最低：链 A/B、链 `practice/`、链阶段测验、一句话「本章作业在第 N 节」。否则 README「读」列把人扔到空分流页。
5. **三套入口收成一套。** 根 README 实操列：有脚本的链目录，书面的链章内「工作实战」锚点，不要统一链 `practice/README.md`。`COURSE_CONTROL` 的起步名单与 `LEARNING.md` 对齐，或主控注明「作者备忘，以 LEARNING 为准」。
6. **STATUS 每个编号只允许一种状态。** 17-1 选 Reader exercise（分层图）或 Incomplete（Playwright），不要两行都写。

## 给主审查员的交接（哪些章最危险）

优先深读（按「抄进项目 / 打错端口」概率）：

1. **第 5 章** — H1–H4 + 测验 2 密码尺。技术章节里 MiniShop 名字用得最满，PRD 重合度最低。
2. **第 13～16 章（含 16A/16B）** — H7 双基线。实操已经 v1.0，正文教学服务仍是另一份契约；第 16 章同时出现 37/1 和 qty=1-only。
3. **第 8 章上（08A）** — H5。MiniShop 检查表含验证码/下架/小计，免责在后文。
4. **第 14 + 19 章** — H6 集合条数；14.6.1 与 14.7 两套路径。面试数字从这里抄。
5. **第 9 章** — M2/M3。序列图表 `/login`，插图 8765 叫教学服务；实操 9-1 却断言 `/api/login`。

相对安全（本轮横切未发现会抄进项目的硬冲突）：1–3、7、11（curl 有对照句）、12A/12B（`…002` 已标明）、17（`goto /` 已改）、20–22（37/1、无状态机）、阶段测验 1/3/4/6/7。

不必再核：`Test123456`、正文 99 分、图表文件是否存在、官方「下一章预告」是否跳 07→04、可运行实操是否误打 `/login`（没有）。

作者主控 `docs/COURSE_CONTROL.md:15-16` 把全文审计和 37/1 复评写成已完成。本次横切说明：**数字基线和预告顺序已稳，换尺口还在第 5、8A、13–16、19 章计数。**
