# FIX RECORD
Audit ID：M-P1-31（第 18 章 serve；对应 CH18-0007 / G01-0011）
原问题：18.7「逐步打开」第 1 步写 `python3 run.py serve`，未给工作目录。仓库根没有 `run.py`；`practice/run.py serve` 会被当成「没有编号 serve」。同节纪律还写「登录是否 200」，与本章骨架 `GET /api/products` 不是同一枪。
修改文件：`chapters/18-performance-testing.md`
修改位置：18.7 逐步打开第 1 步；随后「两条纪律」第 2 条。
原内容：（摘录）
```
1. 确认只对 `127.0.0.1`，教学服务已启动：`python3 run.py serve`。
2. **先小流量看功能断言。** 登录是否 200、是否误伤教学库，比一上来 500 线程重要。
```
修复后内容：（摘录）
```
1. 确认只对 `127.0.0.1`。先进入 `project/minishop` 再启动教学服务（不要在仓库根执行）：`cd project/minishop` 然后 `python3 run.py serve`。浏览器或 curl 访问 `http://127.0.0.1:8765/api/products` 应返回 200。
2. **先小流量看功能断言。** `GET /api/products` 是否 200、是否误伤教学库，比一上来 500 线程重要。
```
为什么这样修：与第 7/10 章、根 README 同一入口。只改 18.7 这一条可复制启动命令和与骨架不一致的「登录 200」。未改 `.jmx`、未要求安装 JMeter。
依据：仓库根无 `run.py`；`project/minishop/run.py` 是教学服务入口；仓库 `.jmx` 为 `GET http://127.0.0.1:8765/api/products`。
是否影响其他章节：16 索引 / 测验 5 Q9 已由 Fix-16 写入 `FIX_M-P1-31.md`。本记录只补第 18 章。
验证结果：仓库根 `ls run.py` → 无此文件；`project/minishop/run.py` 存在。章内 `python3 run.py serve` 仅这一处，且紧挨 `cd project/minishop`。
状态：FIXED（仅第 18 章）
