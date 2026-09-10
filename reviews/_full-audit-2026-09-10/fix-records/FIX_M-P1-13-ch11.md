# FIX RECORD
Audit ID：M-P1-13（第 11 章落点；对应 CH11-0001 / G03-0002）
原问题：11.13「最小读取」可复制 curl 使用 `GET /api/products?keyword=mouse`。MiniShop 搜索是 `keyword.lower() in name/sku`，种子商品名为「无线鼠标」、SKU 为 `SKU-DEMO-001`，都不含英文 `mouse`。学生抄命令得到 HTTP 200 且 `{"items":[]}`，易误报搜索坏了或服务没数据，并与 BUG-001（空白 keyword 仍返回全量）搅在一起。
修改文件：`chapters/11-linux.md`
修改位置：11.13 `curl` 接口测试，「最小读取」说明与可复制命令（原约 L430–L433）
原内容：（摘录）

```
最小读取。MiniShop v1.0 是 `http://127.0.0.1:8765/api/products`，不要打无前缀的 `/products`。

```bash
curl -sS -D - -o ./minishop-curl-body.txt "http://127.0.0.1:8765/api/products?keyword=mouse"
```
```

修复后内容：（摘录）

```
最小读取。MiniShop v1.0 是 `http://127.0.0.1:8765/api/products`，不要打无前缀的 `/products`。无 query 预期 HTTP 200、`items` 3 件（含 `SKU-DEMO-001` 无线鼠标）。过滤可用 `?keyword=SKU-DEMO-001`，或已编码的 `?keyword=%E9%BC%A0%E6%A0%87`（「鼠标」）。不要用 `keyword=mouse`：英文不在中文商品名或 SKU 里，会得到空列表 `{"items":[]}`。

```bash
curl -sS -D - -o ./minishop-curl-body.txt "http://127.0.0.1:8765/api/products"
```
```

为什么这样修：可复制命令改为无 query 的最小读取，预期与种子目录一致（3 件）。过滤给两条能命中的写法：ASCII 的 SKU，以及 URL 编码后的「鼠标」（本机把裸中文放进 curl 请求行会被 MiniShop 的 BaseHTTP 打成 400 Bad request syntax，故不把未编码的 `keyword=鼠标` 写进可复制命令）。明确禁止 `keyword=mouse`，避免空列表被当成故障。只改 11.13 这一落点，未整章重写。
依据：本机 2026-09-10 对 `http://127.0.0.1:8765` 实测——无 query → 200、`items` 3 件；`keyword=mouse` → 200 `{"items":[]}`；`keyword=SKU-DEMO-001` 与 `keyword=%E9%BC%A0%E6%A0%87` → 命中 `SKU-DEMO-001`；裸 `keyword=鼠标` → 400。`project/minishop/server.py` `_get_products` / `seed()`；PRD 教学数据；OpenAPI `GET /api/products`；FIX_PLAN M-P1-13；CHAPTER_11_AUDIT CH11-0001。
是否影响其他章节：本记录只修第 11 章。M-P1-13 在 09a 图、14 断言的落点由 Fix-09 / Fix-14 处理，不在本文件范围。章内 11.13 其余 curl（登录 POST、纪律、工作实战）未改。
验证结果：临时库启动 MiniShop 后执行修复后命令：`HTTP/1.0 200 OK`，Body 为 3 件（`SKU-DEMO-001` 无线鼠标 / `SKU-DEMO-002` 键盘 / `SKU-DEMO-003` 耳机）。`keyword=mouse` 仍空列表，正文已声明不要用。LOCAL REGRESSION：11.13 前后文、路径 `/api/products`、端口 8765、登录 curl、GET/POST 语义句均未改坏；`chapters/11-linux.md` 已无 `keyword=mouse` 作为可复制请求。
状态：FIXED（仅 ch11）
