# Chapter 11 Audit

- Agent：Chapter-Audit-Agent-11
- 日期：2026-09-10
- 范围：仅第 11 章 Linux 及其列出的配套文件。未审其他章正文。
- 结论：**B 小修**
- 总体：**81/100**
- P0：0　P1：1　P2：11　P3：10

上一轮 `reviews/`（chapter-11-review 99→93、stage-4 把 qty=11 写成 500/ERROR、pedagogy 20/30）只作线索。现行正文已把 400 + INFO `inventory reject`、双路径、先搜业务关键字写进开篇；这些旧账不再当作现行缺陷。下列 ISSUE 全部由本轮独立重推命令、对照 PRD/OpenAPI/server.py、打开图片、跑 `python3 practice/run.py 11-1` 得出。

---

## 1. Coverage

| 类型 | 数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| 正文文件 `chapters/11-linux.md` | 1（748 行） | 1 | 0 |
| 一句话核心 / 重要级别 / 主案例 | 3 | 3 | 0 |
| 真实 H1 | 1 | 1 | 0 |
| 真实 H2 小节 | 27 | 27 | 0 |
| H3（错误 10 + 面试 5 + 练习 10 + 门槛 1） | 26 | 26 | 0 |
| 工作实战模板内标题（围栏内，不另计章结构） | 7 | 7 | 0 |
| 正文段落块 | 135 | 135 | 0 |
| 无序列表项 | 76 | 76 | 0 |
| 有序列表项 | 32 | 32 | 0 |
| 检查清单项 | 12 | 12 | 0 |
| 表格 | 10 | 10 | 0 |
| 代码围栏 | 23（bash 19 / text 3 / markdown 1） | 23 | 0 |
| 可独立推导的 bash 命令行 | 48 | 48 | 0 |
| 危险命令出现点（`rm -rf`×9 / `kill -9`×9 / `chmod 777`×7 / `curl\|bash`） | 全部 | 全部 | 0 |
| 正文 PNG 引用 | 3 | 3 | 0 |
| 示意图 HTML 源 | 3 | 3 | 0 |
| 图 alt | 3 | 3 | 0 |
| Markdown 链接（含图） | 13 | 13 | 0 |
| 其中外部链接 | 4 | 4（检索确认官方入口；本环境 `web_fetch` 被 SSRF 拦到 198.18.x，未拿到 HTTP 状态码） | 0 |
| 章内小练习 | 10 | 10（先作答再对答案） | 0 |
| 章内标准答案 | 10 | 10 | 0 |
| 阶段测验 `stage-4-ops.md` 第 11 章题 | Q1–Q4 + Q10 的 Linux 选项 | 已独立作答 | 0 |
| 阶段测验第 12 章题 Q5–Q9 | 5 | **不审第 12 章正文**；仅对 Q9 与 qty=11 交叉口径作答 | 0 |
| 实操 `practice/11-log-grep/` README / main.py / tests | 3 文件 | 3 | 0 |
| 实操生成证据 `validation/latest.json` | 1（本机 2026-09-10 重跑） | 1 | 0 |
| `project/minishop/evidence/linux/*` | 4 | 4 | 0 |
| `project/minishop/evidence/logs/app-sample.log` | 1（17 行） | 1 | 0 |
| MiniShop 对照（PRD / OpenAPI / server.py 购物车与日志 / frontend 文案） | 已读与本章引用相关的部分 | 已读 | 0 |
| SQL 示例 | 0 | 0 | 0 |
| 编号测试用例 / Bug 单 | 0（本章用排障记录，不以 TC/BUG 编号） | 0 | 0 |
| HTTP 示例（curl GET/POST、状态码、Set-Cookie） | 2 条可复制 curl + 选项表 | 2 + 表 | 0 |

**Coverage 100%。未检查 = 0。**

### 1.1 真实 H2 清单（27，全部已读）

1. 这一章解决什么问题
2. 学习目标
3. 前置知识
4. 场景导入：页面只有一句失败，下一步去哪？
5. 11.1 终端、Shell 与你在做什么
6. 11.2 文件系统与路径
7. 11.3 `pwd`、`ls`、`cd`
8. 11.4 `mkdir`、`touch`、`cp`、`mv`、`rm`
9. 11.5 `cat`、`less`、`head`、`tail`
10. 11.6 `grep` 与 `find`
11. 11.7 管道与重定向
12. 11.8 `ps`、`top`、`kill`
13. 11.9 `chmod`
14. 11.10 `df`、`du`、`free`、`which`、`echo`、`history`
15. 11.11 `ssh` 与 `scp`
16. 11.12 日志定位
17. 11.13 `curl` 接口测试
18. MiniShop 工作实战：Linux 排障包
19. 常见错误
20. 面试角度
21. 小练习
22. 练习答案
23. 本章检查清单
24. 本章总结
25. 本章可运行性说明
26. 参考资料
27. 下一章预告

### 1.2 表格清单（10）

| # | 约行 | 内容 | 结论 |
| ---: | ---: | --- | --- |
| 1 | 105 | Linux 常见路径 | 正确；macOS `/Users` 靠图补，正文表仍是 Linux 树 |
| 2 | 142 | pwd/ls/cd | 正确；`ls -h` 需配 `-l` 的说明成立 |
| 3 | 171 | mkdir/touch/cp/mv/rm | 正确；删除无回收站成立 |
| 4 | 207 | cat/head/tail/less | 正确 |
| 5 | 250 | grep/find 选项 | `-R` 表述过粗，见 CH11-0003 |
| 6 | 289 | 重定向 | `>` / `>>` / `2>` / `2>&1` 正确；缺管道组合示例见 CH11-0019 |
| 7 | 339 | chmod 644/755/600 | 数字含义正确 |
| 8 | 357 | df/du/free/which/echo/history | `free -h` 标明 Linux，本机验证失败符合正文 |
| 9 | 404 | 日志来源 | syslog/messages/journalctl/nginx/教学 path 合理；`/var/log/minishop/` 已标未冻结 |
| 10 | 436 | curl 选项 | 与 curl 8.7.1 / 官方 man 语义一致；`-d` 隐含 POST 已用登录命令验证 |

---

## 2. 总评分

| 项 | 分数 | 依据 |
| --- | ---: | --- |
| 技术准确性 | 8/10 | POSIX/GNU 主线正确；MiniShop 400+INFO 已对齐。扣分：`keyword=mouse` 空结果、`pgrep -a` 与 `grep -R` 的 BSD/GNU 差异未声明 |
| 岗位实用性 | 8/10 | 日志/磁盘/脱敏 curl 是测试岗真技能；`ps \| grep minishop` 对 `python3 server.py` 打空；现场日志路径教得不够 |
| 完整性 | 8/10 | 大纲命令主题齐。缺「本机可练 vs Linux」对照表、缺时间对齐图、缺 `logs/app.log` |
| 初学者友好度 | 7/10 | 开篇双路径与「今天先走这条线」有用。命令清单仍长；可复制登录 curl 用 `<redacted>` 会 401 |
| 教学顺序 | 7/10 | 阅读顺序已标 11-1 在 grep 之后。文件物理顺序仍把 11-1 放在 11.13 后；ssh 仍 ⭐⭐⭐ |
| 代码质量 | 8/10 | 本机验证的目录/管道/grep/chmod/kill TERM/curl 均成立。最小读取 curl 业务结果错 |
| 实操质量 | 8/10 | `11-1` 可跑、400 + `inventory reject` + `qty=11` 对齐 PRD。脚本用 Python `in` 代替 grep |
| 练习质量 | 8/10 | 10 题答案与独立作答一致；全是问答，没有「改一条模式再看命中」 |
| 图片质量 | 7/10 | grep-find / pipe 口径已是 400 与 qty=11。path 的 caption 跑题；三张 PNG 底部大片留白；无时间对齐图 |
| **总体** | **81/100** | 无 P0；1 条 P1 可一行修好；其余是声明差异、顺序和练习形态。不是重写级 |

质量标准 20 项 DoD（独立，不是照抄旧审查）：约 **17/20**。未过项：无知识性错误（mouse curl、pgrep/grep 选项）、示例可运行性、图表完全服务难点、星级与「可后读」一致。作者发布线 90 分 / 20/20 是作者目标，不是本审计下限。

---

## 3. P0

无。危险命令均出现在「禁止 / 反例 / 先确认」语境，不是作为可复制的排障步骤。未把 GET/POST 写成「POST 更加密」。未把 macOS `free` 当 Linux 证据。未虚构远程 Linux 主机。qty=11 现行口径是 HTTP **400** + 日志 **INFO** `inventory reject`，与 `server.py`、PRD `R-CART-10`、`evidence/http/05-cart-qty-11.txt`、实操 11-1 一致。

---

## 4. P1

## ISSUE
ID：CH11-0001
文件：`chapters/11-linux.md`
章节：第 11 章
小节：11.13 `curl` 接口测试
精确位置：约 L430–L433，「最小读取」可复制命令
原文：

```bash
curl -sS -D - -o ./minishop-curl-body.txt "http://127.0.0.1:8765/api/products?keyword=mouse"
```

问题等级：P1
问题类别：CODE / ACC / MiniShop
问题说明：把这条当作 MiniShop v1.0 的最小读取示例。本轮对 `http://127.0.0.1:8765` 实打：HTTP **200**，Body 为 `{"items": []}`。
为什么有问题：`server.py` 搜索是 `keyword.lower() in name.lower() or in sku.lower()`。种子商品名是「无线鼠标」，SKU 是 `SKU-DEMO-001`，都不含英文字母 `mouse`。学生按「最小读取」抄命令会得到空列表，容易误报「搜索坏了」或「服务没数据」。同节又写「`200` 仍要看 Body 是否业务失败」，这条示例正好踩进去却不提示空列表是预期。Postman 集合用的是 `keyword=鼠标`（客户端会做 URL 编码）；本机直接把中文放进 curl 请求行会被 MiniShop 的 BaseHTTP 打成 **400 Bad request syntax**。ASCII 安全且能命中的写法是无 keyword 或 `keyword=SKU-DEMO-001`。
依据：本机 curl 2026-09-10；`project/minishop/server.py` `_get_products` 与 `seed()`；PRD 教学数据「无线鼠标」；OpenAPI `GET /api/products`。
建议修改：最小读取改为无查询或按 SKU 过滤；若要演示中文搜索，给出已编码的 query。
推荐替换文本：

```bash
curl -sS -D - -o ./minishop-curl-body.txt "http://127.0.0.1:8765/api/products"
# 预期：HTTP 200，items 含 SKU-DEMO-001 无线鼠标 stock=10 等 3 件
# 若要过滤：?keyword=SKU-DEMO-001
# 不要用 keyword=mouse：英文 mouse 不在中文商品名里，会得到 {"items": []}
```

---

## 5. P2

## ISSUE
ID：CH11-0002
文件：`chapters/11-linux.md`
章节：第 11 章
小节：11.7 管道与重定向
精确位置：约 L297，「可用 `pgrep -a minishop`（若系统有）」
原文：过滤进程时，`ps aux | grep minishop` 可能匹配到 grep 自己。……可用 `pgrep -a minishop`（若系统有）或看完整命令行再判断。
问题等级：P2
问题类别：ACC / TERM / macOS vs Linux
问题说明：把 `pgrep -a` 写成「若系统有」的便携替代，未声明 **同一字母在 GNU 与 BSD 上不是同一选项**。
为什么有问题：Linux procps-ng：`-a, --list-full` = 列出完整命令行。macOS/BSD `man pgrep`：`-a` = Include process ancestors。本机 `man pgrep` 已核对。macOS 上看完整命令行应是 `pgrep -lf minishop`（或 `ps`），不是 `-a`。正文强调「不要假设本机 macOS 的输出可以原样写进缺陷」，这里漏了。
依据：Linux man7 pgrep(1)；本机 macOS `man pgrep`（2026-09-10）。
建议修改：写成「Linux：`pgrep -a` 列出命令行；macOS：`-a` 是祖先进程，看命令行用 `pgrep -lf`」。不要让读者在 macOS 上把 `-a` 当 list-full。
推荐替换文本：不要依赖 `pgrep -a` 当便携写法。Linux（procps）`-a` 才是完整命令行；macOS `-a` 是包含祖先进程。统一建议：`ps aux | grep -v grep | grep minishop`，再人工看 COMMAND 列。

## ISSUE
ID：CH11-0003
文件：`chapters/11-linux.md`
章节：第 11 章
小节：11.6 grep 选项表
精确位置：约 L254，「`grep -R` 递归目录（GNU grep 常用；有的系统用 `grep -r`）」
原文：`grep -R` 递归目录（GNU grep 常用；有的系统用 `grep -r`）
问题等级：P2
问题类别：ACC / macOS vs Linux
问题说明：写成「GNU 用 -R、别的系统用 -r」的拼写差异，实际差异是符号链接策略。
为什么有问题：GNU grep：`-r` 递归且默认不跟随目录符号链接，`-R` 跟随。macOS/BSD grep：`-R` 与 `-r` 是别名，跟随链接要另加 `-S`。本机 `man grep`：`-R, -r, --recursive` 同一段，`-S` 才是 follow symlinks。多数读者在 macOS 上练习，会把正文理解成「只要换成 -r 就和 Linux 一样」。
依据：GNU grep 手册 `-r` / `-R`；本机 BSD grep 2.6.0 man。
建议修改：表内改成「两边都能递归；GNU 的 -R/-r 对符号链接不同；macOS 上 -R 等于 -r，跟链接用 -S」。排障从已知日志目录开始——这句保留。
推荐替换文本：`grep -R` / `grep -r` 都能递归，但 GNU 与 BSD 对符号链接的默认不同。缺陷里粘贴你实际敲的那一条，不要抄「标准答案里的 -R」。

## ISSUE
ID：CH11-0004
文件：`chapters/11-linux.md`
章节：第 11 章
小节：11.7 / 11.8
精确位置：约 L277、L307 `ps aux | grep minishop`；`ps aux | grep -v grep | grep minishop`
原文：`ps aux | grep minishop`
问题等级：P2
问题类别：JOB / MiniShop / CODE
问题说明：用 `minishop` 当进程关键字。本轮在 `cd project/minishop && python3 server.py` 时，`ps aux | grep minishop` **零命中**；实际 COMMAND 是 `.../Python.app/.../Python server.py`。
为什么有问题：README 也允许 `python3 server.py`。`run.py serve` 因为 `execv` 传入 **绝对路径** `.../project/minishop/server.py`，命令行里才有 `minishop`。学生若按「不装依赖也能 python3 server.py」启动，会判断「进程没起来」。正文没有给出 MiniShop 真实进程名。
依据：本机 `ps aux` 2026-09-10；`project/minishop/run.py` `os.execv(sys.executable, [sys.executable, str(server)])`。
建议修改：示例改成 `grep -E 'server.py|minishop'`，并写明「看完整命令行，不要只数 grep 命中」。
推荐替换文本：

```bash
ps aux | grep -v grep | grep -E 'server.py|minishop'
# MiniShop 常见是 python3 server.py，命令行里不一定有单词 minishop
```

## ISSUE
ID：CH11-0005
文件：`chapters/11-linux.md`
章节：第 11 章
小节：11.11 标题星级；学习目标；工作实战第 5 条
精确位置：L374「11.11 `ssh` 与 `scp` ⭐⭐⭐」；学习目标「说明 ssh 与 scp 的用途和授权边界」；工作实战允许写「仅本机练习」
原文：11.11 标 ⭐⭐⭐；章首又写「没有授权测试机就跳，工作实战写仅本机练习」。
问题等级：P2
问题类别：PED / SEQ
问题说明：必须掌握与可跳过互相打架。
为什么有问题：质量标准用 ⭐⭐⭐/⭐⭐/⭐ 当过滤器。读者会以为没跳板机就没学完第 11 章。`chmod` 已降为 ⭐⭐，ssh 没有。
依据：质量标准第七节知识层级；章首「可后读」与 11.11 标题。
建议修改：11.11 改为 ⭐⭐，学习目标改成「能说明用途和授权边界；没有测试机可写仅本机练习」。
推荐替换文本：`## 11.11 ssh 与 scp ⭐⭐`（了解用途与授权边界即可；无远程机跳过动手）。

## ISSUE
ID：CH11-0006
文件：`chapters/11-linux.md`
章节：第 11 章
小节：学习目标
精确位置：L27–L40，12 条子弹
原文：学习目标同时列出 mkdir 全家桶、chmod、ssh/scp、kill -9 不是第一步、curl、排障记录。
问题等级：P2
问题类别：PED
问题说明：一句话核心是「日志、进程和磁盘是页面上看不到的观察通道」，学习目标却是命令清单。
为什么有问题：章首已经加了「今天先走这条线 / 可后读」，但学习目标没有收成过滤器。读者会按 12 条打勾，把反例 `kill -9` 当成主技能。
依据：质量标准「一句话核心当过滤器」；本章 L3 一句话核心。
建议修改：学习目标收成 5 条：pwd/ls → tail/grep 对齐时间 → grep vs find → ps 与 df（free 仅 Linux）→ 脱敏 curl + 排障记录。其余留在对应小节。
推荐替换文本：完成本章后你应该能够：先 `pwd`/`ls` 再动手；用 `tail`/`less`/`grep` 按时间和关键字找到与本次失败对应的一行；说明 grep 搜内容、find 搜文件名；用 `ps` 确认进程、用 `df -h` 看磁盘（`free -h` 仅 Linux）；把 Copy as cURL 脱敏后在授权地址再打一次，完成排障记录。

## ISSUE
ID：CH11-0007
文件：`chapters/11-linux.md`；`practice/11-log-grep/README.md`；`practice/11-log-grep/main.py`
章节：第 11 章
小节：阅读路径 vs 11.13 之后的实操入口；实操 11-1
精确位置：正文 L15–L16 说 11.5–11.7 后立刻做 11-1；可复制入口在 L473（11.13 之后）。`main.py` 用 Python 字符串包含判断，stdout 仍打印「日志观察：grep inventory reject」。
原文：配套可运行实操放在 curl 节之后；README「自己在本机对照时」才真正敲 grep。
问题等级：P2
问题类别：SEQ / EX / PED
问题说明：阅读指南和文件顺序不一致；验收可以被脚本代跑，读者可以一次不敲 `grep`。
为什么有问题：本章要练的是「页面上看不到的那一行你能指出来」。11-1 的判定是对的（400 + inventory reject + qty=11，本轮 `python3 practice/run.py 11-1` 与 `--check` 均通过），但观察通道被 Python 包办。stdout 写 grep，实际没有调用 grep 二进制，会给「我已经会 grep」的错觉。
依据：本轮运行记录；`practice/11-log-grep/main.py` L40–L50；README L19–L23 把本机 grep 标成对照而非必做。
建议修改：把 11-1 入口挪到 11.6/11.7 后；README 把本机 `grep` 列为必做；脚本可保留自动验收，但须打印读者应亲手敲的那条命令。
推荐替换文本：README 验收增加一条：「你在本机对 `evidence/logs/app-sample.log` 亲手执行过 `grep -n "inventory reject"`，不是只看脚本输出。」

## ISSUE
ID：CH11-0008
文件：`chapters/11-linux.md`
章节：第 11 章
小节：开篇 / 前置知识 / 11.1 / 11.3 / 11.10 / 错误 5 / 练习 9
精确位置：macOS vs Linux 散落在 L21、L95、L154、L366、错误 5、练习 9
原文：多处提醒 `ls --help`、`ls` 的 `@`/`+`、`free -h`，但没有一张总表。
问题等级：P2
问题类别：PED / PRE
问题说明：差异声明了，检索成本高。零基础读者做完本机练习仍不确定哪几条能贴进「服务器缺陷」。
为什么有问题：质量标准要求重要信息回答「什么时候用 / 常见错误」。本章目标环境是 Linux 服务器、练习机经常是 macOS，这是章级约束，不应靠读者自己拼。
依据：本机已验证 `ls --help` 失败、`free -h` command not found、`ls -l` 出现 `@`，与散落表述一致，缺汇总。
建议修改：前置知识后增加对照表。
推荐替换文本：

| 你现在的机器 | 本章可以练 | 不要当成 Linux 测试机证据 |
| --- | --- | --- |
| macOS / Windows 终端 | pwd ls cd tail grep find 管道 df -h 脱敏 curl；实操 11-1 | free -h、journalctl、把本机 ls/df 原文贴进「服务器缺陷」 |
| 授权 Linux 测试机 | 上面全部，外加 free -h、系统日志、ps 看应用进程 | 未授权主机、192.0.2.10（文档示例地址） |

## ISSUE
ID：CH11-0009
文件：`chapters/11-linux.md`；`chapters/assets/diagrams/`（无 `ch11-time-align`）
章节：第 11 章
小节：11.12 日志定位；错误 8
精确位置：11.12 步骤 5「把时间戳对齐 Network」；错误 8「核对时区。服务器可能是 UTC」
原文：步骤正确，无图；也没有用仓库里现成的时区差当例子。
问题等级：P2
问题类别：IMG / PED / JOB
问题说明：测试工程师最值钱的「时间对齐」比 11.1–11.4 短，且无图。
为什么有问题：`evidence/linux/curl-login-headers.txt` 的 `Date: Wed, 09 Sep 2026 06:30:08 GMT` 对应 `app-sample.log` 里 `2026-09-09 14:30:08` 的登录（本地 UTC+8）。这是现成教材，正文没有点破。读者会对着 Network 的 GMT 和日志的本地时间说「对不上，所以无关」——错误 8 写了原则，缺 MiniShop 实例。
依据：上述两个 evidence 文件；目录中无 `ch11-time-align.html/.png`。
建议修改：11.12 插入时间对齐示意图，并用 GMT Date vs 本地 asctime 做一行对照。
推荐替换文本：对齐示例：curl 响应头 `Date: ... 06:30:08 GMT` 与日志 `2026-09-09 14:30:08` 是同一秒（UTC+8）。对不上先问时区，再问是不是另一次请求。

## ISSUE
ID：CH11-0010
文件：`chapters/11-linux.md`
章节：第 11 章
小节：11.13 登录 POST 代码块
精确位置：约 L452–L456
原文：旁白写「本机复现用教学账号 `Test1234`」；可复制 JSON 却是 `"password":"<redacted>"`。
问题等级：P2
问题类别：PED / CODE / EX
问题说明：脱敏纪律是对的；可复制块对着 v1.0 会 **401** `{"result":"fail"}`，日志出现 `login fail phone=13800138000`。
为什么有问题：本轮实打：`<redacted>` → 401；`Test1234` → 200 + `Set-Cookie` + token。零基础读者先复制代码块，再读旁白，会以为登录坏了。这不是「命令语法错」，是教学顺序把占位符放进了唯一可复制 POST。
依据：本机 curl 2026-09-10；`server.py` `_login`。
建议修改：给出两条：一条本机可跑（密码写教学账号并声明仅本机）；一条可分享（`<redacted>`）。不要只给后者。
推荐替换文本：

```bash
# 本机教学账号，不要把这行贴到群里
curl -sS -D - -H "Content-Type: application/json" \
  -d '{"phone":"13800138000","password":"Test1234"}' \
  "http://127.0.0.1:8765/api/login"
# 分享/缺陷附件把密码换成 <redacted>，并确认已从 history 删掉
```

## ISSUE
ID：CH11-0011
文件：`chapters/11-linux.md`；`practice/11-log-grep/README.md`
章节：第 11 章
小节：工作实战；11.12
精确位置：工作实战命令只 grep `evidence/logs/app-sample.log`；11.12 应用日志例子是未冻结的 `/var/log/minishop/`
原文：仓库已有本机真实输出……`grep -E "login ok|inventory reject" evidence/logs/app-sample.log`
问题等级：P2
问题类别：JOB / MiniShop
问题说明：现场复现 qty=11 之后，真正追加的是 `project/minishop/logs/app.log`。本章几乎不提这条路径。
为什么有问题：本轮对运行中的 MiniShop POST qty=11 后，`logs/app.log` 立即出现 `INFO  inventory reject ... qty=11`。工作实战只翻预置样本，读者可以不启动服务、不复现，只抄 evidence。图 `ch11-grep-find` 用的是 `logs/app.log`，与工作实战不是同一文件。
依据：本机 `logs/app.log` 追加行 2026-09-10 11:55:24；`server.py` `DEFAULT_LOG = ROOT / "logs" / "app.log"`。
建议修改：工作实战分两步：①对照样本；②启动 MiniShop、复现 qty=11、再 `grep` `logs/app.log`。没有启动则写「仅对照样本」。
推荐替换文本：现场日志：`project/minishop/logs/app.log`（`python3 run.py serve` 后追加）。`evidence/logs/app-sample.log` 是作者摘录，用来对照，不是你刚才那一次请求。

## ISSUE
ID：CH11-0012
文件：`chapters/11-linux.md` 小练习；`practice/11-log-grep/README.md`
章节：第 11 章
小节：小练习 1–10
精确位置：L632–L677
原文：10 道全是问答 / 单选。
问题等级：P2
问题类别：EX / PED
问题说明：没有「改一个输入再看命中如何变」。
为什么有问题：质量标准要求练习覆盖「怎么使用」。本章最容易练的变量就是 grep 模式：`ERROR` → 0 行，`inventory reject` → 5 行。练习 5 只在答案里提醒样本是 INFO，题干仍用一般 `grep ERROR` 管道。读者可以全对 10 题却从未改过一条模式。
依据：练习 1–10 题干；`app-sample.log` 上 `grep ERROR` 0 命中、`grep inventory reject` 5 命中（本轮实测）。
建议修改：练习 5 或另加一题：对 `app-sample.log` 先 `grep ERROR` 再改成 `inventory reject`，写下命中行数。
推荐替换文本：对 `evidence/logs/app-sample.log` 执行 `grep -c ERROR` 与 `grep -c "inventory reject"`。解释为什么前者是 0 不能写成「接口没拒」。

---

## 6. P3

## ISSUE
ID：CH11-0013
文件：`chapters/11-linux.md`；`project/minishop/evidence/logs/app-sample.log`
章节：第 11 章
小节：11.5 教学日志示例
精确位置：L217–L220
原文：

```text
2026-09-09 10:17:00 INFO login ok user=13800138000
2026-09-09 10:17:05 INFO inventory reject sku=SKU-DEMO-001 stock=10 qty=11
```

问题等级：P3
问题类别：ACC / MiniShop
问题说明：紧挨着「仓库 `evidence/logs/app-sample.log` 里……」，给出的时间戳和空格与文件不一致。
为什么有问题：实际行是 `2026-09-09 10:17:07,643 INFO  inventory reject ...`（有毫秒、`INFO` 后双空格，且 10:17:07 还有一条 `login fail`）。formatter 是 `"%(asctime)s INFO  %(message)s"`，级别是写死的 INFO。教学简化可以，但应标明「格式已简化，不要按 10:17:00 去对样本」。
依据：`app-sample.log` L3–L5；`configure_logging()`。
建议修改：直接贴样本里的两行，或加「示例已简化」。
推荐替换文本：直接引用 `2026-09-09 10:17:07,643 INFO  inventory reject sku=SKU-DEMO-001 stock=10 qty=11`。

## ISSUE
ID：CH11-0014
文件：`chapters/11-linux.md`
章节：第 11 章
小节：工作实战「审查摘录」
精确位置：约 L503–L508
原文：命令是 `grep -E "login ok|inventory reject"`；摘录只给两行且无时间戳。
问题等级：P3
问题类别：PED
问题说明：本轮同一条命令命中 **13** 行，与 `evidence/linux/grep-app-log.txt` 一致。标了「摘录」但仍像标准输出。
为什么有问题：学生会对着 13 行怀疑自己多出来了。
依据：本机 grep；`grep-app-log.txt` 13 行。
建议修改：写「命中 13 行，下面是其中 2 行」或改为 `grep "inventory reject" | tail -n 2`。
推荐替换文本：完整输出见 `evidence/linux/grep-app-log.txt`（13 行）。下面只展示形态。

## ISSUE
ID：CH11-0015
文件：`chapters/assets/diagrams/ch11-path.html` 与 `.png`
章节：第 11 章
小节：11.3 配图
精确位置：HTML `<p class="caption">`
原文：示意图：课程证据在 project/minishop/evidence/linux/。危险命令不得在未授权环境复述执行。
问题等级：P3
问题类别：IMG
问题说明：图在讲 pwd/ls/相对路径，caption 在讲证据目录和危险命令。
为什么有问题：alt「终端里的当前目录就是你的位置」是对的；caption 张冠李戴。lead 已经写了 rm 前确认路径，caption 应回收到相对路径。
依据：打开 HTML 与 PNG。
建议修改：caption 改为「相对路径从 pwd 的当前位置算。先 pwd/ls 再 rm。」
推荐替换文本：示意图：相对路径从 `pwd` 的当前位置算。先 `pwd`/`ls` 再 `rm`。

## ISSUE
ID：CH11-0016
文件：`chapters/assets/diagrams/ch11-path.png`、`ch11-grep-find.png`、`ch11-pipe.png`
章节：第 11 章
小节：三张配图
精确位置：整张 PNG
原文：按 `diagrams/README.md` 用 Chrome `--window-size=1320,780` 截图。
问题等级：P3
问题类别：IMG
问题说明：内容只占上半，下半大片空白。
为什么有问题：可读、未错，但印刷/滚动时像「一页没画完」。grep-find 与 pipe 的 HTML 已在 2026-09-10 11:09 更新且与 PNG 同日，内容口径不是旧 500。
依据：实际打开三张 PNG。
建议修改：缩短截图高度或给 `.page` 最小高度，避免半页空白。
推荐替换文本：（排版，不改命题。）

## ISSUE
ID：CH11-0017
文件：`practice/11-log-grep/main.py`
章节：实操 11-1
小节：结论文案
精确位置：L52–L55
原文：只看页面「操作失败」你不知道服务端是否按库存规则拒绝。
问题等级：P3
问题类别：TERM / MiniShop
问题说明：前端失败文案是 `body.error`，即 `qty exceeds stock`。章场景导入也写 `qty exceeds stock`。脚本写成「操作失败」。
为什么有问题：不是功能错（HTTP 400 与日志是对的），但是观察对象的用词和页面、正文不一致。
依据：`frontend/app.js` L93；本章 L50；本轮 11-1 输出。
建议修改：改成「只看页面 qty exceeds stock」。
推荐替换文本：只看页面 `qty exceeds stock` 你不知道服务端是否按库存规则拒绝。

## ISSUE
ID：CH11-0018
文件：`chapters/11-linux.md`；`project/minishop/evidence/linux/curl-login-headers.txt`
章节：第 11 章
小节：11.13 / 工作实战
精确位置：evidence 第一行 `HTTP/1.0 200 OK`；正文未提 MiniShop 是 HTTP/1.0
原文：对照第 9 章阅读状态行。
问题等级：P3
问题类别：HTTP / MiniShop
问题说明：学生刚学 HTTP/1.1，对着 evidence 会问为什么是 1.0。
为什么有问题：这是 BaseHTTP 的真实指纹，诚实证据。缺一句「教学服务是 HTTP/1.0，状态码和头仍然按第 9 章读」。
依据：`curl-login-headers.txt`；本机 curl 响应。
建议修改：工作实战 curl 节加一句 HTTP/1.0 来自 BaseHTTP，不是协议教错。
推荐替换文本：MiniShop 本机服务基于 Python BaseHTTP，状态行是 HTTP/1.0。读状态码、`Content-Type`、`Set-Cookie` 的方法不变。

## ISSUE
ID：CH11-0019
文件：`chapters/11-linux.md`
章节：第 11 章
小节：11.7 重定向表
精确位置：L293 `2>&1`
原文：把错误并进标准输出，常与管道一起用。
问题等级：P3
问题类别：PED
问题说明：表有 `2>&1`，代码块只有 `2>` 写文件，没有 `cmd 2>&1 | grep ...`。
为什么有问题：这是排障高频写法，只在表里出现，零基础不容易拼出来。
依据：11.7 代码块 vs 表。
建议修改：补一行 `ls /no/such/path 2>&1 | tail`。
推荐替换文本：`ls /no/such/path 2>&1 | tail -n 5`

## ISSUE
ID：CH11-0020
文件：`chapters/11-linux.md`；`project/minishop/evidence/linux/df.txt`
章节：第 11 章
小节：11.10 / 工作实战
精确位置：`df.txt` 列名 `Capacity`；GNU df 常见 `Use%`
原文：不要假设本机 macOS 的输出可以原样写进缺陷。
问题等级：P3
问题类别：macOS vs Linux
问题说明：差异原则对，但 `df` 是工作实战必做项，列名差最容易被抄错。
为什么有问题：evidence 已是 APFS `/dev/disk3s5`，诚实。正文可在 11.10 加半句「macOS 列名是 Capacity，Linux 常见 Use%」。
依据：本机 `df -h .`；`df.txt`。
建议修改：11.10 表下加一行列名差异。
推荐替换文本：macOS `df -h` 的使用率列常叫 Capacity；Linux GNU df 常叫 Use%。贴输出时连表头一起贴。

## ISSUE
ID：CH11-0021
文件：`chapters/11-linux.md`
章节：第 11 章
小节：11.8
精确位置：L318–L323 代码块 `kill 12345` / `kill -9 12345`
原文：代码块可复制；周围有「不要对未知 PID 下手」。
问题等级：P3
问题类别：PED
问题说明：警告足够，但示例 PID 在可复制围栏里。若练习机上碰巧有 PID 12345，会误杀。
为什么有问题：`rm -rf /` 放在「禁止」列表而不是「试一试」围栏，处理得更好。kill 可以改成 `<PID>` 占位。
依据：11.8 代码围栏 vs 11.4 禁止列表。
建议修改：围栏内用 `kill <PID>`，并写「把 <PID> 换成你刚用 ps 看到的练习进程」。
推荐替换文本：`kill <PID>`  # 先 ps 确认是你自己的练习进程

## ISSUE
ID：CH11-0022
文件：`chapters/11-linux.md`
章节：第 11 章
小节：11.8 `top`；11.3 `ls -l` 表述
精确位置：L313「按 q 退出」；L335「`ls -l` 最左边一列就是权限」
原文：见上。
问题等级：P3
问题类别：ACC / TERM
问题说明：① GNU top 与 BSD/macOS top 交互键不同，除了 `q` 退出以外几乎不能互相照抄。② `ls -l` 最左 **第一位是文件类型**（`-`/`d`/`l`），后九位才是权限。
为什么有问题：不会教错 kill/chmod 主线，但「最左边一列就是权限」不精确。macOS 上 `top` 的画面也和教材 Linux 截图式描述不同。
依据：POSIX `ls` 长格式；本机 `ls -l`；BSD top vs procps top。
建议修改：改成「最左 10 个字符：第 1 位类型，后 9 位权限」；top 标明 Linux/macOS 界面不同，只要求会退出。
推荐替换文本：`ls -l` 最左像 `-rw-r--r--`：第一位是类型，后面九位才是 rwx。macOS 行尾 `@`/`+` 不是权限坏了。

---

## 7. 逐段问题

对每个真实小节给出独立判断。无 ISSUE 的不编造问题。

| 小节 | 技术 | 初学者 | 与 MiniShop | 问题 |
| --- | --- | --- | --- | --- |
| 一句话核心 | 正确 | 能当过滤器 | 日志/进程/磁盘确实是页面外通道 | 无 |
| 这一章解决什么问题 | 现行 400+INFO 正确；「不要默认 grep ERROR」正确 | 「今天先走这条线」有用 | 与 PRD R-CART-10 一致 | 学习目标未同步收束，CH11-0006 |
| 学习目标 | 12 条都对，但不是过滤器 | 像命令大纲 | ssh/chmod 与主线并列 | CH11-0005/0006 |
| 前置知识 | 接第 9/10 章正确；终端三种来源合理 | WSL 有提、Git Bash 无 | Copy as cURL 脱敏衔接正确 | CH11-0008 |
| 场景导入 | 页面文案 `qty exceeds stock` 与 frontend 一致；Network 400 正确 | 双路径（本机 vs SSH）已取代「必须 SSH」 | 400 不是 500 | 无 P1；本机路径仍 grep 样本，CH11-0011 |
| 11.1 终端/Shell | 程序+选项+参数模型正确；`ls --help` 在 macOS 失败，正文已声明；`which`/`PATH` 正确 | `man` 用 `q` 退出正确 | 无 | 无新 ISSUE |
| 11.2 文件系统 | 树、绝对/相对、`.`/`..`、隐藏文件正确；`/tmp`「可能被清」有「可能」 | `/` 不是练习 rm 的地方，警告够 | `/var/log` 关心日志，正确 | 表是 Linux 路径，macOS `/Users` 靠图，CH11-0008 |
| 11.3 pwd/ls/cd | 命令表正确；`cd -`、`ls -lah` 本机验证；`@`/`+` 已声明 | 先 pwd 再动手，对 | 配图用 `/Users/you/...`，适合 macOS 读者 | 图 caption CH11-0015；`ls -l` 类型位 CH11-0022 |
| 11.4 文件管理 | mkdir -p/touch/cp/mv/rm 本机验证；无回收站正确 | 删除纪律先 ls 再 rm，够 | 练习目录 `~/minishop-linux-lab` 不碰仓库 | `rm -rf /` 在禁止列表，警告足够 |
| 11.5 读日志 | head/tail/less/cat/tail -f 正确；样本是 INFO 已声明 | 不要 cat 大文件，对 | 关键字与 server 日志一致 | 教学时间戳简化 CH11-0013 |
| 11.6 grep/find | 内容 vs 文件名正确；MiniShop 命令已放第一条；`grep ERROR` 对样本 0 行，正文已说 | 从已知目录搜，对 | 与 11-1、evidence 一致 | `-R` 表述 CH11-0003 |
| 11.7 管道/重定向 | `\|` `>` `>>` `2>` 本机验证；`>` 覆盖风险正确 | grep 自己的干扰写了 | `grep inventory` 能打到样本 | pgrep -a CH11-0002；ps minishop CH11-0004；2>&1 示例 CH11-0019 |
| 11.8 ps/top/kill | 默认 TERM=15、-9=KILL 不能捕获，正确；先 ps 再 kill 再 ps，正确 | -9 当反例，对 | 进程名示例弱 | CH11-0004/0021/0022 |
| 11.9 chmod | 644/755/600 正确；777 不是默认修复，正确 | ⭐⭐ 诚实 | 无授权不改系统目录，对 | 无 |
| 11.10 诊断命令 | df/du/which/echo 本机通过；free 在 macOS 失败且正文要求跳过 | 磁盘满 → 可能 500，有「可能」 | df evidence 是 APFS，已声明本机 | CH11-0008/0020 |
| 11.11 ssh/scp | 192.0.2.10 符合 RFC 5737 TEST-NET-1；指纹、600、脱敏、exit/Ctrl+D 正确；不教破解 | 无远程机可跳，正文有 | `/var/log/minishop/` 未冻结 | 星级 CH11-0005。未对 192.0.2.10 发起连接 |
| 11.12 日志定位 | 步骤（问路径 → ls -lh → tail → grep → 对齐时间 → 脱敏）是岗位流程 | journalctl 不可用时找文件，正确 | 教学 path 未冻结 | 缺图与 MiniShop 时区实例 CH11-0009/0011 |
| 11.13 curl | 选项表正确；`-d` 隐含 POST（官方 man + 本机登录验证）；不打 `/products`、不打 `/login` 正确（本机均为 404）；`-k`、`curl\|bash`、HTTPS 仍必要、POST 不是加密，全部避开禁止绝对化 | Copy as cURL 脱敏衔接第 10 章 | 路径/端口是 v1.0 8765 `/api/`，与 PRD/OpenAPI 一致 | **CH11-0001 keyword=mouse**；CH11-0010 `<redacted>` |
| 工作实战 | 产出路径 `exercises/chapter-11-minishop-linux.md` 清楚；允许仅本机；evidence 四件套真实存在 | 模板可填 | pwd-ls 与本机 ls 文件名一致；grep 摘录来自真实样本；df 是 APFS；curl 头已打码 | CH11-0011/0014/0018 |
| 常见错误 1–10 | 十条都是真错误；错误 5/8/9/10 尤其有岗位价值 | 先禁止后解释，略冲，但每条都有「修正」 | 错误 8 时区与 MiniShop 证据能对上却没用实例 | CH11-0009 |
| 面试 5 题 | 结论→原理→场景→示例→边界；curl 题明确不要打 `/login` | 不是背命令 | 登录 URL 正确 | 无 |
| 小练习 / 答案 | 见 §11 | — | 练习 5/10 已写 INFO 不是 ERROR | CH11-0012 |
| 检查清单 / 门槛 | 门槛第 4 条已改为口述 400+INFO 与时间对齐 | 可验证 | 与 11-1 一致 | 11-1 仍不强制亲手 grep |
| 总结 / 可运行性说明 | 七件事与核心一致；诚实写明 ssh/top/kill/journalctl 未对远程执行；macOS 上 free 非必过 | 好 | 教学 IP/path 未冻结 | 声明与 11.8 代码块里仍给出 kill 示例并存 |
| 参考资料 / 预告 | 四条外部官方入口仍是现行官网；内链文件存在；预告 12A「先 SELECT 再改数」，且声明 11 与 12 并列 | 好 | 无越权讲 SQL | 外部 HTTP 状态码见 §18 |

禁止的错误绝对化：本章明确写「登录、下单用 POST 是语义，不是 POST 更加密。HTTPS 仍然必要。」Cookie 只作为 Copy as cURL 要删的凭证，不当成与 Session/Token 三选一。无 P0/P1/P2 等级全球统一。无「没找到 Bug 就没有 Bug」。

---

## 8. 代码问题

### 8.1 正文命令（逐条重推）

| 命令 | 独立推导 | 本轮执行 | 结果 |
| --- | --- | --- | --- |
| `ls -l /tmp` | 长格式列出 | 等价在练习目录执行 `ls -l` | 通过；macOS 带 `@` |
| `ls --help` | GNU 有；BSD 常无 | 执行 | `ls: unrecognized option '--help'`，与正文一致 |
| `man ls` | 手册 | 未进交互；`q` 退出属 less 习惯，正确 | 未交互跑 |
| `pwd` `ls` `ls -l` `ls -la` `ls -lh` | POSIX/GNU/BSD 均有 | 在 `project/minishop` 与 `/tmp` 练习场 | 通过 |
| `cd /tmp` `cd ~` `cd -` `cd ..` | POSIX | 练习场 | `cd -` 回到前一目录，通过 |
| `mkdir -p` `touch` `cp` `mv` `rm`（仅练习文件） | POSIX | `/tmp/ch11-audit-lab-*` | 通过 |
| `head -n` `tail -n` `cat` `echo >` `>>` `2>` | POSIX | 练习场 | 通过 |
| `grep -n "inventory reject" evidence/logs/app-sample.log` | 内容搜索 | 执行 | 5 行 INFO，均含 qty=11 |
| `grep ERROR app.log`（对样本） | 字面 ERROR | 对样本执行 | 0 行，与正文一致 |
| `grep -E "login ok\|inventory reject"` | ERE 交替 | 执行 | 13 行，与 `grep-app-log.txt` 一致 |
| `find . -name "*.log"` | 按名 | 在 minishop 下 | `evidence/logs/app-sample.log`、`logs/app.log` |
| `ps aux` | BSD/GNU 都有 | 执行 | 有 USER/PID/COMMAND |
| `ps aux \| grep minishop` | 关键字 | MiniShop 以 `python3 server.py` 运行时 | **0 命中**，CH11-0004 |
| `kill <自建 sleep PID>` 默认 TERM | 默认 SIGTERM | `sleep 30` 后 `kill` | 进程结束，TERM_OK。**未使用 -9** |
| `chmod 644` | rw-r--r-- | 练习文件 | `-rw-r--r--@` |
| `df -h .` `du -sh` `which curl` `echo $HOME` | 常见 | 执行 | 通过；df 为 APFS |
| `free -h` | Linux procps | 执行 | `command not found`，与正文一致 |
| `pgrep -a` | 见 CH11-0002 | 读 man | macOS `-a` = ancestors |
| `ssh -V` | 客户端存在 | 执行 | OpenSSH_9.9p2。**未登录 192.0.2.10** |
| `curl` GET `/api/products?keyword=mouse` | 章内最小读取 | 执行 | 200 + `{"items": []}`，CH11-0001 |
| `curl` GET `/api/products` | 推导的可用最小读取 | 执行 | 200 + 3 件商品 |
| `curl` GET `/products`、POST `/login` | 正文反例 | 执行 | 均为 404 `not found` |
| `curl` POST `/api/login` `<redacted>` | 可复制块 | 执行 | 401 |
| `curl` POST `/api/login` `Test1234` | 旁白 | 执行 | 200 + Set-Cookie HttpOnly + token |
| `curl -w '%{http_code}'` | 表内选项 | 执行 | 打印 200 |
| `curl -sS -D - -o file` | 头到终端、体到文件 | 执行 | 行为符合 man |
| `curl` POST `/api/cart/items` qty=11 + Bearer | 11-1 / 场景 | 执行 | 400 `qty exceeds stock`；`logs/app.log` 追加 inventory reject |
| `journalctl` | systemd | `command -v` | 本机无 |
| `top` `less` 交互 | q 退出、/ 搜索 | **未进交互** | 仅核对手册习惯 |
| `rm -rf /` `chmod 777` `kill -9` `curl \| bash` `-k` | 反例 | **故意不执行** | 警告足够，见 §7 11.4/11.8/11.9/11.13 |

### 8.2 实操代码

`practice/11-log-grep/main.py`：逻辑正确。`MiniShopLab` 用临时库和临时日志，不改教学库。登录教学账号 → POST `/api/cart/items` `{sku: SKU-DEMO-001, qty: 11}` → 读日志中 `inventory reject`。判定 `cart_status == 400 and hits and "qty=11" in hits[0]` 与 PRD `R-CART-10`、`qty_allowed(11, 10) is False`、`_cart_items` 打 400 并 `_app_log` 一致。

问题：① 观察不是 grep 二进制（CH11-0007）；② 结论文案「操作失败」（CH11-0017）；③ `parsed["token"]` 无登录失败保护，但种子账号下稳定。

`tests/test_lab.py`：调用 `lab.main()` 断言返回 0、http 400、log_hits 含 inventory reject。本轮 `python3 practice/run.py 11-1 --check`：1 passed。

### 8.3 未教授概念

11-1 脚本用到 `urllib`、上下文管理器、临时目录、线程 HTTP 服务。practice README 声明读者不必读懂 `.py`。可接受。不要在第 11 章正文展开这些。

---

## 9. 图片问题

三张图均用 `read_file` 打开 PNG（视觉）和 HTML（源）。无 mermaid。无 `ch11-time-align`。

```
IMG-CH11-001
文件：chapters/assets/diagrams/ch11-path.png（源 ch11-path.html）
出现位置：11.3，alt「终端里的当前目录就是你的位置」
图片主要内容：假终端窗口，pwd=/Users/you/project/minishop，ls 列出 README.md server.py tests/ logs/ evidence/；说明相对路径 logs/app.log 从当前位置算。
技术准确性：正确。macOS 风格路径对多数读者有帮助。ls 是示意，不是 evidence/linux/pwd-ls.txt 的完整列表。
与正文一致性：与 11.3 命令表一致。caption 改去讲 evidence 路径，不一致。
文字是否正确：lead「pwd 问位置，ls 看周围，cd 搬家」正确。
UI 是否过时：示意图，无产品 UI。
教学价值：高，解决「我以为我在某目录」。
可读性：上半清晰，下半大片空白。
是否需要修改：是
修改建议：改 caption；压缩 PNG 高度。
最终结论：MODIFY
```

```
IMG-CH11-002
文件：chapters/assets/diagrams/ch11-grep-find.png（源 ch11-grep-find.html）
出现位置：11.6，alt「grep 找字，find 找文件名」
图片主要内容：左卡 grep 搜内容（grep -E "login ok|inventory reject" logs/app.log）；右卡 find 搜路径（find . -name "app.log"，不读正文）。lead：页面 400 时搜 inventory reject；样本 INFO，不要默认 grep ERROR。
技术准确性：正确。grep vs find 目的不同。
与正文一致性：400 + INFO 已与正文/11-1/evidence 对齐（旧「页面 500」已不在现行图里）。命令指向 logs/app.log，工作实战指向 app-sample.log，文件不同但都合法。
文字是否正确：是。
UI 是否过时：否。
教学价值：高，是本章概念难点。
可读性：命题清楚；底部空白同 CH11-0016。
是否需要修改：可选，统一日志路径或注明「现场 logs/app.log / 对照样本」。
最终结论：KEEP
```

```
IMG-CH11-003
文件：chapters/assets/diagrams/ch11-pipe.png（源 ch11-pipe.html）
出现位置：11.7，alt「管道把左边的出口接到右边的入口」
图片主要内容：tail -n 200 app.log → | → grep "qty=11" → | → 屏幕/文件。caption：| 接输出；> 会覆盖。
技术准确性：管道模型正确。grep "qty=11" 对本仓库样本能命中 inventory reject 行（本轮 5 行）。
与正文一致性：正文 11.7 示例是 grep inventory，图是 qty=11，都打得到超库存行，不冲突。
文字是否正确：是。
UI 是否过时：否。
教学价值：高。
可读性：三卡加竖条能读出管道；底部空白。
是否需要修改：仅排版空白。
最终结论：KEEP
```

缺图（最多作为建议，见 §15）：Network 时间 vs 日志时间（含时区）；本机可练 vs 授权 Linux；ps 认 PID 再 kill。

---

## 10. 表格问题

见 §1.2。需改的表：

- grep 选项表 `-R`：CH11-0003
- 学习目标虽不是表，功能上等同一张「必须掌握清单」：CH11-0006
- 缺「本机 vs Linux」表：CH11-0008
- chmod 数字表：正确，无 ISSUE
- curl 选项表：正确；与 `-d` 隐含 POST 的官方语义一致

`ls -l` 表「长格式：权限、所有者、大小、时间」可补「第一位是类型」，CH11-0022。

---

## 11. 练习与答案问题

### 11.1 章内小练习（先独立作答，再对答案）

| 题 | 独立答案 | 教材答案 | 判定 |
| ---: | --- | --- | --- |
| 1 | pwd=我在哪；ls -l=这里有什么/权限/时间。未确认就 rm/cd 会进错目录 | 同 | 一致 |
| 2 | `../logs/app.log` 依赖 CWD；改绝对路径或先 cd 到固定目录 | 同 | 一致 |
| 3 | 大文件打爆终端；改 head/tail/less/grep | 同 | 一致 |
| 4 | 内容→grep；`*.log` 文件名→find | 同 | 一致 |
| 5 | 末 100 行再筛 ERROR；`>` 覆盖，`grep ERROR > app.log` 可能毁掉日志 | 同，并补充 MiniShop 样本是 INFO | 一致，教材多一句有价值 |
| 6 | B | B | 一致 |
| 7 | du -sh 找大目录，申请授权再清；禁止 rm -rf /var/log、chmod 777 | 同 | 一致 |
| 8 | 删 Cookie/Token/密码；确认测试 URL。只能证明该 HTTP，不能证明按钮/渲染 | 同 | 一致 |
| 9 | 不能说明内存泄漏。free 主要是 Linux 命令 | 同 | 一致 |
| 10 | `grep "inventory reject" evidence/logs/app-sample.log`（或 SKU-DEMO-001）；贴命令+命中行+时间戳；去掉密码/会话/PII。命中是 INFO | 同 | 一致 |

无 【ANSWER VERIFICATION FAILED】。练习形态缺口见 CH11-0012。

### 11.2 阶段测验第 11 章题（先独立作答）

覆盖文件 `chapters/quizzes/stage-4-ops.md`。只评第 11 章题。Q5–Q8、Q10 的 SQL 选项属第 12 章，不审该章正文。

| 题 | 独立答案 | 公布答案 | 判定 |
| ---: | --- | --- | --- |
| 1 | grep 找文件内容；find 找文件名/路径 | 同 | 一致 |
| 2 | -9 不给进程收尾；777 把权限放到最大。先确认 PID 和路径 | 同 | 一致 |
| 3（必过） | free -h 是 Linux 命令，macOS 行为不同。内存结论要到授权 Linux 上看 | 同 | 一致 |
| 4 | 不要写进可分享文件；Copy as cURL 后删凭证；可能进 history。v1.0 为 `POST http://127.0.0.1:8765/api/login`，不要打 `/login` | 同 | 一致 |
| 10 选项 A | 「Linux 是 SQL 硬前置」错误，与正文 L23 一致 | 正确句是 C | 一致（A 作为干扰项成立） |
| 9 交叉 | qty=11 被拒后库中该 SKU 的 qty **不可以**是 11；这不是实操 12-1 | 同 | 口径一致；不扩审第 12 章 |

无 【ANSWER VERIFICATION FAILED】。

### 11.3 实操 11-1 验收

本轮：

```
python3 practice/run.py 11-1          → exit 0
HTTP 400 {"error": "qty exceeds stock"}
日志：INFO  inventory reject sku=SKU-DEMO-001 stock=10 qty=11
python3 practice/run.py 11-1 --check  → 1 passed
```

与 README 验收（400、inventory reject、qty=11、写 latest.json）一致。样本不要 grep ERROR：对 `app-sample.log` 实测 0 行。

---

## 12. 初学者理解障碍

标记 【Beginner Friction】：

1. 748 行命令目录。虽有「今天先走这条线」，学习目标仍是 12 条，读者不知道哪些可以明天再看（CH11-0006）。
2. 可复制登录 curl 用 `<redacted>`，抄完 401（CH11-0010）。
3. 最小读取 `keyword=mouse` 得到空列表（CH11-0001）。
4. 11-1 打印「grep」却不让读者敲 grep（CH11-0007）。
5. macOS 上 `ls --help`、`free`、`pgrep -a`、`grep -R` 行为与教材 Linux 口径不完全同一套，散落在全文（CH11-0002/0003/0008）。
6. `ps | grep minishop` 在 `python3 server.py` 下为 0，读者以为服务没起（CH11-0004）。
7. 工作实战 grep 样本得到 13 行，正文摘录 2 行（CH11-0014）。
8. 图 path 的 caption 不讲 pwd（CH11-0015）。
9. 没有「我现在这台电脑能练什么」总表，开篇又说目标环境是 Linux 服务器（CH11-0008）。
10. Windows 只提 WSL，Git Bash 用户会碰到路径和 `free` 问题，没有出口。

`rm -rf` / `kill -9` / `chmod 777` 的警告对初学者是够的：禁止列表 + 错误 1/2/3 + 工作实战勾选「未做」+ 可运行性说明。不构成 P0。

---

## 13. 岗位能力缺口

标记 【Job Reality Gap】：

1. 现场日志路径 `logs/app.log` 与预置样本未分开（CH11-0011）。入职第一周就是「复现 → tail -f → grep 这一次」。
2. 时间对齐只有原则，没有 MiniShop 的 GMT vs 本地实例（CH11-0009）。这是写缺陷被开发打回的高频原因。
3. 进程识别用产品名 grep，不教「看 COMMAND 全路径」（CH11-0004）。
4. ssh 标必须掌握但允许不做，真实团队则是堡垒机/VPN/工单，本章边界声明是对的，星级过满（CH11-0005）。
5. 没有「改一条 grep 模式」的动手（CH11-0012）。岗位上就是把 ERROR 改成业务关键字。
6. `journalctl -u` 有命令形态，没有「问部署文档里的 unit 名」的更具体例子（可接受，已写因发行版而异）。
7. scp 仍可用；OpenSSH 现行更推 sftp。了解级即可，未单列 ISSUE。

面试五题覆盖 grep/find、磁盘、kill、curl 脱敏，方向对，能支撑初级面试的 Linux 口试。

---

## 14. 建议删除内容

- 不要删 11.4/11.9/11.11 整节，改标可后读即可。
- 不要删 `kill -9` / `chmod 777` / `rm -rf /` 的反例。
- 不要把 `evidence/linux/df.txt` 改成假的 Linux `free -h`。
- 可删学习目标里与「今天先走这条线」重复的 mkdir 全家桶细项，或降成「见 11.4」。
- 可复制块里的 `"password":"<redacted>"` 不要当本机第一条（改为第二条分享版）。

---

## 15. 建议新增内容

1. 本机可练 vs 授权 Linux 表（CH11-0008）。
2. 11.12 时间对齐图 + MiniShop `Date: GMT` vs 日志本地时间一行对照（CH11-0009）。
3. 现场日志 `logs/app.log` 与样本 `app-sample.log` 对照（CH11-0011）。
4. 两条 curl：本机 Test1234 / 分享 `<redacted>`（CH11-0010）。
5. 练习：对同一文件改 grep 模式看命中变化（CH11-0012）。
6. `ps` 认 MiniShop 进程名（server.py）（CH11-0004）。
7. （可选）11.8 先 ps 再 kill 的小图。

---

## 16. 建议重写内容

- **11.13 最小读取 curl**：必须改 `keyword=mouse`（CH11-0001）。这是唯一建议立刻改的可复制命令。
- **学习目标**：按一句话核心重写成 5 条，而不是 12 条命令（CH11-0006）。
- **11-1 入口位置**：从 11.13 之后挪到 11.6/11.7 之后（CH11-0007）。不必重写脚本逻辑。
- 不需要重写 11.1–11.5 路径与读日志主线。
- 不需要把章节拆成 11A/11B。命令目录可保留，靠阅读路径和星级过滤。

---

## 17. 本章结论

**B 小修**

可以发布前建议至少改：CH11-0001（mouse curl）、CH11-0002/0003（选项的 GNU/BSD 差异各一句）、CH11-0010（本机可跑的登录 curl）。其余 P2 是教学顺序与练习形态，不阻断读者学完「日志是观察通道」。

不是 A：存在一条会让学生抄出空搜索结果的 P1，以及多处未声明的 macOS/Linux 选项差异。  
不是 C/D/E：qty=11 的 400+INFO 已与仓库一致；危险命令警告足够；实操可跑；练习答案正确；未虚构远程主机；未教禁止的绝对化规则。

---

## 18. 执行记录

### 18.1 读过的文件

全局：`reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`、`REPOSITORY_INVENTORY.md`、`MASTER_AUDIT.md`、`AUDIT_PROGRESS.md`（只读，未改）；`README.md`；`docs/COURSE_CONTROL.md`、`COURSE_OUTLINE_v1.2.md`、`LEARNING.md`；`standards/QUALITY_STANDARD_v1.0.md`；`practice/README.md`、`STATUS.md`；`exercises/README.md`；`project/minishop/README.md`、`docs/PRD.md`、`docs/openapi.json`。

本章：`chapters/11-linux.md`；`practice/11-log-grep/README.md`、`main.py`、`tests/test_lab.py`、`validation/latest.json`（跑完后的本机文件）；`practice/run.py`、`_http.py`、`_minishop.py`；`project/minishop/evidence/linux/pwd-ls.txt`、`grep-app-log.txt`、`df.txt`、`curl-login-headers.txt`；`evidence/logs/app-sample.log`；`evidence/README.md`；`evidence/http/05-cart-qty-11.txt`；`project/minishop/server.py`（日志、登录、商品搜索、购物车）；`frontend/app.js`（页面失败文案）；`run.py`（serve 进程路径）；`chapters/quizzes/README.md`、`stage-4-ops.md`（先看题再看答案）；`chapters/assets/diagrams/ch11-path.html/.png`、`ch11-grep-find.html/.png`、`ch11-pipe.html/.png`、`README.md`。

线索（独立复核，未照抄结论）：`reviews/chapter-11-review.md`；`reviews/_pedagogy-2026-09-10/ch11.md`、`MASTER.md`、`RUBRIC.md`；`reviews/_rereview-2026-09-09/stage-4-ch09-11-12.md`、`MASTER.md`、`cross-cut.md`；`reviews/v1.2.1-rescore.md`。

未读其他章正文。Q9 只作 qty=11 口径交叉。

### 18.2 实际跑过的命令与结果摘要

| 命令 | 结果摘要 |
| --- | --- |
| `python3 practice/run.py 11-1` | exit 0；HTTP 400；日志 INFO inventory reject qty=11；写出 validation/latest.json |
| `python3 practice/run.py 11-1 --check` | `test_log_has_reject ... ok`，1 passed |
| `cd project/minishop && pwd && ls` | 路径与文件名与 `pwd-ls.txt` 一致 |
| `grep -n "inventory reject" evidence/logs/app-sample.log` | 5 行 INFO |
| `grep ERROR` 对样本 | 0 行 |
| `grep -E "login ok\|inventory reject"` | 13 行 = `grep-app-log.txt` |
| `grep "qty=11"` | 5 行 |
| `find . -name "*.log"` | 样本 + `logs/app.log` |
| 练习场 mkdir/touch/cp/mv/rm/head/tail/echo 重定向/2>/chmod 644/cd - | 通过 |
| `ls --help` | unrecognized option（BSD） |
| `free -h` | command not found |
| `df -h .` | APFS `/dev/disk3s5`，列名 Capacity |
| `which ls/curl/grep/find` | /bin/ls，/usr/bin/{curl,grep,find} |
| `ps aux \| grep minishop`（python3 server.py 运行中） | 无命中 |
| `kill` 默认信号打自建 `sleep` | TERM_OK |
| `man pgrep` / `man grep` / `man kill` / `man curl` | 见 CH11-0002/0003；kill 默认 TERM |
| `ssh -V` | OpenSSH_9.9p2 |
| `python3 server.py`（本机 127.0.0.1:8765，审完已 kill PID 77142） | GET mouse → 空 items；GET 无 keyword → 3 件；POST `/login` 与 GET `/products` → 404；POST `/api/login` redacted → 401；Test1234 → 200+Set-Cookie；qty=11 → 400 且 `logs/app.log` 追加 reject |
| `curl -w '%{http_code}'` | 200 |
| `journalctl` | 本机无此命令 |
| `top`/`less`/`ssh` 登录/`scp`/`kill -9`/`rm -rf /`/`chmod 777`/`curl \| bash` | **未执行** |

副作用：默认 `MINISHOP_RESET=1` 的 `python3 server.py` 会重建教学库。这是项目默认行为。审完已停止本 Agent 启动的 8765 监听（PID 77142）。审查期间还曾见到 PID 76724 的 `Python server.py`（未占用 8765），不是本 Agent 的 8765 进程，未杀。

### 18.3 外部核查

| 条目 | 方式 | 结论 |
| --- | --- | --- |
| GNU Coreutils 手册 URL | web_search；`web_fetch` 被 SSRF 拦到 198.18.x | 官方入口仍是 gnu.org/software/coreutils/manual；单页 HTML 惯例为 coreutils.html。**【External Verification Required】** 本环境未拿到该 URL 的 HTTP 状态码 |
| GNU grep 手册 | 同 | 路径仍是 gnu.org/software/grep/manual/。**-r vs -R 符号链接差异**已用 GNU 文档与 StackExchange/手册交叉确认 |
| curl man | web_search curl.se/docs/manpage.html（页面 2026-09-06） | 现行官方 man；`-d` 发送 POST 已确认 |
| OpenSSH | web_search openssh.com（OpenSSH 10.5，2026-08-11） | 官网仍在；本机客户端 9.9p2 |
| RFC 5737 | web_search | `192.0.2.0/24` TEST-NET-1，文档地址，正文声明正确 |
| Linux pgrep `-a` | man7.org pgrep(1) 检索 | `--list-full` |
| macOS pgrep `-a` | 本机 man | ancestors，不是 list-full |
| macOS grep `-R`/`-r` | 本机 man | 别名；跟链接用 `-S` |
| MiniShop 行为 | 读 server.py + 实打 HTTP | 400 + INFO inventory reject；搜索不认 mouse |

### 18.4 独立作答顺序

阶段测验与章内练习均先根据 Linux/POSIX/MiniShop 实现自行作答，再与教材答案比较。比较结果见 §11。无答案错误。
