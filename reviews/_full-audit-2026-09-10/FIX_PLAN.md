# FIX_PLAN

驱动：`MASTER_AUDIT.md`。优先级 P0 → P1 → 关键 P2。P3 默认不修。  
状态：TODO / IN_PROGRESS / FIXED / VERIFIED / BLOCKED / AUDIT_DISPUTED

## P0

| Audit ID | 文件 | 章节 | 级别 | 类型 | 问题摘要 | 修复方式 | Fix Agent | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MASTER-P0-001 | chapters/01-software-testing-intro.md | 1 | P0 | TEST | 种子账号演登录失败 | 改错误密码或标明假设；钉 BUG-001 为空搜索 | Fix-01 | VERIFIED |

## P1

| Audit ID | 文件 | 章节 | 级别 | 类型 | 问题摘要 | 修复方式 | Fix Agent | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M-P1-02 | chapters/03-software-testing-classification.md | 3 | P1 | ANS | 冒烟「加入购物车」 | 改为更新数量/创建订单；3.6 同步 | Fix-03 | FIXED |
| M-P1-03 | 同上 | 3 | P1 | MiniShop | 空格「异常提示」 | 改为返回全量 / BUG-001 | Fix-03 | FIXED |
| M-P1-04 | 04a/04b + practice/04-requirement-review/template.md | 4 | P1 | EX | 作业三套规格 | 统一 template；矩阵与待确认对齐 | Fix-04 | FIXED |
| M-P1-05 | chapters/05-test-case-design.md + ch05-decision-table | 5 | P1 | PED | 判定表图文错位；状态机过星 | 正文用注册表；通用系统降星；一把过关尺子 | Fix-05 | FIXED |
| M-P1-06 | chapters/06b-test-management.md | 6 | P1 | ANS | 练习 10 答成 qty=11 | 按 BUG-001 重写确认/回归 | Fix-06 | FIXED |
| M-P1-07 | project/minishop/docs/test-plan.md + 06b | 6 | P1 | TEST | 出口混三套 P0 | 出口只写用例优先级 + S1/S2 | Fix-06 | FIXED |
| M-P1-08 | chapters/07-web-basics.md | 7 | P1 | MiniShop | example.test 写成 MiniShop 网址 | 标明教学 URL 非仓库 | Fix-07 | FIXED |
| M-P1-09 | chapters/08b-web-auth-permission.md | 8 | P1 | HTTP | 不带 Bearer≠401 | 写清 Bearer 或 Cookie | Fix-08 | FIXED |
| M-P1-10 | 08b | 8 | P1 | HTTP | GET /api/orders 无 id→404 | 表改 404 或删该行 | Fix-08 | FIXED |
| M-P1-11 | 08a/10/19 + 04-search-empty png | 8 | P1 | IMG | 空搜索截图≈目录 | 正文改指 HTTP 证据；caption 不假装已提交空关键字 | Fix-08 | FIXED |
| M-P1-12 | 08b 练习 10 | 8 | P1 | ANS | 「保持合法值」不可观察 | 预期：列表 qty=1，输入框可仍为 11 | Fix-08 | FIXED |
| M-P1-13 | 09a 图、11 curl、14 断言 | 9/11/14 | P1 | MiniShop | keyword=mouse 空列表 | 图/curl 改无 query 或 keyword=鼠标；14 与集合对齐 | Fix-09,11,14 | VERIFIED |
| M-P1-14 | chapters/10-chrome-devtools.md | 10 | P1 | UI | Preserve log/Timing/限速 | 登录是 hidden；Timing 对齐 Chrome 现名 | Fix-10 | FIXED |
| M-P1-15 | 12a/12b + ch12-tables/pk-fk | 12 | P1 | SQL/IMG | 种子图、sku 当主键、sqlite 第一帧、INSERT 无事务 | 改 HTML；12A 给 sqlite3 命令；INSERT 包事务 | Fix-12 | FIXED |
| M-P1-16 | ch13-four-shapes.html | 13 | P1 | IMG | 缺 sku | 按 13.8 表补 sku 后重截 | Fix-13 | FIXED |
| M-P1-17 | 13 + 09b | 13 | P1 | HTTP | 纸面无 Content-Length；HTTP/1.0 | 补 CL 或标明 curl 会加；响应注明 HTTP/1.0 | Fix-13 | FIXED |
| M-P1-18 | postman collection + 14 | 14 | P1 | CODE | Cookie jar 把 401 打成 201 | disableCookies + 正文 | Fix-14 | FIXED |
| M-P1-19 | 14 + env JSON | 14 | P1 | TERM | orderId vs lastOrderId | 全文 lastOrderId | Fix-14 | FIXED |
| M-P1-20 | 14 | 14 | P1 | PED | 先手建、第6步、只断言数组 | 先导入；删第6步；断言 sku | Fix-14 | FIXED |
| M-P1-21 | ch15-venv | 15 | P1 | IMG | 图让立刻 pip install -r | 图只留 venv+pip list | Fix-15 | FIXED |
| M-P1-22 | chapters/17-automation-overview.md | 17 | P1 | CODE | getByRole 非 Python | 改 get_by_role | Fix-17 | FIXED |
| M-P1-23 | ch18-p95 + 18 正文 | 18 | P1 | IMG | caption 串台；无 P95 算例 | 换 caption；用 5 样本算 P95 | Fix-18 | FIXED |
| M-P1-24 | 19/20/22 + quiz 6 | 19 | P1 | SEQ | 教学服务 qty=1 现在时 | 改过去时：现行即 /api/ + 10/11 | Fix-19,20,22 | FIXED |
| M-P1-25 | 20 + quiz 7 Q8 | 20 | P1 | PED | 可背范文；测验结构互斥 | 范文改提纲；测验改回五段 | Fix-20 | FIXED |
| M-P1-26 | 21 | 21 | P1 | JOB | 简历可抄；未禁独立开发教材 | 模板强制路径；禁自研措辞 | Fix-21 | FIXED |
| M-P1-27 | 22 | 22 | P1 | TERM | 分层命名打架 | 一张对照表 | Fix-22 | FIXED |
| M-P1-28 | 22 | 22 | P1 | EX | 自检空表可抄 37 passed | 启动命令；禁抄数字 | Fix-22 | FIXED |
| M-P1-29 | README + LEARNING + practice/README | 入口 | P1 | SEQ | 2-1 与 run.py | 表标 📖；run.py 提示书面 | Fix-cross | FIXED |
| M-P1-30 | 08a | 8 | P1 | MiniShop | 验证码进优先检查 | 删或标明仅草案 | Fix-08 | FIXED |
| M-P1-31 | 18 + 16 索引 + quiz 5 Q9 | 16/18 | P1 | CODE | run.py 无 cd | cd project/minishop | Fix-16,18 | FIXED |
| M-P1-32 | project/minishop/tests | 19 | P1 | TEST | 缺所属者 GET 200 | 加 pytest | Fix-19 | FIXED |
| M-P1-33 | 21.3 | 21 | P1 | JOB | 默认能使用 Postman/DevTools | 绑学生 GUI 产物 | Fix-21 | FIXED |
| M-P1-34 | 02 + 22 | 2/22 | P1 | JOB | 无 Git PR | 2.9 补 branch/PR 半页；22.2 列入必须掌握 | Fix-02,22 | FIXED |
| M-P1-35 | quizzes/stage-3-web.md | 8/9 | P1 | ANS | 无 token=401 | 无凭证=无 Bearer 且无 Cookie | Fix-08 | FIXED |
| M-P1-36 | 16b | 16 | P1 | CODE | session token + reset_db | 删「改成 session」或加清库禁令 | Fix-16 | FIXED |

## 关键 P2（本轮修）

| Audit ID | 摘要 | Fix Agent | 状态 |
| --- | --- | --- | --- |
| M-P2-01 | PRAGMA 按连接、不进文件 | Fix-12 | FIXED |
| M-P2-02 | Host MUST 400 | Fix-09 | FIXED |
| M-P2-03 | 非法 CL MUST | Fix-09 | FIXED |
| M-P2-04 | root cause 第四词 | Fix-06 | FIXED |
| M-P2-05 | 原则三静+动 | Fix-01 | FIXED |
| M-P2-06 | 需求可测试 ≠ 25010 Testability | Fix-04 | FIXED |
| M-P2-07 | CTFL 仍用 Usability/Portability 主名 | Fix-01 | FIXED |
| M-P2-08 | 06B 答案「加购」 | Fix-06 | FIXED |
| M-P2-09 | 405/415 非 MiniShop 必现 | Fix-09 | FIXED |
| G02-0001 | SameSite 未设置 ≠ 显式 Lax | Fix-08 | FIXED |
| G02-0002 | RFC 6750 TLS MUST | Fix-08 | FIXED |
| G02-0010 | Throughput 含失败 | Fix-18 | FIXED |
| G06-0004 | R-ORDER 下单不读购物车 | Fix-19 | FIXED |

P3 与其余 P2：**本轮不修**（成本收益）。

## 图重截清单（Coordinator）

修完 HTML 后统一 Chrome headless：`ch12-tables` `ch12-pk-fk` `ch13-four-shapes` `ch15-venv` `ch18-p95` `ch09-get-post` `ch05-decision-table`（若改 caption）、`ch19-qty-rule`（title/caption 已改过去时）、`09-pytest-report.png`（基线已是 38 passed / 1 xfailed）以及 caption 含「审查未」的图。
