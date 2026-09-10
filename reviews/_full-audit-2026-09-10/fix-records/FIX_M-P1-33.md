# FIX RECORD
Audit ID：M-P1-33（G08-0003，升 CH21-0005）
原问题：21.3 第一梯队默认把 Postman、DevTools 写成「能使用」，但 `practice/STATUS.md` 10-1 / 14-1 为 Incomplete（作者无 DevTools 面板截图、未点 GUI Runner）。学生可整行复制后现场打不开工具。
修改文件：`chapters/21-job-hunting.md`
修改位置：21.3 第一梯队清单与门闩；工作实战必做第 2 条与完成标准；错误 2；面试角度「你会哪些技能？」；练习 3 题干/答案；检查清单
原内容：（摘录）

```
**建议写成“能使用”（第一梯队）**
需求分析与评审、测试用例（含等价类/边界）、Web 功能测试、缺陷报告、HTTP 与 DevTools、SQL 核对、Linux 看日志、接口测试、Postman、MiniShop 实践。

示例：能使用用例、缺陷、SQL、Postman、pytest 接口；了解分层和性能指标。
```

`practice/STATUS.md`（未改，作对照）：

```
10-1 DevTools 面板    Incomplete：有页面截图和步骤，没有 DevTools 面板本身的截图
14-1 Postman Runner   Incomplete：集合可导入，作者未点 GUI Runner
```

修复后内容：（摘录）

```
第一梯队（仅当你能讲步骤）：… HTTP、SQL 核对、Linux 看日志、接口测试。
（DevTools、Postman、MiniShop 已从默认会做清单拿掉）

Postman、Chrome DevTools：**不要默认写会做。** `practice/STATUS.md` 里作者证据是 Incomplete：10-1 没有 DevTools 面板截图，14-1 未点 GUI Runner。只有你的 `exercises/chapter-14-minishop-postman.md` 里有自己的 Collection Runner 记录，或 `exercises/chapter-10-minishop-devtools.md` 里有 Network 面板截图（脱敏）时，才写会做/能使用；否则写了解，或写「用过作者集合 / 作者截图」。不要补假图来凑档口。

必做 2：Postman、DevTools 只有 exercises 里有自己的 Runner 记录或 Network 截图才写会做，否则写了解或用过作者集合
完成标准：… Postman/DevTools 的档口与 exercises 里是否有自己的 Runner/Network 记录一致。
示例：… Postman/DevTools 无自己的 Runner 或 Network 记录则写了解或用过作者集合，不写会做。
边界：`practice/STATUS.md` 的 10-1 / 14-1 Incomplete 是作者证据，不能当成你已经会做。
```

为什么这样修：作者诚实（Incomplete、禁止补假图）必须保留；学生侧另设闸。第二梯队 pytest 原来就有「若已跑通第 16、19 章」门闩，Postman/DevTools 补对等句。MiniShop 从技能栏移到项目栏，避免把项目名当工具熟练度。未改 STATUS、未补假截图、未改第 10/14 章步骤。
依据：
- 用户指令 M-P1-33：只有 exercises 里有自己的 Runner 记录或 Network 截图才能写「能使用」；否则写了解/用过作者集合；STATUS Incomplete 与正文对齐
- `practice/STATUS.md` 10-1 / 14-1 Incomplete
- 第 10 章产出路径 `exercises/chapter-10-minishop-devtools.md`；第 14 章 `exercises/chapter-14-minishop-postman.md`（必含 Runner 文字结果）
- 质量标准 §十「不得把未执行的 GUI 写成已完成」
- MASTER_AUDIT D8：就业视角 P1
是否影响其他章节：
- 第 22 章 22.2 表仍将「接口 / Postman」「HTTP / DevTools」列为必须掌握，未写 GUI 产物闸。属 G08-0003 跨章剩余，交给 Fix-22，本轮只改第 21 章简历档口。
- 未改 `practice/STATUS.md`（作者证据仍应是 Incomplete）。
验证结果：LOCAL REGRESSION——
- 21.3 第一梯队默认清单不再含 Postman / DevTools / MiniShop 实践
- 「能使用 Postman/DevTools」均带 exercises 自有产物条件，或作为反例（错误 2）
- 正文三次点名 STATUS 10-1 / 14-1 Incomplete，与仓库一致
- HTTP/SQL/Linux 仍可写会做（对应 9-1/12-1/11-1 Complete），pytest 仍保留「已跑通 16、19」门闩
- 未新增 GUI 截图，未把 Incomplete 改成 Complete
状态：FIXED
