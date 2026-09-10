# Chapter 08 Audit

审计员：Chapter-Audit-Agent-08  
日期：2026-09-10  
范围：第 8 章全部（索引 + 08A 页面表单 + 08B 登录态权限 + 实操 8-1 + 阶段测验 3 中的第 8 章题 + 本章示意图/引用截图）。禁止扩审其他章正文。  
核心章，评分从严。先前 `reviews/` 只作线索，结论均为本轮独立复核。

## 1. Coverage

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 索引页 | 1（`08-web-functional-testing.md`，14 行） | 1 | 0 |
| 上/下册正文 | 2 | 2 | 0 |
| 小节/标题（索引 1 + 08A 43 + 08B 47 + 8-1 README 4） | 95 | 95 | 0 |
| 正文段落块（索引 6 + 08A 72 + 08B 92） | 170 | 170 | 0 |
| 表格块（08A 8 + 08B 5 内容表 + 4 模板表 + 8-1 1） | 18 | 18 | 0 |
| 代码块（08A HTML + 教学 URL；08B mermaid / Bearer / 路径 / 测试包模板；8-1 bash） | 7 | 7 | 0 |
| Python 实操代码 | 2（`main.py`、`tests/test_lab.py`） | 2 | 0 |
| Linux/Shell 命令 | 1（`python3 practice/run.py 8-1` 及 `--check`） | 1 | 0 |
| SQL | 0 | 0 | 0 |
| HTTP 示例（教学 URL、Bearer 头、8.14 路径、8-1 五格、登录态描述） | 12 | 12 | 0 |
| 测试用例/步骤（8.13 表、8.14 步骤、08A 工作实战 4 条、08B 测试包要求、8-1 矩阵） | 21 | 21 | 0 |
| Bug 示例（BUG-001、8.17 标题、练习 5/10 缺陷标题、qty=11） | 5 | 5 | 0 |
| 章内练习题 | 10（08A：2/3/4/5/10；08B：1/6/7/8/9） | 10 | 0 |
| 章内标准答案 | 10 | 10 | 0 |
| 阶段测验 3 中第 8 章题 | 6（题 1、2、3、5、9、10） | 6 | 0 |
| 示意图 PNG | 5 | 5 | 0 |
| 示意图 HTML | 5 | 5 | 0 |
| 正文引用截图 PNG | 4（01/02/04/05） | 4 | 0 |
| 对照打开的相邻截图 | 3（03-shop、06-register、07-admin；非正文引用，用于口径） | 3 | 0 |
| 练习页 HTML | 1（`07-html-lab.html`） | 1 | 0 |
| Markdown 链接 | 24（索引 7 + 08A 10 + 08B 5 + 8-1 2） | 24 | 0 |
| MiniShop 权限口径文件 | `PRD.md` R-AUTH/R-PERM、`openapi.json`、`server.py`、`frontend/{index,admin,app}.js`、`evidence/http/01-login-ok.txt` | 全部 | 0 |
| 旧审查线索 | `chapter-08-review.md`、`_pedagogy-2026-09-10/ch08.md`、rereview stage-3 | 已读、未照抄 | 0 |

**Coverage：100%。未检查 = 0。**

未把第 9/10 章正文、测验 3 的题 4/6/7/8（HTTP/DevTools）当作本章缺陷来源。

## 2. 总评分

| 项目 | 得分 |
| --- | ---: |
| 技术准确性 | 7/10 |
| 岗位实用性 | 8/10 |
| 完整性 | 7/10 |
| 初学者友好度 | 7/10 |
| 教学顺序 | 7/10 |
| 代码质量 | 9/10 |
| 实操质量 | 7/10 |
| 练习质量 | 7/10 |
| 图片质量 | 7/10 |
| 九项合计 | 66/90 |
| **总体（折合）** | **73/100** |

折合：66/90×100＝73。核心章目标 95、发布线 90，均未达到。分层理论和 403 主路径是对的；扣分集中在 MiniShop 映射（Cookie 回退 vs「不带 Bearer→401」、集合路径 404、空搜索截图、练习 10 判定）、08A 上册无产出、以及 8-1 只钉两道门。

**20 项 Definition of Done（本轮独立）**

| # | 项 | 结果 |
| --- | --- | --- |
| 1 | 目标明确 | 通过 |
| 2 | 前置知识正确 | 通过（学习顺序 06→08，前置写了 07+06） |
| 3 | 无知识性错误 | **失败**（CH08-0001/0002/0004） |
| 4 | 重要信息未过时 | 通过（SameSite 默认 Lax、None 必须 Secure 与 2026 MDN 一致） |
| 5 | 无错误绝对化 | 通过（明确否定三选一、否定 POST 更安全） |
| 6 | 术语准确 | 通过（HttpOnly/Bearer/Session vs sessionStorage） |
| 7 | 零基础能理解 | 有条件（蛋糕图/三道门清楚；08A 练习从 2 起、上册无闭环） |
| 8 | 示例具体 | 通过 |
| 9 | 有实际工作场景 | 通过 |
| 10 | MiniShop 一致 | **失败**（CH08-0001/0002/0003/0007/0008） |
| 11 | 代码经过验证 | 通过（8-1 本机 0 退出；HTML 可解析） |
| 12 | SQL 操作安全 | 不适用，满足 |
| 13 | 图表帮助理解 | 有条件（分层图/权限图有教学价值；浏览器图写死 400；04 截图不能当 BUG-001 证据） |
| 14 | 知识重要级别明确 | 通过（上传/下载/兼容/响应式 ⭐⭐ 诚实） |
| 15 | 常见错误有价值 | 通过 |
| 16 | 面试题非死记硬背 | 通过（结构对；示例提前用 DevTools，见 CH08-0013） |
| 17 | 练习覆盖目标 | **失败**（一句话核心的分层半边与 401 未纳入 8-1 验收） |
| 18 | 答案与练习对应 | 有条件（练习 10 预期不够可观察） |
| 19 | 检查清单可验证 | 通过 |
| 20 | 衔接下一章 | 通过（09A；状态码精确阅读有意识推迟） |

约 **16/20**，低于「18～19 修正后发布」线。

## 3. P0

无。没有把 Cookie/Session/Token 写成三种可互换产品；没有教 GET 不安全/POST 安全；没有把 `/login` 当可抄 MiniShop 页面；没有把验证码写进 MiniShop 必测；没有把 404 写成他人订单的可接受结果；安全实验限制在授权环境。

## 4. P1

## ISSUE
ID：CH08-0001
文件：`chapters/08b-web-auth-permission.md`；`chapters/assets/diagrams/ch08-privilege.html` / `.png`；`practice/08-privilege/README.md`
章节：第 8 章（下）
小节：8.14 权限测试；三道门示意图；实操 8-1
精确位置：08b L174「无 Bearer 访问…→ 401」；L181「没带有效登录凭证 → **401**」；权限图第一盒「不带 Bearer 访问 GET /api/orders/{id}」
原文：没带有效登录凭证 → **401**。……不带 Bearer 访问 GET /api/orders/{id}。
问题等级：P1
问题类别：HTTP / ACC / TEST
问题说明：正文把「不带 Bearer」直接等同于「未认证 401」。MiniShop `server.py` `_token()` **先读 Bearer，再回退 Cookie `minishop_session=`**。本轮实测：只带 Cookie、不带 `Authorization` 时，`GET /api/orders/{id}` 返回 **200**；两者都不带才是 401。前端 `fetch` 默认 same-origin 会自动带 Cookie（`app.js` 同时还从 `sessionStorage` 加 Bearer）。本章是 **Web 功能测试**，学生在已登录浏览器里「去掉 Authorization 再访问」看不到 401。
为什么有问题：会把学生教错未认证怎么测；也把「Cookie / Token 不是两种登录产品」的现场证据浪费掉——它们是同一份会话标识的两层携带方式。
依据：本机 MiniShopLab 实测；`server.py` L190–199；`app.js` L5–8、L37–47；PRD `R-AUTH`「后续接口以 Bearer 为准，Cookie 可并存」；MDN：HttpOnly Cookie 仍随符合条件的请求发送。
建议修改：401 的操作写成「既不带 `Authorization` 也不带会话 Cookie」（curl/8-1 脚本）；并加一句：浏览器登录后只删 Bearer、Cookie 仍在，MiniShop **仍会认人**。这正是分层，不是「Bearer 才是登录」。
推荐替换文本：

```
未认证 401（MiniShop 门牌）：请求里既没有有效 Bearer，也没有有效会话 Cookie。
在已登录的浏览器里只去掉 Authorization 不够——Cookie 还在。
用实操脚本或 curl 两条对比：
- 不带任何凭证 → 401
- 只带 Cookie / 只带 Bearer → 都能认出你（当前实现；冻结仪式在第 19 章）
```

## ISSUE
ID：CH08-0002
文件：`chapters/08b-web-auth-permission.md`
章节：第 8 章（下）
小节：8.14 类型表「未认证」行
精确位置：L174
原文：无 Bearer 访问 `/api/cart` 或 `/api/orders` → 401
问题等级：P1
问题类别：HTTP / ACC
问题说明：`GET /api/cart` 无凭证确为 401。`GET /api/orders`（无 `{id}`）本轮实测为 **404** `{"error":"not found"}`，OpenAPI 也没有该集合 GET。`POST /api/orders` 与 `GET /api/orders/{id}` 无凭证才是 401。
为什么有问题：学生按表格字面打 `GET /api/orders` 会得到 404，以为 MiniShop 坏了或教材写错。
依据：`server.py` `do_GET`：`/api/orders/` 前缀才进 `_get_order`，否则 `/api/` → 404；本机实测。
建议修改：改成 `GET /api/cart` 或 `GET /api/orders/{id}` 或 `POST /api/orders`。
推荐替换文本：无有效登录凭证访问 `GET /api/cart`、`GET /api/orders/{id}` 或 `POST /api/orders` → 401（注意：没有 `GET /api/orders` 列表接口，打它是 404）。

## ISSUE
ID：CH08-0003
文件：`chapters/08a-web-page-testing.md`；`chapters/assets/04-search-empty-bug001.png`
章节：第 8 章（上）
小节：MiniShop 工作实战（上）第 3 条；8.6
精确位置：08a L314–318
原文：空白搜索仍列出三件商品（BUG-001）
问题等级：P1
问题类别：IMG / TEST
问题说明：工作实战把 `04-search-empty-bug001.png` 当作空白搜索证据。该图关键字框看起来是空的，「共 3 件」、三件商品、购物车 `qty=1`——与登录后默认商品页 `03-shop.png` 肉眼不可分（两图均为 1280×900，仅差 12 字节）。登录成功后 `app.js` `refreshProducts()` **不带 keyword** 也会列出三件，那不是 BUG-001。BUG-001 要的是 `GET /api/products?keyword=` 或仅空白；空格在截图里看不见。
为什么有问题：学生会把「打开店铺看到三件商品」判成缺陷，或者以为已经观察到 BUG-001。
依据：`app.js` L55–56、L65–73；`server.py` L262–272；`bugs/BUG-001.md` 步骤写的是 `?keyword=` / 空格；本轮打开 03 与 04 对照。
建议修改：换一张能证明「发生了搜索」的图：关键字框可见空格，或同屏 Network/`共 3 件` 且地址带 `keyword=`；正文写明默认列表 ≠ 空搜索。
推荐替换文本：对照 04 图之前先写：登录后默认列出三件 **不是** BUG-001。只有提交空/空白关键字（请求带 `keyword=` 或全空格）仍返回三件才是。若截图看不出空格，改用 `evidence/http/03-products-empty-keyword.txt`。

## ISSUE
ID：CH08-0004
文件：`chapters/08a-web-page-testing.md`
章节：第 8 章（上）
小节：练习 10 及答案
精确位置：L383–385、L398
原文：预期：提交失败，数量保持合法值，出现超限或库存不足提示。
问题等级：P1
问题类别：ANS / TEST
问题说明：同一章工作实战第 4 条已经写对：列表保持 `qty=1`，**不是**「变成 10」。`05-cart-qty-11.png` 里输入框仍是 **11**，列表才是 `qty=1`，提示 `qty exceeds stock`。答案「数量保持合法值」没说清是列表还是输入框。学生若把「输入框回到 1」当预期，会给 MiniShop 误报缺陷。
为什么有问题：核心章用例的判定必须可观察、不歧义。第 5 章已经强调「我打不进去」≠「提交被拒绝」；这里答案自己又混了。
依据：`05-cart-qty-11.png`；`app.js` L83–95（失败只改 `cart-msg` 并 `refreshCart`，不把 input 改回）；08a L170、L319。
建议修改：预期拆成三格：提示文案、列表 qty、输入框是否仍显示 11。
推荐替换文本：预期：提交失败；页面提示 `qty exceeds stock`（或等价）；**商品列表**该 SKU 仍为提交前的合法值（本图 `qty=1`）；输入框可以仍显示 11，不要把「框里还是 11」当成失败。v1.0 不要写小计。

## ISSUE
ID：CH08-0005
文件：`chapters/08a-web-page-testing.md`；`chapters/08-web-functional-testing.md`
章节：第 8 章（上）/ 索引
小节：MiniShop 工作实战（上）
精确位置：08a L312–321；索引 L10「08A 对照截图」
原文：对照四张截图：1. label 和 type=password … 完整 Web 测试包模板见 08B。
问题等级：P1
问题类别：PED / EX
问题说明：质量标准要求拆章后上册能独立完成一个小闭环；书面实操要有产出路径。08A 工作实战是「看图打勾」，没有 `exercises/` 路径，也不要求打开 `07-html-lab.html` 做一次空提交。索引把 08A 作业定义成对照截图。08A 一句话核心是「在浏览器这条观察通道上执行判定」，作业却不让学生自己执行一次判定。
为什么有问题：上册读完没有可复核产出；和第 5、6 章已经会写的用例/缺陷单脱节。
依据：`standards/QUALITY_STANDARD_v1.0.md` 第七节；教学尺「上册闭环」。
建议修改：先打开 lab 页空提交，把「浏览器拦住了」写入 `exercises/chapter-08a-page-check.md`，再对照四张截图。
推荐替换文本：

```
先打开 assets/07-html-lab.html，手机号留空点登录。
把「浏览器拦住了」写成观察，不要写成服务端拒绝。本页不连 MiniShop。
把 4 条截图对照写入 exercises/chapter-08a-page-check.md。
现在不要绕过页面打接口（08B / 第 9 章）。
```

## 5. P2

## ISSUE
ID：CH08-0006
文件：`practice/08-privilege/README.md`；`practice/08-privilege/main.py`；`practice/08-privilege/tests/test_lab.py`；`chapters/08b-web-auth-permission.md`
章节：第 8 章（下）
小节：8.14；实操 8-1
精确位置：08b L185；README L19；`test_lab.py` 只断言 403/200/403/200
原文：实操 8-1 把两格 403 跑出来；未认证 401 可以自己对 `/api/orders/{id}` 不带 Bearer 看一眼。
问题等级：P2
问题类别：EX / PED
问题说明：权限图已经画了三道门，8.14 把 401/403 都当 MiniShop 门牌，可运行验收仍只有 403。脚本替学生取了 Bearer，没有「再改一个输入」（去掉凭证看 401）。`--check` 也不锁 401。
为什么有问题：核心章那句的一半是页面观察 vs 服务器判定，8-1 练到了；另一半「不是三种产品」和 401 门牌都停在「自己看一眼」。
依据：本机 `python3 practice/run.py 8-1` 与 `--check` 均通过，输出无 401；教学审查补丁 1 仍未落地。
建议修改：矩阵加一行无凭证 → 401，并在 `latest.json` / unittest 断言。注意与 CH08-0001 一起写清 Cookie。

## ISSUE
ID：CH08-0007
文件：`chapters/08b-web-auth-permission.md`；`practice/08-privilege/main.py`；`project/minishop/frontend/index.html`
章节：第 8 章（下）
小节：错误 3；8.14 末段；8-1 收尾问句
精确位置：08b L338–340；main.py L115
原文：页面藏掉后台按钮，就算测过权限 / 为什么「后台入口在页面上看不见」不能代替这次 403？
问题等级：P2
问题类别：ACC / PED
问题说明：MiniShop 登录后对 **普通用户** 也渲染 `<a href="/admin.html">后台</a>`（`index.html` L53；`05-cart-qty-11.png` 可见）。原则「藏按钮 ≠ 权限」对，但作业问句假定 MiniShop 藏了入口，和项目相反。
为什么有问题：【Beginner Friction】学生打开页面看见「后台」，会以为自己理解错了。
依据：`index.html` L53；本轮打开的 03/04/05 截图。
建议修改：改成「MiniShop **没有**藏后台链接；普通用户点进去静态页仍可能 200，要以 `/api/admin/*` 是否 403 为准。」

## ISSUE
ID：CH08-0008
文件：`chapters/08b-web-auth-permission.md`；`project/minishop/frontend/app.js`；`admin.html`
章节：第 8 章（下）
小节：8.11 Token；面试示例；可运行性说明
精确位置：08b L101–107、L355–357、L425
原文：Token 可以放在 Web Storage。……不要根据「看起来更现代」判断哪种一定更安全。
问题等级：P2
问题类别：ACC / TERM
问题说明：分层表和蛋糕图都对，但始终不点名 **v1.0 页面把 `token` 放进 `sessionStorage.minishop_token`，同时 `Set-Cookie: minishop_session=同一串; HttpOnly`**。学生按本章去 Application 面板会对不上号。`admin.html` L23 也读 sessionStorage。
为什么有问题：本章唯一主案例的分层现场，正文只说到 HTTP 响应，没说到页面脚本这一层。
依据：`app.js` L47–48；`admin.html` L23；`01-login-ok.txt`；PRD `R-AUTH`。
建议修改：加「当前实现」三行，标明未冻结成「必须用 sessionStorage」的契约。
推荐替换文本：当前实现：JSON `token` 与 HttpOnly Cookie 是同一份随机串；页面脚本写入 `sessionStorage`，后续 `fetch` 加 `Authorization: Bearer`。Cookie 仍可能被浏览器自动带上。服务端先看 Bearer，没有再看 Cookie。`sessionStorage` 不是服务端 Session。

## ISSUE
ID：CH08-0009
文件：`chapters/assets/diagrams/ch08-browser-vs-server.html` / `.png`；`chapters/08a-web-page-testing.md` §8.3
章节：第 8 章（上）
小节：8.3 表单测试配图
精确位置：图第二盒「绕过页面直接 POST 空手机号，应 400」
原文：应 400。库里不得出现该用户。
问题等级：P2
问题类别：IMG / SEQ / HTTP
问题说明：08A 正文故意不教状态码（留给第 9 章），图却写死 400。配图紧挨着 **登录** 教学表单；MiniShop **登录**空手机号本轮实测是 **401** `{"result":"fail"}`，**注册**空手机号才是 400。图还用「库里不得出现该用户」，那是注册语义。
为什么有问题：学生会把 400 当已学概念，并可能拿去当 MiniShop 登录预期。
依据：本机实测；08a L127「请求方法的语义在第 9 章展开」；08b L162「具体状态码等到第 9 章」。
建议修改：第二盒改「服务端应拒绝，且库里不得出现该用户（数字留到第 9 章）」。若举 MiniShop，分开登录 401 / 注册 400。

## ISSUE
ID：CH08-0010
文件：`chapters/08a-web-page-testing.md`；`chapters/assets/07-html-lab.html`
章节：第 8 章（上）
小节：8.3 教学示例
精确位置：08a L84「完整、可独立打开」；L86–118 代码块；lab 页密码框
原文：下面是一个**完整、可独立打开**的教学页面
问题等级：P2
问题类别：PED / CODE
问题说明：可独立打开的是 `07-html-lab.html`，不是 markdown 代码块。Lab 密码框 **没有** `minlength`/`maxlength`；代码块是 8～16。场景导入让学生打开 lab，练习 2 问的 `required`+`maxlength=11` 在手机号上两边都有，但密码尺只存在于代码块。标题仍是 `MiniShop 教学登录表单`，学生容易当成正式登录页。
为什么有问题：本章最重要的反例「浏览器约束 ≠ 服务器」有现成 MiniShop 注册框（无 `required`，空提交会打到 `/api/register`），正文没用。
依据：`07-html-lab.html` L20–21；`index.html` 登录有 `required`、注册没有。
建议修改：声明「能打开的是 lab 页；代码块若保留，注明与 lab 字段不完全相同」。工作实战用 MiniShop 注册空提交对照登录空提交。

## ISSUE
ID：CH08-0011
文件：`chapters/08b-web-auth-permission.md`
章节：第 8 章（下）
小节：8.13 登录态怎样测
精确位置：L148–158 表：未登录访问需登录页、退出后访问、过期后操作
原文：未登录访问需登录页 → 拒绝或跳转到登录
问题等级：P2
问题类别：PED / ACC
问题说明：v1.0 没有独立登录页、没有退出入口、Token 不失效。未登录打开的是 `/` 上的登录表单；`/admin.html` 未登录也是静态 200。8.10 已说无退出则记未测项，8.13 最小集合没有同样标注。
为什么有问题：【Beginner Friction】学生会在 MiniShop 里找「跳登录页」「点退出」。
依据：`index.html`；`server.py` 无 logout；PRD 非范围。
建议修改：表旁加「v1.0：无独立受保护页面、无退出、无过期；这些行记未测或改测受保护 API。」

## ISSUE
ID：CH08-0012
文件：`chapters/08b-web-auth-permission.md`；`practice/08-privilege/`
章节：第 8 章（下）
小节：8.14 步骤建议；实操 8-1
精确位置：08b L187–192；README 五格
原文：步骤 1–4 到普通用户 403 为止
问题等级：P2
问题类别：TEST / JOB
问题说明：PRD `R-PERM` 与 OpenAPI 写明 **管理员走 `GET /api/orders/{id}` 读他人订单也是 403**。`tests/test_api.py` `test_order_forbidden_other_user` 已覆盖。8.14/8-1 未提。不是错误，是核心权限口径缺一条。
依据：PRD L27；OpenAPI `/api/orders/{id}` summary；本机 `ADMIN GET A order → 403`。
建议修改：步骤加第 5 条：管理员带自己的 token 读 A 的订单，预期仍 403；管理员看订单列表走 `/api/admin/orders` 且只返回 id。

## ISSUE
ID：CH08-0013
文件：`chapters/08a-web-page-testing.md`
章节：第 8 章（上）
小节：面试角度「浏览器约束和服务端校验」
精确位置：L350
原文：用 DevTools 删掉属性或直接打接口仍可能成功。
问题等级：P2
问题类别：SEQ
问题说明：DevTools 是第 10 章。此处把未教工具当面试示例。
依据：学习顺序 08→09→10。
建议修改：改成打开 `07-html-lab.html` 去掉 `required` 再提交，教学页只显示「已触发提交」，仍不是服务端证据。

## ISSUE
ID：CH08-0014
文件：`chapters/08b-web-auth-permission.md`
章节：第 8 章（下）
小节：8.14
精确位置：L194「不要把 404 写成 MiniShop 的可接受结果。有的系统用 404 隐藏资源」
原文：同上
问题等级：P2
问题类别：JOB / HTTP
问题说明：这句话方向对，但没说 MiniShop **存在但非本人 → 403，不存在 → 404**，等于用状态码泄露「这个 id 在不在」。这是初级权限测试常见追问（OWASP BOLA/IDOR 存在性）。
依据：`server.py` `_get_order` L487–494 先 404 再 403；RFC 9110/MDN 也提到可用 404 隐藏资源。
建议修改：加一句岗位边界：MiniShop 对存在的他人订单回 403、对不存在回 404；测的时候既不要把 404 当他人订单通过，也要记录这个存在性差异。只在自己创建的 id 上测。

## ISSUE
ID：CH08-0015
文件：`chapters/assets/diagrams/ch08-search.html` / `.png`；`chapters/08a-web-page-testing.md` §8.6
章节：第 8 章（上）
小节：8.6 搜索测试配图
精确位置：图中盒「R-SEARCH 预期：400 或空列表并提示输入关键字」
原文：400 或空列表并提示输入关键字
问题等级：P2
问题类别：IMG / SEQ
问题说明：与 `BUG-001.md` 预期举例一致，不是乱编契约。但 08A 未教 400，PRD `R-SEARCH` 只禁止把全量当结果，不规定 400。图把 400 画成 R-SEARCH 预期，学生会抄进用例。
依据：PRD L28；OpenAPI `/api/products` 只文档化 200。
建议修改：R-SEARCH 盒改「不应返回全量；空列表+提示，或明确拒绝。具体数字第 9 章再钉」。

## 6. P3

## ISSUE
ID：CH08-0016
文件：`chapters/08a-web-page-testing.md`；`chapters/08b-web-auth-permission.md`
章节：第 8 章
小节：小练习
精确位置：08A 练习 2 起跳；08B 练习 1、6–9
原文：练习 2 …（无说明 1 在下册）
问题等级：P3
问题类别：PED
问题说明：拆章后编号不连续。08A 未写「练习 1 在 08B」。
建议修改：08A 小练习开头加一句「全章 10 题拆在上下册，本题从 2 开始。」

## ISSUE
ID：CH08-0017
文件：`chapters/assets/diagrams/ch08-auth-layers.html` / `.png`
章节：第 8 章（下）
小节：8.11 配图脚注
精确位置：HTML L30
原文：一层是「是什么」，一层是「存在哪」，一层是「怎么带出门」。
问题等级：P3
问题类别：IMG
问题说明：图实际是四层（凭证 / 服务端 Session / Cookie / 出示方式）。脚注说三层。
建议修改：改成四层各一句，或删「三层」计数。

## ISSUE
ID：CH08-0018
文件：`chapters/08a-web-page-testing.md`
章节：第 8 章（上）
小节：8.6 vs 练习 4
精确位置：L199 与 L377
原文：`https://shop.example.test:8443/products?keyword=mouse&page=2` vs `https://shop.example.test/products?keyword=mouse&page=99999`
问题等级：P3
问题类别：ACC
问题说明：同一教学主机有的带 `:8443` 有的不带。已标明教学 URL，不致教错 MiniShop，但增加噪音。
建议修改：统一带或不带端口，并重复「不是 MiniShop 路由」。

## ISSUE
ID：CH08-0019
文件：`chapters/08a-web-page-testing.md`；`chapters/08b-web-auth-permission.md`
章节：第 8 章
小节：参考资料
精确位置：08a L421「WHATWG HTML Forms」；08b L430「RFC 6750 Bearer Token」
原文：仅有名称，无链接
问题等级：P3
问题类别：LINK
问题说明：零基础无法跳到规范。
建议修改：链到 WHATWG forms 与 RFC 6750（或 MDN 中文导读），并写「不必通读」。

## ISSUE
ID：CH08-0020
文件：`chapters/08a-web-page-testing.md`
章节：第 8 章（上）
小节：8.10
精确位置：L276
原文：不把阈值、提示文案和跳转写成 MiniShop 正式规则
问题等级：P3
问题类别：TERM
问题说明：锁定/验证码/文案确实不是 v1.0 契约；但 `R-PHONE`/`R-PASS` 已在 PRD。把手机号 11 位、密码 8～16 与「锁定模型」捆在一起说「不是正式规则」，测正在跑的 MiniShop 时会缩手。
建议修改：拆开：验证码/锁定/提示文案 = 教学模型；手机号与密码长度测 v1.0 时跟 PRD。

## ISSUE
ID：CH08-0021
文件：`chapters/08b-web-auth-permission.md`
章节：第 8 章（下）
小节：8.15
精确位置：L211「P0 覆盖最常见组合」
原文：列出浏览器 × 操作系统 × 视口的优先级，P0 覆盖最常见组合
问题等级：P3
问题类别：TERM
问题说明：第 5 章已声明 P0/P1 是课程约定。这里直接用 P0，未再声明「不是全球统一」。
建议修改：写「课程优先级 P0（组织标准优先）」。

## ISSUE
ID：CH08-0022
文件：`practice/08-privilege/tests/test_lab.py`；`practice/08-privilege/main.py`
章节：实操 8-1
小节：验收脚本
精确位置：test_lab.py L15–21
原文：只断言四个状态码字段
问题等级：P3
问题类别：CODE
问题说明：不检查 `create==201`、403 Body 不含他人 `id`、管理员列表只有 `id` 字段。`main.py` 的 `ok` 含 201，但 unittest 间接依赖 `main()==0`。
建议修改：断言 `create.status==201`、`b_reads_a` Body 无该 id。

## ISSUE
ID：CH08-0023
文件：`chapters/08a-web-page-testing.md`；`project/minishop/frontend/index.html`
章节：第 8 章（上）
小节：8.3 / 8.10
精确位置：教学表单强调 required；未提 MiniShop 注册框
原文：（缺失）
问题等级：P3
问题类别：PED
问题说明：登录框有 `required`，注册框没有。空注册会打到服务端并 400。这是「浏览器拦了 ≠ 服务器拦了」最好的项目内反例，正文完全没写。升格空间见 CH08-0010。
建议修改：8.3 加 MiniShop 对照一句即可。

## 7. 逐段问题

凡未单列 ISSUE 的单元，本轮判定为 **通过**（含「故意推迟到第 9/10 章」且正文已声明的）。

### 索引 `08-web-functional-testing.md`

| 单元 | 结论 |
| --- | --- |
| 一句话核心 | 通过。两半都成立，能当过滤器。 |
| 拆章说明与两节链接 | 通过。目标文件存在。 |
| 作业链接（对照截图 / 测试包 / 8-1） | 通过可点；作业形态问题见 CH08-0005。 |
| 阶段测验 3（学完第 10 章再做） | 通过。 |
| 下一章 09A | 通过。 |

### 08A 结构段

| 单元 | 结论 |
| --- | --- |
| 一句话核心 | 通过。 |
| 这一章解决什么问题 | 通过。Cookie 放到 08B 正确。缺第 6 章承接句，不单列。 |
| 学习目标 | 通过。退出「无入口则记未测」诚实。 |
| 前置知识 | 通过。 |
| 场景导入 + lab / 8765 / 01-login | 通过。lab 不连服务器写清了。 |

### 08A 8.1–8.10

| 单元 | 结论 |
| --- | --- |
| 8.1 定义与分类轴 | 通过。不把 Web 测试当新类别。v1.0 无验证码/下架/详情/小计均标明。 |
| 8.1 表「权限对吗」 | 通过（预告 08B）。 |
| 8.2 控件角色表 | 通过。MiniShop 有的才写 MiniShop；`/admin.html` 作为链接例正确。 |
| 8.2 Tab/placeholder/a11y 边界 | 通过。完整无障碍超出初级，但「找不到控件」可报缺陷。 |
| 8.3 配图 | CH08-0009。 |
| 8.3 教学 HTML | 语法通过（html.parser 无报错；label/for、password、required、minlength 8、maxlength 16 与 `R-PASS` 对齐）。「可独立打开」见 CH08-0010。`<title>` 仍带 MiniShop。 |
| 8.3 浏览器约束 ≠ 服务端 | 通过。禁止从 `method=post` 推出 POST 更安全，通过。 |
| 8.3 表单清单 | 通过。重复提交、刷新重复提交有岗位价值。 |
| 8.4 输入表 | 通过。等价类/边界接第 5 章。`R-CART-10` 双基线写法可接受。「连续点击加号」MiniShop 无步进器，是一般例子。 |
| 8.4 「不能输入」拆成键入/提交/回显 | 通过。与 CH08-0004 答案未执行同一标准形成对照。 |
| 8.5 链接 | 通过。禁止未授权爬取。fragment 不发给服务器接第 7 章。 |
| 8.6 搜索 + 教学 URL | 通过（教学 URL 已声明）。配图 400 见 CH08-0015。特殊字符只在授权环境、禁止外部注入，通过。 |
| 8.7 分页 | 通过。v1.0 无分页 → 未测项。空白≠通过。 |
| 8.8 上传 ⭐⭐ | 通过。无入口不编步骤；禁止恶意样本；类型绕过仅限自有环境。 |
| 8.9 下载 ⭐⭐ | 通过。脱敏接第 6 章。 |
| 8.10 草案 vs 正式 | 大体通过；阈值捆包见 CH08-0020。v1.0 无验证码、无退出入口，通过。 |

### 08A 后半

| 单元 | 结论 |
| --- | --- |
| 工作实战 1 label/password | 通过（01 能看 label；type=password 在 02 的圆点更明显）。 |
| 工作实战 2 登录失败 | 通过。02 图有「登录失败」，账号 `13800138000`。 |
| 工作实战 3 空白搜索 | CH08-0003。 |
| 工作实战 4 qty=11 | 通过。与 05 图一致：提示 + 列表 `qty=1`。 |
| 错误 1–5 | 通过。 |
| 面试 3 题 | 结构通过；DevTools 见 CH08-0013。空搜索/退出边界通过。 |
| 练习 2–5、10 | 题干通过；答案 10 见 CH08-0004。编号见 CH08-0016。 |
| 检查清单 / 总结 / 可运行性 / 参考 / 预告 | 通过（参考无链 CH08-0019）。 |

### 08B 结构段

| 单元 | 结论 |
| --- | --- |
| 一句话核心 | 通过。正是质量标准禁止项的正确表述。 |
| 学习目标 | 通过。HttpOnly 边界、Bearer≠JWT、横/纵越权都在目标里。 |
| 前置 / 场景导入 | 通过。已改为刷新/隐私窗口，A/B 订单推到 8.14。旧「购物车 URL」已不在。v1.0 无分享购物车 URL，通过。 |

### 08B 8.11–8.17

| 单元 | 结论 |
| --- | --- |
| 8.11 层次表五概念 | 通过。Cookie / Session / Session ID / Token / Bearer 分层正确，常见误解列得准。 |
| mermaid 流程 | 通过。语法有效；「会话和/或令牌」符合 MiniShop（sessions 表 + 同一 token）。 |
| Cookie 属性表 | 通过。HttpOnly **不**阻止携带，写清了；脚本同站请求仍会带，通过。 |
| SameSite / CSRF 段 | 通过。默认 Lax、None 必须 Secure、Lax 挡大多数跨站 POST、顶层 GET 仍可能，与 MDN 2026-09 一致。禁止外部攻击。未宣称 Lax 之后跨站 POST 一定还能改购物车。 |
| Secure + Safari localhost | 通过。Chrome/Firefox 对 localhost 有例外，Safari 更严，与公开行为一致。 |
| 第三方 Cookie / 不展开 CHIPS | 通过。 |
| Cookie 还在 ≠ 会话有效 | 通过。 |
| Session / Session ID 可放 Cookie | 通过。URL 中的 Session ID 风险，通过。 |
| Token / JWT 只是格式 / Web Storage 不自动发送 / sessionStorage≠Session / XSS | 通过。缺 MiniShop sessionStorage 点名，CH08-0008。 |
| 配合组合 + 面试答法 | 通过。 |
| 8.12 Bearer RFC 6750 | 通过。「持有者即可用」、`Authorization: Bearer`、不是 JWT/OAuth/Cookie 的别名。脱敏要求通过。⭐⭐⭐ 偏紧但标明报文在第 9 章。 |
| 8.13 登录态表 | 方向通过；与 v1.0 入口缺口见 CH08-0011。头像不是判定、要做需身份的操作，通过。 |
| 8.14 配图三道门 | 命题通过；401 盒的操作口径见 CH08-0001。横盒标明 200 才是失效，通过。纵盒静态页 200≠API 403，通过。 |
| 8.14 类型表 | 横/纵正确；未认证行 CH08-0001/0002。认证后权限变化标明 v1.0 无锁定，通过。 |
| 8.14 门牌三段 | 教学策略通过（不当 RFC 背）。步骤与 8-1 同通道，通过。禁止 404 当 MiniShop 他人订单通过，通过；存在性见 CH08-0014。授权环境，通过。 |
| 8.15 兼容性 ⭐⭐ | 通过。矩阵来自用户数据而非个人偏好；弱网≠兼容性；未覆盖写未测项。P0 用词 CH08-0021。 |
| 8.16 响应式 ⭐⭐ | 通过。与兼容性拆开；要真的完成一次搜索/加购。375/1280 例子合理。 |
| 8.17 缺陷字段 | 通过。接第 6 章；禁止标题里写死「肯定是前端 Cookie」。 |
| 8-1 入口句 | 通过可点；「藏按钮」口径 CH08-0007。 |

### 08B 后半

| 单元 | 结论 |
| --- | --- |
| 工作实战测试包 | 通过。对象/未测项/8 条用例/1 条缺陷或无缺陷说明/兼容记录；路径 `exercises/chapter-08-minishop-web-functional.md`；禁止密码和完整 Token；禁止编详情页和购物车 URL。 |
| 错误 1–5 | 通过。错误 1/2/4 钉死禁止项。错误 2 写 MiniShop 同时下发 token 与 HttpOnly Cookie，通过。 |
| 面试 3 题 | 通过。MiniShop 同时给 token 与 Set-Cookie、后续 Bearer，与证据文件一致。 |
| 练习 1/6–9 与答案 | 通过。练习 6 已改为 `GET /api/orders/{id}` 403（旧购物车 URL 错误已不在）。 |
| 检查清单 / 总结 / 可运行性 / 参考 / 09A+测验 3 | 通过。 |

### 实操 8-1

| 单元 | 结论 |
| --- | --- |
| README 目标 / R-PERM / 五格 | 他人订单 403、自己 200、非管理员 403、管理员 200：与实现一致。缺 401 见 CH08-0006。 |
| 「脚本带的是 Bearer」+ 对照 `01-login-ok.txt` | 通过（分层半边的阅读作业，不是运行验收）。 |
| `main.py` | 通过。标准库、临时 MiniShop、教学账号、SKU-DEMO-001 qty=1、Bearer 头、写 `validation/latest.json`。本机退出码 0。 |
| `test_lab.py` | 能跑通；覆盖面 CH08-0022。 |
| 收尾问句 | CH08-0007。 |

### 测验 3（仅第 8 章题）

见 §11。题 1/2/3/5/9/10 与正文一致，**无 【ANSWER VERIFICATION FAILED】**。题 4/6/7/8 属第 9/10 章，本审计不判对错。

### MiniShop 前端口径（核对本权限，不扩审第 19 章）

| 点 | 结论 |
| --- | --- |
| 登录页是 `/` 不是 `/login` | 正文未把 `/login` 当可抄页面。通过。 |
| `type=password` + label | 与 08A 工作实战 1 一致。 |
| 注册成功不签发 token | 页面说明与 `R-REG` 一致；08A 8.10 问了「成功后是否自动登录」，未点名 MiniShop 答案。 |
| 后台链接对普通用户可见 | CH08-0007。 |
| `sessionStorage` + Bearer | CH08-0008。 |
| `admin.html` 静态 200，API 401/403 才拦 | 与 8.14 一致。前端把 401/403 合成「无权限」，正文未提，可接受。 |

## 8. 代码问题

| 块 | 结果 |
| --- | --- |
| 08A 教学 HTML | 可解析；`preventDefault` 不连服务。不是 MiniShop 实现，已声明。问题是「可独立打开」名不副实（CH08-0010）。 |
| 08B mermaid | 合法 flowchart，层次与正文一致。 |
| 8-1 `main.py` | 本机运行通过。登录失败会 `SystemExit`。`order_id is None` 时 URL 会变成 `/api/orders/None`，失败路径仍会 `ok=False`。 |
| 8-1 测试 | 1 条用例，间接跑 `main()`。见 CH08-0022。 |
| MiniShop `server.py` 权限（对照用，非本章代码） | 他人/管理员读他人订单 403；无凭证 401；Cookie 回退存在（CH08-0001）。 |

**已执行：**

```text
python3 practice/run.py 8-1          → exit 0
  A 下单 201；B 读 A 403；A 读自己 200；普通用户 admin 403；管理员 admin 200
python3 practice/run.py 8-1 --check  → test_privilege_matrix ok，exit 0
```

额外探针（MiniShopLab，不改仓库）：无凭证 `GET /api/orders/{id}` 401；`GET /api/orders` 404；Cookie-only 读自己 200；管理员读他人 403；登录空手机号 401；注册空手机号 400。

## 9. 图片问题

IMG-CH08-001  
文件：`chapters/assets/diagrams/ch08-browser-vs-server.png` + `.html`  
出现位置：08A §8.3  
图片主要内容：浏览器 `required` 拦住空提交 ≠ 服务器规则。  
技术准确性：命题对；第二盒写死 400，且「库里不得出现」是注册语义。  
与正文一致性：正文不教 400。  
文字是否正确：中文正确。  
UI 是否过时：否（概念图）。  
教学价值：高。  
可读性：好。  
是否需要修改：是。  
修改建议：见 CH08-0009。  
最终结论：**MODIFY**

IMG-CH08-002  
文件：`chapters/assets/diagrams/ch08-search.png` + `.html`  
出现位置：08A §8.6  
图片主要内容：空格搜索列出三件是缺陷，不是「搜索还能用」。  
技术准确性：缺陷判断对；R-SEARCH 盒把 400 写成预期过早。  
与正文一致性：正文空搜索选项是「全量 / 必填 / 无结果」，未规定 400。  
文字是否正确：是。  
UI 是否过时：否。  
教学价值：高。  
可读性：好。  
是否需要修改：是。  
修改建议：见 CH08-0015。  
最终结论：**MODIFY**

IMG-CH08-003  
文件：`chapters/assets/diagrams/ch08-auth-layers.png` + `.html`  
出现位置：08B §8.11  
图片主要内容：Cookie / Session / Token / Bearer 四层蛋糕，否定三选一。MiniShop 脚注 token + HttpOnly Cookie、后续 Bearer。  
技术准确性：正确，且与 `01-login-ok.txt`、`R-AUTH` 一致。  
与正文一致性：高。  
文字是否正确：是。脚注「三层」计数不准（CH08-0017）。  
UI 是否过时：否。  
教学价值：本章最高。  
可读性：好。  
是否需要修改：轻微。  
修改建议：脚注改四层。  
最终结论：**MODIFY**（小改；内容 KEEP 级别）

IMG-CH08-004  
文件：`chapters/assets/diagrams/ch08-privilege.png` + `.html`  
出现位置：08B §8.14  
图片主要内容：未认证 401 / 横向 403 / 纵向 403 三道门；静态页 200 ≠ API 403。  
技术准确性：门牌与 MiniShop 一致；「不带 Bearer」操作见 CH08-0001。横盒标明 200 才是失效，优于旧图。  
与正文一致性：高。  
文字是否正确：是。  
UI 是否过时：否。  
教学价值：高。  
可读性：好。  
是否需要修改：是（401 盒补 Cookie）。  
修改建议：见 CH08-0001。  
最终结论：**MODIFY**

IMG-CH08-005  
文件：`chapters/assets/diagrams/ch08-compat-responsive.png` + `.html`  
出现位置：08B §8.15  
图片主要内容：换浏览器 vs 换宽度不是同一类报告。  
技术准确性：正确。  
与正文一致性：高。  
文字是否正确：是。  
UI 是否过时：否。  
教学价值：足够。  
可读性：好。  
是否需要修改：否。  
最终结论：**KEEP**

IMG-CH08-006  
文件：`chapters/assets/01-login.png`  
出现位置：08A 场景导入、工作实战 1  
图片主要内容：MiniShop 登录+注册表单，有 label。  
技术准确性：与 `index.html` 一致；个人实践项目声明可见。空密码框看不出 `type=password`。  
与正文一致性：工作实战 1 需要结合 02 图才能确认 password。  
文字是否正确：是。  
UI 是否过时：否。  
教学价值：中。  
可读性：好。  
是否需要修改：否（可在正文写「password 看 02 图圆点」）。  
最终结论：**KEEP**

IMG-CH08-007  
文件：`chapters/assets/02-login-fail.png`  
出现位置：08A 工作实战 2  
图片主要内容：`13800138000` + 密码圆点 +「登录失败」。  
技术准确性：与 `app.js` 失败文案一致。  
与正文一致性：高。  
文字是否正确：是。  
UI 是否过时：否。  
教学价值：高。  
可读性：好。  
最终结论：**KEEP**

IMG-CH08-008  
文件：`chapters/assets/04-search-empty-bug001.png`  
出现位置：08A 工作实战 3  
图片主要内容：登录后商品三件、「共 3 件」、关键字框看似为空。  
技术准确性：作为 BUG-001 证据不足，与 `03-shop.png` 不可分。  
与正文一致性：正文把它当空白搜索证据，过强。  
文字是否正确：界面文字对。  
UI 是否过时：否。  
教学价值：低（无法证明搜索发生过）。  
可读性：好。  
是否需要修改：是。  
修改建议：见 CH08-0003。可改用 HTTP 证据 `03-products-empty-keyword.txt`（`keyword=%20%20%20`，200，三件）。  
最终结论：**REPLACE**

IMG-CH08-009  
文件：`chapters/assets/05-cart-qty-11.png`  
出现位置：08A 工作实战 4  
图片主要内容：数量框 11、`qty exceeds stock`、列表 `SKU-DEMO-001 qty=1`；普通用户可见「后台」。  
技术准确性：与实现和 `R-CART-10` 一致。  
与正文一致性：工作实战 4 写对了；练习 10 答案没对齐这张图。  
文字是否正确：是。  
UI 是否过时：否。  
教学价值：高。  
可读性：好。  
最终结论：**KEEP**

IMG-CH08-010  
文件：`chapters/assets/07-html-lab.html`  
出现位置：08A 场景导入、可运行性说明  
图片主要内容：不连服务器的教学登录表单；phone `required maxlength=11`；password 仅 `required`。  
技术准确性：提交被拦住，文案诚实。  
与正文一致性：与 8.3 代码块密码约束不一致（CH08-0010）。  
文字是否正确：是。  
UI 是否过时：否。  
教学价值：高（真正可打开）。  
可读性：好。  
最终结论：**MODIFY**（补密码 8～16 或正文声明差异）

对照打开、正文未引用：`03-shop.png` 支持 CH08-0003；`06-register.png` 与 `01-login.png` **字节级相同**，不能当注册成功证据（本章未引用，不单列 ISSUE）；`07-admin.png` 是管理员已加载态，08B 未用，建议作「普通用户打开后台」对照图。

## 10. 表格问题

| 表 | 结论 |
| --- | --- |
| 08A 8.1 测什么 | 通过。 |
| 08A 8.2 元素 | 通过。 |
| 08A 8.3 表单清单 | 通过。 |
| 08A 8.4 输入 | 通过。 |
| 08A 8.6 搜索 | 通过。 |
| 08A 8.7 分页 | 通过。无入口则未测。 |
| 08A 8.8 / 8.9 | 通过。⭐⭐。 |
| 08B 8.11 概念层次 | 通过。本章最好的表。 |
| 08B Cookie 属性 | 通过。 |
| 08B 8.13 登录态 | 见 CH08-0011。 |
| 08B 8.14 权限类型 | CH08-0001/0002。横/纵两行通过。 |
| 08B 8.16 视口 | 通过。 |
| 08B 测试包模板四表 | 通过。 |
| 8-1 五格 | 与实现一致；缺 401 见 CH08-0006。 |

## 11. 练习与答案问题

### 独立作答（先于对照教材答案）

**08A**

2. 不能。`required`/`maxlength` 是浏览器约束，可被改 DOM、关脚本或直接打接口绕过。服务端是否拒绝要看保存结果或绕过页面的请求。  
3. 至少：是否发出请求；结果是全量、空列表还是错误；有无提示；URL 的 keyword 是什么（空/空格）；刷新是否保持。不能只写「不能搜」。  
4. 不一定是缺陷。可能是合法空态或非法页码未处理。应看总页数、提示、改回 `page=2` 是否恢复、关键词是否还在。该 URL 是教学地址，不是 MiniShop 路由。  
5. 标题要含对象+条件+实际：例如「头像上传选择 0 字节 PNG 时提示成功，重新进入仍显示默认头像」。  
10. 步骤：登录；确认教学 SKU 库存 10、当前列表数量 1；改为 11 提交。预期：失败提示；**列表**不得变成 11。缺陷标题含对象/条件/实际。不写接口路径、不写小计。

**08B**

1. 不是三种登录方式。Cookie：浏览器保存并可能自动发送；Session：服务端会话状态；Token：凭证。常配合，Session ID/Token 都可放进 Cookie。  
6. 横向越权。MiniShop 预期 403。报告要有两个角色、脱敏 URL、Body 是否含 A 的数据。只在授权账号上做。  
7. 不足。可能是缓存。再做一次写操作，并在新窗口打开需登录 URL。  
8. C。  
9. 计划写明 P0 组合来自产品声明；响应式写视口；范围外进未测项和剩余风险，不默认为通过。

**阶段测验 3（第 8 章题）**

1. 层次不同、常配合：Cookie 存/带，Session 服务端状态，Token 凭证。  
2. HttpOnly 阻止脚本读取；不阻止请求自动携带。  
3. 不能。前端约束可绕过。  
5. 401：没认出你（无有效凭证访问受保护接口，如无凭证下单/读订单）。403：认出你但不许（B 读 A 的订单；普通用户 `/api/admin/*`）。  
9. JSON `token` + `Set-Cookie`（HttpOnly）；后续 API 以 Bearer 为准。  
10. C。A 把 Bearer 当成 Session；B 是 DevTools 行为（非本章主课）；D Lax 挡不住一切跨站请求。

### 对照教材答案

| 题 | 结果 |
| --- | --- |
| 08A-2,3,4,5 | 一致。 |
| 08A-10 | **部分不一致**：方向对，但「数量保持合法值」不可观察。记入 CH08-0004，不升格为整题 【ANSWER VERIFICATION FAILED】。 |
| 08B-1,6,7,8,9 | 一致。练习 6 已与 8-1/R-PERM 对齐（旧审查 ISS-08-01 已修）。 |
| 测验 1,2,3,5,9,10 | 一致。测验 5 用「无 token 下单」比 8.14 表的 `/api/orders` 更准确。 |

## 12. 初学者理解障碍

标记 【Beginner Friction】：

1. 08A 练习从 2 起，像漏题（CH08-0016）。  
2. 「可独立打开」的表单其实要复制代码；真正能打开的 lab 页密码尺还不一样（CH08-0010）。  
3. 对着 04 图看不出「我搜过」（CH08-0003）。  
4. 按 8.14 表打 `GET /api/orders` 得到 404（CH08-0002）。  
5. 在已登录浏览器里去掉 Bearer 仍 200（CH08-0001）。  
6. 8.13 找「需登录页 / 退出按钮」找不到（CH08-0011）。  
7. 8-1 问「为什么藏掉后台不能代替 403」，页面上后台链接明明在（CH08-0007）。  
8. 08B 一句话是分层，可运行作业却几乎只练 403；分层要自己去读一份 evidence 文本。  
9. 8.13 刚说状态码留到第 9 章，8.14 立刻出现 401/403。虽有「门牌」缓冲，仍陡。  
10. CSRF/SameSite 单段信息密度高，发生在还没观察过登录请求之前。

## 13. 岗位能力缺口

标记 【Job Reality Gap】：

1. 权限测试标准动作应包含：无凭证、本账号、同级他人、更高权限、权限变更后旧凭证。本章只把中间两格做成可运行。  
2. IDOR 存在性（403 vs 404）未写进步骤（CH08-0014）。  
3. 浏览器自动带 Cookie + 页面脚本带 Bearer 是真实系统的默认形状，正文停在概念表。  
4. 无退出、无过期、无 CSRF Token 的 MiniShop 应明确「这些是未测/未做，不是已经安全」。  
5. 兼容性只有方法没有一次真实双浏览器记录；对初级岗可接受，但工作实战「最小兼容记录」容易写成空表。  
6. 8.15 的 P0 未重复「组织标准优先」。  
7. 管理员读他人订单 403 是冻结口径，岗位口述常问，8-1 没跑。

## 14. 建议删除内容

- 不必删 8.8/8.9 上传下载：已标 ⭐⭐ 且承认 MiniShop 无入口。  
- 不必删 CSRF 整段：有测试边界、有授权限制。可压缩，见下。  
- 若保留 8.3 完整 HTML，删除「可独立打开」四字，或删代码块改链 lab。  
- 08A 工作实战不要再把 04 图单独当作 BUG-001 的充分证据。

## 15. 建议新增内容

1. 8-1 第六格：无 Cookie 无 Bearer → 401；可选第七格：只带 Cookie → 200（分层现场）。  
2. 一句 `sessionStorage.minishop_token` 映射（CH08-0008）。  
3. 08A：`exercises/chapter-08a-page-check.md` + lab 空提交。  
4. MiniShop 登录有 `required`、注册没有的对照。  
5. 普通用户打开 `/admin.html` 的截图（静态 200 +「无权限」），对照 `07-admin.png`。  
6. 管理员 `GET /api/orders/{id}` 仍 403。  
7. 08A 开篇承接第 6 章：上一章会写缺陷单和一页计划，本章把它们用到页面通道。

## 16. 建议重写内容

1. **8.14 未认证行 + 三道门第一盒 + 8-1 README 401 句**（CH08-0001/0002/0006）——必须和 Cookie 回退一起写。  
2. **08A MiniShop 工作实战（上）**（CH08-0005/0003）——从看图改成一次可保存的页面观察。  
3. **练习 10 答案**（CH08-0004）。  
4. **ch08-browser-vs-server 第二盒**（CH08-0009）。  
5. **8-1 收尾问句**（CH08-0007）按真实页面重写。

不需要重写 8.11 层次表、错误 1/2/4、面试「为什么不能说三种登录方式」——这些已经是本章该保留的脊柱。

## 17. 本章结论

**C 明显需要修改**

不是理论写错。Cookie / Session / Token / Bearer 分层、HttpOnly 边界、SameSite/CSRF 授权限制、横/纵越权 403、静态页 ≠ API、禁止三选一和 POST 更安全，经 MDN / RFC 6750 / RFC 9110 常识 / MiniShop 实现核对，主线成立。8-1 对 403 矩阵可运行且与 `R-PERM` 一致。

不能选 B 的原因：核心章仍有 5 条 P1——未认证操作在浏览器里不成立、权限表路径 404、BUG-001 截图不能当证据、练习 10 判定歧义、08A 上册无闭环。这些会让学生在 MiniShop 上抄错尺子。修完 P1 并补 401/Cookie 对照后，可再评 B。

禁止项复核：

- Cookie/Session/Token 三选一：正文否定，通过。  
- GET 不安全 POST 安全：08A 明确禁止，通过。  
- 第 19 章前当冻结契约：教学 URL、草案锁定/验证码有标记；`R-CART-10`/`R-PERM` 用于「正在跑的 v1.0」可接受。搜索图 400 偏越权（P2）。  
- MiniShop 仅个人实践项目：截图和页面均有声明。

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`
- `reviews/_full-audit-2026-09-10/AUDIT_PROGRESS.md`
- `README.md`、`docs/COURSE_CONTROL.md`、`docs/COURSE_OUTLINE_v1.2.md`、`docs/LEARNING.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`、`practice/STATUS.md`、`exercises/README.md`
- `project/minishop/README.md`、`project/minishop/docs/PRD.md`、`project/minishop/docs/openapi.json`
- `chapters/08-web-functional-testing.md`
- `chapters/08a-web-page-testing.md`
- `chapters/08b-web-auth-permission.md`
- `practice/08-privilege/README.md`、`main.py`、`tests/test_lab.py`
- `practice/run.py`、`practice/_http.py`、`practice/_minishop.py`
- `project/minishop/frontend/index.html`、`admin.html`、`app.js`
- `project/minishop/server.py`（鉴权/订单/后台相关）
- `project/minishop/evidence/http/01-login-ok.txt`、`03-products-empty-keyword.txt`
- `project/minishop/bugs/BUG-001.md`
- `project/minishop/tests/test_api.py`（权限用例对照）
- `chapters/quizzes/README.md`、`chapters/quizzes/stage-3-web.md`（只评第 8 章题）
- `chapters/assets/07-html-lab.html`
- `chapters/assets/diagrams/ch08-*.html`（5）+ `ch08-*.png`（5）+ `diagrams/README.md`
- `chapters/assets/01-login.png`、`02-login-fail.png`、`03-shop.png`、`04-search-empty-bug001.png`、`05-cart-qty-11.png`、`06-register.png`、`07-admin.png`
- 线索（独立复核，未照抄结论）：`reviews/chapter-08-review.md`、`reviews/_pedagogy-2026-09-10/ch08.md`、`RUBRIC.md`、`MASTER.md` 第 8 章行、`reviews/_rereview-2026-09-09/stage-3-ch07-08-10.md`

未修改任何教材正文、practice、project。

### 实际跑过的命令与结果摘要

| 命令 | 结果 |
| --- | --- |
| `python3 practice/run.py 8-1` | exit 0。201 / 403 / 200 / 403 / 200。证据 `practice/08-privilege/validation/latest.json` |
| `python3 practice/run.py 8-1 --check` | `test_privilege_matrix` ok |
| MiniShopLab 探针 | 无凭证 GET `/api/orders/{id}` 401；GET `/api/orders` **404**；Cookie-only 自己的订单 200；管理员读他人 403；登录空手机号 **401**；注册空手机号 **400**；`keyword=` 与空格均 200 三件 |
| `html.parser` 解析 08A 教学 HTML | 无报错；label/for、password、required、maxlength 16 存在 |
| sha256 截图 | `01-login.png` == `06-register.png`；`03-shop` 与 `04-search-empty` 同尺寸、差 12 字节 |

### 外部核查

| 条目 | 来源 | 与教材 |
| --- | --- | --- |
| SameSite 未设置时现代浏览器默认 Lax；`None` 必须 `Secure` | MDN `Set-Cookie` / `SameSite`（检索 2026-09-10） | 一致 |
| HttpOnly 禁 `document.cookie`，不禁请求携带 | MDN Set-Cookie / Document.cookie | 一致 |
| Lax 挡跨站子请求/多数 POST，顶层导航 GET 仍可能带 Cookie | MDN SameSite Lax | 一致 |
| Bearer = 出示方式；谁持有谁可用；`Authorization: Bearer` | RFC 6750 | 一致 |
| 401 缺有效认证凭证；403 已理解但拒绝授权 | RFC 9110 §11.3 / §15.5；MDN 401/403 | 8.14「门牌」方向对；未要求本章背 WWW-Authenticate |
| Safari 对 localhost + Secure Cookie 比 Chrome/Firefox 严 | MDN 注释 + WebKit/公开讨论 | 教材「Safari 对 localhost 例外的支持可能不同」谨慎且正确 |
| 404 可被用来隐藏资源存在性 | MDN 404 | 教材提到「有的系统用 404」，未落到 MiniShop 行为 |

### 与旧审查的关系（非照抄）

- 旧 P0（购物车 URL、qty 图写成 10、`/login` 可抄）现行正文 **已不在**。  
- 08A `maxlength=16`、08B 开篇改登录态、8.14 与 8-1 对齐 403、权限图补 401 盒：已部分落地。  
- 仍未落地：8-1 401 进验收、08A 上册产出、教学页 vs lab、浏览器图 400、面试 DevTools。  
- 本轮新发现：Cookie 回退使「不带 Bearer→401」在浏览器里不成立；`GET /api/orders` 404；04 与 03 截图不可分；练习 10 判定歧义；页面并不藏后台链接。

测验 3 第 8 章题独立推导与标准答案一致。练习 10 仅判定措辞不够可观察。  
