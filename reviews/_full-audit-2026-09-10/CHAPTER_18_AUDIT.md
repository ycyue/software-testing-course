# Chapter 18 Audit

审计对象：`chapters/18-performance-testing.md`（性能测试基础）  
审计角色：Chapter-Audit-Agent-18  
日期：2026-09-10  
范围约束：只审第 18 章及明确列出的相关文件；不审其他章正文。  
先前 `reviews/` 只作线索，结论均为本轮独立复核。

## 1. Coverage

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 章节正文 `18-performance-testing.md` | 1 | 1 | 0 |
| 标题 H1–H3（不含代码围栏内作业模板标题） | 51 | 51 | 0 |
| 正文段落（含列表项与声明句，约） | 99 | 99 | 0 |
| 表格 | 4 | 4 | 0 |
| 代码围栏 | 6 | 6 | 0 |
| mermaid 示意图 | 1 | 1 | 0 |
| Python 可运行片段 | 1 | 1 | 0 |
| 打印结果对照块 | 1 | 1 | 0 |
| Linux/Shell 命令（步骤或提及） | 8 | 8 | 0 |
| SQL | 0 | 0 | 0 |
| HTTP 示例 / 路径 | 6 | 6 | 0 |
| 测试用例（工作实战必做 5 项） | 5 | 5 | 0 |
| Bug 示例（库存写成 11 / 非性能缺陷） | 1 | 1 | 0 |
| 常见错误 | 10 | 10 | 0 |
| 面试题 | 6 | 6 | 0 |
| 章内练习题 | 10 | 10 | 0 |
| 章内标准答案 | 10 | 10 | 0 |
| 阶段测验 6 中本章题 | 2（Q2、Q3） | 2 | 0 |
| Markdown 图片引用 | 4 | 4 | 0 |
| 示意图 PNG | 4 | 4 | 0 |
| 示意图 HTML 源 | 4 | 4 | 0 |
| 外部链接（去重后 2 个 URL） | 2 | 2 | 0 |
| 内部链接 | 5 | 5 | 0 |
| `.jmx` 教学骨架 | 1 | 1 | 0 |
| `practice/README.md` 18-1 行 | 1 | 1 | 0 |
| `practice/STATUS.md` 18-1 行 | 1 | 1 | 0 |
| 检查清单项 | 11 | 11 | 0 |
| 自测门槛 | 4 | 4 | 0 |
| 参考资料条目 | 8 | 8 | 0 |

Coverage：**100%**。未检查 = 0。

未执行（已在对应单元标明，不计入“未检查”）：本机无 `jmeter` 命令，未打开 JMeter GUI，未跑 `jmeter -n`。XML 已用 `xmllint` 与 `ElementTree` 解析；`GET http://127.0.0.1:8765/api/products` 已对运行中的 MiniShop 复验 200。

## 2. 总评分

| 项目 | 得分 |
| --- | ---: |
| 技术准确性 | 8/10 |
| 岗位实用性 | 8/10 |
| 完整性 | 8/10 |
| 初学者友好度 | 7/10 |
| 教学顺序 | 8/10 |
| 代码质量 | 8/10 |
| 实操质量 | 8/10 |
| 练习质量 | 8/10 |
| 图片质量 | 6/10 |
| **总体** | **82/100** |

评分依据：负载/压力/耐久、并发≠TPS、Elapsed/Latency、授权纪律、未跑 GUI 的诚实披露均正确，且未把教学数字写成 MiniShop SLA。扣分集中在：（1）名为 P95 的图把 18.4 图注贴错；（2）百分位节唯一算例停在平均/中位/最大，练习 2 也不问 P95；（3）`.jmx` 开了 Functional Test Mode、没有 Assertion，与官方加压纪律和正文“先看功能断言”不完全对齐；（4）`python3 run.py serve` 未给工作目录；（5）practice 把 18-1 写成必须跑的 JMeter，章内过关其实是书面清单。

不因“作者没点 JMeter GUI”扣技术分。该项是诚实证据，不是知识错误。

质量标准 20 项 DoD 本轮判断：**18/20**。不通过项：第 13 项（`ch18-p95` 图注与本节打架）；第 17 项部分不满足（百分位是 ⭐⭐⭐，练习 2 不覆盖 P95）。属“修正后发布”，不是可维持原样发布。

本章结论：**C 明显需要修改**。无 P0；两处 P1 都落在本章标题概念“百分位 / P95”上。

## 3. P0

无。

未发现：把未跑压测写成已完成；把教材毫秒/TPS 写成 MiniShop 冻结 SLA；可抄的裸 `/login`；GET/POST 安全神话当正说；对公网加压当作业；订单状态机；验证码/优惠券当 v1.0 契约。

## 4. P1

```
## ISSUE
ID：CH18-0001
文件：chapters/assets/diagrams/ch18-p95.html ；chapters/assets/diagrams/ch18-p95.png ；chapters/18-performance-testing.md
章节：第 18 章
小节：18.2 响应时间与百分位
精确位置：HTML `<p class="caption">`；PNG 底部图注；正文 L112 引用 `ch18-p95.png`
原文：示意图：并发人数 ≠ TPS。50 线程共用一个教学账号，测的是单用户冲突，不是系统容量。
问题等级：P1
问题类别：IMG
问题说明：P95 柱状图的标题、lead、柱子都在讲五个样本 100/110/120/200/800 与平均值藏不住 800 ms，caption 却整段复制了 18.4「并发 ≠ TPS / 单账号冲突」。PNG 已带这句，read_file 打开可见。
为什么有问题：读者在百分位节看到的第一句图注与本节无关，且与同章 `ch18-tps-concurrency` 图注重复。文件名、alt（「五个样本里平均值藏不住 800 ms」）和图注三套口径。零基础会以为 P95 就是并发人数。
依据：本轮打开 HTML+PNG；对照 18.4 正文 L149；质量标准「图表确实帮助理解」。
建议修改：改 caption 并按 diagrams/README 重截 PNG；柱上标 P50 与尾部。
推荐替换文本：示意图：平均 266 ms 看起来还行，已经有人等到 800 ms。P50 看中间那截（120）；P95/P99 看红柱这一侧。五个点的百分位算法以项目约定为准，800 ms 不是 MiniShop SLA。
```

```
## ISSUE
ID：CH18-0002
文件：chapters/18-performance-testing.md
章节：第 18 章
小节：18.2；练习 2 / 答案 2
精确位置：L93–117；L399–401；L443
原文：五个教学样本只打印平均 266.0、中间值 120、最大值 800。随后定义百分位，但没有在同一组数上指出 P50/P95 大约落在哪。练习 2 问平均值、中间值、最大值；答案同样不停在 P95。
问题等级：P1
问题类别：PED / TERM / EX
问题说明：本节标题是「响应时间与百分位」，图文件名是 `ch18-p95`，学习目标要求「解释响应时间、百分位，以及为什么不能只看平均值」。唯一数值例子只训练平均/中位/最大。
为什么有问题：读者能复述「不要只看平均」，不一定能指着这五根柱说 P95 看的是尾部而不是 266。n=5 时不同算法会得到不同数（最近秩 P95=800；Excel PERCENTILE.INC ≈680），正文已说「算法以项目约定为准」，更应在同一组数上演示「为什么五个点算不出可写进 SLA 的 P95」，而不是完全不算。
依据：本轮 Python 3.14.3 复算平均/中位/最大与教材一致；百分位两种常用取法如上。ISTQB/工程实践用百分位描述尾部，不是用最大值代替定义。
建议修改：在打印结果后补一段教学解释；练习 2 答案加半句。不要把 680 或 800 写成 MiniShop SLA。
推荐替换文本：这五个点里：P50 就是中间值 120 ms（典型）。约 4/5 的请求不超过 200 ms，再往上的尾部是 800 ms。教学上把 P95 理解成「大部分请求里偏慢的那一截」，它靠近红柱，而不是平均值 266 ms。五个点太少，最近秩会落到 800、线性插值大约 680，以项目约定为准。面试先能说明为什么只报 266 会把已经很慢的人藏起来。800 ms 是教学样本，不是 MiniShop SLA。
练习 2 答案末加：P50=120；P95 看尾部（靠近 800），不要把平均 266 当成「大家都还行」。
```

## 5. P2

```
## ISSUE
ID：CH18-0003
文件：chapters/18-performance-testing.md
章节：第 18 章
小节：场景导入
精确位置：L51
原文：有模型，才能写：在什么环境、多少虚拟用户、爬坡多久、P95 是多少、错误率是多少、当时 CPU/内存/磁盘怎样。
问题等级：P2
问题类别：PED / SEQ
问题说明：百分位尚未定义就抛出 P95。
为什么有问题：场景导入的职责是建立「功能绿 ≠ 晚高峰」。P95 是 18.2 的目标词，提前出现会让零基础把「P95」当成必须先背的缩写。
依据：质量标准「生活类比 → 简单模型 → 正式定义」；教学尺「后文不调用尚未教的技能」。
建议修改：场景导入改用「响应时间尾部」，把 P95 留到 18.2。
推荐替换文本：有模型，才能写：在什么环境、多少虚拟用户、爬坡多久、响应时间的尾部怎样（百分位怎么看，见 18.2）、错误率是多少、当时 CPU/内存/磁盘怎样。
```

```
## ISSUE
ID：CH18-0004
文件：chapters/18-performance-testing.md
章节：第 18 章
小节：18.7 JMeter 入门
精确位置：L200；L227–236
原文：需要 Java 才能运行。从 Apache JMeter 下载当前稳定版。… 若只想看通不通，可用 GUI 点绿色启动…
问题等级：P2
问题类别：PED / SEQ
问题说明：章标 ⭐⭐、LEARNING.md 将 17–18 标为了解即可、自测门槛不要求安装。18.7 开篇仍是下载令 + 点绿色启动。
为什么有问题：了解章读起来像必须装工具才能过关。Java 版本也未写：当前稳定线 JMeter 5.6.3 要求 Java 8+（推荐 17+）。
依据：`docs/LEARNING.md`「⚪ 了解即可」；质量标准第三梯队；Apache JMeter Changes / dist 页：5.6.3 requires Java 8+。自测门槛 L469–474 无「必须跑通 JMeter」。
建议修改：明示不安装也能完成本章；下载与点启动只放在「若本机已安装」。
推荐替换文本：**不必为了本章去安装 JMeter 或 Java。** 过关看的是：能认 Test Plan / Thread Group / Sampler / Listener、能区分 GUI 与非 GUI、能完成下面的问题清单。若将来要在授权环境自己跑，需要 Java（JMeter 5.6.x 为 Java 8+，推荐 17+），安装向导以官网为准。点绿色启动也只是 1 用户冒烟，不是负载，更不是学会的条件。
```

```
## ISSUE
ID：CH18-0005
文件：chapters/18-performance-testing.md ；practice/README.md ；practice/STATUS.md
章节：第 18 章
小节：MiniShop 工作实战
精确位置：正文 L265–267；practice/README.md 18-1 行；STATUS.md「18-1 JMeter Incomplete」
原文：章内标题下直接「不要对未授权系统加压」；practice 表：18-1 🚧 有 `.jmx` 骨架和步骤，未安装、未跑 JMeter GUI；STATUS：Incomplete。
问题等级：P2
问题类别：PED / PRE
问题说明：质量标准要求写清类型（✅/📖/🚧）。章内无徽章。practice 把 18-1 命名为 JMeter 且 Incomplete，读者容易读成「必须跑通 GUI 才算学会」。
为什么有问题：本章真正可验收的过关物是 `exercises/chapter-18-minishop-performance.md` 清单。🚧 应只表示骨架未执行，不是过关条件。
依据：`standards/QUALITY_STANDARD_v1.0.md` 第七节；`practice/README.md` L71；`practice/STATUS.md` L36。
建议修改：章内第一段标明 📖 清单过关；practice 18-1 名称改为「性能问题清单 + jmx 骨架」。
推荐替换文本：类型：📖 书面清单（过关产出）。仓库另有教学骨架 `.jmx`，practice 表记为 🚧 只表示审查未安装、未跑 GUI，不是「你必须跑通 JMeter 才算学会」。不要对未授权系统加压。不要把下面的数字抄进简历当已测 SLA。保存：`exercises/chapter-18-minishop-performance.md`。
```

```
## ISSUE
ID：CH18-0006
文件：project/minishop/jmeter/minishop-get-products.jmx ；chapters/18-performance-testing.md
章节：第 18 章
小节：18.7；`.jmx`
精确位置：jmx L4 `TestPlan.functional_mode`=true；HTTPSampler 后无 Assertion；正文 L210、L242、L216–221
原文：骨架勾选 Functional Test Mode；Listener 为 View Results Tree；正文元件表有 Assertion，纪律写「先小流量看功能断言」，树里却没有 Assertion 节点。
问题等级：P2
问题类别：CODE / TEST / JOB
问题说明：官方 Best Practices 16.7 明确：加压不要用 functional mode，不要在负载中开 View Results Tree。Functional mode 会把响应体写入结果文件，拖垮压测机。JMeter 默认把 HTTP 4xx/5xx 当失败（Response Assertion 文档：4xx/5xx normally unsuccessful），但 200 的错误页/空 JSON 仍算成功——没有断言就统计不出「业务错误率」。
为什么有问题：1 用户冒烟勾 functional mode 可以理解，但正文完全没解释这个勾选。学生若把这份 jmx 线程改大，正好踩中官方禁止项。元件表教了 Assertion，可抄树和仓库文件都没有。
依据：https://jmeter.apache.org/usermanual/best-practices.html 「Don't use functional mode」「Don't use View Results Tree… during the load test」；Component Reference Response Assertion：HTTP 4xx/5xx normally regarded as unsuccessful。本轮未装 JMeter，GUI 勾选是否原样显示标 【External Verification Required】。
建议修改：正文声明：骨架为功能冒烟，functional mode 仅调试用，加压前必须关掉并禁用 View Results Tree。树与 jmx 增加 Response Assertion：Response Code 200（或 Contains `items`）。
推荐替换文本（树）：
Test Plan          functional_mode=true（仅调试；加压必须改 false）
└── Thread Group   threads=1, ramp-up=1s, loops=1
    ├── HTTP Request  GET /api/products
    ├── Assertion     Response Code 200
    └── Listener      View Results Tree（加压时禁用；jtl 用 -l 落盘）
```

```
## ISSUE
ID：CH18-0007
文件：chapters/18-performance-testing.md
章节：第 18 章
小节：18.7 逐步打开 第 1 步
精确位置：L229
原文：确认只对 `127.0.0.1`，教学服务已启动：`python3 run.py serve`。
问题等级：P2
问题类别：PRE / PED
问题说明：未写必须先 `cd project/minishop`。仓库根没有 `run.py`；根目录执行会失败。`practice/run.py serve` 会被当成「没有编号 serve」。
为什么有问题：这是本章唯一启动命令。装了 JMeter 的读者会卡在服务没起来，误以为 `.jmx` 坏了。
依据：本轮在仓库根执行 `python3 run.py serve` → `can't open file .../run.py`；`python3 practice/run.py serve` →「没有编号 serve」。`project/minishop/README.md` 正确入口是该目录下的 `python3 run.py serve`。
建议修改：补工作目录。
推荐替换文本：1. 确认只对 `127.0.0.1`。在 `project/minishop` 目录启动教学服务：`python3 run.py serve`（浏览器或 curl 访问 `http://127.0.0.1:8765/api/products` 应返回 200）。不要在仓库根目录执行这条命令。
```

```
## ISSUE
ID：CH18-0008
文件：chapters/18-performance-testing.md
章节：第 18 章
小节：18.1 / 18.8 / 工作实战
精确位置：L77「上线前要知道目标流量下会不会崩」；工作实战未写 MiniShop 技术栈限制
原文：上线前要知道目标流量下会不会崩。
问题等级：P2
问题类别：JOB
问题说明：MiniShop 是本机 `ThreadingHTTPServer` + SQLite（`check_same_thread=False`）的教学服务，每次默认 `MINISHOP_RESET=1`。即使授权、即使把线程开大，测到的也是教学进程和本地磁盘，不是可写进简历的容量规划。
为什么有问题：初级最常见的假证据就是「我对本机 Demo 压过 200 线程」。正文禁止生产压测和编造 SLA，但没把「MiniShop 不是容量规划对象」写成硬句子。
依据：`project/minishop/server.py` L13、L32、L545–560；PRD「本机 HTTP」；质量标准「诚实证据」。
建议修改：在 18.8 或工作实战声明中加一句。
推荐替换文本：MiniShop 是个人实践用的本机教学服务（Python HTTP + SQLite），不是生产系统。即使在本机对 `127.0.0.1:8765` 加压，也不得把结果写成容量规划、性能基线或简历里的「完成压测」。本章过关物是问题清单，不是 TPS 数字。
```

## 6. P3

```
## ISSUE
ID：CH18-0009
文件：chapters/18-performance-testing.md
章节：第 18 章
小节：面试角度「为什么要看 P95」
精确位置：L373
原文：四个 100 ms 加一个 800 ms，平均看起来还行，已有人等到 800 ms。
问题等级：P3
问题类别：PED / SEQ
问题说明：18.2 的五个样本是 100、110、120、200、800（平均 266）。面试改成四个 100 加一个 800（平均 240）。
为什么有问题：对照学习的学生会去对数字，发现对不上，怀疑自己算错。
依据：18.2 L94 与面试 L373。
建议修改：面试改用同一组五个数，或标明「换一组更整齐的数」。
推荐替换文本：示例：100、110、120、200、800 ms，平均 266 ms，已经有人等到 800 ms。
```

```
## ISSUE
ID：CH18-0010
文件：project/minishop/jmeter/minishop-get-products.jmx ；chapters/18-performance-testing.md
章节：第 18 章
小节：18.7 教学树
精确位置：正文 L220「Listener View Results Tree / 写 jtl 文件」；jmx L60 `<stringProp name="filename"></stringProp>`
问题等级：P3
问题类别：CODE / TERM
问题说明：树暗示这份计划会写 jtl。仓库文件的 ResultCollector 文件名为空；非 GUI 的 jtl 来自命令行 `-l`，不是这个空 filename。
为什么有问题：学生打开 jmx 找不到「写 jtl」配置，以为文件坏了。
依据：jmx L33–61；官方 `jmeter -n -t plan.jmx -l result.jtl`。
建议修改：树改为「View Results Tree（调试）；jtl 用 `-l` 落盘」。或给 ResultCollector 一个注释字段说明不要在 GUI 填大文件路径。
推荐替换文本：└── Listener      View Results Tree（调试用；真正负载用 `jmeter -n … -l result.jtl`，不要靠这个空 filename）
```

```
## ISSUE
ID：CH18-0011
文件：chapters/18-performance-testing.md
章节：第 18 章
小节：18.1；18.3；18.6
精确位置：L73「时间行为、容量和稳定性」；L123 吞吐定义；L181–183 压力测试
问题等级：P3
问题类别：TERM
问题说明：三处口径可再钉紧，均未教错。（1）ISO/IEC 25010:2023 性能效率 = time behaviour + resource utilization + capacity；「稳定性」更接近可靠性或 ISTQB endurance，正文用稳定性指耐久可以，最好点明。（2）JMeter Glossary 的 Throughput = 全部请求数 / 首末样本墙钟时间，含失败样本；正文先写「每秒成功请求数」再要求分开成功吞吐与错误率——比 JMeter 默认更严，应注明读 Aggregate 时 Throughput 与 Error % 要一起看。（3）ISTQB 压力测试还包括「资源被削减」变体，正文只写超过预期负载。
为什么有问题：初级对照官方术语时会对「稳定性」「Throughput 列含不含错误」产生疑问，不是会把学生教反。
依据：ISO/IEC 25010:2023 3.2；JMeter Glossary Throughput；ISTQB Glossary / CTFL-PT stress testing。
建议修改：18.1 改为「时间行为、容量，以及用耐久观察的稳定性」；18.3 加一句 Aggregate 的 Throughput 含全部样本；18.6 压力行加「或削减资源」。
推荐替换文本：性能测试检查系统在特定负载下的时间行为与容量（ISO/IEC 25010 性能效率），并用耐久测试观察是否泄漏、是否越来越慢。JMeter Aggregate 的 Throughput 按全部样本计算，必须和 Error % 一起读；缺陷里要写成功吞吐。
```

```
## ISSUE
ID：CH18-0012
文件：chapters/18-performance-testing.md
章节：第 18 章
小节：章头重要级别；18.1–18.6 ⭐⭐⭐；本章总结
精确位置：L5「⭐⭐ 常用」；L69–172 各节 ⭐⭐⭐；L478「真正掌握七件事」
问题等级：P3
问题类别：PED
问题说明：章标常用，概念节必须掌握，结尾「真正掌握」比 LEARNING.md「了解即可」重一档。
为什么有问题：星级本身可以「章了解、概念必须能解释」，但「真正掌握七件事」会让学生以为要会做压测。
依据：`docs/LEARNING.md` 第 17–18 章 ⚪ 了解即可；COURSE_OUTLINE 第三梯队。
建议修改：总结改为「真正能解释七件事」；保留 JMeter ⭐⭐、Spike ⭐。
推荐替换文本：本章需要真正能解释七件事（不是要你独立做完一次生产压测）：
```

```
## ISSUE
ID：CH18-0013
文件：project/minishop/jmeter/minishop-get-products.jmx
章节：第 18 章
小节：`.jmx` 完整性
精确位置：HTTPSamplerProxy 缺少 `HTTPsampler.Arguments`、`HTTPSampler.follow_redirects`、`enabled="true"`；根节点无 `jmeter="5.x"`；`ThreadGroup.num_threads` 用 `intProp`（常见导出为 `stringProp`）
问题等级：P3
问题类别：CODE
问题说明：XML 良构，核心字段齐全，预期可导入。缺省属性一般走 JMeter 默认（follow_redirects 默认 true，enabled 默认 true）。未在 GUI 实开，导入体验标外部核验。
为什么有问题：极少数版本/插件对缺 Arguments 节点过敏时，HTTP 取样器面板可能显示异常。不是路径/端口错误。
依据：jmx 全文；Apache JMeter SaveService `jmeterTestPlan version="1.2" properties="5.0"` 为 5.x 常规头。本机无 JMeter → 【External Verification Required】 File → Open。
建议修改：用本机 JMeter 5.6.x 打开一次，另存为完整导出，保持 1 用户 1 循环、`127.0.0.1:8765`、`GET /api/products`。
推荐替换文本：不改正文数字；仅用 GUI Save 生成带默认属性的完整 `.jmx`。
```

## 7. 逐段问题

下列每个内容单元均已阅读。仅列结论；有 ISSUE 的指向 ID。

| 单元 | 位置 | 结论 |
| --- | --- | --- |
| 标题 + 一句话核心 | L1–3 | 通过。「性能是另一把判定尺子；功能绿了不等于扛得住」可过滤 pytest/CI 当性能结论。 |
| 重要级别 / 主案例 | L5–6 | 章 ⭐⭐ 与第三梯队一致；与节内 ⭐⭐⭐ 张力见 CH18-0012。MiniShop 标个人实践，通过。 |
| 这一章解决什么问题 | L8–16 | 通过。正确区分非功能 vs 功能自动化加速；未跑 GUI、非 SLA、骨架路径 `GET http://127.0.0.1:8765/api/products` 与仓库一致。 |
| 学习目标 8 条 | L19–29 | 通过。过关写成清单而不是压测报告，正确。 |
| 前置知识 | L31–36 | 通过。不要求已装 JMeter。第 3、9–11、16、17 章前置合理。 |
| 场景导入 | L38–51 | 教学规则 qty=11→400 已标「教学规则」，未写成冻结契约。P95 提前出现：CH18-0003。 |
| 场景原因列表 | L42–49 | 通过。CPU/内存/磁盘/锁/连接池/网络分层正确。 |
| mermaid 流程 | L53–63 | 通过。「达标也不代表没有性能风险」符合「没发现 Bug ≠ 没有 Bug」。 |
| 授权纪律段 | L65 | 通过。只授权环境；练习以清单为主。 |
| 18.1 类比与定义 | L71–73 | 通过。ISO 25010「性能效率」方向正确；稳定性口径见 CH18-0011。 |
| 18.1 需要它 / 不能替代 | L75–81 | 通过。pytest 绿 ≠ 并发锁正确，略混「并发功能」与「性能」，仍有教学价值。 |
| 18.1 阈值来源 | L83 | 通过。未冻结 MiniShop P95/TPS。 |
| 18.2 响应时间 / TTFB / Elapsed / Latency | L89–91 | 通过。Chrome Timing 仍有 Waiting (TTFB)；JMeter Glossary：Elapsed=至最后一字节，Latency=至第一响应（一般长于一字节）。正文要求看列名、不混工具，准确。 |
| 18.2 Python 样本 | L93–108 | 通过。本轮复算 266.0 / 120 / 800。 |
| 18.2 图 | L112 | CH18-0001。 |
| 18.2 百分位定义与目标写法 | L115–117 | 定义正确；缺同一组数上的 P95 演示：CH18-0002。 |
| 18.3 吞吐教学计算 | L123–125 | 通过。1000/50=20。 |
| 18.3 TPS / QPS | L127–129 | 通过。事务可含多步；QPS 多用于读；不是互相淘汰。 |
| 18.3 成功吞吐 vs 错误率 | L131 | 通过。JMeter Throughput 含全部样本的细差见 CH18-0011。 |
| 18.4 图 + 并发定义 | L137–151 | 通过。50 思考 vs 5 狂点把并发≠TPS 钉住。单账号 `13800138000` 是反例，PRD 教学账号存在。线程≠连接≠CPU 核，正确。 |
| 18.5 资源表 | L157–164 | 通过。`free -h` 限定 Linux；macOS 不能当生产泄漏证据。 |
| 18.5 对照窗口 | L166–168 | 通过。分层定位与第 6、13 章口径一致（本轮不审他章正文）。 |
| 18.6 表 + Spike | L176–185 | 通过。名称跟模型不跟线程数；Spike 标 ⭐。ISTQB 资源削减变体见 CH18-0011。 |
| 18.6 200 线程≠压力；功能未通先不压 | L187–189 | 通过。 |
| 18.7 图 + JMeter 定位 | L195–198 | 通过。不渲染页面、不执行全部 JS，与 Glossary 一致。 |
| 18.7 需要 Java / 下载 | L200 | CH18-0004。 |
| 18.7 元件表 | L204–210 | 通过。Assertion 列入但骨架没有：CH18-0006。 |
| 18.7 官方 5×2×2=20 | L212 | 通过。Building a Web Test Plan 原文即 5 users × 2 requests × 2 loops = 20。禁止压 `jmeter.apache.org` 是对官方入门靶的正确覆盖（官方教程打的是 jmeter 站点）。 |
| 18.7 教学树 | L214–225 | 通过。已与 `.jmx` 同构 `GET /api/products`（旧审查里的 `POST /login` 已不在现行正文）。jtl 表述见 CH18-0010。 |
| 18.7 逐步打开 1–7 | L227–237 | 步骤 3 路径/端口/方法与 jmx 一致。步骤 1 缺 `cd`：CH18-0007。步骤 4–6 纪律正确。命令 `jmeter -n -t … -l result.jtl` 与官方一致。审查未执行 GUI：属实。 |
| 18.7 两条纪律 + k6/Locust | L239–244 | 通过。与 Best Practices 16.7 一致。 |
| 18.8 岗位表 | L248–261 | 通过。初级边界清楚；禁止把 pytest 并发当性能、禁止简历写生产压测。MiniShop 非容量对象见 CH18-0008。 |
| 工作实战 | L265–306 | 五项必做可判对错；禁止订单状态机、禁止编造阈值。缺类型徽章：CH18-0005。 |
| 错误 1–10 | L310–350 | 全部有价值。错误 9 与第 11 章 `free` 边界一致。错误 4/10 守安全与诚实证据。 |
| 面试 6 题 | L354–389 | 结构「结论→示例→边界」可用。数字不一致：CH18-0009。练习 9 的 GET/POST 神话在面试边界也有呼应。 |
| 小练习 1–10 | L393–438 | 覆盖目标。练习 2 未问 P95：CH18-0002。练习 9 干扰项合格。 |
| 答案 1–10 | L440–451 | 与独立作答一致，无 【ANSWER VERIFICATION FAILED】。答案 10 已是 `GET /api/products`（旧 S6-04 已修）。 |
| 检查清单 + 自测门槛 | L455–474 | 通过。门槛不要求跑 JMeter，与了解章定位一致。 |
| 本章总结 | L476–486 | 七件事内容对；「真正掌握」语气见 CH18-0012。 |
| 可运行性说明 | L488–492 | 通过。Python 3.14.3、未装 JMeter、非 SLA，与本轮事实一致。 |
| 参考资料 | L494–503 | 外部链接内容与正文引用一致；内部五条文件均存在。核验日期 2026-09-08 仍适用于 5.6.3 稳定线。 |
| 下一章预告 | L505–507 | 通过。指向第 19 章个人实践项目，未提前讲完 37/1。 |

禁止的错误绝对化（本章检查结果）：

| 禁止项 | 本章 |
| --- | --- |
| GET 不安全、POST 安全 | 未当正说；练习 9-D 列为错误 |
| Cookie/Session/Token 三选一 | 未出现 |
| P0/P1/P2/P3 全球统一 | 未出现 |
| 没发现 Bug = 没有 Bug | mermaid 明确反说 |
| 测试必须等开发全部完成 | 未出现 |
| 接口自动化 ROI 永远最高 | 未出现 |

## 8. 代码问题

### 8.1 Python 教学样本（L95–99）

```python
samples_ms = [100, 110, 120, 200, 800]
print(sum(samples_ms) / len(samples_ms))
print(sorted(samples_ms)[len(samples_ms) // 2])
print(max(samples_ms))
```

本轮 `python3`（3.14.3）输出：`266.0` / `120` / `800`。与正文 L104–108、可运行性说明一致。奇数个样本用 `n//2` 取中位数正确。无语法/import 问题。隐藏依赖：无。

百分位未算：CH18-0002。本轮补充计算（不写入教材数字当 SLA）：最近秩 P95=800；PERCENTILE.INC ≈680。

### 8.2 吞吐算术

`1000 / 50 = 20` 正确。

### 8.3 mermaid

语法合法。节点含义正确。

### 8.4 工作实战 Markdown 模板

结构完整，阈值槽写「待确认」，声明禁止生产加压与编造 SLA。通过。

### 8.5 `.jmx`（逐字段）

| 字段 | 值 | 判定 |
| --- | --- | --- |
| XML 声明 / 根 | `jmeterTestPlan version="1.2" properties="5.0"` | 5.x SaveService 常规头；`xmllint --noout` 通过 |
| Test Plan 名 | MiniShop v1.0 local GET products | 通过 |
| comments | Personal practice. 1 user 1 loop. Not an SLA. Do not run against production. | 通过 |
| functional_mode | true | 冒烟可接受；未解释：CH18-0006 |
| threads / ramp / loops | 1 / 1 / 1 | 与正文一致，不是负载 |
| scheduler | false | 通过 |
| on_sample_error | continue | 冒烟可接受 |
| domain / port / protocol / path / method | 127.0.0.1 / 8765 / http / /api/products / GET | 与 PRD、OpenAPI、server.py 一致 |
| use_keepalive | true | 通过 |
| Listener | View Results Tree，filename 空 | 调试用；jtl 口径 CH18-0010 |
| Assertion | 无 | CH18-0006 |
| 缺省属性 | Arguments / follow_redirects / enabled | CH18-0013 |

本轮对运行中 MiniShop：

- `GET /api/products` → **200**，3 件商品（鼠标库存 10）。
- `GET /products` → 404（旧答案路径不可用）。
- `GET /api/login` → 404（登录是 POST）。

骨架选无认证的商品列表作为 1 枪冒烟，路径正确。

未跑：`jmeter` 不在 PATH。Java 本机为 23.0.1，满足 5.6.x「Java 8+」，但无 JMeter 发行包。【External Verification Required】：GUI File→Open 是否无告警。

官方加压命令 `jmeter -n -t minishop-get-products.jmx -l result.jtl` 形式正确；正文已写「参数以当前手册为准」。不要在未授权环境执行。本轮未执行 `-n`。

### 8.6 逐步打开命令

`python3 run.py serve` 缺工作目录：CH18-0007。  
`jmeter -n …` 未要求对公网运行：通过。

## 9. 图片问题

四张 PNG 均用 `read_file` 打开；四份 HTML 均通读。另检查场景 mermaid。

```
IMG-CH18-001
文件：chapters/assets/diagrams/ch18-p95.png 与 ch18-p95.html
出现位置：18.2 L112
图片主要内容：五根柱 100/110/120/200/800，红柱为 800；标题写平均 266、中间 120、最慢 800。
技术准确性：柱高与数字一致；未标 P50/P95 落点。
与正文一致性：标题/lead 与 18.2 一致；caption 窜到 18.4。
文字是否正确：caption 错误。
UI 是否过时：示意图，不适用。
教学价值：本应讲「平均藏不住尾部」；图注毁掉第一眼。
可读性：柱与数字清楚。
是否需要修改：是
修改建议：改 caption；红柱旁标「尾部 / P95 附近」；第三柱标 P50≈120。按 diagrams/README 重截 PNG。
最终结论：MODIFY
```

```
IMG-CH18-002
文件：chapters/assets/diagrams/ch18-tps-concurrency.png 与 .html
出现位置：18.4 L137
图片主要内容：并发 vs TPS/吞吐 两栏；50 人思考 vs 5 人狂点。
技术准确性：正确。50 秒 1000 次 → 20 次/秒与正文一致。
与正文一致性：一致。caption 补充单账号冲突与 QPS 口径，属于本节范围。
文字是否正确：正确。
UI 是否过时：否
教学价值：高，钉住本章最易混的一对词。
可读性：好
是否需要修改：否
修改建议：无
最终结论：KEEP
```

```
IMG-CH18-003
文件：chapters/assets/diagrams/ch18-load-stress.png 与 .html
出现位置：18.6 L174
图片主要内容：负载 / 压力 / 耐久三问句；lead 写 200 线程低于预期高峰仍是偏小负载。
技术准确性：与 ISTQB 负载/压力/耐久一致。
与正文一致性：一致。caption 强调授权与 1 用户骨架非 SLA。
文字是否正确：正确。
UI 是否过时：否
教学价值：高
可读性：好
是否需要修改：否
修改建议：无（可选：压力卡补「或削减资源」，非必须）
最终结论：KEEP
```

```
IMG-CH18-004
文件：chapters/assets/diagrams/ch18-jmeter-parts.png 与 .html
出现位置：18.7 L195
图片主要内容：Test Plan / Thread Group / HTTP Sampler / Listener 四零件；骨架 GET /api/products；127.0.0.1:8765；审查未装 JMeter。
技术准确性：正确。非 GUI 加压、jtl 落盘与官方一致。
与正文一致性：与现行教学树、`.jmx` 一致。
文字是否正确：正确。未谎称已跑 GUI。
UI 是否过时：示意图不依赖易变菜单文案，符合章头策略。
教学价值：高
可读性：好
是否需要修改：否
修改建议：无
最终结论：KEEP
```

场景 mermaid：KEEP。不是 PNG，已纳入 Coverage。

## 10. 表格问题

| 表 | 位置 | 结论 |
| --- | --- | --- |
| 资源（CPU/内存/磁盘/网络） | 18.5 | 通过。现象与测试含义匹配；`free` 限定 Linux。 |
| 负载/压力/耐久 | 18.6 | 通过。问句与做法对齐。 |
| JMeter 元件 | 18.7 | 通过。Assertion 行与骨架不一致 → CH18-0006。 |
| 初级岗位三列 | 18.8 | 通过。 |
| 工作实战路径表（模板空表） | 工作实战 | 通过。表头足够；学生自填。 |

无表内数字错误。无把 200 ms 写成国际标准。

## 11. 练习与答案问题

### 11.1 独立作答（先于对照教材答案）

**练习 1**  
pytest 绿只说明这些请求的功能断言成立，没有约定负载、百分位、错误率趋势和加压窗口的资源证据，不能写「性能没有问题」。

**练习 2**  
平均 266.0 ms，中间值 120 ms，最大值 800 ms。只报平均会把已经很慢的 800 ms 藏起来。

**练习 3**  
不是一回事。例如 50 个虚拟用户每步后思考 2 秒：并发高、TPS 低；5 个线程无等待死循环：并发低、请求率高。

**练习 4**  
负载：预期高峰下目标能否达到？压力：超过预期后从哪坏、坏了怎样？耐久：较长时间是否泄漏或越来越慢？

**练习 5**  
未授权加压可能影响他人服务或违法。公网站点不是课程压测靶。只在自有或书面授权环境。

**练习 6**  
Thread Group：虚拟用户数与节奏。HTTP Request：真正发请求。Listener：收集/展示结果。`-n` 是非 GUI，避免压测机被界面和实时 Listener 拖垮。

**练习 7**  
不可靠。测到的是单账号锁/会话冲突，不是系统容量。需要足够多的独立测试用户。

**练习 8**  
应强调磁盘空间/I/O 以及应用写日志或写库，不要只写「接口慢」。还要看同一加压窗口的 CPU、内存和数据库。

**练习 9**  
C。A 把功能工具当负载模型。B 把示例当国际标准。D 是 GET/POST 安全神话；登录也不该用安全方法传密码。

**练习 10**  
环境：授权测试环境 `http://127.0.0.1:8765`。接口：`GET /api/products`（或改数量则 `POST /api/cart/items`）。负载：虚拟用户与爬坡待需求确认。P95：待确认。错误率：待确认。不写订单状态名。非正式 SLA。

### 11.2 对照教材答案

| 题 | 结果 |
| --- | --- |
| 1 | 一致 |
| 2 | 数字一致。双方都未写 P95 → 记入 CH18-0002，不是答错 |
| 3 | 一致 |
| 4 | 一致 |
| 5 | 一致 |
| 6 | 一致 |
| 7 | 一致 |
| 8 | 一致 |
| 9 | 一致 |
| 10 | 一致；现行答案已是 `GET /api/products`，与 `.jmx` 一致 |

**【ANSWER VERIFICATION FAILED】：无。**

### 11.3 阶段测验 6（只评第 18 章题）

独立作答：

- Q2：pytest 绿没有约定负载、百分位和资源证据，功能断言不是负载模型。  
- Q3：未授权对公网或生产做 JMeter 可能造成事故或违法；只在自有或书面授权环境；课程未要求打高并发。

对照测验答案：一致。必过题 Q3 口径正确。Q1、Q4–Q10 属第 17/19 章，本 Agent 不审。

### 11.4 练习设计评价

覆盖学习目标中的差别、平均 vs 尾部、并发≠TPS、三种测试、授权、元件、单账号、资源分层、禁止绝对化、目标草稿。缺口：百分位节没有对应的 P95 计算题。工作实战五项可验收。

## 12. 初学者理解障碍

【Beginner Friction】

1. `ch18-p95` 图注讲并发，和刚看完的柱子无关（CH18-0001）。  
2. 场景导入先出现 P95，定义在后（CH18-0003）。  
3. 百分位节算完平均就结束，读者不知道这五根柱的 P95 该指哪一根（CH18-0002）。  
4. 「需要 Java、下载稳定版、点绿色启动」与「不要求安装」并存（CH18-0004）。  
5. practice 表写 🚧 JMeter Incomplete，章内过关是写清单（CH18-0005）。  
6. `python3 run.py serve` 在仓库根会失败（CH18-0007）。  
7. 授权/非 SLA/未跑 GUI 重复密。对了解章是必要诚实，但会打断「先看例子」。属表达密度，不单列 ISSUE。  
8. JMeter Latency ≠ DevTools Latency ≠ 网络工程师的 latency，正文有提醒，仍建议在 18.2 用一列表格三列对照（建议新增，见 §15）。

## 13. 岗位能力缺口

【Job Reality Gap】

1. 缺 Response Assertion 时，200 的业务失败不会进 Error %（CH18-0006）。真实项目先断言再加压。  
2. Functional Test Mode + View Results Tree 是调试组合，不是负载组合。官方写明加压禁用二者。  
3. MiniShop 本机教学栈测不出容量规划（CH18-0008）。  
4. 未提数据准备（CSV 用户）、思考时间元件、集合点；对了解章可接受。入职后这些比「会点绿色启动」更常见。  
5. 未提 coordinated omission / 开环到达率。18.4 已写「虚拟用户或到达率」，够初级。  
6. 初级岗位表写「协助看日志、把慢复现成带 Timing 的缺陷」——这是正确的岗位现实，应保持。

## 14. 建议删除内容

- 不要删授权纪律、非 SLA、未跑 GUI 的声明。  
- 18.7「逐步打开」步骤 4–7 与随后「两条纪律」有重复，可压缩，不是必须删。  
- 不要把 `.jmx` 改回 `/login`。

## 15. 建议新增内容

1. 18.2：同一组五个数上的 P50/P95 教学句（CH18-0002）。  
2. 18.2：一张三列小表——DevTools TTFB (Waiting) / JMeter Latency / JMeter Elapsed。  
3. 18.7：不安装也能过关的明示（CH18-0004）。  
4. 工作实战类型徽章 📖 + 🚧 含义（CH18-0005）。  
5. `.jmx`：Response Assertion；正文解释 functional mode（CH18-0006）。  
6. 一句「MiniShop 不是容量规划对象」（CH18-0008）。  
7. 启动命令的 `cd project/minishop`（CH18-0007）。

## 16. 建议重写内容

- **必须改：** `ch18-p95.html` caption + 重截 PNG。  
- **必须补：** 18.2 百分位段接到五个样本。  
- **应改：** 18.7 开篇下载令；工作实战类型句；逐步打开的工作目录。  
- **不必重写：** 18.3–18.6 主体、错误 1–10、面试骨架、授权纪律、`.jmx` 的路径/端口/1 用户 1 循环。

旧线索中已在现行正文修复、本轮不再列为开放问题：

- 示例树 `POST /api/login` + `POST /api/cart/items`（pedagogy P18-3 / rereview M5）→ 现行已是 `GET /api/products`。  
- 练习 10 答案 `GET /products`（S6-04）→ 现行已是 `GET /api/products`。

## 17. 本章结论

**C 明显需要修改**

无 P0，核心指标定义、授权纪律、诚实证据、MiniShop 路径与端口均正确，了解章定位也对。但不能给 B：本章标题级概念是百分位，唯一的 P95 图图注串台，唯一的数值例子不算 P95。再加上 JMeter 骨架缺断言/functional mode 未解释、启动命令缺目录、practice 🚧 与清单过关口径分裂，属于明显修改而非小修。

修完 CH18-0001、CH18-0002，并处理 CH18-0004–0007 后，可重新评为 B，发布线可过。不要因为「没点 GUI」把分数打回 90 以下——该项不是本轮扣分理由。

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`
- `reviews/_full-audit-2026-09-10/AUDIT_PROGRESS.md`（只读进度，未改）
- `README.md`
- `docs/COURSE_CONTROL.md`
- `docs/COURSE_OUTLINE_v1.2.md`
- `docs/LEARNING.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`
- `practice/STATUS.md`
- `exercises/README.md`
- `chapters/18-performance-testing.md`（全文）
- `chapters/quizzes/README.md`
- `chapters/quizzes/stage-6-project.md`（只评 Q2、Q3）
- `chapters/assets/diagrams/README.md`
- `chapters/assets/diagrams/ch18-p95.html` + `.png`
- `chapters/assets/diagrams/ch18-tps-concurrency.html` + `.png`
- `chapters/assets/diagrams/ch18-load-stress.html` + `.png`
- `chapters/assets/diagrams/ch18-jmeter-parts.html` + `.png`
- `project/minishop/jmeter/minishop-get-products.jmx`
- `project/minishop/docs/PRD.md`（范围与端口）
- `project/minishop/docs/openapi.json`（`/api/products`）
- `project/minishop/server.py`（`do_GET` / `_get_products` / `serve` / sqlite）
- `project/minishop/README.md`、`run.py` 头部
- `reviews/chapter-18-review.md`（线索，不继承 99 分）
- `reviews/_pedagogy-2026-09-10/ch18.md`、`RUBRIC.md`
- `reviews/_rereview-2026-09-09/stage-6-ch17-19.md`
- `reviews/v1.2.1-rescore.md`（第 18 章行）
- `reviews/full-course-audit-v1.2.md`（第 18 章摘要）

未读其他章正文。内部链接目标文件存在性已 `ls` 确认：`03`/`10`/`11`/`17` 章 md、`QUALITY_STANDARD_v1.0.md`。

### 实际跑过的命令与结果摘要

| 命令 | 结果 |
| --- | --- |
| Python 样本平均/中位/最大 | `266.0` / `120` / `800`，与教材一致 |
| `1000/50` | `20.0` |
| 百分位补充 | 最近秩 P95=800；PERCENTILE.INC ≈680 |
| `which jmeter` / `command -v jmeter` | 未安装 |
| `java -version` | 23.0.1（满足 JMeter 5.6.x Java 8+，但无 JMeter） |
| `python3 --version` | 3.14.3（与可运行性说明一致） |
| `xmllint --noout …jmx` | XML_OK |
| ElementTree 解析 jmx | domain=127.0.0.1 port=8765 path=/api/products method=GET threads=1 loops=1 functional_mode=true |
| `python3 project/minishop/run.py serve`（后台） | `MINISHOP_BASE_URL=http://127.0.0.1:8765` |
| `curl GET /api/products` | 200，3 件商品 |
| `curl GET /products` | 404 |
| `curl GET /api/login` | 404 |
| 仓库根 `python3 run.py serve` | 无此文件 |
| 仓库根 `python3 practice/run.py serve` | 没有编号 serve |
| 结束后 kill 教学服务 | 已终止 |
| `jmeter -n …` | 未跑（无命令） |
| JMeter GUI File→Open | 未跑 |

### 外部核查过的条目

| 条目 | 来源 | 结论 |
| --- | --- | --- |
| 官方入门 5×2×2=20 | jmeter.apache.org Building a Web Test Plan | 与正文一致 |
| Elapsed / Latency | User's Manual Glossary | 与正文一致 |
| Throughput 公式 | Glossary | 全部请求/墙钟；正文更强调成功吞吐 |
| GUI 不用于负载；`-n -t -l`；禁用 View Results Tree；不要 functional mode | Best Practices 16.7；Getting Started 1.0.2 | 正文 GUI 纪律正确；骨架 functional_mode 未讲 |
| Java 版本 | Changes / dist：JMeter 5.6.3 requires Java 8+（推荐 17+） | 正文只写「需要 Java」 |
| 官方入门靶是 jmeter.apache.org | Building a Web Test Plan | 正文禁止压该站，正确覆盖 |
| 不渲染 JS | Glossary Elapsed 段 | 与正文一致 |
| HTTP 4xx/5xx 默认失败 | Component Reference Response Assertion | 修正审计员记忆：不是默认成功；缺断言的问题是 200 业务失败 |
| 负载/压力/耐久/峰值 | ISTQB Glossary / CTFL-PT | 与 18.6 表一致；压力的资源削减变体未写 |
| 性能效率 | ISO/IEC 25010:2023 3.2 | 时间行为+资源+容量；正文「稳定性」需钉口径 |
| TTFB (Waiting) | MDN / Chrome 文档 Timing | 与 18.2 一致 |
| MiniShop `/api/products` 无认证、端口 8765 | OpenAPI + 本轮 curl | 与 jmx 一致 |

【External Verification Required】：JMeter GUI 打开这份精简 `.jmx` 是否弹出缺失属性告警；当前最新 JMeter 主版本若已要求 Java 17 only（本轮核验稳定线仍为 5.6.3 / Java 8+）。
