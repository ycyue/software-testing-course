# FIX RECORD
Audit ID：M-P1-13
原问题：`ch09-get-post` 图把 MiniShop 真路径 `/api/products` 配上英文 `keyword=mouse`。种子商品名是「无线鼠标」等，`mouse` 打仓库会 200 + 空 `items`，和图上「货架上有鼠标」相反。
修改文件：
- `chapters/assets/diagrams/ch09-get-post.html`
- `chapters/09a-network-http-semantics.md`（图下加一句解绑，未改教学 URL）
修改位置：
- 图 GET 卡 monospace 请求行
- 09A §9.8 配图后一句
原内容：（摘录）
```
GET /api/products?keyword=mouse
```
09A 教学示例仍为 `GET /products?keyword=mouse&page=2` + `Host: shop.example.test`（未冻结，本轮保留）。
修复后内容：（摘录）
```
GET /api/products?keyword=鼠标
```
图下新增：示意图路径是 MiniShop 的 `GET /api/products?keyword=鼠标`。09A 教学 URL `shop.example.test` 的 `keyword=mouse` 只是形状例子，对着仓库不要抄成 `/api/products?keyword=mouse`（种子商品名是中文，会得到空列表）。
为什么这样修：保留 `/api/products` 真路径，keyword 改成能命中「无线鼠标」的中文；09A `shop.example.test` 形状例子不动，避免两套 URL 焊死。本 Agent 只改第 9 章图/正文。
依据：CH09-0001；`server.py` `_get_products`（name/sku 小写包含）；种子 `无线鼠标` / `SKU-DEMO-001`；FIX_AGENT_BRIEF「仅第 9 章图/正文」。
是否影响其他章节：第 11 章 curl、第 14 章断言由 Fix-11 / Fix-14 处理（台账已记 ch11/ch14 FIXED）。第 7 章 URL 图仍用教学 query，不改。
验证结果：HTML 已无 `keyword=mouse`；09A 教学 `shop.example.test` / `keyword=mouse` 仍在 §9.5、§9.8、练习 4。PNG 与 HTML 尚未同步。
状态：FIXED（仅第 9 章）
需重截 PNG：是（`chapters/assets/diagrams/ch09-get-post.png`，Coordinator 统一 Chrome 截图）

---

第 14 章落点（Fix-14）见 `FIX_M-P1-13-ch14.md`：14.5 列表脚本改为命中 `SKU-DEMO-001`；`keyword=mouse` 空数组明确不是搜索成功。第 11 章见 `FIX_M-P1-13-ch11.md`。
