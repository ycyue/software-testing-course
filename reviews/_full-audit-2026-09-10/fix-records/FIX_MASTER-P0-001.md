# FIX RECORD
Audit ID：MASTER-P0-001
原问题：场景导入用冻结种子账号 `13800138000` / `Test1234` 演「登录失败并发现缺陷」。同组凭证在 PRD、pytest、第 10/13 章会登录成功。全书仍开放的缺陷是空搜索 BUG-001，不是登录。
修改文件：
- `chapters/01-software-testing-intro.md`
- `chapters/assets/diagrams/ch01-static-dynamic.html`（LOCAL REGRESSION：动态卡仍写「密码填对 → 登录失败」）
修改位置：场景导入（原 L33–42 一带）；MiniShop 工作场景引用块；`ch01-static-dynamic.html` 动态卡。
原内容：（摘录）
```
- 手机号：13800138000
- 密码：Test1234（教学示例，与第 19 章项目数据相同；不是生产密码）

点击登录，结果却是“登录失败”。你发现了一个缺陷，这当然属于测试。
```
动态卡原句：「密码填对，点登录 → 页面写「登录失败」」；工作场景原句：「本章中的手机号、密码、库存数字仅用于解释测试思维。」
修复后内容：（摘录）
```
- 手机号：13800138000
- 正确密码：Test1234（与第 19 章项目数据相同；不是生产密码）

这组凭证在仓库里**会登录成功**，不是开放缺陷。要演示一次「失败观察」，请改用错误密码，例如 `Test1234x`：页面会显示「登录失败」。
…
仓库里真正仍开放、要用实操 1-1 复现的，是空搜索返回全量商品（BUG-001），不要和这次登录失败观察混成一件事。
```
工作场景改为教学账号会登录成功，错误密码只演示失败观察。动态卡改为 `Test1234x` 失败观察，并写明 `Test1234` 会成功、开放缺陷是 BUG-001。
为什么这样修：第一课不能把冻结种子写成真实登录缺陷。失败观察仍能讲清观察 / 判定 / 证据；尺子对照后失败是预期结果，不是仓库缺陷。
依据：`project/minishop/tests/test_api.py` `test_login_ok`（`13800138000` / `Test1234` → 200 + token）；`test_login_wrong_password`（错误密码 → 401）；`project/minishop/bugs/BUG-001.md`（空搜索仍开放）。MiniShop 冻结：密码 Test1234 登录成功。
是否影响其他章节：否。未改第 10/13/19 章。第 1 章示意图 HTML 已对齐；PNG 未重截。
验证结果：
- MiniShopLab：`Test1234` → HTTP 200，`result=ok`，有 token；`Test1234x` → HTTP 401，`{"result":"fail"}`。
- `python3 practice/run.py 1-1 --check`：3 tests OK。
- 章内已无「Test1234 登录失败并发现缺陷」的正说。
- **需重截 PNG**：`chapters/assets/diagrams/ch01-static-dynamic.png`（Coordinator 统一 Chrome 截图）。
状态：FIXED
