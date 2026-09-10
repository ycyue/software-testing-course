# FIX RECORD
Audit ID：M-P1-17
原问题：13.12（及 09B 可抄登录报文）纸面请求无 `Content-Length`；响应写成 `HTTP/1.1 200 OK` 且未说明实装差异。RFC 9112：无 `Content-Length` / `Transfer-Encoding` 则请求无 body。MiniShop `_read_json` 用 `Content-Length or 0` 读体，裸 TCP 按课文发送 → 400 `missing field`。curl 能过只因为自动加长度。实装 `BaseHTTPRequestHandler` 状态行是 `HTTP/1.0`，`Content-Type` 带 `charset=utf-8`，Body 有 `role`。
修改文件：
- `chapters/13-api-testing.md`（13.12）
- `chapters/09b-http-message-observe.md`（9.13 可抄登录报文；与本 ID「13 + 09b」对齐）
修改位置：13.12 请求/响应 `text` 围栏及紧随说明；09B 9.13 同构说明
原内容：（摘录）
```
POST /api/login HTTP/1.1
Host: 127.0.0.1:8765
Content-Type: application/json

{"phone":"13800138000","password":"Test1234"}
```
响应：`HTTP/1.1 200 OK` + `Content-Type: application/json`，无实装注记。
修复后内容：（摘录）
```
POST /api/login HTTP/1.1
Host: 127.0.0.1:8765
Content-Type: application/json
Content-Length: 45

{"phone":"13800138000","password":"Test1234"}
```
说明：`curl -d` 会自动加 `Content-Length`；裸 TCP 必须自己写。响应仍按 HTTP/1.1 语义纸面书写，并注明 MiniShop 实装 `HTTP/1.0 200 OK`、可能有 `charset=utf-8` 与 `role`；不要把 `HTTP/1.0` 当成缺陷。09B 密码为占位符，故纸面写 `Content-Length: <Body 字节数>`，并标明教学密码 `Test1234` 时为 45。
为什么这样修：可抄报文必须能按 RFC 成帧发出；curl 捷径不能冒充完整形状。HTTP/1.0 是 Python 教学服务器默认，不是产品缺陷。
依据：RFC 9112 §6（请求体由 Content-Length 或 Transfer-Encoding 标明）；RFC 9110 §8.6（有语义的 POST 用户代理 SHOULD 发送 Content-Length）；`server.py` `_read_json` / `_json`；`evidence/linux/curl-login-headers.txt` 首行 `HTTP/1.0 200 OK`。
是否影响其他章节：09B 可抄登录与 13.12 对齐。第 9 章 Host / 非法 CL 的 RFC MUST（M-P2-02 / M-P2-03）不在本 ID 范围。
验证结果：教学 Body `{"phone":"13800138000","password":"Test1234"}` UTF-8 长度确为 45。13.12 请求围栏含 `Content-Length: 45`；curl 自动加 / 裸 TCP 必须写已写明；响应注记 HTTP/1.0、charset、role，并明确不要为版本号开缺陷。未把 HTTP/1.0 改成缺陷表述。
状态：FIXED
