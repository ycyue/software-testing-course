# MiniShop v1.0 测试报告

- 项目：MiniShop 个人软件测试实践
- 范围：PRD v1.0
- 日期：2026-09-09
- 环境：本机 Python 3.14.3，pytest 9.1.1，requests 2.34.2
- 采集：`python3 run.py evidence`

## 结论

P0 功能与接口检查通过，含注册（合法 / 非法手机号与密码 / 占用）。存在 1 个开放缺陷 BUG-001（空搜索）。**不能**声称已测通支付或全部订单状态。不作为企业项目经历。

## 自动化

```text
37 passed, 1 xfailed
```

原文：`evidence/pytest-output.txt`。xfailed：`test_empty_keyword_should_not_return_all`（BUG-001）。

相对 2026-09-08 的 22 passed：本轮补了注册、页面表单、qty=11 不落库和商品目录断言。

## 分层

| 层 | 结果 | 证据 |
| --- | --- | --- |
| Web 冒烟 | `/` 含登录与注册表单；`/admin.html` 200；错误密码见「登录失败」；qty=11 页面提示 `qty exceeds stock` | `evidence/screenshots/` |
| 接口 | 注册 201/400/409；登录 200+HttpOnly Cookie；qty=10 200、qty=11 400；下单 201 无 status | `evidence/http/` |
| SQL | 种子：鼠标 qty 1 stock 10、键盘 qty 2 stock 5。证据会话 qty=10 后仍不是 11 | `evidence/sql/seed-join.txt` |
| 日志 | `login ok user=13800138000`；`inventory reject ... qty=11` | `evidence/logs/app-sample.log` |
| 性能 | 未加压 | — |

覆盖矩阵：`docs/prd-coverage-matrix.md`。

## 出口对照

- 无未关闭 P0 缺陷：是
- 已知 P1 BUG-001：开放并记录
- 报告不含订单状态臆造：是
- 数字与仓库 pytest 输出一致：是
