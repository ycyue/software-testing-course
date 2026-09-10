# MiniShop v1.0

个人软件测试实践项目，**不是**企业工作系统，不得写入简历为公司项目。

本目录提供可在本机运行的前端、后端、SQLite、OpenAPI、Postman 集合、pytest、缺陷、日志、截图和测试文档。对应课程第 19 章。

## 一键运行

需要本机 `python3`（审查环境 3.14.3；3.12+ 即可）。

```bash
cd project/minishop
python3 run.py setup      # 创建 .venv 并安装 requirements.txt
python3 run.py serve      # 启动 http://127.0.0.1:8765
```

另开一个终端：

```bash
python3 run.py test       # pytest
python3 run.py evidence   # pytest + curl/SQL/日志/截图（截图需要本机 Chrome）
```

Windows 可用 `run.bat`。macOS / Linux 可用 `./run.sh`。

`server.py` 只使用标准库，不装依赖也能 `python3 server.py`。pytest 需要 `requirements.txt` 里的 `pytest`、`pytest-html` 与 `requests`。

默认 `MINISHOP_RESET=1`：每次启动重建教学库。

教学账号（密码均为 `Test1234`，仅限本机练习）：

| 手机号 | 角色 |
| --- | --- |
| 13800138000 | 普通用户 Tester A |
| 13800138001 | 普通用户 Tester B |
| 13800138099 | 管理员 |

## 自动化

```bash
python3 run.py test
```

本机 2026-09-10：`38 passed, 1 xfailed`（BUG-001）。原始输出：`evidence/pytest-output.txt`。

## v1.0 明确不做

支付、物流、优惠券、订单状态机、HTTPS 终止、生产部署。订单接口只返回 `id`，响应中**没有** `status` 字段。

## 文档与证据

- `docs/PRD.md`：已基线需求
- `docs/prd-coverage-matrix.md`：规则 → 用例 → 证据
- `docs/test-plan.md` / `docs/test-cases.md` / `docs/test-report.md`
- `evidence/`：本机执行产物（HTTP、SQL、日志、截图）
- `bugs/BUG-001.md`：空搜索仍返回全量商品
