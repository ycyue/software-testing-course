# Chapter 17 Audit

审计对象：第 17 章自动化分层（仅本章及相关列出文件）  
审计员：Chapter-Audit-Agent-17  
日期：2026-09-10  
正文：`chapters/17-automation-overview.md`（526 行）

## 1. Coverage

禁止抽样。下列类型均已通读/打开/推导/复跑；**未检查必须为 0**。

| 类型 | 数量 | 已检查 | 未检查 | 备注 |
| --- | ---: | ---: | ---: | --- |
| 正文文件 | 1 | 1 | 0 | `chapters/17-automation-overview.md` |
| 相关配套文件 | 3 | 3 | 0 | `project/minishop/automation/README.md`；`chapters/quizzes/stage-6-project.md` 第 17 章题；`exercises/README.md` 文件名清单 |
| 示意图 PNG | 2 | 2 | 0 | `ch17-pyramid.png`、`ch17-ui-cost.png`（`read_file` 打开） |
| 示意图 HTML | 2 | 2 | 0 | 同名 `.html` 源 |
| 章内 mermaid | 1 | 1 | 0 | 场景导入 flowchart BT |
| H1（围栏外） | 1 | 1 | 0 | 章标题 |
| H2（围栏外） | 22 | 22 | 0 | 含结构块 13 类齐全 |
| H3（围栏外） | 27 | 27 | 0 | 错误 10 + 面试 6 + 练习 10 + 自测门槛 1 |
| 一句话核心 / 重要级别 / 主案例 | 3 | 3 | 0 | 章头 3 行引用块 |
| 正文段落块 | 95 | 95 | 0 | 围栏外连续散文；含面试「结论/示例/边界」句 |
| 表格（正文渲染） | 5 | 5 | 0 | 17.1 / 17.3 / 17.4 / 17.6 / 17.8 |
| 模板内表格（markdown 围栏） | 1 | 1 | 0 | 工作实战分层表表头，无示例行 |
| 代码围栏 | 7 | 7 | 0 | mermaid / python×2 / bash / yaml / text / markdown |
| Linux/Shell 命令 | 2 | 2 | 0 | `pip install pytest-html`；`pytest -q --html=... --self-contained-html` |
| SQL | 0 | 0 | 0 | 本章无 SQL |
| 完整 HTTP 报文 | 0 | 0 | 0 | 仅路径/方法提及：`POST /api/cart/items`、`qty=11`→400 |
| 测试用例（章内示例函数） | 2 | 2 | 0 | Playwright / Selenium 示例结构；无 assert |
| Bug 示例 | 1 | 1 | 0 | 场景导入假想「登录按钮未绑定 / 文案英文」；非 BUG-001 缺陷单 |
| 小练习题 | 10 | 10 | 0 | 先独立作答再对答案 |
| 小练习答案 | 10 | 10 | 0 | |
| 阶段测验第 17 章题 | 1 | 1 | 0 | stage-6 Q1（及答案）；Q2–10 属 18/19，不审他章正文 |
| 检查清单项 | 10 | 10 | 0 | |
| 自测门槛 | 4 | 4 | 0 | |
| 总结要点 | 7 | 7 | 0 | |
| 常见错误 | 10 | 10 | 0 | |
| 面试题 | 6 | 6 | 0 | |
| Markdown 链接（含图） | 11 | 11 | 0 | 外链 6 + 仓内 3 + 图 2 |
| 学习目标条目 | 8 | 8 | 0 | |
| 前置知识条目 | 4 | 4 | 0 | |
| MiniShop 对照点（表+文） | 全部 | 全部 | 0 | `qty_allowed`、`SKU-DEMO-001` 库存 10、`/` 登录页、`#login-btn`、「登录」按钮文案 |
| 仓库 CI 目录 | 1 | 1 | 0 | **无** `.github/`（已确认不存在） |
| MiniShop 实现抽查 | 5 | 5 | 0 | `server.qty_allowed`、`frontend/index.html`、`app.js` 登录绑定、`tests/test_api.py` 8 组 parametrize、`conftest.py` 自起服务 |
| **合计内容单元** | **以上全表** | **100%** | **0** | 未检查 = 0 才宣布完成 |

结构块对照 Quality Standard §七：本章解决什么问题、学习目标、前置知识、场景导入、核心知识（17.1–17.8）、MiniShop 工作实战、常见错误、面试角度、小练习、练习答案、检查清单、本章总结、下一章预告 → **13/13 都在**。缺的是实操「类型」徽章，见 CH17-0007。

## 2. 总评分

| 项目 | 分数 |
| --- | ---: |
| 技术准确性 | 8/10 |
| 岗位实用性 | 8/10 |
| 完整性 | 8/10 |
| 初学者友好度 | 7/10 |
| 教学顺序 | 7/10 |
| 代码质量 | 7/10 |
| 实操质量 | 7/10 |
| 练习质量 | 8/10 |
| 图片质量 | 8/10 |
| **总体** | **80/100** |

分数由 ISSUE 支撑，不继承旧审 99 / 91 / 92。

扣分主因：对照表 Playwright API 用了 Python 不存在的 camelCase（P1）；了解章星级/9 题门槛过重；YAML 示例与 MiniShop 真实运行脱节；安装与 pytest-html 命令像必做实验。

加分主因：接口 ROI 全程带场景、禁止绝对化写进错误 1/练习 9；YAML/Python 均标明「示例结构、不是本仓库流水线」；`goto /` 而非 `/login`；初级边界表可直接用于简历口径；金字塔明确不是 ISTQB 强制比例。

DoD（独立判断，非照抄旧 20/20）：**18/20**。不通过：第 3 项（对照表定位 API 名不准确）、第 14 项（重要级别与 `LEARNING.md`「了解即可」冲突）。其余项通过或仅有 P2/P3 备注。

## 3. P0

无。未把接口 ROI 写成永远最高；未把 YAML 写成「仓库已配置」；未把 `/login` 当可抄路由；未伪造订单状态；未把 Playwright 说成已淘汰 Selenium；Cookie/Session/Token 明确不是金字塔三层。

## 4. P1

## ISSUE
ID：CH17-0004
文件：`chapters/17-automation-overview.md`
章节：第 17 章
小节：17.4 Playwright 与 Selenium
精确位置：L131–137 对照表「定位」行；对照 L145–147 Python 示例
原文：`推荐 getByRole / getByLabel / getByTestId 等`
问题等级：P1
问题类别：CODE / TERM
问题说明：对照表用 JavaScript camelCase 当作推荐定位 API。本课程 Python 轨、示例函数也是 Python。本机已装 Playwright，对 `playwright.sync_api.Page` 内省：`get_by_role` / `get_by_label` / `get_by_test_id` 为 True，`getByRole` / `getByTestId` 为 False。
为什么有问题：零基础按表抄会 `AttributeError`。同一节 Python 示例已经正确写成 `page.get_by_role("button", name="登录")`，表和代码打架，读者无法判断哪边是「正式 API」。
依据：Playwright Python 官方 Writing tests / Locator 文档使用 `get_by_role`；本机 Page API 内省；质量标准「正式代码必须语法正确」——表内 API 名会被当成可抄接口。
建议修改：表内改成 Python 名，并加一句「JS 文档里是 getByRole，Python 是 snake_case」。
推荐替换文本：

```
| 定位 | Python：`get_by_role` / `get_by_label` / `get_by_test_id`（JS 文档写作 getByRole 等，不要在 pytest 里照抄 camelCase） | 常用 id、CSS、XPath 等；同样应避免超长绝对路径 |
```

## 5. P2

## ISSUE
ID：CH17-0001
文件：`chapters/17-automation-overview.md`；对照 `docs/LEARNING.md`
章节：第 17 章
小节：章头重要级别；17.1 / 17.2 / 17.3 / 17.5 / 17.8 / 工作实战；本章总结；进入下一章的自测门槛
精确位置：L4「⭐⭐ 常用」；L56、L76、L97、L174、L266、L283 均为 ⭐⭐⭐；L495「真正掌握七件事」；L488「练习 1～10 至少完成 9 题」
原文：章头 ⭐⭐ 常用；多节 ⭐⭐⭐；总结「真正掌握」；门槛 9/10
问题等级：P2
问题类别：PED / SEQ
问题说明：`LEARNING.md` 把第 17～18 章标为「⚪ 了解即可」；大纲第三梯队才是 UI 自动化与 CI/CD。章内却用必须掌握密度 + 9/10 放行，学习目标一次 8 条能力。
为什么有问题：【Beginner Friction】勤快读者会按核心章去 `pip install pytest-playwright`、配 GitHub Actions。星级在 17.4/17.6 的 ⭐⭐ 与两侧 ⭐⭐⭐ 之间来回跳，不是单调下降。
依据：Quality Standard §三/§七 重要级别；`docs/LEARNING.md` L92；`docs/COURSE_OUTLINE_v1.2.md` 第三梯队；教学尺：了解章不要写成必须掌握的工具手册。
建议修改：章头与 LEARNING 对齐为 ⭐ 了解即可（能口述分层/金字塔/ROI/初级边界；不要求安装 UI 工具或搭 CI）；⭐⭐⭐ 只留给 17.1–17.3 与 17.8 的「能说明」；总结改「能用自己的话说明」；门槛改为地图 + 口述练习 2、4、8、9。
推荐替换文本：见 pedagogy 补丁方向，此处不重贴长文。要点：了解章、不装浏览器、不交 YAML。

## ISSUE
ID：CH17-0002
文件：`chapters/17-automation-overview.md`
章节：第 17 章
小节：MiniShop 工作实战：自动化分层地图
精确位置：L295「按单元 / 接口 / UI / 手工四列，各写至少两条」；L308–309 模板表头 `| 层 | 检查点 | 断言大意 | 现在谁来做 |`（无示例行、无「四列」）
原文：必做 1 要求四列各至少两条；模板是「层」一列
问题等级：P2
问题类别：EX / PED
问题说明：口令「四列」与模板「层」不是同一张表。正文单元层只给了 `qty_allowed(11, 10)` 一条。仓库里其实还有 `valid_phone` / `valid_password`（`server.py`）和第 16 章 `test_qty_rule.py` 四条，但本章未指向，刚会 pytest 接口的读者编不满第二条纯函数检查。
为什么有问题：书面作业无法只靠本章交满；部分学生会去写 Playwright 凑 UI 列，正好违反「本章不交 UI 套件」。
依据：质量标准「练习覆盖目标、答案与练习对应」；MiniShop `server.py` L124–141、`tests/test_qty_rule.py`。
建议修改：改为四层各至少 **1** 条；单元可只写 `qty_allowed`；给一行填好的示例；模板表头与「四层」统一；章内补 📖。
推荐替换文本：四层各一条的示例表（单元 `qty_allowed` / 接口 `POST /api/cart/items` qty=11 / UI 登录按钮 / 手工空搜索体验），并写明「你不必自己实现纯函数」。

## ISSUE
ID：CH17-0003
文件：`chapters/17-automation-overview.md`
章节：第 17 章
小节：场景导入：接口全绿，页面登录按钮却点不动
精确位置：L36–42；mermaid 之后立刻进入 17.1，无「pytest 没写错」锚句
原文：`第 16 章的 pytest 对 POST /api/cart/items 的 qty=11 断言 400，全绿。产品经理打开浏览器：登录按钮没有绑定点击，购物车提示文案是英文。`
问题等级：P2
问题类别：PED / PRE
问题说明：前半句是 MiniShop **真实**行为（本机 `qty_allowed(11,10) is False`；pytest 8 组含 over_stock→400）。后半句是 **假想**故障。实际 `frontend/app.js` 已给 `#login-form` 绑定 submit；文案是中文「登录成功 / 登录失败」，不是英文。mermaid 与 17.2 PNG 都只画金字塔，没有画出「接口门绿、页面门红」。
为什么有问题：【Beginner Friction】学生打开 MiniShop 会发现按钮能点、文案是中文，以为教材过时或自己环境错了。要读到 17.2 / 17.8 才知道第 16 章 pytest 仍是立足层，开篇先打击刚建立的成果。
依据：`frontend/app.js` L33–57；`index.html` L26 按钮「登录」；教学尺「场景要托住上一章」。
建议修改：标明「假想故障，不是 MiniShop 当前缺陷」；mermaid 后立刻写：pytest 没写错，缺的是另一扇门，本章不交 Playwright 套件。
推荐替换文本：

```
（假想故障，用来说明分层；MiniShop v1.0 登录按钮是绑了的，文案也是中文。）
所以测试工程师要问「打在哪扇门」，而不是把第 16 章的 pytest 作废。
接口全绿、登录按钮点不动，说明页面这扇门还没观察；qty 规则仍应留在接口层重复跑。
本章不要求补一套 Playwright。
```

## ISSUE
ID：CH17-0005
文件：`chapters/17-automation-overview.md`；对照 `project/minishop/tests/conftest.py`
章节：第 17 章
小节：17.7 CI/CD
精确位置：L232–251 YAML 围栏
原文：`# 示例结构，不要当作本仓库已配置的 GitHub Actions` + `TEACH_BASE_URL: http://127.0.0.1:PORT` + `python -m pytest -q`
问题等级：P2
问题类别：CODE / PED
问题说明：三次声明「不是本仓库流水线」成立——仓库确无 `.github/`。但示例仍会误导「照这个就能跑 MiniShop」：（1）`conftest.py` 自己 `ThreadingHTTPServer` 起服务，**不读** `TEACH_BASE_URL` / `TEACH_PASSWORD`；（2）作业目录是仓库根时，`python -m pytest -q` 会收集 `practice/*/tests/test_lab.py`，本机 collect 得到 9 个 `import file mismatch` ERROR，**不会**按 MiniShop 方式跑；（3）没有 `cd project/minishop`、不用 `run.py test`、不安装 `requirements.txt` 里的 pytest-html；（4）`127.0.0.1:PORT` 在 GitHub-hosted runner 上没有监听进程。
为什么有问题：【Job Reality Gap】 intern 第一份 CI 往往是抄 YAML。标签挡住了「已经配置」的假话，挡不住「这就是 MiniShop 的正确流水线」的误解。
依据：本机确认 `.github` 不存在；`conftest.py` L17–31；仓库根 `pytest --collect-only -q` 9 errors；`run.py` L61–81 才是项目真实入口。
建议修改：保留「示例结构」标题；YAML 改成 `working-directory: project/minishop` + `pip install -r requirements.txt` + `python -m pytest -q`，删掉虚构 TEACH_*，或加注释「MiniShop 测试自起服务，不需要 BASE_URL；下列 env 只演示密钥写法」。
推荐替换文本：

```yaml
# 示例结构，本仓库没有 .github/workflows。不要提交真实密码。
# 若将来真要跑 MiniShop：在 project/minishop 下 pytest；conftest 会自己起服务。
name: minishop-api-tests
on: [push, pull_request]
jobs:
  pytest:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: project/minishop
    steps:
      - uses: actions/checkout@v4   # 版本以官方文档为准
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m pip install -r requirements.txt
      - run: python -m pytest -q
```

（仍必须保留「不是本仓库正在跑的流水线」。）

## ISSUE
ID：CH17-0006
文件：`chapters/17-automation-overview.md`；对照 `chapters/16a-pytest-basics.md` L258–268、`project/minishop/run.py` L75
章节：第 17 章
小节：17.4 官方安装形态；17.6 审查安装段
精确位置：L139 `pip install pytest-playwright` 再 `playwright install`；L209–214 审查 venv 命令
原文：审查在独立 venv 中安装 pytest-html 4.2.0，对一条本地断言执行：`python3 -m pip install pytest-html` / `python3 -m pytest -q --html=report.html --self-contained-html`
问题等级：P2
问题类别：PED / SEQ
问题说明：了解章出现可复制的 pip/pytest 命令，且 17.6 表「初级怎么用」写「会生成、会打开、会对照失败断言」。第 16 章已经展示 pytest-html 截图；`run.py test` 已生成 `evidence/pytest-report.html`；`requirements.txt` 钉死 `pytest-html==4.2.0`。
为什么有问题：勤快读者会当必做实验，重复安装、在错误目录跑 pytest。本机复核：该命令对单测生成约 32KB 自包含 HTML，**命令本身正确**，问题是语气不像「读者不必执行」。
依据：Playwright Python intro 确是 `pip install pytest-playwright` + `playwright install`（2026-09 文档仍如此）；pytest-html 官方 user guide 确有 `--self-contained-html`；问题在教学顺序与了解章定位。
建议修改：两处都加「读到这里不要执行 pip，也不要下载浏览器 / 读者不必生成 report.html」。17.6 指向 `python3 project/minishop/run.py test` 已经写过的 HTML。
推荐替换文本：`下面命令是审查核验过的写法，读者不必安装、不必生成 report.html。选项名以插件文档为准。想看 HTML，用第 16 章已经跑过的 run.py test。`

## ISSUE
ID：CH17-0007
文件：`chapters/17-automation-overview.md`；`project/minishop/automation/README.md`；`exercises/README.md`；`practice/README.md`
章节：第 17 章
小节：MiniShop 工作实战
精确位置：L283–327；章内无 📖 徽章
原文：工作实战只给产出路径 `exercises/chapter-17-minishop-automation-map.md`
问题等级：P2
问题类别：PED / JOB
问题说明：质量标准要求实操写清目标、最小命令或产出路径、验收条件、**类型（✅/📖/🚧）**。`practice/README.md` 已标 17-1 📖，「不写 Playwright 套件」；章内没有类型徽章。仓库 `project/minishop/automation/README.md` 已写明「自动化在 `../tests/`，不要把本目录理解成第二套框架」，本章不链过去。`exercises/README.md` 示例文件名没有本章。
为什么有问题：【Job Reality Gap】克隆后先看到空的 `automation/` 目录，容易以为缺 UI 套件。了解章的诚实边界写在 practice/STATUS，不写在学生正在读的章内。
依据：Quality Standard §七；`automation/README.md` 全文 8 行；`practice/STATUS.md` L38。
建议修改：章内补「类型：📖 书面」；链到 `project/minishop/automation/README.md`；`exercises/README.md` 加 `chapter-17-minishop-automation-map.md`。
推荐替换文本：`类型：📖 书面。不要安装浏览器，不要提交 YAML。仓库 automation/ 不是第二套框架，见 project/minishop/automation/README.md。`

## 6. P3

## ISSUE
ID：CH17-0008
文件：`chapters/17-automation-overview.md`
章节：第 17 章
小节：17.2 测试金字塔；错误 2；参考资料
精确位置：L83「不是 ISO 或 ISTQB 规定的 70%/20%/10%」
原文：同上
问题等级：P3
问题类别：TERM
问题说明：否定「ISTQB 强制 70/20/10」是对的。但 CTFL v4.0 **§5.1.6 Test Pyramid** 收录该模型（Cohn 2009 三层；层数和命名可以变；K1「Recall the concepts of the test pyramid」）。本章把金字塔和 ISTQB 放在对立修辞里，面试若被问「ISTQB 有没有金字塔」可能答「没有」。
为什么有问题：比例不是标准 ≠ 大纲不谈金字塔。
依据：ISTQB CTFL v4.0 目录 5.1.6；挪威语大纲译本 5.1.6 与培训幻灯「number and naming of layers may differ」；考试结构表含 FL-5.1.6。
建议修改：改成「CTFL 4.0 把金字塔当作规划模型（5.1.6），要求记住概念；**没有**把 70/20/10 写成强制比例。」
推荐替换文本：`它来自敏捷实践（常追溯到 Mike Cohn《Succeeding with Agile》）。ISTQB CTFL 4.0 §5.1.6 收录该模型，用于讨论粒度和自动化投入，不是 ISO 数值标准。面试说「下面多、上面少」，不要背 70/20/10。`

## ISSUE
ID：CH17-0009
文件：`chapters/17-automation-overview.md`
章节：第 17 章
小节：练习 4 答案；对照面试「8 组 parametrize」
精确位置：L468 答案 4「较高：每次构建跑数量四态」；L382「pytest 接口跑 8 组 parametrize」
原文：答案写「数量四态」；面试写 8 组
问题等级：P3
问题类别：ANS
问题说明：仓库 `test_cart_qty_cases` 是 8 组：ok / eq_stock / over_stock / missing / null / empty_str / wrong_type / zero。第 13 章「四态」通常指缺字段 / null / 空串 / 错误类型。答案用「四态」会和学生刚背的 8 组对不上。
为什么有问题：不是答错，是口径漂移。
依据：`tests/test_api.py` L71–84。
建议修改：答案改为「每次构建跑数量边界 + 四态（仓库里是 8 组 parametrize）」。
推荐替换文本：`较高：每次构建跑 qty=10/11 和缺字段/null/空串/错误类型。较低：活动页文案是否温馨。`

## ISSUE
ID：CH17-0010
文件：`chapters/17-automation-overview.md`
章节：第 17 章
小节：17.4 表「与 pytest」；17.7 CD 定义
精确位置：L137「可与 pytest 一起用，需自己组织 fixture」；L228「持续交付 / 持续部署（CD）」
原文：同上
问题等级：P3
问题类别：TERM / JOB
问题说明：（1）pytest-dev/pytest-selenium 插件存在；Selenium 官方 Python 示例也给了 `driver` fixture。说「需自己组织」对初级可以，但不是「没有插件」。（2）持续交付（随时可发布、常有人工闸门）与持续部署（自动上生产）被写成一个词。后文「先能分清自动跑测试和自动上线」部分补救。
为什么有问题：面试追问 CD 两个词时可能糊在一起。
依据：https://github.com/pytest-dev/pytest-selenium ；Humble/Farley 对 CD 的区分；Selenium 文档 Waiting Strategies。
建议修改：表内改为「可与 pytest 一起用；社区有 pytest-selenium，很多团队仍自己写 fixture」。CD 拆成两句。
推荐替换文本：`**持续交付**：流水线一直产出可发布版本，上生产常有人工确认。**持续部署**：通过闸门后自动上生产。初级先分清「自动跑测试（CI）」和「自动上线」。`

## ISSUE
ID：CH17-0011
文件：`chapters/17-automation-overview.md`；`chapters/assets/diagrams/ch17-pyramid.html` / `.png`
章节：第 17 章
小节：场景导入 mermaid；17.2 图
精确位置：L44–50 mermaid；L78 PNG
原文：两处都是单元→接口→UI「下面多上面少」
问题等级：P3
问题类别：IMG / PED
问题说明：开篇 mermaid 与金字塔 PNG 同构，都没有画出场景里的「接口绿、按钮坏」。教学缺口在双门失败和 ROI 分流，不在再画一座塔。
为什么有问题：图没有讲开篇那个难点。
依据：教学尺「图讲难点」；PNG/HTML 文字本身正确（见 §9）。
建议修改：保留金字塔 PNG；场景处换成「接口门绿 / 页面门红」图，或 mermaid 改成双门而不是第三座塔。
推荐替换文本：不强制新图文件名；若增补，命题应是「接口全绿不能证明登录按钮能点」。

## ISSUE
ID：CH17-0012
文件：`chapters/17-automation-overview.md`；`exercises/README.md`
章节：第 17 章
小节：17.6 终端报告；工作实战路径
精确位置：L201「`.` 通过、`F` 失败」；L287–288 产出文件名
原文：终端只介绍 `.` / `F`
问题等级：P3
问题类别：PRE / PED
问题说明：MiniShop 基线是 37 passed, 1 xfailed，终端会出现 `x`。第 16 章已经见过 xfail。17.6 只写 `.`/`F`，不看终端的同事那一段没问题，自己对照 MiniShop 输出时会多一个符号。`exercises/README.md` 示例文件名未列 `chapter-17-minishop-automation-map.md`。
为什么有问题：小一致性，不教错。
依据：本机 `python3 -m pytest -q` → `37 passed, 1 xfailed`；`evidence/pytest-output.txt` 含黄色 `x`。
建议修改：补一句「x 是预期失败（第 16 章的 xfail）」；exercises README 加本章文件名。
推荐替换文本：`pytest 默认把结果打在终端：. 通过、F 失败、x 预期失败（MiniShop 的 BUG-001）。`

## ISSUE
ID：CH17-0013
文件：`chapters/17-automation-overview.md`
章节：第 17 章
小节：17.7 YAML
精确位置：L242–243 `actions/checkout@v4`、`actions/setup-python@v5`
原文：同上
问题等级：P3
问题类别：CODE
问题说明：正文已写「版本钉死以各平台官方文档为准」，方向对。审计日 2026-09-10，`actions/checkout` 最新主版本为 **v7**（v5 Node 24，v6 凭证隔离，v7 默认拒绝危险的 fork checkout）。`@v4` 仍能跑（安全修复已向后移植到浮动主版本标签），但示例不再是「当前默认抄法」。
为什么有问题：了解章不必追最新 patch；若读者 2026 年照抄 v4，只是偏旧不是错。
依据：https://github.com/actions/checkout README「Checkout v7」；changelog 2026-06 安全默认值。
建议修改：示例改 `@v4` 为「以文档为准，审计时常见为 checkout@v4 或更新主版本」，或直接 `@v7` 并保留「会变」。
推荐替换文本：`- uses: actions/checkout@v4  # 主版本会变，复制前看官方 README`

## ISSUE
ID：CH17-0014
文件：`chapters/17-automation-overview.md`
章节：第 17 章
小节：参考资料
精确位置：L513 `ISTQB CTFL：测试级别与测试类型（与金字塔策略模型区分）` 无链接
原文：同上
问题等级：P3
问题类别：LINK
问题说明：其余工具均有官方 URL 且 2026-09 仍可检索到。ISTQB 条没有大纲 PDF / glossary 链接，也没写 4.0 §5.1.6。
为什么有问题：想核验的学生找不到入口。
依据：https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/
建议修改：补 CTFL v4.0 大纲下载链，并写「5.1.6 Test Pyramid；2.x 测试级别」。
推荐替换文本：`- [ISTQB CTFL v4.0 大纲](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)（测试级别 ≠ 金字塔比例）`

## 7. 逐段问题

下列每个 H2/H3 均已读。只列「有问题」或「通过要点」；无问题不虚构。

| 位置 | 判定 | 说明 |
| --- | --- | --- |
| 章标题 + 一句话核心 L1–6 | 通过 | 「越靠近 UI 的观察越贵」能当过滤器，否掉 ROI 永远最高 / 每个按钮都录。主案例写个人实践项目。星级见 CH17-0001。 |
| 开篇警告 L10–14 | 通过 | 地图不是第二套框架；ROI 不绝对化；示例结构 ≠ 已上线 UI/流水线；订单状态不冻结；安装向导会变。这是本章最重要的诚实句，成立。 |
| 学习目标 L16–27 | 通过带 P2 | 8 条覆盖大纲第 17 章范围。对了解章一次列出偏多（CH17-0001）。 |
| 前置知识 L29–34 | 通过 | 第 16 章 pytest、第 3 章「自动化是执行方式」、第 8/13 章页面与接口互补，均与他章一致（第 3 章 L214 原文确认）。不要求先会 Playwright/Jenkins/Allure，正确。 |
| 场景导入 L36–52 | CH17-0003、CH17-0011 | 教学规则库存 10 与 v1.0 一致。mermaid 方向 BT 正确。假想 UI 故障未标明。 |
| 17.1 测试分层 L56–72 | 通过 | 级别 vs 分层拆得开，与 ISTQB 测试级别（组件/集成/系统/验收）不混成互斥。所有者列是「常见」不是全球制度。生活类比清楚。`qty_allowed(11,10)` 为假已复跑。 |
| 17.2 金字塔 L76–93 | CH17-0008、IMG-CH17-001 | 启发式、非 70/20/10、冰淇淋倒置、蜂巢/奖杯 ⭐ 了解——蜂巢（Spotify 微服务）、奖杯（Kent C. Dodds）外部核验属实。对初级含义三条正确：pytest 在中部；不要每个按钮；要会读哪一层红了。 |
| 17.3 接口 ROI L97–123 | 通过 | **质量标准禁止项「接口自动化 ROI 永远最高」被正面拆掉**。优势绑定契约/环境/断言；反例含按钮、文案、布局、契约未定。对照表四行合理。Cookie/Session/Token 不是三选一，正确。 |
| 17.4 Playwright/Selenium L127–170 | CH17-0004、CH17-0006、CH17-0010 | 表：Chromium/Firefox/WebKit、auto-wait、W3C WebDriver、存量 Selenium、pytest-playwright 官方插件——与 2026-09 官方文档一致。未宣布谁淘汰谁。Python 示例 `goto /`、按钮「登录」、`#login-btn` 与 `index.html` 一致。均标「示例结构」。禁止三项（淘汰/录制=会/UI 取代接口）正确。Cypress 不展开合理。 |
| 17.5 UI 成本 L174–195 | 通过 + IMG-CH17-002 | 定位/等待/flaky/覆盖冲动四条是岗位常识。`sleep(3)` 反模式与 Playwright「不要 time.sleep」文档一致。验证码/支付页 MiniShop v1.0 不做，作为一般 UI 成本举例可接受。页面对象标 ⭐⭐ 对了解章略高，并入 CH17-0001。 |
| 17.6 报告 L199–220 | CH17-0006、CH17-0012 | 终端 / pytest-html / Allure 分工正确。Allure「结果目录 + 命令行生成网站」与 allurereport.org pytest 文档一致（`--alluredir` 然后 `allure generate`/`serve`）。「报告只反映跑过的断言」正确。 |
| 17.7 CI/CD L224–262 | CH17-0005、CH17-0010、CH17-0013 | CI 定义正确。密钥不进明文、不扫生产、绿≠出口标准、Newman 与 pytest 并列、CI pytest ≠ 第 18 章负载——全部正确。YAML **没有**写成已配置。 |
| 17.8 初级边界 L266–279 | 通过 | 与大纲二三梯队一致。禁止简历「已测通全部订单状态 / 已上 CI 生产」卡住冻结点。第 1 章岗位图引用合理。 |
| 工作实战 L283–327 | CH17-0002、CH17-0007 | 产出路径、声明、完成标准有。类型徽章、四列/模板、单元第二条范例不足。禁止扫未授权站点、禁止编造 GitHub Actions 日跑生产——正确。 |
| 错误 1–10 L331–370 | 通过 | 10 条都打在真错误上，尤其 1（ROI）、2（假比例）、8（认证≠金字塔）、9（简历）、10（地图≠平台）。 |
| 面试 L375–407 | 通过 + CH17-0009 口径 | 五段结构。8 组 parametrize 与仓库一致（旧审「六种输入」**已修**）。禁止 ROI 永远最高再次出现。 |
| 小练习 + 答案 L411–469 | 见 §11 | 先独立作答，与答案一致；练习 4 口径见 CH17-0009。 |
| 检查清单 + 门槛 L473–491 | CH17-0001 | 清单可验证。9/10 对了解章过重。 |
| 总结 L493–503 | CH17-0001 | 七件事内容对，「真正掌握」语气过重。 |
| 可运行性说明 L505–509 | 通过 | pytest-html 4.2.0 本机复现成功；Playwright/Selenium/GHA 标明未装驱动、未对公网点、仓库未配流水线。与事实一致。 |
| 参考资料 L511–522 | CH17-0008、CH17-0014 | 外链 6 条在 2026-09 检索仍存在（Playwright actionability、Selenium、pytest-html RTD、Allure、GitHub Actions、Playwright Python）。仓内 03 / 16 / 质量标准路径正确。 |
| 下一章预告 L524–526 | 通过（本章侧） | 预告第 18 章，且写明 CI 功能回归不是性能测试。邻章 18 开篇仍写「第 17 章的 CI 能证明这次提交后功能脚本绿了」——**不审第 18 章正文**，记为邻章口径风险：会抵消本章三次「YAML 不是流水线」。 |
| `automation/README.md` | 通过，未在章内引用 | 「不要把本目录理解成第二套框架」正确，指向 `../tests/` + `run.py test`。 |
| 阶段测验 6 Q1 | 通过 | 见 §11。 |

禁止的错误绝对化检查（质量标准 §四）：

| 禁止项 | 本章 |
| --- | --- |
| GET 不安全、POST 安全 | 未出现 |
| Cookie/Session/Token 三选一 | 明确反对（L123、错误 8、练习 9D） |
| P0/P1/P2/P3 全球统一 | 未出现 |
| 没发现 Bug = 没 Bug | CI 绿≠库对/页面对（L220、L260） |
| 测试必须等开发全部完成 | 未出现 |
| 接口自动化 ROI 永远最高 | 作为错误 1 / 练习 9A 打击 |

MiniShop 口径：第 19 章前路径已用 `/api/cart/items` 和 `/`，文末声明「教学路径、端口和选择器非正式契约」。库存 10 / qty=11→400 已是 v1.0 行为。无订单状态名、无验证码作业、无支付。个人实践项目多次声明。

## 8. 代码问题

### 8.1 Playwright 示例（L143–147）

```python
# 示例结构。把 PORT 换成授权的 MiniShop 教学前端；不要对公网随意扫描。
def test_login_button(page):
    page.goto("http://127.0.0.1:PORT/")  # MiniShop v1.0 登录页是 `/`，没有 `/login` 路由
    page.get_by_role("button", name="登录").click()
```

| 检查 | 结果 |
| --- | --- |
| `ast.parse` | 通过 |
| 伪代码标注 | 已标「示例结构」 |
| `goto /` | 与 `index.html` 一致，旧 `/login` 问题已修 |
| `get_by_role("button", name="登录")` | 与 `<button type="submit" id="login-btn">登录</button>` 可访问名一致 |
| `page` fixture | 来自 pytest-playwright，示例未写插件依赖（可接受，因不要求安装） |
| assert | 无。作为结构示意可接受 |
| 字面量 `PORT` | 故意占位；当真跑会失败 |
| 未对公网执行 | 本审计只做 AST + 选择器对照，未启动浏览器点击 |

未列为 P0/P1。表内 camelCase 才是 P1（CH17-0004）。

### 8.2 Selenium 示例（L150–162）

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_login_button_selenium():
    driver = webdriver.Chrome()
    ...
    driver.find_element(By.ID, "login-btn").click()
```

| 检查 | 结果 |
| --- | --- |
| `ast.parse` | 通过 |
| 标注 | 「示例结构」「Selenium 4 常见写法」 |
| `By.ID, "login-btn"` | 与 HTML 一致 |
| `webdriver.Chrome()` | Selenium 4.6+ Selenium Manager 可自动驱；本机 **未装 selenium**，未跑浏览器 |
| `try/finally quit` | 好习惯 |
| 显式等待 | 表强调显式等待，示例没有等待——本地静态页可跑，与表不完全同构 |
| 本环境 | `import selenium` missing，符合章内「审查未安装浏览器驱动」 |

### 8.3 pytest-html 命令（L211–214）

本机执行（独立临时目录一条 `assert 1+1==2`）：

- pytest 9.1.1，pytest-html **4.2.0**（与钉死版本一致）
- `--html` 与 `--self-contained-html` 均在 `pytest --help` 中
- 生成 `report.html` **32119 字节**，含内联 `<style>`，与旧审查「约 32KB」同量级
- 命令**可运行**；问题是教学语气（CH17-0006）

MiniShop `run.py test` 也会写 `evidence/pytest-report.html`（本机该文件 59877 字节）。

### 8.4 GitHub Actions YAML（L232–251）

- PyYAML `safe_load` 语法通过（YAML 1.1 会把键 `on` 读成 `True`，GitHub Actions 官方文档同样用 `on:`，不当作教材错误）
- 三次「不是本仓库流水线」与事实一致（无 `.github/`）
- 与 MiniShop 真实入口脱节 → CH17-0005
- `checkout@v4` 偏旧 → CH17-0013

### 8.5 未运行项（必须说明原因）

| 项 | 原因 |
| --- | --- |
| Playwright 点击 MiniShop | 章内不要求安装；审计只核选择器与 API 名，不把了解章变成 UI 套件 |
| Selenium 示例 | 本机无 `selenium` 包 |
| 真正的 GitHub Actions | 仓库无 workflow，且不应为审计去提交密钥/流水线 |
| Allure CLI | 章内声明不要求安装；未装 |

## 9. 图片问题

### IMG-CH17-001
文件：`chapters/assets/diagrams/ch17-pyramid.png`（源 `ch17-pyramid.html`）
出现位置：17.2 L78，alt「金字塔：下面多、上面少」
图片主要内容：三层梯形。上：UI 少量 / 登录按钮冒烟（红）；中：接口居中 / 登录、qty 规则、401/403（黄）；下：单元最多 / `qty_allowed(11,10) 为假`（绿）。标题「下面多、跑得快；上面少、专门看用户关键路径」。副文否定 70/20/10 与倒置甜筒。脚注：规则优先放接口；ROI 必须带场景。
技术准确性：`qty_allowed(11,10)` 本机为 False。三层顺序与正文一致。不是 ISTQB 强制比例，正确。
与正文一致性：与 17.1 表、17.2 文一致。alt 比图题少「跑得快」四字，不影响。
文字是否正确：中文无错别字；`qty_allowed(11,10)` 无空格与代码 `qty_allowed(11, 10)` 微差，可忽略。
UI 是否过时：示意图，无工具 UI。
教学价值：能当一句教学。与开篇 mermaid 略重复（CH17-0011）。
可读性：1320×780 截图内容靠上，下方大片留白（全套 diagrams 同一窗口尺寸），文字仍清晰。
是否需要修改：可选。不必为留白单独重画。
修改建议：若只改一处，把场景 mermaid 改成双门，金字塔 PNG 保留。
最终结论：**KEEP**

### IMG-CH17-002
文件：`chapters/assets/diagrams/ch17-ui-cost.png`（源 `ch17-ui-cost.html`）
出现位置：17.5 L176，alt「店门一改装修，UI 脚本就要跟着改」
图片主要内容：左卡「接口脚本 / 对着窗口下单」——JSON 稳定时改按钮文案不红；右卡「UI 脚本 / 假装顾客进店」——选择器、等待、弹窗、浏览器差异；`time.sleep` 当默认等待更脆。脚注：录制一遍不等于会 Playwright。
技术准确性：正确。与 17.5 四条成本、错误 4/5 一致。
与正文一致性：alt 用「UI 脚本」，图题用「假顾客脚本」，同义。
文字是否正确：正确。
UI 是否过时：无。
教学价值：把「贵」说成装修，比空讲 flaky 更适合零基础。
可读性：两列卡片清楚；同样有底部留白。
是否需要修改：否。
修改建议：无强制。
最终结论：**KEEP**

HTML 与 PNG 文案一致（已对照源文件）。两图均未出现 `/login`、未写 ROI 永远最高、未画 Cookie 三层。

## 10. 表格问题

| 表 | 位置 | 判定 |
| --- | --- | --- |
| 17.1 分层 | L62–66 | 通过。单元/接口/UI 与 MiniShop 例子匹配。 |
| 17.3 ROI 对照 | L116–121 | 通过。qty=11 放接口；按钮放 UI/手工；提示语放手工。 |
| 17.4 工具对照 | L131–137 | **P1** CH17-0004 定位 API 名；其余行通过。 |
| 17.6 报告 | L203–207 | 通过。Allure「初级：打开已生成报告」符合了解定位；「会生成」略冲，并入 CH17-0006。 |
| 17.8 边界 | L270–275 | 通过。直接可当简历负面清单。 |
| 工作实战模板表 | L308–309 | **P2** CH17-0002：只有表头，与「四列各两条」不一致。 |

无把 Cookie 画进金字塔的表。无 P0/P1/P2 全球统一表。

## 11. 练习与答案问题

### 11.1 章内练习 1–10：独立作答 → 再对教材

**练习 1**  
独立：自动化是执行方式，系统测试是级别，不同维度可组合。分层后：系统级可手工也可自动，自动还可打在接口或 UI。  
教材：同义。  
结论：一致。

**练习 2**  
独立：单元只证明纯函数拒 11；接口证明 HTTP 400 且库不写成 11；UI 证明页面提示/是否发请求。单层看不到另外两层。  
教材：同义。  
结论：一致。本机 `qty_allowed(11,10) is False` 支撑单元句。

**练习 3**  
独立：流水线慢；UI 小改大面积红；难以每次提交跑完。  
教材：流水线过慢；页面小改就大面积失败。回归无法每次提交都跑完。  
结论：一致。

**练习 4**  
独立：高 ROI = 每次构建跑 qty 边界与 Body 形状；低 ROI = 文案语气、验证码好不好认。禁止「永远最高」。  
教材：较高「数量四态」；较低「活动页文案/验证码」。  
结论：方向一致；「四态」与仓库 8 组不完全同口径 → CH17-0009，**不是** 【ANSWER VERIFICATION FAILED】。

**练习 5**  
独立：auto-wait 减少「还不能点就去点」；消灭不了数据冲突、验证码、环境抖动、错误定位。  
教材：同义。  
依据：Playwright Python actionability（click 前 Visible/Stable/Receives Events/Enabled）。  
结论：一致。

**练习 6**  
独立：绝对 XPath 随 DOM 变；失败像产品缺陷。应优先 role/label/testid。  
教材：同义。  
结论：一致。

**练习 7**  
独立：缺可转发的失败现场；pytest-html 补可读报告，不是新测试级别。  
教材：同义。  
结论：一致。

**练习 8**  
独立：先当环境问题（服务没起来）。日志留失败测试名、连接错误、base URL，无密码。  
教材：同义。  
结论：一致。与 YAML 里 `TEACH_BASE_URL` 示例呼应。

**练习 9**  
独立：C。A 绝对化 ROI；B 假比例；D 认证层次误当金字塔。  
教材：C。  
结论：一致。C 与第 3 章 L214 一致。

**练习 10**  
独立：应能：维护 pytest 接口测试、说明分层与金字塔、读报告/CI 失败。不必假装：从零搭 UI 框架、独立负责公司 CI 生产。无订单状态名。  
教材：同义，「合理等价即可」。  
结论：一致。

**无 【ANSWER VERIFICATION FAILED】**。

### 11.2 阶段测验 6 第 17 章题（先独立作答）

覆盖 17/18/19；本 Agent **只答第 17 章题**。明确属于第 17 章的是 **第 1 题**。

**Q1. 测试金字塔想表达什么？接口层 ROI 高是否等于可以取消 Web 冒烟？**  
独立答案：金字塔表达自动化应「下面多、上面少」——底层更快更稳，上层更贵更脆。接口层往往 ROI 高，**不等于**取消 Web 冒烟；按钮未绑定、文案、布局接口看不见。ROI 必须带场景。  
教材答案：下层更快更稳，上层更贵。ROI 必须带场景，不能取消 Web 冒烟。  
结论：一致。无 【ANSWER VERIFICATION FAILED】。

Q2–10 指向性能、pytest 基线数字、订单 `status`、个人实践等，属第 18/19 章范围，按指令不审他章正文。

阶段测验对第 17 章只压金字塔/ROI 一条，分层/Playwright/初级边界靠章内练习覆盖——作为阶段卷可以接受，不单列 ISSUE。

### 11.3 工作实战

无标准答案（读者地图）。完成标准可判定。缺陷见 CH17-0002 / CH17-0007。

## 12. 初学者理解障碍

标记 【Beginner Friction】：

1. 了解章 ⭐⭐⭐ + 「真正掌握」+ 9/10（CH17-0001）。
2. 开篇真实 pytest 绿 + 虚构按钮坏，打开 MiniShop 对不上（CH17-0003）。
3. 「四列各两条」与模板「层」+ 单元只有一例（CH17-0002）。
4. `getByRole` 表 vs `get_by_role` 代码（CH17-0004）——抄表即报错。
5. 17.4/17.6 的 pip 命令没有「不要执行」（CH17-0006）。
6. 空目录 `automation/` 不像「只有 README 指向 tests/」（CH17-0007）。
7. YAML 看起来像能粘贴上 GitHub 的成品（CH17-0005），尽管注释说不是。
8. 学习目标 8 条在前 30 行同时出现（教学尺失败模式：前 50 行倒术语）。内容都有类比，未到 P1。

场景和生活类比（零件/出货口/假顾客、店门装修）是本章对零基础最有效的部分，应保留。

## 13. 岗位能力缺口

标记 【Job Reality Gap】：

1. 初级入职几乎都会碰到「接口绿、页面挂」和「CI 红了先看环境」——17.3 / 17.7 / 错误 6 已经教到，这是本章岗位价值。
2. 真实 CI 是 `working-directory` + `requirements.txt` + 自起服务或显式 start，不是虚构 `TEACH_BASE_URL` 指向 runner 的 localhost（CH17-0005）。
3. Playwright Python 名与 JS 文档名不一致，是新人第一周真实坑（CH17-0004）。
4. 简历口径 17.8 写得好，可直接用。
5. 缺「看一眼仓库 `automation/` 和 `tests/` 再决定有没有 UI 套件」这一职业动作（CH17-0007）。
6. 邻章风险（不审 18 正文）：第 18 章开篇「第 17 章的 CI 能证明提交后功能脚本绿了」会让学生以为第 17 章已经有绿的流水线。本章三次声明会被下一章第一句冲掉。建议由全局一致性 Agent 改第 18 章，不在此对 18 开 ISSUE。

初级工程师能力边界本身 **不是缺口**，是本章完成了大纲要求。

## 14. 建议删除内容

- 不要删金字塔、ROI 反例、初级边界表、错误 1–10。
- 可删或改写：场景导入 mermaid（与 PNG 重复）；17.4 里可执行味道的 `pip install pytest-playwright` 细节（改成「需要时查官方文档」）。
- 不要为「完整」再堆 Cypress/Grid/自愈/AI 录制——章内点到为止是对的。

## 15. 建议新增内容

1. 场景后一句：pytest 没写错；假想按钮故障；本章不交 UI 套件。
2. 工作实战一行填好的四层示例 + 📖 徽章 + 链到 `automation/README.md`。
3. 对照表 Python snake_case 注记。
4. YAML 与 MiniShop 真实目录对齐的注释。
5. （可选）「接口门 / 页面门」图，命题：接口全绿不能证明登录按钮能点。
6. ISTQB 5.1.6 一句：收录模型、不强制比例。

## 16. 建议重写内容

需要**局部重写**，不是整章推倒：

1. 章头星级 + 总结「真正掌握」+ 自测 9/10 → 了解章口径。
2. 工作实战必做 1 与模板表。
3. 17.4 定位行。
4. 17.7 YAML 步骤，使其不像「能跑却用了仓库不存在的环境变量」的成品。

不需要重写：17.1–17.3 主线、错误清单、面试五段、可运行性说明。

## 17. 本章结论

**C 明显需要修改**

理由：技术主线（分层、金字塔启发式、ROI 带场景、不宣布工具淘汰、YAML 非已配置、初级边界、`goto /`）成立，**没有 P0**，可以在当前骨架上改。但有 1 个 P1（Python 不存在的 Playwright API 名）和 6 个 P2（了解章门槛、作业表、场景真假混写、YAML 与仓库脱节、命令像必做、实操类型/空目录），分布在章头、场景、17.4、17.6、17.7、工作实战，不是改一两个错字。

不选 B：P2 数量和「抄表即报错」已经超出小修。  
不选 D/E：不必重写分层地图，更不必改成第二套 Playwright 课。

发布建议：修正 CH17-0004 与 CH17-0001/0002/0005 后再进入「可发布」讨论。了解章目标不是 95 分核心章，但 80 分 + C 意味着 **未到质量标准 90 分发布线**。

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `reviews/_full-audit-2026-09-10/MASTER_AUDIT.md`
- `reviews/_full-audit-2026-09-10/AUDIT_PROGRESS.md`
- `README.md`、`docs/COURSE_CONTROL.md`、`docs/COURSE_OUTLINE_v1.2.md`、`docs/LEARNING.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`、`practice/STATUS.md`、`exercises/README.md`
- `chapters/17-automation-overview.md`（全文）
- `project/minishop/automation/README.md`
- `chapters/quizzes/stage-6-project.md`（第 17 章题独立作答后对答案）
- `chapters/quizzes/README.md`
- `reviews/chapter-17-review.md`（仅线索，未照抄分数）
- `reviews/_pedagogy-2026-09-10/ch17.md`、`RUBRIC.md`（线索）
- `reviews/_rereview-2026-09-09/stage-6-ch17-19.md`（线索；其中「六种输入」「STATUS 把 17-1 写成 Playwright Incomplete」——现行 STATUS 已改，面试已是 8 组）
- `reviews/v1.2.1-rescore.md`、`reviews/full-course-audit-v1.2.md` 相关段（线索）
- `chapters/assets/diagrams/ch17-pyramid.png` + `.html`
- `chapters/assets/diagrams/ch17-ui-cost.png` + `.html`
- `chapters/assets/diagrams/README.md`
- MiniShop 抽查（不为审 19，只核本章例子）：`frontend/index.html`、`frontend/app.js`、`server.py` `qty_allowed`/`valid_phone`、`tests/conftest.py`、`tests/test_api.py` parametrize、`tests/test_qty_rule.py`、`requirements.txt`、`pytest.ini`、`run.py`（pytest-html 与 Playwright 取证）、`README.md`、`evidence/pytest-output.txt`
- 第 3 章自动化段落（核前置句，不审第 3 章）
- 第 16 章索引与 16a pytest-html 截图句（核顺序冲突，不审第 16 章）
- 第 16b 下一章预告仅确认存在「第 17 章」一句（不审 16b）

未读、未审：第 18 章正文除检索到的开篇一句邻章风险外。

### 实际跑过的命令与结果摘要

| 命令 / 动作 | 结果 |
| --- | --- |
| `ast.parse` 两段 Python | 均 OK |
| PyYAML `safe_load` YAML | OK |
| `qty_allowed(11,10)` / `(10,10)` | False / True |
| `Page.get_by_role` / `getByRole` | True / **False** |
| `python3 -m pytest -q` in `project/minishop` | **37 passed, 1 xfailed**（BUG-001） |
| 临时目录 `pytest -q --html=report.html --self-contained-html` | 1 passed；报告 32119 字节，内联 CSS |
| `pytest --help` 过滤 html | `--html`、`--self-contained-html` 存在；pytest-html 4.2.0 |
| 仓库根 `pytest --collect-only -q` | 9 个 `test_lab.py` import mismatch ERROR |
| `ls .github` | **不存在** |
| `index.html` 选择器 | `#login-btn`、按钮文案「登录」、登录页即 `/` |
| selenium import | missing（未跑浏览器） |
| Playwright 点击 | 未执行（了解章 + 不把审计变成 UI 套件） |

### 外部核查过的条目

| 条目 | 来源 | 结论 |
| --- | --- | --- |
| Playwright auto-wait / actionability | playwright.dev/python/docs/actionability（检索 2026-08/09 页） | click 前 Visible/Stable/Receives Events/Enabled；不能消灭一切 flaky |
| Playwright Python 安装 | playwright.dev/python/docs/intro | `pip install pytest-playwright` + `playwright install` 仍是推荐路径 |
| Playwright 定位 | 官方 Writing tests；本机 Page API | Python 为 `get_by_role`，不是 `getByRole` |
| Playwright 与 time.sleep | 官方 Library known issues | 不把 sleep 当常规 |
| Selenium 4 WebDriver / Manager / 显式等待 | selenium.dev waits；PyPI selenium 4.49（2026-09-09） | 表描述正确；Manager 自 4.6 |
| pytest-selenium 插件 | github.com/pytest-dev/pytest-selenium | 存在，故「必须自己组织 fixture」过绝对 |
| pytest-html `--self-contained-html` | pytest-html user_guide.rst；本机 4.2.0 | 命令正确 |
| Allure pytest 两步 | allurereport.org/docs/pytest/ | `--alluredir` 然后 generate/serve |
| GitHub Actions checkout 版本 | github.com/actions/checkout README（Checkout v7，审计日 2026-09） | 示例 v4 能跑但不是最新主版本 |
| 测试金字塔来源 | Cohn Succeeding with Agile；ISTQB CTFL 4.0 §5.1.6 培训材料 | 启发式；ISTQB 收录模型、不规定 70/20/10 |
| 冰淇淋/蜂巢/奖杯 | Alister Scott ice-cream cone；Spotify honeycomb；Kent C. Dodds trophy | 章内 ⭐ 了解即可，名称属实 |
| 70/20/10 | 行业口诀，非 ISO/ISTQB 强制 | 章内否定正确 |

无未决事实需要 `【External Verification Required】` 的死结；ISTQB 5.1.6 英文全文 PDF 本次未能直接打开官方 S3，依据培训幻灯 + 挪威语大纲译本 + CTFL 目录/LO「Recall the concepts of the test pyramid」，足够支撑「收录模型、无 70/20/10 强制」——若要对 5.1.6 逐句引用，建议全局技术 Agent 再下一份官方 PDF。

### 旧审查如何使用

- 初审 99 / 复评 91 / 阶段复审 92：**不继承**。
- 已修复且本轮确认：`goto /` 不是 `/login`；面试 8 组 parametrize；YAML 有「不是本仓库流水线」；ROI 未绝对化；STATUS 不再把 17-1 写成缺 Playwright 回归。
- 仍成立的线索（独立复核后保留）：了解章门槛、作业四列、命令像必做、缺双门图、邻章把 CI 说满。

### Coverage 声明

第 17 章正文每一个标题、段落、定义、列表、表格、代码块、命令、练习、答案、图片、图注、链接均已检查。未检查 = 0。
