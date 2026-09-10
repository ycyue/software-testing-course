# MASTER_AUDIT

- 教程：《软件测试从零基础到初级软件测试工程师》v1.2.2
- 总控：Audit Coordinator
- 日期：2026-09-10
- 方法：22 个 Chapter Agent 并行 + 8 个 Global Agent（Global-02 技术 Red Team 为额度中断后重跑）
- 产物目录：`reviews/_full-audit-2026-09-10/`
- 教材正文：**未改**

本文件不是 22 份报告的拼接。总控已：合并重复 ISSUE、保留不同 Agent 的证据、按权威来源与仓库实装重新评级、裁决分歧。

---

## 0. 一句话结论

方法脊柱（测试 = 观察 + 判定 + 证据）和 MiniShop 可运行主线是真的：practice 1-1…19-1 能绿，pytest **37 passed / 1 xfailed**，BUG-001 仍开放，订单无 `status`，质量标准禁止的六条绝对化没有写成正说。挡发布的不是「理论写反」，而是 **开篇用真种子账号演假登录缺陷**、多处 **可抄 MiniShop oracle 与 `server.py` 不一致**、以及 **完课验收验不到 Postman/DevTools/Git 协作**。

全书质量等级：**C**（可以学习，需要较多修订）。不是 D：没有把 ISTQB / RFC / ISO 25010:2023 主课教反，项目不是空壳。不是 B：核心章（5/8/12/13/14）多条 P1，就业闸门未装。

---

## 1. 覆盖（总控核对）

| 项 | 总数 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 教材章节 | 22 | 22 | 0 |
| 章节 Markdown（含上下册） | 36 | 36 | 0 |
| 示意图 PNG + HTML | 85+85 | 全部打开 | 0 |
| 运行截图 PNG | 9（assets=evidence 哈希相同） | 9 | 0 |
| 章节代码围栏 | 252 | 252（G03 compile/实跑） | 0 |
| 章节表格块 | 163 | 163（各章 Coverage） | 0 |
| 章内小练习 + 答案 | 213+213 | 独立作答 | 0 |
| 阶段测验 | 70 | 独立作答 | 0 |
| 可运行 practice | 10 | 全绿（G03） | 0 |
| MiniShop pytest | 38 collected | 37 passed, 1 xfailed | 0 |

各章 Agent 均宣称 Coverage 100%。总控抽核：每份 `CHAPTER_XX_AUDIT.md` 均有 Coverage 表、ISSUE 块、图片节、练习独立作答记录。未发现空报告。

---

## 2. 各章分数与结论（章 Agent，总控不改分数、只改跨章等级）

| 章 | 分 | 结论 | 总控备注 |
| --: | --: | --- | --- |
| 1 | 76 | C | 开篇登录场景升 **P0**（见分歧 D1） |
| 2 | 76 | C | 无 P1；Git 只到本地 commit |
| 3 | 78 | C | 冒烟答案「加入购物车」P1；3.8 空格提示漏报，总控补 P1 |
| 4 | 78 | C | 作业三套规格 |
| 5 | 71 | C | 核心章；判定表图文错位、状态机过星 |
| 6 | 79 | C | 练习 10 答案对象错 |
| 7 | 81 | C | example.test 写成 MiniShop 网址 |
| 8 | 73 | C | Cookie 回退、`GET /api/orders` 404 |
| 9 | 78 | **B** | 主课 RFC 对齐；图 `keyword=mouse` |
| 10 | 73 | C | Timing 文案、Preserve log 对象 |
| 11 | 81 | **B** | `keyword=mouse` 可复制空列表 |
| 12 | 73 | C | 主键图、种子图、INSERT 无事务 |
| 13 | 73 | C | 四态图缺 sku；报文缺 Content-Length |
| 14 | 66 | C | 核心章最低分；Cookie jar + 变量名 |
| 15 | 76 | C | 35 个 Python 块可跑；venv 图冲突 |
| 16 | 79 | **B** | 无 P1；37/1 复现 |
| 17 | 80 | C | `getByRole` 非 Python API |
| 18 | 82 | C | 章分最高；P95 图注串台 |
| 19 | 81 | **B** | 仓库真；权限正例、空搜索图弱 |
| 20 | 72 | C | 可背范文 |
| 21 | 67 | C | 简历可抄、未禁「独立开发教材」 |
| 22 | 74 | C | 分层命名打架；自检空表 |

算术均分 **76/100**。核心章（5、8、12、13、14、16、19）均分 **74**。作者发布线 90 全面未到。

---

## 3. 总控 P0（合并后）

会把学生教错**冻结项目的既成事实**，或安全风险。

### MASTER-P0-001（采纳 G01-0001，升级 CH01-0002）

- 文件：`chapters/01-software-testing-intro.md` L39–42
- 原文：用 `13800138000` / `Test1234`（写明与第 19 章项目数据相同）登录失败，并宣布发现缺陷
- 总控核验：`project/minishop/tests/test_api.py` `test_login_ok`、PRD 教学数据、第 10/13 章逐步操作均为这组账号 **200 + token**。全书开放缺陷是 BUG-001（空搜索），不是登录。
- 为什么是 P0 不是 P1：这是第一课场景，凭证是冻结种子，学生按「与第 19 章相同」去跑会看见成功。会把公式例子、BUG-001、实操 1-1 的对象搅乱。修改成本低（改错误密码或标明假设）。
- 建议：改用错误密码，或写「这不是仓库现状」；仓库里仍开放的缺陷钉在空搜索。

### 未升为 P0 的高危图（见分歧 D8）

`ch13-four-shapes` 缺 `sku`、oracle 与 `server.py` `_cart_items` 不符。总控维持 **P1 + 必须 REPLACE**，不升 P0：同节 13.8 表每行有 sku，实操 13-1 与实现一致。图会误导，但官方表与练习不是假 oracle。

---

## 4. 总控 P1 总表（去重后，保留多 Agent 证据）

同一事实只留一条 MASTER 号；证据列列出所有来源。

| ID | 主题 | 证据 | 建议 |
| --- | --- | --- | --- |
| M-P1-01 | 开篇假登录缺陷 | CH01-0002, G01-0001 | **已升 P0** |
| M-P1-02 | 冒烟/答案「加入购物车」 | CH03-0001, G04-0001, G07-0011 | 改为更新数量/创建订单 |
| M-P1-03 | 3.8 空格「异常提示」vs BUG-001 | G01-0005（章 3 漏报） | 改成返回全量或标明非 v1.0 |
| M-P1-04 | 第 4 章作业三套规格 + 模板缺列 + 矩阵「不落库」 | CH04-0001/0002/0003 | 统一一份 template |
| M-P1-05 | 判定表图文不是同一业务；场景表混支付；状态机 ⭐⭐⭐ | CH05-0001–0004 | 注册表进正文；通用系统降星 |
| M-P1-06 | 06B 练习 10 把 6-1 答成 qty=11 | CH06-0001, G04-0002, G01-0003 | 按 BUG-001 重写确认/回归 |
| M-P1-07 | 正式 test-plan 出口混三套 P0 | CH06-0002 | 出口只写用例优先级 + S1/S2 |
| M-P1-08 | 第 7 章把 example.test 写成 MiniShop 网址 | CH07-0001, G07-0013 | 教学 URL 标明非仓库 |
| M-P1-09 | 不带 Bearer ≠ 401（Cookie 回退） | CH08-0001, G03 E39–E40 | 写清 Bearer **或** Cookie |
| M-P1-10 | `GET /api/orders` 无 id → 404，表写成 401 | CH08-0002；`server.py` L232–242 总控复核 | 删集合 GET 或改 404 |
| M-P1-11 | 空搜索截图 ≈ 商品目录 | CH08-0003, G05, G06, G19 | 换带 `keyword=` 的 Network/URL 证据 |
| M-P1-12 | 练习 10「数量保持合法值」vs 输入框仍 11 | CH08-0004, G01-0004 | 预期改为列表 qty=1、输入框可仍为 11 |
| M-P1-13 | `keyword=mouse` 打 `/api/products` → 空列表 | CH09-0001, CH11-0001, G03-0002, G05 | 改无 query 或 `keyword=鼠标` |
| M-P1-14 | Preserve log / Timing 文案 / localhost 限速 | CH10-0001–0004 | 对齐 Chrome 152；登录是 hidden 切换 |
| M-P1-15 | ch12 种子图、sku 当主键、12A 无 sqlite 第一帧、INSERT 无事务 | CH12-0001–0004, G03-0009, G05 REPLACE | 重画两图；INSERT 包事务 |
| M-P1-16 | 四态图缺 sku → 全是 `missing sku` | CH13-0001, G05-0001, G03 E43；总控读 `server.py` L366–368 | 按 13.8 表改 JSON 后重截 |
| M-P1-17 | 纸面 HTTP 无 Content-Length；实装 HTTP/1.0 | CH13, G03-0003 | 补长度或标明 curl 会加 |
| M-P1-18 | Postman 无凭证 + cookie jar → 下单 201 | CH14-0001, G03-0001, G06 | `disableCookies: true` |
| M-P1-19 | 正文 `orderId` vs 集合 `lastOrderId` → 越权打成 404 | CH14-0002, G01-0010, G03-0004 | 全文统一 `lastOrderId` |
| M-P1-20 | 先手建再导入；不存在的第 6 步；只断言数组 | CH14-0003–0005 | 14.2 改导入；删第 6 步 |
| M-P1-21 | venv 图让本章立刻 `pip install -r` | CH15-0001, G05 | 图只留 venv + pip list |
| M-P1-22 | Playwright 表 `getByRole`（Python 不存在） | CH17-0004, G03 E60 | 改 `get_by_role` |
| M-P1-23 | P95 图注串成并发≠TPS；无 P95 算例 | CH18-0001/0002, G05 | 换 caption；补 5 样本 P95 |
| M-P1-24 | 收口层「教学服务 qty=1」幽灵基线 | G01-0002, CH19 现在时 | 19/20/22/测验 6 改过去时 |
| M-P1-25 | 面试可背范文 + 测验 Q8 结构互斥 | CH20-0001–0004, G04-0004, G08-0002 | 删满分段；测验改回五段 |
| M-P1-26 | 简历档口三套、主作业可抄、未禁「独立开发教材」 | CH21-0001–0003, G08-0001/0013 | 强制仓库路径；禁自研措辞 |
| M-P1-27 | 必须/高频/了解 vs 三梯队 vs 星级 | CH22-0001/0002, G01-0007 | 一张对照表 |
| M-P1-28 | 结课自检空表可抄 37 passed | CH22-0003 | 写启动命令与禁止抄数字 |
| M-P1-29 | README/LEARNING 书面编号 `2-1` 与 `run.py` 不同构 | G01-0008, G07-0003；总控读 `practice/run.py` PRACTICE_DIRS 无 2-1 | 表上标 📖 或脚本提示书面 |
| M-P1-30 | 08A 仍把验证码列入 MiniShop 优先检查 | G01-0009 | 删或标明仅草案 |
| M-P1-31 | 第 18 章 `python3 run.py serve` 无工作目录 | G01-0011 | `cd project/minishop` |
| M-P1-32 | MiniShop 权限正例（所属者 200）缺 pytest | G06-0001 | 加一条所属者 GET 200 |
| M-P1-33 | 21.3 默认「能使用 Postman/DevTools」但 STATUS Incomplete | G08-0003（升 CH21 P2） | 有学生 GUI 产物才能写「能使用」 |
| M-P1-34 | Git 无 branch/PR；缺陷工具无点击 | G08-0004/0005 | 一页 fork+PR；可选免费云工单 |

P2/P3 原文见各 `CHAPTER_XX_AUDIT.md` 与 `GLOBAL_0X_*.md`。合并后不再把「图留白」「星级微调」抬进总表。

---

## 5. 【Agent Disagreement】总控裁决

### D1 第 1 章种子登录失败：P1 vs P0

- Chapter-01：P1
- Global-01：P0
- 总控核验：原文 L39–42 确实绑定种子账号；`_login` 这组凭证成功。
- **裁决：P0（MASTER-P0-001）。** 理由：冻结契约 + 第一课场景。改法一行。

### D2 第 3 章 3.8 空格异常提示

- Chapter-03：未报
- Global-01：P1
- 总控核验：`03-software-testing-classification.md` L238 原文「连续空格会出现异常提示」。实现是空/空白关键字返回全量（BUG-001），不是异常提示。
- **裁决：P1，记章 3 漏报（M-P1-03）。**

### D3 `ch13-four-shapes`：P1 vs P0

- Chapter-13：REPLACE，P1
- Global-05：P0
- 总控核验：`server.py` L366–368 `"sku" not in data` → `missing sku`。图 2–4 格无 sku。13.8 表有 sku。13-1 与表一致。
- **裁决：维持 P1 + 发布前必须 REPLACE。** 不升 P0，因为同节官方表与可运行实操 oracle 正确；图是局部错误插图，不是唯一判定来源。

### D4 第 14 章练习 8 `orderId` 是否答案错误

- Chapter-14：CH14-0002 含答案口径
- Global-04：练习 8 问断言策略，变量名差异不是答错
- **裁决：资产不一致 = P1（M-P1-19）。练习 8 不标 ANSWER VERIFICATION FAILED。** 改变量名同时关掉正文与集合。

### D5 `ch02-vmodel` REPLACE vs MODIFY

- Chapter-02：倾向重画 V
- Global-05：配对表正确，alt 已声明不是字母 V
- **裁决：MODIFY，不强制画 V。** ISTQB 要的是成对关系，不是字形。

### D6 第 19 章权限正例：P2 vs P1

- Chapter-19：P2
- Global-06：项目签章 P1（R-PERM 只有 403、无所属者 200 用例）
- 总控核验：实现有所属者 200；pytest 未断言。
- **裁决：项目包 P1（M-P1-32）；第 19 章正文保持 P2。** 对象不同。

### D7 第 22 章有无就业承诺

- Chapter-22：无「学完即可就业」
- Global-08：大纲「零基础 → 初级工程师」是隐性承诺
- **裁决：不记 P0/P1 虚假承诺。** 记 P2 定位：把「初级工程师」写成求职方向而非完课头衔；22.2 Postman 行与 STATUS 对齐。真正的 P1 是简历「能使用」与 Incomplete GUI（M-P1-33）。

### D8 第 21 章 Postman/年限：P2 vs 就业 P1

- Chapter-21：P2
- Global-08：升 P1
- **裁决：就业视角 P1（M-P1-33）。** 现场打不开 Postman 会挂，不是文笔问题。

### D9 CH15 `__future__` / CH18 JMeter assertions

- Global-03：`__future__` 不宜当代码缺陷；`.jmx` 无 `ResponseAssertion` 元件（saveConfig 仍有 `<assertions>`）
- **裁决：同意 G03。** 不把 `__future__` 写入总表；JMeter 记 P2「骨架无响应断言」。

### D11 SameSite / RFC 6750 / Throughput（Global-02 vs 章 Agent）

- Chapter-08：SameSite 段、RFC 6750 持有者语义判通过
- Global-02：未设置 ≠ 显式 Lax；6750 TLS MUST 未教；Throughput 定义句冲突
- **裁决：三条均为 P2，不升 P1。** 不挡 MiniShop 主路径；挡 CSRF/Bearer/JMeter 口试。CH08 分层与禁止三选一维持正确。

### D10 第 20 章五段 vs 培训班

- Chapter-20：P1 范文册
- Global-08：就业上再升「不可区分毕业生」
- **裁决：保持 P1（M-P1-25）。** 删可背满分段，加非 MiniShop 现场测。不因「像面试」再堆范文。

---

## 6. Phase 10 总控 Final Red Team（独立于 Global-02）

总控对下列高风险断言重新取证，不采信单一 Agent。

| 断言 | 核验 | 结论 |
| --- | --- | --- |
| ISO/IEC 25010:2023 九特性 | 对照 ISO 页面与 2023 修订说明：Safety 新增；Usability→Interaction Capability；Portability→Flexibility | 第 1 章名单 **正确** |
| GET safe / 幂等 | RFC 9110 §9.2；第 9 章禁止「GET 不安全 POST 安全」 | **正确** |
| Cookie 回退 | `server.py` `_token` L190–199：先 Bearer 再 Cookie | **属实**；「不带 Bearer=401」为假 |
| 购物车 sku 先于 qty | `_cart_items` L366–382 | **属实** |
| `GET /api/orders` 集合 | do_GET 无无 id 列表路由；尾斜杠被排除 | **404 属实** |
| `practice/run.py 2-1` | `PRACTICE_DIRS` 无 2-1；书面只 4-1/6-1 | **「没有编号」属实** |
| pytest 37/1 | G03 E15；多章复跑 | **属实** |
| 种子登录成功 | PRD + test_login_ok | **属实**；第 1 章场景为假 |
| Playwright Python API | G03 E60 | `getByRole` **不存在** |
| 质量标准六条绝对化写成正说 | 22 章 + G03/G04 | **未发现正说** |

### Global-02 落地（重跑完成，无新 P0/P1）

`GLOBAL_02_TECH_REDTEAM.md`：权威半截引用。总控追加：

| ID | 主题 | 裁决 |
| --- | --- | --- |
| G02-0001 | 未设置 SameSite ≠ 显式 Lax（Chrome Lax-allow-unsafe，2 分钟顶层 POST） | **P2**。CH08「与 MDN 一致」过宽。MiniShop Cookie 未设 SameSite。 |
| G02-0002 | 点名 RFC 6750 未提 TLS MUST、禁止明文 Cookie 存 Bearer | **P2**。不推翻分层正确；v1.0 无 HTTPS 必须写明「这不是 RFC 6750 完整用法」。 |
| G02-0003 | SQLite/MySQL/PostgreSQL `LIKE` 大小写 | **P2** |
| G02-0004 | 25010:2023 现用名正确；CTFL 4.0.1 考纲主名可能仍是 Usability/Portability | **P2** + 【External Verification Required】英文 CTFL §2.2.2 列表（G02 被 PDF SSRF 拦住） |
| G02-0010 | JMeter Throughput 定义句写成成功数，工具列含失败 | **升 P2**（原 CH18-0011 P3） |

总控 Final Red Team 表不因此改写：ISO 九特性现用名仍正确；GET safe/幂等仍正确。

---

## 7. 重复与顺序（第二遍 cross-check）

- **允许的贯穿：** 公式、qty=10/11、BUG-001、个人项目、无 status。
- **不允许的再主讲：** 第 13.10 再次 ⭐⭐⭐ 讲 GET/POST 幂等（G01-0014）。
- **正式顺序链** 章末预告 03→07→04 正确。
- **入口打乱：** LEARNING「当天」含 8-1/13-1，会跳过为读 PRD 插入的第 7 章。
- **第 7 章插入：** 动机对，兑现弱（开篇 URL 不是本机登录页；第 4 章仍是规则表）。
- **幽灵双基线：** 13–16 现行已是 v1.0 `/api/`；19/20/22/测验 6 仍用现在时打「教学服务 qty=1」。

---

## 8. 修改路线图（按任务要求排序）

1. **P0** 第 1 章登录场景  
2. **P1 尺子** MiniShop oracle：mouse、四态图、主键/种子图、空搜索截图、Cookie 401、lastOrderId、加入购物车、06B 练习 10、3.8 空格  
3. **课程结构** 书面编号、作业规格、幽灵教学服务、星级/梯队一张表  
4. **核心技能缺失** 学生侧 Postman Runner + Network 截图门闩、Git PR、自写 1 条 pytest  
5. **项目** 所属者 200 用例；`disableCookies`；注册截图去重  
6. **图片** caption 串台清扫；删「审查未…」  
7. **练习** 第 20 章范文墙、测验 Q8、08A 题号  
8. **表达** 第 21 章禁「独立开发教材代码」

---

## 9. 源文件索引

- 章：`CHAPTER_01_AUDIT.md` … `CHAPTER_22_AUDIT.md`
- 全局：`GLOBAL_01_CONSISTENCY.md` `GLOBAL_02_TECH_REDTEAM.md` `GLOBAL_03_CODE.md` `GLOBAL_04_EXERCISES.md` `GLOBAL_05_IMAGES.md` `GLOBAL_06_MINISHOP.md` `GLOBAL_07_BEGINNER.md` `GLOBAL_08_EMPLOYMENT.md`
- 清单：`REPOSITORY_INVENTORY.md` `UNIT_INVENTORY.md` `AUDIT_PROGRESS.md`
- 对外总报告：`SOFTWARE_TESTING_COURSE_FINAL_AUDIT.md`
- 第二轮：`SECOND_PASS_AUDIT.md`；专项 `RT_01_COVERAGE.md` `RT_02_STANDARDS.md` `RT_03_SQL_CODE_QUIZ.md` `RT_04_ABS_LINKS_JOB.md`

---

## 10. Second Pass / Red Team（不采信第一轮）

日期：2026-09-10。方法：总控独立 grep/SQL/curl + 4 个 RT Agent。只收漏网或误判。

### 10.1 新增 P0

无。第一轮唯一 P0（种子账号演登录失败）维持。四态图仍不升 P0。

### 10.2 新增 P1（续编 M-P1-35…）

| ID | 主题 | 证据 | 第一轮为何漏 |
| --- | --- | --- | --- |
| M-P1-35 | 测验 3 第 5 题「无 token 下单 = 401」 | `chapters/quizzes/stage-3-web.md` L9/L22；`server.py` `_token` Cookie 回退；RT03-0005。本机仅缺 Bearer、有 Cookie → **201** | G04 矩阵标「同/过 / server.py 印证」——没把「无 token」和「无凭证」分开。与 M-P1-09 同事实，**测验标准答案是新落点** |
| M-P1-36 | 16.6「登录慢就改 `scope=session`」在 autouse 清库下 → 401 | CH16-0004 原文；G03 E61 复现。第一轮标 **P2** | 可复制错误：按教材改仓库 fixture 会认证全红。总控 **升 P1**。第 16 章「无 P1 / B」不成立 |

M-P1-31 补漏点（不新开号）：测验 5 Q9、第 16 章索引同样写 `python3 run.py setup/test` 无 `cd project/minishop`（RT01-0004）。

### 10.3 新增 P2（教材，非审计元数据）

| ID | 主题 | 来源 | 总控 |
| --- | --- | --- | --- |
| M-P2-01 | `PRAGMA foreign_keys` 按连接生效、不进文件；重开 sqlite3 默认 OFF，`user_id=99` 能插入 | RT03-0001 | 采纳。12.12 审查句只在同连接 ON 时成立 |
| M-P2-02 | Host：HTTP/1.1 MUST 发；缺/多/非法 Host 源服务器 MUST 400；值含非默认端口 | RT02-0001 | 采纳。09A 示例有 Host，但没教 MUST 400。不降「要带 Host」 |
| M-P2-03 | 非法 Content-Length MUST 400 并关连接，不是「可能被拒绝」 | RT02-0002 | 采纳。与 M-P1-17（漏写 CL）不同 |
| M-P2-04 | CTFL 4.0.1 FL-1.2.3 是 root cause + error + defect + failure 四词 | RT02-0003 | 采纳。06A 三格表过窄 |
| M-P2-05 | 原则三：静态**和**动态都尽早 | RT02-0004 | 采纳 |
| M-P2-06 | 25010:2023 Testability 仍在 Maintainability；第 4 章「需求可测试」是另一概念 | RT02-0005 | 采纳。G02 因二手矛盾不立案，本轮 JIS/CTFL 可结案 |
| M-P2-07 | G02-0004 EVR **关闭**：CTFL 4.0.1 §2.2.2 主名确为 Usability/Portability | RT02 打开英文 PDF | 维持 P2 映射缺口，去掉 EVR |
| M-P2-08 | 06B 练习 10 答案「加购」 | RT04-0007 | 采纳。M-P1-02/06 的另一落点 |
| M-P2-09 | 第 9 章要求解释 405/415，OpenAPI/实现没有这两码 | RT04-0008 | 采纳 |
| M-P2-10 | `09-pytest-report.png` 真是 pytest-html 4.2.0，但裁掉 Environment/用例表 | RT04-0009 | 采纳 |
| M-P2-11 | `MINISHOP_RESET=1` 清库 ≠ 入职共享库账号池 | RT04-0010 | 采纳 |
| M-P2-12 | JD 要验证码时怎么诚实答（课程禁止写进 v1.0） | RT04-0011 | 采纳 |
| M-P2-13 | GNU grep/coreutils 手册、ISO 78176 对课程 UA **403** | RT04-0002/0005；总控 `curl -L` 复现 | **P3 倾向**：浏览器常可开，403 像反爬。记链接风险，不升 P1 |
| M-P2-14 | 搜索 `lower()` 包含；`sku-demo-001` 能命中；R-SEARCH 未冻大小写 | RT03-0004 | 采纳 |

### 10.4 明确不采纳

| 候选 | 为何不进总表 |
| --- | --- |
| RT03-0002 把 Postman 跑完后的 MiniShop 库 `qty=10/stock=9` 当成 12.16「零行」被打破 | 12.16 / 工作实战建的是 `~/minishop-sql-lab.sqlite` **教学库**，不是 live `minishop.sqlite`。下单不清购物车已是 G06-0004 P2 |
| RT04-0006 第 3 章「完整购物流程」升 P1 | L185 写的是「改购物车数量到创建订单」，正确。「加入购物车」已是 M-P1-02 |
| RT04-0001 `https://未知地址` 当死链 | 反面教材：`不要 curl https://未知地址 \| sh`。不是要打开的资料链接 |
| RT04-0003 RFC 无 `.html` → 302 | `curl -L` 终态 200。可用 |
| CH13 OpenAPI 无后缀 URL 会失效 | 本轮 `spec.openapis.org/oas/v3.0.3` **200**，与 `.html` 同体积。第一轮该条是误判 |

### 10.5 第一轮评分误判（不改已公布章分，记在第二轮）

| 章 | 第一轮 | 第二轮 | 理由 |
| --: | --- | --- | --- |
| 18 | 82 C | **74–76 C** | 九项 69/90≈77；两处 P1 打在标题概念 P95，却全书最高分 |
| 17 | 80 C | **75–76 C** | 68/90≈76；可抄 `getByRole` |
| 11 | 81 B | **76–77 C** | 69/90≈77；11 条 P2；B 偏松 |
| 16 | 79 B、0 P1 | **C，且有 P1** | M-P1-36 升级后 B 不成立 |
| 19 | 81 B | B 偏松 | 空搜索图在第 8 章是 P1，章内写成 P2 才保住 B |
| 7 | 81 C | 维持 | 72/90≈80，主课成立 |

### 10.6 覆盖洞（审计过程，不是教材 P0）

- MASTER「252 围栏 compile/实跑」过满：mermaid 23、markdown 模板 19 未进 G03 执行矩阵。本轮 mermaid `parse` 23/23 合法。
- G05 图片：103 PNG 无漏；漏列 4 个非示意图 HTML（frontend×2、network-log、pytest-report），当实现/证据读过，不是漏图。
- 浏览器未点 `app.js` 路径；Postman GUI / JMeter GUI / Newman 仍未跑（第一轮已披露）。
