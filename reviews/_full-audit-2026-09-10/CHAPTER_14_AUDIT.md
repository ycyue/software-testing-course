# Chapter 14 Audit

- 审计对象：`chapters/14-postman.md`（核心章）
- 关联资产：`project/minishop/postman/MiniShop.postman_collection.json`、`MiniShop.postman_environment.json`
- 测验：`chapters/quizzes/stage-5-api.md` 第 14 章相关题（Q3 路径口径、Q4 变量覆盖、Q5 401 隔离）
- 示意图：`chapters/assets/diagrams/ch14-workspace.{png,html}`、`ch14-token-relay.{png,html}`；章内另嵌 `08-network-log.png`、`09-pytest-report.png`
- 审计日期：2026-09-10
- Agent：Chapter-Audit-Agent-14
- 结论：**C 明显需要修改**（DoD 13/20，低于 18 不得发布）
- 总体：**66/100**（核心章加严；不是作者未点 GUI 本身扣分）

旧审查只作线索，本文件结论全部独立复核。2026-09-09 阶段复审里「14.7 仍手建 `/login`」**已过时**：现行 14.7 / 工作实战已改为读仓库 15 条 `/api/`。本轮新发现的硬伤是 **Postman Cookie 罐 + MiniShop 接受 Cookie 认证**，使集合「无凭证创建」在 GUI 默认行为下变成 201。

---

## 1. Coverage

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 章内 `##` 小节（含工作实战模板内标题） | 27 | 27 | 0 |
| `###` 小节（错误 1–10、练习 1–10、面试 5 题等） | 26 | 26 | 0 |
| 正文段落块 | 83 | 83 | 0 |
| 列表项 | 100 | 100 | 0 |
| 表格（14.1 / 14.3 / 14.7；模板内表不另计） | 3 | 3 | 0 |
| 代码围栏 | 14 | 14 | 0 |
| 其中 JavaScript | 7 | 7 | 0 |
| Mermaid | 1 | 1 | 0 |
| Linux/Shell 命令 | 1 | 1 | 0 |
| SQL | 0 | 0 | 0（本章无 SQL，N/A） |
| HTTP 示例（URL/Header/Body/方法） | 15+ | 15+ | 0 |
| 仓库 Collection 请求 | 15 | 15 | 0 |
| 仓库 Environment 变量 | 10 | 10 | 0 |
| Collection 内 `pm.test` 脚本 | 15 | 15 | 0 |
| 正文 `pm.test`/`pm.environment` 示例 | 6 | 6 | 0 |
| Bug 示例（BUG-001 / 空搜索） | 1 | 1 | 0 |
| 小练习 | 10 | 10 | 0 |
| 练习答案 | 10 | 10 | 0 |
| 面试题 | 5 | 5 | 0 |
| 常见错误 | 10 | 10 | 0 |
| 检查清单 | 11 | 11 | 0 |
| 自测门槛 | 4 | 4 | 0 |
| 图片 PNG | 4 | 4 | 0 |
| 示意图 HTML | 2 | 2 | 0 |
| 外部链接 | 5 | 5 | 0 |
| 内部链接 | 3 | 3 | 0 |
| 阶段测验第 14 章相关题 | 3（Q3/Q4/Q5） | 3 | 0 |
| 图注 / alt | 4 | 4 | 0 |
| **合计内容单元** | **以上全表** | **全部** | **0** |

Coverage **100%**。未启动 Postman 桌面 GUI / Collection Runner / Newman（本机 `newman`、`postman` 均不存在）。已用 Python `requests` 对 MiniShop 实服务完整重放 15 条（Cookie 罐开/关各一轮），并用模拟 `pm` 对象执行正文脚本。作者未点 GUI **已披露，不记为内容缺陷**。

---

## 2. 总评分

| 项目 | 分数 |
| --- | ---: |
| 技术准确性 | 7/10 |
| 岗位实用性 | 7/10 |
| 完整性 | 7/10 |
| 初学者友好度 | 6/10 |
| 教学顺序 | 6/10 |
| 代码质量 | 6/10 |
| 实操质量 | 6/10 |
| 练习质量 | 7/10 |
| 图片质量 | 7/10 |
| **总体** | **66/100** |

九项合计 59/90，按百分制约 66。核心章目标 95、发布线 90，均未达到。

扣分主因（不是「没点 GUI」）：

1. 仓库集合「无凭证创建」在 Postman 默认 Cookie 罐下会变成 **201**，与「空搜索才允许红」的完成标准冲突（CH14-0001）。
2. 正文 `orderId` / 「第 6 步再创建订单」与仓库 `lastOrderId`、现行 15 条集合不一致（CH14-0002、CH14-0003）。
3. 14.2 仍叫人「新建 Request」，导入与「不要另造」在 14.6.1 / 14.7（CH14-0004）。
4. 14.5 列表脚本只断言数组，踩了 14.2 自己的坑（CH14-0005）。

加分（必须记上，避免只报坏）：

- Workspace / Collection / Environment / `{{var}}` / `pm.test`+`pm.expect` 与 2026-09 官方文档仍一致。
- 变量范围 global→collection→environment→data→local、更窄覆盖更宽，与官方一致。
- 未把 GET/POST 写成加密神话；Cookie 与 Bearer 未写成三选一；Runner 全绿不能代替出口标准；ROI 未绝对化。
- 15 条均为 `/api/`，未把无前缀 `/login` 当可抄契约；空搜索按 R-SEARCH、BUG-001 仍开放；订单无 `status`；qty=10/11 与 PRD 一致。
- GUI 未点、Runner 无截图：**诚实**。

---

## 3. P0

无。

未把 `POST /login`（无 `/api`）写成 MiniShop 可抄契约；未把验证码写进工作实战；未把 Collection Runner 写成作者已跑完；未教授质量标准禁止的六条绝对化。

---

## 4. P1

## ISSUE
ID：CH14-0001
文件：`project/minishop/postman/MiniShop.postman_collection.json`；`chapters/14-postman.md`
章节：第 14 章
小节：14.2 Cookie 段；14.4 未登录用例；14.6 Collection Runner；14.6.1 步骤 7；14.7「无凭证创建」；工作实战完成标准；集合请求「无凭证创建」
精确位置：集合第 199–207 行（无 `Authorization`、无 `protocolProfileBehavior.disableCookies`）；正文 L109、L177–178、L287、L309、L361；`server.py` `_token()` L190–199
原文：

> 无凭证创建 | 无 Authorization | 401
>
> 完成标准：导入并跑通仓库集合（空搜索允许红）

问题等级：P1
问题类别：TEST / CODE / HTTP / JOB
问题说明：MiniShop 在没有 `Authorization: Bearer` 时仍读取 Cookie `minishop_session`（R-AUTH：Cookie 可并存）。登录三条都会 `Set-Cookie`。Postman 默认把 Cookie 写入 cookie jar 并在后续同域请求自动带上。Collection Runner 高级选项里有 **Run collection without using stored cookies**；单请求 Settings 有 **Disable cookie jar**；collection 格式支持 `protocolProfileBehavior.disableCookies`。仓库「无凭证创建」只去掉了 Header，**没有禁用 Cookie 罐**。
为什么有问题：本机对同一套 15 条实服务重放：

| 条件 | 通过 | 失败 |
| --- | ---: | ---: |
| 不发送 Cookie（类似 curl / 禁用 cookie jar） | 14 | 1（空搜索 BUG-001，符合正文） |
| 发送 Cookie 罐（Postman GUI 默认） | 13 | 2（空搜索 + **无凭证创建 HTTP 201**） |

Cookie 罐开启时，三条登录后 jar 里是管理员 `minishop_session`；「无凭证创建」被当成已登录管理员下单，返回 `{"id":"ord-…"}` 201，断言 401 失败。学生按 14.6.1 跑 Runner，会看到**两条红**，但正文只允许空搜索红。他们会误判集合坏了、服务坏了，或给无凭证请求补上 Bearer，把 401 用例毁掉。这是本章主实操资产在所教工具里的默认可运行性失败，**不依赖是否点击过 GUI**：读 JSON + `server.py` 即可预判。
依据：Postman Docs *Create and capture cookies*（Disable cookie jar）；Collection Runner *Run collection without using stored cookies*；`postman-runtime` `protocolProfileBehavior.disableCookies`；PRD R-AUTH；`server.py` `_token()`；`tests/test_api.py` `test_login_ok` 明确用 Cookie 打 `/api/cart` 得 200。
建议修改：

1. 「无凭证创建」加 `"protocolProfileBehavior": {"disableCookies": true}`（或 Pre-request 清 jar，并写进正文）。
2. 14.4 / 14.6 / 错误 5：无凭证 = **不要 Authorization 且不要让 cookie jar 代发会话**。
3. 14.6.1 步骤 7：Runner 勾选 *Run collection without using stored cookies*，并写明默认不勾则 401 条会变 201。
4. 完成标准改为：空搜索允许红；若未禁 Cookie，无凭证也可能红，那是 Cookie 罐不是集合坏了。

推荐替换文本：

```markdown
无凭证不是「这条请求没有填写 Authorization」就够了。Postman 默认会把登录的 `Set-Cookie` 存进 cookie jar，下一请求自动带上。MiniShop 没有 Bearer 时仍认 `minishop_session`（R-AUTH：Cookie 可并存）。测 401 必须同时关掉这条请求的 cookie jar（Settings → Disable cookie jar），或在 Runner 勾选 Run collection without using stored cookies。仓库「无凭证创建」已关闭 cookie jar；不要把它插到登录成功和带 Bearer 的下单中间，也不要给它补 Authorization。
```

---

## ISSUE
ID：CH14-0002
文件：`chapters/14-postman.md`；对照 `MiniShop.postman_environment.json`、`MiniShop.postman_collection.json`
章节：第 14 章
小节：14.2 Path 例子；14.3 变量表；14.5 创建订单脚本；练习 8 答案
精确位置：L98–99；L124；L219–223；L507
原文：

> 例如 Path `/api/orders/:orderId` 与 `{{orderId}}`。
> | `orderId` | 运行中由脚本写入 | 创建订单后保存 |
> `pm.environment.set("orderId", body.id);`
> 保存第一次 `orderId`，第二次 `pm.expect(body.id).to.not.eql(pm.environment.get("orderId"))`。

问题等级：P1
问题类别：TERM / CODE / ANS / SEQ
问题说明：仓库环境变量与越权 URL 用的是 **`lastOrderId`**。集合「创建订单」`set('lastOrderId', json.id)`，「越权-他人订单」`GET {{baseUrl}}/api/orders/{{lastOrderId}}`。正文与练习答案写 `orderId`。
为什么有问题：线性读者按 14.5 脚本 `set("orderId")`，再跑仓库越权请求，Path 里 `{{lastOrderId}}` 仍为空 → 实际打到 `GET /api/orders/` → **404** 而不是 403（`server.py` 对 `/api/orders/` 不进 `_get_order`）。14.7 已改口「集合目前只下一单」，变量名却没改完。练习 8 是自测门槛必答题，答案与可导入资产不一致。
依据：`MiniShop.postman_environment.json` 仅有 `lastOrderId`；集合 L185、L222；`server.py` `do_GET` L232。
建议修改：正文、表、脚本、练习 8 答案、Path 例子一律 `lastOrderId`。Path 示例写成集合真实写法 `{{baseUrl}}/api/orders/{{lastOrderId}}`，再另用一句区分 Postman `:pathVar` 与环境变量。
推荐替换文本：

```markdown
| `lastOrderId` | 运行中由脚本写入 | 创建订单后保存；越权请求的 Path 引用它 |

pm.environment.set("lastOrderId", body.id);
```

---

## ISSUE
ID：CH14-0003
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.5 创建订单之后
精确位置：L227
原文：

> 第 6 步“再创建订单”复用上面脚本：第一次写入 `orderId`，第二次先比较再覆盖。不要只 `set` 而不比较，否则 Runner 无法证明不幂等。

问题等级：P1
问题类别：SEQ / PED
问题说明：现行集合只有一条「创建订单」，**没有**「再创建订单」，也没有七步教案。14.7 L312 已经正确写「集合目前只下一单，没有再创建订单」。14.5 仍指挥学生去做不存在的第 6 步。
为什么有问题：旧教案残留。学生在 Runner 里找「第 6 步」找不到，会以为自己漏导入。不幂等测法应明确为：**复制**「创建订单」再跑，先 `get("lastOrderId")` 再比较。
依据：集合 `item` 恰好 15 条，无第二笔下单；14.7 自身已否定第 6 步。
建议修改：删除「第 6 步」句，改写为与 14.7 相同的「复制请求」测法。
推荐替换文本：

```markdown
仓库集合只有一条「创建订单」，没有「再创建订单」。要证明 v1.0 默认不幂等：复制「创建订单」，在副本里先 `pm.expect(body.id).to.not.eql(pm.environment.get("lastOrderId"))`，再 `set` 覆盖。不要只 set 不比较。
```

---

## ISSUE
ID：CH14-0004
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.2 开篇；对照开篇 L13、14.6.1、14.7、工作实战
精确位置：L84
原文：

> 新建 Request，选择方法，URL 使用变量。路径与仓库集合一致：

问题等级：P1
问题类别：PED / SEQ
问题说明：章首、14.7、工作实战都说**导入** 15 条，不要另造 `/login`。14.2 第一句却把「新建 Request」当成动作。导入步骤在 14.6.1，线性阅读会先手建一套 `/api/login`。
为什么有问题：14.2 还提前使用尚未教的 `{{baseUrl}}`、`Authorization`。新手会造一套与仓库重复、脚本更弱（见 CH14-0005）的请求，再被 14.7 叫停。
依据：开篇 L13；14.7 L297–298；工作实战 L329；`practice/README.md` 14-1「导入 Postman 集合」。
建议修改：14.2 改为先打开已导入的「搜索商品」「登录-正确」；「新建」降为对照，不作为本章动作。
推荐替换文本：

```markdown
先做 14.6.1 的导入，再打开集合里已有的请求，不要新建一套 `/api/login`。

打开「搜索商品」：方法 GET，URL 是 `{{baseUrl}}/api/products?keyword=鼠标`。Params 里的 `keyword` 就是 Query。打开「登录-正确」：方法 POST，Body 为 raw + JSON。
```

---

## ISSUE
ID：CH14-0005
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.5 商品列表脚本；对照 14.2 L94、集合「搜索商品」
精确位置：L191–197
原文：

```javascript
pm.test("列表接口返回 JSON 数组结构", function () {
  pm.expect(pm.response.code).to.eql(200);
  const body = pm.response.json();
  pm.expect(body).to.have.property("items");
  pm.expect(body.items).to.be.an("array");
});
```

> 商品名是「无线鼠标」，搜 `mouse` 会得到空数组，断言「items 为数组」也会绿——那不证明搜到了。

问题等级：P1
问题类别：TEST / CODE / PED
问题说明：14.2 刚警告「只断言数组会绿」，14.5 示例自己只断言数组。仓库「搜索商品」已经 `items[0].sku === 'SKU-DEMO-001'`。
为什么有问题：本机 `GET /api/products?keyword=mouse` 返回 `{"items":[]}`，14.5 脚本仍通过。学生若抄正文而不是集合，会把空搜索和搜英文都标绿。与本章一句话核心「可重复的判定」相反。
依据：集合 L54–60；`server.py` `_get_products` 按 name/sku 包含匹配，「无线鼠标」不含 `mouse`；实服务验证空数组。
建议修改：与集合对齐，断言命中 `SKU-DEMO-001`，并保留「只断言数组不够」那句作为反例，不要当正式脚本。
推荐替换文本：

```javascript
pm.test("列表命中无线鼠标", function () {
  pm.expect(pm.response.code).to.eql(200);
  const items = pm.response.json().items;
  pm.expect(items).to.be.an("array");
  pm.expect(items[0].sku).to.eql("SKU-DEMO-001");
});
```

---

## 5. P2

## ISSUE
ID：CH14-0006
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.6.1 步骤 6
精确位置：L283
原文：

> 顺序建议：注册-非法手机号 → 注册（若 `newPhone` 已用过会 409，改一个未占用号）→ 搜索 → 空搜索-BUG-001 → **登录-正确 / 用户B / 管理员** … → 改数量 1 / 10 / 11 → …

问题等级：P2
问题类别：PED / SEQ
问题说明：简称漏「注册-手机号占用」；合法注册写成「注册」；建议顺序与 JSON 默认顺序不同（JSON 是合法 → 占用 → 非法 → 搜索 → …）。Runner **默认按集合顺序**。
为什么有问题：只要登录在改数量/下单/越权之前、无凭证不插在登录与下单中间，两种顺序都能跑。但学生会按步骤 6 去拖拽顺序，找不到「占用」，也不知道默认不用改。
依据：集合 `item` 顺序 1–15；Postman Collection Runner 默认集合顺序。
建议修改：用 15 个全名列出集合顺序，并写「Runner 默认用这个顺序，不要把无凭证拖到创建订单前面」。

---

## ISSUE
ID：CH14-0007
文件：`chapters/14-postman.md`；`chapters/assets/diagrams/`
章节：第 14 章
小节：14.3 变量范围；14.7 越权链
精确位置：L145；L310；现有 `ch14-token-relay.png` 只画单 `token`
原文：范围从宽到窄…；越权-他人订单 / 管理员读明细 **403**
问题等级：P2
问题类别：IMG / PED
问题说明：本章真正难的机制是 (1) 五层变量谁覆盖谁；(2) `token` / `tokenB` / `tokenAdmin` + `lastOrderId` 三条线如何让越权变红。现图只讲三层对象和单 token 接力。
为什么有问题：14.7 越权依赖「登录-正确写 token 并下单写 lastOrderId，登录-用户B 写 tokenB，再 Bearer {{tokenB}} 打 {{lastOrderId}}」。没有图时，学生容易手抄 token 或用错变量。
依据：质量标准「每个难点概念旁边有示意图」；集合三条登录 + 两条越权。
建议修改：补 `ch14-var-scope`、`ch14-auth-chain`（命题见第 16 节）。现有 token-relay 可留在 14.4 教单 token。

---

## ISSUE
ID：CH14-0008
文件：`chapters/14-postman.md`；`chapters/quizzes/stage-5-api.md` Q5 口径相邻
章节：第 14 章
小节：练习 6 答案
精确位置：L505
原文：

> 若无凭证请求复用已写入的 token，可能变成已认证而测不到 401；若它 unset token，后面的创建订单会误失败。

问题等级：P2
问题类别：ANS / HTTP
问题说明：答案只谈 Header 里的 token / unset。仓库集合的无凭证请求**本来就没有** Authorization；真正会让它变 201 的是 Cookie 罐（CH14-0001）。Environment 里有 token 并不会自动贴到没写 Header 的请求上。
为什么有问题：练习 6 问的是 Runner 顺序。按集合真实形态，把「无凭证创建」插在登录和创建订单之间：若该请求仍无 Authorization、也无 Cookie，401 仍成立，创建订单仍带自己的 Bearer，**不一定**测脏。测脏的充分条件是继承了 collection/folder 级 Authorization，或 cookie jar，或复制请求时忘了删 Header。
依据：集合「无凭证创建」header 仅 Content-Type；Postman 变量不会自动变 Header。
建议修改：答案补三种污染源：① 请求仍带 `Bearer {{token}}`；② cookie jar 代发 `minishop_session`；③ unset 了后续还要用的 token。

---

## ISSUE
ID：CH14-0009
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.6；本章总结；面试
精确位置：L249–265；全文无 Newman / Postman CLI
原文：Collection Runner…（未提命令行）
问题等级：P2
问题类别：JOB
问题说明：初级测试岗把 Postman 集合交给 CI 时，用的是 Newman 或 Postman CLI，不是每天点 GUI Runner。本章标 ⭐⭐⭐ 的 Runner 停在 GUI，只一句「Postman 另有性能运行类型，超出本章」。
为什么有问题：不是要求学生装 Newman，但应有一句：GUI Runner 证明你写的断言；仓库/CI 复现用 Newman/`postman collection run`，且本仓库作者未跑。集合也未声明相对 OpenAPI 的子集边界（缺 GET `/api/cart`、`/api/admin/*`、登录 401、四态 Body）。
依据：Postman Docs *Test your API using the Collection Runner* 明确列出 Postman CLI；`openapi.json` 路径多于 15 条。
建议修改：14.6 末加 ⭐ 了解：CI 用 CLI；本章作业只要求 GUI 文字结果。14.7 加一行「这 15 条是教学子集，不是 OpenAPI 全覆盖」。

---

## ISSUE
ID：CH14-0010
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.2 Params
精确位置：L98–99
原文：`Path /api/orders/:orderId` 与 `{{orderId}}`
问题等级：P2
问题类别：TERM / PED
问题说明：Postman Path 变量是 URL 里的 `:orderId` 再在 Params 里赋值；`{{lastOrderId}}` 是环境变量直接替换。集合用的是后者：`/api/orders/{{lastOrderId}}`。正文把两种写法揉在一句，还用了错误变量名。
为什么有问题：新手会在 Params 建一个 `orderId` 却不引用，或以为 `{{orderId}}` 就是 Path 变量。
依据：Postman 请求 Params 的 Path 与 `{{var}}` 是不同替换层。
建议修改：先给集合原样 URL，再用脚注区分 `:id` 与 `{{lastOrderId}}`。

---

## ISSUE
ID：CH14-0011
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.2 GET/POST 语义
精确位置：L96
原文：第 9 章的语义在这里不变：GET 用于读取…不要说“POST 更安全所以登录必须 POST”
问题等级：P2
问题类别：PED / SEQ
问题说明：安全方法、登录为何 POST，第 9/13 章已教。这里占了「对着集合看 Params / Body / Tests 面板」的位置。语义本身**正确**，不是技术错误。
为什么有问题：核心章 14.2 应把第一帧放在已导入请求的面板，而不是再讲一遍 GET/POST。
依据：大纲第 14 章范围是 Workspace/Collection/变量/脚本/Runner；GET/POST 属第 9 章。
建议修改：压成一句回指第 9、13 章。

---

## ISSUE
ID：CH14-0012
文件：`chapters/14-postman.md`；`MiniShop.postman_collection.json`
章节：第 14 章
小节：14.1 表「按业务文件夹组织」
精确位置：L73
原文：按业务文件夹组织，如 `auth`、`cart`、`orders`
问题等级：P2
问题类别：PED
问题说明：仓库集合是 15 个扁平 `item`，没有 folder。14.1 把它写成纪律，学生打开仓库对不上。
为什么有问题：Runner 靠文件夹也能分段跑。扁平可以，但应标明「教学集合为了少点击做成扁平，工作中再按业务建文件夹」。
依据：集合 JSON 无嵌套 `item`。
建议修改：表内加「仓库集合是扁平 15 条，文件夹是工作中的组织法」。

---

## 6. P3

## ISSUE
ID：CH14-0013
文件：`MiniShop.postman_collection.json`
章节：第 14 章配套集合
小节：越权-他人订单脚本
精确位置：集合 L212–217
原文：`pm.expect(json.id).to.not.eql(pm.environment.get('lastOrderId'));`
问题等级：P3
问题类别：TEST
问题说明：403 体是 `{"error":"forbidden"}`，没有 `id`。`undefined !== lastOrderId` 为真，断言碰巧通过。真正要防的泄露应是 `pm.expect(json).to.not.have.property('id')`（pytest 用了 `"id" not in body or id != order_id`）。
依据：实服务 403 body；`server.py` `_get_order` L494。
建议修改：改成 not.have.property('id')，或删掉这条多余比较。

---

## ISSUE
ID：CH14-0014
文件：`MiniShop.postman_collection.json`
章节：第 14 章配套集合
小节：改数量-合法 / 等于库存
精确位置：集合 L131–132、L147
原文：只 `pm.response.to.have.status(200)`
问题等级：P3
问题类别：TEST
问题说明：未断言 Body 的 `sku`/`qty`。qty=11 拒绝后数量不应变成 11，集合也没 GET `/api/cart` 核对（正文倒是强调脚本绿 ≠ 库对）。
建议修改：至少 `pm.expect(json.qty).to.eql(1)` / `10`；库存核对仍指向 SQL。

---

## ISSUE
ID：CH14-0015
文件：`chapters/14-postman.md`
章节：第 14 章
小节：参考资料
精确位置：L558–561
原文：Variables / Environments / Collection Format 三个 URL
问题等级：P3
问题类别：LINK
问题说明：2026-09-10 探测：

| 正文 URL | HTTP | 最终地址 |
| --- | --- | --- |
| `…/sending-requests/variables/variables` | 308 | `…/use/send-requests/variables/variables/` |
| `…/sending-requests/variables/managing-environments` | 308 | `…/use/send-requests/variables/managing-environments/` |
| `schema.getpostman.com/json/collection/v2.1.0/collection.json` | 301 | `schema.postman.com/json/collection/v2.1.0/collection.json` |
| pm-test-expect | 200 | 同路径仍有效 |
| intro-to-collection-runs | 200 | 同路径仍有效 |

建议修改：换成 308/301 后的 canonical URL。旧链能跳转，不阻断阅读。

---

## ISSUE
ID：CH14-0016
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.3 初始值 / 当前值
精确位置：L147；L281
原文：可分享的初始值与本机当前值
问题等级：P3
问题类别：TERM
问题说明：现行官方文档主用语是 **local value / shared value**。Initial/Current 是旧栏名。章首已声明「界面文案会改」，概念仍对（凭证只留本机、不要分享）。
建议修改：括号注明「界面可能写成 local / shared」。

---

## ISSUE
ID：CH14-0017
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.6.1 末两张图
精确位置：L291–293
原文：本机同等接口证据（curl/pytest，不是 Runner 截图）
问题等级：P3
问题类别：IMG / PED
问题说明：诚实，不是假装 Runner 截图。但对「怎么看 Postman 失败行」零帮助。token-relay 图插在导入步骤开头，命题也不配「Import」。
建议修改：保留并维持「不是 Runner」标题；把 token-relay 移回 14.4。

---

## ISSUE
ID：CH14-0018
文件：`MiniShop.postman_environment.json`
章节：第 14 章配套环境
小节：环境文件格式
精确位置：全文 15 行
原文：仅 `name` + `values`，无 `id`、`_postman_variable_scope`
问题等级：P3
问题类别：CODE
问题说明：官方导出通常带 `id` 与 `_postman_variable_scope: environment`。现行精简 JSON 多数版本仍能 Import 成 Environment，但不是完整导出形态。`type: secret`、password/token 空值是对的。
建议修改：补 `_postman_variable_scope`；保持密钥空。

---

## ISSUE
ID：CH14-0019
文件：`chapters/14-postman.md`
章节：第 14 章
小节：14.5 纪律 vs 登录脚本
精确位置：L237 vs L165–173
原文：一条 `pm.test` 只验证一件主要事情
问题等级：P3
问题类别：PED
问题说明：登录示例把状态码、result、token 类型和 `set` 捆在一条 test 里（集合同样）。作为「失败则不要写入错误 token」这是好设计，但与「一件事」字面冲突。
建议修改：改成「一条 test 一个意图；登录这条意图是『成功才写 token』，所以断言和 set 放一起」。

---

## 7. 逐段问题

| 单元 | 判定 | 关联 |
| --- | --- | --- |
| 标题 / 一句话核心 | 通过。过滤器有效：本章是「可重复集合」，不是再讲 REST。 | — |
| 重要级别 / 核心章目标 | 通过。 | — |
| 这一章解决什么问题 | 通过。承接 curl 手改 Token；不能代替契约和 SQL；导入而非另造 `/login`。 | — |
| 学习目标 8 条 | 通过。与大纲 Workspace/Collection/Env/Token/pm.test/Runner/脱敏对齐。Runner 目标对学习者，不要求作者已点 GUI。 | CH14-0001 完成时需补 Cookie |
| 前置知识 | 通过。第 13/9 章、Cookie≠Bearer、需安装 Postman。 | — |
| 场景导入 + Mermaid | 通过。痛点具体；图 Environment→Request→断言→写回 token→Runner 正确。 | — |
| 14.1 层次表 + 图 | 表技术正确。文件夹纪律与扁平集合不一致。图 KEEP。 | CH14-0012 |
| 14.2 GET/POST | 语义正确（非 POST 更安全）。主动作写成新建；Path 变量名错；列表警告与 14.5 打架。 | CH14-0004/0005/0010/0011 |
| 14.2 Cookie 可并存 | HTTP 口径正确，未写 Postman jar 后果。 | CH14-0001 |
| 14.3 Environment 表 | `baseUrl`/`phone`/`token` 对；`orderId` 错。范围五层与官方一致。`pm.variables.get` 正确。未选环境会原样发出 `{{baseUrl}}` 正确。初始/当前值用语略旧。 | CH14-0002、0016 |
| 14.3 两行 set/get | 已标明不是完整测试。通过。 | — |
| 14.4 Token 接力 | 流程与 `/api/login`、Bearer 正确；登录脚本对实服务 200 可通过并 set token。未提 cookie jar。unset token 不够。 | CH14-0001 |
| 14.5 pm.test/expect | API 未过时（2026-09 官方仍是 `pm.test` + `pm.expect` + `pm.response.code` / `to.have.status`）。列表脚本弱；创建订单变量名错；第 6 步残留。超库存/无凭证脚本在无 Cookie 时正确。 | CH14-0002/0003/0005 |
| 14.6 Runner | Keep variable values / Persist 仍是官方选项名。未写 *without stored cookies*。性能运行超出本章的声明正确。CSV 标进阶诚实。 | CH14-0001、0009 |
| 14.6.1 导入 8 步 | 路径、环境名、8765、password 当前值、空搜索允许红、15 条计数均对。步骤 6 简称与顺序有问题。GUI 未点已披露。 | CH14-0006、0001 |
| 14.7 对照表 | 15 名、方法路径、qty=10/11、201 无 status、403、BUG-001 与 JSON/PRD 一致。缩写合法。明确不要另造 `/login`。Teaching 名称有解释。 | 变量名问题在表外 |
| 工作实战模板 | 产出路径、清单、Token、Runner 文字、脱敏均能验收。完成标准「空搜索允许红」在 Cookie 默认下不充分。 | CH14-0001 |
| 错误 1–10 | 技术正确。缺 Cookie 罐。错误 8 GET 登录、错误 9 幂等、错误 10 集合≠OpenAPI 都对。 | CH14-0001、0008 |
| 面试 5 题 | 结论→边界结构合格。Runner 绿不能上线正确。 | 可补 Cookie 一句 |
| 小练习 1–10 / 答案 | 见 §11。Q7=C 正确。Q8 变量名错。Q6 不完整。 | CH14-0002、0008 |
| 检查清单 / 门槛 | 可验证。门槛 2「无凭证 401」在 GUI 默认下可能失败。 | CH14-0001 |
| 本章总结 7 条 | 通过。 | — |
| 可运行性说明 | **诚实**：未点 GUI；15 条 `/api/`；脚本曾模拟执行。未披露 Cookie 罐会使 401 条失败。 | CH14-0001 |
| 参考资料 | 5 个外部链可到达（2 个 308、1 个 301）。内部链文件存在。核验日期只写在 pm-test 一条。 | CH14-0015 |
| 下一章预告 | 通过。只点读/改小段脚本，不抢 pytest。链到 `15a-python-syntax.md` 存在。 | — |

禁止的错误绝对化：本章均作为**反面**出现（POST 更安全、Cookie/Bearer 三选一、Runner 全绿=无缺陷/可上线）。通过。

MiniShop 第 19 章前口径：本章工作实战与集合已是 v1.0 `/api/`，并标明不要和已删除的教学 `/login` 当成两套契约。通过（旧复审 S5-08 失效）。

---

## 8. 代码问题

### 8.1 正文 JavaScript（7 块）

| 块 | 实服务 / 模拟结果 | 问题 |
| --- | --- | --- |
| `pm.environment.set/get` 两行 | 本身合法；缺 `tokenValue` 定义 | 已标明不是完整测试，通过 |
| 登录成功脚本 | 对 `POST /api/login` 200 `{result:ok, token, role}` **通过** 并写入 token | 未断言 `role`（非必须） |
| 列表脚本 | `keyword=鼠标` 通过；`keyword=mouse` 空数组也通过 | CH14-0005 |
| 超库存 | `qty=11` → 400 `{error: qty exceeds stock}` 通过 | 未断言 error 字符串，弱但可接受 |
| 创建订单 | 201 `{id}` 无 status；连跑两次 id 不同，脚本比较逻辑成立 | 写入 `orderId` 而非 `lastOrderId`（CH14-0002） |
| 无凭证 401 | **无 Cookie** 时 POST `/api/orders` → 401 通过；**仅 Cookie** 时 → 201，脚本失败 | CH14-0001 |
| 练习 4 反例 | 故意错误，教学有效 | 通过 |

`pm.test` / `pm.expect` / `pm.response.code` / `pm.response.json` / `pm.environment.set|get|unset` / `pm.response.to.have.status`：**未过时**（官方 2025-11 / 2026 文档仍列这些 API）。Tests 标签现多叫 Post-response，正文已双写。`pm.test` 现也可出现在 Pre-request，错误 4 限制的是「用 Pre-request 判断响应」，仍然正确。

### 8.2 仓库 Collection（v2.1，15 条）

`info.schema` 指向 Collection v2.1.0，JSON 可解析。全部 URL 含 `/api/`。无 folder。无 collection-level auth。密钥未写死。

对照 OpenAPI / PRD / 实服务（Cookie 关闭）：

| # | name | 方法路径 | 期望 | 实服务 | 脚本 |
| ---: | --- | --- | --- | --- | --- |
| 1 | 注册-合法 | POST `/api/register` | 201 phone 无 token | 201 `phone=13900004444` | 通过 |
| 2 | 注册-手机号占用 | 同 | 409 | 409 `phone taken` | 通过 |
| 3 | 注册-非法手机号 | 同，phone 10 位 | 400 `invalid phone` | 400 | 通过 |
| 4 | 搜索商品 | GET `?keyword=鼠标` | 200 命中 SKU-DEMO-001 | 命中无线鼠标 | 通过 |
| 5 | 空搜索-BUG-001 | `keyword=   ` | 按 R-SEARCH 应失败 | 200 三件商品 | **断言失败，符合 BUG-001** |
| 6 | 登录-正确 | POST `/api/login` | 200 set `token` | 200 + Set-Cookie | 通过 |
| 7 | 登录-用户B | 同 `phoneB` | set `tokenB` | 200 | 通过 |
| 8 | 登录-管理员 | `phoneAdmin` | `role=admin` set `tokenAdmin` | 200 role=admin | 通过 |
| 9 | 改数量-合法 | POST `/api/cart/items` qty=1 | 200 | 200 | 仅状态码（CH14-0014） |
| 10 | 改数量-等于库存 | qty=10 | 200 | 200 | 仅状态码 |
| 11 | 改数量-超库存 | qty=11 | 400 `qty exceeds stock` | 400 | 通过 |
| 12 | 创建订单 | POST `/api/orders` SKU-DEMO-003 qty=1 | 201 id 无 status，set `lastOrderId` | 201 `ord-…` | 通过；不测幂等（14.7 已说明） |
| 13 | 无凭证创建 | 无 Authorization | 401 | 无 Cookie→401；有 Cookie→**201** | CH14-0001 |
| 14 | 越权-他人订单 | GET `/api/orders/{{lastOrderId}}` Bearer tokenB | 403 | 403 `forbidden` | 多余 id 比较碰巧过（CH14-0013） |
| 15 | 越权-管理员读明细 | Bearer tokenAdmin | 403 | 403 | 通过；符合 R-PERM |

创建订单用 `SKU-DEMO-003` 而购物车用 `SKU-DEMO-001`：订单接口按 Body sku/qty 扣库存，不读购物车，解耦合理；正文未写明 sku，P3 级可补一句。

二次 Runner 不重启服务：`注册-合法` 对已占用的 `newPhone` 变 409。正文已提示改号。`MINISHOP_RESET=1` 每次 `run.py serve` 会重建库。

### 8.3 Environment

| key | 文件值 | 判定 |
| --- | --- | --- |
| baseUrl | `http://127.0.0.1:8765` | 与 README / PRD 一致 |
| phone / phoneB / phoneAdmin | 种子号 | 与 PRD 教学数据一致 |
| newPhone | `13900004444` | 合法 11 位，非种子 |
| password / token / tokenB / tokenAdmin | 空，`type: secret` | 正确，不入库 |
| lastOrderId | 空 | 正确；正文误作 orderId |
| orderId | **不存在** | CH14-0002 |

### 8.4 命令

`cd project/minishop && python3 run.py serve`：与项目 README 一致，可启动 `http://127.0.0.1:8765`。默认重置教学库。端口占用时第二份会失败，正文未写，初学者摩擦（不单列 ISSUE）。

Newman / Postman CLI：本机不存在，未跑。不记作者未点 GUI 为缺陷。

---

## 9. 图片问题

### IMG-CH14-001
文件：`chapters/assets/diagrams/ch14-workspace.png`（源 `ch14-workspace.html`）
出现位置：14.1
图片主要内容：三张卡片 Workspace / Collection / Environment。标题「抽屉柜、一叠点菜单、桌上的地址条」。
技术准确性：Environment 覆盖 Collection、password/token 留空、路径 `/api/`、未点 GUI，均正确。
与正文一致性：与 14.1 表一致。隐喻（抽屉柜等）未在卡片上逐一标注，可读但仍能懂。
文字是否正确：是。
UI 是否过时：示意图不是产品截图，不适用。
教学价值：把三层分工收成一句，值留。
可读性：好。
是否需要修改：可选给隐喻加对应标签。
最终结论：**KEEP**

### IMG-CH14-002
文件：`chapters/assets/diagrams/ch14-token-relay.png`（源 `ch14-token-relay.html`）
出现位置：14.6.1 开头（命题更适合 14.4）
图片主要内容：登录 `POST /api/login` → `pm.environment.set('token')` → 改数量 Bearer `{{token}}` qty 1/10/11 → 无凭证不带 Authorization 期望 401。
技术准确性：单 token 接力正确；未画 `tokenB`/`lastOrderId`；未画 Cookie 罐。无凭证「不要带 Authorization」在 GUI 下不充分（CH14-0001）。
与正文一致性：与 14.4 一致；与 14.7 越权链不完整。
文字是否正确：是。`{{token}}` 未写成死 token。
教学价值：本章主机制，值留。缺三线接力另补图，不因此 REPLACE。
可读性：好。
最终结论：**KEEP**（建议移到 14.4；另增 auth-chain）

### IMG-CH14-003
文件：`chapters/assets/08-network-log.png`
出现位置：14.6.1
图片主要内容：MiniShop v1.0 本机请求记录表（登录 200/401、空搜索 BUG-001、qty 10/11、下单无 status、注册 201/409）。自题「不是 Chrome DevTools 面板截图」，token 已打码。
技术准确性：与 PRD / 实服务一致。
与正文一致性：正文标明「curl/pytest，不是 Runner 截图」。未假装 GUI。
教学价值：对 Postman 面板帮助弱，作诚实旁证可留。
可读性：好。
最终结论：**KEEP**

### IMG-CH14-004
文件：`chapters/assets/09-pytest-report.png`
出现位置：14.6.1
图片主要内容：pytest-html，38 tests，37 Passed，1 Expected failure，0 Failed。日期 09-Sep-2026，pytest-html v4.2.0。
技术准确性：与仓库基线 `37 passed, 1 xfailed`（BUG-001）一致。
与正文一致性：alt「pytest 37 passed / 1 expected failure」正确。
教学价值：证明接口基线，不是 Runner。
最终结论：**KEEP**

HTML 源与 PNG 文案一致，未发现「修了 HTML 忘出 PNG」。

---

## 10. 表格问题

| 表 | 判定 |
| --- | --- |
| 14.1 Workspace/Collection/Request | 作用与纪律正确。文件夹示例与扁平集合不一致（CH14-0012）。 |
| 14.3 常用变量 | `baseUrl`/`phone`/`token` 正确。`orderId` 应改 `lastOrderId`（CH14-0002）。缺 `tokenB`/`tokenAdmin`/`newPhone`（可在 14.7 补，非必须进此表）。 |
| 14.7 集合对照 | 15 条缩写可还原到 JSON 全名。方法、断言、403、BUG-001、无 status 均对。Path 写成 `{id}` 作为模式可接受。 |

无把 P0/P1 写成全球统一、无订单状态臆造。

---

## 11. 练习与答案问题

独立作答在对照教材答案之前完成（测验文件虽同页含答案，已按官方变量范围、本章口径与实服务重判）。

### 小练习 1–10

| 题 | 独立答案 | 教材答案 | 结果 |
| ---: | --- | --- | --- |
| 1 | Workspace=协作边界；Collection=一组可分享请求；Request=单次调用。扁平无名列表在 Runner 里不可读。 | 同义 | 通过 |
| 2 | `baseUrl` 随环境变，请求只保留 `/api/` 路径。 | 同义 | 通过 |
| 3 | ① 登录是否 200 且脚本执行 ② 是否选中 Environment 且有 token ③ Header 是否 `Bearer {{token}}` | 同序三点 | 通过（可再加 Cookie 罐） |
| 4 | 未断言就 set；`pm.test` 恒真；失败登录可能写入 `undefined` | 同义 | 通过 |
| 5 | 不能。还要超库存 400/错误体，并 SQL 核 qty/stock | 同义 | 通过 |
| 6 | 见 CH14-0008：教材只谈 token Header/unset，漏 Cookie 罐与「无 Header 并不自动带 token」 | 部分对 | **不记 ANSWER VERIFICATION FAILED**（未写反，不完整） |
| 7 | C | C | 通过。A 泄密、B 三选一、D 出口标准，均应排除 |
| 8 | 第一次 set `lastOrderId`，第二次 `not.eql`；若改幂等则同 id 或拒绝重复，以正式文档为准 | 逻辑对，变量写成 `orderId` | **【ANSWER VERIFICATION FAILED】** 变量名与仓库不一致（CH14-0002） |
| 9 | 密码、token、Cookie、内部 URL；集合与 cURL 一样复制凭证 | 同义 | 通过 |
| 10 | `POST {{baseUrl}}/api/login`；Body `phone`+`{{password}}`；断言 200、`result=ok`、token 为字符串并 set。不写真实密码、不写订单状态 | 合理等价 | 通过 |

### 阶段测验（第 14 章相关）

**Q3** 测 MiniShop v1.0 登录以哪份为准？对着 `POST /login` 会怎样？  
独立：PRD + OpenAPI；路径 `/api/login`；无前缀 `/login` → 404。  
教材：同。通过。与 14.7「不要另造 `/login`」一致。

**Q4** Environment 和 Collection 变量谁覆盖谁？（课程口径）  
独立：Environment 更窄，覆盖 Collection。完整链是 global < collection < environment < data < local。  
教材：Environment 覆盖 Collection。通过。未写 data/local 在阶段测验可接受；14.3 已写全链。

**Q5**（必过）登录脚本写入 token 后，401 用例为什么不能插在已登录下单前还共用 Session？  
独立：已写入的凭证（Header 或 Cookie/Session）会让「无凭证」变成已认证，断言 401 变成 201/200。  
教材：会先带上登录态，测不到 401；不要 autouse token，也不要共用已登录 Session。通过。略偏 pytest 用语，未写反。Cookie 罐是同一类污染，正文应补。

Q7/Q8/Q10 属 15–16 章，本 Agent 不扩审。

---

## 12. 初学者理解障碍

【Beginner Friction】

1. **先建后导**：14.2「新建」→ 14.6.1 才 Import → 14.7「不要另造」。会做两套集合（CH14-0004）。
2. **变量还没教就出现 `{{baseUrl}}`**：14.2 早于 14.3。
3. **`orderId` / `lastOrderId`**：越权红不了却不知道为什么（CH14-0002）。
4. **「第 6 步」幽灵步骤**（CH14-0003）。
5. **Runner 两条红**：空搜索 + 无凭证。正文只解释前者（CH14-0001）。这是最伤验收的摩擦。
6. **password 当前值**：环境文件是空的，漏填则登录全 400/401，步骤 4 有写，仍容易漏。
7. **注册-合法第二次 409**：有提示，但与「跑通」并置时新手会以为集合坏了。
8. **Teaching 名称**：14.7 有解释，仍可能以为还有另一套教学服务。
9. **星级全 ⭐⭐⭐**：变量范围、Runner 持久化对零基础偏密，缺少「可先跳过」标记。

---

## 13. 岗位能力缺口

【Job Reality Gap】

1. Cookie 罐 vs Bearer 是接口测试日常翻车点，本章没教，集合还踩进去（CH14-0001）。
2. Newman / Postman CLI / CI 只字未提（CH14-0009）。
3. 集合无 folder、无 collection-level auth 演示（工作中两者都常见）。
4. 未覆盖 OpenAPI 的 GET `/api/cart`、`/api/admin/*`、登录失败 401、四态 Body；未声明「教学子集」。
5. 无环境：Initial/local vs shared、Vault、团队角色（Viewer 不能改 shared）仅点到分享风险。
6. 断言质量：多条只检查状态码；越权多余比较；没有把 OpenAPI schema 校验（`jsonSchema`）哪怕作为 ⭐。
7. 岗位面试常问「如何参数化 / 如何在 CI 跑集合 / 如何避免把 token 提交到 Git」——前两个偏弱，第三个较好。

不是要求本章写成 Postman 专家课；核心章应把 **401 隔离在真实 GUI 里能红对** 讲完。

---

## 14. 建议删除内容

- 14.5「第 6 步再创建订单」整句（CH14-0003）。
- 14.2 把「新建 Request」当作本章动作的第一句（CH14-0004）。
- 14.5 仅断言 `items` 为数组的「正式」列表脚本（可降为反例，CH14-0005）。
- 可选：14.2 大段 GET/POST 语义，改为回指第 9 章（CH14-0011）。

不要删除：GUI 未点的诚实声明；空搜索允许红；订单无 status；脱敏纪律；Runner 绿 ≠ 出口标准。

---

## 15. 建议新增内容

1. Cookie 罐与 401 隔离（正文 + 集合 `disableCookies` + Runner 选项）。见 CH14-0001。
2. 图 `ch14-var-scope`：global → collection → environment（点名空 token 初始值）→ data → local；旁注未选环境时 `{{baseUrl}}` 原样发出。
3. 图 `ch14-auth-chain`：登录-正确 set token → 创建订单 set lastOrderId → 登录-用户B set tokenB → 越权 Bearer tokenB + Path lastOrderId → 403；无凭证单独、禁 cookie jar → 401。
4. 14.7 一行：15 条是教学子集，不是 OpenAPI 全覆盖。
5. 14.6 一句 ⭐：CI 用 Newman/Postman CLI，本章不要求安装。
6. 创建订单脚本与环境统一 `lastOrderId`；不幂等用「复制请求」而不是第 6 步。

---

## 16. 建议重写内容

- **14.2** 整节：对着已导入请求看 Params/Body/Headers/Response，而不是新建 + 重讲 GET/POST。
- **14.5 列表与创建订单**：脚本与仓库集合逐行对齐（sku 命中、`lastOrderId`、无第 6 步）。
- **14.6.1 步骤 6–7**：15 个全名 + 默认集合顺序 + Cookie 选项 + 允许红的清单（空搜索；若未禁 Cookie 则无凭证也会红）。
- **练习 6、8 答案**：Cookie 罐；`lastOrderId`。

不需要重写：14.1 层次、14.3 范围原理、14.4 单 token 脚本骨架、面试结构、工作实战模板骨架、诚实边界段。

---

## 17. 本章结论

**C 明显需要修改**

不能选 A/B：存在多处 P1，且主实操集合在所教工具的默认行为下无法满足自己写的完成标准。  
不能选 D/E：脊柱（层次、环境、token 脚本、`pm.test`、脱敏、诚实 GUI、v1.0 `/api/` 15 条、BUG-001 开放、订单无 status）是对的，用定点补丁可修，不必整章重设计。

Definition of Done（质量标准 20 项）本轮判定：

| # | 项 | 结果 |
| ---: | --- | --- |
| 1 | 目标明确 | 通过 |
| 2 | 前置知识正确 | 通过 |
| 3 | 无知识性错误 | **失败**（401 隔离在 GUI 下不成立；变量名；幽灵第 6 步） |
| 4 | 重要信息未过时 | 通过（sandbox API 仍有效；个别文档 URL 308） |
| 5 | 无错误绝对化 | 通过 |
| 6 | 术语准确 | **失败**（orderId / lastOrderId；Path `:id` 与 `{{var}}`） |
| 7 | 零基础能理解 | **失败**（先建后导；Runner 两条红无解释） |
| 8 | 示例具体 | **失败**（14.5 与集合两套脚本） |
| 9 | 有实际工作场景 | 通过 |
| 10 | MiniShop 一致 | **失败**（无凭证 × Cookie；变量名） |
| 11 | 代码经过验证 | **失败**（GUI 路径未验证导致 401 条缺陷；无 Cookie 重放 14/15） |
| 12 | SQL 安全 | 不适用，通过 |
| 13 | 图表帮助理解 | 通过（有缺口，未到失败） |
| 14 | 重要级别明确 | 通过 |
| 15 | 常见错误有价值 | 通过（缺 Cookie） |
| 16 | 面试非死记 | 通过 |
| 17 | 练习覆盖目标 | 通过 |
| 18 | 答案对应练习 | **失败**（练习 8 变量名） |
| 19 | 检查清单可验证 | 通过（门槛 2 受 CH14-0001 影响） |
| 20 | 衔接下一章 | 通过 |

**13/20**。17 及以下不得发布。修完 CH14-0001～0005 并重跑「禁 Cookie 的 15 条」后可再评；预期仍要补 Cookie 教学才接近核心章 95。

作者未点 Collection Runner：**按尺不记缺陷**。本轮 P1 来自 JSON + 服务端认证行为，不需要 GUI 也能发现。

---

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`
- `reviews/_full-audit-2026-09-10/AUDIT_PROGRESS.md`
- `README.md`、`docs/COURSE_CONTROL.md`、`docs/COURSE_OUTLINE_v1.2.md`、`docs/LEARNING.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`、`practice/STATUS.md`、`exercises/README.md`
- `project/minishop/README.md`、`docs/PRD.md`、`docs/openapi.json`、`bugs/BUG-001.md`
- `project/minishop/server.py`（`_token` / login / register / cart / orders / get_order）
- `project/minishop/tests/test_api.py`
- `project/minishop/postman/MiniShop.postman_collection.json`
- `project/minishop/postman/MiniShop.postman_environment.json`
- `chapters/14-postman.md`
- `chapters/quizzes/stage-5-api.md`、`chapters/quizzes/README.md`
- `chapters/assets/diagrams/ch14-workspace.{png,html}`、`ch14-token-relay.{png,html}`、`README.md`
- `chapters/assets/08-network-log.png`、`09-pytest-report.png`
- `reviews/chapter-14-review.md`、`reviews/_pedagogy-2026-09-10/ch14.md`、`RUBRIC.md`
- `reviews/v1.2.1-rescore.md`、`reviews/_rereview-2026-09-09/stage-5-ch13-16.md`、`reviews/full-course-audit-v1.2.md`（仅线索；14.7 手建 `/login` 等旧结论已复核为过时）

未读其他章正文（第 13/15 章仅确认内部链接文件存在，未审其内容）。

### 实际跑过的命令与结果摘要

- `python3 --version` → 3.14.3
- `which newman postman` → 均不存在（故无 Newman/GUI 运行）
- 解析 Collection：`info.name=MiniShop v1.0 Teaching`，schema v2.1，**15** 个 item，路径均含 `/api/`
- 启动临时 MiniShop（`MINISHOP_RESET=1`，`MINISHOP_PORT` 随机，独立 sqlite）
- 用 `requests` 按集合顺序重放 15 条，**两轮**：

  - Cookie 关闭：14 pass / 1 fail（空搜索 BUG-001）
  - Cookie 开启（`requests.Session` 保存 `minishop_session`）：13 pass / 2 fail（空搜索 + **无凭证创建 HTTP 201**，body 含新 `id`）
- 登录响应含 `result=ok`、`token`、`role`、`Set-Cookie: minishop_session=…; HttpOnly`
- 仅 Cookie、无 Bearer 的 `POST /api/orders` → **201**（与 pytest `test_login_ok` 用 Cookie 访问 `/api/cart` 一致）
- 越权 403 body = `{"error":"forbidden"}`，无 `id`
- `qty=11` → `{"error":"qty exceeds stock"}`；`keyword=鼠标` 命中 `SKU-DEMO-001`；`keyword=mouse` → `items: []`
- 正文创建订单脚本连跑两次：两个不同 `id`，无 `status`
- `curl -sI` 五个参考链接：见 CH14-0015

未做：Postman 桌面 Import、Collection Runner 点击、Newman。

### 外部核查

| 条目 | 来源 | 结论 |
| --- | --- | --- |
| 变量范围 broad→narrow | Postman Docs *Store and reuse values using variables*；`pm-variables` | global, collection, environment, data, local；更窄覆盖更宽。正文正确 |
| `pm.test` / `pm.expect` / `pm.response.code` | *Writing tests and assertions*（文档页标注 2025-11-04）；本机 GET 该 URL **HTTP 200** | 未过时 |
| `pm.response.to.have.status` | *Write scripts to test API response data* | 未过时；集合在用 |
| Tests vs Post-response | 同上，官方示例写在 Post-response | 正文双写正确 |
| Environment local/shared | *Share variables*；*Edit environment variables* | 正文「初始值/当前值」概念对、用词旧 |
| Collection Runner Keep variable values | *intro-to-collection-runs* HTTP 200 | 名称仍存在 |
| Run collection without using stored cookies | 同上 Advanced settings | **正文未写，集合需要** |
| Disable cookie jar | *Cookies* 文档：请求 Settings → Disable cookie jar | 无凭证条应打开 |
| `protocolProfileBehavior.disableCookies` | postman-runtime 文档 | 可写入 collection JSON |
| Collection Format v2.1 | schema 301 到 `schema.postman.com` 后 HTTP 200 | 仍有效 |
| Variables/Environments 旧路径 | 308 到 `/docs/use/send-requests/variables/…` | 能跳转，建议更新 |

【External Verification Required】：未能在本机打开 Postman 桌面确认 2026 年 GUI 按钮文案是否仍叫 Collection Runner / Tests；正文已声明「用应用内搜索英文名」，不把具体菜单坐标当事实。Cookie 罐行为有官方文档 + 服务端双重依据，不依赖 GUI 截图即可成立。
