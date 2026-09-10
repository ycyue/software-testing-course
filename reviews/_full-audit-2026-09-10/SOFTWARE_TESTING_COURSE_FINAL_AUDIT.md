# SOFTWARE_TESTING_COURSE_FINAL_AUDIT

《软件测试从零基础到初级软件测试工程师》出版级全量审计终稿  
日期：2026-09-10  
总控：Audit Coordinator  
方法：22 章独立 Agent 并行 + 8 个 Global Agent + 总控合并、分歧裁决、Final Red Team  
详细 ISSUE 与裁决：`MASTER_AUDIT.md`  
进度：`AUDIT_PROGRESS.md`

教材正文本次**未修改**。

---

## 1. 总体评分

| 维度 | 分 | 依据 |
| --- | ---: | --- |
| 准确性 | 76 | ISTQB 七原则、ISO 25010:2023 九特性现用名、RFC safe/幂等主课正确；多处 MiniShop 可抄 oracle 与 `server.py` 不符 |
| 完整性 | 72 | 需求→用例→缺陷→HTTP→SQL→接口→pytest→项目链在；Git 协作、缺陷工具实操、GUI 闸门不在 |
| 岗位适用性 | 58 | 能讲方法；默认完课不能演示 Postman/DevTools；人人同一套 qty=11 / BUG-001 / 37-1 |
| 教学设计 | 70 | 脊柱公式清楚；正式顺序 03→07→04 动机对；星级/梯队/高频五套词；第 7 章插入兑现弱 |
| 初学者体验 | 64 | 1-1/5-1 能起步；书面 `2-1` 脚本「没有编号」；15A/11 过载；图文有时对打 |
| 实操质量 | 82 | practice 1-1…19-1 与 `--check` 全绿；MiniShop **37 passed, 1 xfailed** 复现 |
| 项目质量 | 78 | 真前后端、真开放缺陷、真个人项目口径；权限正例、空搜索 Web 证据、Postman Cookie 未达签章 |
| 练习质量 | 76 | 283 道闭卷题 276 道同向；4 道 ANSWER VERIFICATION FAILED |
| 图片质量 | 62 | 85 张示意图全引用、无断链；caption 串台是系统问题；3 张 REPLACE；空搜索截图不可分 |
| 维护性 | 74 | STATUS 诚实；`run.py evidence` 会写回 `chapters/assets/`；收口章仍打已删除的教学服务 |
| **总分** | **71/100** | |

**质量等级：C** — 可以学习，但需要较多修订。

不是 S/A：核心章未到 90。不是 B：P1 尺子多、就业闸门空。不是 D/E：没有把测试理论主课教反，MiniShop 不是空壳，实操能跑。

作者质量标准发布线 90/100、核心章 95：**当前全部未达到**。

---

## 2. P0 问题总表

| ID | 位置 | 问题 |
| --- | --- | --- |
| MASTER-P0-001 | `chapters/01-software-testing-intro.md` L39–42 | 用冻结种子账号 `13800138000` / `Test1234` 演「登录失败并发现缺陷」。同组凭证在 PRD、pytest、第 10/13 章是登录成功。全书开放缺陷是 BUG-001，不是登录。 |

无安全 exploitable P0。无「GET 不安全 POST 安全」类假规则正说。

未升 P0：`ch13-four-shapes` 缺 sku（同节 13.8 表正确）→ P1 必须 REPLACE。见 `MASTER_AUDIT.md` 分歧 D3。

---

## 3. P1 问题总表

去重后 **34 条**，全文见 `MASTER_AUDIT.md` §4。按主题：

**会抄错 MiniShop 观察**

- 冒烟/答案「加入购物车」（第 3 章）
- 3.8 空格「异常提示」（实际是 BUG-001 返回全量）
- `keyword=mouse` → `{"items":[]}`（第 9 图、第 11 curl、第 14 弱断言）
- 不带 Bearer 仍可能 200/201（Cookie 回退）
- `GET /api/orders` 无 id → 404，表写成 401
- 四态图缺 sku，实测 `missing sku`
- 纸面登录报文无 `Content-Length`，裸发 400
- Postman 无凭证 + cookie jar → 201
- `orderId` vs `lastOrderId` → 越权 404
- ch12 把 `products.sku` 当主键；种子图对不上库
- 空搜索截图与商品目录几乎一样
- 06B 练习 10 把 6-1（BUG-001）答成 qty=11
- 08A 验证码仍进 MiniShop 优先检查
- 收口章现在时「教学服务 qty=1」（13–16 已删除）

**作业/验收尺子打架**

- 第 4 章三套规格；template 缺「已确认规则」
- 第 5 章图文判定表错位、状态机 ⭐⭐⭐、三套 8 条过关
- 第 6 章正式计划出口混三套 P0
- README 书面 `2-1` 与 `practice/run.py` 不同构
- 第 22 章自检空表可抄 37 passed

**岗位交付**

- 第 20 章可背范文；测验 Q8 与五段互斥
- 第 21 章简历可抄、未禁「独立开发教材代码」、默认「能使用 Postman/DevTools」
- Playwright 表 `getByRole`（Python 无此 API）
- MiniShop 缺所属者 GET 200 用例
- Git 无 branch/PR；缺陷工具无点击

---

## 4. P2 问题总表（合并主题，不逐条）

- 信息过载：15A 全 ⭐⭐⭐、第 11 章 748 行未拆、08B Cookie/CSRF 密度
- 第 7 章插入未真正服务读 PRD；开篇 URL 不是本机登录页
- caption 从邻图复制（`ch18-p95`、`ch10-ttfb`、`ch16-collect`、`ch05-decision-table`）
- 学生可见「审查未点 GUI / 未安装 JMeter」
- SameSite 未设置 ≠ 显式 Lax（G02-0001）
- 点名 RFC 6750 未写 TLS MUST（G02-0002）
- SQL `LIKE` 大小写方言（G02-0003）
- 25010:2023 现用名 vs CTFL 考纲旧主名未映射（G02-0004）
- JMeter Throughput 定义句「成功数」vs 工具含失败（G02-0010）
- 12.12 INSERT 无 ROLLBACK 会污染后续练习
- 仓库根目录 `pytest` 因多个 `test_lab.py` 收集失败
- 第 13.10 再次 ⭐⭐⭐ 主讲幂等
- LEARNING「当天」实操打乱 07 插队
- 面试「库存 11」听成 stock=11

P2 原文数百条，以各章 §5 与 GLOBAL 报告为准。

---

## 5. P3 问题总表（合并主题）

排版折行、示意图下半留白、`git-scm.com/doc` 跳转、`which` 在 zsh、QUERY 与可缓存名单衔接、Idempotency-Key 仍是 draft、pytest-html `CI:true` 指纹、固定盐勿当安全设计。不阻塞发布。

---

## 6. 最需要修改的 Top 20

1. 第 1 章种子账号演登录失败（P0）
2. Postman「无凭证」未关 cookie jar
3. `ch13-four-shapes` 按 13.8 表补 sku 后重截
4. 全书 `keyword=mouse` 不要绑 `/api/products`
5. 06B 练习 10 按 BUG-001 重写
6. 第 3 章冒烟去掉「加入购物车」
7. 第 8 章写清 Cookie 回退；删假的 `GET /api/orders` 401
8. 正文/集合统一 `lastOrderId`；14.2 先导入
9. 重画 `ch12-pk-fk` / `ch12-tables`
10. 换空搜索证据（URL 或 Network，不要再截目录页）
11. README 实操表区分 ✅ / 📖，避免 `run.py 2-1`
12. 19/20/22/测验 6 删除现在时「教学服务 qty=1」
13. 第 21 章：禁「独立开发 MiniShop」；「能使用」绑定学生 GUI 产物
14. 第 20 章删可背满分段；测验 Q8 改回五段
15. 第 5 章：注册判定表进正文；优惠券/状态机降星；一把过关尺子
16. 第 4 章作业只留一份 template
17. `getByRole` → `get_by_role`
18. 3.8 空格例子对齐 BUG-001
19. 结课自检写启动命令，禁止抄 37 passed
20. 学生作业闸：Postman Runner 记录 + Network 截图 + 1 个 Git PR（不补假图）

---

## 7. 应删除的内容

- 第 1 章把种子成功账号写成登录失败（改，不是删整节）
- 收口章「现行教学服务只让 qty=1」现在时段落
- 第 20 章 20.4–20.14 可整段背的范文（留提纲，删成稿）
- 21.4 可整段复制的四行项目描述（改成空白+路径提示）
- 08A MiniShop 优先检查里的验证码
- `06-register.png` 作为独立注册证据（与 `01-login.png` 字节相同）
- 示意图 caption 里的「审查未点击 / 未安装 JMeter」
- 第 5 章完成标准里倒逼写进 MiniShop 的确认页/锁定/状态机

---

## 8. 应新增的内容

- 第 1 章明确「仓库里仍开放的缺陷是空搜索 BUG-001」
- Postman 请求 `disableCookies` 说明
- 一张「必须掌握 / 大纲梯队 / 星级 / 会做·用过·了解」对照表
- 书面实操在 README 表上的 📖 标记
- MiniShop pytest：所属者 `GET /api/orders/{id}` → 200
- 学生产物闸：`exercises/` 里自写评审、缺陷单、Runner 记录、Network 图
- Git：`branch` / PR 各半页，不要求教完 Git 内部
- SameSite：显式 Lax vs 未设置（Lax-allow-unsafe）三行
- 第 18 章一个真正的 P95 算例（现有 5 个样本够算）

---

## 9. 应重写的内容

- 第 14 章线性阅读：先导入 15 条，再讲面板（现在先新建 Request）
- 第 21 章技能档口与主作业验收
- 第 22 章开篇 mermaid（17/18 消失、Linux/SQL 画成串行）
- `ch18-p95` caption（整段抄了并发≠TPS）
- 第 4 章作业说明（索引 / 04B / template 三套合一）
- 第 5 章 5.9–5.10「实战」表（去掉支付/优惠券路径或彻底标明通用练习系统）

不建议整章推倒重写。没有 E 级章节。

---

## 10. 图片问题总表

Global-05：85 示意图全部被引用，断链 0；KEEP 37 / MODIFY 45 / REPLACE 3。

**REPLACE**

| 文件 | 原因 |
| --- | --- |
| `ch13-four-shapes` | MiniShop Body 缺 sku，oracle 错 |
| `ch12-pk-fk` | `products.sku` 当成主键 |
| `ch12-tables` | 自称种子，缺第三件商品与 admin |

**优先 MODIFY**

`ch18-p95` 图注串台；`ch09-get-post` 的 mouse；`ch05-decision-table` caption 超库存；`ch15-venv` 装包；`ch01-formula` 超纲通道；`04-search-empty-bug001.png` 证明不了提交了空关键字；caption 系统串台（ch10-ttfb、ch16-collect）；「审查未…」四处。

**KEEP 诚实边界：** 不要补假 DevTools 面板、假 JMeter GUI。

运行截图：`01-login` 与 `06-register` sha256 相同。

---

## 11. 代码问题总表

G03 执行矩阵 60+ 项。主线 MATCH。P1 可复制错误：

- Cookie jar → 无凭证下单 201
- `keyword=mouse` 空列表
- 无 `Content-Length` 的纸面 HTTP → 400
- `orderId` / `lastOrderId`
- 12.12 INSERT 无事务（autocommit 永久插入）
- 13.13 `TOKEN=$(curl -D -)` 与 JSON 管道冲突
- 11.6 grep 未给 cwd
- `run.py evidence` 的 `or True` 会写回 `chapters/assets/`
- 仓库根 `pytest` 收集失败（多个 `test_lab.py`）
- Python 表 `getByRole`

第 15 章 35 个 Python 块独立执行与声称输出一致。第 12 章围栏 SQL 用 sqlite3 CLI 数字 MATCH。

---

## 12. 练习与答案问题

G04：283 道先作答。276 同向。

**【ANSWER VERIFICATION FAILED】**

| ID | 题 | 谁错 |
| --- | --- | --- |
| G04-0001 | 第 3 章练习 4 冒烟 | 教材（加入购物车） |
| G04-0002 | 06B 练习 10 | 教材（对象应为 BUG-001） |
| G04-0003 | 第 20 章练习 1「库存 11」 | 教材用词 |
| G04-0004 | 测验 7 第 8 题 STAR vs 五段 | 结构互斥 |

另：12A 练习 4 没写出 JOIN；16B 练习 8 漏 201 / 无 status。08A 题号从 2 起跳。阶段测验无超前必考技术。practice 脚本验收与 v1.0 一致。

---

## 13. MiniShop 项目问题

G06：**有条件通过。** 契约主路径真、37/1 真、缺陷真、不是公司项目。

缺口：所属者 200 无 pytest；Postman 无 Cookie 契约；空搜索 Web 截图弱；`01`/`06` 截图重复；下单不走购物车（PRD 也没写死）；`run.py test` 改写仓库证据；OpenAPI 薄于实现；admin.html 静态 200 ≠ 授权。

简历：禁止假公司有效；挡不住「独立开发教材前后端」。

---

## 14. 岗位能力缺口

G08 就业就绪 **48/100**（招聘官口径，严于教学分）。

| 能力 | 默认完课 |
| --- | --- |
| 测接口 | 能（带教） |
| 诚实描述 MiniShop | 能（若守边界） |
| 看需求 / 写用例 / 提 Bug | 弱（方法在，产物可抄作者） |
| SQL / Linux | 弱（口试能答，不像入职连库） |
| pytest | 弱（会跑作者套件） |
| Postman GUI / DevTools 面板 | 不能（STATUS Incomplete） |
| Git 协作 / 禅道流转 / JMeter / CI | 不能 |

市场高频缺口：Git 协作、Jira/禅道点击、MySQL 客户端、1–3 年/外包 JD 生存、非 MiniShop 现场测、自写自动化。

---

## 15. 教学顺序问题

正式顺序 `01→02→03→07→04→…→22` 章末预告链正确。Linux 与 SQL 并列、不互为硬前置，与大纲一致。

问题在入口与密度，不在箭头：

- LEARNING「当天」含 8-1/13-1，会跳过第 7 章
- 第 7 章插入是为读 PRD，正文却先堆 DNS/Host，开篇 URL 不是本机 MiniShop
- HTTP 201/409 出现在第 5 章用例卡（第 9 章才主讲）
- 14 Postman JS → 15 从零 Python 且整章 ⭐⭐⭐
- 10 GUI → 11 七百行命令

---

## 16. 内容重复问题

允许：公式、qty=10/11、BUG-001、个人项目纪律。  
不允许：第 13.10 再次 ⭐⭐⭐ 讲 GET/POST 幂等。  
收口重复（20–22 禁止句）可接受。  
`keyword=mouse` 是跨章同一错误输入，不是有意复习。

---

## 17. 技术事实风险

已核验为**正确**：ISO 25010:2023 九特性现用名（含 Interaction Capability / Flexibility / Safety）；七原则含 tests wear out；Cookie/Session/Token 非三选一；P0 非全球统一；订单无 status。

**残留风险：** SameSite 默认口径过粗；RFC 6750 只引持有者语义；LIKE 方言；Throughput 定义句；CTFL 考纲质量特性旧主名未映射（G02-0004 EVR）。没有发现 AI 幻觉式的不存在的 pytest API（`getByRole` 是 JS 名误植，不是捏造）。

---

## 18. 过时内容

- Chrome Timing 文案：教材钉 Waiting (TTFB)；Chromium 2022 起 UI 为 Waiting for server response（CH10-0003）
- 未设置 SameSite = Lax 的简化（2026 仍有 Lax-allow-unsafe）
- Idempotency-Key 仍是 IETF draft（了解即可，P3）
- JMeter GUI / Postman Runner：不是过时，是**未跑**；作者已披露

不把 HTTP/1.0 实装当过时错误：是 Python `BaseHTTPRequestHandler` 默认，应标明而非升级装 HTTPS。

---

## 19. AI 生成内容痕迹

未把「文风像 AI」当缺陷。可定位的编辑残留更像工具链：

- 示意图 caption 整段复制邻图（系统性问题，不像逐张手写）
- 「审查未点击」写进学生可见 caption
- 收口章仍警告已删除的教学服务（文档未同步）
- 第 1 章登录故事与项目数据「相同」却结果相反（拼装场景未跑）

这些按 P1/P2 改事实即可，不必以「AI 味」整章重写。

---

## 20. 最终修改路线图

**P0（0.5 h）** 改第 1 章登录场景。

**P1 尺子（6–8 h）** MiniShop oracle 对齐：mouse、四态图、主键/种子图、空搜索证据、Cookie 401、lastOrderId、加入购物车、06B 练习 10、3.8、幽灵教学服务、作业规格。

**课程结构（2 h）** README 📖 标记；星级/梯队一张表；第 14 章先导入。

**核心技能缺失（作者 4 h + 学生 8 h）** 不要补假图。加验收：Runner 记录、Network 截图、fork/PR、自写 1 条 pytest。第 21 章「能使用」绑这些产物。

**项目（2 h）** 所属者 200；`disableCookies`；去重注册截图。

**图片（2 h）** caption 清扫；删「审查未」。

**练习（1.5 h）** 第 20 章范文墙、测验 Q8、08 题号。

**表达（1 h）** 禁独立开发教材代码；结课自检写命令。

---

## 三十六、最终验收问题

### 1. 是否适合真正的零基础从头学到尾？

**有条件适合。** 公式和 1-1/5-1 能起步。会在书面编号、第 7 章插入、第 11/15 章过载、图文不一致处迷路。不能假装「按 README 表逐格敲命令就能学完」。

### 2. 是否存在会把学生教错的技术内容？

**有。** P0：开篇假登录缺陷。P1：Cookie≠401、四态图 oracle、mouse 空列表、加入购物车、练习 10 答错缺陷对象、`getByRole`。主课 ISTQB/RFC/ISO **没有**系统性教反。

### 3. 是否存在培训班话术代替真实软件工程？

**第 20 章有。** 五段做成可背范文，与「不要背名词」对冲。第 1–19 章总体在反话术（禁止绝对化、诚实 Incomplete、个人项目）。第 21 章挡假公司，挡不住「我开发了课程项目」。

### 4. 是否存在明显 AI 幻觉？

**没有捏造不存在的库/RFC 号。** 有拼装未跑的场景（登录失败）和邻图 caption 复制。QUERY=RFC 10008 经 G02 复核正确。

### 5. 是否存在过时技术？

**局部。** DevTools Timing 文案、SameSite 默认简化。JMeter/Postman GUI 是未跑不是过时。HTTP 语义按 RFC 9110 教，方向对。

### 6. 教学顺序是否合理？

**箭头合理，入口和密度不合理。** 03→07→04 是对的。LEARNING 当天实操和第 7 章过厚削弱了插队收益。

### 7. 是否存在知识断层？

**有。** 第 5 章状态码先于第 9 章；14→15 从沙箱 JS 掉进零基础 Python；Git 停在本地 commit；权限正例在项目包里缺测试。

### 8. 是否存在大量重复？

**脊柱重复是设计。** 有害重复不多：13.10 幂等再主讲、mouse 跨章、收口禁止句车轱辘。

### 9. 实操是否足够？

**脚本足够，学生亲手不够。** 10 个可运行实操能绿，但若干用 Python 代替 grep/发报文；Postman/DevTools/JMeter 作者未跑、学生也无闸。克隆仓库 ≠ 学完——这句话正文有，验收没咬住。

### 10. MiniShop 是否足以成为真实简历项目？

**作为个人实践项目：形态够，所有权不够。** 可以写「测过这个仓库里的 MiniShop」。不够写「我从零测完某电商」或「独立开发」。对 0 年功能岗有条件够；对 1–3 年外包不够。课程已正确禁止夸大。

### 11. 完成教程以后是否具备投递初级岗位的基础能力？

**具备「约面」的方法基础，不具备「入职第一周独立干活」的默认证明。** 能讲观察/判定/证据、qty 边界、401/403、SQL JOIN、跑 pytest。现场打开 Postman / 非 MiniShop 登录页 / Git PR 会穿帮。

### 12. 仍然缺少哪些招聘市场高频技能？

Git 协作（branch/PR）、禅道/Jira 流转、MySQL 客户端与只读账号、Chrome Network 学生证据、Postman Runner 学生证据、自写（不是只跑）pytest、1–3 年 JD/外包合同主体、非课程项目的现场测试。

### 13. 哪 20 个问题最应该首先修改？

见本文 §6。

### 14. 如果只能再投入 20 小时，时间花在哪？

| 小时 | 对象 | 做什么 |
| ---: | --- | --- |
| 0.5 | P0 | 改第 1 章登录场景 |
| 6 | P1 尺子 | oracle / 答案 / 图 / Cookie / 变量名 / 编号 |
| 2 | 第 14+21 章 | 先导入；「能使用」绑 GUI 产物 |
| 2 | 第 20 章 | 删范文，留提纲 + 现场测题 |
| 2 | 图片 | 三张 REPLACE + caption 清扫 |
| 1.5 | 第 4–5 章 | 一份作业规格；降星状态机 |
| 2 | MiniShop | 所属者 200、disableCookies、去重截图 |
| 4 | 学生闸（作者侧说明） | 结课必须交 Runner/Network/PR，不补假图 |

不要把 20 小时花在假 DevTools 皮肤或假压测报告上。

### 15. 当前质量等级？

**C：可以学习，但需要较多修订。**

完课学生是「能讲清楚、上手要带」的候选人，不是即战力。教材相对培训班的优势是诚实和可运行项目；劣势是验收验的是作者仓库，不是学生。

---

各章与专项原文：

`reviews/_full-audit-2026-09-10/CHAPTER_01_AUDIT.md` … `CHAPTER_22_AUDIT.md`  
`GLOBAL_01_CONSISTENCY.md` `GLOBAL_02_TECH_REDTEAM.md` `GLOBAL_03_CODE.md` `GLOBAL_04_EXERCISES.md` `GLOBAL_05_IMAGES.md` `GLOBAL_06_MINISHOP.md` `GLOBAL_07_BEGINNER.md` `GLOBAL_08_EMPLOYMENT.md`  
`MASTER_AUDIT.md`
