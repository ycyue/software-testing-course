# MiniShop v1.0

个人软件测试实践项目，**不是**企业工作系统，不得写入简历为公司项目。

本目录提供可在本机运行的前端、后端、SQLite、OpenAPI、Postman 集合、pytest、缺陷、日志和测试文档。对应课程第 19 章。

## 运行

```bash
cd project/minishop
python3 server.py
```

终端会打印 `MINISHOP_BASE_URL=http://127.0.0.1:8765`。浏览器打开该地址。

默认 `MINISHOP_RESET=1`：每次启动重建教学库。

教学账号（密码均为 `Test1234`，仅限本机练习）：

| 手机号 | 角色 |
| --- | --- |
| 13800138000 | 普通用户 Tester A |
| 13800138001 | 普通用户 Tester B |
| 13800138099 | 管理员 |

## 自动化

需要已安装 pytest 与 requests 的虚拟环境：

```bash
python3 -m pytest -q
```

审查记录：22 passed，1 xfailed（BUG-001）。

## v1.0 明确不做

支付、物流、优惠券、订单状态机、HTTPS 终止、生产部署。订单接口只返回 `id`，响应中**没有** `status` 字段。

## 文档

- `docs/PRD.md`：已基线需求
- `docs/openapi.json`：接口契约
- `docs/test-plan.md` / `docs/test-cases.md` / `docs/test-report.md`
- `bugs/BUG-001.md`：空搜索仍返回全量商品
