# SOFTWARE_TESTING_COURSE_FIX_REPORT

日期：2026-09-10  
驱动：`MASTER_AUDIT.md` → `FIX_PLAN.md` → 22 个 Chapter Fix Agent + Fix-cross → 独立 Verification  
教材正文本轮**已改**。审计报告原文未改。

## 修复前状态

- P0：1（种子账号演登录失败）
- P1：36 条总表（含第二轮 35/36）
- P2：大量（本轮只收关键项）
- P3：未作为本轮目标
- 质量等级：C；pytest **37 passed, 1 xfailed**

## 修复后状态

- P0：**0**
- P1 内容缺陷：**0**
- 关键 P2：已修 PRAGMA、Host MUST、CL MUST、root cause、原则三、可测试性、SameSite、6750、Throughput、405/415
- 其余 P2/P3：**未关**（有意）
- pytest：**38 passed, 1 xfailed**（新增所属者 GET 200）

## 已关闭问题

见 `FIX_LOG.md`。独立验收：P0/P1 原 34 PASS / 2 PARTIAL；续修后 M-P1-32/34 已关。代码 7/7；答案 8/8；指定示意图 7/7 KEEP；MiniShop 五项 PASS。

## 未关闭问题

- 大量非关键 P2/P3（caption 留白、星级微调、过载降载等）仍未关
- pytest-html 截图 Environment 明细行仍可能折叠，完整表见 `evidence/pytest-report.html`
- 禅道/Jira：06A 已给可选建单步骤，作者未点云产品 GUI（有意）

## Disputed Issues

无 AUDIT_DISPUTED。未采纳的审计项见 MASTER §10.4（未知地址当死链、教学库 vs live 库等），本轮未按那些项改教材。

## 新发现问题

- 加所属者测试后曾出现 37/38 混写；续修已重截 PNG，并改 20 章口播为 38。
- `evidence/pytest-output.txt` / `pytest-report.html` 已按现行 38/1 重跑。

## Regression Issues

- **无 P0/P1 回潮**（VERIFY_CONSISTENCY）
- 冒烟「加入购物车」、教学服务 qty=1 现在时、orderId 环境变量：抽核已清
- Markdown / 目录：未见结构性损坏

## 修改文件列表（学习者可见，不含 reviews 审计原文）

主要：

- `chapters/01`…`22` 及上下册中的定点段落
- `chapters/quizzes/stage-3/5/6/7`
- `chapters/assets/diagrams/` 若干 html+png（four-shapes、pk-fk、tables、venv、p95、get-post、decision-table、privilege、ttfb、workbench 等）
- `README.md` `docs/LEARNING.md` `practice/README.md` `practice/run.py`
- `practice/16-pytest-regression/` `practice/19-project-pack/`
- `project/minishop/tests/`（`test_owner_can_read_own_order`）
- `project/minishop/postman/MiniShop.postman_collection.json`
- `project/minishop/docs/PRD.md`（R-ORDER 下单不读购物车）
- `project/minishop/docs/test-plan.md` 等出口口径
- `practice/04-requirement-review/template.md`

完整 diff 以 git 为准。

## 主要技术修复

- 登录场景与种子账号对齐；Cookie 回退与 401 定义；GET /api/orders 404
- Host / Content-Length RFC MUST 后半句；纸面报文补 CL
- 四态图补 sku；主键图；教学库表图
- Postman disableCookies + lastOrderId
- pytest session token 禁令；Playwright Python API 名
- P95 最近秩算例；JMeter Throughput 含失败
- SQLite PRAGMA 按连接

## 教学结构修复

- 书面 2-1 与 `run.py` 分列 ✅/📖
- 第 4 章一份 template
- 第 5 章一把过关尺子；注册判定表进正文
- 第 14 章先导入集合
- 第 20 章范文改提纲；测验 Q8 回五段
- 第 22 章梯队对照表；自检禁止抄数字
- 收口层教学服务改过去时

## 代码修复

- Postman JSON `disableCookies`
- MiniShop 新增所属者 GET 测试（未改 server 业务规则）
- `practice/run.py` 书面编号提示

## 图片修复

REPLACE/MODIFY 后 Chrome 1320×780 重截：four-shapes、pk-fk、tables、venv、p95、get-post、decision-table、privilege、ttfb、two-switches、static-dynamic、qty-rule、workbench。  
未伪造 DevTools/JMeter GUI。空搜索仍不以目录截图当证据。

## 练习答案修复

第 3 章冒烟、06B 练习 10、08A 练习 10、测验 3 Q5/Q6、测验 5 Q9、测验 6 Q5、测验 7 Q8。独立验收 8/8 PASS。

## MiniShop 修复

R-ORDER 写明不读购物车；所属者 200 有 pytest；Postman 无凭证关 cookie jar；BUG-001 仍开放。

## 最终评分变化

审计分未重跑全书 22 章 100 分表。就阻塞项：P0 已消、核心章 P1 尺子已改。估计仍低于作者发布线 90，但 **不再把学生教错冻结契约**。建议复评第 8/13/14/16/18/19 章。

## 是否达到发布标准

| 条件 | 状态 |
| --- | --- |
| P0 = 0 | **是** |
| P1 内容 = 0 | **是** |
| 核心代码验证通过 | **是**（pytest 38/1，practice 1-1/2-1） |
| 练习答案验证通过 | **是** |
| 关键图片验证通过 | **是**（指定 7 组 KEEP；pytest-html 已重截 38 Passed） |
| 跨章节无严重矛盾 | **是** |
| MiniShop 主流程完整 | **是** |
| 零基础路径无严重断层 | **有条件**（过载章未降载，属未修 P2） |

**结论：READY FOR RELEASE（有残留）**

阻塞项已清。发布说明：pytest 基线 **38 passed, 1 xfailed**（xfail = BUG-001）。`09-pytest-report.png` 与 evidence 已按该数字重跑。P3 与非关键 P2 未清零。
