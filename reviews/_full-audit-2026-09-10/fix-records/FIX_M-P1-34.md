# FIX RECORD
Audit ID：M-P1-34（G08-0004，仅 22.2）
原问题：22.2 必须掌握表有 Linux/SQL/Postman，无 Git 协作。初级 JD 把 clone/branch/PR 当拉仓库必备。
修改文件：`chapters/22-learning-path.md`
修改位置：22.2 必须掌握能力表；对照表「必须掌握」行；结课自检预填行；本章总结第 2 条
原内容：（摘录）

```
| Linux / SQL | … | 11～12 |
| 接口 / Postman | … | 13～14 |
```

（表中无 Git 行）

修复后内容：（摘录）

```
| Git 协作（branch / PR） | clone；开 branch；用 PR 写清测了什么。能看 log。不写精通 rebase，不要求独立建 CI | 2（2.9） |
```

对照表必须掌握行补「Git 协作（branch/PR，不是完整 Git 课）」。自检预填同步一行。总结：Git 只要 clone / branch / PR，不写精通 rebase。

为什么这样修：只加一行能力，不新开 Git 章、不把 rebase/CI 写进结课门槛。动作细节已在第 2 章 2.9（Fix-02：`FIX_M-P1-34-ch02.md`）。
依据：G08-0004；第 2 章 2.9 现行 fork/branch/PR 最短步骤。
是否影响其他章节：否。2.9 由 Fix-02 已补半页；本章只列入必须掌握，不重复命令课。
验证结果：22.2 表含 branch/PR；无 rebase 教程、无 CI 作业；指向 2.9。
状态：FIXED
