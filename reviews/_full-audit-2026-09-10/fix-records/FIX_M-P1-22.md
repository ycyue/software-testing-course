# FIX RECORD
Audit ID：M-P1-22（CH17-0004 / G03 E60）
原问题：17.4 Playwright 与 Selenium 对照表「定位」行把 JavaScript camelCase（`getByRole` / `getByLabel` / `getByTestId`）写成推荐 API。本课是 Python + pytest 轨；同节示例已是 `page.get_by_role(...)`。按表抄会 `AttributeError`。
修改文件：`chapters/17-automation-overview.md`
修改位置：17.4 对照表「定位」行（原 L135）；同节 Python 示例未改。
原内容：（摘录）

```
| 定位 | 推荐 `getByRole` / `getByLabel` / `getByTestId` 等 | 常用 id、CSS、XPath 等；同样应避免超长绝对路径 |
```

同节已有示例（未改）：

```
page.get_by_role("button", name="登录").click()
```

修复后内容：（摘录）

```
| 定位 | 推荐 Python：`get_by_role` / `get_by_label` / `get_by_test_id`（JS 文档写作 `getByRole` 等，pytest 里不要照抄 camelCase） | 常用 id、CSS、XPath 等；同样应避免超长绝对路径 |
```

为什么这样修：只改对照表这一格，把可抄 API 改成 Playwright Python 的 snake_case，并标明 JS 文档名，避免零基础把 camelCase 写进 pytest。同节示例本来就是 `get_by_role`，表与代码对齐。未整章重写，未改 Selenium 列、安装说明或示例结构。
依据：
- Playwright Python Locators：https://playwright.dev/python/docs/locators （推荐 `page.get_by_role()` / `get_by_label()` / `get_by_test_id()`）
- Playwright JS Locators：`page.getByRole()` 等 camelCase（文档名，不是本课 pytest 可抄接口）
- 本机 `playwright.sync_api.Page` 内省：`get_by_role` / `get_by_label` / `get_by_test_id` 为 True；`getByRole` / `getByLabel` / `getByTestId` 为 False
是否影响其他章节：否。全 `chapters/` 仅本章对照表曾把 `getByRole` 当推荐 API。
验证结果：
- 对照表与同节 `page.get_by_role("button", name="登录")` 一致
- 表内 `getByRole` 只作为「JS 文档写法」出现，并写明 pytest 不要照抄 camelCase
- 其余列（auto-wait、WebDriver、pytest 插件）未动
- Markdown 表仍为 3 列
状态：FIXED
