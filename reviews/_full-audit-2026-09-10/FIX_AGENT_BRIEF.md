# Chapter Fix Agent 统一指令

你在修教材，不是重写教材。

工作区：`/Users/plong/Desktop/学习文件夹/软件测试class`
台账：`reviews/_full-audit-2026-09-10/FIX_PLAN.md`、`MASTER_AUDIT.md`

## 硬约束

1. **只修分配给你的 Audit ID。** 不要为统一文风改无关段落。
2. 优先改该段/该表/该答案/该图。禁止整章重写，除非 FIX_PLAN 写明「重写小节」。
3. 每个 Audit ID 写一条 FIX RECORD 到 `reviews/_full-audit-2026-09-10/fix-records/FIX_<ID>.md`。
4. 技术修复用 ISTQB CTFL 4.x、ISO 25010:2023、RFC 9110/9111/9112、官方工具文档。不要用培训班口号。
5. 初学者能懂：准确但不把 RFC 原文堆上去。
6. MiniShop 冻结：`/api/`、qty=10/11、订单无 status、BUG-001 开放、个人实践项目、密码 Test1234 登录**成功**。
7. 修代码/SQL/JSON 后能跑就跑。预期结果必须同步。
8. 修图：改同名 `.html`，并在记录里写「需重截 PNG」。Coordinator 统一 Chrome 截图。
9. 修练习：独立再解一次，再改正文答案和解析。
10. 禁止改 `reviews/` 里的审计报告原文（只允许写 fix-records 与 FIX_PLAN 状态）。
11. 发现审计本身错了：标记 AUDIT_DISPUTED，不要为了修而改对的内容。
12. 修完做 LOCAL REGRESSION：前后文、术语、代码输出、图注、答案、Markdown。

## FIX RECORD 模板

```
# FIX RECORD
Audit ID：
原问题：
修改文件：
修改位置：
原内容：（摘录）
修复后内容：（摘录）
为什么这样修：
依据：
是否影响其他章节：
验证结果：
状态：FIXED
```
