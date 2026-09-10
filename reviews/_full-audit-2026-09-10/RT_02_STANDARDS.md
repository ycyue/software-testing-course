# RT-02 SECOND PASS：HTTP / ISTQB / ISO

日期：2026-09-10  
Agent：SECOND PASS Red Team（HTTP / ISTQB CTFL 4.0.1 / ISO 25010:2023）  
范围：教材 `chapters/08*` `09*` `10*` `13*` `14*` 的状态码、safe/幂等/可缓存、Host、Content-Length、401/403/405 RFC MUST；全书 ISTQB 七原则、测试级别、V 模型、confirmation vs validation、error/defect/failure、探索性、静态测试；ISO/IEC 25010:2023 九特性译名/子特性。  
硬约束：未改教材。不采信第一轮「主课正确」。只报 MASTER / Global-02 / 章审计**没有的**问题，或第一轮**判错/放过/明确不立案**的问题。

结论先说：**没有新的 P0。** 第一轮挡住了 GET/POST 机密性神话、405 Allow / 401 WWW-Authenticate 观察语气、V 模型四行表非 4.0.1 原文、级别 4 vs 5、SameSite / RFC 6750 TLS。本轮新问题是同一类「引用了权威却没把 MUST / 条款编号读完」：

1. **Host**：章审计判「对应 RFC 9112 / §7.2，OK」，但 HTTP/1.1 缺 Host / 多个 Host / 非法 Host 是 **MUST 400**，教材只写「必须」。  
2. **Content-Length**：09B 写成「不一致时可能被拒绝」；RFC 9112 对非法 CL 是 **MUST 当不可恢复错误，请求 MUST 400 并关连接**。与 CH13-0004（纸面报文漏写该头）不是同一条。  
3. **ISTQB FL-1.2.3** 是四个词：root cause / error / defect / failure。第一轮写「主表正确」，表只有三格。  
4. **原则三** CTFL 原文要求静态**和**动态都尽早；教材 ⭐⭐⭐ 段只落到评审。  
5. **ISO 25010:2023 Testability** 仍挂在 **Maintainability 3.7.5**（第一轮因二手来源矛盾明确不立案）。arc42 把它挂到 Flexibility 是错的。第 4 章「需求可测试性」是另一概念。  
6. **Security / Safety 中文**：九个英文现用名仍然对；JIS 采用本把 Safety 译成「安全性」、Security 保持「セキュリティ」。教材「信息安全性 / 安全保障性」两个都带「安全」，且口语把 Security 缩成账号密码权限，2023 已加 Resistance。

第一轮已报、本轮独立复核后**同意、不重开**的项见第 3 节。

---

## 1. 方法

| 步骤 | 做法 |
| --- | --- |
| 抽教材断言 | 通读 09A/09B 方法表、状态码表、头字段表；08B 401/403 门牌；13.9–13.12；14 状态码断言。通读 01.4–01.5、02.4/02.7、03.4/03.8、04A 4.3/4.8、06A 6.1。 |
| 对照第一轮 | `MASTER_AUDIT.md` D5/D11/Final Red Team 表；`GLOBAL_02_TECH_REDTEAM.md`；CH01/02/03/04/06/08/09/13 ISSUE。已有：mouse、Content-Length 漏写、HTTP/1.0、Cookie 回退、SameSite Lax-allow-unsafe、6750 TLS、V 不画 V、级别表、405/401 MUST 观察语气、QUERY 名单、PATCH 方法属性、Idempotency-Key draft、25010/CTFL 双名单。 |
| 权威原文 | 本机 `curl` RFC 9110 / 9112 纯文本；ISTQB CTFL Syllabus v4.0.1 PDF（istqb.org，2024-09-15，78 页，pypdf 抽取 §1.2.3 / §1.3 / §2.1.2 / §2.2.1–2.2.3 / §3.1.3 / §4.4.2）；JIS X 25010（ISO/IEC 25010:2023 日文采用稿）条款 3.4 / 3.6 / 3.7.5 / 3.8 / 3.9 与图 2。 |
| 不重复规则 | 同一 RFC MUST、同一 CTFL 句子、同一九特性英文名单，只在第一轮放过或判错时升级。 |

---

## 2. 新发现

### P0

无。

### P1

无。下列 P2 会让口试/考证背半截 MUST 或把两个「可测试性」焊成一个，但不会让 MiniShop 主路径测反。

### P2

```
## ISSUE
ID：RT02-0001
文件：chapters/09a-network-http-semantics.md ；chapters/09b-http-message-observe.md
章节：第 9 章
小节：9.5 Host 句；9.11 请求头表
精确位置：09A L204；09B L126
原文：`Host` 在 HTTP/1.1 中是必须的请求头，用来说明要访问哪一个主机。它和 URL 里的 host 对应，但出现在报文头里。 / `Host` | HTTP/1.1 的目标主机 | 是否打到正确环境
问题等级：P2
问题类别：HTTP / STD
问题说明：第一轮 CHAPTER_09 把 Host 判「对应 RFC 9112 / RFC 9110 §7.2，OK」（审计表约 L422）。核到的是「HTTP/1.1 要带 Host」，没核服务端 MUST。RFC 9112：A client MUST send a Host header field in all HTTP/1.1 request messages；A server MUST respond with a 400 (Bad Request) to any HTTP/1.1 request that lacks a Host header field and to any request that contains more than one Host header field line or a Host header field with an invalid field value。RFC 9110 §7.2：Host = uri-host [ ":" port ]；user agent MUST generate Host unless it sends :authority（HTTP/2、HTTP/3）。教材把「必须」写成词汇表，把 Host 说成 URL 里的 host，漏了非默认端口（MiniShop 例子 `Host: 127.0.0.1:8765` 才是完整 authority）。这与 CH09-0004 把 405 Allow / 401 WWW-Authenticate 的 MUST 写成「或含 / 时常」是同一类半截引用；Host 那一行被放过了。
为什么有问题：接口测试手写 HTTP/1.1 或打错虚拟主机时，规范预期是 400，不是「环境不对就换 URL」。HTTP/2 抓包看不到 Host、只看到 :authority，按教材会报「缺 Host」。MiniShop 实装是 HTTP/1.0，缺 Host 的行为不能拿来当 HTTP/1.1 规范结论——必须像 401 缺挑战头那样分开写。
依据：RFC 9112（本机 rfc-editor 纯文本）Host 段；RFC 9110 §7.2 Host = uri-host [ ":" port ]。CHAPTER_09 外部核查表将 Host 标 OK。
建议修改：09.5 / 9.11 写成「HTTP/1.1 客户端 MUST 发 Host，值等于 authority（主机 + 非默认端口）。源服务器对缺 Host / 多个 Host / 非法 Host MUST 回 400。HTTP/2、HTTP/3 常用 :authority。MiniShop v1.0 状态行是 HTTP/1.0，不要用本机缺 Host 的结果当 RFC 结论。」
推荐替换文本：`Host` 是 HTTP/1.1 的强制请求头，值是目标 URI 的 authority：主机名，外加非默认端口（MiniShop 是 `127.0.0.1:8765`，不是只写 host）。源服务器对缺了、写了两个、或值非法的 HTTP/1.1 请求 **必须** 回 400（RFC 9112）。HTTP/2/3 里这个信息常在 `:authority`。MiniShop 当前是 HTTP/1.0，缺 Host 的实测不能写成「已符合 RFC」。
【Agent Disagreement】CHAPTER_09 放过 Host。建议总控：采纳本条为 P2，与 CH09-0004 并列，不降「Host 字段存在」的正确结论。
```

```
## ISSUE
ID：RT02-0002
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：9.11 请求头 `Content-Length`
精确位置：L130
原文：`Content-Length` | Body 长度 | 与实际 Body 不一致时可能被拒绝
问题等级：P2
问题类别：HTTP / STD
问题说明：不是 CH13-0004（13.12 纸面登录报文漏写 Content-Length，裸 TCP 读不到 Body）。09B 是在教这个头的语义，却把成帧错误写成现象。「可能被拒绝」对应不了 RFC MUST。RFC 9112 §6.3：无 Transfer-Encoding 且 Content-Length **非法**（非数字、多个不同值）→ 报文成帧无效，接收方 MUST 当不可恢复错误；若在请求里，服务器 MUST 回 400 并关闭连接。合法 CL 但字节未收齐：MUST 当不完整并关连接。RFC 9110 §8.6：方法对 Body 有语义时（如 POST），用户代理 SHOULD 发送 Content-Length（即使是 0）。RFC 9110 §15.5.12：服务器可以 411 Length Required 拒绝没有 CL 的请求。教材一行把非法 CL、长度不够、漏写 CL 揉成「可能」。
为什么有问题：学生用手写报文测 MiniShop / 网关时，非法 CL 应预期 400 关连接，不是「看看会不会过」。漏写 CL 已经在第 13 章把登录打成 400 missing field；第 9 章先把规范说成运气问题，后面那次失败会被理解成「实现怪癖」。
依据：RFC 9112 §6.3 第 5、6 步（本机纯文本）；RFC 9110 §8.6、§15.5.12。CHAPTER_09 请求头表未单列 CL MUST。
建议修改：拆三句：非法 CL → MUST 400 并断开；合法 CL 字节不够 → 不完整、关连接；POST 有 Body 应带 CL（curl 会自动加，手写不会）。MiniShop `_read_json` 用 `Content-Length or 0`，漏写等于没有 Body。
推荐替换文本：`Content-Length` 给出 Body 的八位组长度，用来成帧（RFC 9112）。头本身非法（不是同一个非负整数）时，HTTP/1.1 接收方必须当不可恢复错误：请求则 400 并关连接。长度合法但字节没收齐，必须当不完整消息并断开。POST 有体时应带这个头；curl 会代写，按第 13 章纸面形状手敲 TCP 不会。MiniShop 读的是 `Content-Length`，写成 0 或省略就等于没有 JSON 体。
```

```
## ISSUE
ID：RT02-0003
文件：chapters/06a-bug-management.md
章节：第 6 章（上）
小节：6.1 错误、缺陷与失效
精确位置：L37–L46「ISTQB 的常用区分」三行表
原文：错误（Error / Mistake）/ 缺陷（Defect / Fault / Bug）/ 失效（Failure）。关系通常是：人的错误可能把缺陷引入……缺陷在特定条件被执行或使用时，才可能表现为失效。
问题等级：P2
问题类别：TEST / TERM
问题说明：三格关系与 Glossary 同向，第一轮 CHAPTER_06 写「主表正确」、Global-02 写「error/defect/failure 主表正确」因此不新开 ISSUE。CTFL **4.0.1 可考 LO 是四个词**。Keywords 与 FL-1.2.3（K2）：Distinguish between **root cause, error, defect, and failure**。§1.2.3 标题即 “Errors, Defects, Failures, and Root Causes”。原文：A root cause is a fundamental reason for the occurrence of a problem (e.g., a situation that leads to an error). Root causes are identified through root cause analysis… further similar failures or defects can be prevented… by addressing the root cause。教材表头自称「ISTQB 的常用区分」，却把 4.0.1 第四项拿掉。后文「不是每一次异常都是产品缺陷」列了数据/环境/重复单，仍没有「根因」这个术语。
为什么有问题：考证/面试「error 和 root cause 有什么区别」按本章会答成三层链。根因是导致人犯错的那条更早原因（工期、培训、环境），不是缺陷本身。第一轮判「主表正确」相对于三词链成立，相对于 CTFL 4.0.1 LO **过宽**。
依据：ISTQB CTFL Syllabus v4.0.1（本机官方 PDF）p.14 Keywords；p.14 FL-1.2.3；p.17 §1.2.3 全文。CHAPTER_06 外部核查表只核了三词。
建议修改：表加第四行「根因（Root Cause）」；链写成 根因 → 错误 → 缺陷 →（可能）失效。注明不是每条失效都能追到单一根因。
推荐替换文本：ISTQB CTFL 4.0.1 要区分四个词：根因（导致人犯错的根本理由）→ 错误（人的不正确判断或动作）→ 缺陷（工作产品里的瑕疵）→ 失效（执行时偏离预期）。测试当场看到的常常是失效；缺陷报告帮团队定位缺陷；根因分析用来减少同类再发。环境辐射等也可以不经过「人的错误」直接造成失效。
【Agent Disagreement】CHAPTER_06 / Global-02「主表正确」。建议总控：三词链保留为对；缺 root cause 单列本条 P2，不把 6.1 整节打成教反。
```

```
## ISSUE
ID：RT02-0004
文件：chapters/01-software-testing-intro.md
章节：第 1 章
小节：1.5 原则三；常见错误 2
精确位置：L229–L233；L375–L376
原文：尽早测试可以节省时间和成本。……所以测试应尽早介入开发生命周期。需求和设计阶段的评审就是静态测试的一部分。 / 修正：需求、设计阶段就可以通过评审等静态测试活动提前介入。
问题等级：P2
问题类别：TEST / STD
问题说明：原则三标题「尽早测试可以节省时间和成本」与 CTFL 4.0.1 第 3 条 Early testing saves time and money 同构。漏的是原文下一句：To find defects early, **both static testing and dynamic testing** should be started as early as possible。教材 ⭐⭐⭐ 段和「常见错误 2」只把尽早落到评审/静态。动态测试「一旦有可执行对象就尽早跑」没有出现。第一轮 CH01 原则三只报了空搜索草稿标签（CH01-0007），未核这条原文。
为什么有问题：学生会把原则三背成「尽早 = 做评审」。CTFL 样本题可以考「代码可运行后还要尽早动态测」。第 2 章左移也不等于「只把静态前移」。
依据：CTFL v4.0.1 §1.3 原则 3（本机 PDF p.18）。
建议修改：原则三补半句「有可执行对象时，动态测试也要尽早，不必等全部编码结束」。常见错误 2 的修正同步。
推荐替换文本：尽早测试节省时间和成本（CTFL 原则三）。需求、设计阶段用评审等静态测试拦截缺陷，避免后面的工作产品被污染；一旦有可运行的组件或接口，动态测试也要尽早开始，而不是等开发全部结束。MiniShop 数量规则在需求评审里就能问清，有实现后用 `qty=10/11` 尽早执行。
```

```
## ISSUE
ID：RT02-0005
文件：chapters/01-software-testing-intro.md ；chapters/04a-requirements-static-testing.md
章节：第 1、4 章
小节：1.4 九特性（无子特性）；4.8 需求可测试性
精确位置：01 L181–202；04A L200–L225
原文：ISO/IEC 25010:2023 的产品质量模型包含九个质量特性。……7. 可维护性（Maintainability） 8. 灵活性（Flexibility）…… / 可测试性意味着要求能够用可行的方法验证，并能判断通过或失败。
问题等级：P2
问题类别：TERM / STD
问题说明：第一轮 MASTER「九特性名单正确」；Global-02 因「Testability 究竟挂 Maintainability 还是 Flexibility，二手来源互相矛盾」**明确不作为 ISSUE**。本轮用 JIS X 25010（ISO/IEC 25010:2023 日文采用，条款编号与 ISO 相同）可以结案：**Testability 仍是可维护性子特性 3.7.5**，不在灵活性 3.8。图 2 把「テスト可能性，試験性」画在保守性（maintainability）下；对照表写 3.7.5 相对 2013「试验性」仅加片假名，3.8 才是由移植性更名为灵活性（适应/扩展/安装/置换，**无** Testability）。arc42 把 Testability 挂到 Flexibility，与官方条款冲突，不应再当「互相矛盾」而搁置。教材两边的缺口是：（1）九特性不列子特性，Testability 从未出现；（2）第 4 章 ⭐⭐⭐「可测试性」讲的是**需求/测试基础能不能写成可判定规则**（CTFL test analysis：evaluate testability of the test basis），不是 ISO 产品特性「产品是否容易建立并执行客观测试」。两个英文词都叫 testability，中文都叫可测试性。
为什么有问题：学生会以为可测试性是第 4 章自造词，或反过来以为 ISO 九特性里漏了一项。面试「可维护性包含什么」按教材只能说「好不好改」，说不出可测试性/模块性。把「登录速度要快不可测」答成「产品 Testability 差」是张冠李戴。
依据：JIS X 25010（ISO/IEC 25010:2023）3.7.5「テスト可能性，試験性（testability）」位于 3.7 保守性；3.8 柔軟性子特性为适应/扩展/安装/置换；图 2。CTFL v4.0.1 §1.4.1 Test analysis：The test basis and the test object are also evaluated to identify defects… and to assess their testability。Global-02「未核 / 不作为 ISSUE」。
建议修改：1.4 可维护性口语加「含是否容易设计并执行测试（Testability，子特性，不是第九个顶层特性）」。4.8 开头加「这里说的是需求写得清不清，不是 ISO 25010 产品质量模型里挂在可维护性下面的那条 Testability」。不要按 arc42 写成灵活性子特性。
推荐替换文本：ISO/IEC 25010:2023 可维护性（Maintainability）的子特性包括模块性、可复用性、可分析性、可修改性和**可测试性（Testability）**。灵活性（Flexibility，由 2011 可移植性更名）是适应、可伸缩、可安装、可替换，**不含** Testability。第 4 章「需求可测试」问的是这条要求能不能写成可观察的通过/失败标准，对象是需求句子，不是「代码好不好测」。
【External Verification Required】未购买 ISO 英文付费全文；条款编号与图结构以 JIS 采用本为准（与 ISO 2023 对应）。若总控要法庭级页码，需打开 ISO/IEC 25010:2023(E) §3.7.5。
```

```
## ISSUE
ID：RT02-0006
文件：chapters/01-software-testing-intro.md ；chapters/03-software-testing-classification.md
章节：第 1、3 章
小节：1.4 教学译名 + 口语六条；1.4 常见错误 5；3.9 非功能
精确位置：01 L188–L202、L385；03 L119
原文：6. 信息安全性（Security）……9. 安全保障性（Safety）。这里的 Security 与 Safety 不是重复概念。……信息安全性：账号、密码、数据和权限是否得到保护。 / 修正：还要考虑性能、可靠性、安全性、兼容性和交互能力。
问题等级：P2
问题类别：TERM / STD
问题说明：九个**英文**现用名正确，MASTER Final Red Team 表这条维持。第一轮 CH01-0024 把译名只标 P3（「保障像 QA 的 assurance」），CH01-0028 标口语「安全性」冲淡区分。本轮升级的是官方译名对照和子特性，不是再争英文名单。JIS X 25010（2023 采用）顶层对译是：Security = **セキュリティ**（不译成「情報安全」），Safety = **安全性**。中文资料分裂成三套：GB/T 25000.10-2016 把 Security 叫「安全性」；JIS/部分 2023 稿把 Safety 叫「安全性」或「无害性」；教材自造「信息安全性 / 安全保障性」。两个教学译名都含「安全」，「保障性」更像 security assurance，和 Safety（避免对人、财产、环境的不可接受风险；JIS 3.9）不是同一词。口语六条把 Security 说成「账号、密码、数据和权限是否得到保护」，只覆盖机密性/访问控制。2023 Security 子特性在 2011 的机密/完整/不可抵赖/可核查/真实性之外，**新增 Resistance（耐攻击性）**，定义含防御恶意攻击模式。常见错误 5 用光秃「安全性」，刚建立的二分立刻塌回一个汉字。3.9 写「信息安全性」与 1.4 教学译法一致，但同样没有 Resistance。
为什么有问题：学生无法稳定回答「Security 和 Safety 中文怎么说」。按教材去读 JIS/部分中文稿，会以为「安全性」是 Security，其实官方采用本把「安全性」给了 Safety。按口语去测 Security，会漏掉完整性、抗抵赖、抗攻击。这不是把 2011 可用性/可移植性当成 2023 顶层名（那点第一轮判对），是译名和子特性仍停在信息安全常识。
依据：JIS X 25010 3.6 セキュリティ（含 3.6.6 耐攻击性）；3.9 安全性（safety）；4.1 九特性日文名单「…セキュリティ、保守性、柔軟性及び安全性」。ISO 预览：Safety 子特性 operational constraint / risk identification / fail safe / hazard warning / safe integration。CH01-0024 仅 P3。
建议修改：保留英文名。中文对译改成「Security（信息安全，不是 Safety）」「Safety（人身/功能安全；日文采用本作「安全性」）」。口语不要再用光秃「安全性」。Security 补半句「还包括完整、抗抵赖、抗攻击，不只是密码」。
推荐替换文本：Security 与 Safety 不是同一个「安全」。Security（教材可写「信息安全」）保护信息和访问授权，2023 还加了抵抗恶意攻击（Resistance）。Safety（人身/功能安全）关注会不会对人、财产或环境造成不可接受的风险；医疗、汽车、工控才常单独立项。不要把两个都译成带「保障/安全」的近义词。GB/T 旧稿用「安全性」指 Security，JIS 2023 采用本用「安全性」指 Safety——答题先写英文。
【Agent Disagreement】CH01-0024 P3「教学区分是对的，保持即可」。建议总控：英文名单仍正确；中文对译与 2023 Resistance 升为 P2，与 G02-0004（CTFL 考纲主名 Usability/Portability）并列，不推翻「未把 2011 可用性当现用顶层名」。
```

### P3

```
## ISSUE
ID：RT02-0007
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：9.10 常用码 307/308、304；9.10 2xx 类
精确位置：L86；L99–L100
原文：2xx | 成功收到并理解，通常已接受处理；307 / 308 | 保持方法的重定向 | 后继请求保持原方法，POST 可能仍是 POST，Body 也可能还在；304 | 缓存再验证成功，不一定是「接口没数据」
问题等级：P3
问题类别：HTTP / TERM
问题说明：行标题「保持方法的重定向」方向对。测试注意把 RFC MUST 写成「可能」。RFC 9110 §15.4 总注：307 与 308 被加入就是为了 unambiguous method-preserving redirects；§15.4.8 对 307：user agent MUST NOT change the request method if it performs an automatic redirection。教材「POST 可能仍是 POST，Body 也可能还在」是观察语气。304：RFC 9110「A 304 response is terminated by the end of the header section; it cannot contain content or trailers。」与 204 同一条硬约束。CH09-0011 已打 204「部分 204」，304 行没写无体。2xx 类定义 RFC 是 received, understood, **and accepted**，教材加「通常」把 accepted 变成或然。
为什么有问题：和 CH09-0004 同类，但 307 标题已经写了「保持方法」，伤害小于 405 Allow。304 有体会被学生当成「缓存接口还是返回了数据」。
依据：RFC 9110 §15.3、§15.4 总注、§15.4.5、§15.4.8（本机纯文本）。§15.4.9 的 308 正文未再重复 MUST NOT 一句，但 15.4 总注把 308 与 307 并列定义为 method-preserving。
建议修改：307/308 改成「自动重定向不得改方法；POST 仍是 POST，体一起重放」。304 加「按规定没有消息体」。2xx 去掉「通常」。
推荐替换文本：307/308：保持方法的重定向（RFC 9110）。自动跳转时不得把 POST 改成 GET；请求体随方法一起走。304：再验证命中，**没有**消息体，不是「接口空数据」。2xx：请求已被收到、理解并接受；200 仍要看 Body 是否业务成功。
```

```
## ISSUE
ID：RT02-0008
文件：chapters/04a-requirements-static-testing.md ；chapters/03-software-testing-classification.md
章节：第 3、4 章
小节：3.1 静态/动态；4.3 静态测试与动态测试
精确位置：03 L87–L91；04A L63
原文：静态测试……通过评审、静态分析等方式检查……发现问题。动态测试需要执行被测对象并观察行为。
问题等级：P3
问题类别：TEST / TERM
问题说明：定义「不执行 / 要执行」正确，第一轮放过。CTFL 4.0.1 §3.1.3 还钉死一条考试常用差：Static testing finds defects directly, while dynamic testing causes failures from which the associated defects are determined through subsequent analysis。静态测试不能造成失效。教材 4.3 动态侧只写「观察行为」，3.1 动态例子写「检查页面提示和接口状态码」，都没接到第 6 章才出现的「失效」。06A「测试人员直接观察到的常常是失效」也不回指：那只适用于动态测试。
为什么有问题：原则一/测验用「缺陷 vs 失效」已经打架（CH01-0027）。静态章再不声明「静态直接找缺陷、动态先看到失效」，三个词会在第 4 章和第 6 章各讲各的。
依据：CTFL v4.0.1 §3.1.3（本机 PDF p.34）；§1.1.2 Testing and Debugging：static testing directly finds defects, and cannot cause failures。
建议修改：4.3 表下加一句对照。不必提前展开 6.1 全表。
推荐替换文本：静态测试不执行被测对象，直接在工作产品里发现缺陷（评审意见、静态分析告警），它不会造成失效。动态测试执行对象，测试人员当场看到的是行为/失效，再分析背后的缺陷。二者互补，不是「不运行就不算测试」。
```

---

## 3. 第一轮已覆盖、本轮独立复核后不重开

| 断言 | 本轮核验 | 处置 |
| --- | --- | --- |
| GET safe / 幂等，POST 否 | RFC 9110 §9.2.1–9.2.2；方法表 GET 是/是、POST 否/否 | 同意 MASTER「正确」。不重开。 |
| 可缓存 ≠ safe；9110 列为 GET/HEAD/POST | RFC 9110 §9.2.3 | 同意。QUERY 衔接已是 G02-0006。 |
| PATCH 非 9110 成员；方法本身非幂等 | RFC 5789；G02-0008 | 不重开。 |
| 405 MUST `Allow`；401 MUST `WWW-Authenticate` | RFC 9110 §15.5.6 / §15.5.2 / §11.6.1 | 同意 CH09-0004。本轮只补 **Host / Content-Length** 同类 MUST。 |
| 403 无额外 MUST 头；可用 404 隐藏存在 | RFC 9110 §15.5.4 MAY 404 | 08B/13 已写。CH08-0014 存在性。不重开。 |
| 204 不能有消息体 | RFC 9110 §15.3.5 | CH09-0011。304 见 RT02-0007。 |
| 纸面 HTTP/1.1 vs 实装 HTTP/1.0；13.12 漏 CL | RFC 9112 成帧 | CH09-0002 / CH13-0004。不把漏写头再报一次。 |
| Cookie 回退、SameSite Lax-allow-unsafe、RFC 6750 TLS | 第一轮 G02-0001/0002、CH08-0001 | 按任务不重复。 |
| 七原则名称与 4.0.1 同构；原则五 tests wear out | PDF §1.3 七条英文标题 | 同意 Global-02。原则一「已知问题」仍是 CH01-0008。原则三尽早动态见 RT02-0004。 |
| V 模型四行表非 4.0.1 原文；§2.1.2 只要成对活动 | PDF §2.1 仅把 V-model 当 sequential 示例 | 同意 CH02-0001。MASTER D5「不强制画 V」本轮不推翻、不升级。 |
| 测试级别口语四级 vs 大纲五级 | PDF §2.2.1 五个级别原文已核对 | 同意 CH03-0002。不重开。 |
| confirmation testing ≠ validation | PDF §2.2.3 confirmation = 原缺陷修好；§1.3 原则七要做 validation；§2.2.1 验收 focuses on validation | 同意 CH02-0009。不重开。 |
| 探索性定义 | PDF §4.4.2 simultaneously designed, executed, and evaluated | 同意 CH03-0008。章程/session 仍是缺口，不重复。 |
| 评审五活动 vs 教材六步 | PDF §3.2.2 五项 | 同意 CH04-0012。 |
| 九特性英文现用名未退回 2011 | JIS 4.1 九个：功能适合 / 性能效率 / 兼容 / 交互 / 可靠 / 安全(Security) / 可维护 / 灵活 / Safety | 同意 MASTER。译名与 Testability 见 RT02-0005/0006。 |
| CTFL §2.2.2 考纲主名 Usability/Portability | **英文 PDF 已打开**：Usability (also known as interaction capability)；Portability (also known as flexibility)；另列 Safety | **关闭 G02-0004 的 EVR**。ISSUE 本身仍成立，不重开新 ID。 |

---

## 4. 第一轮判对、本轮维持的 ISO 点

- 未把 Usability / Portability 写成 2023 顶层现用名。  
- Safety 是 2023 新增顶层特性。  
- 交互能力口语「好不好用」接近 2011 Usability / ISO 25019 quality-in-use：G02-0004 已报；JIS 3.4 注 2「インタラクション容易性はユーザビリティの前提条件」独立印证。不重开。  
- Compatibility 口语 = 浏览器矩阵 vs ISO 共存/互操作：CH03-0011。不重开。

---

## 5. 分歧（相对第一轮）

| 对象 | 第一轮 | 本 Agent | 建议总控 |
| --- | --- | --- | --- |
| 09A/09B Host | 通过 | HTTP/1.1 缺/多/非法 Host **MUST 400**；Host 是 authority 含端口 | 采纳 **RT02-0001** P2 |
| 09B Content-Length「可能被拒绝」 | 未单列（CH13-0004 只打第 13 章漏写） | 非法 CL MUST 400 关连接 | 采纳 **RT02-0002** P2；不要并进 CH13-0004 |
| 06A error/defect/failure | 主表正确 | 4.0.1 LO 是四词，缺 root cause | 采纳 **RT02-0003** P2 |
| 原则三 | 只报草稿标签 | 原文要求静态**和**动态尽早 | 采纳 **RT02-0004** P2 |
| Testability 挂哪 | 二手矛盾，不立案 | JIS/ISO 条款 3.7.5 在可维护性；arc42 挂灵活性为误 | 采纳 **RT02-0005** P2；英文付费页码可选 EVR |
| Security/Safety 中文 | 名单正确；译名 P3 | JIS 把「安全性」给 Safety；口语缩成账号密码；缺 Resistance | 把 CH01-0024 升到与 **RT02-0006** 合并的 P2 |
| G02-0004 英文 §2.2.2 EVR | SSRF 拦住 PDF | 本机已下载 CTFL 4.0.1，名单属实 | **关闭 EVR**，保留 P2 双轨映射 |
| V 模型不画 V | MASTER：MODIFY，不强制字形 | 同意。ISTQB 要成对关系 | 不升级 |

---

## 6. 结论

第二遍没有把第一轮的「主课没教反」推翻：GET 仍是 safe/幂等，九个英文现用名仍是 2023，401/403 方向仍对，error→defect→failure 链仍对。新找到的是 **MUST 和条款编号的另一半**：Host 400、Content-Length 成帧、CTFL 根因、原则三的动态半句、Testability 挂可维护性、Security/Safety 中文对译。

发布含义：不挡 MiniShop 主路径。挡的是「按教材答 HTTP/1.1 缺 Host 会怎样 / 非法 Content-Length 会怎样 / ISTQB 四个词 / ISO 可测试性在哪一层」。建议总控先收 RT02-0001～0006；0007–0008 可随勘误。

未核：ISO/IEC 25010:2023 英文付费 PDF 的 §3.7.5 页码（JIS 采用本已给出条款号与图）；RFC 9110 §15.4.9 的 308 正文未重复 MUST NOT，本条 307/308 结论依赖 §15.4 总注的 method-preserving 定性。
