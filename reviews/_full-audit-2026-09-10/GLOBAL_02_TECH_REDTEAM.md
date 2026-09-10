# Global-02 技术事实 Red Team

日期：2026-09-10  
Agent：Global-Agent-02（技术事实，独立抽核；本轮为额度中断后的重跑，必须落盘）  
范围：`chapters/*.md` 中的定义与技术断言；对照 ISTQB CTFL 4.x / Glossary、ISO/IEC 25010:2023、RFC 9110/6750、Python 3 / pytest / requests、Playwright、SQL 方言、Linux vs macOS、Postman / JMeter、Cookie-Session-Token。  
硬约束：未改教材。未通读 22 份 CHAPTER 审计全文；只 grep 了 ISSUE 标题/问题说明与教材定义段。每类最多深入 8 条最可疑断言。

结论先说：**没有新的 P0。** 章 Agent 已把 CTFL 七原则主线、error/defect/failure、V 模型四行表非 4.0.1 原文、测试级别 4 vs 5、405/401 的 RFC MUST、Playwright `getByRole`、DevTools Timing 改名、Cookie jar 把 401 打绿等打掉。本轮新问题集中在三处「引用了权威却没把权威读完」：SameSite 未设置 ≠ 显式 Lax（Chrome Lax-allow-unsafe）、RFC 6750 的 TLS/Cookie 禁令、以及 CTFL 4.0.1 仍以 Usability/Portability 为主名却把 2023 九特性写成唯一名单。SQL LIKE 大小写方言是第 12 章漏掉的可移植陷阱。

---

## 1. 方法

| 步骤 | 做法 |
| --- | --- |
| 对照章 ISSUE | 只抽 `CHAPTER_XX_AUDIT.md` 的 ID 行与「问题说明」首段，以及 `_CHAPTER_P1_INDEX.md`。不复述已有 CHXX。 |
| 抽教材断言 | grep 定义段：七原则、V 模型、测试级别、25010、safe/幂等/可缓存、401/403/405、pytest/requests、getByRole、LIKE/GROUP BY、grep -R/free/which、pm.*、Cookie/SameSite/Bearer、JMeter Throughput。 |
| 权威抽核 | `web_search` / `web_fetch`：RFC 9110、RFC 10008、RFC 6750、RFC 5789、ISO 25010:2023 预览、arc42、MDN Set-Cookie、Chromium SameSite FAQ、SQLite LIKE、pytest 9.1.1、JMeter 5.6.3、IETF Idempotency-Key draft。ISTQB 英文 PDF 被 SSRF 拦住，CTFL 4.0.1 §2.2.2 英文原句标 【External Verification Required】；丹麦语官方译本 release note 10.1.3 已足够提出名单冲突。 |
| 每类上限 | 每条攻击清单最多 8 条深入；本报告只收「章 Agent 未单列、或裁决过轻」的项。 |
| 不重复 | 代码/命令级假规则（`keyword=mouse`、HTTP/1.0 vs 1.1、Postman Cookie 罐、INSERT 无 ROLLBACK）交给 CH09/11/14 与 GLOBAL_03。 |

攻击清单覆盖结果（深入条数 = 真正对着权威重读的断言，不是 grep 命中数）：

| # | 类别 | 深入 | 新 ISSUE |
| --- | --- | --- | --- |
| 1 | ISTQB CTFL 4.x / Glossary | 8（定义、七原则、级别、V 模型、探索性、error/defect/failure、确认 vs validation、评审活动） | G02-0004（25010 名单与考纲主名） |
| 2 | ISO/IEC 25010:2023 | 8（九特性英文名、Usability/Portability 更名、Safety、Security 译法、性能效率子特性、与 ISTQB 双轨） | 并入 G02-0004 |
| 3 | RFC 9110 | 8（safe/幂等/可缓存、GET/POST、401/403/404/405、PATCH、QUERY、2xx 措辞） | G02-0006、G02-0008 |
| 4 | Python 3 / pytest / requests | 6（type vs isinstance、open encoding、json=、timeout、fixture scope、raise_for_status） | 无新事实错误 |
| 5 | Playwright getByRole vs get_by_role | 1 | 不重复 CH17-0004 |
| 6 | SQL 方言 | 5（LIKE、GROUP BY、FK PRAGMA、TRUNCATE、INTEGER PK NULL） | G02-0003（LIKE）；GROUP BY 已是 CH12-0012 |
| 7 | Linux vs macOS | 6（free、ls --help、grep -R、pgrep -a、which、df 列名） | G02-0009（which/zsh）；其余已是 CH11 |
| 8 | Postman / JMeter | 6（pm.test/code、变量五层、Throughput、Latency、Java 版本、Idempotency-Key） | G02-0005；Throughput 升级见 G02-0010 |
| 9 | Cookie / Session / Token | 6（分层、HttpOnly、SameSite、Secure、Bearer、RFC 6750 TLS） | G02-0001、G02-0002、G02-0007 |
| 10 | 过时知识 | 5（QUERY RFC 号、pytest 9、JMeter 5.6.3、checkout@v4、Idempotency-Key 仍是 draft） | G02-0005；QUERY 号经核验正确 |

---

## 2. 新发现

### P0

无。

### P1

无。本轮最重的两条（SameSite 默认、RFC 6750 TLS）会让面试/缺陷口径写错，但不会让 MiniShop 主路径测反（v1.0 明确不做 HTTPS、不做 CSRF 演练）。

### P2

```
## ISSUE
ID：G02-0001
文件：chapters/08b-web-auth-permission.md
章节：第 8 章（下）
小节：8.11 Cookie 属性表；紧随的 CSRF 段
精确位置：L70；L73
原文：未设置时，现代浏览器通常按 Lax 处理……`SameSite=Lax`（现代浏览器对未设置 SameSite 的常见默认）会挡住大多数跨站 POST
问题等级：P2
问题类别：ACC / TERM
问题说明：把「未设置 SameSite」写成「就是 Lax，因而挡住大多数跨站 POST」。Chrome 对未设置属性的 Cookie 用的是 Lax-allow-unsafe：显式 `SameSite=Lax` 的跨站顶层 POST 始终不带 Cookie；未设置时，Cookie 年龄 ≤ 2 分钟的顶层跨站 POST **会带上**。MDN `Set-Cookie` 2026-09 仍写：When Lax is applied as a default, a more permissive version is used… POST … no more than two minutes。Chromium FAQ 称之为 Lax + POST mitigation。MiniShop `server.py` 的 Set-Cookie 是 `minishop_session=…; HttpOnly; Path=/`，**没有 SameSite**，正好落在这个洞里。
为什么有问题：学生会写两种错缺陷：（1）「未设 SameSite = 已有 Lax，跨站 POST 带不上」；（2）刚登录 2 分钟内的跨站 POST 带上了 Cookie，却按教材判「浏览器坏了」。章 Agent 以「与 2026 MDN 一致」放过。
依据：MDN Set-Cookie / SameSite（检索 2026-09-10）；https://www.chromium.org/updates/same-site/faq/ 「Lax + POST mitigation」；PortSwigger *Bypassing SameSite cookie restrictions*；`project/minishop/server.py` L299。
建议修改：拆成三行：显式 Lax、未设置（Chrome 默认更宽、含 2 分钟顶层 POST）、None 必须 Secure。MiniShop 脚注写「v1.0 Cookie 未设 SameSite」。
推荐替换文本：未设置 SameSite 时，Chrome 等按 **Lax-allow-unsafe** 处理：看起来像 Lax，但 Cookie 写入后约 2 分钟内，顶层跨站 POST 仍可能带上。显式 `SameSite=Lax` 没有这个洞。MiniShop v1.0 的 `Set-Cookie` 只有 `HttpOnly; Path=/`，属于未设置。不要把「默认 Lax」写成「跨站 POST 一定带不上」。`None` 必须同时有 `Secure`。
【Agent Disagreement】CHAPTER_08 把 SameSite 段判「通过 / 与 MDN 2026-09 一致」（审计表 L491、L869）。MDN 同一页写明默认 Lax 使用更宽松版本。建议总控：采纳本条，CH08 该段从「通过」改为 P2。
```

```
## ISSUE
ID：G02-0002
文件：chapters/08b-web-auth-permission.md ；chapters/13-api-testing.md ；chapters/16a-pytest-basics.md
章节：第 8 / 13 / 16 章
小节：8.12 Bearer Token；后续接口用 Bearer 的教学句
精确位置：08b L126「Bearer Token 来自 HTTP 认证实践（RFC 6750）」；L356「后续接口以 Authorization: Bearer 为准」；MiniShop 同时 `Set-Cookie` 同一串
原文：Bearer Token 来自 HTTP 认证实践（RFC 6750）。核心含义是：谁持有这个令牌，谁就可以用它访问被允许的资源。
问题等级：P2
问题类别：ACC / SEC
问题说明：RFC 6750 的核心语义（持有者即可用）教材写对了，但同一份 RFC 的安全要求被整段丢掉。§5 / §5.3：confidentiality protection MUST be applied using TLS；Clients MUST always use TLS (https) when making requests with bearer tokens；Implementations MUST NOT store bearer tokens within cookies that can be sent in the clear。教材一边点名 RFC 6750，一边用明文 HTTP 教 Bearer，并把同一 token 放进可明文发送的 Cookie（MiniShop `Set-Cookie: minishop_session=<token>; HttpOnly; Path=/`，无 Secure）。v1.0「不做 HTTPS」可以是教学范围，但不能让读者以为这就是 RFC 6750 的用法。
为什么有问题：面试「Bearer 要注意什么」若只答「放 Authorization 头」，会把规范禁令漏掉。把 token 放进非 Secure Cookie 正是 RFC 点名的反例。
依据：RFC 6750 §1（TLS mandatory to implement and use）、§5.3「Always use TLS」「Don't store bearer tokens in cookies」。
建议修改：8.12 加边界句：规范要求 Bearer 走 TLS，且不得把 Bearer 放进可明文发送的 Cookie。MiniShop v1.0 是本机 HTTP 教学妥协，禁止抄到生产或简历「已按 RFC 6750 落地」。
推荐替换文本：Bearer 的出示方式见 RFC 6750：`Authorization: Bearer <token>`，持有者即可用。同一份 RFC 还要求：请求必须走 TLS；不得把 Bearer 放进可明文发送的 Cookie。MiniShop v1.0 明确不做 HTTPS，登录同时下发 JSON token 与 HttpOnly Cookie，这是教学模型，不是规范推荐实现。
【Agent Disagreement】CHAPTER_08 将 8.12 判「RFC 6750 通过」（L498）。核的是「持有者即可用 / 不是 JWT」，没核 TLS MUST 与 Cookie 禁令。建议总控：采纳本条为 P2，不降 CH08 已有的分层正确结论。
```

```
## ISSUE
ID：G02-0003
文件：chapters/12a-sql-query.md
章节：第 12 章（上）
小节：12.4「查询部分下面通用」；12.7 LIKE 表
精确位置：L46；L149；L202–216
原文：本章查询语句尽量通用。……查询部分下面通用。 / `LIKE '%鼠标%'` | `%` 匹配任意长度，`_` 匹配单个字符
问题等级：P2
问题类别：ACC / SQL
问题说明：LIKE 的通配符在三引擎相同，**大小写不是**。SQLite 默认对 ASCII 字母大小写不敏感，对非 ASCII（教材例子「鼠标」）按大小写敏感；PostgreSQL 的 `LIKE` 大小写敏感，不敏感要用 `ILIKE`；MySQL 常见 `*_ci` 校对规则下 `LIKE` 不敏感。12.4 写「查询部分下面通用」，12.7 表只讲 `%` / `_`，章 Agent 把 LIKE 判通过（CH12 审计 T4）。GROUP BY 宽松已有 CH12-0012，LIKE 未单列。
为什么有问题：学生把 `name LIKE '%Mouse%'` 当可移植断言，SQLite/MySQL 能绿、PostgreSQL 空结果，会误报产品缺陷。课程明确三引擎都要认识。
依据：SQLite 文档 *LIKE operator*：only understands upper/lower case for ASCII by default；PostgreSQL 9.7.1 LIKE vs ILIKE；MySQL 8 pattern matching 随 collation。
建议修改：LIKE 行加一列「大小写因引擎而异」；练习保留中文例子（避开 ASCII 陷阱），另给一行 ASCII 对照警告。
推荐替换文本：`LIKE` 的 `%` / `_` 三引擎都能用。大小写不要当可移植预期：SQLite 对 ASCII 默认不敏感、对「鼠标」这类非 ASCII 敏感；PostgreSQL `LIKE` 敏感、不敏感用 `ILIKE`；MySQL 看列的 collation。缺陷里写引擎，不要只写「LIKE 没匹配」。
```

```
## ISSUE
ID：G02-0004
文件：chapters/01-software-testing-intro.md ；chapters/03-software-testing-classification.md
章节：第 1、3 章
小节：1.4 九特性清单；3.9 非功能测试点名 25010:2023
精确位置：01 L181–191；03 L119
原文：ISO/IEC 25010:2023 的产品质量模型包含九个质量特性。……4. 交互能力（Interaction Capability）……8. 灵活性（Flexibility）……9. 安全保障性（Safety）
问题等级：P2
问题类别：TERM / STD
问题说明：九个**英文现用名**本身是 2023 产品模型，没有把 Usability/Portability 当现行顶层名，这一点 CH01 判对。漏掉的是双轨：课程同时把 ISTQB CTFL v4.0.1 当参考资料。CTFL 4.0.1 的 ISO 25010 勘误（官方译本 release note 10.1.3）写明：2023 把 Usability→interaction capability、Portability→flexibility，并新增 Safety；**考试材料仍保留原名，只在 §2.2.2 括号补新名**。丹麦语官方译本 2.2.2 仍列 Brugervenlighed（Usability，also known as interaction capability）、Flytbarhed（Portability，also known as flexibility）、Personsikkerhed（Safety）。教材 1.4 把 2023 名写成唯一名单，3.9 只说「旧资料常称易用性」，没说「CTFL 试卷上的主名仍可能是 Usability/Portability」。口语「交互能力：用户是否容易理解和操作」更接近 2011 Usability / ISO 25019 quality-in-use；ISO 25010:2023 3.4 Note 2：Interaction capability is a prerequisite for usability，不是同义词。
为什么有问题：按教材背九个新名去答 CTFL 4.0.1 样本题，会与大纲主名对不上。这不是 2011 过时知识回潮，是「现行 ISO」和「现行考纲」没做映射。
依据：ISO/IEC 25010:2023 预览（Usability/Portability replaced；Safety added；3.4 interaction capability notes）；DSTB CTFL 4.0.1 丹麦语译本 §2.2.2 与 §10.1.3「Vi forbliver med originalen navne」。英文 4.0.1 §2.2.2 原句 【External Verification Required】（istqb.org PDF 本环境 SSRF 拦截）。
建议修改：1.4 清单保留 2023 名，加一行「CTFL 4.0.1 试卷仍可能用 Usability/Portability 作主名，括号里才是 2023 名」。口语不要把 Interaction Capability 直接说成「好不好用」。
推荐替换文本：产品质量模型（ISO/IEC 25010:2023）九个特性现用名如下。ISTQB CTFL 4.0.1 承认这次更名，但大纲正文仍以 Usability / Portability 为主名、括号补 Interaction capability / Flexibility，并增加 Safety。答题先看对方用的是 ISO 2023 还是 CTFL 主名。Interaction capability 是产品侧的交互属性，是 usability（使用成果）的前提，不要背成「就是易用性换了个词」。
```

### P3

```
## ISSUE
ID：G02-0005
文件：chapters/13-api-testing.md
章节：第 13 章
小节：13.10 幂等
精确位置：L309
原文：有的服务支持 `Idempotency-Key` 请求头：相同键的重复 POST 只生效一次。
问题等级：P3
问题类别：STD / OUTDATED
问题说明：「若文档写了就测、没写不要发明」这句纪律是对的。缺的是：到 2026-09，该头仍是 IETF HTTPAPI *Internet-Draft*（`draft-ietf-httpapi-idempotency-key-header`，datatracker 状态 Expired；-07 过期 2026-04-18，编辑稿声称延到 2027-01）。MDN 标 experimental / non-standard。教材把它写成「有的服务支持」的普通可选头，读者会以为已有 RFC。
依据：https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ ；MDN `Idempotency-Key`（status: experimental, non-standard）。
建议修改：加「IETF draft，不是 RFC；以对方 OpenAPI/文档为准」。
推荐替换文本：有的服务用 `Idempotency-Key`（IETF HTTPAPI draft，截至 2026-09 仍不是 RFC；Stripe 等产品各有各的键名）。文档写了再按文档测同键/换键/过期；没写不要发明该头当正式契约。
```

```
## ISSUE
ID：G02-0006
文件：chapters/09a-network-http-semantics.md
章节：第 9 章（上）
小节：9.7 QUERY 句；9.8 可缓存
精确位置：L261；L300
原文：HTTP 还有 QUERY（RFC 10008）等方法，用于带 Body 的安全且可缓存查询；……RFC 9110 把 GET、HEAD 和 POST 列为可缓存方法
问题等级：P3
问题类别：ACC / TERM
问题说明：两句各自对：RFC 10008（2026-06）定义 QUERY 为 safe + idempotent，响应可缓存；RFC 9110 §9.2.3 的可缓存方法仍是 GET、HEAD、POST。紧挨着读会背成「可缓存方法永远只有三个」，刚学的 QUERY 被 9.8 覆盖掉。QUERY 的缓存键还必须包含请求体，和 GET 不是同一套实现。
依据：RFC 9110 §9.2.3；RFC 10008（rfc-editor 2026-06-16 公告；独立打开摘要：safe and idempotent；缓存讨论见 RFC 正文）。章 Agent 已核 QUERY 号正确（CHAPTER_09 外部核查表），未核 9.8 名单与 9.7 的衔接。
建议修改：9.8 改成「RFC 9110 列出 GET/HEAD/POST；RFC 10008 把 QUERY 也定为可缓存，缓存键含 Body。实践中多数缓存仍只做 GET/HEAD」。
推荐替换文本：可缓存 ≠ safe。RFC 9110 列出 GET、HEAD、POST；2026 的 QUERY（RFC 10008）也是可缓存的安全方法，但缓存键要算上 Body，实现比 GET 贵。OPTIONS、TRACE 虽安全，响应默认不可缓存。
```

```
## ISSUE
ID：G02-0007
文件：chapters/08b-web-auth-permission.md
章节：第 8 章（下）
小节：8.11 Cookie 属性表
精确位置：L67
原文：`Expires` / `Max-Age` | 过期后浏览器不应再带上该 Cookie
问题等级：P3
问题类别：ACC
问题说明：两个属性都管过期，对。缺优先级：RFC 6265 同时出现时 **Max-Age 覆盖 Expires**。测试「改过期」只改其中一个，会看到另一个仍生效。
依据：RFC 6265 §5.2.2 / §5.3（Max-Age takes precedence over Expires）。
建议修改：表内加半句「同时出现时 Max-Age 说了算」。
推荐替换文本：`Expires` / `Max-Age`：过期后不应再带上。两个都写时，以 `Max-Age` 为准（RFC 6265）。
```

```
## ISSUE
ID：G02-0008
文件：chapters/09a-network-http-semantics.md
章节：第 9 章（上）
小节：9.7 PATCH 句
精确位置：L261
原文：PATCH（RFC 5789）用于部分更新，**不是** RFC 9110 方法表中的成员；其幂等性取决于应用如何实现，不能当成 GET 那样的默认保证。
问题等级：P3
问题类别：TERM
问题说明：前半句对：PATCH 不在 RFC 9110 §9.3 方法定义列表里。后半句把**方法属性**说成实现细节。RFC 5789：PATCH is neither safe nor idempotent。某次具体 PATCH 可以做成可重试（幂等键、If-Match），但不能改方法表上的「否」。
依据：RFC 5789 §2；RFC 9110 §9.3 列表（GET/HEAD/POST/PUT/DELETE/CONNECT/OPTIONS/TRACE）。
建议修改：改成「方法本身非安全、非幂等；若应用另做了幂等键，按文档测，不要改口说 PATCH 是幂等方法」。
推荐替换文本：PATCH（RFC 5789）做部分更新，不在 RFC 9110 的方法定义表里。规范把它定为非安全、非幂等。应用可以用条件请求或幂等键让某次 PATCH 可重试，那是应用契约，不是方法属性变成了「是」。
```

```
## ISSUE
ID：G02-0009
文件：chapters/11-linux.md
章节：第 11 章
小节：11.10 which
精确位置：L363
原文：`which curl` | curl 在哪 | 命令找不到、有多个版本
问题等级：P3
问题类别：TERM / macOS
问题说明：章 Agent 已覆盖 `free -h`、`ls --help`、`grep -R` vs `-r`、`pgrep -a`（CH11-000x）。漏了 `which`：macOS 默认 zsh 里 `which` 是 shell builtin，会打印 alias/function；Linux 排障常见的是 `/usr/bin/which` 只给磁盘路径。教材把 `which curl` 当「命令在哪」的通用写法，本课读者大量在 macOS 练习。
依据：zsh `which` builtin vs GNU `which(1)`；POSIX 更稳的是 `command -v`。
建议修改：写成 `command -v curl`，或注明 zsh `which` 可能打出 alias。
推荐替换文本：查可执行文件路径用 `command -v curl`（zsh/bash 都有）。zsh 的 `which` 是 builtin，可能打出 alias，不要把那一行当服务器上的真实二进制路径写进缺陷。
```

```
## ISSUE
ID：G02-0010
文件：chapters/18-performance-testing.md
章节：第 18 章
小节：18.3 吞吐量定义
精确位置：L123
原文：吞吐量是单位时间内完成的工作量，例如每秒成功请求数。
问题等级：P3（建议升级 CH18-0011 的同一点）
问题类别：TERM
问题说明：章 Agent CH18-0011 已写 JMeter Throughput = 全部样本 / 墙钟、含失败，但只标 P3，且说「未教错」。18.3 是 ⭐⭐⭐ 定义句，第一个例子就是「成功请求数」；JMeter Aggregate 同名列含 500。学生对照工具会以为教材和工具有一个在撒谎。这是口径冲突，不是「比 JMeter 更严」。
依据：Apache JMeter Glossary *Throughput*：number of requests / total time，含全部样本；正文 L131 才要求分开成功吞吐与错误率，来不及救定义句。
建议修改：定义句改成「单位时间完成的请求数」；立刻写「JMeter Throughput 列含失败，必须和 Error % 一起读；缺陷里写成功吞吐」。
推荐替换文本：吞吐量是单位时间内完成的请求数。JMeter Aggregate 的 Throughput 按**全部样本**算（含失败）。统计时分开写成功吞吐和错误率；每秒 1000 次全是 500 不是容量胜利。
【Agent Disagreement】建议把 CH18-0011 中 Throughput 子项从「未教错 / P3」升到与本条合并的 P2，或至少在 18.3 定义句改词。稳定性/压力测试资源削减两条可维持 P3。
```

---

## 3. 已由章节覆盖、故不重复的高风险点

V 模型四行表并非 CTFL 4.0.1 原文（CH02-0001）；测试级别口语四级 vs 大纲五级（CH03-0002）；评审六步 vs 五活动（CH04-0012）；error/defect/failure 主表正确（CH06）；405 `Allow` / 401 `WWW-Authenticate` 的 RFC MUST 被写成观察语气（CH09-0004）；Playwright 对照表 `getByRole` 不是 Python API（CH17-0004）；Timing 面板现行文案是 Waiting for server response（CH10-0003）；Cookie 罐让「无 Bearer」变 200/201（CH08-0001 / CH14-0001）；`grep -R` / `pgrep -a` 的 GNU vs BSD（CH11）；SQLite GROUP BY 同样宽松（CH12-0012）。

独立复核后**同意章 Agent、不新开 ISSUE**的项：七原则与 CTFL 4.0.1 同构（原则五正式名 tests wear out）；ISO 25010:2023 九个英文现用名未退回 2011；RFC 10008 QUERY（2026-06）存在且为 safe/idempotent；RFC 9110 方法表的 safe/幂等列（含 CONNECT 否/否、TRACE 是/是）正确；pytest 9.1.1 / `json=` / `timeout` / `type(x) is int` 避开 `True == 1` 均成立；JMeter 稳定线仍是 5.6.3（Java 8+，推荐 17）。

---

## 4. 分歧

| 对象 | 章 Agent | 本 Agent | 建议总控 |
| --- | --- | --- | --- |
| 08b SameSite 默认 = Lax | 通过，与 MDN 一致 | MDN 写明默认是更宽的 Lax-allow-unsafe；MiniShop Cookie 未设 SameSite | 采纳 **G02-0001** P2 |
| 08b RFC 6750 | 通过（持有者语义） | 同一 RFC 的 TLS MUST 与「禁止明文 Cookie 存 Bearer」未教 | 采纳 **G02-0002** P2；不推翻分层正确 |
| 12a LIKE 通用 | 通过 | 大小写三引擎不同 | 采纳 **G02-0003** P2 |
| 01/03 25010 名单 | 2023 现用名正确 | 名对，但与 CTFL 4.0.1「主名仍用 Usability/Portability」未映射 | 采纳 **G02-0004** P2；英文大纲原句需总控补开 PDF |
| CH18-0011 Throughput | P3「未教错」 | ⭐⭐⭐ 定义句已把吞吐说成成功数 | 升为 P2 或并入 **G02-0010** |
| CH03-0002 四级 vs 五级 | P2，因有「组织差异」免责 | 同意不升 P1：免责句成立，且 MiniShop 无外部系统 | 维持 CH03-0002 P2 |
| CH17-0004 getByRole | P1 | 同意，不升级、不重复 | 维持 |
| QUERY = RFC 10008 | 正确 | 独立复核正确 | 无分歧；只补 9.8 名单衔接（G02-0006） |

---

## 5. 结论

章级技术审计把 ISTQB 主线、HTTP 方法神话、Python/pytest 可抄 API、Playwright 语言绑、Linux 几条显眼方言都挡住了。Red Team 新找到的是**权威引用的半截**：SameSite、RFC 6750、ISO/CTFL 双名单、LIKE 大小写。没有发现「GET 比 POST 安全」「Cookie/Session/Token 三选一」「25010:2011 当现行」这类质量标准禁令回潮。

发布含义：不挡 MiniShop 主路径跑通；挡「按教材答 CSRF / Bearer / CTFL 质量特性 / 跨引擎 LIKE」这类岗位口试。建议总控先收 G02-0001～0004，其余 P3 可随下一轮勘误。

未核：ISTQB 英文 PDF 原文 §2.2.2 列表（G02-0004 EVR）；ISO 25010:2023 付费全文里 Testability 究竟挂在 Maintainability 还是 Flexibility（二手来源互相矛盾，**不作为 ISSUE**）。
