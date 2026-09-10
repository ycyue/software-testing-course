# RT-04 Second Pass：绝对化 / 疑似编造 / 外链 / 跨章 / MiniShop 闭环 / 截图时效 / 岗位

- 角色：SECOND PASS Red Team
- 日期：2026-09-10
- 对照：`MASTER_AUDIT.md`、G01/G05/G06/G07/G08、各 `CHAPTER_XX_AUDIT.md`
- 硬约束：未改教材。只报**新问题**或**第一轮误判**。质量标准六条禁止项、Git/Jira/Postman GUI、所属者 200、Cookie jar、空搜索图、`git-scm.com/doc` 跳 `/docs`、Chrome 152 Timing、冒烟「加入购物车」——已在总表或章报里的，不重复开单。
- 问题前缀：`RT04-000N`

---

## 0. 方法与覆盖

| 项 | 做法 | 结果 |
| --- | --- | --- |
| 绝对化用语 | `chapters/*.md` 检索：一定/必须/只能/所有/永远/完全/企业都是/实际工作就是 | 绝大多数是否定句、星级或 ISTQB 原则；六条禁止项仍无正说 |
| 无出处数字/模型 | 检索 %、通常、企业都、ISTQB 规定、行业惯例、研究表明 | 未发现新的「通常 80%」「ISTQB 规定必须 + 无条款」 |
| 外链 | 抽取 `chapters/` + `README.md` + `docs/LEARNING.md` + 第 22 章 22.6 全部 `https://`；`curl -L` + 不跟随的 `-I` | 55 个 https；`LEARNING.md` 无外链 |
| MiniShop 闭环 | 读 `server.py` `_create_order`、`frontend/index.html`/`app.js`、PRD、OpenAPI、第 3/6/9 章按钮与流程句 | 下单**不读、不清** `cart_items`；前端下单后不 `refreshCart` |
| 截图 | 打开 `09-pytest-report.png`、`ch14-*.png`、`ch18-jmeter-parts.png`、`08-network-log.png`；对照 PyPI pytest-html 4.2.0、JMeter 5.6.3 | pytest-html 版本未过时；无 Postman/JMeter GUI 假图 |
| 岗位 | 对照 G08 已报 Git/Jira/Postman GUI/年限/ATS 同义词，另找入职数据/验证码缺口 | 见 RT04-0010、RT04-0011 |

**未检查 = 0**（范围内）。本机 Python `ssl` 缺根证书，外链一律 `curl`（非 urllib）。

---

## 1. 负向结论（第一轮已对，不升新单）

1. **质量标准六条错误绝对化**：全书仍未写成正说。命中的「永远 / 所有公司 / 必须等开发」几乎都在「错误 N」或测验干扰项里。
2. **「企业都是 / 实际工作就是」**：`chapters/` 零命中正说。
3. **pytest-html**：仓库钉 4.2.0，PyPI **latest 仍是 4.2.0**。`09-pytest-report.png` 页眉 `pytest-html v4.2.0`，**就是**所标工具，不是 JUnit/Allure 冒充。
4. **Postman / JMeter**：没有工具 GUI 截图。`ch14-workspace` / `ch14-token-relay` / `ch18-jmeter-parts` 是教学卡片，caption 写明未点 GUI / 未安装。不构成「过时截图」。JMeter 官网当前包仍是 **5.6.3**。
5. **`git-scm.com/doc`**：本轮仍 200、body 548B、canonical `/docs`。CH22 P3 成立，不重开。
6. **Postman 旧路径 308、`schema.getpostman.com` 301**：CH14-0015 已报，仍能跳。
7. **下单不走购物车（实现）**：G06-0004 / CH19-0017 / CH13-0020 已报项目侧。本轮只补**教材第 3 章把假闭环写成系统测试例子**（RT04-0006）。
8. **第 3 章答案「加入购物车 / 提交订单」**：M-P1-02 / CH03-0001 / G04-0001。本轮只补 **06B 答案「加购」**（RT04-0007）。

---

## 2. 外链实测总表（新问题加粗）

`curl -L --max-redirs 8`，UA=`Mozilla/5.0 course-audit`，2026-09-10。教学用 `*.example.test` 不请求。

| URL | 终态 | 备注 |
| --- | --- | --- |
| 绝大多数官方文档（MDN/Chrome/Python/pytest/RFC-html/ISTQB 页与 PDF/JMeter/Playwright/Selenium/GitHub Actions/WHATWG/curl.se 等） | 200 | 站点内规范化跳转（pytest.org→/en/stable/ 等）不报 |
| `https://spec.openapis.org/oas/v3.0.3` | **200**，398758 B，与 `.html` 同体积 | CH13-0019「必须加 .html」**误判** |
| `https://github.com/ycyue/software-testing-course` | 200 | 仓库标题即本课程，README clone 不是空壳 |
| `https://git-scm.com/doc` | 200，548 B 跳转页 | 已知 P3 |
| `https://schema.getpostman.com/json/collection/v2.1.0/collection.json` | 301 → schema.postman.com | 已知 CH14 |
| Postman Variables / Environments 旧路径 | 308 → `/docs/use/send-requests/variables/…` | 已知 CH14 |
| `https://www.rfc-editor.org/rfc/rfc9110`（无 `.html`） | **302** → `/info/rfc9110/` | **新**；`.html` 才是 1.1 MB 规范正文 |
| 同形 `rfc9111`、`rfc8259` | 同 302 → `/info/` | **新** |
| `https://www.iso.org/standard/78176.html` | **403** Cloudflare challenge（完整 Chrome UA 同样 403） | CH22 已记；**CH01 误判为已打开** |
| `https://www.gnu.org/software/grep/manual/` | curl 短 UA **200**（8 KB 索引）；**Chrome 152 UA → 403** | **新**；`grep.html` 本轮超时 |
| `https://www.openssh.com/` | **301** → `https://www.openssh.org/` | **新** P3 |
| `https://未知地址` | DNS 到环境槽 `198.18.2.25`，TLS 失败，HTTP **000** | **必报** |

---

## 3. P0

无。未发现：把六条禁止项写成正说、编造 ISTQB 必须条款、外链指向恶意载荷、把下单清空购物车写成已冻结事实。

---

## 4. ISSUE

## ISSUE
ID：RT04-0001  
文件：`chapters/11-linux.md`  
章节：第 11 章  
小节：11.13 curl 纪律  
精确位置：L464  
原文：`不要 curl https://未知地址 | sh 或 curl … | bash`  
问题等级：P2  
问题类别：LINK / SEC  
问题说明：任务点名「若存在必报」。这是可复制的字面 URL，不是 `example.invalid`。本轮 `curl https://未知地址`：解析到审计环境的 `198.18.2.25:443`，`SSL_ERROR_SYSCALL`，状态 000。CH11 外链表写「web_fetch 被 SSRF 拦，未拿到 HTTP 状态码」，**未登记此条**。  
为什么有问题：纪律句的意图（禁止管道执行未知脚本）正确，但把它写成 `https://` 链接会出现在全书外链清点里，学生若当真请求会得到证书/连接失败，并可能被安全课当成「教材里的活 URL」。  
依据：本轮 curl；RFC 2606 `.invalid`。  
建议修改：改成 `https://example.invalid/install.sh` 或纯文字「未知 URL」，不要可解析的伪主机。  
推荐替换文本：`不要 curl https://example.invalid/install.sh | sh（或任何未知地址管道进 bash）`

## ISSUE
ID：RT04-0002  
文件：`chapters/11-linux.md`  
章节：第 11 章  
小节：参考资料  
精确位置：L739  
原文：`[grep 手册](https://www.gnu.org/software/grep/manual/)`  
问题等级：P2  
问题类别：LINK  
问题说明：学生用浏览器点开的路径，在 **Chrome 152 完整 UA** 下 HTTP **403 Forbidden**（199 B 的 Apache 拒绝页）。`curl/8` 或 `Mozilla/5.0 course-audit` 得到 200、8 KB 索引页（不是完整手册）。`https://www.gnu.org/software/grep/manual/grep.html` 本轮 **超时**。CH11 写「2026-09-08 核验」且审计以 web_search 代替状态码。  
为什么有问题：参考资料是给零基础点的。按教材默认浏览器打开会 403，会以为手册失效或自己网络被墙。Coreutils 长手册同域 `coreutils.html` 本轮 200，不是整站挂了。  
依据：本轮两条 UA 对照 curl。  
建议修改：改直链 `https://www.gnu.org/software/grep/manual/grep.html`（若仍超时则改 `info grep` / man 页说明）；或写「站点对部分浏览器 UA 回 403，用 `man grep`」。  
推荐替换文本：`GNU grep 手册以本机 man grep 为准；网页版 https://www.gnu.org/software/grep/manual/html_node/ 若 403 不要当工具坏了。`

## ISSUE
ID：RT04-0003  
文件：`chapters/09a-network-http-semantics.md`；`chapters/09b-http-message-observe.md`；`chapters/13-api-testing.md`  
章节：第 9、13 章  
小节：参考资料  
精确位置：09A L445–446；09B 同形 RFC 9110；13 L657 `rfc8259`  
原文：`https://www.rfc-editor.org/rfc/rfc9110`（无 `.html`）；`…/rfc9111`；`…/rfc8259`  
问题等级：P2  
问题类别：LINK  
问题说明：无后缀 URL **HTTP 302** 到 `/info/rfcNNNN/` 元数据页（跟随后 info 页约 4.7 MB，内嵌多种格式）。规范 HTML 正文稳定入口是 `https://www.rfc-editor.org/rfc/rfc9110.html`（本轮 **200，1 187 554 B，无跳转**）。第 9 章写「2026-09-08 核验」，CH09 外链被 SSRF 拦住、**未记录 302**。  
为什么有问题：教材要学生「打开 RFC 9110」核对 safe/幂等。点课文链接先落到 info 目录，不是 §9.2 正文。初学者会停在摘要页，或以为规范只有简介。  
依据：`curl -sSI` Location；对比 `.html` 200。  
建议修改：三处都改 `.html`（或 `/rfc/rfc9110.txt`）。info 页可作「版本与状态」辅链。  
推荐替换文本：`[RFC 9110 HTML](https://www.rfc-editor.org/rfc/rfc9110.html)`

## ISSUE
ID：RT04-0004  
文件：`chapters/11-linux.md`  
章节：第 11 章  
小节：参考资料  
精确位置：L741  
原文：`[OpenSSH](https://www.openssh.com/)`  
问题等级：P3  
问题类别：LINK  
问题说明：`https://www.openssh.com/` **HTTP/1.0 301** → `https://www.openssh.org/`。能到，但课文域名已不是现行首页。CH11 用 web_search「官网仍在」，未记 301。  
依据：本轮 `curl -sSI`。  
建议修改：改为 `https://www.openssh.org/`。  
推荐替换文本：`[OpenSSH](https://www.openssh.org/)`

## ISSUE
ID：RT04-0005  
文件：`chapters/01-software-testing-intro.md`（同 URL 亦在第 22 章 22.6）  
章节：第 1 章参考资料；对照 CH01 vs CH22  
小节：参考资料  
精确位置：01 L518 `https://www.iso.org/standard/78176.html`  
原文：CH01 审计「打开 ISO 页面：Edition 2，2023-11」；「ISTQB、ISO 页面均打开成功」  
问题等级：P2  
问题类别：LINK / 【误判】  
问题说明：本轮完整 Chrome UA 对该 URL 仍是 **403** + `cf-mitigated: challenge`。CH22 已记 403；**CH01 记成功打开是误判**；MASTER 未收进 P1 总表。标准本身仍是 2023 第 2 版（付费），不是死标准。  
为什么有问题：第 1 章把 ISO 官方页当零基础核验入口。学生直链常撞 Cloudflare，会以为「九特性链接坏了」。九特性现用名正确（MASTER Phase 10），问题只在**可达性**。  
依据：本轮 403；CH22 L686；CH01 L887–L893。  
建议修改：保留 ISO 编号，链到不挑战的二次说明（如 ISO 预览/新闻稿），并写「官方页常要人机验证、全文付费」。不要让 CH01 再写「已打开成功」当证据。  
推荐替换文本：`ISO/IEC 25010:2023（付费）。官方目录 https://www.iso.org/standard/78176.html 可能出现人机验证；课程用教学译名，以 2023 九特性现用名为准。`

## ISSUE
ID：RT04-0006  
文件：`chapters/03-software-testing-classification.md` ↔ `project/minishop/server.py` `_create_order`；`frontend/app.js`；`docs/PRD.md` R-ORDER；`docs/openapi.json`  
章节：第 3 章 3.5 系统测试 vs MiniShop v1.0  
小节：系统测试例子  
精确位置：03 L185；对照 `server.py` L415 起；`app.js` L97–112；`index.html` L62–78  
原文：`MiniShop 示例：从注册、登录、看商品、改购物车数量到创建订单，验证完整购物流程。`  
问题等级：P1  
问题类别：MiniShop / SEQ / TEST  
问题说明：【新闭环，G01 未收】实现：`_create_order` **只扣 `products.stock`，SELECT/UPDATE 都不碰 `cart_items`**。前端「购物车」按钮是「更新数量」，「下单」是另一个表单「创建订单」，默认都是 `SKU-DEMO-001`；下单成功只写 `订单 id=`，**不** `refreshCart()` / `refreshProducts()`。PRD R-ORDER 与 OpenAPI 也没写订单来自购物车。G06-0004 / CH19-0017 已把**项目简化**记 P2。漏掉的是：**第 3 章把这条断裂路径叫「完整购物流程」**，系统测试定义会让学生以为改数量 → 下单是一条结算链。  
为什么有问题：按 3.5 做系统测试的人会：1）改购物车 qty=10；2）点「创建订单」；3）预期购物车清空或 qty 下降。实际购物车仍 10，库存被另一条 POST 扣掉，随后可出现 **qty > 剩余 stock**。同章作业 L304 已禁止「加入购物车/结算」，系统测试例子却用「完整购物流程」把两张表单粘回去。这不是重复 M-P1-02 的按钮文案，是**观察对象被教成一条不存在的端到端**。  
依据：本轮读 `_create_order`、下单 handler；PRD R-ORDER 无购物车字段；G01 全文无「完整购物流程」。  
建议修改：3.5 改成两条独立检查：改数量（列表 qty 变、stock 不变）；创建订单（201+id、stock 减、**购物车行仍在**）。标明「v1.0 不是从购物车结算」。  
推荐替换文本：`系统测试例子（v1.0）：注册→登录→列表→把 SKU-DEMO-001 更新为合法数量→再单独 POST 创建订单（成功只返回 id）。创建订单不读取、不清空购物车，这是教学简化，不要写成「完整结算流程」。`

## ISSUE
ID：RT04-0007  
文件：`chapters/06b-test-management.md`  
章节：第 6 章（下）  
小节：练习 10 答案  
精确位置：L326  
原文：`回归测试：至少覆盖加购、修改为合法数量、修改为库存值`  
问题等级：P2  
问题类别：ANS / MiniShop  
问题说明：前端没有「加购」按钮，只有「更新数量」。M-P1-02 / CH03-0001 打的是第 3 章冒烟答案「加入购物车」「提交订单」。**06B 标准答案仍写「加购」**，G01-0003 只纠正了「6-1 对象被答成 qty=11」，没改这个动词。08A L57 已正确列出「更新数量」「创建订单」。  
为什么有问题：对完 06B 答案的人会去页面找「加购」，或把 combo 教学页的「加入购物车」抄进回归范围。  
依据：`index.html` L68、L78；08A 控件表。  
建议修改：加购 → 更新数量；并与 G01-0003 一起把确认对象改回 BUG-001。  
推荐替换文本：`回归：合法关键字搜索、登录、把某 SKU「更新数量」为 10、创建订单（id、无 status）。不要写加购/结算。`

## ISSUE
ID：RT04-0008  
文件：`project/minishop/docs/openapi.json`；`chapters/09b-http-message-observe.md`  
章节：冻结契约 vs 第 9 章  
小节：OpenAPI responses；9.10「必须能解释的常用码」  
精确位置：OpenAPI 九条 path 的 `responses`；09B L90–110（405、415）  
原文：OpenAPI `/api/login` 仅 200/401；`/api/cart/items` 仅 200/400/401；9.10 把 **405、415** 放进必须能解释表  
问题等级：P2  
问题类别：HTTP / MiniShop  
问题说明：G06-0007 已报 login 缺 400/Cookie、cart 缺 404、login 200 文案串到订单。**增量：** 实现里 **没有任何 405 / 415**。`do_GET` 对 `/api/login`、无 id 的 `/api/orders` 一律 404；`_read_json` 不看 `Content-Type`，错媒体类型仍按 JSON 解析或 400 invalid json。OpenAPI 作为质量标准里的冻结契约，全路径不出现 405/415。第 9 章却要求必须能解释这两码，且失败观察表会把学生领到 MiniShop 上去找。CH09-0003 已写「MiniShop 不见 405」，落点在第 9 章表，**没打到 OpenAPI**；G01 跨章未收。  
为什么有问题：对照 OpenAPI 写用例的人不会设计 405；对照第 9 章的人会把 GET `/api/login` 的 404 写成「方法不允许缺陷」。冻结契约与「必须掌握的状态码」对不上。  
依据：`server.py` do_GET/do_POST 尾部 404；OpenAPI 全文无 405/415；09B L105、L125 附近 415 行。  
建议修改：OpenAPI 用描述句写「未声明的方法 → 404，本项目不实现 405 Allow」；9.10 分列「通用 / MiniShop v1.0」。login 补 400（可并进 G06-0007 修订，不必两套文案）。  
推荐替换文本：OpenAPI `/api/login` 增加 `"400": {"description": "invalid json or missing field"}`；info.description 加一句 `Wrong method on /api/* returns 404, not 405.`

## ISSUE
ID：RT04-0009  
文件：`chapters/assets/09-pytest-report.png`（`project/minishop/evidence/screenshots/09-pytest-report.png` 同哈希）；`chapters/16a-pytest-basics.md`；`chapters/19-minishop-project.md`  
章节：第 16、19 章  
小节：pytest-html 截图  
精确位置：16A L268；19 L248  
原文：`![pytest-html 37 passed / 1 expected failure](assets/09-pytest-report.png)`  
问题等级：P2  
问题类别：IMG  
问题说明：【截图时效 / G05 误判偏轻】工具版本 **没有过时**（4.2.0 = 2026-09 PyPI latest）。问题是这张图**不像一份 2026 pytest-html 报告**：Environment 标题下是空的；结果表只有表头（Result/Test/Duration/Links），**零行用例名**。同目录 HTML `evidence/pytest-report.html` 有完整环境表（G06 已见 `CI: true`）和 38 行结果。G05 对 IMG 09 的结论是 KEEP「数字」。数字对，**作为「这就是 pytest-html」的教学截图不合格**——学生自己生成的 4.2.0 报告会多出两大块，会怀疑截了错工具。  
为什么有问题：第 16/19 章用它证明「会打开 HTML 报告」。打开后对不上自己的文件，比 Timing 文案更直接。不是「根本不是所标工具」，是**裁掉了该工具 2026 默认可见的两段**。  
依据：本轮打开 PNG；对照 html 环境块与用例表；PyPI pytest-html 4.2.0。  
建议修改：REPLACE 为含 Environment 至少 3 行 + 展开 2～3 条用例名的图；或 caption 写「只截汇总条，完整报告见 evidence/pytest-report.html」。G05 KEEP 改为 MODIFY/REPLACE。  
推荐替换文本：图注：`pytest-html 4.2.0 汇总：37 passed / 1 expected failure。完整报告还包含 Environment 与用例列表，见 evidence/pytest-report.html。`

## ISSUE
ID：RT04-0010  
文件：`chapters/21-job-hunting.md`；`chapters/19-minishop-project.md`；`chapters/05-test-case-design.md`  
章节：第 21 / 19 / 5 章  
小节：21.5 投递；19.3 启动；5.4 后置  
精确位置：19 L106 `MINISHOP_RESET=1`（默认）每次启动重建教学库；05 L108、L132 提到数据污染；21.5 无账号池  
原文：每次启动重建教学库，避免脏数据冒充回归失败。  
问题等级：P2  
问题类别：JOB  
问题说明：【岗位新点，不是 Git/Jira/Postman GUI】G08 已覆盖协作 Git、缺陷工具点击、GUI 闸、年限、ATS 同义词。漏的是入职第一周的**数据策略**：公司测试环境几乎从不「每次启动 DROP 全库」。MiniShop 三人共用 `13800138000`，RESET=1 被写成优点。第 5 章有「唯一测试数据」一句，第 21 章投递/简历没有「不要把清库当正常测试环境」「不要共用教材手机号当公司账号」。  
为什么有问题：学生入职后会：把「昨天的订单不见了」当缺陷；用同一个手机号撞别人的用例；不会申请账号池/造数规范。这和「会不会 Git」是不同的穿帮方式。  
依据：19 L106；教学数据三人电话；G08-0008～0016 无「账号池/清库」。  
建议修改：21.3 或 22.5 加半页：共享环境 ≠ RESET；手机号用自己的后缀；造数要可回收。19 章脚注：RESET=1 是教学隔离，简历不要写「我设计了数据重置方案」。  
推荐替换文本：`MiniShop 每次启动清库是为了让 37/1 可重复，不是公司测试环境的做法。入职后先问：账号池、能否造数、清库要谁批。不要用 13800138000 当「我的测试账号」。`

## ISSUE
ID：RT04-0011  
文件：`chapters/21-job-hunting.md`  
章节：第 21 章  
小节：21.5 匹配策略  
精确位置：L150–L161  
原文：功能测试主投；对不上的要求不要加假技能；未写验证码/短信。  
问题等级：P2  
问题类别：JOB  
问题说明：【岗位新点】国内初级 Web/App JD 高频行是「短信验证码、图形验证码、登录鉴权」。课程正确禁止把验证码写进 MiniShop 契约（M-P1-30 是 08A 优先检查表）。21.5 **没教学生看见 JD 写验证码时怎么说**：测试环境关闭/白名单/一次性码，而不是「我测过 MiniShop 所以会测验证码」或留空被 ATS 筛掉。G08-0012 列了 Apifox/Charles/Excel/ADB，**没有验证码应答句**。  
为什么有问题：诚实边界挡住假 MiniShop 验证码，但求职章没有替代话术。老实人不投带验证码的功能岗（初级岗大多数都有）；不老实人把第 5 章通用练习系统的验证码抄进简历。  
依据：PRD 非范围「短信验证码」；21.5 全文无验证码/短信/白名单。  
建议修改：21.5 加一行同义词纪律：JD「验证码」→ 答「课程项目无此功能；入职按测试环境开关或白名单测，不编 MiniShop 验证码」。  
推荐替换文本：`JD 写图形/短信验证码：写「了解常见测法（测试环境关闭、白名单手机号），MiniShop v1.0 无此功能，未练过绕过。」禁止把通用练习系统的验证码表抄进项目经历。`

## ISSUE
ID：RT04-0012  
文件：`chapters/11-linux.md`  
章节：第 11 章  
小节：11.3 pwd  
精确位置：L119  
原文：`确认位置永远比“感觉在哪”可靠：先 pwd。`  
问题等级：P3  
问题类别：ABS  
问题说明：任务要求区分「禁止绝对化的教学句」和「教材自己在绝对化」。本句是教材自己用「永远」下操作规则。作为 pwd 口诀可接受，但和全书「不要永远」纪律并排时，是少数**正说绝对化**。不是质量标准六条。  
建议修改：`先 pwd，不要凭感觉写路径。`  
推荐替换文本：同上。

---

## 5. 误判（不重复开教材缺陷，只纠正第一轮）

| 第一轮 | 本轮 | 裁决 |
| --- | --- | --- |
| CH13-0019：`spec.openapis.org/oas/v3.0.3` 缺 `.html` 可能失效 | 无后缀 **200**，与 `.html` 同 398758 B | **误判**。可改成 .html 作规范写法，但不能当死链 |
| CH01：ISO 78176「打开成功」 | Chrome UA **403** | **误判可达性**；九特性内容仍对（MASTER Phase 10） |
| G05 KEEP `09-pytest-report.png`「数字对」 | 汇总对，Environment/用例表被裁空 | **KEEP 过宽** → 见 RT04-0009 |
| CH11 外链「检索确认官方入口」 | grep 手册 Chrome 403；openssh.com 301；`未知地址` 未登记 | 外链覆盖声明过满 |
| CH09 外链 SSRF、RFC「核验」 | `rfc/rfc9110` 无后缀 302 `/info/` | 漏记跳转；见 RT04-0003 |

未推翻：M-P1-02 按钮文案、G06-0004 下单不读车（项目侧）、G08 Git/Jira/Postman GUI、Chrome Timing、空搜索图、所属者 200、Cookie jar。

---

## 6. 绝对化与编造：检索摘要

**教材自己绝对化（已开单或不够开单）：**

- RT04-0012：`永远` + pwd。
- 其余「永远 / 所有公司 / 必须」：错误节、测验干扰项、⭐⭐⭐ 必须掌握、ISTQB 原则一/二（「只能证明存在」「穷尽不可能」）——这些是**正确的反绝对化或标准原文**，不报。

**疑似编造：本轮无新 P1。**

- 「一天 80 封」是禁止海投的反例，CH21 已判通过。
- 「支付模块 21 个 / 注册 2 个」有「假设」。
- 「约 2/10、3/10」标了行业/教学示例。
- 测试金字塔明确 **不是** ISO/ISTQB 的 70/20/10。
- RFC 10008 QUERY（2026-06）经检索属实，G02 已核，不报编造。
- CTFL 2026-08 考试结构表仍写 **CTFL v4.0**，课文链 v4.0.1 PDF **200**，未过时。

---

## 7. 跨章（只补 G01/G07 漏的）

| 漏项 | 为何不是复述 G01/G07 |
| --- | --- |
| 3.5「完整购物流程」vs 下单不读车 | G01 收了冒烟按钮、空格提示、幽灵 qty=1、保持原值，**没收系统测试定义把假结算链写实** |
| 06B 答案「加购」 | G01-0003 只改确认对象；动词仍错 |
| 9.10 必须 405/415 vs OpenAPI/实现从无这两码 | CH09 章内有；G01 跨章未接到冻结契约 |
| RFC 无后缀 302 | 章 Agent 被 SSRF 拦住，G01 不审外链 |

难度突跃、第 7 章插入、书面 2-1、星级三套名：G07/G01 已密，不重开。

---

## 8. MiniShop 闭环核对（本轮实读，不改仓库）

| 检查 | 结果 | 去向 |
| --- | --- | --- |
| 下单是否读取购物车 | 否 | RT04-0006（教材系统测试例子）+ 已有 G06-0004 |
| 下单是否清空购物车 | 否，SQL 不 DELETE/UPDATE cart_items | 同上 |
| 前端下单后是否刷新车/库存 | 否 | G06-0004 已含，不新开 |
| 按钮 vs 第 3 章答案 | 「更新数量」「创建订单」vs「加入购物车」「提交订单」 | 已有 M-P1-02；06B「加购」= RT04-0007 |
| OpenAPI 缺码 | login 无 400；cart 无 404；全路径无 405/415；login 200 文案写订单 | 前几项 G06-0007；405/415 增量 = RT04-0008 |

---

## 9. 建议总控

1. 外链发布前用**真实浏览器 UA** 再打一遍（grep 手册、ISO）。只跑 `curl` 短 UA 会漏 403。
2. RFC 引用统一 `.html`。
3. 第 3 章系统测试例子和第 6B「加购」与第 3 章冒烟按钮是同一把尺子的三个断点，修订时一起改。
4. pytest-html 图换一张带用例名的；不要为了「数字对」KEEP。
5. 就业章补「清库≠共享环境」「JD 验证码怎么诚实答」，不要再叠 Git/Jira/Postman GUI。

---

## 10. 执行记录

读过：`MASTER_AUDIT.md`、`AUDIT_AGENT_BRIEF.md`、`QUALITY_STANDARD_v1.0.md`、G01/G02/G05/G06/G07/G08 相关段、CH01/CH03/CH09/CH11/CH13/CH14/CH22 外链与误判段、`server.py` `_create_order`/`do_GET`、`frontend/index.html`+`app.js`、PRD、OpenAPI、`09-pytest-report.png`、`ch14-*.png`、`ch18-jmeter-parts.png`、`08-network-log.png`、`evidence/pytest-report.html` 头。

命令摘要：抽取 55 个 https；`curl -L` 全表；对 ISO/grep/RFC/openssh/未知地址做 `-I` 与 Chrome UA 对照；PyPI pytest-html latest=4.2.0；JMeter 下载页 5.6.3；GitHub `ycyue/software-testing-course` 200。

未改教材。
