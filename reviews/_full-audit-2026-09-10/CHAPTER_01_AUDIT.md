# Chapter 01 Audit

审计对象：第 1 章《软件测试入门》及其列出的配套材料。  
审计员：Chapter-Audit-Agent-01  
日期：2026-09-10  
范围边界：只审第 1 章正文、实操 1-1、阶段测验中覆盖第 1 章的题目（第 1、2、9、10 题）、本章 6 张示意图及指定全局口径文件。未审其他章正文。

## 1. Coverage

禁止抽样。下表数量均已逐项检查，未检查列必须为 0。

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 章节 Markdown 文件 | 1（`chapters/01-software-testing-intro.md`，519 行） | 1 | 0 |
| 小节标题（H1–H3） | 57（H1=1，H2=24，H3=32） | 57 | 0 |
| 叙述行（非标题/非表格/非代码） | 116 | 116 | 0 |
| 列表项 | 96 | 96 | 0 |
| 引用块 | 7 | 7 | 0 |
| 表格 | 2（核心公式表、开发 vs 测试表） | 2 | 0 |
| 代码块 | 2（bash 命令 1，mermaid 流程图 1） | 2 | 0 |
| Linux/Shell 命令 | 章内 1 条 + 实操 README 6 条命令示例 | 7 | 0 |
| SQL | 0 | 0 | 0 |
| HTTP 示例 | 实操 `GET /api/products?keyword=%20%20%20`；证据 `03-products-empty-keyword.txt`；图中 HTTP/401 | 全部 | 0 |
| 测试用例 | 实操三臂 A/B/C + unittest 3 条 | 全部 | 0 |
| Bug 示例 | 登录失败假设、BUG-001、库存 9999/99999、qty=11、支付模块集群、明文密码、首页 20 秒 | 全部 | 0 |
| 章内练习 | 8 | 8 | 0 |
| 章内答案 | 8 | 8 | 0 |
| 实操 README 口头三问 | 3 | 3 | 0 |
| 阶段测验本章题 | 4（题 1、2、9、10 及对应答案） | 4 | 0 |
| 学习目标 | 9 | 9 | 0 |
| 常见错误 | 5 | 5 | 0 |
| 检查清单 | 14 | 14 | 0 |
| 进入下一章自测门槛 | 5（第 0～4 条） | 5 | 0 |
| 面试问答 | 4 | 4 | 0 |
| 七大原则正文 + 总结 | 7 + 7 | 14 | 0 |
| ISO/IEC 25010:2023 特性列表 | 9 | 9 | 0 |
| 图片 PNG | 6 | 6（均用 read_file 打开） | 0 |
| 图片 HTML 源 | 6 | 6 | 0 |
| Markdown 链接（不含图片） | 5 | 5 | 0 |
| 外部链接 | 2（ISTQB CTFL 页、ISO 25010:2023 页） | 2（已打开页面核验） | 0 |
| 实操 Python | `main.py`、`tests/test_lab.py`，以及运行依赖 `practice/run.py`、`_http.py`、`_minishop.py` | 全部 | 0 |
| 生成证据 `validation/latest.json` | 1（本机跑出） | 1 | 0 |
| 全局口径文件 | README、COURSE_CONTROL、OUTLINE、LEARNING、QUALITY_STANDARD、practice README/STATUS、chapter-01-review、pedagogy ch01 | 全部 | 0 |

Coverage：**100%。未检查 = 0。**

先前 `reviews/chapter-01-review.md` 与 `reviews/_pedagogy-2026-09-10/ch01.md` 只作线索。独立复核后：C01-2（原则七 V&V 三角）、C01-5（MiniShop 定性）、C01-6 的门槛第 0 条（跑 1-1）已回写正文；C01-1/C01-3/C01-4/C01-7/C01-8/C01-9 仍有残留，见 ISSUE。

## 2. 总评分

| 项 | 分数 |
| --- | ---: |
| 技术准确性 | 8/10 |
| 岗位实用性 | 8/10 |
| 完整性 | 8/10 |
| 初学者友好度 | 7/10 |
| 教学顺序 | 8/10 |
| 代码质量 | 7/10 |
| 实操质量 | 8/10 |
| 练习质量 | 7/10 |
| 图片质量 | 7/10 |
| **总体** | **76/100** |

九项合计 68/90，百分制折算 76。扣分由下面 ISSUE 支撑，不因篇幅给分。

核心事实（ISTQB 七原则、ISO/IEC 25010:2023 九特性现用名、静态/动态、QA≠测试岗英文名、禁止的错误绝对化）总体正确。扣分集中在：脊柱公式被写成「缺一不可」却未标明这是教学模型；实操臂 B 的判定原文已经宣布实现不合规；开篇登录失败绑定了仓库里会登录成功的账号；示意图未跟正文补丁对齐。

## 3. P0

无。本章没有把 GET/POST 安全性讲反、没有把 Cookie/Session/Token 写成三种可互换产品、没有把 P0/P1/P2/P3 说成全球统一、没有把「没发现 Bug」写成「系统没有 Bug」、没有把「测试必须等开发全部完成」当成正确规则。后两条在「常见错误」里被明确修正。

## 4. P1

## ISSUE
ID：CH01-0001
文件：`practice/01-observation-oracle-evidence/main.py`；`practice/01-observation-oracle-evidence/README.md`；`chapters/01-software-testing-intro.md`；`project/minishop/docs/PRD.md`（仅作为本章判定原文被引用）
章节：第 1 章
小节：核心公式；实操 1-1 臂 B
精确位置：`main.py` `ORACLE` 常量第 24–27 行；README 臂对照表「B 只有判定」行；正文第 63 行
原文：
```
ORACLE = (
    "R-SEARCH：关键字为空或仅空白时，不应把全量商品当成搜索结果"
    "（当前实现不符合，见 BUG-001）。"
)
```
正文：「只有判定：你读过 PRD。没有运行，不知道实现违不违反。」
README：「知道需求，不知道实现违不违反」
问题等级：P1
问题类别：PED / TEST / CODE / ANS
问题说明：臂 B 的教学点是「只有判定、没有观察，所以不知道实现违不违反」。实际打印的判定原文已经写明「当前实现不符合，见 BUG-001」。PRD `R-SEARCH` 单元格把规则和实现结论写在同一格，脚本又原样复制。学生在「不发 HTTP」的那一段就已经看到答案。`--check` 的 `test_oracle_sends_no_request` 只断言出现 `R-SEARCH`、不出现 `HTTP `，并不禁止 `BUG-001` / `不符合`。
为什么有问题：这会把本章最重要的对照实验做废。学生无法体会「尺子本身不告诉你这次量出来是多少」；他们看到的是「需求文档已经替你写好了缺陷单」。剩下的正确点只是「阅读不是执行」，但正文和 README 的那句「不知道实现违不违反」在这个仓库里是假的。
依据：本机 `python3 practice/run.py 1-1 -- --arm oracle` 输出含「当前实现不符合，见 BUG-001」，紧接着又印「实现有没有违反？不跑系统，你说不准。」自相矛盾。ISTQB 的 test oracle 是 expected result 的来源，不应夹带 actual result。
建议修改：把规则和实现备注拆开。判定只保留规则句；BUG-001 放到臂 C 或缺陷单。unittest 应断言臂 B 输出不含 `不符合`、`BUG-001`。
推荐替换文本：
```
ORACLE = "R-SEARCH：关键字为空或仅空白时，不应把全量商品当成搜索结果。"
```
臂 B 打印后再写：「这只是尺子。尺子上不会写『这次量出来超了』；那要看系统实际返回什么。」PRD 建议改为两列或脚注：「规则」与「v1.0 实现备注（见 BUG-001）」分开。

## ISSUE
ID：CH01-0002
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：场景导入：登录失败，这算测试吗？
精确位置：第 33–42 行
原文：「MiniShop 是本仓库里的个人软件测试实践项目」之后，给出手机号 `13800138000`、密码 `Test1234`，并写「教学示例，与第 19 章项目数据相同」；紧接着「点击登录，结果却是『登录失败』。你发现了一个缺陷」。
问题等级：P1
问题类别：TEST / SEQ / PRE
问题说明：这组账号是 MiniShop 种子用户。`project/minishop/tests/test_api.py` 的 `test_login_ok` 断言 `13800138000` / `Test1234` 登录返回 200、`result=ok`、非空 token。场景却把它写成一次真实失败并「发现了一个缺陷」。后文 MiniShop 工作场景又说「手机号、密码仅用于解释测试思维」，两处口径互相打架。
为什么有问题：零基础读者会以为仓库登录是坏的，或把 BUG-001 理解成登录缺陷。他们按「与第 19 章项目数据相同」去跑，会看到登录成功，从而怀疑开篇例子、公式表和实操 1-1 哪一个才是「仓库现状」。教学假设可以保留，但不能绑死真实会成功的凭证还说失败。
依据：`server.py` 种子用户 `13800138000` + `hash_password("Test1234")`；`test_login_ok` 期望 200。质量标准：第 19 章之前的路径/字段若当教学约定必须标明，不得写成已冻结契约的既成事实。
建议修改：要么改用明显虚构的失败（错误密码、未写明的需求），并写「这不是仓库现状」；要么用仓库里真的开放缺陷（空搜索 / BUG-001）做开篇。
推荐替换文本：
```
先用一个假设场景把公式走通——注意：下面这次「登录失败」不是 MiniShop v1.0 的开放缺陷。仓库里 `13800138000` / `Test1234` 按 PRD 应当登录成功。

假设某次构建里，需求仍是「正确手机号和密码进入首页」，你输入了正确账号，页面却写「登录失败」。你怎么知道这算缺陷？因为需求是判定；你输入并看到失败提示是观察；若不截图、不写步骤，明天开发说「我这边是好的」，你拿什么证明——那是证据。

本章仓库里真正仍开放、要用实操 1-1 复现的，是空搜索返回全量商品（BUG-001），不要和这个登录假设混成一件事。
```

## 5. P2

## ISSUE
ID：CH01-0003
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：核心公式：测试 = 观察 + 判定 + 证据
精确位置：第 1–3 行一句话核心；第 48–64 行「三块缺一不可」
原文：「测试 = 观察 + 判定 + 证据。」「三块缺一不可。」「只有判定：你读过 PRD。没有运行，不知道实现违不违反。」随后第 66 行又说「需求评审也是测试」。
问题等级：P2
问题类别：TERM / PED / ACC
问题说明：公式是有效的教学脊柱，但正文把它写成测试的定义，并声称缺一不可。ISTQB CTFL 4.0/4.0.1 的定义是：testing is a set of activities to discover defects and evaluate the quality of software work products（Glossary v3：The process within the software development lifecycle that evaluates the quality of a component or system and related work products）。测试活动包括规划、分析、设计、实现、执行、完成；静态测试并不「运行系统」。把「只读 PRD」说成「还不是测试」，与 1.1「评审需求已经是测试」直接冲突，除非立刻把评审重新解释成「对文档的观察」——这是事后补丁，初学者读公式段时已经先被「缺一不可」卡住。
为什么有问题：学生可能在面试/ISTQB 场景把这句背成行业定义，或认为没有书面证据的探索性测试、没有执行的评审都不算测试。后文「可靠测试 = 范围 + 观察通道 + 判定标准 + 证据 + 风险说明」其实更接近工程实际，却被放在公式之后当「外壳」，主句仍然过绝对。
依据：ASTQB 转述的 CTFL 1.1；ISTQB Glossary `testing` / `quality control`；本章 1.1 自己的完整表述。质量标准允许「一句话核心」，但核心不能与后文和权威定义互相否决。
建议修改：标明「教学模型，不是 ISTQB 原句」；把「缺一不可」改成「执行一次动态测试并要让别人能复核时，三块都要在」；评审单独说「观察对象是工作产品，不是运行中的系统」。
推荐替换文本：
```
本课程用一句教学模型把后面各章串起来（不是 ISTQB 对 testing 的原句定义）：

测试要能回答三件事——看见了什么（观察）、凭什么对错（判定 / test oracle）、别人怎么复核（证据）。

ISTQB 把测试定义为一组发现缺陷、评价工作产品质量的活动，包含静态与动态，也包括规划与设计。缺了书面证据的探索、不运行程序的评审，仍然是测试；但若你要对别人声称「这套构建测过了」，三块就都得能指出来。
```

## ISSUE
ID：CH01-0004
文件：`chapters/assets/diagrams/ch01-formula.html`；`chapters/assets/diagrams/ch01-formula.png`；`chapters/01-software-testing-intro.md` 第 52–58 行
章节：第 1 章
小节：核心公式
精确位置：公式图三张卡片；正文公式表第三行已改为「复现步骤 + 屏幕/命令输出 + bugs/BUG-001.md」
原文（图）：观察含「页面、HTTP、日志、SQL、接口 JSON」；判定含「OpenAPI、不变式」；证据含「报文、pytest」。
问题等级：P2
问题类别：IMG / PRE / PED
问题说明：教学审查 C01-3 已把正文表的证据列改成第 1 章能懂的步骤/输出/缺陷单，图没有同步。第 1 章前置知识写「无需编程」，阅读提示说「不必会 Python」。图却把 HTTP/SQL/OpenAPI/pytest 堆进三块。
为什么有问题：图是脊柱图，读者会先看图。未教概念会让人以为「不会 pytest 就不算留下证据」。正文与图口径分裂。
依据：`docs/LEARNING.md` 与质量标准：图要讲本章难点，不堆后面章节工具名。
建议修改：图三块与现用正文表对齐；caption 可写「后面章节会增加 HTTP、SQL、pytest 等观察通道和证据形式」。重新导出 PNG。
推荐替换文本：见第 9 节 IMG-CH01-001。

## ISSUE
ID：CH01-0005
文件：`chapters/assets/diagrams/ch01-net-holes.html`；`ch01-net-holes.png`
章节：第 1 章
小节：1.5 原则一
精确位置：左卡「错误密码 401」；中卡「空搜索 BUG-001 这种已知漏洞」
原文：「登录成功、错误密码 401、qty=11 被拒绝。」「没测过的浏览器、没想到的并发、空搜索 BUG-001 这种已知漏洞。」
问题等级：P2
问题类别：IMG / PRE / HTTP / PED
问题说明：401 是第 9 章才教的状态码。BUG-001 是已经发现并建单的缺陷，放在「网没盖住 / 还可能有鱼」语义错误——它是网里已经捞到的鱼，用来说明「已知缺陷仍开放」，不是「没测到」。
为什么有问题：原则一要讲的是「没捞到 ≠ 海里没鱼」。把已知 BUG-001 放进网外，学生会以为「已知开放缺陷」等于「未覆盖」。401 对零基础是噪音。
依据：CTFL 1.3 原则一（ASTQB 转述 syllabus）：testing shows the presence, not the absence of defects。教学审查 C01-9。
建议修改：左卡改「错误密码被拒绝」；中卡改「没测过的浏览器 / 没想到的输入」；已知 BUG-001 不要放在网外。
推荐替换文本：见 IMG-CH01-002。

## ISSUE
ID：CH01-0006
文件：`chapters/assets/diagrams/ch01-static-dynamic.html`；`ch01-static-dynamic.png`
章节：第 1 章
小节：1.1 测试不只是运行软件
精确位置：静态测试卡片内部
原文：「假设的草稿，不是仓库 PRD」与「仓库对照：R-SEARCH；实现见 BUG-001」写在同一张纸上，下方又说「此时 MiniShop 甚至还没有可点击的页面」。
问题等级：P2
问题类别：IMG / PED
问题说明：正文 1.1 开头已把「草稿缺口」和「仓库 BUG-001」拆成两个故事，图仍混在静态卡片里。一边说还没有可点页面，一边指向已实现的 BUG-001。
为什么有问题：静态卡的教学点是「程序没跑也能测」。指向仓库实现会把静态例子拽回动态现状。
依据：正文第 85–89 行已经拆开；图未跟补丁。
建议修改：静态卡只留草稿缺口；BUG-001 不要出现在静态卡。动态卡可继续用登录假设，或改用空搜索动态复现（并标明那是仓库现状）。

## ISSUE
ID：CH01-0007
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.1「测试不只是运行软件」末段；1.5 原则三
精确位置：第 103 行；第 231 行
原文：第 103 行「例如在需求评审中发现空搜索是否返回全量没有写清（假设的草稿，不是仓库 PRD；对照 `R-SEARCH` / BUG-001）。」第 231 行「需求评审时发现空搜索规则没有写清楚」——此处未再标明假设草稿。
问题等级：P2
问题类别：PED / SEQ
问题说明：C01-1 只修了 1.1 开头的分条，同一节后段和原则三又把「没写清」和仓库已有 `R-SEARCH` 拧回一句。读者会再问：到底写清了没有？
为什么有问题：空搜索在本章同时扮演「需求缺口（静态假设）」和「规则已写清、实现违反（动态现状）」两个角色。分条之后必须处处标明身份，否则拆分等于没拆。
依据：当前仓库 PRD `R-SEARCH` 已有规则；BUG-001 仍开放。原则三的成本故事完全可以用「假设早期草稿没写这句」。
建议修改：第 103 行静态例子不再夹 `对照 R-SEARCH / BUG-001`。原则三写明「这是假设的早期草稿，不是现在的 PRD」。
推荐替换文本（原则三）：
```
假设早期草稿还没写空搜索规则。评审时补一句话，通常只改文档；若等前端、后端、用例都做完才发现，返工会贵得多。现在仓库里的 PRD 已经有 R-SEARCH，实现仍违反——那是另一件事（BUG-001），不要和「当时没写清」混成同一个时间线。
```

## ISSUE
ID：CH01-0008
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.5 原则一
精确位置：第 212 行
原文：「执行 100 次测试没有发现问题，只能说明在已经覆盖的范围内没有发现已知问题」
问题等级：P2
问题类别：TERM / ACC
问题说明：「没有发现已知问题」是同义反复：没发现的就还不是「已知」。CTFL 原则一是：testing can show defects are present, but cannot prove there are no defects；even if no defects are found, testing cannot prove correctness.
为什么有问题：学生可能理解成「没发现的是未知问题，发现的才算数」，错过「样本外仍可能有缺陷」。后文放行话术「未发现阻塞上线的已知严重缺陷」是结论写法，不应提前污染原则定义。
依据：ASTQB 1.3 转述 CTFL 4.0 原则一原文。
建议修改：改成「只能说明在已经执行的范围内没有观察到失效，不能证明系统没有缺陷」。
推荐替换文本：「执行 100 次测试没有发现问题，只能说明在已经覆盖的范围内未观察到失效，不能证明系统没有缺陷。」

## ISSUE
ID：CH01-0009
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.8 常见软件测试岗位；学习目标末条
精确位置：第 321 行标题 `⭐⭐⭐`；第 25 行学习目标「认识常见测试岗位和发展方向」
原文：岗位节标必须掌握；阅读提示（第 5 行）写「岗位名称、ISO 质量特性不必一次背完」。
问题等级：P2
问题类别：PED
问题说明：第一次读被标成 ⭐⭐⭐ 的岗位地图，实际是名词清单（Selenium/Playwright/JMeter/CI/CD），比 1.1–1.5 更浅、更不需要当堂记住。星级与阅读提示、与「功能测试是入口」的定位冲突。
为什么有问题：零基础会以为必须背工具名单才能进入第 2 章。
依据：质量标准星级定义；教学审查 C01-4。
建议修改：1.8 改为 ⭐，首句写「第一次只看功能测试工程师」。学习目标改为「知道功能测试是常见入口，其余岗位当地图」。

## ISSUE
ID：CH01-0010
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.4 什么叫软件质量
精确位置：第 181–204 行
原文：先编号列出 ISO/IEC 25010:2023 九个特性，再说「初学阶段不需要背完整标准」，再给六条口语版。
问题等级：P2
问题类别：PED
问题说明：解释顺序违反质量标准「生活类比 → 简单模型 → 正式定义」。下单反例和图已经足够说明「质量是多面的」；九特性清单应作查阅附录。特性名单本身是 2023 现用名，技术上正确，问题是坡度。
为什么有问题：开篇承诺不必背完，1.4 却先要求扫过 Interaction Capability / Flexibility / Safety 三套中英对照。
依据：QUALITY_STANDARD 第三节；ISO/IEC 25010:2023 官方页确认九特性；教学审查 C01-7。
建议修改：先下单反例 + 六问；九特性收到「查标准时看」的短列表，并保持「教学译法」声明。

## ISSUE
ID：CH01-0011
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.5 原则二
精确位置：第 227 行
原文：「因此需要等价类、边界值、风险分析和优先级，把有限资源集中到更有代表性的场景。」
问题等级：P2
问题类别：PRE / SEQ
问题说明：等价类、边界值是第 5 章技法。CTFL 原则二只要求理解 exhaustive testing is impossible，并用 techniques / prioritization / risk-based testing 聚焦——教材可以推迟点名技法。
为什么有问题：零基础会以为现在就要会设计等价类，或把原则二记成「要做等价类」而不是「测不完所以要抽样」。
依据：学习顺序 01 在 05 之前；CTFL 4.0 原则二。
建议修改：「所以只能抽样。怎么抽，第 5 章再教等价类和边界值；这里先接受测不完，并用风险决定先测哪。」

## ISSUE
ID：CH01-0012
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.2 原因一
精确位置：第 132 行
原文：「例如需求写库存上限 9999，实现却接受 99999。……不要把『0～9999』抄成 MiniShop v1.0 规则：PRD 钉的是当前库存，教学数据里鼠标是 10 件，`qty=10` 允许、`qty=11` 拒绝。」
问题等级：P2
问题类别：PED / SEQ
问题说明：人会犯错的完整小例子被 MiniShop 免责声明从中切断。警告里的「0～9999」也不是这个例子用过的数字（例子是上限 9999 vs 实现 99999）。
为什么有问题：初学者跟完 9999 还没形成「多写一个 9 就会出事」的印象，就被拽去 qty=10/11。两个故事都对，但不应叠在同一句。
依据：PRD `R-CART-10` 确为 qty=10/11；质量标准要求示例完整。
建议修改：9999 例子单独讲完。另起一句：「MiniShop v1.0 不要抄 9999，库存规则是当前可售库存，鼠标教学数据 10 件。」

## ISSUE
ID：CH01-0013
文件：`practice/01-observation-oracle-evidence/main.py`；`tests/test_lab.py`
章节：第 1 章
小节：实操 1-1 臂 C
精确位置：`main.py` 第 52 行 `violates = observe["status"] == 200 and count == 3`
原文：把「违反 R-SEARCH」实现成「HTTP 200 且恰好 3 件」。
问题等级：P2
问题类别：TEST / CODE
问题说明：R-SEARCH 的判定是「空/空白关键字不应把全量商品当成搜索结果」，不是「不得返回 3」。当前种子库恰好 3 件，所以能复现。若以后多一个 SKU，空搜索返回 4 件仍是同一缺陷，脚本会走「本次没有复现」分支（exit 2），并教学生把魔法数字当 oracle。
为什么有问题：第 1 章正在教「判定是尺子」。尺子写成「==3」是坏习惯，后面接口/自动化章会更难纠正。
依据：PRD R-SEARCH；`server.py` `_get_products` 对 blank keyword 返回全表；BUG-001 预期是「不应展示全量」。
建议修改：比较空搜索 `items` 与无 keyword / 全量列表是否相同，或断言 blank keyword 返回了全部种子 SKU，而不是 `count == 3`。
推荐替换文本：
```
full_skus = {"SKU-DEMO-001", "SKU-DEMO-002", "SKU-DEMO-003"}
returned = {it["sku"] for it in items} if items else set()
violates = observe["status"] == 200 and returned == full_skus
```

## ISSUE
ID：CH01-0014
文件：`practice/01-observation-oracle-evidence/main.py`；`practice/01-observation-oracle-evidence/README.md`
章节：第 1 章
小节：实操 1-1 最小命令
精确位置：README「只看某一臂」列出 `--arm full`；`main.py` 第 97–106 行
原文：README 把 `--arm full` 与 observe/oracle 并列成「只看某一臂」。代码在 `arm != oracle` 时总是先跑 `arm_observe`，只有 `--arm observe` 会提前返回；`--arm full` 与默认 `--arm all` 一样打印 A+B+C。
问题等级：P2
问题类别：CODE / EX
问题说明：本机 `python3 practice/run.py 1-1 -- --arm full` 仍输出臂 A、臂 B、臂 C。文档承诺不成立。
为什么有问题：学生按「只看 C」去对照验收条件，会被 A/B 输出干扰；也说明 `--arm` 四个选项没有四个行为。
依据：实际运行输出。
建议修改：`--arm full` 只跑 C（可在内部静默调用 observe 以取数据，但不打印臂 A/B 的教学旁白）；或 README 改为「`--arm full` 仍会先观察再对照」。

## ISSUE
ID：CH01-0015
文件：`chapters/01-software-testing-intro.md`；`chapters/quizzes/stage-1-foundations.md`
章节：第 1 章
小节：小练习；阶段测验 1
精确位置：练习 1–8；测验题 1、2、9、10
原文：八题覆盖定义、静态评审、质量多维、原则一/二/四/七、开发测试关系。没有一题要求学生用「观察 / 判定 / 证据」拆一条例子。阶段测验本章四题同样不考公式。
问题等级：P2
问题类别：EX / PED
问题说明：一句话核心和实操 1-1 都围着公式，章内练习和阶段测验却不强制使用它。学生可以答对 8 题、过测验，仍然不会用公式当过滤器。
为什么有问题：质量标准要求练习覆盖本章目标；本章目标的过滤器就是那句话。
依据：QUALITY_STANDARD 第七章「一句话核心」；`docs/LEARNING.md` 把公式当全书脊柱。
建议修改：加一题：「用观察/判定/证据拆开『空白搜索返回 3 件』；并说明缺哪一块还叫不叫测试。」阶段测验可在后续改版时加一道必过。

## ISSUE
ID：CH01-0016
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.1 / 1.7 / 面试角度
精确位置：全章无「调试 / debugging」
原文：无
问题等级：P2
问题类别：JOB / TERM / PED
问题说明：ISTQB CTFL FL-1.1.2 要求区分 testing 与 debugging：测试发现失效/缺陷，调试定位并修复。初级岗位入职第一周就会碰到「你帮我看一下是不是代码问题」。本章讲测试 vs 开发，却不讲测试 vs 调试。
为什么有问题：学生容易把「提交 Bug」理解成「要给出根因和补丁」，或把开发的 debug 当成测试。
依据：CTFL 4.0 1.1.2（ASTQB 1.1 What is Testing 页转述 syllabus）。
建议修改：在 1.1 或 1.7 加 4～6 行：测试报告失效与证据；调试找原因并修改代码；确认测试验证修复。不必展开第 2 章术语。

## ISSUE
ID：CH01-0017
文件：`chapters/01-software-testing-intro.md`；`chapters/assets/diagrams/ch01-qa-qc-testing.html`
章节：第 1 章
小节：1.3 Testing、QC 和 QA
精确位置：正文第 160–168 行直接给三句定义；工厂类比只在图的 lead/卡片标题
原文：正文无「生产线 / 这批货」类比。
问题等级：P2
问题类别：PED
问题说明：质量标准要求生活类比先于正式定义。没看图的读者（纯 Markdown、部分阅读器不渲染 PNG）只能看到抽象缩写。
为什么有问题：QA/QC/Testing 是本章易混点，类比是真正降低门槛的部分，却不在可复制的正文里。
依据：QUALITY_STANDARD 第三节；ISTQB CTFL 1.2.2：Testing is a form of QC；QA is process-oriented, preventive。
建议修改：正文先写三句工厂类比，再给定义，并保留「招聘启事里的 QA Engineer 可能就是测试岗」。

## ISSUE
ID：CH01-0018
文件：`practice/01-observation-oracle-evidence/README.md`
章节：第 1 章
小节：实操 1-1 Code map
精确位置：第 13 行「可改的输入: `--arm observe|oracle|full|all`」
原文：把切换观看臂写成「可改的输入」。
问题等级：P2
问题类别：EX / PED
问题说明：`docs/LEARNING.md` 的「再改」层是「改哪一个输入，判定如何变」。这里改的是看哪一段输出，被测输入始终是空白关键字。学生没有自己补过一次判定。
为什么有问题：门槛和实操都停在「看脚本替你做完的三臂」，缺少「只看观察、自己说算不算 Bug」。
依据：教学审查 C01-6；LEARNING 三层阅读。
建议修改：Code map 改成「观看开关，不是被测输入」。门槛第 0 条加：只跑 `--arm observe`，对照 PRD 自己补一句判定（不要先看臂 C）。

## ISSUE
ID：CH01-0019
文件：`practice/01-observation-oracle-evidence/README.md`；`main.py` 打印文本
章节：第 1 章
小节：实操 1-1
精确位置：README 臂 A「调用 GET /api/products?keyword=   」；脚本打印 `GET ... HTTP 200`
原文：在「无需编程、你不需要会 Python」的实操里，主观察通道是 HTTP GET 和 items 数量。
问题等级：P2
问题类别：PRE / PED
问题说明：HTTP 方法、状态码、query 是第 9/13 章内容。实操设计成「对着三段中文旁白回答」是可行的，但 README 把 GET 写进「你做了什么」，零基础会以为必须会发接口。
为什么有问题：开篇实操的认知负荷从「看三块缺一」变成「这是不是网路请求」。
依据：前置知识「无需计算机专业知识」；正式顺序 09 在 01 之后。
建议修改：README 改成「脚本帮你搜了一次空白关键字，屏幕会告诉你返回了几件商品。GET/HTTP 字样先当『一次询问系统的记录』，第 9 章再拆。」脚本旁白同步降术语。

## ISSUE
ID：CH01-0020
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：进入下一章的自测门槛
精确位置：第 491 行第 0 条
原文：「跑通 `python3 practice/run.py 1-1` 和 `python3 practice/run.py 1-1 --check`」
问题等级：P2
问题类别：EX / PED
问题说明：门槛已要求跑 1-1（教学审查 C01-6 部分已修），但没有要求「只跑 observe、自己补判定、口头回答 README 三问」。`--check` 通过只证明脚本结构，不证明学生理解公式。
为什么有问题：学生可以不看输出、不答题，命令绿了就进第 2 章。
依据：质量标准「检查清单能验证能力」；practice README 三问才是认知验收。
建议修改：第 0 条加上「再只跑 `-- --arm observe`，自己补一句判定，口头回答 README 三问」。

## 6. P3

## ISSUE
ID：CH01-0021
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.5 原则四
精确位置：第 237 行
原文：「假设过去几个版本中，支付模块发现 21 个问题」
问题等级：P3
问题类别：SEQ
问题说明：1.2 已声明支付不是 MiniShop v1.0 范围；原则四未再标明。章末总声明能兜住，但原则四是独立可读段。
建议修改：加「这是电商领域例子，不是 MiniShop v1.0 模块」。

## ISSUE
ID：CH01-0022
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.5 原则七末句
精确位置：第 261 行
原文：「第 2 章会单独讲『确认测试』这个词——那是缺陷修没修好，和这里不是同一件事。」
问题等级：P3
问题类别：SEQ / PED
问题说明：比开篇登录例子更绕。原则七讲的是 absence-of-defects fallacy，不需要为了防第 2 章术语而预打补丁。V&V 英文三角已删，这句残留仍会让人去翻第 2 章。
建议修改：删掉。或改成「后面讲研发流程时会区分『规格对不对』和『缺陷修没修好』，这里只要记住：符合规格仍可能不好用。」

## ISSUE
ID：CH01-0023
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：面试角度
精确位置：第 389 行 `⭐⭐⭐`
原文：面试节标必须掌握，内容是本章复述。
问题等级：P3
问题类别：PED
问题说明：与 1.1/1.5 抢星级。第一次读可跳。
建议修改：改为 ⭐⭐，注明「可先跳，求职前再回看」。

## ISSUE
ID：CH01-0024
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.4 ISO 特性 8、9
精确位置：第 190–193 行
原文：Security → 信息安全性；Safety → 安全保障性。已声明教学译法。
问题等级：P3
问题类别：TERM
问题说明：教学区分是对的（中文「安全」会把 Security/Safety 叠在一起）。「保障」容易让人以为是 QA 的 assurance。官方中文国家标准若尚未对齐 2023 版，保持教学译法即可，但可加一句「有的材料把 Safety 译成功能安全/人身安全」。
依据：ISO/IEC 25010:2023 增加 Safety；Usability→Interaction Capability；Portability→Flexibility。本章未误用 2011 旧名，这点应保留。
建议修改：括号加「Safety，不是 Security」。

## ISSUE
ID：CH01-0025
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.2 原因一
精确位置：第 132 行
原文：例子是「上限 9999 / 实现 99999」，警告却写「不要把『0～9999』抄成 MiniShop」。
问题等级：P3
问题类别：ACC
问题说明：警告数字与例子不一致，像从旧稿残留。
建议修改：警告改为「不要把这个 9999 上限抄进 MiniShop 用例」。

## ISSUE
ID：CH01-0026
文件：`practice/01-observation-oracle-evidence/main.py`
章节：第 1 章
小节：实操 1-1 `arm_full`
精确位置：第 50 行 `def arm_full(base_url: str, observe: dict)`
原文：`base_url` 未使用。
问题等级：P3
问题类别：CODE
问题说明：不影响运行。会让以后读代码的人以为 C 臂会再发一次请求。
建议修改：删参数，或在 C 臂用 `base_url` 把请求 URL 写入 JSON 证据。

## ISSUE
ID：CH01-0027
文件：`chapters/quizzes/stage-1-foundations.md`；`chapters/01-software-testing-intro.md`
章节：第 1 章 / 阶段测验 1
小节：测验题 1 答案 vs 原则一
精确位置：测验答案第 1 条「测试只能证明发现了失效」；正文原则一标题用「缺陷」
原文：术语不完全对齐。
问题等级：P3
问题类别：TERM / ANS
问题说明：ISTQB 原则一原文用 defects；动态测试观察到的是 failure。测验用「失效」更贴近动态测试，正文用「缺陷」更贴近原则名称。不是答错，但学生会对答案时产生「我写缺陷算不算对」。
建议修改：测验答案补一句「原则名称里说缺陷；动态测试当场看到的是失效。答题说『不能证明没有缺陷』即可。」
【ANSWER VERIFICATION FAILED】：否。独立作答与标准答案同向。

## ISSUE
ID：CH01-0028
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.4 口语版；常见错误 5；本章总结 4
精确位置：第 201、385、504 行
原文：刚区分 Security/Safety 之后，口语和总结又写「安全性」。
问题等级：P3
问题类别：TERM
问题说明：对电商入门可接受，但会把刚建立的区分冲掉。
建议修改：口语固定用「信息安全」；Safety 标明「普通电商很少直接测」。

## ISSUE
ID：CH01-0029
文件：`chapters/01-software-testing-intro.md`
章节：第 1 章
小节：1.5 原则五标题
精确位置：第 241 行
原文：「测试会逐渐失效（测试会磨损）」
问题等级：P3
问题类别：TERM
问题说明：CTFL 4.0.1 名称是 tests wear out。正文正确解释为「发现新缺陷的能力下降」，并保留杀虫剂悖论旧称、肯定回归价值。标题「逐渐失效」容易理解成「自动化回归会越跑越错」。
依据：CTFL 原则五：If the same tests are repeated many times, they become increasingly ineffective in detecting new defects；However, repeating the same tests can have a beneficial outcome, e.g. automated regression testing.
建议修改：标题改为「测试会磨损（tests wear out）」。

## ISSUE
ID：CH01-0030
文件：`practice/01-observation-oracle-evidence/README.md`
章节：第 1 章
小节：读完请回答
精确位置：第 61–65 行三问，无答案
原文：三问
问题等级：P3
问题类别：EX / ANS
问题说明：章内小练习有答案；公式三问作为脊柱验收却只在 README。口头即可，但对自学读者不友好。
建议修改：在章内练习加对应题，或在 README 末加「参考要点（先自己答）」。

## ISSUE
ID：CH01-0031
文件：`chapters/assets/diagrams/ch01-quality.html`；`ch01-quality.png`
章节：第 1 章
小节：1.4
精确位置：四张卡片把兼容/交互、可靠/安全两两合并
原文：caption 已补「还有可维护性、灵活性、安全保障性」
问题等级：P3
问题类别：IMG
问题说明：对初学压缩可以，但「可靠/安全」一张卡会再混 Security。不是错误，是信息损失。
建议修改：若保持四卡，安全卡标题改为「信息安全」；Safety 只放 caption。

## 7. 逐段问题

| 位置 | 结论 |
| --- | --- |
| 一句话核心 / 阅读提示 | 公式有用，但未标明教学模型。阅读提示「不必背岗位和 ISO」与后文星级、1.4 清单冲突。见 CH01-0003、0009、0010。 |
| 这一章解决什么问题 | 无技术错误。把后续各章挂到观察/判定/证据上，作为地图成立。 |
| 学习目标 | 9 条能覆盖本章。末条岗位目标与「不必一次背完」打架。见 CH01-0009。 |
| 前置知识 | 「无需专业基础」诚实。与实操 GET/HTTP、图中 pytest 不一致。见 CH01-0004、0019。 |
| 场景导入 | MiniShop 已定性为个人实践项目（C01-5 已修）。登录失败绑定真实成功账号。见 CH01-0002。观察/判定/证据三次落点清楚。 |
| 核心公式 + 表 + 命令 | 表的证据列已是第 1 章语言；「缺一不可」过绝对；臂 B 文案与仓库 PRD 冲突。命令 `python3 practice/run.py 1-1` 本机可跑。见 CH01-0001、0003、0004。 |
| 1.1 开头分条 | 静态草稿 vs 动态 BUG-001 拆开，方向正确。 |
| 1.1 测试不只是运行软件 | 定义接近 ISTQB（发现缺陷、评价质量、静态+动态、不能保证绝对正确）。「预防缺陷」偏 QA/静态收益，可接受。第 103 行又把草稿和仓库拧回。缺测试 vs 调试。见 CH01-0007、0016。 |
| 1.1 测试要回答哪些问题 | 8 问具体，无绝对化。无问题。 |
| 1.2 原因一 | 人会犯错成立。9999 被免责声明切断，「0～9999」与例子不一致。见 CH01-0012、0025。qty=10/11 与 PRD 一致，且标明不要抄 9999。 |
| 1.2 原因二 | 组合复杂度成立。优惠券/支付/订单状态机已标明不是 v1.0。无问题。 |
| 1.2 原因三 | 年龄 18～60 扩展到边界/非法输入，方向正确，且未写成 MiniShop 字段。无问题。 |
| 1.2 原因四 | 缺陷成本例子（登录、重复扣款、隐私）合理；未把 MiniShop 写成会扣款。无问题。 |
| 1.3 QA/QC/Testing | 与 CTFL 1.2.2 同向：Testing is a form of QC；QA 过程/预防；QC 产品。正文补充「岗位名称会混用」正确。工厂类比只在图。见 CH01-0017。未把 QA 写成测试的英文名。 |
| 1.4 软件质量 | 九特性名为 2023 现用名，未把 Usability/Portability 当现用名。Security vs Safety 区分正确。先清单后说不必背。口语「安全性」冲淡区分。见 CH01-0010、0024、0028。20 秒/Safari/明文由「假设 MiniShop 可以下单，但…」带出，未伪造成实测指标。 |
| 1.5 原则一 | 与 CTFL 原则一一致。放行话术处理得好。「已知问题」用词差。图有 401/BUG-001 错位。见 CH01-0005、0008。 |
| 1.5 原则二 | 穷尽不可能正确。8～20 已标明不要抄进 v1.0（PRD 为 8～16 且须字母数字）。提前点名等价类。见 CH01-0011。 |
| 1.5 原则三 | 尽早测试节省成本，与 CTFL 一致。例子未标明假设草稿。见 CH01-0007。缺一张成本随阶段上升的图（教学审查建议，非错误）。 |
| 1.5 原则四 | 缺陷集群 + 帕累托直觉正确。支付模块无本地非范围声明。见 CH01-0021。 |
| 1.5 原则五 | 已对齐 tests wear out，保留杀虫剂悖论旧称，并肯定回归价值。与 CTFL 4.0.1 一致。标题「逐渐失效」偏强。见 CH01-0029。 |
| 1.5 原则六 | 上下文依赖正确，银行 vs 游戏例子合适。无「万能清单」。无问题。 |
| 1.5 原则七 | 无缺陷谬论与 CTFL absence-of-defects fallacy 一致；用「符合规格 ≠ 满足需要」代替 V&V 英文三角，方向对。残留确认测试预告。见 CH01-0022。 |
| 1.5 总结七条 | 与正文同向，可作记忆钩。无问题。 |
| 1.6 每天在做什么 | mermaid 标明不是所有团队固定流程。购物车问题清单具体。「v1.0 没有删除购物车接口，也没有结算页」与 `server.py` 仅 GET `/api/cart`、POST `/api/cart/items`、无 checkout 一致。回归想到登录和创建订单，好。无问题。 |
| 1.7 测试 vs 开发 | 表和「共同对质量负责」正确，未写成对立。缺测试 vs 调试。见 CH01-0016。 |
| 1.8 岗位 | 内容作为地图可用；「接口测试是能力不一定是岗位」写得好。星级过高，工具名单过早。见 CH01-0009。 |
| 1.9 职业发展 | 常见国内路线，未承诺薪资/职称。⭐⭐ 合适。无问题。 |
| MiniShop 工作场景 | 个人实践项目、第 19 章前教学约定、v1.0 非范围、实操 1-1 命令，口径正确。面试口头回答「测试不只是找 Bug」可用。 |
| 常见错误 1–5 | 覆盖质量标准禁止的两条绝对化（没发现 Bug、必须等开发完成），修正正确。第 5 条「安全性」见 CH01-0028。 |
| 面试角度 | 四问都要求理解而非只背名称。星级见 CH01-0023。未把公式当作唯一标准答案，错失巩固机会。 |
| 小练习 + 答案 | 见第 11 节。答案与题对应，独立作答一致。未覆盖公式。见 CH01-0015。 |
| 检查清单 | 14 项可口头复述。未单列「能用公式拆一次测试」。 |
| 自测门槛 | 第 0 条要求跑 1-1，比旧版可判定。仍缺自己补判定。见 CH01-0020。第 4 条「至少答对 7 题」可操作。 |
| 本章总结 | 五条正确，未包含公式原句（可视为有意降载）。「安全」见 CH01-0028。 |
| 下一章预告 | 与第 2 章主题（流程、提测、Sprint、回归）一致，未越界讲完 SDLC。 |
| 可运行性说明 | 「概念正文没有 Python/SQL/curl/pytest 片段」属实。配套 1-1 本机 ✅。 |
| 参考资料 | ISTQB、ISO 链接均有效，版本声明与页面一致。见第 18 节。 |

## 8. 代码问题

实操 1-1 本机结果：

```
python3 practice/run.py 1-1          → exit 0，复现 BUG-001，写出 validation/latest.json
python3 practice/run.py 1-1 --check  → 3 tests, OK, 约 1.0s
python3 practice/run.py 1-1 -- --arm observe  → 只打印臂 A，exit 0
python3 practice/run.py 1-1 -- --arm oracle   → 只打印臂 B，exit 0
python3 practice/run.py 1-1 -- --arm full     → 仍打印 A+B+C，exit 0
```

`latest.json`（本机 2026-09-10T03:53:47Z）：`violates_r_search: true`，`bug: BUG-001`，`item_count: 3`。

| 点 | 结论 |
| --- | --- |
| 语法 / 标准库 / 临时 MiniShop / 不占 8765 | 成立。`MiniShopLab` 用端口 0 + 临时库。 |
| 臂 A 无结论用语 | 成立。输出无 BUG-001、无「不符合」。 |
| 臂 B 不发 HTTP | 成立。但判定字符串泄漏实现结论。CH01-0001。 |
| 臂 C 证据路径 | 成立。相对仓库根的路径打印正确。 |
| `count == 3` 当 oracle | 脆。CH01-0013。 |
| `--arm full` | 与 `all` 同行为。CH01-0014。 |
| `arm_full` 的 `base_url` | 未使用。CH01-0026。 |
| unittest 覆盖 | 只锁结构（A 无结论、B 无 HTTP、C 写 JSON），不锁教学不变量「B 不准剧透」。 |
| `_http.py` / `_minishop.py` | 标准库，错误信息可读。第 1 章读者被要求 Skip，合理。 |
| 章内 Python/SQL/curl | 无。bash 仅一条入口命令，已跑通。 |

章内 mermaid 流程图语义正确，不是可运行代码。

## 9. 图片问题

六张 PNG 均实际打开，并对照同名 HTML。均为概念示意图，不是过时 GUI 截图。HTML 与 PNG 文案一致。

IMG-CH01-001
文件：`chapters/assets/diagrams/ch01-formula.png` + `.html`
出现位置：核心公式节
图片主要内容：三块卡片讲观察/判定/证据缺一不可，例子为空搜索 3 件商品、R-SEARCH、BUG-001。
技术准确性：脊柱对；把 HTTP/SQL/OpenAPI/pytest 写成第 1 章证据形态不准确。
与正文一致性：正文表证据列已改为步骤+输出+缺陷单，图未改。
文字是否正确：中文无错字；「不应当全量结果」与正文「不应当成全量结果」微差。
UI 是否过时：否（概念卡）。
教学价值：高，是全书脊柱图。
可读性：好。
是否需要修改：是
修改建议：三块改为：观察=空白搜索返回 3 件；判定=PRD R-SEARCH 说不应当成全量；证据=步骤、屏幕输出、`bugs/BUG-001.md`。删 OpenAPI/pytest/SQL。caption 可写后面章节会加通道。
最终结论：MODIFY

IMG-CH01-002
文件：`chapters/assets/diagrams/ch01-net-holes.png` + `.html`
出现位置：1.5 原则一
图片主要内容：渔网隐喻；已测 / 网外 / 放行话术。
技术准确性：隐喻对；「错误密码 401」超纲；BUG-001 放在网外错误。
与正文一致性：正文未写 401；正文把 BUG-001 当已发现缺陷。
文字是否正确：有。
UI 是否过时：否。
教学价值：高。
可读性：好。
是否需要修改：是
修改建议：401→「错误密码被拒绝」；网外→未测浏览器/未想到的输入；BUG-001 不要放网外。
最终结论：MODIFY

IMG-CH01-003
文件：`chapters/assets/diagrams/ch01-qa-qc-testing.png` + `.html`
出现位置：1.3
图片主要内容：工厂类比下的 QA/QC/Testing，并提醒工牌英文≠概念。
技术准确性：与 CTFL 1.2.2 同向。测试「提供信息，不保证绝对没有 Bug」正确。
与正文一致性：正文缺类比，图比正文更好教。
文字是否正确：是。
UI 是否过时：否。
教学价值：高。
可读性：好。
是否需要修改：否（建议把类比写回正文，图可 KEEP）
最终结论：KEEP

IMG-CH01-004
文件：`chapters/assets/diagrams/ch01-quality.png` + `.html`
出现位置：1.4
图片主要内容：能下单 ≠ 质量好；四卡压缩九特性。
技术准确性：未使用 2011 旧名；caption 补了可维护性/灵活性/Safety。可靠/安全合并略混。
与正文一致性：与 20 秒、Safari、明文、qty=11 一致。
文字是否正确：是。
UI 是否过时：否。
教学价值：高。
可读性：好。
是否需要修改：可选。见 CH01-0031。
最终结论：KEEP（可选 MODIFY 安全卡标题）

IMG-CH01-005
文件：`chapters/assets/diagrams/ch01-static-dynamic.png` + `.html`
出现位置：1.1
图片主要内容：左静态审草稿，右动态点登录。
技术准确性：静态/动态定义对。静态卡同时写「还没有页面」和「仓库 BUG-001」自相矛盾。
与正文一致性：正文开头已拆两个故事，图未拆干净。
文字是否正确：是。
UI 是否过时：否。
教学价值：高。
可读性：好。
是否需要修改：是
修改建议：静态卡只留草稿缺口；删「仓库对照 R-SEARCH；实现见 BUG-001」。
最终结论：MODIFY

IMG-CH01-006
文件：`chapters/assets/diagrams/ch01-tester-dev.png` + `.html`
出现位置：1.7
图片主要内容：同一登录框，开发问如何实现，测试问边界/权限/回归。
技术准确性：对。年龄边界与 1.2 例子呼应。
与正文一致性：与 1.7 表一致。
文字是否正确：是。
UI 是否过时：否。
教学价值：高。
可读性：好。
是否需要修改：否
最终结论：KEEP

缺图（非错误，建议）：原则二组合爆炸、原则三缺陷成本随阶段上升、原则七规格符合 vs 用户要的。渔网图只覆盖原则一。

## 10. 表格问题

表 1（核心公式，第 54–58 行）

| 列 | 结论 |
| --- | --- |
| 观察 | MiniShop 空搜索返回 3 件，与实操、证据文件一致。 |
| 判定 | 写成「空关键字不应当成全量结果」，比 PRD 单元格干净（PRD 夹带实现备注）。表本身可用。 |
| 证据 | 已改为步骤+输出+缺陷单，适合第 1 章。与公式图不一致，见 CH01-0004。 |

表 2（开发 vs 测试，第 309–315 行）

无技术错误。代码要求一行避免了「测试不必会代码 / 测试必须会代码」的绝对化。未提调试，见 CH01-0016。

实操 README 臂对照表：臂 B「不知道实现违不违反」与打印原文冲突，见 CH01-0001。臂 A/C 描述与运行输出一致。

## 11. 练习与答案问题

### 11.1 章内练习（先独立作答，再对答案）

练习 1：哪一个更准确？独立答案 **C**。教材答案 C。一致。A 穷尽、B 原则一反面、D 常见错误 2。

练习 2：需求评审问中文/空格是否算测试？独立答案：算，这是静态测试/需求评审，用来发现歧义、遗漏、不可测边界。教材：属于测试，提前发现歧义遗漏和边界不清。一致。教材未点名「静态测试」，可接受。

练习 3：功能都能用但每页 15 秒。独立答案：不能简单说质量好；功能适合性可能过关，性能效率差；是否达标取决于项目阈值。教材同向。一致。

练习 4：1000 条用例无 Bug 能否说系统没有 Bug？独立答案：不能。原则一。教材同向。一致。

练习 5：为何不能测完密码所有输入？独立答案：组合爆炸，穷尽测试不可能。教材同向。一致。

练习 6：支付模块历史缺陷多，如何分配？独立答案：按风险给该模块更多资源，缺陷集群。教材同向。一致。支付非 MiniShop v1.0，题干是通用情景，不判答错。

练习 7：完全按需求实现、无严重 Bug、用户仍觉得不好用。独立答案：无缺陷谬论。教材同向。一致。

练习 8：为何不是敌人。独立答案：职责不同，质量目标相同；提缺陷是为了早暴露风险。教材为参考答案、合理表达即可。一致。

【ANSWER VERIFICATION FAILED】：无。

缺口：没有公式拆解题。见 CH01-0015。八题全是识别/口述，没有「改一个输入」。对导论章可接受，但对已提供可运行实操的章偏弱。

### 11.2 实操 README 三问（独立作答；无印刷答案）

1. 为什么「系统返回了 3 件商品」单独不能叫测试结论？  
   独立答案：这只是观察。没有 R-SEARCH 这类尺子，3 件可能对也可能错，不能下通过/失败。

2. 为什么只读 PRD 也不能说已经测过搜索？  
   独立答案：那只是判定。没有向系统要一次实际结果，不能声称测过实现。即使本文库 PRD 已写「当前不符合」，那句话本身仍要靠观察复核，否则只是文档主张。

3. 发现了问题却不写证据，开发说明天是好的，如何证明？  
   独立答案：几乎无法证明，只能再跑一遍。步骤、输出、缺陷单才能让别人独立复核。

无法对印刷答案。不判 FAILED。见 CH01-0030。

### 11.3 阶段测验中覆盖第 1 章的题（先独立作答）

只审题 1、2、9、10。题 3–8 属第 2/3/7 章，不在本审计展开。

题 1（必过）：为什么「这次没发现 Bug」不能写成「系统没有 Bug」？  
独立答案：测试只能表明发现了缺陷/失效，不能证明没有缺陷。未测路径、未想到的数据、环境差异都可能藏问题。  
教材：测试只能证明发现了失效，不能证明没有缺陷。……  
一致。术语「失效 vs 缺陷」见 CH01-0027。

题 2：QA、QC、Testing 用一句话区分。  
独立答案：QA 关注过程如何建立/改进质量并提供信心；QC 关注产品是否达到质量要求；Testing 通过评审、分析、设计、执行等活动获取质量信息，是 QC 的主要手段。岗位名称会混用。  
教材同向。一致。

题 9：哪句正确？独立答案 **C**（需求和设计工作产品可以接受静态测试）。A、B 为本章明确反对的绝对化；D 混名。教材 C。一致。

题 10：MiniShop 应被介绍成什么？独立答案：个人软件测试实践项目。教材同句。一致。本章场景导入现已有这句，只读第 1 章可以对上（C01-5 已修）。

【ANSWER VERIFICATION FAILED】：无。

## 12. 初学者理解障碍

标记 【Beginner Friction】：

1. 开篇登录失败用了真实会成功的账号，随后实操又换成空搜索。两条故事抢「仓库里的那个 Bug」。CH01-0002。
2. 空搜索同时是「草稿没写清」和「PRD 已写清、实现违反」。1.1 开头拆开，后文和图又合并。CH01-0006、0007。
3. 臂 B 屏幕上先剧透 BUG-001，再问「你说不准」。CH01-0001。
4. 公式图/实操输出出现 HTTP、SQL、OpenAPI、pytest、401、GET。前置知识承诺零基础。CH01-0004、0005、0019。
5. 1.4 九特性中英对照 + Security/Safety 之后，立刻说不必背。CH01-0010。
6. 1.5 七条原则连发，原则二点名第 5 章技法。CH01-0011。
7. 1.2 的 9999 例子被 qty=10/11 打断。CH01-0012。
8. 学习目标把 QA/QC、七原则、岗位一次列完，阅读提示又说先只记公式和原则一。目标清单本身就是摩擦。
9. 实操声称「可改的输入」其实改不了被测关键字。CH01-0018。
10. 「确认测试」指向第 2 章，原则七正在讲另一件事。CH01-0022。

能跟住的部分：登录/空搜索的三块拆解、渔网隐喻、能下单不等于质量好、开发测试问不同的话、常见错误五条。这些应保留。

## 13. 岗位能力缺口

标记 【Job Reality Gap】：

1. 测试 vs 调试未讲。入职后最常见的角色边界之一。CH01-0016。
2. 公式作为工作口令很有用（没尺子别下结论、没证据别扯皮），但真实测试还有范围、覆盖、风险、入口/出口。后文「可靠测试 = …」有补，却不够显眼。
3. 1.8 岗位地图对校招浏览有用，当成 ⭐⭐⭐ 会让人以为初级岗要同时会 JMeter/Playwright/测开。国内招聘把测试写成 QA Engineer 这一点本章写对了。
4. 缺陷报告要素在 1.6 点到环境/步骤/实际/预期/截图，方向对，但没有让学生写一张（那是 6-1）。第 1 章可以只要求「指到 BUG-001 文件」。
5. error / defect / failure 未引入。ISTQB 1.2.3 有，工作里「这是缺陷还是环境问题」每周都发生。可作建议新增，不必当 P1。
6. 实操成功标准是复现故意开放的 BUG，不是修好。这一点非常符合岗位现实（以及本仓库诚实证据原则），应保留。

## 14. 建议删除内容

1. 判定原文和臂 B 输出里的「（当前实现不符合，见 BUG-001）」。规则留下，实现结论移走。
2. 公式图中的 OpenAPI / pytest / SQL 堆砌。
3. 渔网图「错误密码 401」、把 BUG-001 放在网外。
4. 静态图里「仓库对照 R-SEARCH；实现见 BUG-001」。
5. 原则七末句对第 2 章「确认测试」的预打补丁。
6. 原则二当前句里的「等价类、边界值」六字（可改成「第 5 章再教怎么抽」）。
7. 1.8 的 ⭐⭐⭐（不是删整节，是降星；整节可保留为地图）。

不要删：MiniShop 个人实践项目定性、原则五的 tests wear out 对齐、QA 岗位名混用说明、v1.0 非范围、实操 1-1 本身、常见错误里对两条禁止绝对化的修正。

## 15. 建议新增内容

1. 明确一句：公式是教学模型，ISTQB 定义是「一组发现缺陷、评价工作产品质量的活动」。
2. 测试 vs 调试短框（发现失效 vs 修代码）。
3. 练习：用观察/判定/证据拆空搜索；只跑 `--arm observe` 自己写判定。
4. 原则三成本图（同一缺口越晚越贵）。可选：原则二组合爆炸图、原则七规格 vs 用户目标图。
5. 1.3 正文写入工厂类比，不把类比只放在 PNG。
6. （可选，非阻塞）error/defect/failure 三词各举登录一例，或明确「留给第 6 章」。

## 16. 建议重写内容

1. **场景导入**：登录假设与仓库真实账号脱钩，或改用 BUG-001 开篇。见 CH01-0002。
2. **臂 B / PRD R-SEARCH 单元格**：规则与实现备注分离。见 CH01-0001。
3. **核心公式段「三块缺一不可」**：改成有适用范围的教学模型，并消解与「评审也是测试」的冲突。见 CH01-0003。
4. **1.4 坡度**：反例和图在前，九特性作查阅。见 CH01-0010。
5. **三张图重导出**：`ch01-formula`、`ch01-net-holes`、`ch01-static-dynamic`。见第 9 节。
6. **1.8 开头**：降星 + 「第一次只看功能测试」。

不建议整章推倒。骨架（公式、静态/动态、七原则、质量多维、MiniShop 诚实边界、可运行 1-1）应保留。

## 17. 本章结论

**C 明显需要修改**

不是 E：世界观、七原则、ISO 25010:2023 现用名、QA/QC 分层、禁止的错误绝对化、MiniShop 个人项目定性、实操能跑且能复现仍开放的 BUG-001，这些已经够用，不需要重新设计章节。

不是 A/B：脊柱实验的臂 B 在屏幕上剧透答案；开篇缺陷故事与仓库登录事实相反；教学审查已指出的图/星级/ISO 坡度只修了一部分。这些会把第 1 章最想教会的那句话教拧。

发布建议：修 CH01-0001、CH01-0002，并同步三张图与臂 B 文案后，可再评是否升到 B。当前按独立审计不能给发布线 90 分。

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `reviews/_full-audit-2026-09-10/AUDIT_PROGRESS.md`（进度表，未当结论）
- `reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`（占位，未当结论）
- `chapters/01-software-testing-intro.md`（全文）
- `practice/01-observation-oracle-evidence/README.md`
- `practice/01-observation-oracle-evidence/main.py`
- `practice/01-observation-oracle-evidence/tests/test_lab.py`
- `practice/01-observation-oracle-evidence/validation/latest.json`（跑完后）
- `practice/run.py`、`practice/_http.py`、`practice/_minishop.py`
- `practice/README.md`、`practice/STATUS.md`
- `chapters/quizzes/stage-1-foundations.md`（只审第 1、2、9、10 题）
- `chapters/quizzes/README.md`（确认阶段 1 覆盖第 1/2/3/7 章）
- `reviews/chapter-01-review.md`（线索）
- `reviews/_pedagogy-2026-09-10/ch01.md`（线索）
- `README.md`、`docs/COURSE_CONTROL.md`、`docs/COURSE_OUTLINE_v1.2.md`、`docs/LEARNING.md`、`standards/QUALITY_STANDARD_v1.0.md`
- `project/minishop/docs/PRD.md`（R-SEARCH、R-PASS、教学数据）
- `project/minishop/bugs/BUG-001.md`
- `project/minishop/evidence/http/03-products-empty-keyword.txt`
- `project/minishop/tests/test_api.py`（仅核登录 200 vs 场景失败）
- `project/minishop/server.py`（种子用户、空搜索实现、无删除购物车/结算）
- 示意图 HTML+PNG：`ch01-formula`、`ch01-net-holes`、`ch01-qa-qc-testing`、`ch01-quality`、`ch01-static-dynamic`、`ch01-tester-dev`
- `chapters/assets/diagrams/README.md`

未读其他章正文。

### 实际跑过的命令与结果摘要

| 命令 | 结果 |
| --- | --- |
| `python3 --version` | Python 3.14.3 |
| `python3 practice/run.py 1-1` | exit 0。臂 A：HTTP 200，items 数量 3，无通过/失败。臂 B：打印 R-SEARCH 且含「当前实现不符合，见 BUG-001」，无 HTTP。臂 C：结论不符合 R-SEARCH，写出 `practice/01-observation-oracle-evidence/validation/latest.json`。 |
| `python3 practice/run.py 1-1 --check` | `Ran 3 tests in 1.040s` **OK** |
| `python3 practice/run.py 1-1 -- --arm observe` | 仅臂 A，exit 0 |
| `python3 practice/run.py 1-1 -- --arm oracle` | 仅臂 B，exit 0（含剧透句） |
| `python3 practice/run.py 1-1 -- --arm full` | 打印 A+B+C，与 `all` 相同，exit 0 |

未改教材正文、practice、project。

### 外部核查过的条目

| 条目 | 来源 | 本章是否对齐 |
| --- | --- | --- |
| CTFL 页面提供 Syllabus v4.0.1 | 打开 `https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/`，确有 “ISTQB CTFL Syllabus v4.0.1” 下载 | 参考链接有效 |
| testing 定义 | CTFL 1.1（ASTQB 转述）：a set of activities to discover defects and evaluate the quality of software work products；Glossary：evaluates the quality of a component or system and related work products | 1.1 完整表述接近；公式不是 ISTQB 原句 |
| Testing vs debugging | CTFL 1.1.2 | 本章未讲 |
| Testing vs QA/QC | CTFL 1.2.2：Testing is a form of QC；QC product-oriented corrective；QA process-oriented preventive。Glossary：QA = activities focused on providing confidence that quality requirements will be fulfilled；QC = activities designed to evaluate the quality of a component or system | 1.3 同向，简化可接受 |
| 七原则 | ASTQB 1.3 转述 CTFL 4.0：presence not absence；exhaustive impossible；early testing；defects cluster；tests wear out；context dependent；absence-of-defects fallacy。原则五旧称 pesticide paradox | 1.5 对齐 4.0.1 名称；原则五正文正确 |
| ISO/IEC 25010:2023 | 打开 `https://www.iso.org/standard/78176.html`：Edition 2，2023-11，九特性。ANSI/arc42：Usability→Interaction Capability，Portability→Flexibility，新增 Safety | 九特性现用名正确，未把 2011 旧名当真 |
| Security vs Safety | ISO 25010:2023 将 Safety 提升为顶层特性；Security 仍为信息/系统保护 | 1.4 区分正确 |
| MiniShop 登录 | `test_login_ok`：13800138000 / Test1234 → 200 | 场景「登录失败」与仓库相反 |
| MiniShop 空搜索 | 证据文件 HTTP 200、三件 SKU；server 对 blank keyword 返回全表 | 实操复现成立 |
| MiniShop 无结算页/无删购物车接口 | `server.py` 无 checkout、无 do_DELETE cart | 1.6 陈述正确 |
| 密码规则 | PRD R-PASS 8～16 且须字母数字 | 原则二 8～20 已标明不要抄 |
| 外部链接可达性 | ISTQB、ISO 页面均打开成功 | 无死链 |

Glossary 站点 `glossary.istqb.org` 本次直接打开未返回正文（页面无内容），定义改用 web_search 快照 + CTFL 1.2.2 转述交叉核对，不单靠记忆。

未购买 ISO 全文，九特性名称与 2011→2023 变更依据公开预览与 arc42/ANSI 引述；若需子特性级原文，标记为已用二级来源，不假装读过付费标准全文。
