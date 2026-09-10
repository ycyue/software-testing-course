# FIX RECORD
Audit ID：M-P2-04
原问题：06A 6.1 自称 ISTQB 常用区分，表只有错误 / 缺陷 / 失效三格。CTFL 4.0.1 可考 LO FL-1.2.3 是四个词：root cause、error、defect、failure。缺根因会把「error 和 root cause 有什么区别」答成三层链。
修改文件：`chapters/06a-bug-management.md`
修改位置：学习目标首条；§6.1 导语与四列表；关系句；「因此」第三条；检查清单首条
原内容：（摘录）
> 先把三个容易混用的词分开。ISTQB 的常用区分是：
> | 错误（Error / Mistake） | … |
> | 缺陷（Defect / Fault / Bug） | … |
> | 失效（Failure） | … |
> 关系通常是：人的错误可能把缺陷引入……
> 根因可能是代码，也可能是需求、数据、配置或环境。
修复后内容：（摘录）
> 先把四个容易混用的词分开。ISTQB CTFL 4.0.1（FL-1.2.3）要区分的是：
> | 根因（Root Cause） | 导致问题发生的根本理由，例如导致人犯错的条件 | 库存规则未评审、工期紧，比较符被写反 |
> | 错误（Error / Mistake） | … |
> | 缺陷（Defect / Fault / Bug） | … |
> | 失效（Failure） | … |
> 关系通常是：根因 → 错误 → 缺陷 →（可能）失效。……不是每条失效都能追到单一根因。
为什么这样修：只在原表补第四项短定义和一条链，不重写 6.1。原「根因可能是代码…」把缺陷所在位置说成根因，与第四词冲突，改为根因分析用来减少同类再发。学习目标和清单与表对齐。
依据：ISTQB CTFL Syllabus v4.0.1 Keywords 与 FL-1.2.3（K2）Distinguish between root cause, error, defect, and failure；§1.2.3：A root cause is a fundamental reason for the occurrence of a problem；RT02-0003；FIX_PLAN M-P2-04
是否影响其他章节：示意图 `ch06-error-defect-failure` 仍为三张卡片，本 ID 只要求表补第四项，不重截 PNG。练习 1 仍考错误/缺陷/失效三层对应，可保留。
验证结果：表四行齐全；链含根因；未把环境故障写成必须经过人的错误；未整章重写。
状态：FIXED
