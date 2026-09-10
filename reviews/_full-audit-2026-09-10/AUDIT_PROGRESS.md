# AUDIT_PROGRESS — 2026-09-10 出版级全量审计（收口）

状态：**Phase 11 完成。** 22 章 + 8 个 Global + 总控合并/分歧裁决/Final Red Team 已落盘。

对外报告：`SOFTWARE_TESTING_COURSE_FINAL_AUDIT.md`  
合并裁决：`MASTER_AUDIT.md`

## 仓库覆盖统计

| 项 | 总数 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 文件（排除 .git / pycache） | 403 | 403（清单级；逐内容单元由章/专项 Agent） | 0 |
| 章节 | 22 | 22 | 0 |
| 章节 Markdown（含上下册） | 36 | 36 | 0 |
| 章节正文行 | 14867 | 14867 | 0 |
| 图片 PNG | 103 | 103 | 0 |
| 示意图 PNG+HTML | 85+85 | 全部打开 | 0 |
| 章节代码围栏 | 252 | 252 | 0 |
| 全书 md 代码围栏 | 818 | 章节 252 深审；其余多为 reviews 历史 | — |
| 章节表格块 | 163 | 163 | 0 |
| 章内练习+答案 | 213+213 | 独立作答 | 0 |
| 阶段测验题 | 70 | 独立作答 | 0 |
| Practice 目录 | 12 | 12 | 0 |
| 可运行 practice | 10 | 10 全绿 | 0 |

## Agent 进度

| Agent | 任务 | 状态 | Coverage | P0 | P1 | P2 | P3 |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Chapter-01 | 第1章 | complete | 100% | 0* | 2 | 18 | 11 |
| Chapter-02 | 第2章 | complete | 100% | 0 | 0 | 10 | 7 |
| Chapter-03 | 第3章 | complete | 100% | 0 | 1 | 6 | 7 |
| Chapter-04 | 第4章 | complete | 100% | 0 | 3 | 12 | 7 |
| Chapter-05 | 第5章 | complete | 100% | 0 | 4 | 19 | 7 |
| Chapter-06 | 第6章 | complete | 100% | 0 | 2 | 8 | 8 |
| Chapter-07 | 第7章 | complete | 100% | 0 | 1 | 10 | 8 |
| Chapter-08 | 第8章 | complete | 100% | 0 | 5 | 10 | 8 |
| Chapter-09 | 第9章 | complete | 100% | 0 | 1 | 9 | 8 |
| Chapter-10 | 第10章 | complete | 100% | 0 | 4 | 5 | 7 |
| Chapter-11 | 第11章 | complete | 100% | 0 | 1 | 11 | 10 |
| Chapter-12 | 第12章 | complete | 100% | 0 | 4 | 13 | 8 |
| Chapter-13 | 第13章 | complete | 100% | 0 | 1 | 13 | 6 |
| Chapter-14 | 第14章 | complete | 100% | 0 | 5 | 7 | 7 |
| Chapter-15 | 第15章 | complete | 100% | 0 | 1 | 10 | 9 |
| Chapter-16 | 第16章 | complete | 100% | 0 | 0 | 9 | 12 |
| Chapter-17 | 第17章 | complete | 100% | 0 | 1 | 6 | 7 |
| Chapter-18 | 第18章 | complete | 100% | 0 | 2 | 6 | 5 |
| Chapter-19 | 第19章 | complete | 100% | 0 | 0 | 11 | 6 |
| Chapter-20 | 第20章 | complete | 100% | 0 | 4 | 12 | 6 |
| Chapter-21 | 第21章 | complete | 100% | 0 | 3 | 8 | 7 |
| Chapter-22 | 第22章 | complete | 100% | 0 | 3 | 5 | 8 |
| Global-01 | 跨章节 | complete | 100% | 1 | 10 | — | — |
| Global-02 | 技术事实 | complete（重跑） | 抽核 | 0 | 0 | 4+ | 5 |
| Global-03 | 代码与命令 | complete | 252 围栏+实跑 | 0 | 4 | — | — |
| Global-04 | 练习与答案 | complete | 283 题 | 0 | 2 | 2 | — |
| Global-05 | 图片 | complete | 85+9+102 引用 | 1† | — | — | — |
| Global-06 | MiniShop | complete | 项目闭环 | 0 | 1 | 8 | 4 |
| Global-07 | 初学者体验 | complete | 正式顺序走读 | 0 | 20 | 23 | — |
| Global-08 | 就业能力 | complete | 能力矩阵 | 0 | 7 | — | — |
| Coordinator | 合并/裁决/终审 | complete | — | 1 | 34 去重 | — | — |

\* 章 1 原报 0 P0；总控将 CH01-0002 升为全书唯一 P0。  
† Global-05 将四态图升 P0；总控维持 P1+必须 REPLACE（见 MASTER 分歧 D3）。

章 Agent 的 P0/P1/P2/P3 为各报告 ISSUE 块计数，跨章去重后不以简单相加当全书问题数。

## 终局

- 全书总分 **71/100**
- 等级 **C**
- 唯一总控 P0：第 1 章种子账号演登录失败

## Second Pass

| 项 | 结果 |
| --- | --- |
| 状态 | complete |
| 新增 P0 | 0 |
| 新增 P1 | 2（M-P1-35 测验 3 Q5 Cookie；M-P1-36 session fixture 升级） |
| 新增教材 P2 | 14（MASTER §10.3） |
| PNG 漏图 | 0 |
| SQL 数字算错 | 0 |
| 过高评分 | 第 18/17/11/16/19 章 |
| 报告 | `SECOND_PASS_AUDIT.md` |
