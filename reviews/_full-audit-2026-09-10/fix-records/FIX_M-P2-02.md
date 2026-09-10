# FIX RECORD
Audit ID：M-P2-02
原问题：09A 只把 Host 写成「HTTP/1.1 必须的请求头 / 对应 URL 里的 host」，没教客户端 MUST 发、值含非默认端口、源服务器对缺/多/非法 Host MUST 400。MiniShop 实装 HTTP/1.0，缺 Host 的实测不能当 RFC 结论。
修改文件：
- `chapters/09a-network-http-semantics.md`（§9.5 Host 段；参考资料补 RFC 9112）
- `chapters/09b-http-message-observe.md`（§9.11 Host 行 + 表下交叉引用，避免 09B 表仍写成「目标主机」）
修改位置：09A §9.5 教学请求示例后的 Host 段；09B 请求头表 `Host` 行
原内容：（摘录）
```
`Host` 在 HTTP/1.1 中是必须的请求头，用来说明要访问哪一个主机。它和 URL 里的 host 对应，但出现在报文头里。
```
09B 原表：`Host` | HTTP/1.1 的目标主机 | 是否打到正确环境
修复后内容：（摘录）
```
`Host` 是 HTTP/1.1 的强制请求头。值等于目标 URI 的 authority：主机名，外加非默认端口。上面教学例子默认 80，可以只写 `shop.example.test`；MiniShop 本机是 `Host: 127.0.0.1:8765`，端口必须写上。RFC 9112 规定：HTTP/1.1 客户端必须发送 Host；源服务器对缺 Host、多个 Host、或值非法的请求必须回 400。HTTP/2、HTTP/3 里这个信息常在 `:authority`。MiniShop v1.0 跑在 HTTP/1.0 上，缺 Host 的实测不能写成「已符合 RFC」。
```
为什么这样修：补上 RFC 9112 服务端 MUST 400 与 authority 含端口，同时把 MiniShop HTTP/1.0 实测和规范结论拆开。不降「要带 Host」。
依据：RFC 9112 Host 段（HTTP/1.1 客户端 MUST 发 Host；缺/多/非法 Host 源服务器 MUST 400）；RFC 9110 §7.2 `Host = uri-host [ ":" port ]`；RT02-0001。
是否影响其他章节：09B 请求头表同步一句，避免上下节口径分叉。未改 MiniShop 实现。
验证结果：09A 教学 URL `shop.example.test` 保留；Host 段含 MUST 400、非默认端口、HTTP/1.0 免责。未把缺 Host 的本机实测写成规范。
状态：FIXED
