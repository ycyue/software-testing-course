# SECOND_PASS_AUDIT

第二轮 Red Team。不采信第一轮结论。从仓库原文对照 `MASTER_AUDIT.md`。  
日期：2026-09-10  
总控 + RT-01 Coverage/Overscore、RT-02 HTTP/ISTQB/ISO、RT-03 SQL/代码/测验、RT-04 绝对化/链接/岗位。

教材正文仍未改。

---

## 必须回答的问题

### 第一轮漏掉多少问题？

**教材侧新收：2 条 P1 + 14 条 P2。**  
另有审计过程问题（Coverage 表过满、分数虚高、G04 测验 3 Q5 误判为通过），不计入「教材新缺陷」但计入本轮发现。

不是「第一轮没干活」。SQL 数字、pytest 37/1、85 张示意图、practice 全绿、外链主体 200，本轮复现成立。漏的是：测验落点、fixture 建议的等级、SQLite PRAGMA 连接作用域、Host/CL 的 RFC MUST 后半句、若干链接对爬虫 403。

### 新增多少 P0？

**0。** 不新增。第一轮 MASTER-P0-001（种子账号演登录失败）维持。  
`ch13-four-shapes` 本轮仍不升 P0（同节 13.8 表 + 13-1 正确）。

### 新增多少 P1？

**2。**

| ID | 内容 | 第一轮错在哪 |
| --- | --- | --- |
| M-P1-35 | 测验 3 第 5 题：MiniShop「无 token 下单 = 401」。有 Cookie、无 Bearer → **201** | G04 标通过。与 M-P1-09 同机制，**标准答案是新落点** |
| M-P1-36 | 16.6「登录慢改 `scope=session`」+ autouse 清库 → 401 | CH16-0004 写成 P2。按可复制错误升 P1 |

### 哪些章节第一轮评价过高？

| 章 | 第一轮 | 应下调 |
| --: | --- | --- |
| **18** | 82 / C | **74–76 / C**。P95 是标题概念，两处 P1 仍拿最高分 |
| **17** | 80 / C | **75–76 / C**。`getByRole` 可抄即报错 |
| **11** | 81 / **B** | **76–77 / C**。B 偏松 |
| **16** | 79 / **B**、号称 0 P1 | **C**。M-P1-36 之后不能 B |
| **19** | 81 / B | B 靠把空搜索图留在 P2；与第 8 章 P1 不一致 |

第 7 章 81 **不压**（九项折合约 80，主课成立）。  
第 14 章 66 仍是核心章最低，不虚高。

### 哪些内容第一轮没有真正检查？

| 内容 | 第一轮实际 | 本轮 |
| --- | --- | --- |
| mermaid 23 | 计入 252「compile/实跑」，G03 矩阵没有 | `mermaid.parse` 23/23 合法，**未渲染出图** |
| markdown 作业模板 19 | 当正文读；不当代码跑 | 不能 compile。Coverage 记账错 |
| 测验 3 Q5 对 Cookie | 问答做过，**对照错了** | 独立 HTTP：仅缺 Bearer → 201 |
| 测验 5 Q9 / 16 索引 `run.py` | 判「过」，未从仓库根实跑 | 无 `cd`，与 M-P1-31 同类 |
| `PRAGMA foreign_keys` 新连接 | 只在同连接 ON 下跑了失败用例 | 新连接默认 OFF，`user_id=99` 能插入 |
| Host / 非法 CL 的 RFC MUST | 核到「要有这个头」 | 缺 Host MUST 400；非法 CL MUST 关连接 |
| CTFL 四词 root cause | 三格 error/defect/failure 判正确 | FL-1.2.3 是四个词 |
| ISO / GNU 手册对爬虫 | CH01/CH22 写 HTTP 200 | 本轮 `curl`：**403**（浏览器可能仍开） |
| 前端 HTML 当「图」 | G05 图总表未列 | 实现层读过，不是漏图 |
| 浏览器点击 `app.js` | 明确未点 | 本轮仍未点（HTTP 等价） |
| Postman GUI / JMeter GUI | 已披露未跑 | 仍未跑 |

### 哪些图片第一轮遗漏？

**PNG：0。** 磁盘 103（85 示意图 + 9 运行截图 + 9 evidence 副本），G05 全打开，本轮文件集合一致。无断链。`06-register.png` 未挂是重复文件，第一轮已记。

G05 总表漏列 4 个 **非示意图 HTML**（`frontend/index.html` `admin.html` `network-log.html` `pytest-report.html`）。第一轮当实现/证据读过。**不记漏图。**

### 哪些代码块第一轮遗漏？

- **执行层遗漏：** mermaid 23、markdown 19。不是没读，是没按代码执行。
- **SQL 19 条围栏：** 本轮按 12.4 自建库重跑，COUNT/SUM/AVG/JOIN/NULL **全部 MATCH**。第一轮数字没有算错。
- **Postman 15 条 `pm.expect`：** 第一轮抽核 Cookie/401 与 `lastOrderId`。本轮逐条：越权 403 无 `id` 时 `json.id` 空转；改数量只断言 200（RT03-0003 P2）。
- **python/bash 主线：** 无新的「第一轮没跑」的可运行块。

### 哪些答案第一轮没有真正验证？

| 题 | 第一轮 | 本轮独立作答 |
| --- | --- | --- |
| 测验 3 Q5 401 例子 | G04「通过」 | **失败。** 无 Bearer + Cookie = 201。M-P1-35 |
| 测验 3 Q6 Preserve log | G04「通过」，注「MiniShop 可不跳转」 | 题未钉 MiniShop，答案仍按整页跳转写。维持第一轮 CH10 P1，不新开测验 FAIL |
| 测验 6 Q5 教学服务 qty=1 | 已进 M-P1-24 | 维持 |
| 测验 7 Q8 五段 vs STAR | G04-0004 已报 | 维持 |
| 章内 213 题 | G04 6 道 FAIL | 本轮 **无新整题写反** |
| 12A 审查数字 | G03 MATCH | 本轮 MATCH |

### 当前是否还有明显审计盲区？

**有，且应写明，不要再写成 Coverage=100%。**

1. **浏览器里真实点击** MiniShop 前端（下单后是否 `refreshCart` 只按源码推断）。
2. **Postman Collection Runner / Newman GUI**（Cookie jar 已用 HTTP 复现，GUI 仍缺）。
3. **JMeter GUI 导入 `.jmx`**（无本机 `jmeter`）。
4. **mermaid-cli 渲染**（语法过，像素未出）。
5. **ISO 25010:2023 付费全文**（九特性英文名、Testability 挂 Maintainability 已用公开预览/JIS；子特性全表仍 EVR）。
6. **Chrome 152 实机面板**与教材 Timing 文案（第一轮已报，本轮未再开 Chrome）。
7. **GNU/ISO 403**：不确定学生浏览器是否同样被拦。

这些盲区 **不像** 还会藏新的 P0 假规则；可能藏的是更多 P2 工具 UI / 链接反爬。

---

## 20 项检查对照

| # | 检查 | 第二轮结果 |
| --: | --- | --- |
| 1 | 未真正逐段的章 | 22 章都有非空审计。空洞在 **执行声明**（mermaid/模板/测验命令）不在「某章没人读」 |
| 2 | MASTER 没有的技术问题 | M-P1-35/36；M-P2-01…14 |
| 3 | 图片跳过 | PNG 无跳过 |
| 4 | 代码块逐个验证 | 可解释器块第一轮做过；mermaid/markdown 没有 |
| 5 | SQL 重推导 | 数字全对；新问题是 PRAGMA 作用域 |
| 6 | 练习独立作答 | 测验 3 Q5 第一轮假通过；其余无新整题反 |
| 7 | HTTP / RFC / MDN | 主课 safe/幂等仍对。新：Host MUST 400、非法 CL MUST |
| 8 | ISTQB CTFL 4.x | 七原则主线仍对。新：root cause 第四词；原则三静+动 |
| 9 | ISO 25010:2023 | 九特性英文现用名仍对。新：Testability 仍在可维护性；CTFL 考纲旧主名 |
| 10 | 绝对化词 | 「永远/必须」几乎都在禁止句。无「企业都是/实际工作就是」正说。P3：`pwd`「永远比感觉可靠」 |
| 11 | 疑似编造数字/引用 | 未发现新的「通常 80%」。金字塔明确否定 70/20/10 |
| 12 | 跨章矛盾 | 无超出 G01 的新 P1。06B「加购」为旧伤落点 |
| 13 | 重复教学 | 无新的不允许再主讲 |
| 14 | 前置倒置 | 无新 P1 |
| 15 | 难度突跃 | 无新 P1；过载仍是 15A/11 |
| 16 | 岗位脱节 | 新 P2：RESET≠账号池；JD 验证码怎么答 |
| 17 | MiniShop 闭环 | 下单不读购物车第一轮已报。本轮不把教学库与 live 库焊成新 P1 |
| 18 | 截图 vs 工具版本 | pytest-html **4.2.0 仍是当前版**。图裁空 Environment。无假 Postman/JMeter GUI |
| 19 | 链接可访问 | 48 个 https：`curl -L` **45×200**；GNU×2 + ISO **403**。`未知地址`不是资料链。RFC 无 html 经 `-L` 仍 200 |
| 20 | 过高评分 | 18/17/11/16/19，见上表 |

---

## 总控不采纳（避免假阳性）

- 把 live MiniShop 下单后 `qty=10/stock=9` 写成 12.16 教学库「零行」被打破  
- `https://未知地址` 当 404  
- RFC 302 当死链（跟随后 200）  
- 第 3 章 L185「改数量到下单」升 P1（该句正确）

---

## 对第一轮 Coverage 表的修正

不要再写「章节代码围栏 252 已 compile/实跑、未检查 0」。

应写成：

- python/bash/sql/js/json 等：**实跑或 compile**
- mermaid 23 / markdown 19 / 多数 text：**已读源，未当解释器输入**
- PNG 103：**已打开**
- 阶段测验 70：**独立作答；其中 1 题第一轮对照错（现 M-P1-35）**

---

详细 ISSUE：`RT_01_COVERAGE.md` `RT_02_STANDARDS.md` `RT_03_SQL_CODE_QUIZ.md` `RT_04_ABS_LINKS_JOB.md`  
已合并进 `MASTER_AUDIT.md` §10。
