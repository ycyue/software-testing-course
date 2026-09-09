# 软件测试从零基础到初级测试工程师

**测试 = 观察 + 判定 + 证据**——本课程围绕这个核心公式，用 22 章把软件测试从思维方式讲到可展示的 MiniShop 项目。全书正文、示意图、阶段测验和配套实操练习都在本仓库，欢迎亲手做一遍。

| 📚 **22 章** 正文，零基础到初级测试工程师 | 🛒 **MiniShop** 可运行实践项目 | 🧪 **起步实操** 一条命令完成一次测试动作 |
| :---: | :---: | :---: |

> 找 Bug 只是观察里出现了不符合判定的结果。没有尺子（判定），你只是在看热闹；没有底稿（证据），你无法向别人证明你看见了什么。

## 先跑起来

需要本机 `python3`（3.12+ 即可）。

```bash
git clone https://github.com/ycyue/software-testing-course.git
cd software-testing-course

# 当天就能做的最小实操：空白搜索到底算不算 Bug？
python3 practice/run.py 1-1
```

把 MiniShop 项目本身跑起来：

```bash
cd project/minishop
python3 run.py setup      # 创建 .venv 并安装 pytest / requests
python3 run.py serve      # 浏览器打开 http://127.0.0.1:8765
```

另开一个终端：

```bash
python3 run.py test       # 基线：37 passed, 1 xfailed（BUG-001 仍开放）
```

教学账号密码均为 `Test1234`，只许用在本机。MiniShop 是**个人软件测试实践项目**，不得写成某公司电商系统。

如何读、先读哪几章、实操怎么分层：见 **[学习建议](docs/LEARNING.md)**。

## 内容速览（按学习顺序）

文件名里的章号保留历史编号；**阅读请按下表，不要按 04 在 07 前面的文件名顺序。**  
「读」= 章节正文；「实操」= 该章最小可验收的动手练习。

| 章 | 主题 | 一句话核心 | 正文 | 实操 |
| :--: | --- | --- | :--: | :--: |
| 1 | 软件测试入门 | **测试 = 观察 + 判定 + 证据** | [读](chapters/01-software-testing-intro.md) | [1-1](practice/01-observation-oracle-evidence/) |
| 2 | 研发流程与测试位置 | 测试位置由生命周期决定，不是等开发写完 | [读](chapters/02-software-development-process.md) | [2-1](practice/README.md) |
| 3 | 测试分类 | 分类是坐标轴，不是互斥工种 | [读](chapters/03-software-testing-classification.md) | [3-1](practice/README.md) |
| 7 | Web 基础 | 页面只是一条观察通道 | [读](chapters/07-web-basics.md) | [7-1](practice/README.md) |
| 4 | 需求分析与静态测试 | 判定标准来自需求；需求不清后面全漂 | [读](chapters/04-requirements-analysis-and-static-testing.md) | [4-1](practice/04-requirement-review/) |
| 5 | 测试用例设计 | 用例是把判定写成可执行步骤 | [读](chapters/05-test-case-design.md) | [5-1](practice/05-qty-boundary/) |
| 6 | 缺陷与测试管理 | 缺陷单是证据；计划回答测什么、不测什么 | [读](chapters/06-bug-and-test-management.md) | [6-1](practice/06-bug-report/) |
| 8 | Web 功能测试 | Cookie / Session / Token 不是三种可互换产品 | [读](chapters/08-web-functional-testing.md) | [8-1](practice/08-privilege/) |
| 9 | 网络与 HTTP | HTTP 把观察拆成方法、路径、头、体 | [读](chapters/09-computer-network-and-http.md) | [9-1](practice/09-http-observe/) |
| 10 | Chrome DevTools | 把已经发生的观察打开给你看 | [读](chapters/10-chrome-devtools.md) | [10-1](practice/README.md) |
| 11 | Linux | 日志和进程是页面上看不到的通道 | [读](chapters/11-linux.md) | [11-1](practice/11-log-grep/) |
| 12 | 数据库与 SQL | UI 对了库不对，仍是缺陷 | [读](chapters/12-database-and-sql.md) | [12-1](practice/12-sql-cross-check/) |
| 13 | 接口测试 | 绕过 UI，直接对契约观察 | [读](chapters/13-api-testing.md) | [13-1](practice/13-api-shapes/) |
| 14 | Postman | 把接口观察做成可重复集合 | [读](chapters/14-postman.md) | [14-1](practice/README.md) |
| 15 | Python 基础 | Python 是为了处理观察结果 | [读](chapters/15-python-basics.md) | [15-1](practice/15-json-check/) |
| 16 | pytest | 把明确的判定交给脚本回归 | [读](chapters/16-pytest.md) | [16-1](practice/16-pytest-regression/) |
| 17 | 自动化分层 | 越靠近 UI 的观察越贵 | [读](chapters/17-automation-overview.md) | [17-1](practice/README.md) |
| 18 | 性能测试基础 | 功能绿了不等于扛得住 | [读](chapters/18-performance-testing.md) | [18-1](practice/README.md) |
| 19 | MiniShop 项目 | 把三要素收成能指给人看的仓库 | [读](chapters/19-minishop-project.md) | [19-1](practice/19-project-pack/) |
| 20 | 面试 | 用项目证据讲，不要背名词 | [读](chapters/20-interview.md) | [20-1](practice/README.md) |
| 21 | 求职 | 只写仓库里能指出来的东西 | [读](chapters/21-job-hunting.md) | [21-1](practice/README.md) |
| 22 | 学习路线 | 先保住能测完 MiniShop 主路径 | [读](chapters/22-learning-path.md) | [22-1](practice/README.md) |

> 实操类型：✅ 可运行 / 📖 书面实操（写评审、点 GUI）/ 🚧 骨架在、作者未跑完。说明见 [practice/README.md](practice/README.md)。  
> 过长章拆成上/下（04、06、08、12、15、16），索引页只负责分流。

## MiniShop 是什么、不是什么

本仓库唯一主案例。有前端、后端、SQLite、PRD、OpenAPI、Postman 集合、pytest、日志、缺陷和证据目录。

**v1.0 明确不做：** 支付、物流、优惠券、订单状态机、HTTPS、生产部署。订单成功只返回 `id`，响应里**没有** `status`。

第 19 章之前正文若出现验证码、优惠券、`/login` 教学路径，会标明那是教学约定，不是已冻结契约。项目规则以 [`project/minishop/docs/PRD.md`](project/minishop/docs/PRD.md) 为准。

已知开放缺陷：[BUG-001 空搜索返回全量商品](project/minishop/bugs/BUG-001.md)。pytest 里对应 1 条 xfail。不要写成已修复。

## 阶段测验与作业

- 阶段测验：[chapters/quizzes/](chapters/quizzes/README.md)（10 题至少 8 题，必过题要用自己的话解释）
- 自己的书面作业放 [`exercises/`](exercises/README.md)，参考答案在各章正文
- 概念示意图：[chapters/assets/diagrams/](chapters/assets/diagrams/README.md)

## 诚实边界（作者没有假装做过的事）

- Postman Collection Runner、JMeter GUI、Chrome DevTools **面板**本身：无截图
- 第 18 章有 `.jmx` 骨架，**未安装、未跑** JMeter
- Playwright 只用于取证，不是 UI 回归套件
- 每次默认重置教学库，不适合当长期环境

完整台账：[practice/STATUS.md](practice/STATUS.md)。

## 作者工作台

写教材、审查、评分用这些文件；**学习者不必从这里开始。**

- [课程主控](docs/COURSE_CONTROL.md)
- [v1.2 大纲](docs/COURSE_OUTLINE_v1.2.md)
- [质量标准](standards/QUALITY_STANDARD_v1.0.md)
- [v1.2.1 复评（取消大面积 99 分）](reviews/v1.2.1-rescore.md)
- 逐章审查记录在 `reviews/`

当前版本 **v1.2.2**：在 v1.2.1 证据与重评之上，补上读者入口、核心公式和可运行起步实操。正文仍是 22 章。
