# FIX RECORD
Audit ID：M-P1-18
原问题：仓库集合「无凭证创建」只去掉 Authorization。Postman 默认 cookie jar 会带上登录的 `minishop_session`，MiniShop 无 Bearer 时仍认 Cookie，请求变成 201，401 断言失败。正文完成标准只允许空搜索红。
修改文件：`project/minishop/postman/MiniShop.postman_collection.json`；`chapters/14-postman.md`
修改位置：集合「无凭证创建」item；正文 14.2 Cookie 段、14.4 未登录用例、14.5 401 脚本后、14.6 第 3 点、14.6.1 步骤 7、14.7 对照表、工作实战完成标准、错误 5、练习 6 答案、自测门槛 2、检查清单
原内容：（摘录）

集合「无凭证创建」无 `protocolProfileBehavior`。正文：「无凭证创建 | 无 Authorization | 401」；完成标准「导入并跑通仓库集合（空搜索允许红）」。

修复后内容：（摘录）

```json
"name": "无凭证创建",
"protocolProfileBehavior": {"disableCookies": true},
```

正文：无凭证 = 不要 Authorization **且**关掉 cookie jar。仓库该条已 `disableCookies`。Runner 可勾选 Run collection without using stored cookies；关掉 Disable cookie jar 又没勾该选项时，无凭证会因 Cookie 变成 201，不是集合坏了。

为什么这样修：R-AUTH 允许 Cookie 与 Bearer 并存。登录三条都会 `Set-Cookie`。GUI 默认 cookie jar 会污染 401 用例。请求级 `disableCookies` 不依赖学生记得勾 Runner 高级选项。
依据：Postman Docs *Disable cookie jar*；Collection Runner *Run collection without using stored cookies*；`postman-runtime` `protocolProfileBehavior.disableCookies`；PRD R-AUTH；`server.py` `_token()`；实服务无 Cookie → 401，仅 Cookie → 201。
是否影响其他章节：第 8/16 章「无凭证」口径同类（M-P1-09 / M-P1-35 由其他 Agent）。本章集合行为与 14 正文已对齐。练习 6 答案补了 Cookie 罐，避免与新口径打架（CH14-0008 其余 P2 未扩修）。
验证结果：`python3 -c json.loads` 通过；item 数仍 15；「无凭证创建」`disableCookies=true` 且无 Authorization。实服务：无 Cookie `POST /api/orders` → 401 `unauthorized`；带 `minishop_session` → 201 含 `id`。
状态：FIXED
