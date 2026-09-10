# VERIFY_CODE — Verification-Agent-02

日期：2026-09-10  
范围：代码 / SQL / 命令独立复跑  
约束：**未改教材**（未写 `chapters/`、`practice/`、`project/`）。只写入本文件。  
先前 `FIX_*.md` / 审计报告只作线索，结论全部来自本轮命令与文件读取。

## 总表

| # | 检查项 | 结果 |
| --- | --- | --- |
| 1 | `python3 practice/run.py 2-1` 应说明书面实操 | **PASS** |
| 2 | `python3 practice/run.py 1-1 --check` | **PASS** |
| 3 | MiniShop pytest：38 passed, 1 xfailed；有 `test_owner_can_read_own_order` | **PASS** |
| 4 | Postman JSON：无凭证创建 `disableCookies`；`lastOrderId` | **PASS** |
| 5 | 12.12 INSERT 在事务里；抽跑 sqlite3 PRAGMA 说明存在 | **PASS** |
| 6 | 13.12 可抄报文含 `Content-Length` | **PASS** |
| 7 | `get_by_role` 表 | **PASS** |

**7/7 PASS。** 本轮未发现需回退的代码/SQL/命令缺口。

---

## 1. `python3 practice/run.py 2-1` 说明书面实操 — PASS

**命令（仓库根）：** `python3 practice/run.py 2-1`  
**退出码：** 2（无脚本、未启动程序；与 `print_no_script()` 设计一致）

**stdout（全文）：**

```
2-1 是书面实操（📖），没有可运行脚本。
python3 practice/run.py 2-1 不会启动任何程序，也不能代替你写或点 GUI。
打开：chapters/02-software-development-process.md
小节：2.8 MiniShop 工作实战
产出写入 exercises/。完整清单见 practice/README.md.
```

判定：不再打印「没有编号 2-1」。明确类型（书面 📖）、不会启动程序、给出打开路径与小节。`chapters/02-software-development-process.md` 存在。

---

## 2. `python3 practice/run.py 1-1 --check` — PASS

**命令（仓库根）：** `python3 practice/run.py 1-1 --check`  
**退出码：** 0

实际调用：

```
python3 -m unittest discover -s …/practice/01-observation-oracle-evidence/tests -v
```

结果：

```
test_full_writes_evidence_and_flags_bug ... ok
test_observe_has_no_verdict ... ok
test_oracle_sends_no_request ... ok
Ran 3 tests in 1.049s
OK
```

3 条 unittest 全绿。

---

## 3. MiniShop pytest 38 passed / 1 xfailed + 所属者用例 — PASS

**命令：** `cd project/minishop && .venv/bin/python -m pytest -q --tb=line`

```
.......................x...............
XFAIL tests/test_api.py::test_empty_keyword_should_not_return_all - BUG-001 empty keyword returns full catalog
38 passed, 1 xfailed in 1.10s
```

收集：`39 tests collected` = 38 passed + 1 xfailed。

`tests/test_api.py::test_owner_can_read_own_order` 在收集清单中。单独复跑：

```
.venv/bin/python -m pytest tests/test_api.py::test_owner_can_read_own_order -q
1 passed in 0.59s
```

源码断言：所属者 `GET /api/orders/{id}` → 200；`id` 一致；`items == [{"sku":"SKU-DEMO-003","qty":1}]`；`"status" not in body`。xfail 仍只 BUG-001。

注意：在仓库根直接 `python3 -m pytest` 会因多个 `tests/test_lab.py` 同名收集失败。教材入口是 `cd project/minishop`（`pytest.ini` `testpaths = tests`），本轮按该入口复跑。

---

## 4. Postman JSON：无凭证创建 disableCookies；lastOrderId — PASS

文件：

- `project/minishop/postman/MiniShop.postman_collection.json`
- `project/minishop/postman/MiniShop.postman_environment.json`

`json.loads` 成功。Collection v2.1；**15** 条请求。

「无凭证创建」：

- `protocolProfileBehavior.disableCookies === true`
- Header 仅 `Content-Type: application/json`
- 无 `Authorization`，request 无 `auth` 字段
- URL：`{{baseUrl}}/api/orders`

`lastOrderId`：

- 环境 keys 含 `lastOrderId`，**不含** `orderId`
- 「创建订单」脚本：`pm.environment.set('lastOrderId', json.id);`
- 「越权-他人订单」「越权-管理员读明细」URL：`{{baseUrl}}/api/orders/{{lastOrderId}}`
- 集合全文 `lastOrderId` 出现 4 次，`orderId` 出现 0 次
- `chapters/14-postman.md` 检索环境变量名 `orderId`：无命中

---

## 5. 12.12 INSERT 在事务里；sqlite3 PRAGMA 说明存在 — PASS

### 5.1 教材可抄块

`chapters/12b-sql-write-and-minishop.md` §12.12 可复制 SQL 为：

```sql
PRAGMA foreign_keys = ON;
BEGIN;
… SELECT …
INSERT INTO cart_items (user_id, product_id, qty) VALUES (1, 3, 1);
… SELECT …
ROLLBACK;
```

耳机 INSERT 包在 `BEGIN`/`ROLLBACK` 内，不是裸自动提交。

PRAGMA 说明（按连接、不进文件）存在于：

- `chapters/12a-sql-query.md` §12.3、§12.4、§12.6
- `chapters/12b-sql-write-and-minishop.md` §12.12 段首与失败 INSERT 块

### 5.2 独立抽跑（sqlite3 3.43.2；临时库 `/tmp/verify-code-pragma-20260910.sqlite`，未碰教学文件 / MiniShop 主库）

按 12.4 DDL 建库（建库连接 `PRAGMA foreign_keys = ON`）。

| 实验 | 结果 | 与教材 |
| --- | --- | --- |
| 新连接 `PRAGMA foreign_keys;` | `0` | 开关不写入文件 |
| 新连接、不写 PRAGMA，`INSERT … VALUES (99,1,1)` | 成功，id=4 | 默认不强制外键 |
| 清掉幽灵行后，新连接先 `ON` 再插 99 | `FOREIGN KEY constraint failed (19)`，退出 1 | 12.12 审查句 |
| 12.12 事务内插耳机 `(1,3,1)` 再 `ROLLBACK` | 事务内可见 1 行；回滚后 `cart_items` 仍 3 行；user 1 × product 3 为 0 | INSERT 在事务里可回退 |
| 回滚后 LEFT JOIN `SKU-DEMO-003` qty | 空 | 练习 7「003 数量为空」不被污染 |
| `sqlite_master` 含 PRAGMA 的 sql | 无 | 说明不进 schema |

---

## 6. 13.12 可抄报文含 Content-Length — PASS

`chapters/13-api-testing.md` §13.12 请求围栏：

```text
POST /api/login HTTP/1.1
Host: 127.0.0.1:8765
Content-Type: application/json
Content-Length: 45

{"phone":"13800138000","password":"Test1234"}
```

Body UTF-8 / ASCII 长度均为 **45**，与纸面 `Content-Length: 45` 一致。围栏后说明：`curl -d` 会自动加长度；裸 TCP 必须自己写；RFC 9112 用 CL 或 TE 标明请求体。

---

## 7. `get_by_role` 表 — PASS

`chapters/17-automation-overview.md` §17.4 对照表「定位」行：

> 推荐 Python：`get_by_role` / `get_by_label` / `get_by_test_id`（JS 文档写作 `getByRole` 等，pytest 里不要照抄 camelCase）

同节示例：`page.get_by_role("button", name="登录").click()`。表内 `getByRole` 仅作 JS 文档名，不是可抄 Python API。

本机 `playwright.sync_api.Page` 内省：

| 属性 | hasattr |
| --- | --- |
| `get_by_role` / `get_by_label` / `get_by_test_id` | True |
| `getByRole` / `getByLabel` / `getByTestId` | False |

按表现抄 snake_case 可定位；抄 camelCase 会 `AttributeError`。表与 API 一致。

---

## 执行记录

| 命令 | 结果摘要 |
| --- | --- |
| `python3 practice/run.py 2-1` | 书面实操说明；exit 2 |
| `python3 practice/run.py 1-1 --check` | 3 tests OK；exit 0 |
| `cd project/minishop && .venv/bin/python -m pytest -q` | 38 passed, 1 xfailed |
| 同上 `--collect-only -q` | 39 collected，含 `test_owner_can_read_own_order` |
| 同上 `tests/test_api.py::test_owner_can_read_own_order` | 1 passed |
| `python3 json.loads` 两份 Postman JSON | 合法；15 条；disableCookies；lastOrderId |
| `sqlite3` 临时教学库 PRAGMA / INSERT 事务 | 见 §5.2 |
| Body 字节长度 vs 13.12 CL | 45 = 45 |
| Playwright `Page` hasattr | snake_case True，camelCase False |

读取未改：`practice/run.py`；`project/minishop/tests/test_api.py`；两份 Postman JSON；`chapters/12a-sql-query.md`、`12b-sql-write-and-minishop.md`、`13-api-testing.md`、`17-automation-overview.md`。

未启动长期 `run.py serve`；pytest 用 `conftest` 临时库 + 随机端口。sqlite3 只用 `/tmp` 副本。
