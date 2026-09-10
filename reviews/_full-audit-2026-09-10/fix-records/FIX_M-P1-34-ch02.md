# FIX RECORD
Audit ID：M-P1-34（本章只修 2.9；22.2 必须掌握表归 Fix-22）
原问题：第 2 章 Git 停在本地 `status/add/commit`，`push` 只作警告；全文无 branch/PR。就业审计 G08-0004 / MASTER M-P1-34：初级岗入职第一周是 clone、建分支、开 PR，课程把 Git 停在本地五条。
修改文件：`chapters/02-software-development-process.md`
修改位置：2.9 末尾（本地五条命令之后）；学习目标最后一条、练习 9 与答案、检查清单、自测门槛 4、可运行性说明、参考资料。未改 V 模型正文。
原内容：（摘录）
```
`git commit` 不等于上传互联网。`git push` 会更新远端引用，执行前应确认远端、分支、权限和团队流程。本章不要求强制推送，也不要在不明仓库中照抄命令。
```
学习目标原为「使用最小 Git 工作流保存一次文档修改。」练习 9 只要求本地五条命令、不要推无权限远端。
修复后内容：（摘录）
```
`git commit` 不等于上传互联网。`git push` 会更新远端引用，只推到你自己拥有的仓；执行前确认远端、分支和权限。不要在不明仓库中照抄命令。

本地提交只证明你会记一版文件。入职第一周更常见的是：在自己的仓建分支、提交、开 Pull Request（PR）。下面只练这一遍，不讲 rebase，也不给课程作者提 PR。

**最短可做步骤**（fork 或自建空仓，二选一）：
1. fork 或新建空仓并 clone 自己的仓
2. git switch -c practice-ch02（旧版 git checkout -b）
3. 一次 commit，只改 exercises/
4. git push -u origin practice-ch02，在自己的仓开 PR；描述写 MiniShop 是个人实践，不是任职项目，不是独立开发
```
为什么这样修：M-P1-34 要求 2.9 补 branch/PR 半页，不是新开 Git 课。最短路径覆盖 fork/自建空仓、分支、一次提交、开 PR；PR 描述钉死 MiniShop 个人实践口径。警告 fork 后「Compare & pull request」默认指向上游，避免学生给课程原仓提 PR。本地五条命令块保留，不顺手改 CH02-0007（课程仓库 `git init` 嵌套，P2，本轮不修）。V 模型成对表未动。
依据：FIX_PLAN M-P1-34；GLOBAL_08 G08-0004；Git 官方 `git switch -c`（https://git-scm.com/docs/git-switch）；GitHub Docs「Creating a pull request」；课程冻结口径 MiniShop = 个人实践、禁止写成独立开发。本机 `git version 2.39.5`，`git switch -c` 可识别。
是否影响其他章节：本章练习 9/清单/门槛与 2.9 对齐。第 22 章 22.2 必须掌握表补 Git 行不在本记录范围，M-P1-34 整体仍待 Fix-22。第 21 章简历措辞未改。
验证结果：V 模型「系统设计 / 架构设计 → 集成测试」原文仍在；2.9 含 fork 或空仓、`git switch -c` / `checkout -b`、一次 commit、自己仓 PR、描述个人实践；未写 rebase/merge 课。LOCAL REGRESSION：学习目标、练习 9、答案 9、清单、门槛、可运行性、参考资料已同步。
状态：FIXED（仅 ch02）；M-P1-34 跨章部分 IN_PROGRESS
