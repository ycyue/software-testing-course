# Chapter 13 Audit

审计员：Chapter-Audit-Agent-13  
日期：2026-09-10  
范围：仅第 13 章接口测试及其明确列出的相关文件。未审其他章正文。  
对象：`chapters/13-api-testing.md`，`practice/13-api-shapes/`，`project/minishop/docs/openapi.json`，`project/minishop/docs/PRD.md`（核对接口口径），`chapters/quizzes/stage-5-api.md` 中第 13 章题，示意图 `ch13-ui-vs-api` / `ch13-four-slots` / `ch13-four-shapes` / `ch13-401-403`（png+html）。

旧审查（`reviews/chapter-13-review.md`、`reviews/_pedagogy-2026-09-10/ch13.md`、v1.2.1 91 分、阶段 5 复审 88 分）只作线索。本轮独立复核，不继承分数。上一轮主伤「教学 `/login` 与 v1.0 `/api/` 双路径」在现行正文、curl、13-1 中**已不存在**。

---

## 1. Coverage

正文 `chapters/13-api-testing.md`：667 行，约 14 955 字符。

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 章标题 H1 | 1 | 1 | 0 |
| 小节 H2（代码围栏外） | 27 | 27 | 0 |
| 小节 H3（错误/面试/练习/门槛） | 26 | 26 | 0 |
| 一句话核心 / 学习目标 / 前置 / 清单 / 总结 / 预告 | 全套结构节 | 全套 | 0 |
| 正文段落（非标题/非表/非列表/非代码） | 98 | 98 | 0 |
| 列表项（目标、文档清单、纪律、步骤、检查清单等） | 全部 | 全部 | 0 |
| 教学表格 | 8 | 8 | 0 |
| 工作实战模板表 | 1 | 1 | 0 |
| 代码围栏 | 11 | 11 | 0 |
| 其中 JSON 块 | 3 | 3 | 0 |
| 其中 mermaid | 1 | 1 | 0 |
| 其中 bash | 3 | 3 | 0 |
| 其中 HTTP `text` | 2 | 2 | 0 |
| 其中产出路径 / 模板 markdown | 2 | 2 | 0 |
| Linux/Shell 命令（serve、curl 登录、TOKEN 管道、下单、13-1） | 6 | 6 | 0 |
| SQL 可执行语句 | 0（只指向第 12 章 `SELECT`） | 0 | 0 |
| SQL 提及 | 10 | 10 | 0 |
| HTTP 示例（报文 2 + curl 登录 + TOKEN/下单 + 13-1 路径） | 5 | 5 | 0 |
| 行内 JSON 对象 | 19+ | 全部 `json.loads` | 0 |
| 测试用例（13.8 表 8 + 13.9 表 5 + 13.10 表 4 + 13-1 四态） | 21 | 21 | 0 |
| Bug / 缺陷场景 | 2（qty=11 脏写；BUG-001 文末） | 2 | 0 |
| 常见错误 | 10 | 10 | 0 |
| 面试题 | 5 | 5 | 0 |
| 小练习 | 10 | 10 | 0 |
| 练习答案 | 10 | 10 | 0 |
| 检查清单项 | 11 | 11 | 0 |
| 正文 PNG | 4 | 4（`read_file` 打开） | 0 |
| 配套 HTML 源 | 4 | 4 | 0 |
| 外部链接 | 3 | 3（检索核验；直连 RFC/MDN 被环境 SSRF 拦截） | 0 |
| 仓库内链接 | 5 | 5（文件均存在） | 0 |
| 阶段测验第 13 章题 | Q1、Q2、Q3（Q8/Q10 与本章口径交叉） | 先独立作答再对照 | 0 |
| practice README / main.py / tests/test_lab.py | 3 | 3 | 0 |
| OpenAPI 全文件 + 正文摘录 | 1+1 | 1+1 | 0 |
| PRD 接口口径 | R-CART / R-CART-10 / R-AUTH / R-ORDER / R-PERM / R-SEARCH / 非范围 | 已核对 | 0 |

**未检查 = 0。Coverage 100%。**

H2 清单（全部过目）：这一章解决什么问题；学习目标；前置知识；场景导入；13.1–13.13；工作实战；常见错误；面试角度；小练习；练习答案；检查清单；总结；可运行性说明；参考资料；下一章预告。

---

## 2. 总评分

核心章，按 brief 从严。九项各 /10，总体按九项合计折合百分。

| 项 | 分数 | 依据摘要 |
| --- | ---: | --- |
| 技术准确性 | 7/10 | REST≠JSON、四态、401/403、POST 默认不幂等、订单无 `status` 均对；四态图 MiniShop 报文抄出来会对不上标注的 error；HTTP 报文缺 Content-Length；响应写成 HTTP/1.1，实现是 HTTP/1.0 |
| 岗位实用性 | 8/10 | 四态、改 Path id、连点 POST、接口+SQL 是初级接口测试真活；放错格子只停在口头题 |
| 完整性 | 8/10 | 大纲条目齐；仓库 OpenAPI 无 `security`/error schema，正文仍按「锁图标 / 415」教 |
| 初学者友好度 | 7/10 | 后厨类比清楚；REST/OpenAPI 在第一发和四格之前；13.8 表在可抄登录之前 |
| 教学顺序 | 6/10 | 四格（13.7）和登录 curl（13.12）都晚于 REST/文档/四态表；13.2「可跳」引用尚未教的四格 |
| 代码质量 | 8/10 | 13-1 与 curl 可跑且与 `server.py` 一致；13.12 手写 HTTP 按 RFC 9112 成帧会失败 |
| 实操质量 | 8/10 | `python3 practice/run.py 13-1` 与 `--check` 均绿；脚本代发 Body，读者不必自己改形状 |
| 练习质量 | 8/10 | 10 题与答案一致；工作实战四态已对齐 13-1；未强制「同一字段放错格子」 |
| 图片质量 | 6/10 | 401/403 与四格命题对；四态图缺 `sku`；店门/后厨图 Body 也不完整 |
| **总体** | **73/100** | 九项合计 66/90 → 73。核心章发布目标 95，质量标准最低 90。本轮不得按可发布计 |

上一轮双路径 P0 已修，概念骨架可用，但核心章仍被图 oracle、报文成帧和课序拖在发布线以下。

---

## 3. P0

无。

未发现会把学生系统教错到「GET 不安全 / POST 安全」「Cookie/Session/Token 三选一」「接口自动化 ROI 永远最高」「订单有 status」「对着 v1.0 打 `/login` 还能当登录契约」这一级的现行正文。旧审查里的教学 `/login` 可抄示例，本轮正文、curl、13-1 均已改为 `/api/`。

---

## 4. P1

## ISSUE
ID：CH13-0001
文件：`chapters/assets/diagrams/ch13-four-shapes.html`、`chapters/assets/diagrams/ch13-four-shapes.png`；插入点 `chapters/13-api-testing.md` 13.8
章节：第 13 章
小节：13.8 缺失、空值、null、错误类型、边界
精确位置：四态图第二～四格 JSON；图 lead「MiniShop 购物车 Body」
原文：`{"qty":null}` → 400 `null qty`；`{"qty":""}` → 400 `wrong type qty`；`{"qty":"1"}` → 400 `wrong type qty`（仅第一格带 `sku`）
问题等级：P1
问题类别：IMG / TEST / ACC
问题说明：图自称 MiniShop 购物车 Body，并给出具体 error 字符串。`server.py` `_cart_items` 先查 `"sku" not in data`，再查 qty。缺 `sku` 时固定 `400 missing sku`，到不了 `null qty` / `wrong type qty`。
为什么有问题：学生若按图构造请求（而不是按旁边的 13.8 表），会得到与图注不同的判定，并可能把「缺 sku」写成「null 校验」。13.8 表、实操 13-1 都带了 `sku`，图与正文主表打架。
依据：本机 MiniShopLab：`{"qty":null|""|"1"|11}` + Bearer → 全部 `{"error":"missing sku"}`。对照 `project/minishop/server.py` `_cart_items` 中 sku 检查在 qty 之前。RFC 8259 只保证这些 JSON 合法，不保证业务 error 文案。
建议修改：四格都带 `"sku":"SKU-DEMO-001"`，与 13.8 表、13-1 完全同一组 Body。可用脚注说明「一次只破坏 qty」。
推荐替换文本：见第 16 节补丁。

---

## 5. P2

## ISSUE
ID：CH13-0002
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.2 REST；13.5 文档；13.6 OpenAPI；13.7 四格
精确位置：L82「可跳：会填四格…再回来读」；四格正式定义在 L224
原文：可跳：会填四格、能对着文档发请求，再回来读。
问题等级：P2
问题类别：SEQ / PED
问题说明：REST 已降为 ⭐⭐ 并加可跳，但四格仍放在 OpenAPI/Swagger UI 之后。可跳条件用的是尚未讲授的技能。13.5 第 4 条已点名 Path/Query/Header/Body，模型却后出现。
为什么有问题：初级岗位的第一枪应是「数据放哪一格」，不是架构风格和文档工具史。测错格子等于没测，这句话现在来得太晚。
依据：质量标准「解释顺序：生活类比 → 简单模型 → 正式定义 → 例子」；大纲第 13 章把 Path/Query/Header/Body 列为与 REST 并列的核心，不是 REST 的附录。
建议修改：把现行 13.7（含 `ch13-four-slots`）移到 13.1 之后、REST/OpenAPI 之前。
推荐替换文本：见第 16 节。

## ISSUE
ID：CH13-0003
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.8 vs 13.12
精确位置：L246 四态表与 `run.py 13-1`；可抄 `POST /api/login` 在 L336 之后
原文：请求必须带 Bearer……配套实操：`python3 practice/run.py 13-1`。
问题等级：P2
问题类别：SEQ / EX
问题说明：13.8 要求带 Bearer 测形状，但最小可抄登录 curl 在 13.12。13-1 脚本代登，读者仍不会自己发登录。工作实战第 2 条才补登录，课内表已经用过了。
为什么有问题：跟着手抄 13.8 表的人会先打出 401，把「未认证」和「缺字段」叠在一起——正文自己警告过这件事，却没把钥匙放在警告前面。
依据：13.8「无 Bearer 时购物车是 401，不要先测形状」；实测无 Bearer → `401 unauthorized`。
建议修改：在 13.8 表前插入最小 `POST /api/login`（serve + `/api/` + 取 token），登录细节仍可留在 13.12。
推荐替换文本：见第 16 节。

## ISSUE
ID：CH13-0004
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.12 登录 API
精确位置：L349–L365 HTTP `text` 请求/响应
原文：
```
POST /api/login HTTP/1.1
Host: 127.0.0.1:8765
Content-Type: application/json

{"phone":"13800138000","password":"Test1234"}
```
响应写成 `HTTP/1.1 200 OK` + `Content-Type: application/json`。
问题等级：P2
问题类别：HTTP / ACC
问题说明：RFC 9112 §6：请求体是否存在由 `Content-Length` 或 `Transfer-Encoding` 信号。无二者则无 body。MiniShop `_read_json` 用 `Content-Length or 0` 读体。按正文原样用 socket 发送 → `HTTP/1.0 400` `missing field`。补上 Content-Length 后才是 200。另外 `BaseHTTPRequestHandler` 默认 `protocol_version = HTTP/1.0`，真实状态行是 `HTTP/1.0 200 OK`，`Content-Type: application/json; charset=utf-8`，并带 `Content-Length`。
为什么有问题：curl 能过是因为 curl 自动加 Content-Length，不是因为报文示例可照抄。核心接口章要求对照 RFC，却给出一个按 RFC 成帧会失败、按实现对照版本号也不符的「形状」。
依据：RFC 9112「The presence of a message body in a request is signaled by a Content-Length or Transfer-Encoding header field」；本机 raw socket 对照实验（见 §18）。
建议修改：请求补 `Content-Length`；响应改为 HTTP/1.0（或注明「curl 看到的是 HTTP/1.0，教学形状省略部分头」），并写出真实 `Content-Type`。
推荐替换文本：见第 16 节。

## ISSUE
ID：CH13-0005
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.7 Path、Query、Header、Body
精确位置：L240
原文：`Content-Type: application/json` 与真正的 JSON Body 必须一致。声明 JSON 却发送表单，或反过来，常见 `415` 或服务端解析失败。
问题等级：P2
问题类别：HTTP / TEST / MiniShop
问题说明：行业常见 415 的判断本身符合 RFC 9110 §15.5.16。但学生本章只打 MiniShop：`_read_json` 不看 Content-Type，只要字节是 JSON 对象就解析。本机把合法 JSON 标成 `application/x-www-form-urlencoded` 仍 `200` 写购物车。
为什么有问题：读者按 13.7 在 MiniShop 上做「错误 Content-Type」会看到成功，可能以为自己测错了，或得出「Content-Type 无所谓」。
依据：本机 MiniShopLab；`server.py` `_read_json`。
建议修改：保留「常见 415」，立刻补一句 MiniShop 当前不校验 Content-Type，所以这一条在本项目上是「文档/实现差」，不要当成 415 用例的预期。
推荐替换文本：声明与 Body 不一致时，许多服务返回 415。MiniShop v1.0 不读 Content-Type，只要 Body 能 `json.loads` 成对象就会往下走——测到 200 不是「Content-Type 不重要」，是这条契约没写进实现。

## ISSUE
ID：CH13-0006
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.13 订单 API
精确位置：L389「Body 需要 `sku`」；L409「不要指望下单接口替你练完库存规则」
原文：Body 需要 `sku`。……超库存应在购物车接口测……不要指望下单接口替你练完库存规则。
问题等级：P2
问题类别：ACC / MiniShop
问题说明：OpenAPI `POST /api/orders` `required: ["sku","qty"]`。只发 sku → `400 missing field`（不是购物车的 `missing qty`）。`qty=11` 下单 → `400 qty exceeds stock`，与购物车同一句。PRD R-ORDER 没写库存，实现写了。
为什么有问题：「Body 只要 sku」是错的可抄口径；「下单接口不练库存」会被理解成「下单不校验库存」。
依据：OpenAPI paths./api/orders；本机 `qty=11` 下单 400；`server.py` `_create_order` 调用 `qty_allowed`。
建议修改：Body 写明 `sku`+`qty`。库存主练购物车可以保留，但必须说「下单实现也会 400，只是本章不把它当主用例」。
推荐替换文本：Body 必填 `sku` 与 `qty`（OpenAPI `required`）。库存规则主练 `POST /api/cart/items`；`POST /api/orders` 对 `qty=11` 当前实现同样 400 `qty exceeds stock`，不要据此发明订单状态，也不要写成「下单不校验库存」。

## ISSUE
ID：CH13-0007
文件：`chapters/assets/diagrams/ch13-ui-vs-api.html` / `.png`
章节：第 13 章
小节：13.4
精确位置：后厨窗口卡片
原文：直接 `POST /api/cart/items {"qty":11}`，看 400 和库里有没有写成 11。
问题等级：P2
问题类别：IMG / MiniShop
问题说明：缺 `sku`、缺 Bearer。无 Bearer → 401；有 Bearer 无 sku → `missing sku`。400「没写成 11」碰巧成立，但原因不是库存规则。场景导入用的完整 Body `{"sku":"SKU-DEMO-001","qty":11}` 才是对的。
为什么有问题：本章最容易被记住的那张分工图，把主案例打成了不完整报文。
依据：与 CH13-0001 同一套 MiniShopLab 结果。
建议修改：改成 `{"sku":"SKU-DEMO-001","qty":11}` 并点明要 Bearer。
推荐替换文本：直接 `POST /api/cart/items`，Bearer + `{"sku":"SKU-DEMO-001","qty":11}`，看 400 `qty exceeds stock`，库里不得变成 11。

## ISSUE
ID：CH13-0008
文件：`chapters/13-api-testing.md`；`project/minishop/docs/openapi.json`
章节：第 13 章
小节：13.6 OpenAPI 与 Swagger
精确位置：L216–L220
原文：`security` / 锁图标表示需要认证。Swagger UI 上的 “Try it out” 适合探索……
问题等级：P2
问题类别：PRE / MiniShop / PED
问题说明：仓库 `openapi.json` 无 `security`、无 `components`、无 servers，登录 200 也没有 token/Set-Cookie schema。仓库不托管 Swagger UI。学生打开「完整文件」对不上锁图标，也点不到 Try it out。
为什么有问题：13.6 把 OpenAPI 当用例来源，但真正能设计四态/Cookie 的信息在 PRD 与 `server.py`。文档能力教对了，落到本项目上会空转。
依据：`project/minishop/docs/openapi.json` 全文件检索无 `security`；PRD R-AUTH 有 Cookie+Bearer。
建议修改：写明 MiniShop 这份 OpenAPI 是薄摘录：没有锁图标、没有 error schema；认证与错误字符串以 PRD + 实现为准。Try it out 改为「可用任意 OpenAPI 阅读器打开该 json，本仓库没有内置 Swagger UI」。
推荐替换文本：见第 15 节。

## ISSUE
ID：CH13-0009
文件：`chapters/13-api-testing.md`；`chapters/assets/diagrams/ch13-four-slots.html`
章节：第 13 章
小节：13.7 Query 行；四格图 Query 卡
精确位置：L234；图 `keyword=   空搜索`
原文：Query……缺失、空、类型、组合；……搜 `mouse` 会空
问题等级：P2
问题类别：TEST / MiniShop
问题说明：`keyword=mouse` 空列表，实测成立。空/空白 keyword 是 BUG-001（全量 3 件），PRD R-SEARCH 的判定是否定的。13.7 与四格图把「空搜索」写成测试动作，不给判定。文末才说 BUG-001 仍开放。
为什么有问题：第 1 章主缺陷在接口章 Query 格子里再次出现，却没有尺子。
依据：PRD R-SEARCH；本机 `keyword=` → 3 件；`keyword=mouse` → `items: []`。
建议修改：Query 行拆成「`mouse` → 空列表（实现符合）」和「空关键字 → 当前仍返回全量，见 BUG-001，不要写成已修复」。
推荐替换文本：Query：`keyword=mouse` 应空；`keyword` 为空或空白按 R-SEARCH 不应返回全量（BUG-001 仍开放）。

## ISSUE
ID：CH13-0010
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.10 幂等
精确位置：L304 登录行
原文：登录 | 通常仍是同一用户会话 | 看是否发两套冲突凭证
问题等级：P2
问题类别：ACC / MiniShop
问题说明：MiniShop 每次登录 `INSERT` 新 session，旧 token 仍能打 `/api/cart`。两次成功登录 = 两套都有效的凭证，不是「同一会话」。
为什么有问题：学生若按「通常同一会话」去断言 MiniShop，会把真实现象当成异常或反过来漏测。
依据：本机两次登录 token 不同，旧 Bearer 仍 200。
建议修改：登录行改成「看是否吊销旧 token」；MiniShop 当前两次登录两个 token 都有效，记观察，不要发明单点登录。
推荐替换文本：登录：重复 POST 是否新发 token、旧 token 是否失效。MiniShop 当前两次都 200、两枚 token 都能用——这是观察，不是 SSO 契约。

## ISSUE
ID：CH13-0011
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.3 JSON
精确位置：L123 错误类型行
原文：`{"qty":"11"}` 看起来像 11，类型是字符串
问题等级：P2
问题类别：PED / TEST
问题说明：13.8 / 13-1 错误类型用 `"1"`，超库存用数字 11。13.3 用 `"11"` 会把「类型错」和「库存边界」叠在同一个数字上。若某实现先 coerce 再比库存，oracle 会变成 `qty exceeds stock` 而不是 wrong type。
为什么有问题：本章反复强调一次一个无效条件，自己的入门表却用了会混淆的字面量。
依据：13.8 表与 13-1 均用 `"1"`；`server.py` 先 `type(qty) is not int` 再比库存。
建议修改：13.3 错误类型改成 `{"qty":"1"}`，与 13.8/13-1/四态图一致。
推荐替换文本：错误类型 | `{"qty":"1"}` | 看起来像 1，JSON 类型是字符串，不是数字。

## ISSUE
ID：CH13-0012
文件：`chapters/13-api-testing.md`；`practice/13-api-shapes/`
章节：第 13 章
小节：工作实战；实操 13-1
精确位置：必做 1–7；`practice/13-api-shapes/main.py` 写死 CASES
原文：必做含四态、边界、未认证或越权、重复 POST；无「同一字段放错格子」。13-1 脚本代发四种 Body。
问题等级：P2
问题类别：EX / PED
问题说明：练习 5 问 qty=11 放 Query/Header/Body 意味着什么，工作实战不要求做。13.7 的脊柱句「测错格子等于没测到」没有强制观察。13-1 验收是看输出，读者可以不改任何 JSON。
为什么有问题：本章独特技能是改形状和改格子；可运行实操只演示了形状，格子仍是口答题。
依据：本机 `POST /api/cart/items?qty=11` + Body `qty=1` → 200 `qty=1`（Query 被忽略）；缺 Body qty + Query 11 → `missing qty`。
建议修改：工作实战加一条「同一 qty=11 放进 Query，Body 合法或不带 qty」；13-1 README 加选做：改 `CASES` 里某一个 Body 看结论如何变。
推荐替换文本：见第 15 节。

## ISSUE
ID：CH13-0013
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.9；13.10
精确位置：L288「禁用后再用旧 Token」；L307「支付回调」
原文：认证后权限变化 | 禁用后再用旧 Token | 应失败。支付回调 | 可能重复入账 | 高风险，正式规则未冻结前只记录风险。
问题等级：P2
问题类别：MiniShop / JOB / PRE
问题说明：质量标准：第 19 章前的支付必须标明教学约定。支付行写了「未冻结」，仍像一张可执行表。MiniShop 无禁用用户、无支付回调，学生无法在本章环境复现。
为什么有问题：权限表其它行都能在 MiniShop 打到；这两行不能，却没有「本项目不可跑」。
依据：PRD 非范围：支付、订单状态机；`server.py` 无 disable user / webhook。
建议修改：标成「一般系统要测，MiniShop v1.0 没有这两条，不要造数据」。
推荐替换文本：禁用用户、支付回调：一般项目高风险点；v1.0 明确不做，只记风险，不要在本机发明接口。

## ISSUE
ID：CH13-0014
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.6；13.10
精确位置：标题 ⭐⭐⭐；Idempotency-Key 段
原文：13.6 OpenAPI 与 Swagger ⭐⭐⭐；13.10 整节 ⭐⭐⭐ 含 Idempotency-Key
问题等级：P2
问题类别：PED
问题说明：REST 已诚实降为 ⭐⭐。OpenAPI 读 `required`/`responses` 应 ⭐⭐⭐，但 Swagger 一词源流、GraphQL/RPC 一笔、MiniShop 没有的 Idempotency-Key 仍挂在必须掌握节里。学习目标也仍要求「用测试视角解释 REST」。
为什么有问题：星级是过滤器。全 ⭐⭐⭐ 等于没有过滤器。
依据：质量标准「知识层级统一使用 ⭐⭐⭐/⭐⭐/⭐」；13.2 已证明作者知道可跳。
建议修改：13.6 拆成「读 OpenAPI ⭐⭐⭐」+「Swagger 工具史 ⭐」；Idempotency-Key 降为 ⭐⭐ 并标明 MiniShop 无此头。学习目标 REST 条与 13.2 可跳对齐。
推荐替换文本：读 `paths` / `required` / `responses` ⭐⭐⭐。Swagger 是工具和旧规范名，了解即可。文档没写 `Idempotency-Key` 就不要发明（⭐⭐）。

---

## 6. P3

## ISSUE
ID：CH13-0015
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：开篇 L15；13.3 L120；13.9 表「坏凭证」
精确位置：多处
原文：当前实现与 PRD 一致；缺字段例子 `{}`；「认证后权限变化」未标不可跑（主问题见 P2）
问题等级：P3
问题类别：TERM / MiniShop / PED
问题说明：开篇「当前实现与 PRD 一致」与 R-SEARCH/BUG-001 不完全一致，文末才补。13.3 用 `{}` 讲「键不存在」在 JSON 课可以，但和下文 MiniShop 缺 qty 仍留 sku 并排，初学者会抄空对象。13.12 响应 JSON 紧凑无空格，实现 `json.dumps` 带空格——等价，但对照证据时会有人较真。
为什么有问题：都不会单独教错契约，但增加对不上的摩擦。
依据：PRD R-SEARCH；`json.dumps` 默认分隔符。
建议修改：开篇改为「购物车/登录/订单主规则与 PRD 一致；空搜索见 BUG-001」。13.3 缺字段例子改 `{"sku":"SKU-DEMO-001"}` 或标明「只演示 JSON，不是购物车报文」。
推荐替换文本：当前实现的登录、购物车、订单与 PRD 一致；空搜索仍是 BUG-001，不要写成已修复。

## ISSUE
ID：CH13-0016
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.9；13.10
精确位置：整节定义段
原文：第 9 章：GET 安全且幂等；POST 规范不保证幂等。401/403 表几乎是 08B 的接口版。
问题等级：P3
问题类别：SEQ / PED
问题说明：协议定义第 9 章已有；本章该练改 id、连点 POST。现在仍先复述再应用。不是错误（RFC 9110 GET 安全且幂等、POST 不保证幂等，表已核）。
为什么有问题：篇幅挤掉「超时后查询是否已创建」的 MiniShop 做法。
依据：RFC 9110 §9.2.1 / §9.2.2；方法表 GET yes/yes，POST no/no。
建议修改：定义一句回指 09A，本节只留 MiniShop 三行操作。
推荐替换文本：safe/幂等定义见第 9 章。本节只问：同一请求两次，业务效果一次还是两次？

## ISSUE
ID：CH13-0017
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：工作实战模板
精确位置：L449 `| 条件 | 位置 | 状态码 | Body 类型 | 库是否被改 |`
原文：Body 类型
问题等级：P3
问题类别：PED
问题说明：「Body 类型」可被理解成请求 JSON 类型或响应 Content-Type。四态课需要的是「请求形状 + 响应 error」。
建议修改：改成「请求形状 | 响应 error」。
推荐替换文本：`| 条件 | 放在哪一格 | 状态码 | 请求形状 | 响应 error | 库是否被改 |`

## ISSUE
ID：CH13-0018
文件：`chapters/13-api-testing.md`；`project/minishop/docs/openapi.json`；`project/minishop/server.py`
章节：第 13 章
小节：13.8；13.12；可运行性说明
精确位置：错误字符串当契约；401 无 `WWW-Authenticate`
原文：这四态的错误字符串与实操 13-1、`server.py` 一致。
问题等级：P3
问题类别：HTTP / JOB
问题说明：用实现字符串当教学 oracle 可以，但 OpenAPI 400 只写 `Rule or type error`。RFC 9110：产生 401 的服务端 MUST 发 `WWW-Authenticate`。MiniShop 401 无此头。正文不提，岗位上有人会拿 RFC 卡 401。
依据：RFC 9110 §15.5.2 / §11.6.1（检索核验）；本机 401 响应头无 WWW-Authenticate。
建议修改：注明 error 字符串来自当前实现，尚未写入 OpenAPI schema；401 缺挑战头是实现简化，不要写进「已符合 RFC 的认证」。
推荐替换文本：四态 error 以 `server.py` 为准，OpenAPI 尚未描述 Body。MiniShop 401 不带 `WWW-Authenticate`，这是教学实现简化。

## ISSUE
ID：CH13-0019
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：参考资料
精确位置：L658–L659
原文：`https://spec.openapis.org/oas/v3.0.3`；`https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods`
问题等级：P3
问题类别：LINK
问题说明：MDN 现行文档路径与课文一致（检索到 2025-07 页面，GET 安全/幂等、POST 均否）。OpenAPI 3.0.3 权威 HTML 为 `…/v3.0.3.html`。本环境直连被 SSRF 拦截，无后缀 URL 是否 302 **【External Verification Required】**。
建议修改：OpenAPI 链接改为 `https://spec.openapis.org/oas/v3.0.3.html`。
推荐替换文本：同上。

## ISSUE
ID：CH13-0020
文件：`chapters/13-api-testing.md`
章节：第 13 章
小节：13.11；练习 8
精确位置：L332；L577
原文：接口若返回成功，`cart_items.qty` 不得大于 `products.stock`。练习 8 用假设体 `200 {"ok":true}`。
问题等级：P3
问题类别：MiniShop / PED
问题说明：下单扣库存、不改购物车。先把购物车写成 10 再下单，会出现购物车 qty > 剩余 stock。练习 8 的 `{"ok":true}` 不是 MiniShop 成功体（购物车成功是 `{"sku","qty"}`），题目是假设，建议标「假设响应」。
依据：本机两次 `POST /api/orders` 后商品 stock 从 10 降到 8，购物车行仍在。
建议修改：一致性表加一行「下单成功后购物车未清，再改数量要用当前库存」。练习 8 标明假设。
推荐替换文本：练习 8 题干改为「假设某接口返回 `200 {"ok":true}`（不是 MiniShop 原文字段）……」。

---

## 7. 逐段问题

| 单元 | 判定 |
| --- | --- |
| 一句话核心 | 通过。能筛掉「只点页面 / 只看 200 / 用 REST 纯度报缺陷」。 |
| 开篇职责段 | 大体通过。L15「当前实现与 PRD 一致」过满，见 CH13-0015。安全边界（只打本机/授权环境）正确。 |
| 学习目标 | 通过，但 REST 条与 13.2 可跳不完全对齐（CH13-0014）。 |
| 前置知识 | 通过。HTTP 方法/状态码/头体、Cookie/Token 层次、脱敏 curl，与 8/9/11 衔接。 |
| 场景导入 + mermaid | 通过。场景 JSON `{"sku":"SKU-DEMO-001","qty":11}` 合法且与库存规则一致。流程图「文档→请求→状态码→SELECT」正确，未画三层定位（建议新增，非错误）。 |
| 13.1 接口和 API | 通过。HTTP API 不是全部接口；后厨窗口类比与后文一致。 |
| 13.2 REST | 概念通过：REST 是风格、不等于 JSON、不以纯度报缺陷、ROI 不永远最高、GraphQL/RPC 不硬套。课序/星级见 CH13-0002、CH13-0014。表中 201/401 与 MiniShop 订单/登录相符。 |
| 13.3 JSON | RFC 8259 六种值、缺键/`null`/`""`/错误类型、`0`/`false`/`[]`/`{}` 不是 null、注释/单引号/尾逗号非标准：均通过（`json.loads` 对非法样例失败）。错误类型字面量 `"11"` 见 CH13-0011；缺字段 `{}` 见 CH13-0015。 |
| 13.4 UI vs 接口 | 概念通过。互补、不能互相取消、不能因「更高级」取消手工。图见 CH13-0007。 |
| 13.5 读文档 | 通过。八条清单是岗位清单。文档与实现不一致先记问题，正确。 |
| 13.6 OpenAPI | 摘录 `json.loads` 通过，且 `/api/login.post` 与仓库文件该节点逐字段相同（`openapi=3.0.3`、`required: phone,password`、200/401）。Swagger≠OpenAPI 的史实正确。锁图标/Try it out 见 CH13-0008。 |
| 13.7 四格 | 概念通过。query 非 GET 专属（RFC 9110 请求目标可带 query）；密码不进 query 正确。`mouse` 空列表实测成立。空搜索判定缺失见 CH13-0009。Content-Type 见 CH13-0005。 |
| 13.8 四态+边界 | **表**与 `server.py`、13-1 一致（本机 8 行全中）。**图**见 CH13-0001。登录 curl 过晚见 CH13-0003。`qty=1.0`（JSON number → Python float）会 `wrong type qty`，表未列，属岗位缺口见 §13。 |
| 13.9 权限 | 401/403 语义与 RFC 9110 / MDN 一致；正文写明项目可能混用、以契约为准。横向越权 MiniShop **403**、管理员打 `GET /api/orders/{id}` 也是 403：实测成立，且符合 PRD R-PERM 与 OpenAPI summary。禁用用户见 CH13-0013。Body 不得带他人数据：B 读 A → `{"error":"forbidden"}` 无 id，通过。 |
| 13.10 幂等 | GET 安全且幂等、POST 不保证：与 RFC 9110 方法表一致。购物车「设为 2 两次仍是 2」符合本实现 upsert。创建订单两次两个 id：实测成立。登录行见 CH13-0010。支付/Idempotency-Key 见 CH13-0013/0014。超时后查询：原则对，MiniShop 无专门超时模拟。 |
| 13.11 一致性 | 通过。组合表能定位层。库存不得 qty>stock 作为购物车规则成立；下单后购物车不清见 CH13-0020。 |
| 13.12 登录 | 路径 `/api/login`、密码在 Body、错误密码 401、token + `Set-Cookie` `HttpOnly` `Path=/`、Cookie 与 Bearer 并存非三选一：与 PRD R-AUTH、实测一致。无 `/api` 的 `/login` → 404，实测成立。报文成帧见 CH13-0004。curl `-d` 隐含 POST，命令可跑。 |
| 13.13 订单 | 201 + 仅 `id`、无 `status`、无认证 401、两次不同 id：全部实测成立。sku/qty/库存措辞见 CH13-0006。TOKEN 管道不用 `-D -`，正确。 |
| 工作实战 | 四态已对齐 13-1（旧审查「漏空串」已修）。缺放错格子见 CH13-0012。完成标准禁止编造订单状态、禁止明文密码：通过。模板列名见 CH13-0017。 |
| 常见错误 1–10 | 通过。覆盖 REST 纯度、四态、200 不看 Body、query 密码、UI/接口互相取消、Cookie 三选一、未授权扫描、只看第一次 201、打 `/login`。未触犯质量标准六条禁令。错误 4「安全方法」沿用第 9 章 RFC 含义，不是「POST 更安全」神话。 |
| 面试五题 | 通过。结论→原理→场景→示例→边界；不把接口 ROI 绝对化；401/403 以契约为准。 |
| 小练习 + 答案 | 见 §11。无 【ANSWER VERIFICATION FAILED】。 |
| 检查清单 / 门槛 / 总结 | 通过。能指向 serve + `/api/login` + 四态。 |
| 可运行性说明 | curl 类声明与本机结果一致（登录 200、错密 401、qty 10/11、四态 error、订单两次 201 无 status）。未声明 HTTP/1.1 与 Content-Length，和 13.12 示例的缺口一致。 |
| 参考资料 / 预告 | 章内链文件均存在。不抢第 14 章 Collection/`pm.test`。链接见 CH13-0019。 |

---

## 8. 代码问题

### 8.1 正文 JSON（全部重新 `json.loads`）

| 块 | 结果 |
| --- | --- |
| 场景 `{"sku":"SKU-DEMO-001","qty":11}` | 合法对象 |
| 13.3 `{"sku":"SKU-DEMO-001","qty":1}` | 合法对象 |
| OpenAPI 摘录 | 合法；`paths./api/login.post` 与 `project/minishop/docs/openapi.json` 该节点相等 |
| 行内对象（`{}`、`null`、`""`、`"11"`/`"1"`、qty 1/10/11、登录 Body、下单 Body） | 全部合法 |
| 课文声称非法：单引号、尾逗号、注释 | `json.loads` 均失败，与 RFC 8259 一致 |

### 8.2 正文 HTTP / curl（重新推导 + 实跑）

| 示例 | 结果 |
| --- | --- |
| `python3 project/minishop/run.py serve` | 命令形状正确（本轮用 MiniShopLab 等价拉起，避免占用 8765） |
| curl 登录（无 `-X`，`-d` 隐含 POST） | 等价请求 200，JSON 含 `result/token/role`，`Set-Cookie: minishop_session=…; HttpOnly; Path=/` |
| 错误密码 | 401 `{"result":"fail"}` |
| `POST /login` | 404 `{"error":"not found"}` |
| TOKEN `$()` + `POST /api/orders` | 201 `{"id":"ord-…"}`，无 `status`；再发一次不同 id |
| 13.12 手写 HTTP/1.1 **无 Content-Length** | **400 missing field**（CH13-0004） |
| 同上 **有 Content-Length** | 200 |
| 真实状态行 | `HTTP/1.0 200 OK`，不是课文的 HTTP/1.1 |

### 8.3 实操代码

`practice/13-api-shapes/main.py`：标准库 + `_http`/`_minishop`，隔离临时库，先登录再四态，断言状态码与 error 字符串。`CASES` 与 13.8 表、README 表一致。`json.dumps({"qty": None})` 正确发出 JSON `null`。

`tests/test_lab.py`：`main()==0` 且四行 name/ok。`--check` 0.52s OK。

问题：脚本代发，读者不改 Body（CH13-0012）。实现质量本身无语法/import 错误。

### 8.4 OpenAPI vs PRD vs 实现（本章口径）

| 项 | OpenAPI | PRD | 实现 | 正文 |
| --- | --- | --- | --- | --- |
| `/api/login` POST | 有 | R-AUTH | 有 | 有 |
| 登录 200 token | 描述「OK with token」无 schema | token + Set-Cookie | 两者都有 | 13.12 完整 |
| 购物车 required sku+qty | 有 | R-CART | 有，且区分 missing/null/type | 13.8 表正确 |
| 订单 required sku+qty | 有 | R-ORDER | 缺任一 → `missing field` | 13.13 漏 qty（CH13-0006） |
| 订单 201 仅 id | 「Created id」 | 无 status | `{"id"}` | 正确 |
| 订单不幂等 | summary 写了 | R-ORDER | 两 id | 正确 |
| 他人订单 403 | 写了 admin 也 403 | R-PERM | 403 | 正确 |
| `security` | **无** | Bearer 为准 | Bearer 或 Cookie | 13.6 教锁图标（CH13-0008） |
| 空搜索 | 未写否定规则 | R-SEARCH | BUG-001 全量 | 13.7 弱（CH13-0009） |

---

## 9. 图片问题

四张 PNG 均用 `read_file` 打开；四张 HTML 逐行对照。PNG 与 HTML 文案一致，未见截图错版。

### IMG-CH13-001
文件：`chapters/assets/diagrams/ch13-ui-vs-api.png` + `.html`
出现位置：13.4
图片主要内容：店门（UI）vs 后厨窗口（接口），不能互相取消。
技术准确性：分工正确。后厨示例 Body 缺 sku/Bearer，400 的原因会被误当成库存规则。
与正文一致性：场景导入用完整 sku+qty=11，图更简，不一致。
文字是否正确：caption「pytest 全绿仍可能首页点不开」作为一般命题成立；MiniShop `test_home_has_login_and_register_form` 其实打了首页 HTML，略满。
UI 是否过时：示意图，无工具 UI。
教学价值：高，是本章分工句。
可读性：好。
是否需要修改：是
修改建议：后厨 Body 改为带 sku 的 qty=11，并写 Bearer。
最终结论：**MODIFY**

### IMG-CH13-002
文件：`chapters/assets/diagrams/ch13-four-slots.png` + `.html`
出现位置：13.7
图片主要内容：Path/Query/Header/Body 四格；命题「测错格子，等于没测到」。
技术准确性：四格职责正确；密码不进 Query、qty 进 Body 正确。Query「空搜索」无 BUG-001 判定。Body 把缺/null/""/"1"/0/11 混成「各是一条」，四态与边界未分开（表里是分开的）。
与正文一致性：caption 已无教学 `/login`（旧审查 CH13-05 已修）。盒子为 `/api/orders`、keyword、Bearer，与 v1.0 一致。
文字是否正确：是。
UI 是否过时：否。
教学价值：高，本章脊柱图。
可读性：好。
是否需要修改：小改 Query 判定即可。
最终结论：**MODIFY**（轻：Query 补 BUG-001；Body 可注明 0/11 是边界不是四态）

### IMG-CH13-003
文件：`chapters/assets/diagrams/ch13-four-shapes.png` + `.html`
出现位置：13.8
图片主要内容：缺字段 / null / 空串 / `"1"` 四条用例。
技术准确性：**不合格**。自称 MiniShop 购物车 Body，2–4 格缺 `sku`，实测全是 `missing sku`，不是图上的 `null qty` / `wrong type qty`。第一格带 sku，内部也不自洽。
与正文一致性：与 13.8 表、13-1 冲突。
文字是否正确：命题句（JSON 合法 ≠ 同一用例）正确；MiniShop error 标注错误。
UI 是否过时：否。
教学价值：命题需要这张图，但当前会教错 oracle。
可读性：好。
是否需要修改：是，必须改 JSON。
最终结论：**REPLACE**（或 MODIFY 到与 13.8 表逐字节相同）

### IMG-CH13-004
文件：`chapters/assets/diagrams/ch13-401-403.png` + `.html`
出现位置：13.9
图片主要内容：401 没认出你 / 403 认出你但不许进。
技术准确性：与 RFC 9110 401/403 方向一致；MiniShop 无凭证下单 401、普通用户 `/api/admin/products` 403、B 读 A 订单 403，均实测成立。caption 要求断言 Body 无他人订单 id，正确。
与正文一致性：好。
文字是否正确：是。「密码错误」是登录 401，与「没带 token」不是同一资源，但对初级比喻可接受。
UI 是否过时：否。
教学价值：高，与 08B 页面权限互补。
可读性：好。
是否需要修改：否
最终结论：**KEEP**

缺图（建议，不算现行错误）：13.10「两次 POST /api/orders → 两个 id」；13.11 接口/库/页面三列。优先修四态图，不必先加新图。

---

## 10. 表格问题

| 表 | 结论 |
| --- | --- |
| 13.2 REST 约定 | 通过。不以 REST 纯度报缺陷。 |
| 13.3 JSON 四态 | 概念通过；`"11"` 见 CH13-0011。 |
| 13.4 UI vs 接口 | 通过。 |
| 13.7 四格 | 通过；Query 空搜索缺判定 CH13-0009。 |
| 13.8 购物车用例 | **通过且与实现一致**（本轮主表，不再是旧审查里缺 sku 的那版）。 |
| 13.9 权限 | MiniShop 403 行正确；禁用用户行不可跑 CH13-0013。 |
| 13.10 幂等 | 订单行正确；登录行 CH13-0010；支付行 CH13-0013。 |
| 13.11 一致性组合 | 通过。 |
| 工作实战异常表 | 列名「Body 类型」歧义 CH13-0017。 |
| practice README 四态表 | 与 13-1、server 一致。 |

---

## 11. 练习与答案问题

### 11.1 独立作答（先解题，再对教材答案）

**练习 1**  
独立：页面可能限制输入或根本不暴露参数；隐藏接口、错误类型、改 Path id 只有直接打 API 才稳。例：输入框 max=10 时页面加购成功，接口仍可能接受 `qty=11`。  
对照：一致。

**练习 2**  
独立：不是一回事。测试听已发布文档和实现，不拿 REST 纯度当缺陷。  
对照：一致。

**练习 3**  
独立：A。`{"qty":null}` 与 `{}` 在 JSON 里分别是空值 vs 缺键；B、C 是重复合法输入。  
对照：一致。

**练习 4**  
独立：缺 `phone`、缺 `password`、两者都缺；再加 `null` 与 `""`（若文档未等同）。  
对照：一致。  
附注：MiniShop 登录对 `phone:null`/`""` 走 401 而不是 400（键在，查无此人）。题目问的是「应设计哪些失败用例」，不是预测状态码，**不记 ANS FAIL**。

**练习 5**  
独立：Query/Header 是测「放错格子会不会被误接受」；合法 qty 在 Body。实测 Query `qty=11` 被忽略。  
对照：一致。

**练习 6**  
独立：MiniShop 应 403；Body 无 A 的订单明细；B 自己的资源未被改。只看「页面打不开」不够。  
对照：一致。实测 `403 {"error":"forbidden"}`，无 `id`。

**练习 7**  
独立：说明创建 POST 默认不幂等。若产品要求一次业务一笔，缺陷应写重复 POST 多个 id，附两次响应和行数。  
对照：一致。实测两个不同 id。

**练习 8**  
独立：持久化/规则层；不要写成「前端显示不对」。  
对照：一致。题干 `{"ok":true}` 不是 MiniShop 原文，见 CH13-0020。

**练习 9**  
独立：C。A 是 ROI 绝对化；B 把 Bearer 当成 REST 定义；D 是 GET/POST 安全神话。  
对照：一致。

**练习 10**  
独立：方法 POST；路径 `/api/login`；JSON Body 含 phone/password；200 且有 token 与 Set-Cookie HttpOnly；错误密码 401；后续 Bearer 访问 `/api/cart`。不写订单状态。  
对照：一致。

无 【ANSWER VERIFICATION FAILED】。

工作实战与 13-1 四态口径已对齐（旧「空串被 qty=11 顶替」已修）。缺口是放错格子未进必做（CH13-0012）。

### 11.2 阶段测验第 13 章题（独立作答后对照）

测验文件答案同页，读取时可见；仍按技术事实重解。

| 题 | 独立答案 | 教材答案 | 对照 |
| --- | --- | --- | --- |
| Q1 接口 vs UI | 接口：规则/数据/权限/组合；UI：按钮/跳转/文案。页面挂了接口绿仍可能失败，不能互相取消。 | 接口稳定、适合规则和权限；UI 看按钮跳转文案。页面挂了接口绿仍可能失败。 | 一致 |
| Q2 四态为何分开（必过） | JSON 不是同一件事，校验分支不同；不能合成一条「异常」。 | JSON 里不是同一件事，服务端常走不同分支。 | 一致 |
| Q3 登录口径 / `POST /login` | 以 PRD + OpenAPI 为准；路径 `/api/login`；无前缀 `/login` → 404。 | 同左。 | 一致；本机 404 |
| Q8 ROI（本章也写了） | 不是永远最高。 | 不是。全新天天改文案的页面不适合先自动。 | 一致 |
| Q10 | B。`requests.post(..., json={})` 发 JSON Body。 | B | 一致（考点跨 15/16，口径与本章不冲突） |

Q4–Q7、Q9 属 14/16/19，本 Agent 不扩审他章正文。

---

## 12. 初学者理解障碍

标记 【Beginner Friction】：

1. **第一发太晚。** 读完 REST、OpenAPI 摘录、Swagger UI，还没有亲手发出过登录。13-1 会绿，但那是脚本的绿。
2. **「可跳 REST」无法执行。** 可跳条件是「会填四格」，四格在后面。
3. **Bearer 还没拿到就出现四态表。** 先 401 再 400，两种失败叠在一起。
4. **图比表更抢眼，图还缺 sku。** 初学者抄图不抄表。
5. **error 字符串当标准答案，OpenAPI 里找不到。** 对照「完整文件」会以为自己看错文档。
6. **HTTP 报文示例按字面发送会 400。** 已会 curl 的人没事；正在学「报文长什么样」的人会卡住。
7. **`qty=1.0`、错误 Content-Type 在 MiniShop 上的真实结果与课文「常见」不一致**，没有「你在本项目上会看到什么」的旁注。
8. **空搜索 / `mouse` / 四态 / 库存 11** 四种「空或异常」容易被捏成一类，13.7 没有把 BUG-001 拉回来当尺子。

---

## 13. 岗位能力缺口

标记 【Job Reality Gap】：

1. 契约测试（schema 断言、OpenAPI 响应校验）只教到「看 responses 列表」，没有把 MiniShop 缺 error schema 当成缺陷示例。
2. 放错格子（Query 里的 qty、Header 里的业务字段）是真实漏测点，本章停留在练习 5。
3. JSON number 在不同语言里的 int/float（Python `1.0` → `wrong type qty`）未提，线上常见。
4. 401 与 `WWW-Authenticate`、Bearer 大小写、过期 token 与乱码 token 的细分，表里有「坏凭证」无 MiniShop 实验。
5. 创建超时后的「查是否已创建」只有原则，没有 `GET /api/orders/{id}` 步骤。
6. 下单不清理购物车、库存被订单改写后购物车 qty 可能大于剩余 stock，是数据一致性点，13.13 未提。
7. 重复登录是否吊销旧 session，13.10 的「通常同一会话」与大量真实系统（含 MiniShop）不符。
8. 初级招聘还会问分页、版本号 `/v1`、限流 429、幂等键——正文诚实不展开可以，但应标明「入职后再学」，避免学生以为四格+四态=接口测试全集。

未把「接口自动化 ROI 永远最高」写成岗位真理：通过。

---

## 14. 建议删除内容

- 不必删除 REST 节，删除的是它的**位置和强制星级占用**（已 ⭐⭐，还要后移）。
- 13.10 支付回调行：删出 MiniShop 操作表，改到「一般风险、本项目没有」。
- 13.6 不要让学生以为仓库里有 Swagger UI 可点 Try it out。
- 不要恢复任何无 `/api` 的 `/login` 可抄示例（现行已无，保持）。

---

## 15. 建议新增内容

1. 13.1 之后立刻给出四格 + 最小登录 curl（serve、`/api/login`、Bearer）。
2. 四态图与 13.8 表使用**同一组**带 `sku` 的 Body。
3. 工作实战第 5b 条：同一 `qty=11` 放进 Query。
4. 一句 MiniShop 特例：不校验 Content-Type；401 无 `WWW-Authenticate`；响应是 HTTP/1.0。
5. Query 空关键字指向 BUG-001。
6. 可选：`qty: 1.0` 作为「看起来像整数、语言层是 float」的一条。
7. 13.13 补 OpenAPI `required: [sku, qty]`，并说明下单也会拒绝超库存。

---

## 16. 建议重写内容

### 16.1 课序（13.2–13.8）

建议顺序：13.1 接口是什么 → **四格** → **最小登录 curl** → JSON 四态（对着已登录购物车）→ 读文档/OpenAPI → REST 可跳 → 权限/幂等/一致性 → 登录/订单细节。

### 16.2 四态图 JSON（替换 CH13-0001）

四格均使用：

```json
{"sku":"SKU-DEMO-001"}
{"sku":"SKU-DEMO-001","qty":null}
{"sku":"SKU-DEMO-001","qty":""}
{"sku":"SKU-DEMO-001","qty":"1"}
```

error 仍为 `missing qty` / `null qty` / `wrong type qty` / `wrong type qty`。脚注：本实现 3 与 4 文案相同，记录仍要分开。

### 16.3 13.12 HTTP 示例（替换 CH13-0004）

```http
POST /api/login HTTP/1.1
Host: 127.0.0.1:8765
Content-Type: application/json
Content-Length: 45

{"phone":"13800138000","password":"Test1234"}
```

并注明：用 curl 时不必手写 Content-Length；MiniShop 当前状态行是 `HTTP/1.0 200 OK`，`Content-Type: application/json; charset=utf-8`。按课文省略头去裸发 TCP，Body 不会被读到。

### 16.4 13.8 前最小登录（插入）

```bash
python3 project/minishop/run.py serve
curl -sS -H "Content-Type: application/json" \
  -d '{"phone":"13800138000","password":"Test1234"}' \
  "http://127.0.0.1:8765/api/login"
```

路径是 `/api/login`。把 `token` 放进 `Authorization: Bearer`。没有 `/api` 的 `/login` 是 404。

---

## 17. 本章结论

**C 明显需要修改**

不是 E（重新设计）：REST≠JSON、四态、401/403、POST 不幂等、订单无 status、禁止 `/login`、13-1 可跑，骨架对。  
不是 A/B：核心章有一张会给错 MiniShop oracle 的四态图、HTTP 报文按 RFC 不可裸发、四格和登录仍排在 REST/文档/四态之后。  
达到 C：修图、补 Content-Length、把四格和最小登录前移、对齐 OpenAPI/实现旁注后，可再评是否升 B。

质量标准 DoD（本章）：

| # | 项 | 结果 |
| ---: | --- | --- |
| 1 | 目标明确 | 通过 |
| 2 | 前置知识正确 | 通过 |
| 3 | 无知识性错误 | **失败**（四态图 oracle；HTTP 示例成帧） |
| 4 | 重要信息未过时 | 通过（RFC 8259 / 9110 / OpenAPI 3.0.3） |
| 5 | 无错误绝对化 | 通过 |
| 6 | 术语准确 | 通过（401/403、safe/幂等沿 RFC） |
| 7 | 零基础能理解 | 弱（课序） |
| 8 | 示例具体 | 弱（报文不可裸发） |
| 9 | 有实际工作场景 | 通过 |
| 10 | MiniShop 一致 | **失败**（图、13.13 sku-only、HTTP/1.1 vs 1.0、OpenAPI 锁图标） |
| 11 | 代码经过验证 | 部分（curl/13-1 通过，手写 HTTP 失败） |
| 12 | SQL 操作安全 | 不适用但满足（只指向授权 SELECT） |
| 13 | 图表帮助理解 | **失败**（四态图会给错判定） |
| 14 | 知识重要级别明确 | 弱（除 REST 外仍几乎全 ⭐⭐⭐） |
| 15 | 常见错误有价值 | 通过 |
| 16 | 面试题非死记硬背 | 通过 |
| 17 | 练习覆盖目标 | 弱通过（缺强制放错格子） |
| 18 | 答案与练习对应 | 通过 |
| 19 | 检查清单可验证 | 通过 |
| 20 | 衔接下一章 | 通过 |

**17/20（3 项明确失败）。17 及以下不得发布。** 核心章目标 95，本轮 73。

旧结论处理：v1.2.1「91、双路径」——双路径现行已修，91 不再适用。阶段 5 复审 88 的「正文 curl 打教学服务会 404」——现行 curl 打 `/api/login`，该项关闭。教学审查 CH13-04（工作实战漏空串）、CH13-05（四格图教学 `/login` caption）现行已修。CH13-01/02/03（课序）未完全落地。

---

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`
- `README.md`、`docs/COURSE_CONTROL.md`、`docs/COURSE_OUTLINE_v1.2.md`、`docs/LEARNING.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`、`practice/STATUS.md`、`exercises/README.md`
- `project/minishop/README.md`
- `chapters/13-api-testing.md`（全文）
- `practice/13-api-shapes/README.md`、`main.py`、`tests/test_lab.py`、`validation/latest.json`（跑后）
- `practice/run.py`、`practice/_http.py`、`practice/_minishop.py`
- `project/minishop/docs/openapi.json`（全文）
- `project/minishop/docs/PRD.md`（全文）
- `project/minishop/server.py`（登录/鉴权/购物车/订单/JSON 读取）
- `project/minishop/tests/test_api.py`（对照口径，未扩审第 16/19 章）
- `project/minishop/evidence/http/01-login-ok.txt`、`06-order-create.txt`
- `chapters/quizzes/README.md`、`chapters/quizzes/stage-5-api.md`（第 13 章题）
- `reviews/chapter-13-review.md`、`reviews/_pedagogy-2026-09-10/ch13.md`（线索）
- `reviews/v1.2.1-rescore.md`、`reviews/_rereview-2026-09-09/stage-5-ch13-16.md`（线索，不继承分数）
- `chapters/assets/diagrams/README.md`
- 示意图：`ch13-ui-vs-api` / `ch13-four-slots` / `ch13-four-shapes` / `ch13-401-403` 的 png+html 共 8 个文件

未读其他章正文。

### 实际跑过的命令与结果摘要

```text
python3 practice/run.py 13-1
→ exit 0
  missing     400 missing qty OK
  null        400 null qty OK
  empty_str   400 wrong type qty OK
  wrong_type  400 wrong type qty OK
  证据 practice/13-api-shapes/validation/latest.json

python3 practice/run.py 13-1 --check
→ unittest test_four_shapes ... ok  (0.523s)
```

MiniShopLab 对照（与 `server.py` 同一套 handler）：

- 登录 200，`result=ok`，token，`role=user`，无 `status`；`Set-Cookie: minishop_session=…; HttpOnly; Path=/`
- 错密码 401；`POST /login` 404
- 购物车 13.8 表 8 行：1/10 → 200；11 → `qty exceeds stock`；缺 qty / null / `""` / `"1"` / 0 → 与课文 error 一致
- 图上无 sku 的 Body：全部 `missing sku`
- 无 Bearer：401 `unauthorized`
- Query `qty=11` + Body `qty=1` → 200 qty=1；Query 11 + 缺 Body qty → `missing qty`
- Content-Type 标成表单、Body 仍是 JSON → **200**（不是 415）
- 裸 TCP 无 Content-Length 登录 → **400 missing field**，状态行 HTTP/1.0
- 有 Content-Length → 200
- `qty: 1.0` → `wrong type qty`
- `keyword=mouse` → `items: []`；空 keyword → 3 件（BUG-001）
- 订单两次 201、不同 id、无 status；`qty=11` 下单 400 `qty exceeds stock`；缺 qty/sku → `missing field`；null qty → `wrong type qty`（订单不区分 null）
- B 读 A、管理员读 A 的 `GET /api/orders/{id}` → 403；普通用户 `/api/admin/products` → 403
- 两次登录两个 token，旧 token 仍能 200 读购物车
- 401 响应无 `WWW-Authenticate`

正文 JSON 块与 OpenAPI 摘录均 `json.loads` 成功。

### 外部核查

| 条目 | 来源 | 结论 |
| --- | --- | --- |
| JSON 值与禁止注释/单引号/尾逗号 | RFC 8259（检索 + `json.loads`） | 课文正确 |
| GET 安全且幂等、POST 否 | RFC 9110 方法表；MDN Methods | 课文正确 |
| 请求体由 Content-Length 或 TE 成帧 | RFC 9112 §6 | 13.12 示例不完整 |
| 401 / 403 方向 | RFC 9110 §15.5.2/15.5.4；MDN Authentication | 课文方向正确；401 MUST `WWW-Authenticate` MiniShop 未做 |
| 415 Unsupported Media Type | RFC 9110 §15.5.16 | 「常见 415」行业正确，MiniShop 不返回 |
| OpenAPI 3.0.3 | spec.openapis.org / OAI 发布说明 | 版本存在；无后缀 URL 直连 【External Verification Required】 |
| MDN Methods URL | 检索到 `…/Web/HTTP/Reference/Methods` | 路径与课文一致 |
| RFC/MDN/OpenAPI 页面正文 | `web_fetch` SSRF 拦截 198.18.0.0/16；web-reader MCP 余额不足 | 未能打开 RFC HTML 原文；结论来自检索摘要 + 实现实验 |

未改教材、practice、project。本文件为该章唯一写入。
