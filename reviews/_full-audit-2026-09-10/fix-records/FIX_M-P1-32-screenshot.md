# FIX RECORD

Audit ID：M-P1-32（收口 PNG）
原问题：所属者 GET 测试已加，基线 38/1，但 `09-pytest-report.png` 仍显示 37 Passed
修改文件：
- `project/minishop/evidence/pytest-output.txt`
- `project/minishop/evidence/pytest-report.html`
- `project/minishop/evidence/screenshots/09-pytest-report.png`
- `chapters/assets/09-pytest-report.png`
- `chapters/20-interview.md`（口播 37→38）
修改位置：pytest-html 汇总条
原内容：37 Passed / 38 tests
修复后内容：39 tests；**38 Passed**；1 Expected failures；pytest-html v4.2.0；日期 10-Sep-2026 13:43
为什么这样修：截图必须与现行基线一致
依据：本机 `.venv` pytest 38 passed, 1 xfailed
是否影响其他章节：14/16A/19 共用该 PNG，现与正文 38 对齐
验证结果：打开 PNG 可见 38 Passed / 1 Expected failures
状态：FIXED
