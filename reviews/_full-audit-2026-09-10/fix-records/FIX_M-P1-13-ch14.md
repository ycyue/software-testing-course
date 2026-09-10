# FIX RECORD
Audit ID：M-P1-13（第 14 章落点；对应 CH14-0005 / G03-0002。09a 见图 FIX_M-P1-13.md，11 见 FIX_M-P1-13-ch11.md）
原问题：`keyword=mouse` 打 `/api/products` 得到空数组 `{"items":[]}`。第 14 章 14.5 列表脚本只断言 `items` 为数组，空数组也会绿，被当成搜索成功；与仓库集合「搜索商品」（`keyword=鼠标` + `items[0].sku === SKU-DEMO-001`）不对齐。
修改文件：`chapters/14-postman.md`
修改位置：14.2 搜索面板说明；14.5 列表脚本
原内容：（摘录）

```javascript
pm.test("列表接口返回 JSON 数组结构", function () {
  pm.expect(pm.response.code).to.eql(200);
  const body = pm.response.json();
  pm.expect(body).to.have.property("items");
  pm.expect(body.items).to.be.an("array");
});
```

修复后内容：（摘录）

14.2：仓库「搜索商品」用 `keyword=鼠标` 并断言命中 `SKU-DEMO-001`。搜 `mouse` 得到空数组——这不是搜索成功，也不要和 BUG-001 混为一谈。

```javascript
pm.test("列表命中无线鼠标", function () {
  pm.expect(pm.response.code).to.eql(200);
  const items = pm.response.json().items;
  pm.expect(items).to.be.an("array");
  pm.expect(items[0].sku).to.eql("SKU-DEMO-001");
});
```

为什么这样修：种子商品名是「无线鼠标」，不含英文字母 `mouse`。只断言数组会把空列表标绿。正文示例必须与仓库集合同一 oracle（命中 sku），并把 `mouse` 明确写成反例。
依据：`server.py` `_get_products` 按 name/sku 包含匹配；实服务 `keyword=鼠标` → `SKU-DEMO-001`，`keyword=mouse` → `{"items":[]}`；集合「搜索商品」已断言 sku；CH14-0005 / G03-0002。
是否影响其他章节：09a 图、11.13 curl 由 Fix-09、Fix-11 另记。第 14 章不再把空数组当搜索成功。
验证结果：临时 MiniShop 复现 `keyword=鼠标` 200 命中 `SKU-DEMO-001`；`keyword=mouse` 200 `{"items":[]}`。集合 JSON `json.loads` 通过，搜索 URL 仍为 `keyword=鼠标`。正文已无「只断言数组即成功」的正式脚本。
状态：FIXED（仅 ch14）
