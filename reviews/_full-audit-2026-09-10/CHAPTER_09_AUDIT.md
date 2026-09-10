# Chapter 09 Audit

审计角色：Chapter-Audit-Agent-09  
范围：第 9 章全部（索引 + 09A 语义 + 09B 报文观察 + 实操 9-1 + 第 9 章测验题 + 本章示意图 + MiniShop HTTP 证据抽核）  
日期：2026-09-10  
禁止：未审其他章正文。HTTP 按 RFC 9110/9111/9112、RFC 10008、RFC 5789 核查，不以记忆下死结论。

## 1. Coverage

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 索引页（`09-computer-network-and-http.md`） | 1 页 / 14 行 | 14 行 | **0** |
| 09A 二级标题 | 21 | 21 | **0** |
| 09A 三级标题 | 21 | 21 | **0** |
| 09B 二级标题（不含模板代码块内伪标题） | 19 | 19 | **0** |
| 09B 三级标题 | 21 | 21 | **0** |
| 实操 README 二级标题 | 4 | 4 | **0** |
| 正文段落/空白分隔块（09A+09B） | 85 + 60 | 145 | **0** |
| 列表项（09A+09B+索引） | 60 + 65 + 2 | 127 | **0** |
| 检查清单项 | 8 + 6 | 14 | **0** |
| 表格 | 09A 9 + 09B 8 + 实操 1 = 18 | 18 | **0** |
| 代码围栏块 | 09A 6 + 09B 6 + 实操 1 = 13 | 13 | **0** |
| mermaid 图 | 3 | 3 | **0** |
| Linux/Shell 命令 | 3 | 3（9-1 已实跑） | **0** |
| SQL | 0 | 0 | **0** |
| HTTP 示例（教学 GET、反例、可抄登录、后续 GET、练习报文、示意图路径） | 10 | 10（均重新推导） | **0** |
| 测试用例（`tests/test_lab.py`） | 1 | 1 | **0** |
| Bug 示例（独立编号） | 0（仅「缺陷标题或未发现协议级异常」占位） | 0 | **0** |
| 练习题 | 09A 5 + 09B 5 + 实操 9-1 + 测验第 9 章 3 题 = 14 | 14（先独立作答） | **0** |
| 标准答案 | 10 + 测验 3 | 13 | **0** |
| 示意图 PNG | 6 | 6（`read_file` 打开） | **0** |
| 示意图 HTML | 6 | 6 | **0** |
| Markdown 图片引用 | 6 | 6 | **0** |
| 内部链接 | 全部解析 | 全部存在 | **0** |
| 外部链接 | 5 | 5（检索确认；本环境 rfc-editor/MDN 被 SSRF 拦截，见 §18） | **0** |
| MiniShop `evidence/http/*.txt` | 9 | 9 | **0** |
| `network-log.html` | 1 | 1 | **0** |
| practice 源码（`main.py` / `tests/test_lab.py` / `_http.py` / `_minishop.py`） | 4 | 4 | **0** |
| 阶段测验全文（只评第 9 章题 4/5/9；1–3、6–8、10 属第 8/10 章，不审他章正文） | 3 题 | 3 | **0** |

Coverage：**100%**。未检查列全为 0。

单元清单（每条均已读并判定，问题见对应 ID）：

**索引 `09-computer-network-and-http.md`：** 一句话核心、拆章说明、09A/09B 链接、作业划分、实操 9-1、阶段测验 3、下一章指针。

**09A：** 章问题 / 学习目标 / 前置 / 场景导入 / 9.1 地图 / 9.2 IP·端口 / 9.3 TCP·UDP / 9.4 三次握手 / 9.5 HTTP 形状 / 9.6 HTTPS·TLS / 9.7 方法 / 9.8 GET·POST / 常见错误 1–6 / 面试三题 / 练习 1–5 与答案 / 清单与自测门槛 / 总结 / 可运行性 / 参考资料 / 下一节。

**09B：** 节问题 / 目标 / 前置 / 场景 / 9.9 四格 / 9.10 状态码 / 9.11 Header / 9.12 Body / 9.13 登录报文 / 工作实战模板 / 常见错误 1–5 / 面试两题 / 练习 6–10 与答案 / 清单与门槛 / 总结 / 可运行性 / 参考资料 / 下一章。

**实操：** README 目标/命令/验收；`main.py` 四格打印与脱敏；`test_lab.py` 断言 POST `/api/login` + token + Set-Cookie 且证据无 `Test1234`。

**图：** `ch09-ip-port` / `ch09-tcp-knock` / `ch09-https-wrap` / `ch09-get-post` / `ch09-http-letter` / `ch09-status`（html+png）。

## 2. 总评分

| 项 | 分数 |
| --- | ---: |
| 技术准确性 | 9/10 |
| 岗位实用性 | 8/10 |
| 完整性 | 8/10 |
| 初学者友好度 | 7/10 |
| 教学顺序 | 8/10 |
| 代码质量 | 8/10 |
| 实操质量 | 7/10 |
| 练习质量 | 8/10 |
| 图片质量 | 7/10 |
| 结构与表达 | 8/10 |
| **总体** | **78/100** |

（审计模板列了 9 个 10 分项 + 总体/100。为凑 10×10，将质量标准中的「结构与表达」补为第 10 项。9 项合计 70，加结构 8 = **78**。）

评分依据：GET/POST 的 safe / 幂等 / 可缓存拆分与 RFC 9110 §9.2 对齐，且明确禁止「GET 不安全、POST 安全」，这是本章主课，给技术 9。扣分来自 MiniShop 可抄报文与实装不完全同构、405/401 的 RFC MUST 被写成观察语气、示意图 `keyword=mouse` 打在 `/api/products` 上会空列表、实操代填四格。无 P0。不因篇幅给高分。旧审查 99/94 与教学审查 20/30 **只作线索，分数独立给出**。

Definition of Done（对照质量标准 20 项，本章）：约 **18/20**。待修：示例与 MiniShop 实装同构（项 8/10）、图表 keyword（项 13）。项 3 核心 HTTP 语义通过；405 Allow / 204 措辞为周边瑕疵，不单独打掉「无知识性错误」整项。**修正 P1 与关键 P2 后可按发布线考虑；当前不是 20/20。**

## 3. P0

无。下列禁止项均未在本章以错误绝对化形式教授：

- 「GET 不安全、POST 安全」——09A §9.8、常见错误 1、练习 3、测验 Q4 均反着打。
- Cookie / Session / Token 三选一——09B 错误 3、实操 9-1 结论、R-AUTH 口径一致。
- 可抄 `POST /login` 当作 MiniShop——已改为反例框，无完整请求行（旧 P0 已不在现行正文）。

## 4. P1

```
## ISSUE
ID：CH09-0001
文件：chapters/assets/diagrams/ch09-get-post.html；chapters/assets/diagrams/ch09-get-post.png
章节：第 9 章（上）§9.8
小节：GET 与 POST 示意图
精确位置：左卡 monospace 行 `GET /api/products?keyword=mouse`；配图标题「货架上现在有哪些鼠标？」
原文：GET /api/products?keyword=mouse
问题等级：P1
问题类别：IMG / HTTP / MiniShop
问题说明：图使用 MiniShop v1.0 真实路径 `/api/products`，却配英文 keyword `mouse`。种子商品名是「无线鼠标」「键盘」「耳机」，SKU 为 `SKU-DEMO-001` 等。`keyword` 按 name/sku 小写包含匹配，`mouse` 不会命中。
为什么有问题：学生按图对 MiniShop 做 09B 书面 GET 观察，会得到 HTTP 200 且 `items: []`，和图上「货架上有鼠标」相反，容易误判搜索坏了，或与 BUG-001（空关键字返回全量）搅在一起。09A 正文教学 URL 用的是未冻结的 `/products?keyword=mouse`，图却升级成 `/api/`，标签纪律在图上掉了。
依据：本次对 MiniShopLab 实发 `GET /api/products?keyword=mouse` → `200 {"items": []}`；`server.py` `_get_products`；PRD 教学数据。RFC 不涉及此条，这是案例一致性。
建议修改：路径保留 `/api/products` 时改 keyword 为 `鼠标` 或 `SKU-DEMO-001`；若坚持 `mouse`，改回未冻结教学路径 `/products` 并标明「不是 MiniShop v1.0」。
推荐替换文本：`GET /api/products?keyword=鼠标`（旁注：v1.0 商品名是中文，「mouse」会空列表）。
```

## 5. P2

```
## ISSUE
ID：CH09-0002
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：§9.13 示例：MiniShop v1.0 的 JSON 登录
精确位置：可抄请求/响应两块（约 L191–204）
原文：
POST /api/login HTTP/1.1
…
HTTP/1.1 200 OK
Content-Type: application/json
Set-Cookie: minishop_session=<redacted>; Path=/; HttpOnly
{"result":"ok","token":"<redacted>"}
问题等级：P2
问题类别：HTTP / MiniShop
问题说明：本节自称「唯一可对照、可抄」的 MiniShop v1.0 报文。实装与 evidence 为：状态行 HTTP/1.0（BaseHTTPRequestHandler 默认）、`Content-Type: application/json; charset=utf-8`、`Set-Cookie: …; HttpOnly; Path=/`、Body 含 `role`。本次实跑 Body：`{"result": "ok", "token": "…", "role": "user"}`；`urllib` `resp.version == 10`。
为什么有问题：实操 9-1 会打印 `keys=['result', 'token', 'role']`。学生对照「可抄报文」会以为自己多出来的 `role` 或 HTTP/1.0 是环境错误。关键字段（POST、`/api/login`、token、Set-Cookie HttpOnly）是对的，所以不是 P0/P1，但「可抄=实装」的承诺过满。
依据：本次 `python3 practice/run.py 9-1`；`evidence/http/01-login-ok.txt`；`evidence/linux/curl-login-headers.txt`（`HTTP/1.0 200 OK` / `BaseHTTP/0.6`）；`server.py` `_login` / `_json`。RFC 9112 允许教学用 HTTP/1.1 纸面形状，但必须标明与实装差异。
建议修改：保留 HTTP/1.1 纸面形状，加一行实装注记；Body 补 `role` 或写「应用还可能返回 role，以 OpenAPI/实际为准」。
推荐替换文本：在响应块后增加：「纸面按 HTTP/1.1 写。MiniShop v1.0 跑在 Python `BaseHTTPRequestHandler` 上，curl -v 常见 `HTTP/1.0`；Body 实装还有 `role`。对比时看方法、路径、token、Set-Cookie，不要为版本号或多余字段报缺陷。」
```

```
## ISSUE
ID：CH09-0003
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：§9.13「登录失败时看什么」；并波及 §9.10 的 405/415
精确位置：失败观察表 405 / 415 / 429 / TLS 行（约 L225–228）
原文：`405` 方法不被该路径接受；`415` Content-Type 不匹配；`429` 尝试次数过多；TLS 失败
问题等级：P2
问题类别：HTTP / TEST / MiniShop
问题说明：该表挂在「阅读 MiniShop 登录请求」下。对 MiniShop 实发：`GET /api/login` → **404** `{"error":"not found"}`，无 `Allow`；错误 `Content-Type` 仍按字节 `json.loads`，失败是 **400** invalid json，从不 415；无验证码/限流，无 429；v1.0 明确不做 HTTPS，无 TLS 失败。
为什么有问题：学生按表在 MiniShop 上找 405/415，会找不到，回头怀疑自己抓包。RFC 语义本身没错，错在没把「通用诊断」和「本仓库会看到的码」分开。
依据：本次实发 GET `/api/login`、POST `/login` 均为 404；`do_GET` 对 `/api/*` 未匹配即 404；`_read_json` 不读 Content-Type；PRD 非范围「正式域名、HTTPS」。RFC 9110 §15.5.6：路径存在但不允许该方法才是 405。
建议修改：表分两列「通用」/「MiniShop v1.0」；MiniShop 登录失败主路径写 401+`result=fail`、缺字段 400、打到 `/login` 或 GET `/api/login` 为 404（不是登录坏了，也不是 405）。
推荐替换文本：`| 对着 MiniShop 用 GET 打 /api/login，或 POST /login | 404。本项目未实现 405。不要写成登录功能坏了。 |`
```

```
## ISSUE
ID：CH09-0004
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：§9.10 常用码表；§9.11 WWW-Authenticate
精确位置：405 行「响应或含 Allow」；WWW-Authenticate「401 时常出现」
原文：405「响应或含 Allow」；`WWW-Authenticate`「401 时常出现」
问题等级：P2
问题类别：HTTP / TERM
问题说明：RFC 9110 §15.5.6：origin server **MUST** generate `Allow` in a 405。§15.5.2：generating a 401 **MUST** send `WWW-Authenticate`。正文改成「或含」「时常」，把规范强制说成现象。MiniShop 401 也没有该头，学生若按 RFC 硬断言会误报，若按教材则学不到 MUST。
为什么有问题：测试工程师需要同时知道「规范要求」和「大量 JSON API 不遵守」。只写观察语气，面试/缺陷评审会偏。
依据：RFC 9110 §15.5.2、§15.5.6（archive.vn / IETF HTML 摘录，2026-09-10 检索）。本次 MiniShop 401 响应头无 WWW-Authenticate。
建议修改：拆成「规范 MUST」+「大量 API 省略，缺陷要以项目约定为准」。
推荐替换文本：`405：规范要求带 Allow（RFC 9110 §15.5.6）。很多框架对未注册路由直接 404，MiniShop 就是这样。401：规范要求 WWW-Authenticate（§15.5.2）；Bearer JSON API 经常省略，MiniShop 省略。`
```

```
## ISSUE
ID：CH09-0005
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：练习 6；§9.10「若 MiniShop 约定失败时 HTTP 仍为 200」
精确位置：练习 6 题干（约 L345–346）；§9.10 段末（约 L114）
原文：响应是 `200 OK`，Body 为 `{"success":false,"message":"密码错误"}`；「若 MiniShop 约定失败时 HTTP 仍为 200」
问题等级：P2
问题类别：EX / ANS / MiniShop
问题说明：200 包业务失败是必须会的考点，题本身对。但 MiniShop 登录失败实装是 **401** + `{"result":"fail"}`（evidence `02-login-bad.txt`）。「若 MiniShop 约定」像在说本项目可能如此，实际并未如此。
为什么有问题：学生刚看完可抄登录报文和 9-1，再做练习 6，会以为自己抓到的 401 与答案冲突。【不是 ANSWER VERIFICATION FAILED】——答案对通用题是对的；缺的是「这不是 MiniShop 登录」标签。
依据：本次 POST 错误密码 → 401 `{"result":"fail"}`，无 Set-Cookie。
建议修改：题干标明「通用例子，不是 MiniShop」；MiniShop 对照改为 401 + `result=fail` 仍要读 Body。
推荐替换文本：练习 6 首句加：「下面不是 MiniShop 登录（MiniShop 密码错误是 401 + `result=fail`）。有的系统会 200 包业务码：…」
```

```
## ISSUE
ID：CH09-0006
文件：chapters/09a-network-http-semantics.md
章节：第 9 章（上）
小节：§9.2 端口表 vs `ch09-ip-port` 图
精确位置：scheme 表第三列标题「本章教学环境」（约 L107–110）；图 `ch09-ip-port.png` 高亮 8765
原文：自定义行「第 7 章示例用过 8443」；列名却是「本章教学环境」
问题等级：P2
问题类别：PED / SEQ / MiniShop
问题说明：同节正文已写 MiniShop 默认 `127.0.0.1:8765`，图也画 8765，表的「本章教学环境」列却是 80/443/8443。练习 1 又考 8443。
为什么有问题：零基础会问「到底敲哪扇门」。8443 作为第 7 章 HTTPS 示例应保留，但不能占用「本章教学环境」这个列名。
依据：PRD「本机 HTTP，默认 http://127.0.0.1:8765」；图 html/png 一致为 8765。
建议修改：列名改为「省略端口时 / 本章例子」；加一行 MiniShop v1.0 → 8765。
推荐替换文本：`| MiniShop v1.0 | 8765 | 必须写在 URL 里；不是 80，也不是第 7 章示例的 8443 |`
```

```
## ISSUE
ID：CH09-0007
文件：practice/09-http-observe/README.md；practice/09-http-observe/main.py；chapters/09b-http-message-observe.md
章节：第 9 章 / 实操 9-1
小节：实操与工作实战
精确位置：README「动手前先在纸上填四格」；`main.py` 只发一次 POST `/api/login`；09B 工作实战要求 GET+POST
原文：脚本打印四格；书面还要求一次搜索 GET
问题等级：P2
问题类别：EX / PED
问题说明：9-1 会自己填方法/路径/头/体，学生不识别也不改一格。没有 `/login` → 404 对照（教学审查补丁写过，现行脚本未做）。书面要求 GET 观察，脚本不练 GET。
为什么有问题：本章一句话核心是「拆成方法、路径、头、体」。验收目前只能证明脚本会登录，不能证明学生会填格。抄错路径是本章明确要防的错，却只写在散文里。
依据：本次 `python3 practice/run.py 9-1` 与 `--check` 均通过；`main.py` 无第二次请求；README 已有纸表但无强制。
建议修改：纸表保留；脚本在成功后再 POST `/login`，打印「对照：404，路径错不是密码错」，不写入 latest.json 成功四格；可选 GET `/api/products?keyword=鼠标` 作为 GET 格。
推荐替换文本：见上。验收仍只断言 `/api/login` 200 + token + Set-Cookie。
```

```
## ISSUE
ID：CH09-0008
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：§9.10
精确位置：常用码整表（约 L92–110）；409 行
原文：409「状态冲突，如重复提交」；表内 201/204/303/307/308/415/429 与 200/401/403 同为 ⭐⭐⭐ 节
问题等级：P2
问题类别：HTTP / PED / MiniShop
问题说明：① 表是百科墙，练习真正用到的是 200 仍看 Body、401/403、404。② 缺 RFC 9110 §15.5.21 **422 Unprocessable Content**（语法对、语义无法处理），初级接口测试极常见，任务清单点名要核。③ 409 用「重复提交」当例子：MiniShop 重复 POST `/api/orders` 是两个 201/两个 id（R-ORDER 默认不幂等）；409 在本项目是注册占用、库存变化。
为什么有问题：学生可能给「连点下单两笔」打 409 预期，和冻结契约相反。422 不出现，到第 13 章会把 422 当成 400 的别名。
依据：RFC 9110 §15.5.10 Conflict、§15.5.21 422；PRD R-ORDER、R-REG；`evidence/http/06-order-create.txt` 201；`08-register-duplicate.txt` 409。
建议修改：⭐⭐⭐ 先会 200/401/403/404/405/500；其余标 ⭐ 查阅。409 例子改「注册手机号已占用」。补一行 422，并写「MiniShop 用 400 覆盖这类校验，不出现 422」。
推荐替换文本：`| 409 | 与当前资源状态冲突 | MiniShop：注册占用。不要把「重复下单两笔」默认写成 409，v1.0 下单默认不幂等。 |`
```

```
## ISSUE
ID：CH09-0009
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：§9.11 Set-Cookie
精确位置：响应头表 Set-Cookie 行（约 L139）
原文：测试时看什么：`HttpOnly`、`Secure`、`SameSite`
问题等级：P2
问题类别：HTTP / JOB / MiniShop
问题说明：看这些属性是对的。MiniShop 实装只有 `HttpOnly; Path=/`，没有 `Secure`/`SameSite`，因为 v1.0 是本机 HTTP。不说明这一点，学生会按表给 MiniShop 提「缺少 Secure」缺陷。
为什么有问题：岗位上缺 Secure 在 HTTPS 站点常是真缺陷；在本课程 HTTP 教学环境是预期。需要环境条件。
依据：本次 Set-Cookie `minishop_session=…; HttpOnly; Path=/`；PRD 非范围 HTTPS。
建议修改：表后加一句条件。
推荐替换文本：「`Secure` 只在 HTTPS 有意义。MiniShop v1.0 是 http://127.0.0.1，Cookie 没有 Secure 不是本项目缺陷；换到 HTTPS 环境就要查。」
```

```
## ISSUE
ID：CH09-0010
文件：chapters/09a-network-http-semantics.md；chapters/assets/diagrams/ch09-https-wrap.html
章节：第 9 章（上）
小节：§9.4 mermaid；§9.6 图
精确位置：握手序列 Note「之后才能发送明文 HTTP」；HTTPS 图 lead「先握手、验证书，再传 HTTP」
原文：见上
问题等级：P2
问题类别：HTTP / PED
问题说明：① mermaid 把 TCP 之后的应用数据写成「明文 HTTP」。HTTPS 场景下 TCP 之后是 TLS，HTTP 在 TLS 里，不是明文。同块 Note 后半句才补 TLS，前半句已经教错分层。② HTTPS 图「先握手」紧挨刚学完的 TCP 三次握手，未写「TLS 握手」。
为什么有问题：本章花了整节防止「三次握手=HTTP 三步」，又用同一个「握手」词指 TLS，分层会糊回去。
依据：RFC 9110 §4.2.2 https URI（HTTP over TLS）；RFC 8446 TLS 在 TCP（或等价）之上。教学图 html 原文。
建议修改：Note 改为「之后才能发 HTTP；若 URL 是 https，先做 TLS，HTTP 在隧道里，路上不是明文」。图改为「先做 TLS 握手并验证书」。
推荐替换文本：同上。
```

## 6. P3

```
## ISSUE
ID：CH09-0011
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：§9.12
精确位置：「没有 Body 也可能是正常的，例如部分 204 响应」
原文：例如部分 204 响应
问题等级：P3
问题类别：HTTP / TERM
问题说明：RFC 9110 §15.3.5：204 不能含 message body，由头字段后第一个空行结束。「部分 204」像在说有的 204 有体。
依据：RFC 9110 §15.3.5
建议修改：改为「例如 204 No Content 按规定没有消息体」。
推荐替换文本：`没有 Body 也可能是正常的。204 No Content 按规定没有消息体（RFC 9110 §15.3.5）。`
```

```
## ISSUE
ID：CH09-0012
文件：chapters/09a-network-http-semantics.md
章节：第 9 章（上）
小节：§9.8 缓存
精确位置：「POST 响应只有带明确新鲜度等信息时才可能被存储」
原文：带明确新鲜度等信息
问题等级：P3
问题类别：HTTP
问题说明：RFC 9110 §9.3.3 还要求 `Content-Location` 与 POST 的 target URI 相同，缓存结果才能给后续 GET/HEAD 用。正文「等」盖住了这条，教学可接受，但不完整。
依据：RFC 9110 §9.3.3
建议修改：加半句 Content-Location 条件，或写「还有 Content-Location 等限制，初级记住：不要指望 POST 响应像 GET 那样被复用」。
推荐替换文本：`规范还要求带与目标 URI 相同的 Content-Location；多数实现仍不按 GET 缓存 POST。`
```

```
## ISSUE
ID：CH09-0013
文件：chapters/09a-network-http-semantics.md
章节：第 9 章（上）
小节：文首重要级别；§9.3 HTTP/3 段
精确位置：L7「重要级别：⭐⭐⭐」；§9.3 HTTP/3 段无 ⭐
原文：阅读提示说 9.1–9.4 是 ⭐⭐，UDP/HTTP/3 标 ⭐ 可跳；文首整册仍 ⭐⭐⭐；HTTP/3 段未标 ⭐
问题等级：P3
问题类别：PED
问题说明：阅读提示与节标题已对齐到 ⭐⭐ 地图，文首和 HTTP/3 段没跟上。不是知识错误。
依据：现行 09A L5–L7、L131 vs §9.1–9.4 标题。
建议修改：文首改为「本节地图 ⭐⭐，方法语义 ⭐⭐⭐」；HTTP/3 段首加「⭐ 可跳」。
推荐替换文本：见上。
```

```
## ISSUE
ID：CH09-0014
文件：chapters/09b-http-message-observe.md
章节：第 9 章（下）
小节：§9.13 反例段末
精确位置：L184
原文：3xx 的阅读要点收到 9.10
问题等级：P3
问题类别：PED
问题说明：「收到」是补丁笔记口吻，应为「放在 / 见」。
依据：现行正文。
建议修改：改为「3xx 怎么读，见 9.10」。
推荐替换文本：`3xx 怎么读见 9.10：…`
```

```
## ISSUE
ID：CH09-0015
文件：chapters/assets/diagrams/ch09-http-letter.html（及 png）
章节：第 9 章（下）§9.9
小节：信图
精确位置：左信 phone=13800138000，右信 401 + result=fail
原文：教学账号配失败邮戳
问题等级：P3
问题类别：IMG
问题说明：401 示例本身很好，但用了种子账号 `13800138000`。密码已 redacted，仍可能让人以为这个号会失败。
依据：图 html；种子用户该号密码 `Test1234` 登录为 200。
建议修改：失败例改用不存在的号，或加「这是密码错误的示意，不是这个手机号无效」。
推荐替换文本：phone 改 `13900000000`，或标题写「密码错误示例」。
```

```
## ISSUE
ID：CH09-0016
文件：chapters/09a-network-http-semantics.md
章节：第 9 章（上）
小节：§9.8 对照表 MiniShop 例子；场景导入
精确位置：GET 行「搜索商品、打开详情」；场景把证书问题列入 MiniShop 测试环境
原文：打开详情；HTTPS 证书不被信任
问题等级：P3
问题类别：MiniShop / PED
问题说明：v1.0 没有独立详情页。MiniShop 不做 HTTPS，场景第一条又点名 MiniShop。TLS 作为通用分层可以留，应标「一般站点 / 若环境是 HTTPS」。
依据：PRD 范围与非范围。
建议修改：GET 例子改为「搜索商品、打开列表」；场景 TLS 条加「若该环境走 HTTPS；MiniShop v1.0 是 HTTP」。
推荐替换文本：见上。
```

```
## ISSUE
ID：CH09-0017
文件：chapters/09a-network-http-semantics.md；chapters/09b-http-message-observe.md
章节：第 9 章（上）§9.8；（下）§9.10
小节：301/302；201
精确位置：301/302 行偏写 302 改 GET；201「应能找到新资源位置」
原文：不少客户端会把 POST 后的 302 改成 GET；201 应能找到新资源位置
问题等级：P3
问题类别：HTTP
问题说明：RFC 9110 §15.4.2 与 §15.4.3 对 301 和 302 都是 MAY 把 POST 改 GET。201：Location 不是必须，缺省则目标 URI 即资源；MiniShop 201 无 Location，id 在 Body（注册/下单）。
依据：RFC 9110 §15.3.2、§15.4.2–3；本次 POST `/api/register` 201，无 Location。
建议修改：301/302 都写 MAY 改方法；201 写「看 Location 或 Body 里的 id，不要因为没有 Location 就报 MiniShop 缺陷」。
推荐替换文本：见上。
```

```
## ISSUE
ID：CH09-0018
文件：practice/09-http-observe/main.py；chapters/assets/diagrams/*.png
章节：实操 9-1 / 示意图 PNG
小节：四格打印；png 画布
精确位置：`main.py` 头只打印 Content-Type；png 由 1320×780 截出，短图底部大块留白
原文：头：Content-Type: application/json
问题等级：P3
问题类别：EX / IMG
问题说明：09B 把头格定义为 Host / Content-Type / Cookie·Authorization，脚本只展示 Content-Type。PNG 留白不影响正确性，略损可读性。
依据：`main.py` L38；diagrams/README 截图命令 window-size=1320,780。
建议修改：打印 Host（或「由客户端自动加」）；截图可裁切。非必须。
推荐替换文本：`头：Host（客户端自动加）; Content-Type: application/json`
```

## 7. 逐段问题

判定：OK = 本单元无独立 ISSUE；ISSUE = 见上 ID。未抽样。

### 索引

| 单元 | 判定 |
| --- | --- |
| 一句话核心（四格 + 不按安不安全划分） | OK，双核与 09A/09B 分工清楚 |
| 拆章目录、作业 1–5 / 6–10、实操 9-1 | OK |
| 阶段测验 3（学完第 10 章再做） | OK，不把第 10 章提前讲完 |
| 下一章 DevTools | OK |

### 09A

| 单元 | 判定 |
| --- | --- |
| 一句话核心 / 阅读提示 | 阅读提示与节星级大体对齐；文首仍 ⭐⭐⭐ → CH09-0013 |
| 这一章解决什么问题 | OK。明确 safe≠机密，四格放到 09B |
| 学习目标 | OK，五条均可在节内找到对应 |
| 前置知识 | OK。学习顺序 1–8（含插在前面的第 7 章） |
| 场景导入 + mermaid 分层 | 通用分层 OK；MiniShop 场景夹 TLS → CH09-0016 |
| 9.1 地图表、无状态、OSI 不是日常清单 | OK |
| 9.2 IP | OK。回环 vs 本机 MiniShop 例外写清 |
| 9.2 端口表 + 图 | CH09-0006；图本身 KEEP |
| 9.3 TCP/UDP、HTTP/3 在 UDP | 技术 OK；HTTP/3 未标 ⭐ 可跳 → CH09-0013 |
| 9.4 三次握手 mermaid/要点 | 模型正确（SYN / SYN-ACK / ACK），未与 HTTP 三步混淆；「明文 HTTP」→ CH09-0010。**不过度**：已声明不讲序号/窗口/挥手，⭐⭐ 且提示可略读 |
| 9.5 HTTP 形状、Host 必须、HTTP/2·3 不是纯文本 | OK。Host 对应 RFC 9112 / RFC 9110 §7.2。教学 GET `/products` 已标未冻结 |
| 9.6 HTTPS=TLS 上的 HTTP；GET 改 POST 不加密 | OK，硬约束命中。图「先握手」→ CH09-0010 |
| 9.7 safe / 幂等定义与方法表 | OK。与 RFC 9110 §9.2.1–9.2.2 及 IANA 方法表一致。PATCH=RFC 5789、QUERY=RFC 10008（2026-06）正确。TRACE 安全≠无风险 OK。CONNECT 非安全非幂等 OK |
| 9.7 MiniShop 若用 GET 加购 | OK，反模式且是「如果」 |
| 9.7 登录重复≠两笔订单 | OK，与 R-ORDER 下单不幂等分开 |
| 9.8 禁止绝对化表 | OK。长度限制、query 不等于 GET，均对 |
| 9.8 query/body 泄露面 | OK |
| 9.8 可缓存≠safe；POST 可缓存但不能替代再 POST | 主旨 OK；Content-Location → CH09-0012 |
| 9.8 对照表 | MiniShop「打开详情」→ CH09-0016 |
| 常见错误 1–6 | OK |
| 面试 GET/POST、HTTP/HTTPS、幂等 | OK，含边界 |
| 练习 1–5 与答案 | OK，独立作答一致，见 §11 |
| 清单 / 门槛 / 总结 / 可运行性 / 参考资料 | OK。RFC 9110 标注 2026-09-08 核验，与 QUERY 已入标的时间线相容 |
| 外部链接 | 见 §18 |

### 09B

| 单元 | 判定 |
| --- | --- |
| 一句话核心 / 前置（不会说 POST 更安全） | OK |
| 场景：先问四格 | OK |
| 9.9 mermaid + 信图 + 请求/响应表 | 四问已对齐方法/路径/头/体。信图 401 教学可用 → CH09-0015 |
| 9.9 路径行只留 `/api/login` | OK（旧 P0 已修） |
| 9.10 类别表 | OK。2xx 仍看 Body；3xx 含缓存再验证；5xx 不要写成浏览器坏了 |
| 9.10 常用码 | 语义大体正确；分层不足、缺 422、409 例子、405/401 MUST → CH09-0004、CH09-0008；201/301 → CH09-0017 |
| 9.10 401 vs 403、200≠业务成功 | OK。MiniShop 他人订单 403 与 `server.py` `_get_order` 一致 |
| 9.11 请求/响应头 | 头名大小写不敏感 OK。Authorization 脱敏 OK。Set-Cookie 属性缺环境条件 → CH09-0009 |
| 9.12 Body / Content-Type / JSON 形状 | OK。204 措辞 → CH09-0011 |
| 9.13 反例 `/login` 无可抄请求行 | OK |
| 9.13 可抄 `/api/login` | CH09-0002 |
| 9.13 后续 `Authorization: Bearer` | OK。frontend `authHeaders()` 确发 Bearer；文已声明不因此消灭 Cookie/Session |
| 9.13 失败表 | CH09-0003 |
| 工作实战模板 / 完成标准 | 标准含 safe/幂等、禁止「POST 更安全」、路径 `/api/login`，OK。GET 依赖书面、9-1 不练 GET → CH09-0007 |
| 常见错误 1–5 | OK |
| 面试 401/403、不能只看页面 | OK |
| 练习 6–10 与答案 | 答案与独立作答一致；练习 6 缺 MiniShop 标签 → CH09-0005 |
| 清单含 200/302/304/401/403/404/500 | OK。304 在练习中弱，可接受 |
| 可运行性：9-1 ✅、未假装 DevTools 面板 | OK，诚实 |
| 「3xx 要点收到 9.10」 | CH09-0014 |

### 实操 / 测验 / 证据

| 单元 | 判定 |
| --- | --- |
| 实操 README 纸表、最小命令、验收、密码不入库 | OK 方向对；脚本未对照 404 → CH09-0007 |
| `main.py` / `test_lab.py` | 可运行、脱敏、断言 R-AUTH；代填四格 → CH09-0007 |
| 测验 Q4/Q5/Q9 | 独立作答与公布答案一致，见 §11 |
| evidence 01–09 与 network-log.html | 与 PRD/实装一致；network-log 声明非 DevTools 截图，OK |
| 示意图 6 组 | 见 §9；P1 仅 get-post keyword |

## 8. 代码问题

| 位置 | 判定 |
| --- | --- |
| `practice/09-http-observe/main.py` | 语法正确；stdlib；临时 MiniShop 不碰教学库；密码不写 latest.json。本次运行 exit 0，打印四格、200、token、Set-Cookie。缺 `/login` 对照与 GET，见 CH09-0007。头格过窄见 CH09-0018 |
| `tests/test_lab.py` | 断言 method/path/token/Set-Cookie/无明文密码。只有一条路径，不测 401。P3 测试薄，不单列 ISSUE |
| `practice/_http.py` | `HTTPError` 仍返回 status/body，适合观察 4xx。可运行 |
| `practice/_minishop.py` | 临时目录 + 线程服务，退出清理。可运行 |
| 09A/09B mermaid | 语法成立。握手 Note 见 CH09-0010 |
| 09B 可抄 HTTP 文本 | 作为 HTTP/1.1 纸面形状合法；与实装差异见 CH09-0002 |
| 09A `GET /products?keyword=mouse&page=2` | 教学未冻结，标了。MiniShop 无 `page`、路径是 `/api/products`。不要对着仓库抄。OK |
| Shell：`python3 practice/run.py 9-1`、`--check`、`cd project/minishop && python3 run.py serve` | 第一条与第二条本次已跑通。serve 未在本审计启动长期进程，9-1 已自拉临时实例，等价验证登录报文 |

**HTTP 示例重新推导（本次实跑 MiniShopLab）：**

| 示例 | 推导结果 |
| --- | --- |
| 教学 `GET /products?keyword=mouse&page=2` | 非 MiniShop。对仓库 GET `/products` → 404 |
| 图 `GET /api/products?keyword=mouse` | **200 + 空 items**。与图文案冲突。CH09-0001 |
| `POST /api/login` 正确密码 | 200；Set-Cookie HttpOnly；Body `result/token/role` |
| `POST /api/login` 错误密码 | 401 `{"result":"fail"}` 无 Set-Cookie |
| `POST /login` | 404 |
| `GET /api/login` | 404，无 Allow |
| `GET /api/cart` 无凭证 | 401 `unauthorized`，无 WWW-Authenticate |
| `GET /api/cart` Bearer | 200，购物车项 |
| `GET /api/admin/orders` 普通用户 | 403 |
| `POST /api/register` | 201，无 Location、无 token |
| `POST /api/cart/items` qty=11 | 400 `qty exceeds stock`（与状态图「qty=11 是 400」一致） |

前端 `app.js`：`POST /api/login` JSON；成功后 `Authorization: Bearer`；失败一律页面「登录失败」。与 09B「页面文案是回信的人话」一致。

## 9. 图片问题

六张均打开 html 源 + png。html 与 png 文案一致。无断链。

```
IMG-CH09-001
文件：chapters/assets/diagrams/ch09-ip-port.html + .png
出现位置：09A §9.2
图片主要内容：127.0.0.1 这栋楼；门 80/443/8765，8765 为 MiniShop v1.0
技术准确性：正确。敲错门还没有 HTTP 状态码。ping 通≠8765 开着。
与正文一致性：图用 8765，表用 8443 当「本章教学环境」，见 CH09-0006
文字是否正确：是
UI 是否过时：否（讲解图）
教学价值：高，直接服务「连不上先看门牌」
可读性：好
是否需要修改：列名/表与图对齐即可，图可 KEEP
修改建议：不必改画面；改 §9.2 表
最终结论：KEEP
```

```
IMG-CH09-002
文件：chapters/assets/diagrams/ch09-tcp-knock.html + .png
出现位置：09A §9.4
图片主要内容：SYN / SYN-ACK / ACK；握手成功≠登录成功；HTTPS 还要 TLS
技术准确性：三次握手简化模型正确。未画序号/旗标，正文已声明。未把握手写成 HTTP 三步。
与正文一致性：一致
文字是否正确：是
UI 是否过时：否
教学价值：高，防「握手=登录」
可读性：好；png 下部留白（CH09-0018）
是否需要修改：否
修改建议：无
最终结论：KEEP
```

```
IMG-CH09-003
文件：chapters/assets/diagrams/ch09-https-wrap.html + .png
出现位置：09A §9.6
图片主要内容：http 明文 POST 仍可见；https = HTTP+TLS；safe≠机密；MiniShop v1.0 是本机 HTTP
技术准确性：分层正确。明文侧可再标方法/头也被看光（已写路径/query/Body/Cookie）。
与正文一致性：一致。caption 明确不要写成已上线 HTTPS。
文字是否正确：是。「先握手」易与 TCP 握手撞词，CH09-0010
UI 是否过时：否
教学价值：高，打在本章过滤器上
可读性：好
是否需要修改：改「TLS 握手」三字
修改建议：见 CH09-0010
最终结论：MODIFY
```

```
IMG-CH09-004
文件：chapters/assets/diagrams/ch09-get-post.html + .png
出现位置：09A §9.8
图片主要内容：GET 看货架 / POST 交表格；safe 与幂等；加密看 HTTPS；POST /api/login 与 /api/orders
技术准确性：方法语义正确，R-ORDER 不幂等正确。GET 行 `keyword=mouse` 打在 `/api/products` 上对 MiniShop 空列表。
与正文一致性：正文教学 URL 是 `/products`；图用了 `/api/products`
文字是否正确：路径与 keyword 组合不正确（对 v1.0）
UI 是否过时：否
教学价值：高，但会被空搜索带偏
可读性：好
是否需要修改：是
修改建议：见 CH09-0001
最终结论：MODIFY
```

```
IMG-CH09-005
文件：chapters/assets/diagrams/ch09-http-letter.html + .png
出现位置：09B §9.9（已从 09A 挪来）
图片主要内容：请求四格（POST /api/login、Host、Content-Type、脱敏 Body）对 401 回信
技术准确性：401+`result=fail` 与 MiniShop 密码错误一致。密码已 redacted。无 `/login`。
与正文一致性：插在四格主课，命题对准。可抄成功报文是 200，图是失败例，教学可并存。
文字是否正确：是。教学号+401 略易误会，CH09-0015
UI 是否过时：否
教学价值：高，就是 09B 难点图
可读性：好
是否需要修改：可选换失败手机号
修改建议：CH09-0015
最终结论：KEEP（可选 MODIFY 账号）
```

```
IMG-CH09-006
文件：chapters/assets/diagrams/ch09-status.html + .png
出现位置：09B §9.10
图片主要内容：2xx 仍看 Body；3xx 方法可能变；400 qty=11；401/403 对照；404/409/5xx
技术准确性：与 MiniShop qty=11=400、无 token 下单 401、普通用户管理员接口 403 一致。未画 308/422，可接受。
与正文一致性：一致
文字是否正确：是。「登录 200 才有 token」对 MiniShop 登录成立（注册 201 无 token，图说的是登录）
UI 是否过时：否
教学价值：高；401/403 已有卡片，不必另出 ch09-401-403 也能讲
可读性：好；png 留白
是否需要修改：否
修改建议：无
最终结论：KEEP
```

未发现 pedagogy 点名的 `ch09-four-slots` / `ch09-401-403` 新文件。信图已承担四格；状态图已承担 401/403。不另报缺图 P1。

## 10. 表格问题

| 表 | 判定 |
| --- | --- |
| 09A 9.1 问题×层×例子 | OK |
| 09A 9.2 scheme/端口 | 列名「本章教学环境」误导，CH09-0006 |
| 09A 9.3 TCP/UDP | OK。HTTP/3 基于 QUIC/UDP 正确 |
| 09A 9.6 证书/混合内容/代理 | OK |
| 09A 9.7 性质定义 | OK，safe/幂等「不是什么」列有价值 |
| 09A 9.7 方法×安全×幂等 | 与 RFC 9110 方法登记表一致；PATCH/QUERY 在表外附注，正确 |
| 09A 9.8 错误说法 | OK，覆盖质量标准禁止项 |
| 09A 9.8 query/body | OK |
| 09A 9.8 GET vs POST | OK |
| 09B 请求四部分 / 响应三部分 | OK，路径已是 `/api/login` |
| 09B 1xx–5xx 类别 | OK |
| 09B 常用状态码 | 见 CH09-0004、0008、0017 |
| 09B 请求头 / 响应头 | Host/Content-Type/Authorization/Cookie 均有。Secure 条件见 CH09-0009 |
| 09B Content-Type | OK |
| 09B 登录失败观察 | CH09-0003 |
| 实操纸表四格 | OK |

无表内数字自相矛盾。无把 P0/P1 等级写成全球统一（本章未涉及该禁止项）。

## 11. 练习与答案问题

独立作答在读公布答案之前完成（测验答案同文件，题干先解；公布答案后复核）。

### 09A 练习 1–5

| 题 | 独立答案 | 教材答案 | 结果 |
| --- | --- | --- | --- |
| 1 | IP 找主机（常经 DNS）；端口找该主机上的服务。默认 HTTPS 443。写 8443 是因为服务不在 443，省略会被客户端当成 443 | 同 | 一致 |
| 2 | 不能。只说明 TCP 连接建立。HTTPS 还要 TLS，登录还要 HTTP 业务 | 同 | 一致 |
| 3 | C。A 把 URL 泄露说成 safe；B/D 把 POST 当加密 | C | 一致 |
| 4 | 加购改购物车，不是 safe 语义，预取/爬虫可能误触发；搜索是读当前列表，GET 安全且幂等，query 可分享。GET 加购还会让重复抓取重复加购 | 同 | 一致 |
| 5 | URL 进历史、日志、Referer、截图、分享。HTTPS 只保护传输路径。登录也不该用安全方法 | 同 | 一致 |

### 09B 练习 6–10

| 题 | 独立答案 | 教材答案 | 结果 |
| --- | --- | --- | --- |
| 6 | 不能只凭 200 判用例失败。预期要同时写状态码和 Body（及页面）。此例协议成功、业务失败 | 同 | 一致。标签问题 CH09-0005，**不是答案错误** |
| 7 | 401 更接近未认证；403 更接近已认证但拒绝。若都 200+错误码，按约定断言字段，不要用「标准 401」强行判错 | 同 | 一致 |
| 8 | 下一请求通常仍自动带 Cookie；`document.cookie` 读不到 HttpOnly | 同 | 一致 |
| 9 | 更可能卡在 TLS。TCP 可能已成功，HTTP 登录 Body 还没发出 | 同 | 一致 |
| 10 | POST；`/api/login`；密码在 Body 不在 query；登录态：响应 Set-Cookie 与 JSON token；后续 Bearer 和/或 Cookie | 同 | 一致 |

无 【ANSWER VERIFICATION FAILED】。

### 阶段测验 3（仅第 9 章题）

独立答案：

- **Q4（必过）** safe：客户端不请求改变资源状态（写日志不破定义）。幂等：多次相同请求的预期效果与一次相同。可缓存是另一项，不等于 safe。不能说「GET 不安全、POST 安全」。
- **Q5** 401：缺少或无效认证（MiniShop：无 token 下单/购物车）。403：服务器拒绝，常见已认证无权限（MiniShop：普通用户 `/api/admin/*`；他人订单）。项目可能混用，以约定+报文为准。
- **Q9** 响应 JSON `token` 与 `Set-Cookie`（HttpOnly）。后续 API 以 Bearer 为准。

与公布答案一致。Q5 教材举 `/api/admin/orders` 或 `/api/admin/products`，与实装 403 一致。Q1–3、6–8、10 属第 8/10 章，本 Agent 不审他章正文，不给那些题的对错结论。

### 实操 9-1

先按 README 在纸上填四格（不看脚本）：方法 POST、路径 `/api/login`、头 Content-Type application/json、体 phone+password。  
再跑：与纸上一致，且 200 + token + Set-Cookie。脚本问「为什么不能说 GET 不安全 POST 安全」——因为 safe 是只读语义，机密看 TLS。

## 12. 初学者理解障碍

标记 【Beginner Friction】：

1. **两套端口**：8765（真 MiniShop）与 8443（第 7 章 HTTPS 示例）并列，表还叫「本章教学环境」。CH09-0006。
2. **两套路径风格**：09A 教学 `/products`、反模式 `/cart/add`，09B/图/实操 `/api/...`。正文有冻结声明，图 CH09-0001 把两套拼错。
3. **HTTP/1.1 纸面 vs HTTP/1.0 实装**。curl -v 第一行就不一样。CH09-0002。
4. **练习 6 的 200+密码错误 vs 实操/证据的 401**。CH09-0005。
5. **「握手」一词先指 TCP 再指 TLS**。CH09-0010。
6. **状态码一表铺开**，第一次读会以为 307/415/429 与 401 同等必须背。CH09-0008。
7. **实操代填四格**，纸表可跳。CH09-0007。
8. 09A 文首仍标整册 ⭐⭐⭐，与「地图可略读」打架。CH09-0013。

未发现「先讲不要 X 再讲 X 是什么」的反序，除 9.8 用「不要使用的绝对化」开 GET/POST——此处先有结论句再拆，可接受。

## 13. 岗位能力缺口

标记 【Job Reality Gap】：

1. **422** 未出现。Laravel/Spring 校验失败常用 422，和 400/415 的差别是接口测试口头禅。CH09-0008。
2. **405 vs 框架 404**：真实服务经常对「错方法」返回 404。教材按 RFC 讲 405 是对的，但要用 MiniShop 当反例。CH09-0003/0004。
3. **401 无 WWW-Authenticate** 在 JSON API 极常见。应同时教 MUST 与现实。CH09-0004。
4. **Cookie Secure/SameSite** 检查清单没有环境前提。CH09-0009。
5. **实操没有改一格**：岗位上要自己改 path/header 看差异，现在是观看脚本演出。CH09-0007。
6. 本章不教抓包工具、不教 TLS 版本/套件，定位正确（⭐⭐ 地图）。缺的是「看 MiniShop 真实状态行 HTTP/1.0」这一眼，不是 Wireshark。

未要求本章讲 OSI 七层背诵、未要求配置 OpenSSL，这是正确的岗位裁剪，不是缺口。

## 14. 建议删除内容

- 不建议删 TRACE/CONNECT：标了少见，且为对齐 RFC 9110 方法表。
- 不建议删三次握手整节：已 ⭐⭐ 且服务「连不上≠密码错」。不要再加序号/窗口。
- 不建议删 09A 教学 `/products` 示例：已标未冻结。
- 可删或改写：§9.10 把 201/204/303/307/308/415/429 与 200/401 混在同一「必须能解释」表里的观感（改为查阅，不是删码）。

## 15. 建议新增内容

1. MiniShop 对照小表：登录成功 200+token+Set-Cookie+role；失败 401+`result=fail`；错路径 404；本项目不见 405/415/422/429/TLS。
2. 422 一行 +「本项目用 400」。
3. 实操第二次请求：`POST /login` → 404。
4. 可抄报文下的 HTTP/1.0 / `role` / charset 注记。
5. Set-Cookie 属性的 HTTPS 前提。
6. （可选）GET `/api/products?keyword=鼠标` 作为书面 GET 的推荐输入，避免抄图上的 `mouse`。

## 16. 建议重写内容

1. **CH09-0001 图**：`keyword=mouse` 不要绑 `/api/products`。
2. **§9.13 可抄报文**：加实装注记，Body 与 evidence 对齐。
3. **§9.13 失败表**：通用 vs MiniShop 两列。
4. **§9.10**：分层 ⭐⭐⭐ / ⭐；409 例子；补 422。
5. **§9.2 端口表**：列名与 8765 行。
6. **§9.4 mermaid Note 与 HTTPS 图「握手」用词**。

不需要重写 9.7/9.8 方法语义——这是本章写得最好的部分。

## 17. 本章结论

**B 小修**

理由：主课（safe / 幂等 / 可缓存 / GET vs POST / TLS 分层 / 四格 / 200≠业务成功 / 401 vs 403 / MiniShop `/api/login`）技术正确，质量标准禁止的 GET/POST 安全神话没有出现。旧 P0（可抄 `/login`）现行正文已改成反例。剩余是一张图把 MiniShop 路径和英文 keyword 拼错（P1）、可抄报文与实装不完全同构、RFC MUST 弱化、实操代填、状态码未分层。属于局部补丁，不是重写方法语义。

不要选 A：还有 P1 和若干会让学生对照 MiniShop 对不上的 P2。  
不要选 C：核心 RFC 口径与拆章结构已经能用。

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`
- `reviews/_full-audit-2026-09-10/AUDIT_PROGRESS.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `README.md`（入口与第 9 章行）
- `docs/COURSE_CONTROL.md`
- `docs/COURSE_OUTLINE_v1.2.md`（第 9 章范围）
- `docs/LEARNING.md`
- `practice/README.md`、`practice/STATUS.md`、`exercises/README.md`
- `chapters/09-computer-network-and-http.md`
- `chapters/09a-network-http-semantics.md`
- `chapters/09b-http-message-observe.md`
- `practice/09-http-observe/README.md`、`main.py`、`tests/test_lab.py`、`validation/latest.json`（跑后）
- `practice/run.py`、`practice/_http.py`、`practice/_minishop.py`
- `chapters/quizzes/README.md`、`chapters/quizzes/stage-3-web.md`（第 9 章题）
- `reviews/chapter-09-review.md`（线索，未照抄分数）
- `reviews/_pedagogy-2026-09-10/ch09.md`、`RUBRIC.md`（线索；确认旧 P0 `/login` 已修、实操对照仍缺）
- `reviews/_rereview-2026-09-09/stage-4-ch09-11-12.md`（线索；拆章已发生）
- `reviews/v1.2.1-rescore.md` 第 9 章行（线索）
- `project/minishop/docs/PRD.md`（R-AUTH/R-ORDER/R-PERM/非范围）
- `project/minishop/docs/openapi.json`（`/api/login`）
- `project/minishop/server.py`（登录、401/403、404、Cookie/Bearer）
- `project/minishop/frontend/app.js`（登录 fetch）
- `project/minishop/evidence/README.md`
- `project/minishop/evidence/http/01-login-ok.txt` … `09-register-bad-phone.txt`
- `project/minishop/evidence/http/network-log.html`
- `project/minishop/evidence/linux/curl-login-headers.txt`
- `chapters/assets/diagrams/README.md`
- `chapters/assets/diagrams/ch09-*.html` 与 `ch09-*.png`（6 组）

未读其他章正文。邻章只核了链接目标文件存在。

### 实际跑过的命令与结果摘要

```text
python3 practice/run.py 9-1
→ exit 0
  方法 POST，路径 /api/login，头 Content-Type application/json
  状态 200，Set-Cookie 有，token 有，keys=['result','token','role']
  latest.json 无 Test1234

python3 practice/run.py 9-1 --check
→ test_four_slots_and_auth ... ok  (0.516s)

独立 MiniShopLab 重放：
  POST /api/login 正确 → 200，HTTP version 10，Set-Cookie HttpOnly; Path=/，Body 含 role
  POST /api/login 错误 → 401 {"result":"fail"}
  POST /login → 404
  GET /api/login → 404，无 Allow
  GET /api/products?keyword=mouse → 200 {"items":[]}
  GET /api/cart 无凭证 → 401，无 WWW-Authenticate
  GET /api/cart Bearer → 200
  GET /api/admin/orders 普通用户 → 403
  POST /api/register → 201，无 Location
  POST /api/cart/items qty=11 → 400
```

未启动长期 `run.py serve`：9-1 已自拉临时实例，登录契约已验证。

### 外部核查

本环境 `web_fetch`/`open_page` 访问 `rfc-editor.org`、`ietf.org`、`developer.mozilla.org` 因 SSRF（解析到 198.18.0.0/16）失败。改用 `web_search` 交叉核：

| 条目 | 来源 | 结论 |
| --- | --- | --- |
| RFC 9110 safe：GET/HEAD/OPTIONS/TRACE | IETF HTML / DevDocs 摘录 §9.2.1 | 与教材表一致 |
| RFC 9110 幂等：PUT/DELETE + 安全方法；POST/CONNECT 否 | §9.2.2；IANA 方法表 | 一致 |
| RFC 9110 可缓存方法 GET/HEAD/POST；OPTIONS/TRACE 响应默认不可缓存 | §9.2.3、§9.3.7、§9.3.8 | 一致 |
| POST 缓存条件：新鲜度 + Content-Location=target URI；只能满足后续 GET/HEAD | §9.3.3 | 教材主旨对，条件写「等」→ CH09-0012 |
| PATCH 不在 9110 方法表，属 RFC 5789 | 9110 §9.3 列表 | 教材正确 |
| QUERY = RFC 10008（2026-06 发布，safe+idempotent，带 Body） | rfc-editor 公告 2026-06-16；Wikipedia HTTP 方法表 2026-09-09 | 教材正确，**不是【External Verification Required】** |
| 401 MUST WWW-Authenticate；405 MUST Allow；422 Unprocessable Content | RFC 9110 §15.5.2 / §15.5.6 / §15.5.21 | 教材 401/403 解释方向对；MUST 弱化与缺 422 已报 |
| 301/302 MAY 改 POST→GET；303 用 GET；307/308 保持方法 | §15.4.x | 教材正确；301 与 302 同等 MAY → CH09-0017 |
| 204 无 body | §15.3.5 | CH09-0011 |
| Host 在 HTTP/1.1 必须 | RFC 9110 §7.2 / RFC 9112 | 教材正确 |
| MDN Methods / Status URL | 检索到 `…/Web/HTTP/Reference/Methods`（2025-07）、`…/Status`（2026-01） | 链接形态有效 |
| MDN Glossary HTTPS | 未抓到页面正文 | 路径与 MDN 现行 Glossary 惯例一致；**页面全文【External Verification Required】**（SSRF） |
| TCP 三次握手 SYN/SYN-ACK/ACK | 教学简化；未宣称含序号细节 | 对初级测试足够，不过度 |

### 与旧审查的关系（独立复核，未照抄）

- 旧 `chapter-09-review.md` 纠 PATCH 归属：现行已修，确认。
- 教学审查 CH09-01 可抄 `/login`：现行已改为反例，**不再报 P0**。
- 教学审查 CH09-04 脚本打 `/login` 404：现行 **未做**，维持 P2（CH09-0007）。
- 教学审查星级/四格图搬家：星级大体已改，信图已在 09B；HTTP/3 段内 ⭐ 与文首 ⭐⭐⭐ 残留 P3。
- 本报告新发现：图 `keyword=mouse`+`/api/products` 空列表（P1）；HTTP/1.0 与 `role`；405/401 MUST；练习 6 与 MiniShop 401 错位。

### 第 9 章硬核技术结论（任务点名项）

| 点 | 教材 | 本审计 |
| --- | --- | --- |
| safe / idempotent vs 「GET 安全 POST 不安全」错误话术 | 明确禁止并给 RFC 定义 | **通过** |
| 状态码 301/302/304/401/403/404/405/409/500 | 有，方向对 | 通过；405 MUST、409 例子、缺 **422** 见 ISSUE |
| Host、Content-Type、Authorization、Cookie | 均有教学表 | 通过；Secure 缺环境条件 |
| HTTP/1.1 vs HTTPS/TLS 分层 | HTTPS=TLS 上的 HTTP；方法不加密 | 通过；mermaid「明文 HTTP」与「握手」用词见 CH09-0010 |
| 三次握手是否过度/是否有错 | 简化模型 + 不等于登录 | **无错、不过度**（⭐⭐，不讲序号/挥手） |