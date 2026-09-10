# FIX RECORD
Audit ID：M-P1-16
原问题：`ch13-four-shapes` 自称 MiniShop 购物车 Body，但第 2～4 格只有 `{"qty":null}` / `{"qty":""}` / `{"qty":"1"}`。`server.py` `_cart_items` 先查 `"sku" not in data` → 400 `missing sku`，到不了图上的 `null qty` / `wrong type qty`。13.8 表每行都有 sku，图会把缺 sku 画成 null 校验。
修改文件：
- `chapters/assets/diagrams/ch13-four-shapes.html`
- `chapters/assets/diagrams/ch13-four-shapes.png`
修改位置：13.8 四态图四格 Body 与 caption
原内容：（摘录）
```
{"sku":"SKU-DEMO-001"}  → 400 missing qty
{"qty":null}            → 400 null qty
{"qty":""}              → 400 wrong type qty
{"qty":"1"}             → 400 wrong type qty
```
修复后内容：（摘录）
```
{"sku":"SKU-DEMO-001"}              → 400 missing qty
{"sku":"SKU-DEMO-001","qty":null}   → 400 null qty
{"sku":"SKU-DEMO-001","qty":""}     → 400 wrong type qty
{"sku":"SKU-DEMO-001","qty":"1"}    → 400 wrong type qty
```
caption 补：一次只破坏 qty。缺 sku 会先变成 missing sku，不要画成 null qty。
为什么这样修：oracle 必须跟 `_cart_items` 校验顺序和 13.8 表同一组 Body。只破坏 qty、四格都带 `SKU-DEMO-001`，才测到 null / 空串 / 错误类型，而不是缺 sku。
依据：`project/minishop/server.py` `_cart_items`（先 missing sku，再 missing qty / null qty / wrong type qty）；13.8 表；实操 13-1 `CASES`。
是否影响其他章节：否。13.8 表、13-1、OpenAPI 本就带 sku。第 15 章四态图讲的是 Python `get("qty")`，不是 MiniShop 购物车契约，未改。
验证结果：HTML 四格 JSON 与 13.8 表逐字节相同；裸 `{"qty":null}` 等已不存在。PNG 已按 `chapters/assets/diagrams/README.md` 用 Chrome headless `--window-size=1320,780` 重截（1320×780），目视四格均含 sku 且 error 为 missing qty / null qty / wrong type qty / wrong type qty。需重截 PNG：已重截；Coordinator 统一重跑同一命令可覆盖。
状态：FIXED
