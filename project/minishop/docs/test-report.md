# MiniShop v1.0 测试报告

- 项目：MiniShop 个人软件测试实践
- 范围：PRD v1.0
- 日期：2026-09-08
- 环境：本机 Python 3.14.3，pytest 9.1.1，requests 2.34.2

## 结论

P0 功能与接口检查通过。存在 1 个开放缺陷 BUG-001（空搜索）。**不能**声称已测通支付或全部订单状态。不作为企业项目经历。

## 自动化

```text
22 passed, 1 xfailed
```

xfailed：`test_empty_keyword_should_not_return_all`（BUG-001）。

## 分层

| 层 | 结果 |
| --- | --- |
| Web 冒烟 | `/` 与 `/admin.html` 返回 200 |
| 接口 | 登录、购物车规则、下单 id、401/403 通过 |
| SQL | 种子数据含 Tester A 购物车；超库存被拒绝 |
| 日志 | `login ok user=13800138000`；`inventory reject ... qty=11` |
| 性能 | 未加压 |

## 出口对照

- 无未关闭 P0 缺陷：是
- 已知 P1 BUG-001：开放并记录
- 报告不含订单状态臆造：是
