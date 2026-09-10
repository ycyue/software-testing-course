# FIX RECORD
Audit ID：M-P1-29
原问题：根 README 学习顺序表里 2-1/3-1/7-1 等书面实操与可运行 1-1 同形态，读者会照抄 `python3 practice/run.py 2-1`；脚本原先当未知编号打印「没有编号 2-1」，像练习不存在。
修改文件：`README.md`、`docs/LEARNING.md`、`practice/README.md`、`practice/run.py`、`practice/STATUS.md`
修改位置：根 README 内容速览实操列与表下说明；LEARNING「第一批实操」收束句；practice 清单命令块与各章表引言；`run.py` 书面编号分支与 `--list`；STATUS 书面实操段。未改 `chapters/` 正文。
原内容：（摘录）

根表实操列：`[2-1](chapters/02-…)` 与 `[1-1](practice/01-…)` 同形态。
`run.py`：未知编号 → `没有编号 2-1。先 python3 practice/run.py --list`

修复后内容：（摘录）

根表：`✅ [1-1](…)` vs `📖 [2-1](…) 章内作业，无脚本`
`python3 practice/run.py 2-1` 打印：

```
2-1 是书面实操（📖），没有可运行脚本。
python3 practice/run.py 2-1 不会启动任何程序，也不能代替你写或点 GUI。
打开：chapters/02-software-development-process.md
小节：2.8 MiniShop 工作实战
```

退出码 2（未跑脚本）。`--list` 分列 ✅ / 📖 / 🚧。

为什么这样修：同一张读者入口表必须先区分类型，脚本再把抄进命令行的 2-1 从「没有编号」改成「这是书面实操、没有脚本」。章内标题补编号属章节正文，本单禁止改，故入口与 run.py 单独闭环。
依据：G01-0008、G07-0003；FIX_PLAN M-P1-29「表标 📖；run.py 提示书面」。
是否影响其他章节：否。不改章节正文。书面编号仍指向原章锚点。可运行 1-1 `--check` 仍 3 passed。
验证结果：
- `python3 practice/run.py 2-1` / `3-1` / `7-1` / `10-1` / `14-1` / `18-1`：声明无脚本，exit 2，未启动 MiniShop。
- `python3 practice/run.py 99-9`：仍「没有编号」。
- `python3 practice/run.py 1-1 --check`：3 tests OK。
- 书面路径对应 `chapters/*.md` 均存在。
状态：FIXED
