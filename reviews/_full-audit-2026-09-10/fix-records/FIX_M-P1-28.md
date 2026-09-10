# FIX RECORD
Audit ID：M-P1-28（CH22-0003）
原问题：结课自检空表，必做只写「启动 MiniShop 或说明最近一次 pytest 数字」，学生可抄 README/证据里的 37 passed 交差。
修改文件：`chapters/22-learning-path.md`；`practice/README.md` 22-1；`exercises/README.md`
修改位置：结课自检必做 2～5、模板、完成标准、课程收束门槛第 2 条、可运行性说明
原内容：（摘录）

```
3. 启动 MiniShop 或说明最近一次 pytest 数字；
| 必须掌握项 | 会 / 不会 |
完成标准：有诚实的“不会”；项目五句无公司名、无状态机；90 天目标可执行。
```

修复后内容：（摘录）

```
3. 在仓库根目录执行 `cd project/minishop && python3 run.py test`；把本机最后一行贴进自检。不要抄正文、README 或 evidence/pytest-output.txt 里的数字（包括 37 passed）。
模板预填 11 行必须掌握 +「第三梯队未写成精通」；pytest 槽位写「本机最后一行」。
完成标准：pytest 行是本机输出或真实报错；90 天坏例子=学自动化/精通性能；好例子=在团队现有接口框架里加一条登录用例。
类型：📖 书面实操。
```

为什么这样修：质量标准要求实操写清命令和可判对错的验收。仓库证据曾写 37 passed，现行套件已变成 38 passed / 1 xfailed；正文禁止抄数字，才能逼出本机输出。
依据：`standards/QUALITY_STANDARD_v1.0.md` §七、§十；CH22-0003；本机 `cd project/minishop && python3 run.py test`。
是否影响其他章节：`exercises/README.md` 补文件名示例 `chapter-22-self-check.md`（仓库仍不提交该学员产出）。未改 `evidence/pytest-output.txt`（仍为旧 37 passed，更说明不能抄）。
验证结果：
- 命令：`cd project/minishop && python3 run.py test`（实际调用 `.venv/bin/python -m pytest -q`）
- 本机 2026-09-10 最后一行：`38 passed, 1 xfailed in 0.75s`（XFAIL：`test_empty_keyword_should_not_return_all` / BUG-001）
- 收集 39 = 38 passed + 1 xfailed（含 `test_owner_can_read_own_order`）
- 正文未写入 38 passed，只禁止抄 37 passed
- 跑完后已还原 `evidence/pytest-output.txt`，避免把审查基线文件改掉
状态：FIXED
