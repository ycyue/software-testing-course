# FIX RECORD
Audit ID：M-P2-09
原问题：09B §9.10「必须能解释的常用码」把 405/415 与 MiniShop 主路径码并列，OpenAPI 与 `server.py` 全路径不返回这两码。学生会把 `GET /api/login` 的 404 写成方法不允许缺陷。
修改文件：`chapters/09b-http-message-observe.md`
修改位置：§9.10 状态码表 405/415 行及表后一句；§9.13 登录失败观察表 405/415 行（同一口径，避免表领去仓库找码）
原内容：（摘录）
```
| 405 | Method Not Allowed | 路径存在但不接受该方法，响应或含 `Allow` |
| 415 | Unsupported Media Type | `Content-Type` 不被接受 |
```
失败表：`405` 方法不被该路径接受；`415` Content-Type 不匹配
修复后内容：（摘录）
```
| 405 | Method Not Allowed | 路径存在但不接受该方法。口试讲语义；MiniShop v1.0 OpenAPI/实现未必返回，不要写成项目必测码 |
| 415 | Unsupported Media Type | `Content-Type` 不被接受。口试讲语义；MiniShop v1.0 OpenAPI/实现未必返回，不要写成项目必测码 |
```
表后：405 和 415 是通用 HTTP 语义，面试要能解释。MiniShop v1.0 的 OpenAPI 和实现没有这两码：错方法常见 404，不认的 `Content-Type` 仍按 JSON 解析或回 400。不要把它们写进本项目必测用例。
为什么这样修：保留口试语义，切断「项目必测」。未改 OpenAPI（RT04-0008 建议的契约句不在本 Agent 范围；第 9 章落点已够用）。
依据：`server.py` `do_GET`/`do_POST` 未匹配 → 404；`_read_json` 不看 `Content-Type`；OpenAPI 无 405/415；RFC 9110 §15.5.6 / §15.5.16 仍是口试语义；RT04-0008。
是否影响其他章节：未改 `openapi.json`。检查清单仍是 200/302/304/401/403/404/500，未把 405/415 加进必过门槛。
验证结果：状态码表与失败观察表均标明 MiniShop v1.0 未必返回；语义行仍在，可供口试。
状态：FIXED
