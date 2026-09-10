# FIX RECORD
Audit ID：M-P1-04（CH04-0001 / CH04-0002 / CH04-0003）
原问题：第 4 章作业同时存在「四份内容」、04B 内嵌 9 列表、`template.md` 三套规格；验收第 5 条约束「已确认规则」，但学生复制的模板没有该节；04B 让学生对照覆盖矩阵，矩阵把未冻结的「不落库」写成 R-CART 要点。
修改文件：
- `chapters/04b-minishop-requirement-review.md`
- `practice/04-requirement-review/template.md`
- `practice/04-requirement-review/README.md`
- `project/minishop/docs/prd-coverage-matrix.md`
修改位置：
- 04B「MiniShop 工作实战：需求评审包」整节；练习 9 / 答案 9；参考资料矩阵条
- `template.md`「范围与非范围」之后
- 实操 4-1 README 验收条件第 5 条之后
- 覆盖矩阵 R-CART-10 行「要点」及表下对照句
原内容：（摘录）
> 选择注册、登录或购物车之一，提交以下四份内容：
> 1. 功能流程和业务对象；
> …（04B 内嵌第二套 9 列 markdown）
> 对照仓库正式评审：`project/minishop/docs/requirement-review.md` 与覆盖矩阵 `docs/prd-coverage-matrix.md`。
> （template.md 无「已确认规则」节）
> （矩阵）R-CART / R-CART-10 | qty=11 拒绝且不落库
修复后内容：（摘录）
> 提交一份记录：直接复制 `practice/04-requirement-review/template.md`，存为 `exercises/chapter-04-minishop-requirement-review.md`。不要另做第二套表。
> 完成标准与实操 4-1 相同（五条）。评 v1.0 时「已确认规则」只许抄 PRD；矩阵「不落库」是实现观察，写进已确认规则不合格。
> template 新增「已确认规则」三列，并写明来源只能是 PRD，不能是草案或覆盖矩阵。
> 矩阵要点改为「qty=11 拒绝（PRD）；不落库为实现观察，非 PRD 原文」。未改 `PRD.md` 冻结句。
为什么这样修：作业只留一份规格，验收第 5 条才有落点；学生不会把实现侧「不落库」抄成已确认规则。
依据：CH04-0001/0002/0003；Quality Standard「练习覆盖目标」「答案与练习对应」；PRD `R-CART-10` 只写 qty=11 拒绝；stage-2 Q2 不要发明失败保持原值。
是否影响其他章节：第 5/19 章仍可引用覆盖矩阵当证据，但第 4 章作业不再把它当 PRD。未改冻结 PRD 规则、未改测试/实现。
验证结果：04B 已无「四份内容」和内嵌第二套表；template / 04B / 4-1 README 同五条验收；`python3 practice/run.py 4-1` 退出码 0；`PRD.md` R-CART-10 原文未动。
状态：FIXED
