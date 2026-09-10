# FIX RECORD
Audit ID：M-P1-35
原问题：阶段测验 3 第 5 题标准答案写「401 未通过认证（无 token 下单）」。MiniShop 仅缺 `Authorization`、Cookie `minishop_session` 仍在时，`POST /api/orders` 为 **201**，不是 401。
修改文件：`chapters/quizzes/stage-3-web.md`
修改位置：答案第 5 题；同卷答案第 9 题末句作 LOCAL REGRESSION（原「后续 API 以 Bearer 为准」会与第 5 题打架）。
原内容：（摘录）
> 5. 401 未通过认证（无 token 下单）；403 已认证但没权限（普通用户打 `/api/admin/*`，……）。
> 9. ……后续 API 以 Bearer 为准。
修复后内容：（摘录）
> 5. 401：没认出你——无有效凭证（无 Bearer **且** 无 Cookie `minishop_session`）……仅缺 `Authorization`、浏览器仍带着 Cookie 时，MiniShop 仍可能 201。403：……普通用户打 `/api/admin/*`……或用户 B 读 A 的 `GET /api/orders/{id}`。
> 9. ……后续请求可以带 Bearer；没有 Bearer 时 Cookie `minishop_session` 仍能认人。
为什么这样修：与 M-P1-09 同一机制，落点是测验标准答案。把「无 token」写成 401 会判错 Cookie-only 201。
依据：MiniShopLab：Cookie-only `POST /api/orders` + sku/qty → **201**；无凭证同请求 → **401**。`server.py` `_token()`。
是否影响其他章节：08B 见 M-P1-09。第 20 章面试示例、第 9 章状态码示意图仍有「无 token 下单」旧句，不在本 ID 范围。
验证结果：改完后独立再答测验 3（先于对照答案）：
1. 层次不同、常配合：Cookie 存/带，Session 服务端状态，Token 凭证。
2. HttpOnly 阻止脚本读取；不阻止请求自动携带。
3. 不能。前端约束可绕过。
4. safe=不请求改变资源状态；幂等=多次与一次效果相同；可缓存是另一项。不能说 GET 不安全、POST 安全。
5. 401=无凭证（无 Bearer **且** 无 Cookie）访问受保护接口；仅缺 Authorization 仍可能 201。403=已认证但不许（B 读 A 订单；普通用户 `/api/admin/*`）。
6. 先开 Network 以免请求已结束；Preserve log 防整页跳转清空列表（MiniShop 登录是 hidden 切换，见第 10 章口径）。
7. 先删 Cookie / Authorization / 密码再保存或转发。
8. Waiting 是已建连后等首字节，不等于下载完成，也不等于页面级 TTFB。
9. JSON `token` + `Set-Cookie`（HttpOnly）；后续可带 Bearer，Cookie 仍能认人。
10. C。A 把 Bearer 当 Session；B Disable cache 关面板后通常不生效；D Lax 挡不住一切跨站请求。
对照新答案：第 5、9 题一致；其余与卷面一致。
状态：FIXED
