# RT_01 Coverage & Overscore（第二轮 Red Team）

- 角色：SECOND PASS / Coverage & Overscore
- 日期：2026-09-10
- 对照：`MASTER_AUDIT.md`、各 `CHAPTER_XX_AUDIT.md` Coverage 表、`UNIT_INVENTORY.md`、`GLOBAL_03_CODE.md`、`GLOBAL_05_IMAGES.md`
- 硬约束：未改教材。问题 ID：`RT01-000N`。
- 方法：不采信第一轮「Coverage 100% / 252 围栏 compile 实跑 / 分数」。对任务点名的漏检面逐段打开；对怀疑虚高的章用「九项合计 ÷ 90」和「P1 是否打在标题概念」重判。

一句话：第一轮 **不是空报告**，practice 主线、pytest 37/1、OpenAPI 九条路径、阶段测验 70 题问答、示意图 PNG 确实有人碰过。MASTER 的 Coverage 表仍然 **过满**：把 mermaid / markdown 模板算进「compile/实跑」，把索引页和测验命令当成已执行。分数上，第 18/17/11 章九项折合与公布分差 4～5 分；第 18 章两处 P1 打在标题概念 P95，却拿了全书最高分。第 7 章不压分。

---

## 1. 第一轮 Coverage 声明 vs 本轮核验

MASTER §1 / `AUDIT_PROGRESS.md` 写「未检查 = 0」。本轮只推翻「检查」被写成「执行」的那些行。

| 任务点名资产 | 第一轮声称 | 本轮 | 判定 |
| --- | --- | --- | --- |
| `chapters/quizzes/*` 全文（README + 7×10 题） | G04：70 题独立作答；覆盖声明与 README 一致 | 70 题矩阵在 `GLOBAL_04` §5；问答层做过。**测验 5 Q9 的 `run.py setup/test` 未从仓库根实跑**，判「过」 | 问答有；命令覆盖洞 → RT01-0004 |
| `practice/_http.py` `_minishop.py` `run.py` | G03「全部读 + 实跑」；E01–E14 | 源码逐段复核。G03 已开 P3（unittest 类名、Lab 类属性互踩）。本轮无新 P1 | 第一轮确实查过 |
| `project/minishop/frontend/*.js`（及 html/css） | G03：读 + HTTP 对照；**未开浏览器点击**。CH08/CH19 读过 `app.js` / `admin.html` | 静态复读：路径 `/api/*`、Bearer、空 keyword 发 `?keyword=`、注册不自动登录，均与 PRD 一致。浏览器点击仍未做 | 披露了未点；无新 P1 → RT01-0005 附记 |
| `docs/openapi.json` 全路径 | G03「路径对照 server」；G06「9 条 `/api/*` 与路由集合一致」 | 9 path 与 `server.py` `do_GET/do_POST` 一一对应：`/api/login` `/api/register` `/api/products` `/api/cart` `/api/cart/items` `/api/orders` `/api/orders/{id}` `/api/admin/products` `/api/admin/orders`。无 response schema（已 G06-0007）。集合 GET `/api/orders` 不在文档里，与 404 实现一致 | 路径层查过；schema 层本来就薄 |
| `exercises/README.md` | 多章 Agent 读过，散点报「缺本章文件名」 | 示例只列 5 个；正文至少 19 条产出路径。第一轮没有全局对照表 | 查过但没收口 → RT01-0006 |
| `chapters/assets/07-html-*.html` | CH07「源码 + dump-dom + JS」；G05 打开 2 页 | 密码无 8～16（G05 MODIFY）、combo 有 ¥99（G03-0020）——已有单 | 第一轮确实查过 |
| mermaid 块 23 | 计入 252；各章 Coverage「mermaid 已检查」 | G03 **范围句排除** mermaid，执行矩阵无渲染/解析。本轮静态：23/23 首行合法，方括号/花括号计数匹配 | 读了源；**未执行** → RT01-0002 |
| 索引页 04/06/08/09/12/15/16 | 各章 Coverage 计 1 页 / 14 行 | 七页全文 14 行，链接可解析。06「进入第 8 章」与学习顺序 03→07→04→…→06→08 一致。**16 索引 `python3 run.py test` 无 `cd`** | 读过；16 索引命令漏标 → RT01-0004 |
| 章节代码围栏 252 | MASTER：「252（G03 compile/实跑）」 | G03 类型表只执行 python/bash/sql/js/json/html/css/ini/yaml + 部分 HTTP。mermaid 23 + markdown 19 + 大量 text **不能 compile** | 总表过满 → RT01-0001 |

---

## 2. UNIT_INVENTORY 围栏 vs GLOBAL_03 执行矩阵

`UNIT_INVENTORY.md`：text 82、python 47、bash 44、**mermaid 23**、**markdown 19**、sql 19、javascript 8、json 5、html 2、css/ini/yaml 各 1。合计 **252**。

G03 §1 范围原句只列「python/bash/sql/json/javascript/yaml/html/css/ini/http-text」，**没有 mermaid、没有 markdown**。类型表也没有这两行。然后用「合计 252 / 已检查 252 / 未检查 0」把它们吞进去。MASTER 再升级成「compile/实跑」。

### 2.1 声称检查、执行矩阵里没有的围栏

| 语言 | 数量 | 第一轮实际做了什么 | 本轮 |
| --- | ---: | --- | --- |
| mermaid | 23 | 章 Agent 读源；无 `mmdc`/parse 记录 | 静态扫描 23 块：`flowchart TD/LR/BT`、`sequenceDiagram`、`stateDiagram-v2`。未发现括号失配或未知头。语义上第 7 章渲染图 A/B 并行汇入 C、第 17 章 `flowchart BT` 金字塔，语法成立。**不能把「已读」写成「已执行」** |
| markdown 模板 | 19 | 章 Agent 当作业模板读；CH04 抓到缺列。G03 无 markdown 行 | 模板不是代码。G03 把它算进 252 compile 是错账 |
| 伪代码 / 公式 text | 计入 text 82 | 无单独类。例：第 5 章等价覆盖率公式、第 18 章 JMeter 树 ASCII | 不能 compile。G03 执行矩阵未点名 |
| HTTP 纸面报文（```text```） | 散布 09A/09B/13（及 08B Bearer 一行） | E31–E36、E50：登录缺 `Content-Length`、实装 HTTP/1.0；E32：`keyword=mouse` | **已执行**：13.12 / 09B 登录可抄报文（→ G03-0003 / M-P1-17）。**未单独进矩阵**：09A `GET /products?keyword=mouse`（Host `shop.example.test`，本来就不是 MiniShop）；09B `GET /api/cart` + Bearer（E39 测的是 Cookie 回退，不是这条纸面 GET） |

markdown 19 处位置（作业模板，不是可跑代码）：

`04b` 评审记录、`06a` 缺陷卡、`06b` 计划、`07` 观察报告、`08b` 功能测试包、`09b` HTTP 观察、`10` DevTools、`11` Linux 排障、`12b` SQL 验证、`13` 接口检查、`14` Postman 集合、`15b` Python 数据检查、`16b` pytest 记录、`17` 分层地图、`18` 性能清单、`19` 执行记录、`20` 口述稿、`21` 简历、`22` 结课自检。

mermaid 23 处：01 流程；02×2（阶段地图 / Scrum）；03 六轴；05 因果图 + 状态机；06A 缺陷生命周期；07×3（访问六步 / 请求响应 / 渲染）；08B 认证分层；09A×2 + 09B 序列；10 DevTools；13 接口流；14 Postman；17 金字塔；18 性能模型；19 收口；20 五段；21 简历证据；22 路线。

### 2.2 第一轮真正执行了的（本轮不翻案）

- python 47：G03 E17–E21、E60；第 15 章声称输出 MATCH。
- sql 19：E24–E30。
- bash 中 curl/grep/git：E32、E50–E54。危险命令（`kill 12345` / `ssh tester@192.0.2.10`）静态审，E63 故意跳过——这行诚实。
- practice 10 条 `--check` 全绿；MiniShop **37 passed / 1 xfailed**。
- JS 围栏 `node --check`；前端 `app.js` 不在 8 个围栏里，是仓库文件，G03 读过。

---

## 3. GLOBAL_05 图片总表 vs 磁盘 png/html

### 3.1 PNG：无漏文件

磁盘（排除 `.git` / `reviews`）：

- 示意图 `chapters/assets/diagrams/ch*.png`：**85**
- 运行截图 `chapters/assets/*.png`：**9**
- 证据副本 `project/minishop/evidence/screenshots/*.png`：**9**（G05 已做 sha256 全等）

合计 **103**，与 MASTER / G05 一致。85 张示意图均有同名 HTML。`06-register.png` 章节无 `![]`、与 `01-login.png` 字节相同——G05 已列为未引用 / DELETE，不是漏图。

教学草稿 `ch04-two-rulers.png` 磁盘上不存在，G05 已说明不是断链。

### 3.2 HTML：示意图无漏；总表漏了 4 个非示意图 HTML

磁盘 HTML（排除 `reviews/`）：

| 类 | 数量 | G05 总表 |
| --- | ---: | --- |
| `diagrams/ch*.html` | 85 | 85，已打开 |
| `07-html-lab.html` / `07-html-combo.html` | 2 | 2，已打开 |
| `project/minishop/frontend/index.html` | 1 | **未列入图片表**（G03/CH19 当实现读过） |
| `project/minishop/frontend/admin.html` | 1 | 同上 |
| `project/minishop/evidence/http/network-log.html` | 1 | **未列入**（CH09/CH19 当 HTTP 证据读过） |
| `project/minishop/evidence/pytest-report.html` | 1 | **未列入**（CH19 只核摘要数字，明确不逐字节） |

G05 范围本来是「图片」。任务要求「磁盘全部 png/html」时，这 4 个 HTML 不在总表里。**不是断链，是清单口径窄了一圈。** 不把它们当漏图 P1。

`diagrams/_theme.css`、`diagrams/README.md`：G05 已标为源/说明。

---

## 4. 过高评分（只压有证据的章）

比较规则：九项（各 /10）合计 ÷ 90 × 100，对照公布「总体」。P1 是否打在**该章标题概念**上。不为找问题而压第 7 章。

| 章 | 公布 | 九项合计 | 折合 | 公布−折合 | P0/P1 | 标题概念上的 P1？ | 本轮 |
| --: | --: | --: | --: | --: | --- | --- | --- |
| 18 | **82** C | 8+8+8+7+8+8+8+8+6 = **69/90** | **77** | **+5** | 0 / 2 | **是**（P95 图注串台 + 不算 P95） | 虚高。建议 **74～76 C** |
| 17 | 80 C | 8+8+8+7+7+7+7+8+8 = **68/90** | **76** | **+4** | 0 / 1 | 部分（17.4 对照表 `getByRole`，了解章可抄 API） | 虚高。建议 **75～76 C** |
| 11 | 81 **B** | 8+8+8+7+7+8+8+8+7 = **69/90** | **77** | **+4** | 0 / 1 | 否（Linux 定义没错；P1 在 11.13 MiniShop curl） | 分数虚高；**B 偏松**。建议 **76～77 C** |
| 7 | 81 C | 9+8+8+7+8+9+7+8+8 = **72/90** | **80** | +1（报告自己写了 72/90 → 81） | 0 / 1 | 开篇 MiniShop 网址，主课 URL/DNS/DOM 正确 | **不压。** 维持 C，约 80 |
| 19 | 81 **B** | 8+8+8+7+8+8+8+9+7 = **71/90** | **79** | +2 | 章内 0 P1 | 同一张空搜索图在第 8 章是 P1 | 分数轻微虚高；**B 靠「章内 0 P1」**，等级判松 → RT01-0010 |
| 16 | 79 **B** | 九项 71/90≈79；另加第 10 维后 **79** | 79 | 0 | 章内 0 P1 | fixture 课「改 session → 401」被写成 P2 | 算术不虚；**严重度偏低** → RT01-0009 |

对照：第 14 章 59/90→66、第 8/12/13 章 66/90→73，核心章按折合记账。第 18 章了解章、折合 77、两处标题 P1，公布 82，是全书最明显的分数膨胀。

第 18 章自己写「C 明显需要修改」——**结论档对，分数不对**。

---

## 5. ISSUE

不重复 MASTER 已立案的主题（假登录、加入购物车、Cookie 回退、`keyword=mouse`、四态缺 sku、P95 串台、`getByRole`、qty=1 幽灵、测验 Q8 五段 vs STAR、所属者 200 缺 pytest…），除非本轮认为 **等级或覆盖范围判错**。

---

## ISSUE

ID：RT01-0001  
文件：`reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`；`GLOBAL_03_CODE.md`；`UNIT_INVENTORY.md`  
章节：审计元数据（非教材）  
小节：MASTER §1 Coverage；G03 §1  
精确位置：MASTER L30「章节代码围栏 252（G03 compile/实跑）」；G03 合计 252 / 未检查 0  
原文：已检查 252，未检查 0；compile/实跑  
问题等级：P2  
问题类别：COV / AUDIT  
问题说明：UNIT 的 252 含 mermaid 23 + markdown 19 + text 82。G03 范围句与执行矩阵只覆盖可解释器跑的语言和部分 HTTP。把「读过围栏」写成「compile/实跑」让总控 Coverage 表看起来 100%，实际有 ~42 块从未进入执行矩阵。  
为什么有问题：后续读者会以为 23 张 mermaid 渲染过、19 份作业模板当代码跑过。这是第二轮必须打的覆盖洞，不是教材新缺陷。  
依据：UNIT 语言分布；G03 E01–E63 无 mermaid/markdown；本轮 mermaid 静态扫描。  
建议修改：MASTER Coverage 拆三行：可执行围栏（python/bash/sql/js/json/…）实跑；mermaid/markdown/text **已读未执行**；HTTP 纸面列出已 socket 的 ID。  
推荐替换文本：章节围栏 252：python/bash/sql/js/json/html/css/ini/yaml 已 compile 或实跑；mermaid 23 / markdown 19 已读源、未渲染；HTTP 纸面见 G03 E31–E36。

---

## ISSUE

ID：RT01-0002  
文件：`chapters/*.md` 中 23 个 mermaid 围栏；`GLOBAL_03_CODE.md`  
章节：跨章（图源）  
小节：各章场景导入 / 模型图  
精确位置：见 UNIT_INVENTORY mermaid 行  
原文：各章 Coverage「mermaid N / 已检查 N / 0」  
问题等级：P2  
问题类别：COV / IMG  
问题说明：章 Agent 把 mermaid 当已检查。G03 不渲染。本环境 `mmdc` 不在 PATH（npx 包存在但本轮未强制拉浏览器渲染）。静态检查：23/23 头合法、括号匹配，**未发现会让 GitHub 预览直接碎掉的语法错误**。  
为什么有问题：覆盖声明超额。若以后改图，没有「渲染基线」。不是教材 P1。  
依据：`rg '```mermaid'` → 23；本轮脚本按块扫描。  
建议修改：补一行「mermaid：源码审阅，未用 mermaid-cli 出图」。不要写进 252 实跑。  
推荐替换文本：见 RT01-0001。

---

## ISSUE

ID：RT01-0003  
文件：上表 19 个 ```markdown 作业模板  
章节：跨章  
小节：MiniShop 工作实战模板  
精确位置：UNIT markdown 19 行  
原文：G03 合计 252 已检查  
问题等级：P3  
问题类别：COV  
问题说明：markdown 模板应当作业规格审（缺列、四列 vs 层），不该进 compile 桶。CH04 对 04 模板缺列是真审；G03 没有 markdown 执行行却吃进 252。  
为什么有问题：同 RT01-0001 的账。模板内容缺陷已由各章 ISSUE 覆盖，这里只记账。  
依据：UNIT；G03 §1 类型表。  
建议修改：252 拆账。  
推荐替换文本：markdown 19 = 书面模板，已由章 Agent 读，不计入 compile。

---

## ISSUE

ID：RT01-0004  
文件：`chapters/quizzes/stage-5-api.md` Q9；`chapters/16-pytest.md` L10；对照 `chapters/18-performance-testing.md`（已 M-P1-31）  
章节：测验 5 + 第 16 章索引  
小节：依赖安装 / 索引作业  
精确位置：测验答案「`python3 run.py setup` 然后 `python3 run.py test`」；索引「跑 `python3 run.py test`（37 passed / 1 xfailed）」  
原文：均无 `cd project/minishop`  
问题等级：P2  
问题类别：COV / PRE / CODE  
问题说明：M-P1-31 只钉第 18 章 `python3 run.py serve`。同类命令在 **测验 5 第 9 题标准答案** 和第 **16 章索引**（学生入口，14 行里最可复制的一句）再次出现。G04 阶段 5 矩阵 Q9「同 / 过」；CH16 Coverage 把索引标已检查，P1 栏空。仓库根没有 `run.py`；`practice/run.py test` 会走「没有编号」。  
为什么有问题：这不是新发明「缺工作目录」主题，是第一轮 **漏扫副本**。测验答案会被学生当一键命令抄。等级保持 P2：16B / 第 19 章正确入口有 `cd`；索引和测验是短入口。不升 P1，避免与 M-P1-31 双计。  
依据：本轮读索引与测验全文；G04 L928 Q9「过」；`practice/run.py` PRACTICE_DIRS。  
建议修改：总控把 M-P1-31 扩成「凡写 `run.py setup/test/serve` 必须带 `cd project/minishop`」，补测验 5 Q9 与 16 索引。  
推荐替换文本：`cd project/minishop && python3 run.py setup && python3 run.py test`（37 passed / 1 xfailed）。不要在仓库根执行。

---

## ISSUE

ID：RT01-0005  
文件：`GLOBAL_05_IMAGES.md`；磁盘 HTML  
章节：图片审计口径  
小节：G05 §1 / §3  
精确位置：Coverage 表只列 85+9+9 PNG 与 85+2 示意图/练习 HTML  
原文：未打开 0  
问题等级：P3  
问题类别：COV / IMG  
问题说明：PNG 103 张与磁盘一致，**无漏图、无断链**。任务「磁盘全部 png/html」下，G05 未列 `frontend/index.html`、`admin.html`、`evidence/http/network-log.html`、`evidence/pytest-report.html`。前两个实现文件、后两个生成证据；CH19 已声明 pytest-report 不逐字节。  
为什么有问题：MASTER「示意图 85+85 全部打开」仍成立。把「图片 100%」读成「仓库 HTML 100%」会满。  
依据：`find … -name '*.html'`（排除 reviews）= 91。  
建议修改：G05 Coverage 加「非示意图 HTML 4，不在图片审计分母；由 G03/G06/章 19 读」。  
推荐替换文本：无教材替换。

---

## ISSUE

ID：RT01-0006  
文件：`exercises/README.md`  
章节：书面作业入口  
小节：建议文件名列表 L7–L11  
精确位置：只列举 04 / 12 / 16 / 19 / 21  
原文：建议文件名与各章工作实战路径一致，例如这五条  
问题等级：P2  
问题类别：COV / PED  
问题说明：第一轮 CH02/03/07/17/20/22 等已散点报「README 没有本章文件名」。没有人做 **正文路径全集 vs README 示例** 对照。正文至少：`chapter-03-classification-card`、`chapter-04-…review`、`chapter-05-…test-cases`、`chapter-06-bug-001`、`chapter-06-…test-plan`、`chapter-07-web-observation`、`chapter-08-…web-functional`、`chapter-09-…http-observation`、`chapter-10-…devtools`、`chapter-11-…linux`、`chapter-12-…sql`、`chapter-13-…api`、`chapter-14-…postman`、`chapter-15-…python`、`chapter-16-…pytest`、`chapter-17-…automation-map`、`chapter-18-…performance`、`chapter-19-…run`、`chapter-20-interview-script`、`chapter-21-resume`、`chapter-22-self-check`。README 5 / ≥19。  
为什么有问题：学生只看 `exercises/README.md` 会以为书面作业只有五份。不是答案错误。第一轮漏的是 **汇总**。  
依据：本轮 `rg exercises/chapter-`；`exercises/README.md` 全文 13 行。  
建议修改：README 改成「各章工作实战里的路径为准」+ 完整清单，或删「例如」以免被当成闭集。  
推荐替换文本：书面作业文件名以各章「MiniShop 工作实战」为准，不要只看下面五条例子。

---

## ISSUE

ID：RT01-0007  
文件：`CHAPTER_18_AUDIT.md`；`chapters/18-performance-testing.md`  
章节：第 18 章  
小节：总评分；18.2 百分位  
精确位置：总体 82；CH18-0001/0002  
原文：总体 82/100；图片 6/10；两处 P1 在 P95  
问题等级：P2  
问题类别：AUDIT / SCORE  
问题说明：九项 69/90 ≈ **77**，公布 **82（+5）**。两处 P1 打在章标题概念「响应时间与百分位」：图注整段是邻图「并发≠TPS」；唯一算例停在平均/中位/最大，练习 2 也不问 P95。了解章（LEARNING ⚪）拿全书最高分。章结论已是 C，分数与结论打架。  
为什么有问题：和核心章（14=66、5=71、8/12/13=73）比，了解章带标题 P1 不应是最高分。不是新的教材 P1（M-P1-23 已立）。本单只打 **虚高**。  
依据：CHAPTER_18 评分表；MASTER L57。  
建议修改：总控改记第 18 章 **74～76 C**。不要改教材。  
推荐替换文本：无。

---

## ISSUE

ID：RT01-0008  
文件：`CHAPTER_17_AUDIT.md`  
章节：第 17 章  
小节：总评分  
精确位置：总体 80；CH17-0004 `getByRole`  
原文：80/100  
问题等级：P3  
问题类别：AUDIT / SCORE  
问题说明：九项 68/90 ≈ **76**，公布 **80（+4）**。P1 在 17.4 对照表（Python 轨可抄 camelCase）。主课金字塔/ROI 未绝对化，了解章 80 仍偏高。  
为什么有问题：分数膨胀小于第 18 章；P1 已 M-P1-22。本单只打虚高。  
依据：CHAPTER_17 评分表。  
建议修改：总控改记 **75～76 C**。  
推荐替换文本：无。

---

## ISSUE

ID：RT01-0009  
文件：`CHAPTER_16_AUDIT.md`；`GLOBAL_03_CODE.md` E61 / G03-0014  
章节：第 16 章  
小节：16.6「登录很慢再改为 session」；CH16-0004  
精确位置：CH16-0004 现为 P2；章结论 B、P1=0  
原文：登录很慢时再改为 `scope="session"`  
问题等级：P1（等级判错；主题已有章内 P2，不新开教材事实）  
问题类别：AUDIT / CODE  
问题说明：G03 给 P1 的操作定义是「按教材复制得到与课文不同的观察」。E61：登录 200 → `reset_db` → 同 token 购物车 **401**。16.6 把改 session 写成可执行建议。CH16 自己复现了 401，却标 P2，再凭「无 P1」给 **B 小修**。算术 79 不虚；**档位虚**。  
为什么有问题：核心 pytest 章。学生按「最稳是 function，慢了改 session」改仓库 `token_a`，认证用例会红，看起来像 pytest 坏了。与 Postman cookie 罐、缺 Content-Length 同类。  
依据：G03 E61；CH16-0004 正文；MASTER P1 表未收这条。  
建议修改：总控把 CH16-0004 **升 P1**（可并入总表新行，或并进「可复制脚本与实装冲突」）。第 16 章结论改为 **C**，分数可留 76～79。  
推荐替换文本：无教材新文本；用 CH16-0004 已给的替换（token 必须 function）。

---

## ISSUE

ID：RT01-0010  
文件：`CHAPTER_19_AUDIT.md` CH19-0007；对照 CH08-0003 / M-P1-11 / G05  
章节：第 19 章  
小节：19.5 空搜索截图；总评 B  
精确位置：CH19-0007 **P2**；总体 81 B  
原文：alt「空搜索 BUG-001」；章内 0 P1  
问题等级：P2（审计等级不一致；图本身已是 MASTER P1）  
问题类别：AUDIT / IMG  
问题说明：同一文件 `04-search-empty-bug001.png`：第 8 章 P1 + REPLACE，G05 同意 REPLACE，MASTER M-P1-11。第 19 章是项目收口、把这张图当开放缺陷的展示证据，却标 P2，从而「无 P1 → B」。九项 71/90≈79，公布 81，膨胀不大；**B 靠降级同一张图**。  
为什么有问题：收成章的视觉证据弱于 HTTP 证据，学生会以为「空搜索」长得像商品目录。事实已立案；本单打章间等级不一致导致的过档。  
依据：CH19-0007；CH08-0003；G05 `04-search-empty`；MASTER M-P1-11。  
建议修改：CH19-0007 与 M-P1-11 对齐为章内 P1（或注明「项目图沿用 M-P1-11，不单开」）。第 19 章改为 **C**，分数 **78～79**。所属者 200 缺 pytest 维持项目包 P1（M-P1-32），不要和这张图加两次。  
推荐替换文本：无。

---

## ISSUE

ID：RT01-0011  
文件：`CHAPTER_11_AUDIT.md`  
章节：第 11 章  
小节：总评分 81 B  
精确位置：九项 69/90；P1=CH11-0001 `keyword=mouse`；P2×11  
原文：81/100；B 小修  
问题等级：P3  
问题类别：AUDIT / SCORE  
问题说明：折合 **77**，公布 **81（+4）**。P1 不是 Linux 定义教错，是 11.13「最小读取」curl 打空列表（已 M-P1-13）。11 条 P2（cwd、pgrep -a、ps 打空、`<redacted>` 登录 401…）不算「小修」。B 的通常含义是改一两处可发布。  
为什么有问题：与第 9 章同 P1（mouse）、78/B 相比，第 11 章 P2 密度更高却 81/B。  
依据：CHAPTER_11 评分表与 ISSUE 计数；MASTER 给第 11 章 B。  
建议修改：分数 **76～77**；结论 **C**（可以学，curl 示例和一批声明要改）。不把 mouse 再开新教材 P1。  
推荐替换文本：无。

---

## 6. 本轮确认：第一轮确实查过、不新开单

| 项 | 证据 | 结论 |
| --- | --- | --- |
| 测验 70 题问答 | G04 §5 七张矩阵；Q8 FAIL 已 G04-0004 / M-P1-25；Q5 qty=1 已 G04-0010 / M-P1-24 | 全文问答做过。本轮复读未发现第三处 ANS FAIL |
| `quizzes/README.md` | 15 行；阶段 1 在学完第 7 章后，与学习顺序一致 | 无问题 |
| `practice/_http.py` | urllib 自动 Content-Length、JSON Accept、HTTPError 解析 | 与纸面缺 CL 分工正确；G03 已跑 |
| `practice/_minishop.py` | 临时库 + 随机端口；退出不恢复类属性 | G03-0018 P3 已立 |
| `practice/run.py` | 10 个可运行 ID + 书面 4-1/6-1；无 2-1 | M-P1-29 已立 |
| `frontend/app.js` | 登录/注册/搜索/购物车/下单；`encodeURIComponent`；`innerHTML` | G03-0017 P3 XSS 已立；空搜发 `?keyword=` 与 BUG-001 一致 |
| `frontend/index.html` | 登录 `required`、注册无 HTML5 尺、无加购按钮 | 与第 8 章「浏览器 required ≠ 服务端」同向 |
| `admin.html` | 401/403 合成「无权限」 | CH08 L541「可接受」；静态 200 vs API 403 已 CH19-0009 |
| OpenAPI 9 path | 与 `server.py` 路由集合一致；`/api/cart/items` 无 404 已 G03-0019 | `_get_order`：非所属者（含管理员看他人单）403，与「admin get 403」在越权场景成立 |
| `07-html-lab.html` / combo | 不连服务器；lab 密码无 8～16；combo「加入购物车」+ ¥99 | G05 / G03 / CH07 已立 |
| 索引 04/06/08/09/12/15 | 分流 + 作业锚点 + 测验指针，无错误绝对化 | 06→08 不是漏第 7 章 |
| 第 7 章 81 | 72/90≈80 | **不压分** |

前端 G03「未开浏览器点击」仍是覆盖限制：没有点击注册失败路径、没有看空搜提交后的 Network。静态与 HTTP 矩阵已覆盖主路径，不升 P1。

---

## 7. 给总控的调整建议

1. MASTER Coverage 表：删掉「252 compile/实跑」这种写法。拆可执行 / 已读未跑。全书「未检查 = 0」这条 **不成立**（至少 mermaid 渲染、markdown compile、测验 Q9 命令、前端点击）。
2. 分数：18 → 74～76 C（最高分不该在这章）；17 → 75～76 C；11 → 76～77 **C**；19 → 78～79 **C**；16 分数可留、结论 **C**（升 CH16-0004）。7 不动。
3. 总表新行只需：CH16 session token（升 P1）；M-P1-31 扩测验 5 Q9 + 16 索引；CH19 空搜索图与 M-P1-11 对齐。不要把 P95 / mouse / getByRole 再写一遍。
4. 不改教材。本文件只审计第一轮覆盖与分数。

---

## 8. 本轮打开但未改的路径（取证）

- 测验：`chapters/quizzes/README.md` + `stage-1` … `stage-7` 全文
- 索引：`04` `06` `08` `09` `12` `15` `16` 七页全文
- `practice/_http.py` `_minishop.py` `run.py`
- `project/minishop/frontend/app.js` `index.html` `admin.html`
- `project/minishop/docs/openapi.json` 全文 9 path
- `exercises/README.md`
- `chapters/assets/07-html-lab.html` `07-html-combo.html`
- 磁盘全部 png/html 清单（find）
- UNIT 252 围栏表 + G03 E01–E63 + 23 mermaid 源块
