# 阶段测验 3：Web 与 HTTP

覆盖第 8、9（09A/09B）、10 章。通过线：≥8/10；第 1、4、7 题必过。

1. （必过）为什么不能说“Cookie、Session、Token 是三种登录方式”？
2. `HttpOnly` 能阻止什么？不能阻止什么？
3. 浏览器 `required` 通过，能否证明服务端也会拒绝空手机号？
4. （必过）按 RFC 9110：safe、幂等、可缓存分别约束什么？能不能说“GET 不安全、POST 安全”？
5. 401 和 403 差在哪？MiniShop 里各举一例。
6. 为什么要先打开 Network 再点登录？Preserve log 解决什么？登录成功就一定要勾吗？
7. （必过）Copy as cURL 之后必须先做什么，才能保存或发给别人？
8. Timing 里 **Waiting for server response**（旧称 Waiting (TTFB)）大致包含什么？它等于下载完成时间吗？等于 web.dev 的页面 TTFB 吗？
9. MiniShop v1.0 登录成功时，你应在 Network 里看到哪两类凭证痕迹？（当前实现已是这样；冻结仪式在第 19 章）
10. 哪句正确？ A. Bearer Token 就是 Session B. Disable cache 关掉 DevTools 后通常仍生效 C. 200 也要看响应体 D. Lax Cookie 能挡住一切跨站请求

## 答案

1. 它们层次不同：Cookie 是存储/携带机制，Session 是服务端状态，Token 是凭证。常配合使用。
2. 阻止页面脚本读取该 Cookie；不阻止浏览器在后续请求里自动带上它。
3. 不能。前端约束可被绕过，要以接口或存库结果为准。
4. safe：客户端不请求改变资源状态（写日志不破定义）。幂等：多次相同请求的预期效果与一次相同。可缓存是另一项，不等于 safe。不能用“安全/不安全”替换这两个词，更不能说 GET 不安全、POST 安全。
5. 401：没认出你——无有效凭证（无 Bearer **且** 无 Cookie `minishop_session`）访问受保护接口，例如两者都不带时 `POST /api/orders`。仅缺 `Authorization`、浏览器仍带着 Cookie 时，MiniShop 仍可能 201。403：已认出你但不许，例如普通用户打 `/api/admin/*`（`/api/admin/orders` 或 `/api/admin/products`），或用户 B 读 A 的 `GET /api/orders/{id}`。
6. 先开 Network 是因为请求可能在打开面板前已经结束，与是否跳转无关。Preserve log 解决的是**有文档跳转/整页导航时**列表被清空，不是「登录就必须勾」。MiniShop v1.0 登录是页面内 hidden 切换，未勾选时登录 POST 通常还在；要看清空效果，登录后点「后台」进入 `/admin.html`。
7. 删除 Cookie、Authorization、密码等凭证，只在授权环境复现。
8. 等待首字节，含已建连后的一次往返和服务器准备时间。不等于整段下载完成。现行 Chrome 英文面板写 **Waiting for server response**（文档/旧版可能写 Waiting (TTFB)）；该段不含 DNS/建连/TLS，也不是 web.dev/CrUX 从导航起算的页面 TTFB。
9. 响应 JSON 里的 `token`，以及 `Set-Cookie`（HttpOnly）。后续请求可以带 Bearer；没有 Bearer 时 Cookie `minishop_session` 仍能认人。
10. C。
