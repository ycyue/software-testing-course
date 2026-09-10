# FIX RECORD
Audit ID：M-P1-10（对应 CH08-0002）
原问题：8.14 类型表把无凭证访问 `GET /api/orders`（无 `{id}`）写成 401。该路径没有集合 GET，实测 **404** `{"error":"not found"}`。
修改文件：`chapters/08b-web-auth-permission.md`
修改位置：8.14「未认证」行 MiniShop 例子
原内容：（摘录）
> 无 Bearer 访问 `/api/cart` 或 `/api/orders` → 401
修复后内容：（摘录）
> 无 Bearer **且** 无 Cookie `minishop_session` 访问 `GET /api/cart`、`GET /api/orders/{id}` 或 `POST /api/orders` → 401。没有 `GET /api/orders` 列表接口，打它是 **404**，不是 401。
为什么这样修：学生按表格字面打 `GET /api/orders` 会得到 404，误以为 MiniShop 坏了或教材写错。401 只出现在受保护且存在的接口上。
依据：`server.py` `do_GET`：仅 `/api/orders/` 前缀进 `_get_order`，其余 `/api/` → 404。本机 `GET /api/orders` → 404。OpenAPI 无该集合 GET。
是否影响其他章节：与 M-P1-09 同一单元格；8.14「不要把 404 写成他人订单的可接受结果」未改（那是另一条存在性口径）。
验证结果：表内路径与实测 401/404 对齐。
状态：FIXED
