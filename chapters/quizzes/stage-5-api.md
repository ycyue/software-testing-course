# 阶段测验 5：接口与自动化

覆盖第 13～16 章。通过线：≥8/10；第 2、5、8 题必过。

1. 接口测试和 UI 测试各擅长什么？为什么不能互相取消？
2. （必过）缺字段、`null`、`""`、错误类型为什么要分开测？
3. 测 MiniShop v1.0 登录应以哪份为准？对着服务打 `POST /login`（无 `/api`）会怎样？
4. Postman Environment 和 Collection 变量，谁覆盖谁？（课程口径）
5. （必过）登录脚本把 token 写入环境后，401 用例为什么不能插在“已登录下单”前面还共用同一个已登录 Session？
6. 为什么常用 `python3 -m pytest` 而不是直接 `pytest`？
7. fixture 和 `@pytest.mark.parametrize` 怎么分工？购物车多种 Body 用哪个？
8. （必过）接口自动化 ROI 是不是永远最高？举一个更该先手工的例子。
9. MiniShop v1.0 依赖装在哪？一键命令是什么？
10. 哪句正确？ A. Cookie/Session/Token 是三种 pytest 插件 B. `requests.post(..., json={...})` 发送 JSON Body C. GET 比 POST 安全所以登录用 GET D. 全绿等于没有缺陷

## 答案

1. 接口稳定、适合规则和权限；UI 能看到按钮、跳转、文案。页面挂了接口绿仍可能失败。
2. 它们在 JSON 里不是同一件事，服务端常走不同分支。
3. `project/minishop/docs/PRD.md` 与 OpenAPI。路径是 `/api/login`；无前缀的 `/login` 会 404。
4. Environment 覆盖 Collection。
5. 会先带上登录态，测不到 401。无凭证用例不要 autouse token，也不要共用已登录 Session。
6. `-m` 用的是当前解释器（通常是 venv）里的 pytest。
7. fixture 准备环境；parametrize 展开数据。多种 Body 用 parametrize。
8. 不是。全新、天天改文案的页面不适合先自动。
9. `project/minishop/requirements.txt`。`python3 run.py setup` 然后 `python3 run.py test`。
10. B。
