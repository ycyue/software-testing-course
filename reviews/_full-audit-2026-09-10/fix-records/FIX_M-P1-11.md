# FIX RECORD
Audit ID：M-P1-11（对应 CH08-0003 / G05 对 04 图 REPLACE）
原问题：`04-search-empty-bug001.png` 几乎等于登录后商品目录 `03-shop.png`，不能证明提交了空/空白关键字。08A 工作实战第 3 条把它当 BUG-001 证据。
修改文件：
- `chapters/08a-web-page-testing.md`（工作实战第 3 条）
- `chapters/10-chrome-devtools.md`（步骤 6 caption）
- `chapters/19-minishop-project.md`（19.5 caption；本章已有 HTTP 指向，补「不要伪造 DevTools 面板图」）
修改位置：08A MiniShop 工作实战（上）第 3 条；第 10 章逐步操作 6；第 19 章 19.5 截图注。
原内容：（摘录）
> 3. 空白搜索仍列出三件商品（BUG-001）；
> ![空白搜索仍返回三件商品](assets/04-search-empty-bug001.png)
> ![空搜索 BUG-001](assets/04-search-empty-bug001.png)
修复后内容：（摘录）
> **不要**把 `04-search-empty-bug001.png` 当空搜索证据：它几乎等于登录后的商品目录页……请对 `project/minishop/evidence/http/03-products-empty-keyword.txt`（`keyword=%20%20%20`，200，三件）。不要伪造 DevTools 面板图。
为什么这样修：登录后默认 `refreshProducts()` 不带 keyword 也是三件。BUG-001 的观察是「请求带了空/空白 keyword 仍全量」。截图看不出空格，也不能看 URL/Network。按任务不伪造 DevTools 面板图，改指已有 HTTP 证据。
依据：`evidence/http/03-products-empty-keyword.txt`；本机 `GET /api/products?keyword=%20%20%20` → 200，三件；G05 像素 diff 仅搜索框边框。
是否影响其他章节：第 6 章 `06a` 仍引用该 PNG 为线索图，不在本 ID 文件列表。示意图 `ch08-search.html` 仍写该截图（CH08-0015，本轮不修）。
验证结果：08A/10/19 均声明该图 ≠ 空搜索证据，并指向 `03-products-empty-keyword.txt`。未新增伪造面板图。
状态：FIXED

---

# FIX RECORD（续 · 第 19 章项目包）
Audit ID：M-P1-11（第 19 章收口与项目证据，配合 Fix-08）
原问题：第 19 章把 `04-search-empty-bug001.png` 当开放缺陷展示证据；`BUG-001.md` / 覆盖矩阵也把该 PNG 写成「空格提交后共 3 件」。
修改文件：`chapters/19-minishop-project.md`；`project/minishop/bugs/BUG-001.md`；`docs/prd-coverage-matrix.md`；`docs/test-cases.md`
修改位置：19.5 alt 与图下说明；19.9；可运行性说明；缺陷单证据节；矩阵 / TC-SEARCH-001 证据列
原内容：（摘录）

```
![空搜索 BUG-001](assets/04-search-empty-bug001.png)
截图：搜索框为空格提交后页面「共 3 件」
矩阵证据：03-products-empty-keyword.txt、04-search-empty-bug001.png
```

修复后内容：（摘录）

```
![空搜索截图看起来像商品目录，不能当 BUG-001 页面证据](...)
04 图与默认目录几乎一样……请看 HTTP 03-products-empty-keyword.txt（keyword=%20%20%20 → 200，三件）
BUG-001 主证据是该 HTTP；PNG 不能单独当「已提交空白关键字」的页面证据
```

为什么这样修：任务要求第 19 章空搜索截图不能当 BUG-001 页面证据，指向 HTTP。PNG 未替换（Coordinator 统一截图）；过渡期改挂 HTTP。
依据：CH08-0003；CH19-0007；G05 `04-search-empty`；`evidence/http/03-products-empty-keyword.txt`。
是否影响其他章节：08A/10 已由 Fix-08 改指 HTTP。未伪造 DevTools 面板图。
验证结果：第 19 章 19.5/19.9 与 BUG-001 均以 HTTP 为主证据。
状态：FIXED
