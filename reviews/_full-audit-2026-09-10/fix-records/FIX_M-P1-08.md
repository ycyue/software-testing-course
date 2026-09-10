# FIX RECORD
Audit ID：M-P1-08（CH07-0001；G07-0013 中与第 7 章开篇 URL 相关的部分）
原问题：第 7 章把教学用 `https://shop.example.test` 写成 MiniShop 网址/测试环境地址，并预设未登录就能看到商品首页。仓库 v1.0 本机是 `http://127.0.0.1:8765/`，第一帧是登录/注册页。
修改文件：`chapters/07-web-basics.md`
修改位置：「这一章解决什么问题」开篇；「场景导入」；7.2 流程起句；7.3 拆解示例导语；7.5「MiniShop 场景」
原内容：（摘录）
> 当你在浏览器里输入 MiniShop 的网址并看到商品首页时……
>
> 你在浏览器地址栏输入：
> `https://shop.example.test:8443/products?keyword=mouse&page=2#reviews`
>
> 测试环境地址：`https://shop.example.test`
修复后内容：（摘录）
> 仓库 MiniShop 本机地址是 `http://127.0.0.1:8765/`，未登录时第一帧是登录/注册页，不是商品首页。
>
> 下面这条是**教学 URL**……**不是**仓库地址：
> `https://shop.example.test:8443/products?keyword=mouse&page=2#reviews`
>
> 仓库 MiniShop 本机没有域名，登录页就是 `http://127.0.0.1:8765/`。……`https://shop.example.test` 是**教学 URL**……**不是**仓库测试环境地址。
为什么这样修：只把「example.test = MiniShop 本机」的口径拆开，保留教学拆 URL 的完整六段例子和 7.3 表格。零基础不会去敲 `.test` 当仓库站点，也不会把未登录第一帧当成商品首页。
依据：`project/minishop/docs/PRD.md`（本机 `http://127.0.0.1:8765`；页面为 `/` 与 `/admin.html`）；`project/minishop/frontend/index.html` 未登录第一帧含登录/注册；质量标准第五节「第 19 章之前的路径必须标明教学约定」；RFC 6761 `.test` 为保留 TLD，不宜当本机可解析地址。
是否影响其他章节：否。第 8 章已自行标明同类教学 URL。G07-0013 里「04 开篇补 PRD 能读/不能读盒子、LEARNING 插入理由」不在 M-P1-08 本章范围内，未改 `04a` / `LEARNING.md`。
验证结果：LOCAL REGRESSION——`shop.example.test` 六段拆解与 7.3 表仍在；7.5 不再把该 host 写成测试环境地址；7-1 工作实战仍指向 `http://127.0.0.1:8765/` 登录页；练习 1 的 `admin.example.test` 教学拆解未删。未改图、未整章重写。
状态：FIXED
