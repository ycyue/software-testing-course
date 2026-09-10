# Chapter 15 Audit

审计角色：Chapter-Audit-Agent-15  
日期：2026-09-10  
范围：第 15 章全部（索引 + 15A 语法 + 15B 文件 JSON + 实操 15-1 + 阶段测验 5 中与第 15 章相关的题 + 四张 ch15 示意图 png/html）。未审其他章正文。  
审查解释器：Python 3.14.3（与教材声明一致）

## 1. Coverage

禁止抽样。下表「未检查」必须为 0。实践代码、测验、示意图均计入本章交付物。

| 类型 | 数量 | 已检查 | 未检查 | 备注 |
| --- | ---: | ---: | ---: | --- |
| 索引页 `15-python-basics.md` | 1（14 行） | 1 | 0 | 一句话核心、分流、作业与测验入口 |
| 15A 小节（H2） | 21 | 21 | 0 | 含结构节 + 15.1–15.8 |
| 15A 子节（H3） | 23 | 23 | 0 | 含错误/面试/练习题 |
| 15B 小节（H2） | 20 | 20 | 0 | 含结构节 + 15.9–15.12 + 工作实战 |
| 15B 子节（H3） | 12 | 12 | 0 | 另含模板内 H2（环境/运行/结论/声明） |
| 正文/散文块 | 6+122+89=217 | 217 | 0 | 按空行分块；含列表与引用 |
| 表格 | 8 | 8 | 0 | 15A×4，15B×4 |
| Markdown 代码围栏 | 0+47+26=73 | 73 | 0 | 见下表分语言 |
| 其中 `python` 围栏 | 35 | 35 | 0 | 全部复制到临时目录独立执行 |
| 其中 `text` 围栏 | 31 | 31 | 0 | 对照运行输出 |
| 其中 `bash` 围栏 | 6 | 6 | 0 | 15A×1、15B×4、15-1 README×1 |
| 其中 `json` / `markdown` 围栏 | 1+1 | 2 | 0 | `cart_cases.json` 可 `json.loads`；记录模板未当代码跑 |
| 正文/表格中的 Shell 命令 | 16 | 16 | 0 | 本机执行了 version / hello / venv / pip list / 15-1 / 检查脚本；Windows `py -3` 与 Activate 未点 |
| SQL | 0 | 0 | 0 | 本章无 SQL |
| HTTP 示例 | 2 | 2 | 0 | 散文 + 实操：`GET /api/products`；LOGIN_* 是 JSON 字符串不是完整报文 |
| 测试用例（教学） | 8+若干 assert | 全部 | 0 | `cart_cases.json` 八条 + `qty_allowed` / `extract_token` / 超库存 / 订单无 status |
| Bug 示例 | 0 | 0 | 0 | 本章不讲 BUG-001 |
| 章内小练习 | 10 | 10 | 0 | 先独立作答再对答案 |
| 章内标准答案 | 10 | 10 | 0 | |
| 面试题 | 6 | 6 | 0 | 15A×3，15B×3 |
| 常见错误条目 | 9 | 9 | 0 | 15A×5，15B×4 |
| 检查清单条目 | 7 | 7 | 0 | 15A×4，15B×3 |
| 图片 PNG | 4 | 4 | 0 | 均 `read_file` 打开 |
| 示意图 HTML | 4 | 4 | 0 | 均 `read_file` 打开 |
| Markdown 图片引用 | 4 | 4 | 0 | alt 与 png/html 三方对照 |
| Markdown 链接 | 4+6+5+2=17 | 17 | 0 | 内部链接全部存在；外部 3 条用检索核对 |
| 实操 README / main.py / test_lab.py | 3 文件 | 3 | 0 | 跑 `15-1` 与 `--check` |
| 阶段测验 5 题+答案 | 10+10 | 10+10 | 0 | 先独立作答；本章专属题弱 |
| MiniShop 口径点 | 库存 10 / 三件商品 / 订单无 status / 教学 token | 全部 | 0 | 对照 PRD、`server.py`、OpenAPI |

代码围栏分文件：

| 文件 | python | text | bash | 其他 |
| --- | ---: | ---: | ---: | --- |
| `chapters/15-python-basics.md` | 0 | 0 | 0 | 0 |
| `chapters/15a-python-syntax.md` | 25 | 21 | 1 | 0 |
| `chapters/15b-python-files-json.md` | 10 | 10 | 4 | json×1，markdown×1 |
| `practice/15-json-check/README.md` | 0 | 0 | 1 | 0 |

Coverage：**100%。未检查 = 0。**

## 2. 总评分

| 项目 | 分数 |
| --- | ---: |
| 技术准确性 | 9/10 |
| 岗位实用性 | 8/10 |
| 完整性 | 8/10 |
| 初学者友好度 | 7/10 |
| 教学顺序 | 8/10 |
| 代码质量 | 9/10 |
| 实操质量 | 6/10 |
| 练习质量 | 7/10 |
| 图片质量 | 6/10 |
| **总体** | **76/100** |

扣分由 ISSUE 支撑：Python / JSON / venv 事实与官方文档和本机 3.14.3 运行高度一致（高分），但 venv 示意图与正文互殴、15A 过长过星、实操几乎不让学生写判定、阶段测验几乎不考本章陷阱。

质量标准 DoD 20 项（本章视角，不是作者自评分）：干净通过约 12 项；图表、级别、练习覆盖、MiniShop 教学字符串、零基础坡度、清单可验证为部分通过。不足 18/20 干净项。发布线 90/100 是作者目标，不是本审计下限。

## 3. P0

无。没有把学生教成错误语言事实、没有安全可利用载荷、没有把教学 JSON 写成已冻结 OpenAPI 契约（工作实战完成标准第 5 条写了非正式契约）。禁止的错误绝对化（GET/POST 安全神话、Cookie/Session/Token 三选一、P0 全球统一、没找到 Bug 就没有 Bug、测试必须等开发写完、接口自动化 ROI 永远最高）均未当作正确规则教授；练习 9 / 15A:45 还主动打假。

## 4. P1

```
## ISSUE
ID：CH15-0001
文件：chapters/assets/diagrams/ch15-venv.html ；chapters/assets/diagrams/ch15-venv.png
章节：第 15 章（下）
小节：15.9 模块、import、venv 与 pip
精确位置：HTML 第 7 行三列卡片；PNG 中间「.venv」与右侧「课程仓库」盒
原文：
  「python3 -m venv .venv 后 pip install -r requirements.txt」
  「第 19 章已备好」
  「cd project/minishop && python3 run.py setup」
问题等级：P1
问题类别：IMG / SEQ / PRE
问题说明：示意图把「本章练习目录只建 venv、看 pip list」画成了「立刻装 requirements 并进入课程仓库 setup」。
为什么有问题：15B 正文明确「本章不要安装 requests / pytest；下一章再装」「不要拿课程仓库当乱装包的实验场」。图却指向 `pip install -r` 和第 19 章的 `run.py setup`。学生按图做会提前装 pytest/requests，或把课程仓库当成安装场；按正文做则与图冲突。右侧「第 19 章」也不对：正文说的是下一章（16）再装。
依据：15b-python-files-json.md:59-81、:486、:577；Quality Standard v1.0 零基础不得把未到的工具链提前当本章步骤；Packaging User Guide：venv 隔离后按项目需要装包，但教学顺序由教材约束。
建议修改：三列改成与正文同一把尺子。
推荐替换文本：
  ① 系统 Python：不要 sudo pip，也不要 --break-system-packages
  ② 练习目录 .venv：python3 -m venv .venv 后 python3 -m pip list，本章只该看到 pip
  ③ 课程仓库：第 16 章再用 project/minishop 的 python3 run.py setup；本章不要在仓库里装包
  删掉 caption「审查未点击」（作者元信息，不是给读者的）。
```

## 5. P2

```
## ISSUE
ID：CH15-0002
文件：chapters/15a-python-syntax.md
章节：第 15 章（上）
小节：15.4 / 15.5 / 15.6 / 15.7
精确位置：H2「15.5 列表、元组、集合 ⭐⭐⭐」（约 227 行）；15.4 切片表；15.6 浅拷贝；15.7 列表推导
原文：元组、集合与列表绑在同一颗必须掌握星；切片 / split / 浅拷贝 / 推导全部塞进上册。
问题等级：P2
问题类别：PED
问题说明：上册 711 行，除列表推导标 ⭐⭐ 外几乎全 ⭐⭐⭐。本章作业真正用的是 list/dict、真值、函数、避开可变默认。
为什么有问题：零基础没有可跳路径。元组/集合的 JSON 边界（dumps 成数组、set 不能 dumps）对测试有价值，但不应与 list 同级「必须掌握」。结果是「测试用 Python」被读成 CS101 巡礼，和一句话核心打架。
依据：Quality Standard v1.0 知识层级必须诚实；COURSE_OUTLINE 第 15 章「不追求成为 Python 开发工程师」。
建议修改：列表 ⭐⭐⭐；元组/集合改为 ⭐ 可跳，各留一句 JSON 边界；切片/split 标 ⭐⭐；浅拷贝保留短例即可。
推荐替换文本：见第 16 节。
```

```
## ISSUE
ID：CH15-0003
文件：chapters/15a-python-syntax.md
章节：第 15 章（上）
小节：15.8 之后到「文件、JSON…见 15B」
精确位置：约 590 行；上册无「工作实战」也无可验收产出路径
原文：上册练习为问答题 + 选择题 + 读函数；唯一可运行文件示例是 hello_minishop.py。
问题等级：P2
问题类别：PED / EX
问题说明：拆章要求上册也有小闭环。学习目标第一条是「运行一个 .py 文件」，但没有对应的书面/文件验收（例如 qty_allowed.py 四条 assert）。
为什么有问题：学生可以只看打印、不保存文件。15B 才第一次要求自己的目录和脚本，坡度陡。
依据：Quality Standard v1.0「每章至少对应一个实操」；拆章说明「避免一次读完失去练习节奏」。
建议修改：15.8 后加 `exercises/chapter-15a-qty.md` + `qty_allowed.py`，无输出即通过。
推荐替换文本：见第 16 节。
```

```
## ISSUE
ID：CH15-0004
文件：practice/15-json-check/README.md ；chapters/15b-python-files-json.md
章节：第 15 章（下）
小节：实操 15-1；MiniShop 工作实战
精确位置：README 验收条件（约 21–24 行）；15B 338–436 行完整脚本
原文：15-1 验收是 HTTP 200、3 件商品、鼠标 stock=10；工作实战把 qty_status / extract_token 全文贴出。
问题等级：P2
问题类别：EX / JOB
问题说明：实操对齐了章句「把响应当数据读」，但学生只跑封装脚本。工作实战把四态判定抄过去就能绿。
为什么有问题：章句是「Python 是为了处理观察结果」。处理（写判定）被作者做完了。岗位上初级测试要能改一处输入看结论变红、能自己分四态，而不是会敲 `practice/run.py 15-1`。
依据：docs/LEARNING.md 三层「先做 / 再改 / 能交代」；Quality Standard「实操要能练会该章那句话」。
建议修改：README 加「改一处」；工作实战挖空 qty_status，对照实现移到答案后。
推荐替换文本：见第 16 节。
```

```
## ISSUE
ID：CH15-0005
文件：chapters/assets/diagrams/ch15-*.html（及对应 png）
章节：第 15 章上/下
小节：15.3 真值；15.6 列表字典；15.9 venv；15.12 四态
精确位置：各文件 `<p class="caption">`
原文：
  list-dict caption：「缺键不要用 get 当成和 null 同一条用例。函数默认参数不要用 []。」
  four-json caption：「用 json.loads，不要 eval。手机号、SKU、token 都是字符串。」
  truthy caption：转去讲 True==1（主命题是 if qty 吃掉 0）
问题等级：P2
问题类别：IMG / PED
问题说明：四张图的主标题/lead 对准真难点，图注却常讲另一张图的课。
为什么有问题：初学者用 caption 当「这张图要记住什么」。list-dict 图在讲结构，注脚却是 get/null 和可变默认；四态图在讲四种空，注脚却是 eval 和手机号。教学信号被拆开。
依据：Quality Standard「图表确实帮助理解」；alt 文本其实是对的，与 caption 不一致。
建议修改：caption 只复述本图标题命题。可变默认若需要图，另开一张，不要寄生在 list-dict。
推荐替换文本：见第 9 节各 IMG 记录。
```

```
## ISSUE
ID：CH15-0006
文件：chapters/15b-python-files-json.md
章节：第 15 章（下）
小节：小练习 7
精确位置：534–536 行题目；556 行答案
原文：`eval('{"qty": 1}')` 和 `json.loads('{"qty": 1}')` 哪一个是测试脚本该用的？为什么另一个不行？
问题等级：P2
问题类别：EX / PED
问题说明：该字符串对 eval 和 json.loads 都能成功返回 `{'qty': 1}`（本机已跑）。答案说 eval「不行」是因为执行代码、不按 JSON 约束，事实对；学生在 REPL 里会看到两个都能跑，从而怀疑答案。
为什么有问题：「不行」被理解成「会报错」。选了一条两边都合法的例子，把安全课变成了玄学。
依据：本机 Python 3.14.3：`eval('{"qty": 1}')` 成功；`eval('{"qty": null}')` 为 NameError；`json.loads('{"qty": null}')` 成功。
建议修改：改用含 `null` 或 `true` 的 JSON，让 eval 立刻失败。
推荐替换文本：
  `eval('{"qty": null}')` 和 `json.loads('{"qty": null}')` 哪一个是测试脚本该用的？在 REPL 里两个都试一次，解释为什么看起来「像字典」的字符串也不能 eval。
```

```
## ISSUE
ID：CH15-0007
文件：chapters/15b-python-files-json.md
章节：第 15 章（下）
小节：工作实战脚本 LOGIN_OK / LOGIN_BAD
精确位置：341–342 行
原文：
  LOGIN_OK = '{"result":"ok","token":"teach-token"}'
  LOGIN_BAD = '{"result":"error"}'
问题等级：P2
问题类别：TEST / TERM
问题说明：v1.0 登录失败体是 `{"result":"fail"}`（401），成功体还有 `role`，token 是 uuid，不是 `teach-token`。脚本自己的标签已声明非正式错误码，但这两条 JSON 看起来像登录 API 样例，未标明与冻结契约的差异。
为什么有问题：Quality Standard：第 19 章之前的路径/字段必须标明教学约定。学生可能把 `result: error` 抄进第 16/19 章断言。
依据：project/minishop/server.py `_login`：成功 `{"result":"ok","token":...,"role":...}`；失败 `self._json(401, {"result": "fail"})`。
建议修改：字段改成与 v1.0 失败体一致，或在赋值上方用注释写明「教学字符串，不是 /api/login 冻结样例」。
推荐替换文本：
  # 教学字符串，不是 MiniShop v1.0 /api/login 的冻结样例。
  # v1.0 失败是 {"result":"fail"}，成功还有 role，token 为随机值。
  LOGIN_BAD = '{"result":"fail"}'
```

```
## ISSUE
ID：CH15-0008
文件：chapters/quizzes/stage-5-api.md
章节：阶段测验 5（覆盖 13–16，含 15A/15B）
小节：题 1–10
精确位置：全文 10 题
原文：无单独的真值 / 可变默认 / json.load vs loads / eval / UTF-8 题。最接近第 15 章的是第 6 题（python3 -m pytest）和第 9 题（requirements.txt / run.py setup）。
问题等级：P2
问题类别：EX / PED
问题说明：测验 README 写明覆盖 15A/15B，但 10 题里没有一道直接考本章必须掌握的测试陷阱。
为什么有问题：学生可以完全不会 `if qty:`、可变默认、`json.loads` vs `eval`，仍靠 13/14/16 的题过线。必过题 2/5/8 也不绑定第 15 章。
依据：chapters/quizzes/README.md 阶段 5 覆盖 15A/15B；Quality Standard 练习应覆盖目标。
建议修改：把第 6 或第 9 题改成、或增补一道第 15 章必过：`if qty:` 与库存 0，或 eval vs json.loads（用 null 例）。
推荐替换文本：见第 15 节。
```

```
## ISSUE
ID：CH15-0009
文件：chapters/15b-python-files-json.md
章节：第 15 章（下）
小节：15.10 文件
精确位置：93–107 行
原文：「先准备 cart_cases.json（内容见 15.12 实战）」；运行后打印 `list 8 合法数量`
问题等级：P2
问题类别：SEQ / CODE
问题说明：可运行片段出现在给出文件内容之前。按页顺序执行会 FileNotFoundError（本机用错路径已复现该异常类型）。
为什么有问题：教材把这段标成有确定打印结果的正式代码。学生必须先跳到 15.12 复制 8 条。前向引用虽然写了「见 15.12」，仍打断「复制即跑」。
依据：Quality Standard 正式代码应上下文完整；本机无该文件时 `json.load` 抛 FileNotFoundError。
建议修改：15.10 先给 2 条最小 JSON，完整 8 条仍放 15.12；或把读取示例移到工作实战之后。
推荐替换文本：见第 16 节。
```

```
## ISSUE
ID：CH15-0010
文件：chapters/15a-python-syntax.md ；chapters/15b-python-files-json.md
章节：第 15 章上/下
小节：15.2；15.9；工作实战
精确位置：15A:56–57 与 84 行；15B:73 与 441 行
原文：Windows 查版本用 `py -3 --version`，真正跑脚本仍写 `python3 hello_minishop.py` / `python3 check_minishop_data.py`。
问题等级：P2
问题类别：PRE / PED
问题说明：python.org 安装后 Windows 常用 `py -3`，`python3` 可能不在 PATH。
为什么有问题：15.2 刚强调「确认你运行的就是 3.x」，随即给一条 Windows 上不一定存在的命令。激活脚本写了 cmd/PowerShell，运行命令没给 `py -3` 对照。
依据：15.2 表格自己把 Windows 写成 `py -3`；本审计在 macOS 上无法点击 `py -3`（见执行记录）。
建议修改：凡给出 `python3 foo.py` 的地方加一句「Windows 用 `py -3 foo.py`」。
推荐替换文本：`python3 hello_minishop.py`（Windows：`py -3 hello_minishop.py`）
```

```
## ISSUE
ID：CH15-0011
文件：chapters/15b-python-files-json.md
章节：第 15 章（下）
小节：15.9
精确位置：59–65 行 PEP 668 段落后直接 `python3 -m venv .venv`
原文：讲了发行版 Python 拒绝 pip，正确反应是建 venv。
问题等级：P2
问题类别：PRE / JOB
问题说明：Debian/Ubuntu 上常见下一脚失败是 `ensurepip is not available` / 未装 `python3-venv`，与「pip 被 PEP 668 拒绝」不是同一件事。
为什么有问题：只处理了「不要 --break-system-packages」，没处理「venv 模块本身不存在」。这是初级岗位 Linux 测试机上的高频摩擦。
依据：PEP 668 要求发行版在 python3 能用但 venv 不能用时写明如何使 venv 可用；Debian README.venv 指向 `python3-venv` / `python3-full`。本审计未在 Debian 上复现，属对照 PEP 的教学缺口而非本机失败。
建议修改：加一句：若 `python3 -m venv` 报 ensurepip/venv 模块不存在，用发行版包装 `python3-venv`（不要 sudo pip）。
推荐替换文本：若命令失败并提到 ensurepip 或 venv 模块，先装发行版包（Debian/Ubuntu 常见为 `python3-venv`），再重新创建 `.venv`。不要用 sudo pip 补救。
```

## 6. P3

```
## ISSUE
ID：CH15-0012
文件：chapters/15a-python-syntax.md
章节：第 15 章（上）
小节：15.3 `==` 和 `is`
精确位置：159 行
原文：Python 3.14 会对“用 `is` 比较 int 字面量”给出 SyntaxWarning
问题等级：P3
问题类别：ACC / TERM
问题说明：本机 3.14.3 确有 `SyntaxWarning: "is" with 'int' literal. Did you mean "=="?`。该警告自 3.8 起就有，不是 3.14 新行为。
为什么有问题：学生在 3.12（教材允许的最低版本）上也会看到警告，却可能以为「只有 3.14 才管」。结论「不要写 qty is 11」仍然正确。
依据：本机编译 `qty is 11` 的 SyntaxWarning；Python 3.8 bpo-34850。
建议修改：改为「3.8 起（含本课 3.12+）会 SyntaxWarning」。
推荐替换文本：不要写 `qty is 11`。3.8 起用 `is` 比较 int 字面量会 SyntaxWarning；即便小整数偶尔 `is` 为真，也不能当测试依据。
```

```
## ISSUE
ID：CH15-0013
文件：chapters/15a-python-syntax.md
章节：第 15 章（上）
小节：15.3 真值
精确位置：166 行
原文：当成假：None、False、0、0.0、""、[]、{}
问题等级：P3
问题类别：ACC
问题说明：官方 Truth Value Testing 还包括 ()、set()、0j 等。对测试够用，但图 ch15-truthy 的 lead 还丢掉了正文里的 0.0。
为什么有问题：不是错误，是不完整。学生遇到空元组当假时会以为教材没教过。
依据：https://docs.python.org/3/library/stdtypes.html#truth-value-testing （检索摘要，docs.python.org 直连被 SSRF 拦截）。
建议修改：加「空元组 ()、空集合 set() 也是假；本章例子用 0 / "" / [] 就够」。
推荐替换文本：在条件里，下面这些会被当成假：None、False、数字零、空字符串、空容器（""、()、[]、{}、set()）。库存为 0 的商品是合法业务数据。
```

```
## ISSUE
ID：CH15-0014
文件：chapters/15b-python-files-json.md
章节：第 15 章（下）
小节：15.10
精确位置：109–112 行表
原文：loads/dumps 的「对象」列写成「字符串」；load/dump 的对象列为「—」
问题等级：P3
问题类别：TERM
问题说明：官方区分的是「字符串 vs 文件对象」，两边都有 Python 对象。表头「对象」含糊。
为什么有问题：刚学的学生会以为 dumps 不处理 dict。正文下一句实际能补上。
依据：docs.python.org/3/library/json.html：load(fp) / loads(s)。
建议修改：列改为「Python 对象 ↔ 字符串」与「Python 对象 ↔ 文件」。
推荐替换文本：
  | 函数 | 作用 |
  | json.loads / json.dumps | 字符串 ↔ Python 对象，不直接碰磁盘 |
  | json.load / json.dump | 文件对象 ↔ Python 对象 |
```

```
## ISSUE
ID：CH15-0015
文件：chapters/15a-python-syntax.md
章节：第 15 章（上）
小节：15.3 / 15.4 / 15.5
精确位置：115、222、280、298 行
原文：在 15B 教 json 模块之前使用 json.loads / json.dumps（float 例子、路径拼接纪律、元组/集合边界）。
问题等级：P3
问题类别：SEQ
问题说明：测试上下文需要提前露脸，但上册尚未 `import json` 教学。
为什么有问题：15.5 集合例已经完整 `import json` 并跑 TypeError，等于提前上了 15B 的课。可接受，略陡。
依据：json 正式节在 15.12。
建议修改：集合/元组两段加「json 模块下册细讲，这里只看边界」。
推荐替换文本：JSON 没有元组/集合（模块用法见 15B）。这里只要记住：dumps(tuple) 变成数组；set 会 TypeError。
```

```
## ISSUE
ID：CH15-0016
文件：chapters/assets/diagrams/ch15-venv.html
章节：第 15 章（下）
小节：15.9
精确位置：HTML 第 8 行 caption
原文：「示意图：.venv 不要进 Git。Windows 激活脚本见第 15 章，审查未点击。」
问题等级：P3
问题类别：IMG / PED
问题说明：「审查未点击」是作者工作台留言，泄漏进读者图注。四张 PNG 下部大面积留白，印刷/滚动时像没画完。
为什么有问题：学生不需要知道审查有没有点 Windows。留白降低「这张图在讲什么」的密度。
依据：打开的 png 实际画面。
建议修改：caption 改为「.venv 不要进 Git。venv 不是安全沙箱。」截图时裁掉空白。
推荐替换文本：示意图：.venv 不要进 Git。venv 隔离的是包装位置，不是 HTTP 权限。
```

```
## ISSUE
ID：CH15-0017
文件：practice/15-json-check/main.py
章节：实操 15-1
小节：main()
精确位置：第 4 行 `from __future__ import annotations`；第 28 行 `parsed` 未使用
原文：`status, _h, raw, parsed = request(...)` 之后只用 raw 落盘再 loads。
问题等级：P3
问题类别：CODE
问题说明：学生按 LEARNING.md 可以不读实现。若读了：未教的 future 注解（3.14 上该 future 已属历史兼容），以及故意丢弃的 parsed，和正文「落盘再读」是一致的，但会显得脚本随便。
为什么有问题：零基础章配套代码最好不要无提示引入未教语法。`parsed` 不用是风格问题，不是功能 bug。
依据：15-1 已跑通；Python 3.14 What’s New：`from __future__ import annotations` 行为未变但属于被替代的写法。
建议修改：改成 `status, _h, raw, _parsed = ...` 或去掉解包；future 行可删（3.12+ 不需要它来跑这段）。
推荐替换文本：`status, _h, raw, _unused = request("GET", f"{shop.base_url}/api/products")`
```

```
## ISSUE
ID：CH15-0018
文件：chapters/15b-python-files-json.md
章节：第 15 章（下）
小节：15.12；面试「中文 JSON」
精确位置：302 行；520–524 行
原文：dumps 默认 ensure_ascii=True，中文写成 \uXXXX；面试以「无线鼠标」为例。没有可运行的中文 dumps 对比块。
问题等级：P3
问题类别：PED / CODE
问题说明：学习目标含 UTF-8 读写，面试题要求能讲 ensure_ascii=False，但学生没有一段「跑完就能看见 \u 与汉字」的代码。
为什么有问题：15-1 的商品名恰好是「无线鼠标」，本可当对比，正文没用。
依据：本机 `json.dumps({"name":"无线鼠标"})` 为 `"{\\"name\\": \\"\\u65e0\\u7ebf\\u9f20\\u6807\\"}"` 一类转义；`ensure_ascii=False` 保留汉字。
建议修改：15.12 数字陷阱后再加 4 行 dumps 对比。
推荐替换文本：
  print(json.dumps({"name": "无线鼠标"}))
  print(json.dumps({"name": "无线鼠标"}, ensure_ascii=False))
```

```
## ISSUE
ID：CH15-0019
文件：chapters/assets/diagrams/ch15-four-json.html
章节：第 15 章（下）
小节：15.12
精确位置：第 7 行第四张卡片 `{"qty": "1"}`
原文：错误类型示例是字符串 `"1"`；工作实战用例是 `"11"`。
问题等级：P3
问题类别：IMG
问题说明：两种都是错误类型，与 MiniShop `test_api.py` 的 `"1"` 反而更接近。和图旁正文/八条用例不完全同构。
为什么有问题：对照练习 4 的 `{"qty": 11}`（合法整数）时，学生可能把图里的第四格当成「11 的另一种写法」。
依据：15B cart_cases 第七条 qty 为 `"11"`；server.py 对非 int 返回 wrong type qty。
建议修改：第四格改成 `{"qty": "11"}`，与用例一致。
推荐替换文本：错误类型卡片：`{"qty": "11"}` 键在，值是字符串不是 int。
```

```
## ISSUE
ID：CH15-0020
文件：chapters/15b-python-files-json.md
章节：第 15 章（下）
小节：15.12 末尾到工作实战之间；工作实战之后
精确位置：305–307 行；485–486 行
原文：实操 15-1 入口和「仓库已提供 requirements.txt 与 python3 run.py setup」都是无标题段落。后者未写 `cd project/minishop`。
问题等级：P3
问题类别：PED / PRE
问题说明：15-1 是本章唯一可运行实操，却不像一个节。setup 从仓库根目录执行会找不到 `run.py`（根目录没有该文件；practice/run.py 也不接受 setup）。
为什么有问题：本章本来禁止学生现在就 setup，这条提示更容易被误跑且跑失败。
依据：仓库根无 `run.py`；`project/minishop/run.py` 才有 setup。
建议修改：加「配套实操」小标题；setup 写成 `cd project/minishop && python3 run.py setup`，并重复「本章不要执行」。
推荐替换文本：配套实操（标准库 GET，不装 requests）：`python3 practice/run.py 15-1`。课程仓库的依赖安装留到第 16 章：`cd project/minishop && python3 run.py setup`。
```

## 7. 逐段问题

### 索引 `chapters/15-python-basics.md`

| 单元 | 结论 |
| --- | --- |
| 标题 + 一句话核心 | 通过。与 15A 一致，能过滤「成为开发」。 |
| 拆章说明与两节链接 | 通过。链接存在。 |
| 作业 / HTTP 口径 / 测验入口 | 通过。写明 15A 不发 HTTP、15-1 发一次、工作实战只处理本地 JSON；测验建议学完 16。旧审查 S5-13「15A 说不发 HTTP、15-1 却发」已修。 |
| 「读完第二节后进入第 16 章」 | 通过。 |

### 15A 结构节

| 单元 | 结论 |
| --- | --- |
| 解决什么问题 / 不讲 class 装饰器继承异步 | 通过。正文无这些语法，仅在「不讲」句出现。 |
| 学习目标 | 通过。与后文函数/真值/可变默认对齐；缺上册文件产出见 CH15-0003。 |
| 前置知识 | 通过。顺序 13→14→15，能读 JSON。 |
| 场景导入 | 通过。qty=11/stock=10、四态、上半章不发 HTTP、15-1 预习口径一致。未把路径写成冻结契约。 |

### 15A 核心知识

| 单元 | 结论 |
| --- | --- |
| 15.1 为什么学 Python | 通过。生活类比、正式定义、时机、不能替代的工作、ROI 不绝对化。 |
| 15.2 安装与脚本 | 基本通过。3.12+、python3 vs py -3、缩进、注释纪律、assert 不是 pytest 专用，均对。审查输出 Python 3.14.3 本机复核。Windows 跑脚本命令见 CH15-0010。 |
| 15.3 变量与类型 | 通过。名字贴在对象上；手机号用 str；类型表与 JSON 对应正确。 |
| 15.3 == 与 is | 通过。None 用 is；不要 qty is 11。版本表述见 CH15-0012。 |
| 15.3 真值 | 通过。`if qty` 吃掉 0 的例子本机打印匹配。见 CH15-0013。 |
| True 冒充 int | 通过。`True==1` 本机 True；`type(True) is int` False；`isinstance(True, int)` True。用 `type is int` 合理，并声明不必学继承。 |
| 15.4 字符串 | 通过。len/切片/f-string 输出匹配。`"11"` 不是 11 的测试纪律正确。 |
| 15.5 列表 | 通过。输出匹配。 |
| 15.5 元组 | 通过。赋值 TypeError → `tuple_immutable`。JSON 无元组。过星见 CH15-0002。 |
| 15.5 集合 | 通过。`json.dumps(set)` TypeError。过星与提前 import json 见 CH15-0002/0015。 |
| 15.6 字典 | 通过。get 四态打印匹配；`in` 查键不查值；浅拷贝例子匹配。 |
| 15.7 条件循环推导 | 通过。超库存打印 SKU-DEMO-002。`stocks.items()` 无代码例见轻量缺口，未单开 ISSUE。 |
| 15.8 函数 / 可变默认 / assert | 通过。`bucket=[]` 第二次 `['a','b']`；`None` 修复后 `['b']`；assert 无输出；`-O` 会剥 assert 的警告正确（本机 `-O` 下 `assert False` 仍打印 survived）。 |

### 15A 收口

| 单元 | 结论 |
| --- | --- |
| 常见错误 1–5 | 通过。都是真陷阱。 |
| 面试三题 | 通过。结论→示例→边界。 |
| 小练习 1/3/4/5/6/8 | 题号跳号已说明。答案独立核对通过。练习 4 有「null 不是 Python」警告，摩擦降为 P3 未单开。 |
| 清单 / 总结 / 可运行性 / 参考 / 预告 | 通过。教程链接存在。无工作实战见 CH15-0003。 |

### 15B 结构节与 15.9–15.12

| 单元 | 结论 |
| --- | --- |
| 一句话核心 / 目标 / 前置 / 场景 | 通过。文件+JSON 当证据，与脊柱公式一致。 |
| 15.9 模块 venv pip | 正文通过：`python3 -m pip`、PEP 668、禁止 sudo pip 与随手 break-system-packages、uv/Poetry 非必修、`.venv` 不进 Git、`if __name__=="__main__"`。图见 CH15-0001。缺 python3-venv 包见 CH15-0011。本机 `python3 -m venv` 后 pip list 可见 pip 25.3。 |
| 15.10 文件 | 编码/with/"w" 截断纪律正确。读取示例顺序见 CH15-0009；对照表见 CH15-0014。提供 8 条文件后输出确为 `list 8 合法数量`。 |
| 15.11 异常 | 通过。JSONDecodeError 是 ValueError 子类（本机 MRO 验证）；缺键 KeyError；不要裸 except；非法 JSON 不要修一修当成功。 |
| 15.12 JSON 对照 | 通过。转换表与官方默认表一致；RFC 8259 vs 文档仍写 RFC 7159 的提示正确（3.14 json.html 仍写 RFC 7159）。非法 JSON 三例均 JSONDecodeError。11 vs 11.0 类型不同且 `11.0==11` 为真，均本机验证。禁止 eval 正确。中文 dumps 缺可运行对比见 CH15-0018。 |
| 实操入口段落 | 口径通过（标准库 GET、不装 requests）。结构见 CH15-0020。 |

### 15B 工作实战与收口

| 单元 | 结论 |
| --- | --- |
| cart_cases.json 8 条 | 通过。expect 是脚本标签已声明。`json.loads` 成功。与 MiniShop 数量规则（正整数且 ≤ 库存）及 server.py `qty_allowed` 同构。 |
| check_minishop_data.py | 可运行，输出 `token_ok / over SKU-DEMO-002 / cases_ok 8`。订单只断言有 id、无 status，符合 v1.0。整份可贴见 CH15-0004。LOGIN_BAD 见 CH15-0007。 |
| 完成标准 / 记录模板 | 通过。个人练习、非正式 OpenAPI、无密码入库。 |
| 常见错误 / 面试 | 通过。venv 不是沙箱、不要 eval、UTF-8。 |
| 小练习 2/7/9/10 | 2/9/10 答案正确。7 见 CH15-0006。9 打假 Cookie/Session/Token 与 True 子类，符合质量标准。 |
| 清单 / 总结 / 可运行性 / 参考 / 预告 | 通过。json 文档与 16A 链接存在。 |

### 实操 15-1

| 单元 | 结论 |
| --- | --- |
| README 目标/命令/验收 | 通过。类型 ✅ 在 practice/README.md。缺「改一处」见 CH15-0004。 |
| main.py | 标准库 urllib + 临时 MiniShop，不装 requests。落盘再 loads。本机 HTTP 200、3 件、鼠标 10、无线鼠标。 |
| tests/test_lab.py | `15-1 --check`：1 test ok。 |
| 与 PRD | SKU-DEMO-001 无线鼠标库存 10；三件商品。一致。 |

### 阶段测验 5

见第 11 节。无答案错误。覆盖缺口见 CH15-0008。

## 8. 代码问题

35 个教材 `python` 围栏全部在临时目录独立执行（工作实战脚本同时写入 `cart_cases.json`）。声称「运行后打印 / 审查结果」的块，stdout 与教材一致。两个「最简单」无 print 的片段（单元素 list、单 dict）按设计无输出。

| 文件 | 行 | 块 | 运行 | 输出 |
| --- | ---: | ---: | --- | --- |
| 15a | 77 | hello print | OK | hello, minishop（另存 /tmp/hello_minishop.py 再跑同样） |
| 15a | 103 | 变量赋值 | OK | 无输出（设计如此） |
| 15a | 120 | type 打印 | OK | `str int False None` |
| 15a | 144 | == / is | OK | True / False / True |
| 15a | 170 | if qty | OK | 被当成没有数量 |
| 15a | 194 | 字符串 | OK | 11 138 8000 True / True / f-string |
| 15a | 235 | 单元素 list | OK | 无输出 |
| 15a | 241 | 购物车 list | OK | 2 SKU-DEMO-001 11 / 3 |
| 15a | 264 | 元组不可变 | OK | tuple_immutable |
| 15a | 286 | set 去重 | OK | 3 2 True |
| 15a | 300 | set dumps | OK | set_not_json |
| 15a | 328 | 单 dict | OK | 无输出 |
| 15a | 334 | get / in | OK | 五段打印匹配 |
| 15a | 362 | 缺键/null/0 | OK | 匹配 |
| 15a | 384 | in 查键 | OK | True / False |
| 15a | 399 | 别名 vs copy | OK | 11 1 |
| 15a | 421 | if/elif | OK | exceeds_stock |
| 15a | 444 | for 超库存 | OK | SKU-DEMO-002 |
| 15a | 468 | 推导 | OK | 两个 SKU |
| 15a | 491 | add | OK | 3 |
| 15a | 507 | qty_allowed | OK | True True False False |
| 15a | 533 | 可变默认 | OK | ['a'] / ['a', 'b'] |
| 15a | 552 | None 修复 | OK | ['a'] / ['b'] |
| 15a | 575 | assert 自检 | OK | 无输出 |
| 15a | 667 | 练习 8 仅定义 | OK | 无输出 |
| 15b | 35 | json.loads token | OK | teach-token |
| 15b | 95 | json.load 文件 | OK | list 8 合法数量（提供 8 条后） |
| 15b | 116 | json.dump | OK | 无终端输出，写出文件 |
| 15b | 146 | int("x") | OK | not an int |
| 15b | 161 | parse_object | OK | 1 / None |
| 15b | 187 | KeyError | OK | missing qty |
| 15b | 229 | loads/dumps/tuple | OK | 四行匹配，含 `{"qty": null, "ok": true}` 与 `[1, 2]` |
| 15b | 258 | 非法 JSON | OK | invalid×3 |
| 15b | 286 | 11 vs 11.0 | OK | int / float |
| 15b | 338 | 完整检查脚本 | OK | token_ok / over SKU-DEMO-002 / cases_ok 8 |

额外本机核对（非教材块，用于事实核查）：

- `True == 1` True；`type(True) is int` False；`isinstance(True, int)` True
- `json.JSONDecodeError` 继承 `ValueError`
- `eval('{"qty": 1}')` 成功（支撑 CH15-0006）
- `python3 -O` 剥掉 assert
- `open` 默认编码：本机 UTF-8 mode=1（macOS）；教材强调 Windows 显式 utf-8 仍然正确（PEP 686 默认 UTF-8 针对 3.15+，当前稳定 3.14）

Practice：`python3 practice/run.py 15-1` 退出码 0；`--check` 1 passed。轻微代码气味见 CH15-0017。无装饰器、无 class、无 async。

未跑：Windows `py -3`、Activate.ps1、python.org 安装向导（教材已声明向导会变）。

## 9. 图片问题

四张图都用 `read_file` 打开了 png 与 html。png 与 html 内容一致（同源导出）。

```
IMG-CH15-001
文件：chapters/assets/diagrams/ch15-truthy.png ；ch15-truthy.html
出现位置：15a-python-syntax.md 15.3 真值（163 行）
图片主要内容：三列对照 if qty: / "qty" in item / qty == 0。标题「库存为 0 是合法生意」。
技术准确性：正确。0 在布尔上下文为假。第三列「不要用 is 比较整数」正确。
与正文一致性：主命题一致。lead 列出的假值比正文少 0.0。
文字是否正确：是。caption 转向 True==1，与主标题不完全同轴。
UI 是否过时：否（概念图）。
教学价值：高。这是测试用 Python 的核心陷阱。
可读性：标题清楚；png 下部大面积留白。
是否需要修改：轻微。
修改建议：caption 保持「库存为 0 时不要写 if qty」。lead 补 0.0 或与正文对齐。
最终结论：MODIFY
```

```
IMG-CH15-002
文件：chapters/assets/diagrams/ch15-list-dict.png ；ch15-list-dict.html
出现位置：15a-python-syntax.md 15.6（321 行）
图片主要内容：`{"items":[...]}` 示例；说明多行 list、一行 dict。
技术准确性：结构正确。SKU-DEMO-002 qty=2 stock=5 与 MiniShop 种子购物车数量一致（不是超库存例，可接受）。
与正文一致性：正文超库存例用 qty=11；图用 qty=2。都合法，未标明「这是种子购物车不是超库存例」。
文字是否正确：正文区提到「集合能去重」，对本图可选。caption 讲 get/null 和可变默认，跑题（CH15-0005）。
UI 是否过时：否。
教学价值：高。接口 JSON 的核心形状。
可读性：代码卡片清楚；下部留白。
是否需要修改：caption 必须改。
修改建议：caption 改为「多行是 list，一行是 dict；外层再用 dict 包 items。」
最终结论：MODIFY
```

```
IMG-CH15-003
文件：chapters/assets/diagrams/ch15-venv.png ；ch15-venv.html
出现位置：15b-python-files-json.md 15.9（30 行）
图片主要内容：系统 Python vs .venv vs 课程仓库三列。标题正确：「不是安全沙箱」。
技术准确性：venv 不是沙箱、不要 sudo pip，正确。中间列 pip install -r、右列第 19 章 setup，与本章步骤冲突（CH15-0001）。
与正文一致性：差。正文本章不装包、不拿仓库当安装场。
文字是否正确：标题/lead 对；盒子步骤错；caption「审查未点击」不该出现。
UI 是否过时：否。
教学价值：命题有价值，当前图会把学生带偏。
可读性：三列清楚；下部留白。
是否需要修改：必须改盒子与 caption。
修改建议：见 CH15-0001 推荐替换。
最终结论：MODIFY
```

```
IMG-CH15-004
文件：chapters/assets/diagrams/ch15-four-json.png ；ch15-four-json.html
出现位置：15b-python-files-json.md 15.12（211 行）
图片主要内容：缺字段 / null / 空串 / 错误类型四格。标题强调 get 得到 None 时还不知道是哪一种。
技术准确性：四态正确，与第 13 章及 qty_status 一致。第四格 `"1"` 与用例 `"11"` 不完全同构（CH15-0019）。
与正文一致性：主命题一致。caption 讲 eval 和手机号，跑题（CH15-0005）。
文字是否正确：卡片内正确。
UI 是否过时：否。
教学价值：高。应在 15A 练习 4 附近也出现（练习 4 就要分类，图却在 15B）。
可读性：四列清楚；下部留白。
是否需要修改：caption；第四格字符串建议改为 "11"；可在 15A 15.6 复用同一 png。
最终结论：MODIFY
```

无 DELETE。无 KEEP（四张都至少要改 caption 或盒子）。没有可变默认示意图，建议新增见第 15 节。

## 10. 表格问题

| 表 | 位置 | 结论 |
| --- | --- | --- |
| 系统常用命令 | 15A 15.2 | 通过。Windows 用 py -3 查版本正确。 |
| 内置类型 | 15A 15.3 | 通过。float/json.loads、bool/JSON true、None/null 对应正确。 |
| 字符串操作 | 15A 15.4 | 通过。f-string 3.6+ 对；本课最低 3.12。strip/split 无独立运行块，不构成错误。 |
| dict 取值 | 15A 15.6 | 通过。本机核对缺键 KeyError vs get None vs in False vs 默认值。 |
| 标准库 vs 第三方 | 15B 15.9 | 通过。 |
| loads vs load | 15B 15.10 | 基本对，表头含糊见 CH15-0014。 |
| JSON↔Python | 15B 15.12 | 通过。与官方默认转换表一致。反向 set 不能默认编码，已用代码证明。 |
| 非法 JSON | 15B 15.12 | 通过。单引号、True、末尾逗号均 JSONDecodeError。表中的 None 未放进可运行 samples，本机补跑同样 DecodeError。 |

无 P0/P1 表格错误。

## 11. 练习与答案问题

### 11.1 章内小练习（先独立作答，再对教材）

独立答案：

1. 初级自动化要处理接口 JSON/文件/可重复判定，不是交付业务系统。dict/list/JSON 是把第 13 章检查点写成步骤的最小工具箱。  
3. `qty=0` 时 `if qty:` 走假分支。应 `qty == 0` 或先检查类型再比较。  
4. `{}`：键不在，get None，缺字段。`{"qty": null}`：键在，get None，null。`{"qty": ""}`：键在，值 `""`，空串/错误类型。`{"qty": 11}`：键在，值 11，再和库存比。不能当 Python 字面量。  
5. 多行是 list，一行是 dict；外层 dict 包 `items`，与常见 JSON 对象包裹数组一致，也方便放其它字段。  
6. B。`token is None`。A/C 把「没有 token」和 0/False 搅在一起；D 用 is 比字符串。  
8. 默认 `[]` 跨调用共享；先 `"a"` 再 `"b"` 第二次为 `['a', 'b']`。改 `None`，函数内新建 list。  
2. `python3 -m pip` 对着当前解释器；加 venv 只动本项目。`sudo pip` 改系统，还可能装到没用的解释器。  
7. 该用 `json.loads`。eval 执行代码。**独立补充：** 题目里的 `'{"qty": 1}'` 对 eval 也会成功，应换 `null`/`true` 才能在 REPL 看到差异。  
9. D。A 把认证层次说成库；B 与事实相反（True 是 int 子类，isinstance 为真）；C 违反四态。  
10. 成功 `"teach-token"`；缺 token 为 `None`；qty=11 stock=10 为 `exceeds_stock`。不写订单状态名。

对照教材：1/2/3/4/5/6/8/9/10 一致。第 7 题答案事实正确，题目选例不当 → CH15-0006，**不是** 【ANSWER VERIFICATION FAILED】。

### 11.2 阶段测验 5（先独立作答）

题目与答案在同一文件。独立推理如下，再对照文末答案。

1. 接口擅长稳定契约、规则、权限；UI 擅长按钮、跳转、文案。不能互相取消：页面挂了接口仍可能绿。  
2. （必过）缺字段 / null / "" / 错误类型在 JSON 里不是同一件事，服务端常走不同分支；`get` 还会把缺字段和 null 都变成 None。  
3. 以 PRD 与 OpenAPI 为准。v1.0 登录是 `/api/login`；无前缀 `/login` 会 404。  
4. 课程口径：Environment 覆盖 Collection。  
5. （必过）token 已写入共享 Session 时，插在前面的 401 用例会带着登录态，测不到未授权。  
6. `python3 -m pytest` 用的是当前解释器（通常 venv）里的 pytest，避免 PATH 上另一个可执行文件。  
7. fixture 准备环境；parametrize 展开数据。多种 Body 用 parametrize。  
8. （必过）ROI 不是永远最高。天天改文案的全新页面更该先手工。  
9. `project/minishop/requirements.txt`；在该目录 `python3 run.py setup` 然后 `python3 run.py test`。  
10. B。`requests.post(..., json={...})` 发 JSON Body。A/C/D 分别是插件神话、GET/POST 安全神话、全绿即无缺陷神话。

对照教材答案：10/10 一致。无 【ANSWER VERIFICATION FAILED】。  
覆盖问题：第 15 章专属陷阱几乎没考 → CH15-0008。第 6、9 题跨 15/16，独立答案与教材一致。

### 11.3 工作实战与 15-1

工作实战八条 expect 本机全部命中。15-1 验收本机命中。弱在「学生不用手写」→ CH15-0004。

## 12. 初学者理解障碍

标记 【Beginner Friction】：

- 15A 711 行、几乎全 ⭐⭐⭐，零基础只能硬读完再进 15B（CH15-0002）。  
- 练习 4 虽警告 null 不是 Python，上册仍出现 JSON 形状；性急的人会贴进 REPL。  
- 15.10 先跑后给文件（CH15-0009）。  
- 练习 7 在 REPL 里「两个都能跑」（CH15-0006）。  
- Windows 查版本用 py -3、跑脚本写 python3（CH15-0010）。  
- Debian 上 venv 模块可能不存在（CH15-0011）。  
- 图 caption 与标题不是同一句话（CH15-0005）。  
- 图让装 requirements，正文禁止（CH15-0001）——这是最伤新手的互殴。  
- `__name__`、`type(x).__name__`、f-string 的 `f` 前缀解释偏短，可接受。  
- 15-1 实现里的 pathlib / 类型注解 / MiniShopLab，LEARNING.md 允许跳过，但仍会吓到点开 main.py 的人（CH15-0017）。

未发现把装饰器、继承体系、异步无提示塞进正文。`True 是 int 的子类` 有「不必学继承」护栏，通过。

## 13. 岗位能力缺口

标记 【Job Reality Gap】：

- 初级测试入职后立刻要：读 JSON、分四态、venv、不要 sudo pip、不要 eval。这些本章都教了，且用 MiniShop 数量规则，岗位方向对。  
- 缺口：几乎不要求学生自己写判定函数；15-1 是「跑通作者的脚本」。真实工作是改断言、改输入、看红绿。  
- 缺口：没有「改 stock 判定再跑必须失败」的回归动作。  
- 缺口：阶段测验不锁本章陷阱，面试前容易漏 `if qty` 和可变默认。  
- 已做对的岗位纪律：密码/完整 token 不入库；venv 不是沙箱；订单不编造 status；教学标签不等于正式错误码；显式 UTF-8；`python3 -m pip`。  
- Windows 与 Debian 环境摩擦会在真实岗位第一天出现，正文只覆盖了 macOS/Linux 主路径。

## 14. 建议删除内容

- ch15-venv 盒子里的 `pip install -r requirements.txt`、`第 19 章已备好`、`run.py setup`（或移到第 16 章图）。  
- 四张图 caption 中跑题的 eval / 可变默认 / 手机号 / 「审查未点击」。  
- 15A 若需降篇幅：元组 TypeError 与 set dumps 可收进「可跳」折叠，不必删技术事实。  
- 不要删可变默认反例、真值反例、四态、禁止 eval——那些是本章价值。

## 15. 建议新增内容

1. 15A 小闭环：`qty_allowed.py` + `exercises/chapter-15a-qty.md`。  
2. 15-1 README「改一处」：读 products.json 写三行（顶层类型、stock 是 10 还是 "10"、把判定改成 9 必须红）。  
3. 工作实战挖空 `qty_status`。  
4. 15.12 四行中文 `ensure_ascii` 对比。  
5. 可选图 `ch15-mutable-default`：共享 list vs None 修复。  
6. 阶段测验 1 道第 15 章题，例如：库存允许为 0 时为什么不能写 `if qty:`，或 eval vs json.loads（用 null）。  
7. 15.10 内联 2 条最小 `cart_cases.json`。  
8. Windows `py -3 script.py` 对照句；Debian `python3-venv` 一句。

## 16. 建议重写内容

### 15.5 标题与导语

```markdown
## 15.5 列表 ⭐⭐⭐（元组 / 集合 ⭐ 可跳）

接口里的数组进 Python 就是 list。购物车多行用列表，一行里的字段用字典。先会 len、下标、append 和 for item in items。

元组、集合不是本章作业所需。JSON 没有这两种：json.dumps((1, 2)) 会变成数组；set 不能直接 dumps。去重可以 list(set(skus))，其余可跳。
```

（保留现有列表示例；元组/集合两段可标「可跳」。）

### 15A 15.8 后小闭环

```markdown
## 上册小闭环：qty_allowed.py ⭐⭐⭐

在自己的练习目录保存该文件（不发 HTTP，不装包）。python3 qty_allowed.py 无输出即通过。
书面记录 exercises/chapter-15a-qty.md：命令、有无输出、为什么 "11" 和 0 必须分开拒。
缺字段 / null 放到 15B，用文件做。
```

（函数体用正文已有的 qty_allowed + 五条 assert。）

### 15.10 最小文件

```markdown
先在当前目录保存只有两条的 cart_cases.json（完整八条见 15.12）：

[
  {"name": "合法数量", "sku": "SKU-DEMO-001", "qty": 1, "stock": 10, "expect": "ok"},
  {"name": "超过库存", "sku": "SKU-DEMO-001", "qty": 11, "stock": 10, "expect": "exceeds_stock"}
]
```

（若保留 15.10 打印 `list 8 合法数量`，必须把读取示例移到 15.12 之后。）

### ch15-venv 盒子

见 CH15-0001。

### 练习 7

见 CH15-0006。

## 17. 本章结论

**C 明显需要修改**

不是 E：技术脊柱正确，35 个 Python 块可跑，15-1 对真实 `/api/products` 绿，未把学生教成开发，也未踩质量标准禁止的绝对化。  
不是 A/B：存在 P1 图文互殴，加上 15A 过星、实操不写判定、测验不考本章、LOGIN_BAD 未标明与 v1.0 差异，超出「改几个错字」。  
不是 D：不需要重写知识顺序。改图、降星、加闭环、挖空 qty_status、换练习 7 字符串即可回到发布质量。

优先修改顺序：CH15-0001（图）→ CH15-0004（实操手写）→ CH15-0006（练习 7）→ CH15-0007（登录 JSON 标签）→ CH15-0002/0003（15A 坡度）→ caption（0005）。

## 18. 执行记录

### 读过的文件

- `reviews/_full-audit-2026-09-10/AUDIT_AGENT_BRIEF.md`
- `reviews/_full-audit-2026-09-10/REPOSITORY_INVENTORY.md`
- `README.md`、`docs/COURSE_CONTROL.md`、`docs/COURSE_OUTLINE_v1.2.md`、`docs/LEARNING.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`、`practice/STATUS.md`、`exercises/README.md`
- `project/minishop/README.md`（口径）；`project/minishop/docs/PRD.md` 商品/库存条目；`project/minishop/docs/openapi.json` `/api/products`；`project/minishop/server.py` 登录体、`qty_allowed`、商品种子（只核本章相关字段，未审第 19 章正文）
- `chapters/15-python-basics.md`
- `chapters/15a-python-syntax.md`（全文 711 行）
- `chapters/15b-python-files-json.md`（全文 586 行）
- `practice/15-json-check/README.md`、`main.py`、`tests/test_lab.py`
- `practice/_http.py`、`practice/_minishop.py`（确认 15-1 为标准库，不装 requests）
- `chapters/quizzes/README.md`、`chapters/quizzes/stage-5-api.md`
- `reviews/chapter-15-review.md`、`reviews/_pedagogy-2026-09-10/ch15.md`（线索，结论独立复核，未照抄分数）
- `reviews/v1.2.1-rescore.md` 第 15 章行、`reviews/_rereview-2026-09-09/stage-5-ch13-16.md` 第 15 章段（线索）
- 示意图：`ch15-truthy` / `ch15-list-dict` / `ch15-venv` / `ch15-four-json` 的 png+html
- `.gitignore` 中 15-1 validation 规则

未读其他章正文。第 16 章只确认 `16a-pytest-basics.md` 链接存在。

### 实际跑过的命令与结果摘要

| 命令 | 结果 |
| --- | --- |
| `python3 --version` | Python 3.14.3（与教材审查机器声明一致） |
| 抽取 15A/15B 全部 35 个 python 围栏到临时文件执行 | 35/35 退出码 0；有「运行后打印」的块 stdout 与教材一致；完整检查脚本输出 `token_ok` / `over SKU-DEMO-002` / `cases_ok 8` |
| `python3 /tmp/hello_minishop.py` | `hello, minishop` |
| `python3 practice/run.py 15-1` | 退出码 0；HTTP 200；3 件；鼠标 stock=10；写出 validation/products.json 与 latest.json |
| `python3 practice/run.py 15-1 --check` | `Ran 1 test ... OK` |
| `python3 -m venv /tmp/ch15_venv_audit/venv` 后该环境 `python3 -m pip list` | 可见 `pip 25.3` |
| `json.loads` 八条 cart_cases | `list 8 合法数量` |
| 真值 / True==1 / 11.0==11 / JSONDecodeError MRO / 非法 JSON / eval vs loads / `is` SyntaxWarning / `python3 -O` assert / 可变默认 | 见第 8 节；支撑教材正确点与 CH15-0006/0012 |
| 无 cart 文件时 `json.load` | FileNotFoundError（支撑 CH15-0009） |
| 内部相对链接解析 | 17 条内部目标均存在 |

未执行：Windows `py -3`、`.venv\Scripts\activate` / `Activate.ps1`、python.org 安装向导、`source .venv/bin/activate` 进交互 shell（venv 以解释器路径直接调用代替）、`sudo pip`（故意不跑）。

15-1 证据摘要（本机，gitignore，不入库）：

```
HTTP 200
items 3
SKU-DEMO-001 无线鼠标 stock=10
SKU-DEMO-002 键盘 stock=5
SKU-DEMO-003 耳机 stock=3
verdict: JSON 已落盘再读回：三件商品，鼠标库存 10。
```

### 外部核查

| 条目 | 方法 | 结论 |
| --- | --- | --- |
| Truth Value Testing | web_search 抓取 docs.python.org/3/library/stdtypes.html | 假值含 None/False/零/空容器。教材子集正确 |
| bool 是 int 子类、True==1 | 官方 datamodel + 本机 | 与教材一致 |
| 可变默认参数只求值一次 | 本机反例 + 教程「Default Argument Values」检索 | 与教材一致 |
| json.load vs loads、转换表、ensure_ascii 默认 True、JSONDecodeError⊂ValueError、文档仍写 RFC 7159 | web_search 抓取 docs.python.org/3/library/json.html（直连 SSRF blocked） | 与教材 15.12 提示一致 |
| RFC 8259 为现行 JSON 标准 | 教材声明；与 json 模块文档滞后的说明合理 | 通过 |
| `python3 -m pip` / venv / PEP 668 / 不要随手 --break-system-packages | PEP 668、Packaging 实践检索 | 与 15.9 一致 |
| `is` 字面量 SyntaxWarning | 本机 3.14.3 | 有警告；归因「3.14 才有」过窄（CH15-0012） |
| MiniShop 登录失败体 | 读 server.py | `result: fail` 不是 `error`（CH15-0007） |
| 商品种子 | server.py STOCK_MOUSE=10；三件 SKU | 与 15-1 一致 |
| 订单响应无 status | 工作实战断言 + 课程冻结口径 | 通过 |

**【External Verification Required】**：Windows `py -3` 与 PowerShell 执行策略；某一具体 Debian 镜像上 `python3 -m venv` 是否缺 `python3-venv` 包（教学缺口按 PEP 668 提出，未在本机 Debian 复现）。

### 与旧审查的关系

- `reviews/chapter-15-review.md` 曾 99 分、v1.2.1 改 94 并写「本章仍不发 HTTP」——现状 15-1 **确实**发一次标准库 HTTP，索引与 15A/15B 已改成预习口径，旧「不发 HTTP」扣分不再适用。  
- 教学审查 P15-4（venv 图）仍然成立，本审计独立开 CH15-0001。  
- S5-13（15A 不发 HTTP vs 15-1）现行正文已修，不重复开单。  
- 练习跳号现行已说明，不重复开单。  
- 未把旧 92/94/99 写入本报告总分。
