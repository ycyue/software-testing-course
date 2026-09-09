# 实操练习

← [返回主目录](../README.md) · 📚 [学习建议](../docs/LEARNING.md)

本目录是课程的 **实操练习**：在 MiniShop 上亲手做一次测试动作，留下可复核的结果。

不是另一套电商系统。章末「小练习」巩固概念；这里动手。书面产出（评审记录、缺陷单、简历草稿）存进 [`exercises/`](../exercises/README.md)。

你不需要读懂每个 `.py` 文件。先看目标、最小命令、验收条件。

## 三种实操

| 图标 | 类型 | 含义 |
| :--: | --- | --- |
| ✅ | **可运行实操** | 一条命令能出结论和 `validation/latest.json` |
| 📖 | **书面实操** | 写评审/缺陷单，或使用 Postman / 浏览器 |
| 🚧 | **未跑完** | 仓库有骨架或步骤，作者没有留下 GUI/压测结论 |

```bash
python3 practice/run.py --list
python3 practice/run.py 1-1
python3 practice/run.py 1-1 --check
```

1-1、5-1、8-1、9-1、11-1、12-1、13-1、15-1 只依赖 Python 3 标准库，会自己拉起临时 MiniShop。  
16-1、19-1 需要先 `python3 project/minishop/run.py setup`。

克隆仓库 ≠ 实操完成。状态见 [STATUS.md](STATUS.md)。`validation/latest.json` 是你本机跑出来的证据，已加入 `.gitignore`，不会把工作区弄脏。

## 怎么做

| 层级 | 先看什么 |
| --- | --- |
| **先做** | 目标、一条命令、验收条件。从 [1-1](01-observation-oracle-evidence/) 开始 |
| **再改** | 你改哪一个输入，结论如何变（空白关键字、qty、SQL） |
| **能交代** | 本机 `validation/latest.json`（不入库）、缺陷是否仍开放，别人能否复核 |

## 可运行实操

当天先做 1-1。后面按学习顺序补。

| 编号 | 项目 | 类型 | 你要亲手做成什么 |
| :--: | --- | :--: | --- |
| 1-1 | [observation-oracle-evidence](01-observation-oracle-evidence/) | ✅ | 对空白搜索分别只观察、只读需求、对照并留证据 |
| 5-1 | [qty-boundary](05-qty-boundary/) | ✅ | `qty=10` 与 `qty=11` 成对测，说明切点 |
| 8-1 | [privilege](08-privilege/) | ✅ | 他人订单 403；普通用户进不了后台 |
| 9-1 | [http-observe](09-http-observe/) | ✅ | 把一次登录拆成方法、路径、头、体 |
| 11-1 | [log-grep](11-log-grep/) | ✅ | `qty=11` 之后在日志里 grep `inventory reject` |
| 12-1 | [sql-cross-check](12-sql-cross-check/) | ✅ | 用 SQL JOIN 核对购物车数量 |
| 13-1 | [api-shapes](13-api-shapes/) | ✅ | 缺字段 / null / 空串 / 错误类型分开测 |
| 15-1 | [json-check](15-json-check/) | ✅ | 把商品列表当成 JSON 读回来 |
| 16-1 | [pytest-regression](16-pytest-regression/) | ✅ | 跑通 pytest，能解释 1 条 xfail |
| 19-1 | [project-pack](19-project-pack/) | ✅ | PRD、BUG-001、OpenAPI 都在，基线仍是 37/1 |

## 各章实操

按**正式学习顺序**。未单列脚本的章，实操就是该章「MiniShop 工作实战」：把产出存进 `exercises/`。

| 编号 | 章 | 类型 | 做什么 | 入口 |
| :--: | --- | :--: | --- | --- |
| 1-1 | 1 | ✅ | 观察 / 判定 / 证据 对照 | [01-…](01-observation-oracle-evidence/) |
| 2-1 | 2 | 📖 | 在 MiniShop 上标出需求→提测→冒烟会落在哪 | [第 2 章工作实战](../chapters/02-software-development-process.md) |
| 3-1 | 3 | 📖 | 给登录、搜索、购物车贴分类坐标，不要互斥单选 | [第 3 章工作实战](../chapters/03-software-testing-classification.md) |
| 7-1 | 7 | 📖 | 打开页面，记录 URL 与 HTML | [第 7 章](../chapters/07-web-basics.md) · [HTML 练习页](../chapters/assets/07-html-lab.html) |
| 4-1 | 4 | 📖 | 写一页需求评审，分清教学草案和 v1.0 PRD | [04-…](04-requirement-review/) |
| 5-1 | 5 | ✅ | 库存边界两侧 | [05-…](05-qty-boundary/) |
| 6-1 | 6 | 📖 | 按模板写缺陷单（可针对 BUG-001） | [06-…](06-bug-report/) |
| 8-1 | 8 | ✅ | 他人订单 403、非管理员 403 | [08-…](08-privilege/) |
| 9-1 | 9 | ✅ | HTTP 四格 | [09-…](09-http-observe/) |
| 10-1 | 10 | 📖 | DevTools 取证；**仓库没有面板截图** | [第 10 章](../chapters/10-chrome-devtools.md) |
| 11-1 | 11 | ✅ | qty=11 后 grep 日志 | [11-…](11-log-grep/) |
| 12-1 | 12 | ✅ | SQL 交叉验证 | [12-…](12-sql-cross-check/) |
| 13-1 | 13 | ✅ | 四种 Body 形状 | [13-…](13-api-shapes/) |
| 14-1 | 14 | 📖 | 导入 Postman 集合；**作者未点 GUI Runner** | [第 14 章](../chapters/14-postman.md) |
| 15-1 | 15 | ✅ | 读商品 JSON | [15-…](15-json-check/) |
| 16-1 | 16 | ✅ | pytest 基线 | [16-…](16-pytest-regression/) |
| 17-1 | 17 | 📖 | 画 MiniShop 自动化分层，不写 Playwright 套件 | [第 17 章](../chapters/17-automation-overview.md) |
| 18-1 | 18 | 🚧 | 有 `.jmx` 骨架和步骤，**未安装、未跑 JMeter GUI** | [第 18 章](../chapters/18-performance-testing.md) |
| 19-1 | 19 | ✅ | 项目包 + pytest 基线 | [19-…](19-project-pack/) |
| 20-1 | 20 | 📖 | 用项目证据写一页面试口述 | [第 20 章](../chapters/20-interview.md) |
| 21-1 | 21 | 📖 | 一页诚实简历草稿 | [第 21 章](../chapters/21-job-hunting.md) |
| 22-1 | 22 | 📖 | 对照三梯队做结课自检 | [第 22 章](../chapters/22-learning-path.md) |

第 19 章之前正文里的 `/login`、验证码、优惠券若出现，是**教学约定**，可运行实操一律打 v1.0 的 `/api/` 与 PRD 规则。
