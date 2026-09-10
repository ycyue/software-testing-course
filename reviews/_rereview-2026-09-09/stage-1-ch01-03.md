# 第 1～3 章独立复审（2026-09-09）

审查员：只读正文/PRD/图/测验/实操，未改 `chapters/`。旧分（联合复审 98/99/99、v1.2.1 的 93/93/92）只当待核实主张，本文件按 Quality Standard v1.0 与冻结口径重判。

核验过的外部锚点：ISTQB CTFL 4.0.1 七原则与测试过程主活动、V 模型成对关系；ISO/IEC 25010:2023 产品质量模型九特性（Usability→Interaction Capability，Portability→Flexibility，新增 Safety）；Scrum Guide 2020 三类职责。本机执行 `python3 practice/run.py 1-1 --check`：3 tests OK（约 1.0s）。

---

## 总判

三章脊柱仍清楚：**测试 = 观察 + 判定 + 证据**；V 模型没有写成「系统设计↔系统测试」；学习顺序在第 3 章文末预告为 **03→07→04**，没有把下一章写成第 4 章；禁止绝对化（没发现 Bug≠没 Bug、测试必须等开发写完、P0 全球统一、GET/POST 安全、Cookie/Session/Token 三选一、接口 ROI 永远最高）均未正说；教学账号是 `Test1234`；BUG-001 仍按开放缺陷使用。这些是本轮**不应再翻案**的部分。

不能发布的原因不在世界观，而在**把教学扩展写进 MiniShop 作业**。第 3 章「MiniShop 工作实战」主场景是「已下架商品仍可加入购物车」+「商品服务/购物车服务」+「购物车结算」：PRD v1.0 与 `server.py` 都没有商品状态/下架、没有双服务、没有结算、没有删购物车接口。第 1、2 章回归例子同样把「购物车删除、结算」当成项目功能。第 1 章文末「无可运行代码」与章首实操 1-1（已跑通）互相否定。

**结论：第 1、2 章 91 分、DoD 18～19，属「修正后发布」；第 3 章 88 分低于发布线 90，不得按当前正文发布。** 先改第 3 章工作实战对齐 v1.0，再扫三章「结算/删除/下架/0～9999」。

---

## 各章评分（含 DoD x/20）

| 章 | 技术25 | 完整15 | 初学15 | 实战15 | 示例10 | 项目5 | 面试5 | 练习5 | 结构5 | **总分** | **DoD** | 发布 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 23 | 14 | 13 | 14 | 9 | 4 | 5 | 5 | 4 | **91** | **18/20** | 修正后 |
| 2 | 24 | 14 | 14 | 13 | 8 | 4 | 5 | 5 | 4 | **91** | **19/20** | 修正后 |
| 3 | 23 | 14 | 14 | 13 | 8 | 3 | 4 | 5 | 4 | **88** | **18/20** | 不得发布 |

DoD 不通过项：

| 章 | 不通过 | 说明 |
| --- | --- | --- |
| 1 | 10 MiniShop 一致；11 代码/可运行口径 | 把 0～9999、连错锁号、退款、购物车删除/结算写成 MiniShop；文末宣称无 Python，章首却要求跑 `practice/run.py 1-1`（本机已通过） |
| 2 | 10 MiniShop 一致 | 2.8 已标明教学假设，但确认/回归例子仍写「结算、多端库存」；v1.0 无结算、无多端 |
| 3 | 10 MiniShop 一致；13 图表/实战图景 | 工作实战主需求「已下架」不存在；`ch03-six-axes` 的「六顶帽子」与正文六条轴不对齐 |

其余 DoD（目标、前置、七原则/V 模型/Scrum 无硬错误、无禁止绝对化、ISO 2023 未写成「易用性」原文、面试非死记、练习与答案对应、第 3 章预告第 7 章）通过。

第 1 章扣分主要在项目口径和「可运行性说明」自相矛盾，公式+实操 1-1 是全书最强开篇，故仍过 90。第 2 章 V 模型、STLC 主活动、左移/右移、Scrum Developers 口径准确。第 3 章分类坐标系本身可留，被工作实战和重复的冒烟/确认/回归拖到线下。

---

## Issues

### Issue 1 -- Severity: high

- **File:** `chapters/03-software-testing-classification.md:303-315`（连带 `:369` 面试）
- **Description:** 「MiniShop 工作实战」把需求写成修复「已下架商品仍可加入购物车」，并要求测「商品服务与购物车服务的交互」「购物车结算」。这是把教学扩展写成项目能力。PRD v1.0 范围只有注册/登录/商品列表与搜索/购物车数量/创建订单（成功只返回 `id`）；商品表无上架状态；实现是单进程 `server.py`，不是两个服务；页面按钮是「更新数量」「创建订单」，没有结算。学习者会按这张卡片去仓库里找不存在的功能，或把下架/结算抄进第 19 章用例。
- **Suggestion:** 主场景改成仓库里已有的两件：空搜索对照 `R-SEARCH`（BUG-001 仍开放），或 `SKU-DEMO-001` 库存 10 时 `qty=10` 允许、`qty=11` 拒绝。集成级观察用「改数量接口 vs `products.stock`」，回归用「改数量 + 创建订单（Body 无 `status`）」。面试 `:369` 的「结算」同步改掉。
- **Status:** open

### Issue 2 -- Severity: high

- **File:** `chapters/01-software-testing-intro.md:291`；`chapters/02-software-development-process.md:247`、`:280`；`chapters/03-software-testing-classification.md:245`、`:311`
- **Description:** 三章都把「购物车删除 / 结算」当作 MiniShop 修复后的回归对象。实现里 `qty < 1` 直接 400（`server.py` `_cart_items`），没有删除购物车接口；非范围包含支付，创建订单成功只返回 `id`。第 3 章 `:245` 已经写明「v1.0 没有结算金额字段」，同一章工作实战和面试又写「购物车结算」——章内自相矛盾，不是漏标一次。
- **Suggestion:** 回归例子统一成：合法数量、等于库存、登录、创建订单、库存扣减（下单才会扣库存，改购物车数量不会）。删除/结算若要保留，必须写成「电商领域思路，不要写进项目用例」，与 `:245` 同一句式。
- **Status:** open

### Issue 3 -- Severity: medium

- **File:** `chapters/01-software-testing-intro.md:125`
- **Description:** 「MiniShop 规定库存范围为 0～9999 件，代码却实现成 0～99999」被写成项目规则。PRD 没有库存上下限；`products.stock` 只是整数；教学库存是 10/5/3。`:218` 对密码 8～20 vs 8～16 做了「不要抄进项目用例」的隔离，库存范围没有同等隔离。会直接被抄成第 19 章用例。
- **Suggestion:** 改成未绑定 MiniShop 的位数错误例子，或改用已冻结的 `R-CART-10`（10 允许、11 拒绝）。
- **Status:** open

### Issue 4 -- Severity: medium

- **File:** `chapters/01-software-testing-intro.md:501-503`（与 `:5`、`:74-76` 冲突）；`practice/01-observation-oracle-evidence/`
- **Description:** 章首阅读提示和核心公式要求跑 `python3 practice/run.py 1-1`；文末可运行性说明写「没有 Python、SQL、curl、JSON 或 pytest 示例，因此没有需要执行验证的代码」。这是诚实证据口径错误。本机 `python3 practice/run.py 1-1 --check` 已通过，且复现 BUG-001（空白关键字 200 + 3 件）。v1.2.1 写「第 1 章纯概念、无运行产物」已过时，不能再当评分依据。
- **Suggestion:** 可运行性说明改为：概念正文无片段代码；配套实操 1-1 为 ✅ 可运行，验收见 `practice/01-observation-oracle-evidence/README.md`。
- **Status:** open

### Issue 5 -- Severity: medium

- **File:** `chapters/01-software-testing-intro.md:81-82`、`:96`、`:224`；`chapters/assets/diagrams/ch01-static-dynamic.png`（图内「PRD 片段」：连输错、冻结账号）
- **Description:** 静态测试例子用「密码连续输错 20 次 / 账号冻结何时恢复 / 退款规则互相矛盾」，示意图直接标成 MiniShop「PRD 片段」。PRD 无冻结、无连错锁定、无退款（退款在非范围）。第 3 章 `:89` 对「退款后优惠券」有「不是 v1.0」标签，第 1 章同类例子没有。冻结口径要求第 19 章前的优惠券/支付/订单状态必须标明教学约定；退款/冻结虽不在短名单，但写成 MiniShop PRD 会同样被抄。
- **Suggestion:** 图和正文改成 v1.0 真缺口（空搜索该不该返回全量，即 `R-SEARCH`/BUG-001），或明确「假设的 PRD 草稿，不是仓库 PRD」。
- **Status:** open

### Issue 6 -- Severity: medium

- **File:** `chapters/01-software-testing-intro.md:252` → 第 2、3 章「确认测试」
- **Description:** 原则七把 Validation 译成「确认」，紧接着第 2、3 章的核心术语「确认测试」是 Confirmation testing（缺陷修复验证）。ISTQB 里这是两个词。第 1 章已提醒「不要只凭中文词面」，但没有预告下一章「确认」会换含义。零基础会把 Validation 和确认测试合成一件事。
- **Suggestion:** 原则七改用「确认（Validation，是否满足预期用途）」并加半句：后文「确认测试」专指 Confirmation，不是 Validation。
- **Status:** open

### Issue 7 -- Severity: medium

- **File:** `chapters/02-software-development-process.md:221-247` 与 `chapters/03-software-testing-classification.md:216-247`
- **Description:** 冒烟 / 确认 / 回归在相邻两章各讲一遍，MiniShop 购物车超库存例子几乎相同。第 3 章的分类贡献只是「把它们挂到目的轴」，不需要再定义一次。这是整段可删的重复，不是两处互相纠正。
- **Suggestion:** 第 3 章 3.6–3.7 收成「第 2 章已定义；本轴只回答这一轮为什么测」，留一张对照表即可。
- **Status:** open

### Issue 8 -- Severity: medium

- **File:** `chapters/03-software-testing-classification.md:93` vs `:470`；对照 `docs/COURSE_CONTROL.md:81`（01→02→03→07→04）
- **Description:** 文末预告正确（下一章第 7 章，再进入第 4 章）。但 3.1 写「第 4 章将主讲静态测试」，按文件名排序的读者会从 `03` 走进 `04`，跳过 Web。这不是把下一章误写成第 4 章，而是章内指针与学习顺序冲突，必须记。
- **Suggestion:** `:93` 改成「按学习顺序先读第 7 章 Web，再在第 4 章主讲静态测试；本节只定位置」。
- **Status:** open

### Issue 9 -- Severity: medium

- **File:** `chapters/assets/diagrams/ch03-six-axes.png`（源 `ch03-six-axes.html`）；对照 `chapters/03-software-testing-classification.md:65-72`
- **Description:** 正文六条轴是：静态/动态、级别、质量目标、黑白盒、手工/自动化、目的/时机。图标题「六顶帽子」实际是：功能、黑盒、系统级、手工、也可自动化、回归候选——缺「是否执行」，把同一条执行方式拆成两顶。核心课要靠这张图记住坐标系，轴对不上会记错。
- **Suggestion:** 六顶帽子与六条轴一一对应；手工/自动化合并为一顶。
- **Status:** open

### Issue 10 -- Severity: medium

- **File:** `chapters/quizzes/stage-1-foundations.md:2`、`:6`、`:17-23`
- **Description:** （1）答案 2 写「QC 侧重工作产品和过程的控制」，第 1 章 `:154-156` 是 QA=过程、QC=产品是否达标、Testing=取质量信息。测验把「过程」塞进 QC，和正文打架。（2）答案 6 用「登录 401/200」和「好不好用」：401 是第 9 章 HTTP 观察，阶段 1 只覆盖到第 7 章；「好不好用」是易用性口语，第 3 章已要求 ISO 25010:2023 用「交互能力」并标明旧译。题干要 MiniShop 各举一例，答案却不点 v1.0 真实例（空搜索、qty=11、订单 Body 无 status）。
- **Suggestion:** QC 定义拉回第 1 章；功能例用登录成功进首页或 `qty=11` 被拒；非功能例用搜索是否在约定时间内返回 / 提示是否能懂（交互能力），不要「好不好用」当术语。
- **Status:** open

### Issue 11 -- Severity: low

- **File:** `chapters/02-software-development-process.md:290-297` vs `:386-388`、`:400`
- **Description:** 2.9 说「在自己的练习仓库」执行，示例却是 `git add chapters/02-software-development-process.md`。练习 9 要改的是学习者自己的 Markdown。空练习仓库照抄会 pathspec 失败；在本课程仓库照抄会把教材文件提交进去。命令本身在本仓库路径是存在的，所以不是旧复审里那个「文件已改名」错误，但仍是示例对象错位。
- **Suggestion:** 示例改成 `git add notes.md` 或 `exercises/ch02.md`，并写明不要 add `chapters/`。
- **Status:** open

### Issue 12 -- Severity: low

- **File:** `chapters/02-software-development-process.md:266-269`；`practice/README.md` 表「2-1」
- **Description:** 2.8 声明「尚不是仓库级正式规格，正式 PRD 建立后以基线为准」。仓库里 PRD v1.0 已经存在，且这条数量规则就是 `R-CART`。教学隔离有必要，但「建立后」是过时时间线。`practice/README.md` 把 2-1 写成「在 MiniShop 上标出需求→提测→冒烟会落在哪」，正文 2.8 却是一张已填满的表，没有空白验收和 ✅/📖 类型（Quality Standard 第七节要求实操写清类型与验收）。
- **Suggestion:** 改成「与第 19 章 PRD `R-CART` 同方向，本章先当教学假设」；2.8 留空四格让学生填，或把 2-1 指向练习 3。
- **Status:** open

---

## 结构简化机会（code-judo：能否删掉整类复杂度）

1. **第 3 章不要再定义冒烟/确认/回归。** 第 2 章 2.7 已经够用。第 3 章只保留「目的轴」一行和指向第 2 章的链接。删掉 3.6–3.7 的完整重讲，比继续打磨措辞更有效（Issue 7）。
2. **第 3 章工作实战不要发明下架/微服务。** 分类课用登录错误密码或 `qty=11` 就能戴满六轴。少一个虚构电商功能，项目一致性和实战同时变好（Issue 1）。
3. **第 1 章 1.8–1.9 岗位与发展路线** 对脊柱（观察/判定/证据）几乎无贡献，和第 21–22 章重复。可压成一段「起点是功能测试，岗位名以招聘 JD 为准，路线见第 22 章」。
4. **第 2 章 2.9 Git** 不是「测试在生命周期中的位置」。最小 Git 可挪到第 11 章或练习仓库 README；本章留一句「证据要进版本库」即可。
5. **第 1 章 ISO 九特性清单** 对零基础过密。正文只展开功能/性能/兼容/交互/可靠/信息安全，其余三个放脚注或图注（图 `ch01-quality` 已经这么做了），正文 1.4 的 1–9 编号表可删。

这些是删整类复杂度，不是再补一节「注意」。

---

## 未改但可接受的风险

- **ISO 25010:2023 教学译法**（交互能力、安全保障性、灵活性）不是 ISO 官方中文；正文已标明「本课程教学译法」，且未把 Interaction Capability 正说成「易用性」。可接受。
- **灰盒** 不是 CTFL 4.0 一等公民；第 3 章已写成行业实践并要求说清用了哪些内部信息。可接受。
- **示意图提前出现 401/400/403、pytest、OpenAPI、SQL。** 对第 1 章零基础偏早，但没有教错 MiniShop 登录失败确为 401。当作后续观察通道的预告，不升 Issue。
- **支付作为缺陷集群例子**（第 1 章原则四、练习 6）：`:129` 已声明支付不是 v1.0。保留可以，不要再写进 MiniShop 工作实战。
- **2.8 数量规则与 `R-CART` 同方向却标成教学假设：** 符合「第 19 章前不把字段当冻结契约」。时间线用词见 Issue 12，规则本身可留。
- **MiniShop 正文未每次重复「个人实践项目」：** 三章没有冒充公司项目；阶段测验第 10 题覆盖。可接受。
- **阶段测验含第 7 章题（7、8）：** 测验 README 写明学完第 7 章再做。不把 7、8 题算进第 1–3 章缺陷。
- **BUG-001 故意开放、密码 `Test1234`、订单成功无 `status`、空搜索仍失败：** 与 PRD/实现/实操 1-1 一致，不要「修掉」。

---

给主审查员：先改 Issue 1（第 3 章工作实战对齐 v1.0 的 BUG-001 或 `qty=11`），否则第 3 章不能过 90；同一批扫掉三章里的「结算/购物车删除/下架」（Issue 2）。第 1 章只需要改可运行性说明、去掉 0～9999 这条假 MiniShop 规则，公式和实操 1-1 不要动。V 模型、学习顺序 03→07、七原则、Test1234、BUG-001 开放这五条冻结口径本轮是守住的，回写时不要改回去。
