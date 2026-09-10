# FIX RECORD
Audit ID：M-P1-31（第 16 章索引、16A/16B 可复制命令、测验 5 第 9 题；第 18 章 `run.py serve` 留给 Fix-18）
原问题：仓库根没有 `run.py`。第 16 章索引、测验 5 第 9 题标准答案，以及 16A/16B 若干可抄句子写 `python3 run.py setup/test` 且无 `cd project/minishop`。从仓库根执行会 `can't open file .../run.py`；`python3 practice/run.py test` 走「没有编号」。RT01-0004；与第 18 章同类。
修改文件：
- `chapters/16-pytest.md`
- `chapters/16a-pytest-basics.md`
- `chapters/16b-pytest-fixtures.md`
- `chapters/quizzes/stage-5-api.md`
修改位置：16 索引作业句；16A 16.5/安装段/面试示例；16B 工作实战模板、面试示例、检查清单、可运行性说明；测验 5 第 9 题答案。
原内容：（摘录）
```
跑 `python3 run.py test`（37 passed / 1 xfailed）
（由 `python3 run.py test` 收集，自己起临时端口）
仓库套件用 `python3 run.py test`
示例：先 `python3 run.py setup` 再 `python3 run.py test`。
- 命令：`python3 run.py test`
示例：`python3 run.py test` → 37 passed, 1 xfailed。
- [ ] 我能跑通 `python3 run.py test`
`python3 run.py test` 本机 2026-09-09：37 passed, 1 xfailed。
9. `project/minishop/requirements.txt`。`python3 run.py setup` 然后 `python3 run.py test`。
```
修复后内容：（摘录）
```
跑 `cd project/minishop && python3 run.py test`（37 passed / 1 xfailed）
（由 `cd project/minishop && python3 run.py test` 收集，自己起临时端口）
仓库套件用 `cd project/minishop && python3 run.py test`
示例：`cd project/minishop && python3 run.py setup && python3 run.py test`。
- 命令：`cd project/minishop && python3 run.py test`
示例：`cd project/minishop && python3 run.py test` → 37 passed, 1 xfailed。
- [ ] 我能跑通 `cd project/minishop && python3 run.py test`
`cd project/minishop && python3 run.py test` 本机 2026-09-09：37 passed, 1 xfailed。
9. `project/minishop/requirements.txt`。`cd project/minishop && python3 run.py setup && python3 run.py test`。不要在仓库根执行。
```
为什么这样修：学生入口和测验答案会被整句复制。16A 安装块、16B 工作实战块原本已有 `cd project/minishop` 再分行写 `run.py`，保留。凡单独出现的 `python3 run.py setup/test` 补同一条 cwd。第 18 章 `python3 run.py serve` 不在本 Agent 范围。
依据：仓库根无 `run.py`；`practice/run.py` 只接受练习编号；`project/minishop/README.md` 入口是该目录下的 `python3 run.py setup/test`。
是否影响其他章节：测验 5 覆盖 13–16 章，第 9 题答案与 16 索引、16B 工作实战对齐。第 18 章 `run.py serve` 见 `FIX_M-P1-31-ch18.md`（Fix-18 已补 `cd project/minishop`）。16.10 的 `python3 -m pytest` 无 cwd 是 CH16-0009（P2，本轮不修）。
验证结果：仓库根 `python3 run.py test` → `can't open file '.../run.py'`；`python3 practice/run.py test` →「没有编号 test」。16A/16B 已有 `cd` 的代码块未改。未跑 `project/minishop` 内 `run.py test`（会覆盖 evidence）。
状态：FIXED（16 索引 + 16A/16B 相关命令 + 测验 5 Q9）。第 18 章部分见 Fix-18。
