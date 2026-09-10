# FIX RECORD
Audit ID：M-P2-06（RT02-0005，第 4 章落点）
原问题：04A §4.8「需求可测试性」与 ISO/IEC 25010:2023 可维护性子特性 Testability 同名，未标明对象不同。学生会把「登录速度要快不可测」答成「产品 Testability 差」，或以为 ISO 九特性漏了一项。
修改文件：`chapters/04a-requirements-static-testing.md`
修改位置：§4.8 开篇定义句之后（原 L202）
原内容：（摘录）
> 可测试性意味着要求能够用可行的方法验证，并能判断通过或失败。
修复后内容：（摘录）
> 可测试性意味着要求能够用可行的方法验证，并能判断通过或失败。这里的「需求可测试」问的是这句话能不能写成可观察的通过/失败标准，对象是需求句子；它不是 ISO/IEC 25010:2023 可维护性（Maintainability）子特性 Testability（产品是否容易建立并执行测试）。
为什么这样修：只补一句对照，不重写 4.8。两个 testability 对象不同：前者是 CTFL 测试分析对测试基础的可判定性，后者是产品质量模型里可维护性 3.7.5。未按 arc42 写成灵活性子特性。
依据：RT02-0005；JIS X 25010 / ISO/IEC 25010:2023 3.7.5 Testability 位于 Maintainability，3.8 Flexibility 不含 Testability；CTFL v4.0.1 §1.4.1 test analysis 评估 test basis 的 testability。第 1 章九特性补子特性不在本任务范围。
是否影响其他章节：否。未改第 1 章 1.4。
验证结果：4.8 其余禁止擅自补「2 秒」的教法未动；未把需求可测试写成 ISO 产品特性。
状态：FIXED
