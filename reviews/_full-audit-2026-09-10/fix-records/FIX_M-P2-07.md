# FIX RECORD
Audit ID：M-P2-07
原问题：1.4 给出 ISO/IEC 25010:2023 九特性现用名（正确），但课程同时以 ISTQB CTFL 4.0.1 为参考。考纲 §2.2.2 主名仍可能是 Usability / Portability（括号补 2023 名）。教材把 2023 名写成唯一名单，面试/试卷会对不上。
修改文件：`chapters/01-software-testing-intro.md`
修改位置：1.4 九特性名单之后、Security vs Safety 段之前。
原内容：（摘录）
```
8. 灵活性（Flexibility）
9. 安全保障性（Safety）

这里的 Security 与 Safety 不是重复概念。
```
修复后内容：（摘录）
```
8. 灵活性（Flexibility）
9. 安全保障性（Safety）

ISTQB CTFL 4.0.1 承认这次更名，但考纲 §2.2.2 的主名仍可能是 Usability / Portability（括号里才是 Interaction Capability / Flexibility），并另列 Safety。面试或答题以对方试卷用语为准，不要把 ISO 2023 现用名和考纲主名混成一套必背名单。

这里的 Security 与 Safety 不是重复概念。
```
为什么这样修：九特性 2023 现用名应保留；缺口是双轨映射，不是把名单改回 2011。一句就能让考生先看对方用的是 ISO 2023 还是试卷用语。
依据：ISO/IEC 25010:2023 九特性现用名（Usability→Interaction Capability，Portability→Flexibility，新增 Safety）。ISTQB CTFL Syllabus v4.0.1 §2.2.2：Usability (also known as interaction capability)；Portability (also known as flexibility)；另列 Safety。来源：G02-0004（EVR 已由 RT02 关闭）/ MASTER M-P2-07。
是否影响其他章节：否。第 3 章 3.9 同缺口不在本 Agent 范围，未改。
验证结果：九特性英文现用名未改动；新增句明确考纲主名与面试以试卷用语为准。未把 Usability/Portability 写成 2023 顶层现用名。
状态：FIXED
