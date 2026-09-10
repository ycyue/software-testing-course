# FIX RECORD
Audit ID：M-P2-03
原问题：09B 把 `Content-Length` 写成「与实际 Body 不一致时可能被拒绝」，把非法 CL、字节不够、漏写揉成运气问题。非法 CL 在 HTTP/1.1 是 MUST 400 并关连接。
修改文件：`chapters/09b-http-message-observe.md`
修改位置：§9.11 请求头表 `Content-Length` 行；表下补三句拆分
原内容：（摘录）
```
| `Content-Length` | Body 长度 | 与实际 Body 不一致时可能被拒绝 |
```
修复后内容：（摘录）
表行：`Content-Length` | Body 的八位组长度，用来成帧 | 非法值：HTTP/1.1 必须 400 并关连接。漏写与非法分开；curl 会自动加
表下：头本身非法（不是同一个非负整数，或两个不同值）时，HTTP/1.1 接收方必须当不可恢复错误：请求则 400 并关闭连接（RFC 9112）。长度合法但字节没收齐，必须当不完整消息并断开。POST 有体时应带这个头；curl 会自动加，按第 13 章纸面形状手敲 TCP 不会。MiniShop 读的是 `Content-Length`，写成 0 或省略就等于没有 JSON 体。
为什么这样修：非法 CL 是成帧错误（MUST），漏写是另一条（curl 会代写；MiniShop 当 0 字节）。与 M-P1-17（第 13 章纸面漏写 CL）分开，不并进那条。
依据：RFC 9112 §6.3；RFC 9110 §8.6、§15.5.12；`server.py` `_read_json`：`int(self.headers.get("Content-Length") or 0)`；RT02-0002。
是否影响其他章节：点到第 13 章手写 TCP 不会自动加 CL，正文仍由 Fix-13 处理 M-P1-17。
验证结果：09B 已无「可能被拒绝」；非法 / 漏写 / curl 自动加 三句分开。未改 MiniShop 读 CL 的实现。
状态：FIXED
