# Chapter 10 Audit

- 审计员：Chapter-Audit-Agent-10
- 日期：2026-09-10
- 范围：仅第 10 章 Chrome DevTools 及其明确列出的相关文件（正文、示意图、引用截图、章内 10-1、阶段测验 3 中第 10 章题、STATUS 诚实边界、全局标准对照）
- 正文：`chapters/10-chrome-devtools.md`（691 行）
- 本机核验：Chrome 152.0.7977.83；Python 3.14.3；`http://127.0.0.1:8765` 已在听；Chromium `RequestTimingView.ts` 当前 Timing 文案

## 1. Coverage

禁止抽样。下列类型全部打开、全部判定；未检查必须为 0。

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 章内标题（不含模板围栏内标题） | 57 | 57 | 0 |
| 正文散文块（去围栏后空行分段） | 163 | 163 | 0 |
| 无序列表项 | 78 | 78 | 0 |
| 有序列表项 | 70 | 70 | 0 |
| 表格 | 6 | 6 | 0 |
| 代码围栏 | 3 | 3 | 0 |
| mermaid 图 | 1 | 1 | 0 |
| Linux/Shell 命令（含启动命令） | 1 | 1 | 0 |
| 快捷键/菜单路径 | 8 | 8 | 0 |
| SQL | 0 | 0 | 0 |
| HTTP 示例/路径 | 8 | 8 | 0 |
| 测试用例（逐步操作步骤） | 8 | 8 | 0 |
| Bug 示例 | 1（BUG-001） | 1 | 0 |
| 小练习题 | 10 | 10 | 0 |
| 小练习答案 | 10 | 10 | 0 |
| 章内书面实操 10-1（含模板字段与完成标准） | 1 | 1 | 0 |
| 常见错误 | 10 | 10 | 0 |
| 面试题 | 5 | 5 | 0 |
| 检查清单项 | 13 | 13 | 0 |
| 自测门槛 | 4 | 4 | 0 |
| 正文 Markdown 图片 | 9 | 9 | 0 |
| 示意图 HTML 源 | 3 | 3 | 0 |
| 正文 Markdown 链接 | 9 | 9 | 0 |
| 阶段测验 3 全 10 题（先独立作答；第 6–10 题为第 10 章主覆盖） | 10 | 10 | 0 |
| 全局/STATUS/旧审查（仅作线索后独立复核） | 已读 | 已读 | 0 |

单元清单（全部已检）：

1. 标题 + 一句话核心 + 重要级别 + 主案例定性
2. 这一章解决什么问题
3. 学习目标（10 条）
4. 前置知识
5. 场景导入 + mermaid
6. 安全边界句
7. 10.1 打开方式表 + 三面板图 + 三面板表 + Application 旁路
8. 10.2 功能名地图 + Command Menu + Disable cache 时效
9. 10.3 Elements
10. 10.4 Console
11. 10.5 Network 顺序与列
12. 10.6 请求定位
13. 10.7 Request/Response 子标签表 + 阅读纪律
14. 10.8 前后端假设表
15. 10.9 Preserve log
16. 10.10 Disable cache + Service Worker
17. 10.11 Copy as cURL + HAR sanitized
18. 10.12 网络限速 ⭐⭐ + Chrome 145 Request conditions
19. 10.13 Timing/TTFB 表 + 瀑布图
20. 10.14 登录定位 10 步
21. 10.15 慢加载定位 8 步
22. MiniShop 逐步操作 8 步 + 5 张页面图 + 1 张整理表
23. 工作实战模板 7 节 + 完成标准 5 条
24. 常见错误 1–10
25. 面试 5 题
26. 小练习 1–10 与答案
27. 检查清单 + 自测门槛
28. 总结 7 事 + 可运行性说明 + 参考资料 + 下一章预告 + 测验入口

未检查 = 0。Coverage 100%。

## 2. 总评分

| 项目 | 得分 |
| --- | ---: |
| 技术准确性 | 7/10 |
| 岗位实用性 | 8/10 |
| 完整性 | 7/10 |
| 初学者友好度 | 7/10 |
| 教学顺序 | 8/10 |
| 代码质量 | 9/10 |
| 实操质量 | 6/10 |
| 练习质量 | 8/10 |
| 图片质量 | 6/10 |
| **总体** | **73/100** |

评分口径：九项各 10 分，合计 66/90，按 100 分制折算 73。不沿用旧审 99/91。第 10 章不是质量标准里的核心章（5/8/12/13/14/16/19），但仍按「会不会把人教错、能不能在 Chrome 里找到东西」打。

分数被 ISSUE 支撑：无 P0；4 个 P1（Preserve log 演示对象、caption 串台、Timing 文案过时且与 Web Vitals TTFB 不等价、localhost 限速预期缺失）把技术准确性、实操、图片压下来。诚实边界（未拍面板、STATUS Incomplete）本身不扣「撒谎」分，但也不能当成已经练会面板。

Definition of Done（质量标准第八节，独立判定）：

| # | 检查项 | 结果 |
| ---: | --- | --- |
| 1 | 目标明确 | 通过。取证而非成为前端。 |
| 2 | 前置知识正确 | 通过。接 1–9 章报文与 Cookie/Token 头字段。 |
| 3 | 无知识性错误 | **不通过。** Timing 面板英文现文案不是 Waiting (TTFB)；MiniShop 登录不是整页跳转。 |
| 4 | 重要信息未过时 | **不通过。** 声称 2026-09-08 按官方 Network 参考核验，但该文档仍写 Waiting (TTFB)，Chromium 源码自 2022 已改为 Waiting for server response；本机 Chrome 152。 |
| 5 | 无错误绝对化 | 通过。未把 GET/POST 讲成加密；未把 Cookie/Session/Token 写成三选一；前后端只给假设。 |
| 6 | 术语准确 | **不通过。** 见 CH10-0003。 |
| 7 | 零基础能理解 | 有条件。缺第一眼线框；Preserve log 在主案例上「看起来没效果」。 |
| 8 | 示例具体 | 有条件。有真页面截图；04 看不出三个空格。 |
| 9 | 有实际工作场景 | 通过。登录失败取证、弱网拆 TTFB/下载。 |
| 10 | MiniShop 一致 | 有条件。`POST /api/login`、token + Set-Cookie、BUG-001、qty=11 与 PRD/实现一致；冻结仪式标明在第 19 章，符合全书口径。Preserve log 未映射到 `/admin.html`。 |
| 11 | 代码经过验证 | 不适用，满足。无课程内可执行 GUI 代码；HTTP 事实本机 curl 复核。 |
| 12 | SQL 操作安全 | 不适用，满足。 |
| 13 | 图表确实帮助理解 | **不通过。** 两张示意图 caption 串台。 |
| 14 | 知识重要级别明确 | 有条件。限速 ⭐⭐、HAR/单请求限速了解即可，诚实；Elements/Console 与 Network 同标 ⭐⭐⭐，实操却「有或没有都行」。 |
| 15 | 常见错误有价值 | 通过。十条都是岗位高频。 |
| 16 | 面试题不是死记硬背 | 通过。有边界。 |
| 17 | 练习覆盖目标 | 有条件。10 道概念题覆盖主线；10-1 完成标准有「无整页跳转」逃生门，但门槛 2 仍要求抓住会跳转的请求。 |
| 18 | 答案与练习对应 | 通过。独立作答后与标准答案一致，无 【ANSWER VERIFICATION FAILED】。 |
| 19 | 检查清单可验证能力 | **不通过。** 门槛 2 与 MiniShop 登录实现冲突。 |
| 20 | 能自然衔接下一章 | 通过。预告 Linux/`curl`，不提前讲完第 18 章性能。 |

**DoD：15/20。** 按质量标准：17 项及以下不得发布。

## 3. P0

无。教材没有假装拍过 DevTools 面板；没有教未授权注入；没有把 GET/POST 讲成安全神话；没有把 Cookie/Session/Token 写成三选一；第 19 章之前的路径标明教学实现/冻结仪式，未写成已冻结契约。

## 4. P1

见 CH10-0001、CH10-0002、CH10-0003、CH10-0004。

## 5. P2

见 CH10-0005 至 CH10-0009。

## 6. P3

见 CH10-0010 至 CH10-0016。

## 7. 逐段问题

### 标题 / 一句话核心 / 级别 / 主案例

原文：「DevTools 把浏览器里已经发生的观察打开给你看。」「⭐⭐⭐」「MiniShop 个人软件测试实践项目」。

判定：核心句能当过滤器，能丢掉「成为前端」和「用限速制定 SLA」。主案例定性正确。无 ISSUE。

### 这一章解决什么问题（L8–14）

技术内容正确：第 9 章会读报文，本章打开浏览器里的观察；界面会改、以功能名为准。开篇第二句把 TTFB、Preserve log、Disable cache、Copy as cURL 与三个抽屉并列倒完，见 CH10-0007。未把未拍面板写成已拍。

### 学习目标（L16–29）

十条与后文对应。第 7 条「在会跳转的流程中使用 Preserve log」本身正确，但后文主案例并不跳转，见 CH10-0001。

### 前置知识（L31–36）

正式顺序 1–9、URL/GET/POST/状态码/头/体、Cookie 与 Token 头字段、需要本机 Chrome：正确。其他浏览器「类似工具、本章以 Chrome 为准」可接受。

### 场景导入（L38–61）

缺陷对比正确：无工具只能写「登录失败」；有 Network 可写 `POST /api/login`、401、无 Set-Cookie。路径明确「是 `/api/login`，不是 `/login`」。构建号标明教学示例。mermaid：先开 DevTools → Elements/Console/Network → 对照四格 → 缺陷或假设。安全句禁止未授权注入、拦截他人 Cookie、公开带密码 cURL：正确。

本机 curl 复核：错误密码 `401` + `{"result":"fail"}`、无 Set-Cookie；正确密码 `200` + token + `Set-Cookie: minishop_session=…; HttpOnly; Path=/`。场景文案与实现一致。

### 10.1 打开 DevTools

快捷键对照 [Open Chrome DevTools](https://developer.chrome.com/docs/devtools/open) 与 [Keyboard shortcuts](https://developer.chrome.com/docs/devtools/shortcuts)：

| 教材 | 官方 | 判定 |
| --- | --- | --- |
| Win/Linux `F12` / `Ctrl+Shift+I` | 是 | 通过 |
| macOS `Cmd+Option+I` | 是 | 通过 |
| Win `Ctrl+Shift+C` | 是 | 通过 |
| macOS `Cmd+Option+C` | 官方「打开 Elements」同时列 `Cmd+Shift+C` **或** `Cmd+Option+C` | 未写全，CH10-0015 |
| 菜单 Win「更多工具 → 开发者工具」；macOS「视图 → 开发者 → 开发者工具」 | 是 | 通过 |

停靠位置说明正确。三面板表（Elements/Console/Network 各回答/不回答什么）正确。Application 观察 HttpOnly Cookie：正确，且标明非大纲主面板。缺「打开后第一眼看哪」，见 CH10-0006。

### 10.2 界面会变

Preserve log / Disable cache / Copy as cURL / throttling / Timing 作为「要完成的事」：正确。Command Menu 须先聚焦 DevTools：正确（macOS 未聚焦时 `Cmd+Shift+P` 是打印）。Command Menu 实际命令名是 Keep log…，见 CH10-0010。Disable cache 关掉 DevTools 后通常恢复：与官方 “Disable cache (while DevTools is open)” 及 Chromium 命令 `Disable cache while DevTools is open` 一致。

### 10.3 Elements

源代码 ≠ 当前 DOM；检查 button/a/div、disabled/hidden/CSS 挡住、搜索文本；临时改 DOM 只是假设验证、刷新消失：全部正确。`index.html` 的 `#login-msg` 初始为空，「登录失败」由 `app.js` 写入：与练习 3 同类事实。无章内 30 秒操作，见 CH10-0005。

### 10.4 Console

红/黄级别、CORS ≠ 没接口、混合内容、禁止粘贴来路不明脚本、有报错≠根因：正确。MiniShop 是 `http://127.0.0.1` 同源，课程站点上通常看不到 CORS/混合内容，正文当通用清单可接受。无章内 30 秒操作，见 CH10-0005。

### 10.5 Network

「先开面板、勾选、清空、再操作」是岗位正确顺序。列名 Name/Method/Status/Type/Size/Time 仍是 Network 默认列。「打开一个页面 ≠ 一次网络请求」接第 7 章，正确。Type 列写成 `js、css、img` 混用了过滤按钮名与 Type 值，见 CH10-0013。第 2 步就要勾 Preserve log / Disable cache，含义到 10.9/10.10 才讲，见 CH10-0007。

### 10.6 请求定位

Fetch/XHR、Doc 过滤名与 [Network features reference](https://developer.chrome.com/docs/devtools/network/reference) 一致。路径片段 `login`/`products`/`cart`、看 Method 与时机、30x 后一条：正确。找不到 POST 的四条原因（没先开、没 Preserve log、前端校验没发出、过滤太窄）：正确。MiniShop 登录表单有 `required`，空提交会被浏览器拦住、请求不发出，这条用得上。

### 10.7 Request 与 Response

官方子标签仍是 Headers、Payload、Preview、Response、Timing、Cookies；General 在 Headers 里。教材写「Payload 或 Request（以当前标签名为准）」是合理对冲。阅读纪律（200 仍看 Body、Preview vs Response、截图脱敏、HttpOnly 在 Elements 里看不见）：正确。把第 8/9 章层次放回面板：正确。

### 10.8 前后端问题

七行观察→待验证方向→不能说死：正确，尤其 CORS 与 TTFB≠一定是数据库。示例缺陷句符合第 6 章证据风格。无 ISSUE。

### 10.9 Preserve log

默认导航/刷新清空列表、勾选后跨导航保留、测完关掉以免列表膨胀：与官方 “Save requests across page loads / Preserve log” 一致。SPA 句「对整页跳转最关键」正确，但**没有**写明 MiniShop v1.0 登录只是 `hidden` 切换，见 CH10-0001。图 caption 串台见 CH10-0002。

### 10.10 Disable cache

模拟首次访问、旧资源掩盖缺陷、真实用户可能有缓存、通常仅当前已开 DevTools 的标签页、Service Worker / `from ServiceWorker`：正确。措辞「不会自动等于 Disable cache 对整个操作系统生效」见 CH10-0012。

### 10.11 Copy as cURL

右键 Copy → Copy as cURL 会带 URL/方法/头/Cookie：正确。脱敏四步、bash vs cmd、只复现这一次 HTTP 而非渲染/TLS 全现场：正确。官方还列 Copy as PowerShell / Copy as fetch，见 CH10-0011。HAR：官方默认 **Export HAR (sanitized)**，去掉 Cookie / Set-Cookie / Authorization；教材要求选 sanitized 且仍人工查密码/Token：正确（sanitized 不管 JSON 体里的密码）。

### 10.12 网络限速 ⭐⭐

官方预设现为 Fast 4G / Slow 4G / 3G 等，教材写「例如 3G、Slow 4G」「名称以当前列表为准」：正确。近似而非基站、限速扭曲绝对值、默认整页而非单资源、Chrome 145+ Request conditions 了解即可：与 [Throttle individual network requests](https://developer.chrome.com/blog/throttle-individual-network-requests)（Chrome 145，2025-12-12 / 2026-01-16）一致。禁止私自规定 200 ms：正确，把阈值推给第 3、18 章。星级诚实。

### 10.13 Timing 与 TTFB

阶段表 Queueing/Stalled、DNS/建连/TLS、Waiting、Content Download 的**含义**与官方阶段解释一致。瀑布图、不要把每条长条写成同一个 Bug、缺陷应写 URL/大约值/是否限速/是否 Disable cache/是否可复现：岗位正确。

问题：教材把面板文案钉死为 **Waiting (TTFB)**，并声称按 2026-09-08 官方文档核验。官方文档确实仍写 Waiting (TTFB)（页面 Last updated 2024-07-16），但 Chromium 源码 2022-05-03 已改为 **Waiting for server response**，理由正是「this timing isn't congruent with the TTFB metric」。当前 `RequestTimingView.ts` 仍是该字符串。本机 Chrome 152。见 CH10-0003。图 caption 串台见 CH10-0002。

### 10.14 MiniShop 登录定位

「当前实现登录就是 `POST /api/login`；冻结仪式在第 19 章」符合全书口径（第 19 章前不得写成已冻结契约），**不是**问题。10 步顺序正确。第 3 步勾 Preserve log 在 MiniShop 登录上看不到「POST 被清空」，见 CH10-0001。第 9 步「随后落地请求是否带 Cookie 或 Authorization」：登录成功后 `refreshProducts()` 的 `GET /api/products` **不带** Authorization；`refreshCart()` 的 `GET /api/cart` 带 Bearer；同源 fetch 默认会带 Cookie。教材用「或」可接受，但零基础可能点错行。

### 10.15 MiniShop 慢加载定位

步骤完整，禁止把限速毫秒写成 MiniShop SLA：正确。缺 localhost 预期，见 CH10-0004。本机对 `/api/login` 测得约 5.6 ms 到达首字节、下载可忽略：印证「本机 TTFB 常常仍然短」。

### MiniShop 逐步操作（本机已跑通）

标题下第一段明确：审查环境未能截取 **DevTools 面板本身**；仓库是页面截图和请求记录；读者必须自己打开 DevTools。与 `practice/STATUS.md`「10-1 Incomplete：没有 DevTools 面板本身的截图」、根 README 诚实边界一致。**未假装已拍摄。** 启动命令 `cd project/minishop && python3 run.py serve` 与 `project/minishop/run.py` 一致。

逐步 1–5、7 与实现/证据一致。逐步 6「三个空格」截图无法证明输入，见 CH10-0008。逐步 6–7 重复第 5/8 章缺陷，冲淡本章技能，见 CH10-0009。全程未打开 Elements/Console，见 CH10-0005。未用「后台」做真导航，见 CH10-0001。

### MiniShop 工作实战：DevTools 取证包

产出路径 `exercises/chapter-10-minishop-devtools.md`、模板字段、完成标准可判断对错。完成标准第 1 条允许「或证明无整页跳转」——这是逃生门，10-1 **可以**交。与门槛 2、10.9 主叙事不一致，见 CH10-0001。类型图标 📖 只在 `practice/README.md`，章内未标，见 CH10-0014。禁止未脱敏 HAR/cURL、禁止打第三方当靶场：正确。

### 常见错误 1–10

十条均正确，且与 10.5–10.12 对应。错误 2 默认「跳转后找不到 POST」在 MiniShop 登录上较少发生，见 CH10-0001。错误 8 与 10.12 一致。无单独知识性错误。

### 面试角度

五题均「结论 → 原理/示例 → 边界」。Preserve log vs Disable cache 区分正确。TTFB 定义跟官方文档走，面板文案问题同 CH10-0003。Copy as cURL 边界「cURL 成功 ≠ 页面渲染成功」正确。

### 小练习 / 答案 / 清单 / 总结 / 可运行性 / 参考资料 / 预告

见第 11 节。参考资料四条 Chrome 链接均存在且主题匹配；章内链 07/08/09、质量标准、阶段测验 3：正确。下一章 Linux 不抢戏。可运行性说明再次承认未截取面板 UI：诚实。Waiting (TTFB) 核验日期问题见 CH10-0003。

## 8. 代码问题

本章无 Python/SQL/pytest。三块围栏：

1. mermaid flowchart：语法有效，命题正确（先开再操作，三抽屉，对照四格）。
2. `exercises/chapter-10-minishop-devtools.md` 路径：与 `exercises/README.md` 约定一致。
3. 取证模板：字段完整，明确不要贴密码，cURL 两行确认脱敏与授权环境。

无 CODE 类 P0/P1。Copy as cURL 示例在练习 6 用 `session_demo=…` 省略号，不是可运行命令，教学用途可接受。

本机可运行命令：`cd project/minishop && python3 run.py serve`。审计时 8765 已有进程在听，未二次抢端口。curl 结果见第 18 节。

## 9. 图片问题

九张 PNG 均用 `read_file` 打开；三张 HTML 源均打开。结论见下。无 DevTools 面板截图——这是作者声明的负结果，**KEEP 诚实边界，不要为了分数伪造面板图。**

### IMG-CH10-001

文件：`chapters/assets/diagrams/ch10-three-panels.png` + `.html`  
出现位置：10.1 三面板表前  
图片主要内容：同一句「登录失败」对应 Elements / Console / Network 三个抽屉。  
技术准确性：正确（CORS ≠ 没接口；401 vs 没发出；临时 DOM ≠ 修复）。  
与正文一致性：与 10.1/10.3/10.4/10.8 一致。  
文字是否正确：是。  
UI 是否过时：示意图不是 Chrome 皮肤，不适用。  
教学价值：高，章的主命题。  
可读性：三列卡片清楚；下方大片留白。  
是否需要修改：可选补第一眼线框（CH10-0006），本图命题可留。  
最终结论：**KEEP**

### IMG-CH10-002

文件：`chapters/assets/diagrams/ch10-two-switches.png` + `.html`  
出现位置：10.9 Preserve log  
图片主要内容：标题/卡片在讲 Preserve log vs Disable cache。  
技术准确性：卡片正文正确。  
与正文一致性：标题与 10.9/10.10 一致。  
文字是否正确：**caption 在讲 Copy as cURL 脱敏**，与本图命题无关。  
UI 是否过时：不适用。  
教学价值：命题对，caption 破坏。  
可读性：两列清楚。  
是否需要修改：是。  
最终结论：**MODIFY**（CH10-0002）

### IMG-CH10-003

文件：`chapters/assets/diagrams/ch10-ttfb.png` + `.html`  
出现位置：10.13 Timing 与 TTFB  
图片主要内容：Waiting/TTFB 与下载两色条。  
技术准确性：两段拆分正确；lead 不要把限速当 SLA 正确。条上仍写 Waiting / TTFB，与现行面板文案不完全同字，见 CH10-0003。  
与正文一致性：标题与 10.13 一致。  
文字是否正确：**caption 在讲 Preserve log / Disable cache**，串台。  
UI 是否过时：条目标签 Waiting/TTFB 相对现行「Waiting for server response」偏旧。  
教学价值：命题对，caption 破坏。  
可读性：比例条直观。  
是否需要修改：是。  
最终结论：**MODIFY**（CH10-0002，并建议条目标签加现行文案）

### IMG-CH10-004

文件：`chapters/assets/01-login.png`  
出现位置：逐步操作第 3 步  
图片主要内容：MiniShop 登录+注册页，注明个人实践项目 v1.0。  
技术准确性：与 `frontend/index.html` 一致。  
与正文一致性：是。  
文字是否正确：是。  
UI 是否过时：这是课程页面，不是 Chrome UI。  
教学价值：给零基础第一帧。  
可读性：好。  
最终结论：**KEEP**

### IMG-CH10-005

文件：`chapters/assets/02-login-fail.png`  
出现位置：逐步操作第 4 步  
图片主要内容：手机号 13800138000、密码已填、文案「登录失败」。  
技术准确性：与错误密码路径一致。密码以圆点显示，未泄露。  
与正文一致性：是。  
教学价值：页面现象；**不是** Network 401 的证据，正文已要求读者自己看面板。  
最终结论：**KEEP**

### IMG-CH10-006

文件：`chapters/assets/03-shop.png`  
出现位置：逐步操作第 5 步  
图片主要内容：登录后商品区，当前用户 13800138000 (user)，有「后台」链接，三件商品，购物车 qty=1。  
技术准确性：与实现一致。后台链到 `/admin.html`，正文从未用它演示 Preserve log。  
最终结论：**KEEP**（链接本身不是错；缺使用说明见 CH10-0001）

### IMG-CH10-007

文件：`chapters/assets/04-search-empty-bug001.png`  
出现位置：逐步操作第 6 步  
图片主要内容：商品「共 3 件」，关键字框看起来为空。  
技术准确性：BUG-001 真实（本机 `keyword=%20%20%20` 仍 3 件）。**截图不能区分空、三空格、未搜索。** 与 03 几乎同构图。  
最终结论：**MODIFY 或 REPLACE**（CH10-0008）

### IMG-CH10-008

文件：`chapters/assets/05-cart-qty-11.png`  
出现位置：逐步操作第 7 步  
图片主要内容：数量 11，「qty exceeds stock」，列表仍 qty=1 不是 11。  
技术准确性：与 `POST /api/cart/items` 400 及 R-CART-10 一致。  
最终结论：**KEEP**（内容对；是否应出现在 DevTools 章见 CH10-0009）

### IMG-CH10-009

文件：`chapters/assets/08-network-log.png`（同源 `project/minishop/evidence/http/network-log.html`）  
出现位置：逐步操作第 8 步  
图片主要内容：整理后的请求表，标题写明「不是 Chrome DevTools 面板截图」，token/Cookie 已打码。  
技术准确性：本机 curl 复核登录 200/401、空关键字 3 件、qty=11 400，与表一致。  
诚实性：高。  
最终结论：**KEEP**

## 10. 表格问题

| 表 | 位置 | 判定 |
| --- | --- | --- |
| 打开方式 | 10.1 | 基本正确；macOS 检查元素快捷键未列 `Cmd+Shift+C`（CH10-0015） |
| 三面板回答/不回答 | 10.1 | 正确 |
| Network 列 | 10.5 | 列名正确；Type 值略混（CH10-0013） |
| 你要找的东西 / 通常在哪 | 10.7 | 正确；Payload 或 Request 的对冲合适 |
| 前后端观察 | 10.8 | 正确，无绝对化 |
| Timing 阶段 | 10.13 | 阶段含义正确；Waiting (TTFB) 作为**面板标签**过时（CH10-0003） |

无表格内 MiniShop 字段与 PRD 冲突。`{"success":false}` 只出现在练习 5，是教学反例，不是 MiniShop 契约（实现是 `result`）。

## 11. 练习与答案问题

### 11.1 独立作答（先于对答案）

**练习 1**  
独立：Network 只记录打开之后的请求；先点登录，POST 可能已经结束。  
教材：否则请求可能在打开面板前已经完成。  
比较：一致。

**练习 2**  
独立：Preserve log。默认导航清空列表。  
教材：Preserve log。跳转默认清空。  
比较：对这道「假设会跳转」的题一致。MiniShop 主路径并不跳转，题干没有说 MiniShop，故**不**判 【ANSWER VERIFICATION FAILED】。教学风险归 CH10-0001。

**练习 3**  
独立：文案由脚本写入 DOM；不能断言后端没返回库存，应看数据请求 Response。  
教材：同。  
比较：一致。`index.html` 无「登录失败」字符串，同类事实成立。

**练习 4**  
独立：B。  
教材：B。A/C/D 夸大范围。  
比较：一致。

**练习 5**  
独立：把协议成功当成业务成功。  
教材：必须打开 Response/Preview。  
比较：一致。

**练习 6**  
独立：删 Cookie/Token/密码；确认测试 URL。不能证明按钮绑定/渲染。  
教材：同。  
比较：一致。

**练习 7**  
独立：更像体积/带宽导致的下载慢，不是该接口服务端计算慢。记限速预设、Disable cache、URL/类型、可复现性。  
教材：同。  
比较：一致。localhost 特款见 CH10-0004，本题未指定 MiniShop，不判答案错。

**练习 8**  
独立：假设一脚本在发请求前出错；假设二按钮未绑定或客户端校验拦住。没有对应请求就不能说后端挂了。  
教材：同。  
比较：一致。

**练习 9**  
独立：浏览器按 CORS 未把响应交给脚本；Network 已是 200。记 URL、状态码、Console 原文。  
教材：同。  
比较：一致。

**练习 10**  
独立：打开登录页 → 打开 Network → 勾选 Preserve log（及按需 Disable cache）→ 清空 → 提交 → 筛出登录请求 → 记方法、状态码、是否 Set-Cookie。  
教材：示例等价步骤。  
比较：一致。

无 【ANSWER VERIFICATION FAILED】。

### 11.2 书面 10-1 独立作答（评估可操作性）

按模板独立填写。GUI 面板未在本审计会话用 Playwright 点击（仓库无 Playwright 依赖）；HTTP 与 DOM 事实已用 curl + 源码复核。Chrome 152 已安装。

```markdown
# MiniShop DevTools 取证记录（审计员独立作答）

## 环境
- 站点：http://127.0.0.1:8765 （本机已有 serve）
- 构建/版本：MiniShop v1.0 当前实现；冻结仪式在第 19 章
- Chrome 版本：152.0.7977.83
- 视口：审计未驱动 GUI 视口
- Preserve log：登录主路径无整页跳转，勾不勾列表通常都还在
- Disable cache：建议开；本记录 HTTP 侧用 curl，不走浏览器缓存
- 限速预设：无（curl）；见慢加载预期
- 日期：2026-09-10

## 登录或提交
- 操作步骤：POST /api/login JSON `{phone, password}`（页面是表单 submit + fetch，非跳到 /login）
- 错误密码：POST /api/login → 401，Body `{"result":"fail"}`，无 Set-Cookie；页面 #login-msg 显示「登录失败」（源代码无此文案）
- 正确密码 Test1234：200，Body `{"result":"ok","token":"<redacted>","role":"user"}`，响应头 `Set-Cookie: minishop_session=<redacted>; HttpOnly; Path=/`
- 请求体类型：JSON（不要把密码写入缺陷）
- 跳转：无。`loginPanel.hidden=true; shopPanel.hidden=false`。后续 GET /api/products 无 Authorization；GET /api/cart 有 Bearer。同源 Cookie 仍可能带上。
- 页面结果：进入商品区，与 03-shop.png 同类

## 慢加载
- 页面：首页/商品区，本机 127.0.0.1
- 最长的 3 条：本记录未开 DevTools 限速。curl 登录 TTFB 约 5.6 ms，下载约 0 ms。
- 预期（若读者开 Slow 4G）：接口 TTFB 仍常短；被拉长的多半是文档/脚本/图片的 Content Download。不得写成 MiniShop 数据库慢或 SLA。
- 限速开/关对比：未在 GUI 完成。【操作缺口】教材 10.15 未写这条预期。

## Console / Elements
- Elements：登录按钮是 `<button type="submit" id="login-btn">`；「登录失败」在 #login-msg，查看源代码没有。
- Console：同源，预期无 CORS；错误密码路径无必要的 TypeError。没有红字就应写「无脚本错误」。
- 逐步操作一次都没要求打开这两个面板。

## 假设
- 更像前端：无对应请求 + Console TypeError（本次未发生）。
- 更像后端：401 + JSON fail 与页面「登录失败」一致，待核对账号规则（本次是错误密码，属预期失败不是缺陷）。
- 空搜索 200 仍三件：更像后端违反 R-SEARCH（BUG-001），前端只是原样展示。
- 下一步：空搜索对照 R-SEARCH；Preserve log 用「后台」`/admin.html` 做一次真文档导航对比。

## cURL
- 已删除 Cookie/Token/密码：是
- 仅用于授权环境：是
- 示例：`curl -X POST 'http://127.0.0.1:8765/api/login' -H 'Content-Type: application/json' -d '{"phone":"13800138000","password":"<redacted>"}'`
```

**可操作性结论：**

- 完成标准 5 条里，登录方法/状态码/登录态头、双方向假设、cURL 脱敏、慢加载区分 TTFB/下载（若读者真开了 Timing）都能做。
- 「Preserve log 的使用说明或证明无整页跳转」——细心读者可以写「无整页跳转」。粗心读者按 10.9/10.14/门槛 2 会以为开关坏了。
- 作者未提供面板截图：符合诚实证据，不构成 10-1 不可交；构成「仓库不能代替读者打开 Chrome」。
- 因此 10-1 **书面可交**，但 **Preserve log 与限速两条的主案例可操作性不足**（CH10-0001、CH10-0004）。

### 11.3 阶段测验 3（先独立作答）

覆盖 8/9/10 章。第 10 章主覆盖为 6–10；1–5 为第 8/9 章，仍独立作答以核验本章引用的口径。

| 题 | 独立答案 | 教材答案 | 比较 |
| ---: | --- | --- | --- |
| 1 | Cookie/Session/Token 层次不同，常配合，不是三种登录方式 | 同 | 一致 |
| 2 | HttpOnly 挡页面脚本读 Cookie，不挡浏览器自动带上 | 同 | 一致 |
| 3 | 不能。`required` 可被绕过 | 同 | 一致 |
| 4 | safe/幂等/可缓存是不同约束；不能说 GET 不安全、POST 安全 | 同 | 一致 |
| 5 | 401 未认证；403 已认证无权限。MiniShop：无 token 下单 401；普通用户 `/api/admin/*` 403 | 同 | 一致 |
| 6 | 先开 Network 否则请求已结束。Preserve log 避免导航清空列表 | 同 | 一致 |
| 7 | 先删 Cookie/Authorization/密码等凭证，只在授权环境复现 | 同 | 一致 |
| 8 | 等首字节，含往返与服务器准备；≠ 下载完成 | 同 | 一致（面板标签问题不在测验答案里） |
| 9 | JSON `token` + `Set-Cookie`（HttpOnly）。后续 Bearer | 同。本机 curl 证实 | 一致 |
| 10 | C。A/B/D 错 | C | 一致 |

必过题 1、4、7：独立能用自己的话解释，与答案一致。通过线按知识可过。第 6 题 Preserve log 是一般原理，不是 MiniShop 特款。

## 12. 初学者理解障碍

【Beginner Friction】

1. 打开 DevTools 可能停在上次的 Sources/Performance，没有「顶栏只找 Elements/Console/Network」的第一眼（CH10-0006）。
2. 10.5 就要勾两个开关，要到 10.9/10.10 才知道勾了会发生什么（CH10-0007）。
3. 按 10.9 演示勾 Preserve log 再登录，POST 还在，以为开关无效（CH10-0001）。截图 03 里「后台」是真导航入口，正文不说。
4. Timing 里找不到「Waiting (TTFB)」字样，找到「Waiting for server response」不敢认（CH10-0003）。中文界面【External Verification Required】可能是「等待服务器响应」。
5. Elements/Console 标 ⭐⭐⭐，逐步操作一次不打开，取证包又写「有或明确没有」（CH10-0005）。
6. 开篇功能名清单超过最小例子（CH10-0007）。
7. Command Menu 搜 “Preserve log” 能因 tag `preserve` 命中，但列表显示 “Keep log on page reload / navigation”，零基础会对不上（CH10-0010）。
8. 04 截图与 03 几乎一样，「三个空格」看不见（CH10-0008）。

## 13. 岗位能力缺口

【Job Reality Gap】

1. 真实项目大量 SPA：Preserve log 不是每次登录的关键开关，过滤器 + 操作时机才是。教材把「登录成功跳首页」写成默认故事，和新手站的 SPA 现状相反。
2. Chrome Timing 的 Waiting 阶段 ≠ web.dev / CrUX TTFB（后者含跳转、DNS、连接、TLS）。Chrome 2022 改名就是为了消这个歧义。教材仍用 Waiting (TTFB) 当面板名，入职后对 Lighthouse/RUM 会对不上（CH10-0003）。
3. 初级岗位日常：Application 看 Cookie、Disable cache + 硬刷新、Copy as cURL 给开发、HAR 默认 sanitized。这些有讲。缺：Network 过滤属性（`status-code:`、`domain:`）、Initiator、重放 XHR、Override、Issues 面板——了解即可即可，不升格为 P1。
4. 限速是 request-level 近似，Lighthouse 用另一套校准值。教材已说不能当 SLA，够初级。缺 localhost 预期会让人编造后端慢（CH10-0004）。
5. Copy as cURL 在 Windows 还有 cmd 注入史（Chromium 已修）；岗位上应优先 bash 形式并脱敏。教材方向对，未提 PowerShell（CH10-0011）。

## 14. 建议删除内容

- 不要删除诚实声明（未拍面板、08-network-log 非皮肤）。
- 不要为分数补拍伪造的 DevTools 皮肤。
- 逐步操作第 6–7 步（空搜索 / qty=11）建议从本章主路径拿掉或压成「可选对照第 5/8 章」，避免冲淡 Network 技能（CH10-0009）。不是知识错误。
- 不要删「冻结仪式在第 19 章」。那是全书口径，旧复审建议删掉会与 `AUDIT_AGENT_BRIEF` MiniShop 规则冲突。

## 15. 建议新增内容

1. 10.1 后：功能名级第一眼（顶栏三标签 / 列表上方两勾选 / 点行后 Headers·Response·Timing）。示意图可新建 `ch10-first-look`，不要画真实皮肤。
2. 10.9 与 10.14：写明 v1.0 登录是 `hidden` 切换；用「后台」`/admin.html` 做 Preserve log 勾/不勾对比。
3. 10.3 / 10.4 末与逐步操作：错误密码后各 30 秒——检查「登录失败」在 DOM；Console 有无红字（没有就写没有）。
4. 10.13 / 10.15：面板文案 **Waiting for server response**（旧称 Waiting (TTFB)）；该阶段不含 DNS/建连/TLS；≠ Web Vitals TTFB。localhost 限速预期：TTFB 仍常短，拉长的多半是下载。
5. 10.2 Command Menu：搜 `preserve` / `Disable cache`；列表可能显示 Keep log… / Disable cache while DevTools is open。

## 16. 建议重写内容

- 开篇只留三个抽屉；开关与 TTFB 放到 10.2 地图（CH10-0007）。
- `ch10-ttfb.html` / `ch10-two-switches.html` 的 `<p class="caption">` 改回本题，并按 diagrams README 重截 PNG（CH10-0002）。
- 10.13 表第一列改为「Waiting for server response（文档仍可能写 Waiting (TTFB)）」或等价对冲，与 10.2「以功能名为准、文案会变」的原则对齐（CH10-0003）。
- 门槛 2 改为：要么在 `/admin.html` 真导航下抓住登录 POST，要么书面证明本次无整页跳转（与 10-1 完成标准对齐）（CH10-0001）。

## 17. 本章结论

**C 明显需要修改**

不是 E：主线（先开再操作、三抽屉、两开关不是一件事、200 仍看 Body、cURL 脱敏、限速≠SLA、前后端只给假设、未拍面板诚实）是对的，能改。  
不是 B：四个 P1 会让零基础在 Chrome 152 的 Timing 上找错字、在 MiniShop 上误判 Preserve log、在 localhost 限速下编造后端慢，且 DoD 15/20。  
达到作者发布线 90/100：**否**（本审计 73/100）。旧审 99/91 不能作为当前成绩。

优先修改顺序：CH10-0003（Timing 文案）→ CH10-0001（Preserve log 映射到 `/admin.html`）→ CH10-0002（caption）→ CH10-0004（localhost 预期）→ P2 第一眼与 Elements/Console 微操作。

## ISSUE 清单

## ISSUE
ID：CH10-0001
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.9 Preserve log；10.14；MiniShop 逐步操作；自测门槛 2；错误 2；面试「Preserve log」示例
精确位置：L241–252；L357–367；L392–393；L651；L497–499；L547–548
原文：「默认情况下，导航或刷新会清空 Network 列表。登录成功后常发生跳转，**登录那条 POST 会消失**。」「勾选 Preserve log」；门槛「在授权站点亲手完成一次：Preserve log 下抓住会跳转的请求」
问题等级：P1
问题类别：PED / TEST / SEQ
问题说明：MiniShop v1.0 登录成功执行 `loginPanel.hidden = true; shopPanel.hidden = false`，没有文档导航。未勾 Preserve log 时登录 POST 通常仍在列表里。读者按 10.14/逐步操作勾上开关，看不到「POST 消失」，容易认为开关无效。商品区已有 `<a href="/admin.html">后台</a>`，那才是一次真导航。10-1 完成标准有「或证明无整页跳转」逃生门，但门槛 2 没有。
为什么有问题：主案例与要教的现象错配，属于会把操作学错，不是用词偏好。
依据：`project/minishop/frontend/app.js` L47–56；`index.html` L52–53；Chrome 官方 Preserve log 只对 page loads/navigation 清列表生效。
建议修改：写明同页 `hidden` 切换；用「后台」做勾/不勾对比；门槛 2 与 10-1 完成标准对齐。
推荐替换文本：
「MiniShop v1.0 登录成功只是把登录区隐藏、商品区显示，**不是整页跳转**。因此即使用户没勾 Preserve log，登录 POST 通常还在列表里。不要据此认为这个开关没用。
要亲眼看到「导航清空列表」：登录后点「后台」进入 `/admin.html`。对比未勾选时登录 POST 消失、勾选后还在。若只测登录、不点后台，就写『本次无整页跳转，Preserve log 未改变列表』。」

## ISSUE
ID：CH10-0002
文件：chapters/assets/diagrams/ch10-ttfb.html；ch10-two-switches.html（及对应 png）
章节：第 10 章
小节：10.9 图注；10.13 图注
精确位置：各文件 `<p class="caption">`；正文 L239、L325
原文：
- ch10-ttfb caption：「Preserve log 保住跳转前的请求；Disable cache 通常只在 DevTools 打开时生效。」
- ch10-two-switches caption：「Copy as cURL 会带上 Cookie 和密码，保存前必须脱敏。」
问题等级：P1
问题类别：IMG / PED
问题说明：两张图的标题/卡片命题正确，脚注互相串到下一课。读者会以为 TTFB 图在讲开关、开关图在讲 cURL。
为什么有问题：示意图的 caption 是读者第一眼的结论句，串台等于教错这张图要记住什么。
依据：质量标准「图表确实帮助理解」；两张 HTML 的 `<h1>` 与 caption 不一致。
建议修改：caption 改回与 `<h1>` 同一命题，按 `chapters/assets/diagrams/README.md` 重截 png。
推荐替换文本：
- ch10-ttfb：`示意图：Waiting for server response（旧文档称 Waiting (TTFB)）是等第一字节；后面才是把正文传完。限速下的毫秒不能当线上 SLA。`
- ch10-two-switches：`示意图：Preserve log 管列表会不会被导航清空；Disable cache 管这次排障要不要用本地缓存演戏。两个开关不是同一件事。`

## ISSUE
ID：CH10-0003
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.2；10.13；面试「什么是 TTFB」；可运行性说明
精确位置：L100；L329–337；L557–561；L670
原文：「**Timing** 中的 **Waiting (TTFB)**」；「Chrome 文档把 **Waiting (TTFB)** 解释为……」；「功能名称依据……Waiting (TTFB) 于 2026-09-08 核验」
问题等级：P1
问题类别：TERM / ACC
问题说明：官方 Network 参考仍写 Waiting (TTFB)（页面 Last updated 2024-07-16）。Chromium `RequestTimingView.ts` 在 2022-05-03 已把 UI 字符串改为 `Waiting for server response`，commit message：「The timing here isn't congruent with the TTFB metric」。当前 main 仍是该字符串。审计本机 Chrome 152.0.7977.83。该阶段也不含 DNS/建连/TLS（那些在 Timing 里单独列出）；web.dev TTFB 从导航开始算，包含这些。教材把面板名钉死为 Waiting (TTFB)，零基础在 152 里按字搜会找不到。
为什么有问题：这是 ⭐⭐⭐ 操作章，读者必须在面板里认出阶段。跟过时文档不跟现行 UI，违反本章自己「以功能名为准、文案会变」的原则，也违反质量标准「重要信息未过时」。
依据：https://chromium.googlesource.com/devtools/devtools-frontend.git/+/a062a6afd7adbad75b099c7e2321e49f96a409b7 ；当前 https://chromium.googlesource.com/devtools/devtools-frontend/+/refs/heads/main/front_end/panels/network/RequestTimingView.ts （`waitingTtfb: 'Waiting for server response'`）；web.dev TTFB 定义。中文 UI 精确译文 【External Verification Required】。
建议修改：主文案改为现行 UI 字符串，括号注明文档旧称与 Web Vitals TTFB 不是同一段尺子。
推荐替换文本：
「打开请求的 **Timing**（时序）。现行 Chrome 英文 UI 把等待首字节这一段标成 **Waiting for server response**（官方文档和旧版本仍可能写 **Waiting (TTFB)**）。它包含一次已建立连接之后的往返，以及服务器准备响应的时间；**不含** 上面单独列出的 DNS、建连、TLS。这与 web.dev/CrUX 的页面 TTFB（从开始导航算到首字节）不是同一把尺子。限速下的绝对值不能当生产 SLA。」

## ISSUE
ID：CH10-0004
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.15 MiniShop 慢加载定位
精确位置：L371–384（步骤 8 之后）
原文：「不要把限速下的绝对毫秒写成 MiniShop 的正式性能指标。……本章产出的是**定位证据**」
问题等级：P1
问题类别：PED / TEST / EX
问题说明：禁止当 SLA 是对的，但没写本机 `127.0.0.1` 上即使开较慢预设，接口 TTFB 也常常仍然短，被拉长的多半是图片/脚本下载。本机 curl 登录约 5.6 ms 首字节。读者按「区分 TTFB 与下载」若看到接口 TTFB 短，可能编造「数据库慢」或「接口不合格」来凑取证包。
为什么有问题：10-1 强制产出慢加载记录；错误预期会生成假缺陷。
依据：本机实测；Chrome 限速是 request-level 近似（Lighthouse throttling.md）；MiniShop 无慢接口、无 SLA。
建议修改：补预期记法，禁止把限速毫秒写成 MiniShop 缺陷。
推荐替换文本：
「本机 `127.0.0.1` 上即使开了较慢限速，接口 Waiting 也常常仍然短，被拉长的多半是图片或脚本的 Content Download。这正好说明限速卡的是传输，不是 MiniShop 的算法。记录写『Waiting 短、下载长』即可。不要把限速下的绝对毫秒写成 MiniShop 性能缺陷，也不要编造数据库慢。三条最长的都是文档或接口且 Waiting 仍短，也据实写。」

## ISSUE
ID：CH10-0005
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.3；10.4；逐步操作；取证包第 3 条
精确位置：L108–137；L388–416；L430
原文：Elements/Console 标 ⭐⭐⭐；取证包「一条 Console 或 Elements 补充证据（有或明确没有）」；逐步操作只走 Network。
问题等级：P2
问题类别：PED / EX
问题说明：与 Network 同级必须掌握，但章内零微操作。读者会认为「打开过 Network 就算会 Elements/Console」。
为什么有问题：星级不诚实，技能没有落地。
依据：质量标准「每个重要知识点至少回答怎么使用」；逐步操作 8 步无 Elements/Console。
建议修改：错误密码后各做 30 秒；逐步操作第 4 步后增加切 Console、检查「登录失败」在 DOM。
推荐替换文本：见第 15 节第 3 条。

## ISSUE
ID：CH10-0006
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.1 三面板表后；逐步操作第 2 步
精确位置：L75–86；L393
原文：打开后停靠位置说明；「切到 Network」，无顶栏/工具条/子标签的第一眼结构。
问题等级：P2
问题类别：PED / IMG
问题说明：功能名稳定，但零基础打开后可能停在 Sources/Performance。Command Menu 是退路，不能代替第一眼。作者未拍面板是诚实的，可用线框而不是皮肤。
为什么有问题：工具章缺「打开后手往哪放」。
依据：官方 Open DevTools：上次用的面板会被记住。
建议修改：补功能名级线框或等价三条文字。
推荐替换文本：
「打开后先看顶上一排**功能名**，不要追图标坐标。这一眼里只找三块：1. 顶栏 Elements、Console、Network（中间可能夹着 Sources、Performance，先忽略）；2. 点 Network 后，列表上方 Preserve log、Disable cache；3. 点一条后出现 Headers / Response / Timing。」

## ISSUE
ID：CH10-0007
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：这一章解决什么问题；10.5
精确位置：L10–12；L143–148
原文：开篇并列 Elements/Console/Network/Preserve log/Disable cache/Copy as cURL/限速/TTFB；10.5 第 2 步「勾选需要的 Preserve log、Disable cache」。
问题等级：P2
问题类别：SEQ / PED
问题说明：最小例子之前功能名过载；开关在会用之后才解释。
为什么有问题：坡度在 Network 内部是对的，章首和 10.5 提前透支。
依据：质量标准解释顺序；教学审查 P10-06（独立复核后同意，不照抄分数）。
建议修改：开篇只留三个抽屉；10.5 可写「先勾上，含义见 10.9/10.10」。
推荐替换文本：
「本章用 Chrome DevTools 把页面现象还原成证据。先掌握三个抽屉：Elements 看当前页面、Console 看脚本报错、Network 看发出的请求。Preserve log、Disable cache、Copy as cURL 和『慢在等还是慢在下载』放到 Network 里学，不要开篇就当操作清单。」

## ISSUE
ID：CH10-0008
文件：chapters/10-chrome-devtools.md ；chapters/assets/04-search-empty-bug001.png
章节：第 10 章
小节：MiniShop 逐步操作第 6 步
精确位置：L406–408
原文：「搜索框输入三个空格并搜索。……本机实现仍返回三件，记 BUG-001」配 04 图。
问题等级：P2
问题类别：IMG / EX
问题说明：关键字框在图上看起来为空；与 03-shop.png 几乎同构图。HTTP 证据 `keyword=%20%20%20` 是真的，但**这张页图证明不了**「三个空格」。空与三空格在 BUG-001 下都会全量返回，图更容易被读成「刚登录的商品列表」。
为什么有问题：逐步操作声称用截图证明输入，证明力不足。
依据：对 03 与 04 的实际看图；`evidence/http/03-products-empty-keyword.txt`。
建议修改：图上让关键字可见（例如「   」旁加说明「三空格」），或改文案为「空/空白关键字（图上可能看不出空格，以 Network 的 `keyword=` 为准）」。
推荐替换文本：「搜索框输入三个空格并搜索。以 Network 里 `GET /api/products?keyword=%20%20%20` 为准——页面截图看不出空格。按 R-SEARCH 不应全量；本机仍返回三件，记 BUG-001。」

## ISSUE
ID：CH10-0009
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：MiniShop 逐步操作第 6–7 步
精确位置：L406–412
原文：空搜索 BUG-001；qty=11 → 400 `qty exceeds stock`
问题等级：P2
问题类别：PED / SEQ
问题说明：两条是第 5/8 章已练过的判定，不是 DevTools 新技能。放在「本机已跑通」主路径里，读者会以为本章验收的是再抓一次 BUG-001。
为什么有问题：冲淡「先开 Network、读 Timing、脱敏 cURL」。
依据：学习目标无「再次证明 BUG-001」；10-1 完成标准也不以 BUG-001 为必交。
建议修改：改为可选「对照第 5、8 章」或移到取证包附录。
推荐替换文本：「（可选，对照第 5/8 章）空搜索与 qty=11 的页面现象应能在 Network 里对上 `GET /api/products` 与 `POST /api/cart/items`。本章验收不依赖这两条缺陷，重点仍是头、体、Timing 与脱敏。」

## ISSUE
ID：CH10-0010
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.2 Command Menu
精确位置：L102
原文：「用 Command Menu……搜索英文功能名」
问题等级：P3
问题类别：TERM
问题说明：Command Menu 里 Preserve log 的命令标题是 `Keep log on page reload / navigation` / `Don’t keep log…`；`preserve` 只是搜索 tag。Disable cache 命令是 `Disable cache while DevTools is open`。搜「Preserve log」通常仍能因 tag 命中，但列表字不同。
为什么有问题：找不到选项时的退路可能对不上字。
依据：devtools-frontend `network-meta.ts` UIStrings。
建议修改：写明列表可能显示 Keep log…，并可用 preserve / Disable cache 作搜索词。
推荐替换文本：「找不到勾选时，先让 DevTools 处于焦点，再 `Ctrl+Shift+P`（macOS `Cmd+Shift+P`）搜索 `preserve` 或 `Disable cache`。列表里可能显示 **Keep log on page reload / navigation**、**Disable cache while DevTools is open**，与面板勾选框 Preserve log / Disable cache 是同一功能。」

## ISSUE
ID：CH10-0011
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.11 Copy as cURL
精确位置：L297
原文：「Copy as cURL 有时还分 **bash** 与 **cmd**。」
问题等级：P3
问题类别：ACC
问题说明：官方 Network 参考还列 Copy as PowerShell、Copy as fetch。bash/cmd 分流仍存在于部分构建，不是错，只是不全。
依据：https://developer.chrome.com/docs/devtools/network/reference 导出一节。
建议修改：补一句 PowerShell/fetch 了解即可，macOS/Linux 用 bash。
推荐替换文本：「Copy 菜单里还可能出现 **Copy as cURL (bash/cmd)**、**Copy as PowerShell**、**Copy as fetch**。在 macOS/Linux 终端用 bash 形式。它复现的是这一次 HTTP 请求，不是完整渲染。」

## ISSUE
ID：CH10-0012
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.10
精确位置：L267
原文：「Disable cache 不会自动等于 Disable cache 对整个操作系统生效，通常只作用于**当前已打开 DevTools 的标签页**。」
问题等级：P3
问题类别：PED
问题说明：同语反复，意思对。
建议修改：改成「它不会关掉整台电脑或其他标签页的缓存，通常只作用于当前已打开 DevTools 的标签页。」
推荐替换文本：见上。

## ISSUE
ID：CH10-0013
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.5 列表常见列
精确位置：L160
原文：「Type | document、xhr、fetch、js、css、img」
问题等级：P3
问题类别：TERM
问题说明：过滤按钮是 Fetch/XHR、JS、CSS、Img、Doc；Type 列常见值是 document、script、stylesheet、image、xhr、fetch。教材把按钮名和列值混在一行。
依据：官方 Filter requests by type。
建议修改：列值与过滤按钮分开写。
推荐替换文本：「Type | document、script、stylesheet、image、xhr、fetch 等。过滤按钮名是 Doc / JS / CSS / Img / Fetch/XHR，和列里的单词不一定逐字相同。」

## ISSUE
ID：CH10-0014
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：MiniShop 工作实战
精确位置：L422–437
原文：工作实战未标 📖，未重复 `python3 run.py serve`
问题等级：P3
问题类别：PED
问题说明：质量标准要求写清类型（✅/📖/🚧）。`practice/README.md` 已标 10-1 📖 且注明无面板截图；章内逐步操作有命令，工作实战段没有。只读工作实战的人可能不知道如何启动 MiniShop。
依据：`standards/QUALITY_STANDARD_v1.0.md` 第七节。
建议修改：工作实战标题加 📖；「最小命令见上一节逐步操作第 1 步」。
推荐替换文本：「类型：📖 书面实操（仓库 **没有** DevTools 面板截图）。最小命令：上一节第 1 步 `cd project/minishop && python3 run.py serve`。」

## ISSUE
ID：CH10-0015
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：10.1 打开方式表
精确位置：L72
原文：macOS 检查元素 `Cmd+Option+C`
问题等级：P3
问题类别：ACC
问题说明：官方同时列出 `Command+Shift+C` **或** `Command+Option+C`。只写后者不算错。
依据：https://developer.chrome.com/docs/devtools/shortcuts
建议修改：macOS 格写成 `Cmd+Option+C` 或 `Cmd+Shift+C`。
推荐替换文本：「`Cmd+Option+C` 或 `Cmd+Shift+C`，或页面右键 **检查** / **Inspect**」

## ISSUE
ID：CH10-0016
文件：chapters/10-chrome-devtools.md
章节：第 10 章
小节：MiniShop 逐步操作标题
精确位置：L388
原文：「MiniShop 逐步操作（本机已跑通）」
问题等级：P3
问题类别：PED
问题说明：紧随其后的段落已诚实说明未截取面板。标题单独读会像 GUI 全绿。STATUS 将 10-1 标 Incomplete 仅针对面板截图。不是撒谎，是标题过满。
依据：`practice/STATUS.md`；正文 L390–391。
建议修改：标题改为「MiniShop 逐步操作（页面与报文已跑通；面板须你自己打开）」。
推荐替换文本：见上。

---

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `reviews/_full-audit-2026-09-10/AUDIT_PROGRESS.md`
- `reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`（仅结构，未采信旧分）
- `README.md`（诚实边界、10-1 入口）
- `docs/COURSE_CONTROL.md`
- `docs/COURSE_OUTLINE_v1.2.md`（第 10 章大纲条目）
- `docs/LEARNING.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`（10-1 📖）
- `practice/STATUS.md`（10-1 Incomplete：无面板截图）
- `exercises/README.md`
- `project/minishop/README.md`
- `project/minishop/docs/PRD.md`（R-AUTH / R-SEARCH / R-CART-10）
- `chapters/10-chrome-devtools.md`（全文）
- `chapters/quizzes/stage-3-web.md`（先独立作答再对答案）
- `chapters/quizzes/README.md`
- `chapters/assets/diagrams/README.md`
- `chapters/assets/diagrams/ch10-three-panels.html` / `ch10-two-switches.html` / `ch10-ttfb.html`
- `chapters/assets/diagrams/ch10-three-panels.png` / `ch10-two-switches.png` / `ch10-ttfb.png`（read_file 打开）
- `chapters/assets/01-login.png` / `02-login-fail.png` / `03-shop.png` / `04-search-empty-bug001.png` / `05-cart-qty-11.png` / `08-network-log.png`（read_file 打开）
- `project/minishop/frontend/index.html` / `app.js` / `admin.html`
- `project/minishop/server.py`（`_login` / Set-Cookie）
- `project/minishop/run.py`（serve）
- `project/minishop/evidence/README.md`
- `project/minishop/evidence/http/01-login-ok.txt` / `02-login-bad.txt` / `03-products-empty-keyword.txt` / `05-cart-qty-11.txt` / `network-log.html`
- `reviews/chapter-10-review.md`（线索，未采信 99 分）
- `reviews/_pedagogy-2026-09-10/ch10.md`（线索；P10-01..06 经独立复核后部分采纳）
- `reviews/_rereview-2026-09-09/stage-3-ch07-08-10.md`（仅第 10 章相关线索）
- `reviews/v1.2.1-rescore.md`（第 10 章 91 分线索）

未审其他章正文。

### 实际跑过的命令与结果摘要

- 统计正文：691 行，57 个章内标题，6 表，3 代码块，9 图，9 链。
- Chrome：`/Applications/Google Chrome.app/.../Google Chrome --version` → **152.0.7977.83**。
- 8765 已被 MiniShop 占用（PID 76770），未重启，直接打已运行实例。
- `curl POST /api/login` 错误密码 → **401** `{"result":"fail"}`，无 Set-Cookie。
- `curl POST /api/login` `13800138000` / `Test1234` → **200**，`result=ok`，token 已打码，**Set-Cookie HttpOnly**。
- `GET /api/products?keyword=%20%20%20` → **200**，3 件（BUG-001）。
- `POST /api/cart/items` qty=11 + Bearer → **400** `{"error":"qty exceeds stock"}`。
- Python 计时登录：约 **5.6 ms** 到首字节，下载约 0 ms。
- `HEAD /` → 501（教材未教 HEAD，不记 ISSUE）。
- 未安装 Playwright，**未**自动点击 DevTools GUI、**未**补拍面板图。
- 未在本会话执行 `python3 run.py serve`（端口已占用）。

### 外部核查

| 条目 | 来源 | 结论 |
| --- | --- | --- |
| Preserve log / Disable cache / Copy as cURL / Fetch/XHR / Doc / Payload / General / HAR sanitized | developer.chrome.com/docs/devtools/network/reference | 与教材功能名一致 |
| Disable cache while DevTools is open | 同上 + Preferences + network-meta.ts | 与教材一致 |
| Command Menu 快捷键须 DevTools 焦点 | developer.chrome.com/docs/devtools/command-menu | 教材已写焦点，正确 |
| Command Menu 命令标题 Keep log… | Chromium network-meta.ts | 教材只说搜英文功能名，不完全（CH10-0010） |
| Waiting (TTFB) 文档定义 | Network features reference L629–632 | 文档仍用旧名 |
| Timing **UI** 字符串 | Chromium RequestTimingView.ts；2022-05-03 Paul Irish 改名 | 现行 **Waiting for server response**（CH10-0003） |
| 限速预设 Fast/Slow 4G、3G | Network features reference | 教材举例可接受 |
| Chrome 145 Request conditions | developer.chrome.com/blog/throttle-individual-network-requests | 教材「了解即可」正确 |
| 打开方式 / 检查元素快捷键 | developer.chrome.com/docs/devtools/open 与 /shortcuts | 基本正确（CH10-0015） |
| Elements / Console 文档链接 | /docs/devtools/css ； /docs/devtools/console | 链接有效，主题匹配 |
| Web Vitals TTFB 含连接建立 | web.dev/articles/ttfb | 与 Chrome Waiting 阶段不等价（CH10-0003） |
| 中文面板「等待服务器响应」 | 未在本机切中文界面点开 Timing | 【External Verification Required】 |

### 旧审查处理

- `chapter-10-review.md` 99 分、v1.2.1 91 分：不采用为本次分数。91 只扣「无面板截图」不够：面板未拍是诚实项，真正的 P1 是 UI 文案、Preserve log 对象、caption、localhost 预期。
- 教学审查 P10-01..06：独立复核后，P10-03/04/05 升或保持 P1 写入 CH10-0001/0002/0004；P10-01/02/06 作 P2 写入 CH10-0006/0005/0007。新增 CH10-0003（旧审查未报 Timing 改名）。
- 「10.14 不冻结可删」：**拒绝**。与 Brief MiniShop 口径冲突。

### 未做事项（不假装完成）

- 未逐步点击 Chrome 152 中文 UI 核对每一句翻译。
- 未在 GUI 里实际勾选 Slow 4G 看 MiniShop 瀑布图。
- 未导出 HAR 文件做残留凭证扫描。
- 未审第 9、11 章正文（只核对衔接句与预告）。
