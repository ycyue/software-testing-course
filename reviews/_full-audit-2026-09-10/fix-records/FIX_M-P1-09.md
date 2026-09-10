# FIX RECORD
Audit ID：M-P1-09（对应 CH08-0001）
原问题：08B 把「不带 Bearer」写成 MiniShop 未认证 401。`server.py` `_token()` 先读 Bearer，再回退 Cookie `minishop_session`。已登录浏览器只删 Authorization 仍可能 200/201。
修改文件：
- `chapters/08b-web-auth-permission.md`
- `chapters/assets/diagrams/ch08-privilege.html`（需重截 PNG）
- `practice/08-privilege/README.md`（与 08B 8.14 口径对齐）
修改位置：8.12 MiniShop 当前实现；8.14 未认证行与 401 门牌；面试示例；可运行性说明；三道门第一盒；8-1 README 401 句。
原内容：（摘录）
> 无 Bearer 访问 `/api/cart` 或 `/api/orders` → 401
> 没带有效登录凭证 → **401**
> 未认证 401 可以自己对 `/api/orders/{id}` 不带 Bearer 看一眼。
修复后内容：（摘录）
> MiniShop 无 Bearer 时仍读 Cookie `minishop_session`。401 是无 Bearer **且** 无 Cookie。
> 已登录浏览器里只删 Authorization 不够。
> 未认证 401 要用 curl/脚本同时去掉 `Authorization` 和 Cookie。
为什么这样修：Web 功能测试发生在已登录浏览器里；Cookie 会自动带上。把「不带 Bearer」写成 401 会教错未认证怎么测，也浪费「Cookie 与 Token 不是两种登录产品」的现场。
依据：本机 MiniShopLab：Cookie-only `POST /api/orders`（sku+qty=1）→ **201**；Cookie-only `GET /api/orders/{id}` → **200**；两者都不带 → **401**。`server.py` L190–199；PRD `R-AUTH`「Cookie 可并存」。
是否影响其他章节：测验 3 第 5 题见 M-P1-35。第 14 章 Cookie jar 是另一条（M-P1-18）。示意图 PNG 需 Coordinator 按同名 HTML 重截。
验证结果：08B 未认证口径与探针一致；8-1 README 不再写「不带 Bearer 看一眼」。
状态：FIXED
