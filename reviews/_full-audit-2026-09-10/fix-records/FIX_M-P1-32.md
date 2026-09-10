# FIX RECORD
Audit ID：M-P1-32（G06-0001 / CH19-0006）
原问题：R-PERM「所属者可读自己的订单」只有 B 读 A → 403 的拒绝路径；所属者 `GET /api/orders/{id}` → 200 且无 `status` 无 pytest。若实现改成「谁都 403」，现网仍绿。
修改文件：
- `project/minishop/tests/test_api.py`（新增 `test_owner_can_read_own_order`）
- `project/minishop/docs/test-cases.md`、`test-points.md`、`prd-coverage-matrix.md`、`test-report.md`、`resume-evidence.md`、`README.md`
- `project/minishop/evidence/pytest-output.txt`、`evidence/pytest-report.html`
- `chapters/19-minishop-project.md`（写死的 37 passed → 38 passed；覆盖句补所属者 200）
- `README.md`；`practice/19-project-pack/`；`practice/16-pytest-regression/`（同一套 pytest 门闩，不改会红）
- `chapters/16-pytest.md`、`16a-pytest-basics.md`、`16b-pytest-fixtures.md`；`practice/README.md`、`practice/STATUS.md`、`practice/run.py`
- `chapters/quizzes/stage-6-project.md` Q6 审查数字
修改位置：`test_order_forbidden_other_user` 之后；第 19 章 19.1/19.4/19.8/练习 3/门槛/总结/可运行性；实操 16-1 / 19-1 判定串
原内容：（摘录）

```
pytest 仅有 test_order_forbidden_other_user → 403
37 passed, 1 xfailed；收集 38
practice 19-1：checks["passed_37"] = "37 passed" in text
```

修复后内容：（摘录）

```
def test_owner_can_read_own_order(...):
    ... GET /api/orders/{id} ...
    assert mine.status_code == 200
    assert body["id"] == order_id
    assert body["items"] == [{"sku": "SKU-DEMO-003", "qty": 1}]
    assert "status" not in body

TC-PERM-002 所属者读自己的订单 | 200，body 有 id 与 items，无 status
38 passed, 1 xfailed；收集 39 = 38 + 1 xfail
```

为什么这样修：权限测试允许/拒绝成对。只加一条 passed，不拆、不改 xfail（仍是 BUG-001 `strict=True` 一条）。未改 `server.py`。
依据：PRD R-PERM；OpenAPI `GET /api/orders/{id}` 200「id and items, no status」；ISTQB 访问控制成对。
是否影响其他章节：第 16 章作业/16-1 与仓库基线同一数字，已同步为 38/1。第 20/21 章仍写「审查记录 37」，并注明以本机为准；未整章改面试/求职文。`09-pytest-report.png` 仍是旧截图，需 Coordinator 重截。
验证结果：`cd project/minishop && .venv/bin/python -m pytest -q` → **38 passed, 1 xfailed**。`python3 practice/run.py 16-1` 与 `19-1` 退出 0；两套 `tests/test_lab.py` unittest OK。xfail 仍只 `test_empty_keyword_should_not_return_all`。
状态：FIXED
