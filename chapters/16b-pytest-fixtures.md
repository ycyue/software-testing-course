# 第 16 章（下）：fixture、参数化与 MiniShop 自动化

> **一句话核心：** fixture 负责准备观察所需的前置，不负责发明判定。

> 重要级别：⭐⭐⭐ 必须掌握  
> 核心章节发布目标：≥95/100  
> 上一节：[16A pytest 基础](16a-pytest-basics.md)

## 这一章解决什么问题

把 token 和 base_url 从每条测试里抽出来，用 parametrize 覆盖数量和四态。工作实战是读懂并跑 `project/minishop/tests/`，不要另写一台 `/login` 教学服务。

## 学习目标

- 用 fixture 注入 `base_url` 和 `token_a`；
- 401 用例不要 autouse token；
- 用 parametrize 覆盖数量与四态；
- 读 `pytest.ini` 的 `testpaths`。

## 前置知识

已完成 16A。

## 场景导入

每条测试都自己登录一次，token 写得到处都是。fixture 把前置抽出来；parametrize 把 qty=1/10/11 和缺字段四态展开。抽错了也会出事：`autouse` 登录后再测 401，往往测脏。仓库 `conftest.py` 里 `token_a` **没有** autouse；另有 `reset_seed_db` 是 autouse，用来把库打回种子，不是拿来测 401 的。

## 16.6 fixture 与 scope ⭐⭐⭐

![fixture 准备环境，parametrize 展开数据](assets/diagrams/ch16-fixture.png)


**fixture** 是测试运行前（或后）准备好的东西：地址、账号、token。测试函数写同名参数，pytest 会注入。下面是**片段**，完整 `conftest.py` 见实战。

```python
import os

import pytest
import requests

TIMEOUT = 5


@pytest.fixture
def base_url():
    url = os.environ.get("MINISHOP_BASE_URL", "http://127.0.0.1:8765")
    return url.rstrip("/")
```

`test_login_ok(base_url)` 并不需要你手动调用 `base_url()`。仓库套件自己起临时端口，见 `tests/conftest.py`。

| scope | 何时创建一次 | 适用 |
| --- | --- | --- |
| `function` | 每个测试（默认） | 入门默认；隔离最好 |
| `class` | 一个测试类 | 本章不用 class |
| `module` | 该文件 | 文件内共享只读配置 |
| `package` | 包 | ⭐ 了解 |
| `session` | 整次 pytest | 登录贵、启动服务 |

`token_a` 用默认 `function` 最稳：每个需要它的测试自己登录一次。登录很慢时再改为 `scope="session"`。不要把 `token_a` 设成 `autouse=True`：无凭证用例也会先多打一次登录；若再共用 `requests.Session` 或自动带上 Cookie，401 就会测脏。仓库里 `token_a` 只 `return` 字符串，不会自动粘到没有声明该参数的请求上，但不要依赖这种巧合。

需要收尾时用 `yield`：`yield` 之前是准备，之后是清理。`token_a` 直接 `return` 字符串即可。

fixture 里的 `assert` 失败算 **setup 错误**，测试函数体还没执行。先看是环境（服务没启动）还是业务断言失败。

---

## 16.7 conftest.py ⭐⭐⭐

`conftest.py` 专门放本目录及子目录都能用的 fixture。它**不会**被当成测试模块收集。

项目根目录放一份即可。测试函数仍写在 `tests/test_*.py`。不要在 `conftest.py` 里写 `test_` 函数。

同一 fixture 名在测试文件里再定义，会覆盖更外层的定义。入门阶段保持一层 `conftest.py`，避免同名打架。

---

## 16.8 Token fixture ⭐⭐⭐

![401 用例不要先自动登录](assets/diagrams/ch16-no-autouse.png)


下面两段是**片段**，须放进 `conftest.py` / `tests/test_api.py`，不能单独当脚本执行。仓库里 fixture 名叫 `token_a`。

```python
import pytest
import requests

TIMEOUT = 5


@pytest.fixture
def token_a(base_url):
    response = requests.post(
        f"{base_url}/api/login",
        json={"phone": "13800138000", "password": "Test1234"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    value = response.json().get("token")
    assert type(value) is str and value != ""
    return value
```

需要认证的测试声明 `token_a` 参数：

```python
def test_create_order_returns_id(base_url, token_a):
    response = requests.post(
        f"{base_url}/api/orders",
        json={"sku": "SKU-DEMO-003", "qty": 1},
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=5,
    )
    assert response.status_code == 201
    body = response.json()
    assert "id" in body
    assert "status" not in body
```

无凭证用例**不要**声明 `token_a`，也不要复用 `requests.Session` 里已经存下的 Cookie 来“顺便”带登录态——除非你在测 Cookie 认证。MiniShop 购物车和订单看的是 Bearer。Cookie 与 Bearer 可同时出现在登录响应里。

---

## 16.9 parametrize：数据驱动 ⭐⭐⭐

同一检查逻辑、多组输入，用 `@pytest.mark.parametrize`，不要复制六个几乎一样的函数。须与 `base_url` fixture 一起由 pytest 收集。

```python
import pytest
import requests

TIMEOUT = 5


@pytest.mark.parametrize(
    "body, status",
    [
        ({"sku": "SKU-DEMO-001", "qty": 1}, 200),
        ({"sku": "SKU-DEMO-001", "qty": 10}, 200),
        ({"sku": "SKU-DEMO-001", "qty": 11}, 400),
        ({"sku": "SKU-DEMO-001"}, 400),
        ({"sku": "SKU-DEMO-001", "qty": None}, 400),
        ({"sku": "SKU-DEMO-001", "qty": ""}, 400),
        ({"sku": "SKU-DEMO-001", "qty": "1"}, 400),
        ({"sku": "SKU-DEMO-001", "qty": 0}, 400),
    ],
    ids=["ok", "eq_stock", "over_stock", "missing", "null", "empty_str", "wrong_type", "zero"],
)
def test_cart_qty_cases(base_url, token_a, body, status):
    response = requests.post(
        f"{base_url}/api/cart/items",
        json=body,
        headers={"Authorization": f"Bearer {token_a}"},
        timeout=TIMEOUT,
    )
    assert response.status_code == status
```

`ids` 出现在收集列表和失败报告里，比默认的 `[body0]` 好读。仓库 `tests/test_api.py` 就是这张表：含 `qty=10` → 200，且带 Bearer。

一次只变一个主要无效条件，与第 13 章一致。购物车**必须**带 Bearer，无凭证是另一条 401，不要和四态叠在一起。

从 JSON 文件读用例也可以，本质仍是 parametrize 的数据来源。先把表写在装饰器里。

---

## 16.10 目录结构与基础配置 ⭐⭐⭐

仓库目录（不要另造 `teach_server.py`）：

```text
project/minishop/
  pytest.ini
  tests/
    conftest.py
    test_api.py
    test_register.py
    test_qty_rule.py
```

`pytest.ini`：

```ini
[pytest]
testpaths = tests
addopts = -ra
```

`testpaths` 限制搜索目录。`-ra` 在结束时多打印跳过等原因（本章用得少，但报告更完整）。

有的项目把配置写在 `pyproject.toml` 的 `[tool.pytest.ini_options]`。pytest 9 还认识 `pytest.toml`。入门用 `pytest.ini` 即可；遇到空的 `pytest.ini` 时，它仍会成为配置来源，不要留一个空白文件在仓库里干扰其他配置。

常用命令：

```bash
python3 -m pytest
python3 -m pytest -q
python3 -m pytest --collect-only -q
python3 -m pytest -k login
python3 -m pytest tests/test_api.py
```

`-k login` 按名字过滤。`--collect-only` 只看收集到哪些测试，不发请求。

需要把项目根目录加入导入路径时，可在 ini 里设 `pythonpath = .`。本章示例把辅助函数写在测试文件或 `conftest.py`，不必先上这条。

---


配套可运行实操：[实操 16-1 pytest 基线](../practice/16-pytest-regression/README.md)（先 `python3 project/minishop/run.py setup`，再 `python3 practice/run.py 16-1`）。37 passed / 1 xfailed 对应 BUG-001 仍开放。

## MiniShop 工作实战：读仓库 pytest 包 ⭐⭐⭐

不要复制一份 `teach_server.py`。对端就是 MiniShop，测试已经在 `project/minishop/tests/`。保存说明：

```text
exercises/chapter-16-minishop-pytest.md
```

先跑：

```bash
cd project/minishop
python3 run.py setup
python3 run.py test
```

预期摘要：`37 passed, 1 xfailed`。然后打开三个文件，用自己的话写下来：

1. `tests/conftest.py`：`base_url` 怎样起临时端口；`token_a` 为什么不是 autouse；`reset_seed_db` 是干什么的。
2. `tests/test_api.py`：`test_cart_qty_cases` 为什么 `qty=10` 是 200、购物车为什么带 Bearer。
3. `tests/test_register.py`：合法注册为什么是 201、没有 token。

可选加分：在练习目录**复制** `test_qty_rule.py` 的纯函数思路，加一条你自己的边界（不要改仓库里正在跑的套件，除非你在做第 19 章项目）。

完成标准：

1. 本机 `run.py test` 数字能指出来（37 / 1，或以你最新输出为准）；
2. 能解释 xfail 对应 BUG-001，不是「全绿」；
3. 能指出购物车八组 parametrize 里 `eq_stock` 和 `over_stock`；
4. 能说明无 Bearer 下单是 401、他人订单是 403；
5. 不另造 `/login` 教学服务。

记录模板：

```markdown
# MiniShop pytest 记录

## 环境
- Python / pytest / requests 版本：
- 命令：`python3 run.py test`
- 日期：

## 结果
- 收集条数：
- passed / xfailed：
- xfail 对应哪个缺陷：

## 我读懂的三处
- conftest：
- 购物车 parametrize：
- 注册：
```

---


仓库正式结果（2026-09-09）：`37 passed, 1 xfailed`。输出：`project/minishop/evidence/pytest-output.txt`。HTML 报告：`evidence/pytest-report.html`。

## 常见错误

### 错误 1：给 401 用例 `autouse` `token_a`

修正：会先多登录一次；若再共用 Session 或 Cookie，就测不到未认证。需要 token 的测试显式写参数。

### 错误 2：把 xfail 说成全绿

修正：仓库套件是 37 passed / 1 xfailed。xfail 对应仍开放的 BUG-001，不是「没有缺陷」。

### 错误 3：fixture 里写判定，parametrize 里准备环境

修正：fixture 准备观察所需的前置，不负责发明判定。购物车八组 Body 用 parametrize 展开。

### 错误 4：两次下单成功却去断言订单 `status`

修正：v1.0 下单成功只保证 `id`。默认不幂等：两个 id。没有状态机。

## 面试角度 ⭐⭐⭐

### fixture 和 parametrize 各干什么？

结论：fixture 准备环境，parametrize 展开数据。  
示例：`base_url` / `token_a` 用 fixture；购物车 `qty=10/11` 与缺字段、null、空串、错误类型用 parametrize（须带 Bearer）。  
边界：不要用 autouse token 去测 401。

### 仓库 37/1 能说成没有缺陷吗？

结论：不能。1 条 xfail 跟踪仍开放的 BUG-001。  
示例：`python3 run.py test` → 37 passed, 1 xfailed。  
边界：简历里只写仓库里能指出来的数字，并以本机最新输出为准。

### 连续两次创建订单，自动化应断言什么？

结论：两次都 201、两个不同 `id`、Body 没有 `status`。  
边界：若以后需求改成幂等，再改期望，不要现在编状态机。

## 小练习

题号跨上下册：本节为 5～10；其余在 16A。

### 练习 5

`token_a` fixture 的默认 scope 是什么？为什么 401 用例不能 `autouse` 这个 fixture？

### 练习 6

`conftest.py` 会被当成测试文件收集吗？公共 `base_url` 应放哪？

### 练习 7

用一句话区分 fixture 与 `@pytest.mark.parametrize`。购物车 qty 与四态应主要用哪一个？

### 练习 8

连续两次 `POST /api/orders` 得到两个 `id`，自动化应断言什么？不要写订单状态名。

### 练习 9

哪一句正确？

A. 接口自动化 ROI 永远高于 UI  
B. Cookie、Session、Token 是三种 pytest 插件，三选一  
C. `requests.post(..., json={...})` 发送 JSON Body  
D. GET 比 POST 安全，所以登录必须用 GET

### 练习 10

列出 MiniShop 登录测试最少要断言的 4 项（含一项失败密码）。密码如何提供？不要写订单状态名。


## 练习答案

5. `function`。`autouse` 会让无凭证测试先多登录一次；若再共用 Session 或 Cookie，就测不到 401。需要 token 的测试显式写参数（仓库里是 `token_a`）。

6. 不会。放在项目或 `tests` 目录的 `conftest.py`。

7. fixture 准备环境，parametrize 展开数据。购物车 qty / 四态用 parametrize。

8. 两次都成功创建且 `id` 不同（v1.0 默认不幂等）。若正式需求只允许一笔，再按正式文档改期望。

9. C。A 违反 ROI 绝对化；B 把认证层次说成插件；D 是 GET/POST 安全神话。

10. 状态码 200、`result=ok`、token 为非空字符串、错误密码 401。密码用仓库教学账号 `Test1234`，只许本机，不入库。合理四项即可。

---


## 本章检查清单

- [ ] 我会用 fixture 和 parametrize
- [ ] 我知道 401 不要 autouse token
- [ ] 我能解释 37 passed / 1 xfailed，不会说成全绿
- [ ] 我能跑通 `python3 run.py test`

## 本章总结

fixture 准备前置，parametrize 展开数据。401 不要 autouse token。仓库基线是 37 passed / 1 xfailed。

## 阶段测验

[阶段测验 5](quizzes/stage-5-api.md)

## 本章可运行性说明

`python3 run.py test` 本机 2026-09-09：37 passed, 1 xfailed。对端是 `project/minishop`，没有第二套 `/login` 教学服务。

## 参考资料

- [16A](16a-pytest-basics.md)
- `project/minishop/evidence/pytest-output.txt`

## 下一章预告

第 17 章《自动化测试进阶概览》。
