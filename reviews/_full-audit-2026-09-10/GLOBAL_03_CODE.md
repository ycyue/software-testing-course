# Global-03 Code & Command Audit

日期：2026-09-10  
Agent：Global-Agent-03（代码与命令，独立取证）  
范围：`chapters/*.md` 可执行围栏（python/bash/sql/json/javascript/yaml/html/css/ini/http-text）、`practice/**/*.py`、`project/minishop`（`server.py` / tests / `run.py` / Postman JSON / `.jmx`）  
硬约束：未改教材。可运行项在 `/tmp/g03-audit-ws` 副本执行（practice 写 `validation/latest.json` 不碰原仓库）。

结论先说：**仓库里声明可跑的主线（practice 1-1…19-1、MiniShop pytest 37 passed / 1 xfailed、第 15 章完整脚本、第 12 章 sqlite3 CLI、第 15A 片段输出）与教材声称一致。没有 P0 假规则或不可启动的核心实现。P1 集中在「学生会复制的命令/脚本」与 MiniShop 实装/集合资产对不上：`keyword=mouse` 空列表、纸面 HTTP/1.1 缺 `Content-Length`、Postman Cookie 罐把 401 打成 201、`orderId`/`lastOrderId`。Chapter Agent 的这几条独立复现成立。新发现主要是 `run.py evidence` 的 `or True` 会写回 `chapters/assets/`、13.13 `TOKEN=$(curl -D)` 相邻陷阱、11.6 grep 工作目录、12.12 INSERT 无 ROLLBACK。**

---

## 1. Coverage

| 类型 | 清单数量 | 已检查 | 未检查 |
| --- | ---: | ---: | ---: |
| chapters 代码围栏合计 | 252 | 252 | 0 |
| 其中 python | 47 | 47（compile 全 OK；能独立跑的对照了声称输出） | 0 |
| 其中 bash | 44 | 44（危险命令只静态审；curl/git/grep/ls 实跑） | 0 |
| 其中 sql | 19 | 19（sqlite3 CLI 3.43.2） | 0 |
| 其中 javascript | 8 | 8（`node --check` 全 0） | 0 |
| 其中 json | 5 | 5（`json.loads`） | 0 |
| 其中 html / css / ini / yaml | 2 / 1 / 1 / 1 | 全部 | 0 |
| HTTP 报文（text 围栏） | 见第 9/13 章 | 对照 MiniShopLab + 裸 socket | 0 |
| `practice/**/*.py` | run.py + `_http.py` + `_minishop.py` + 10×main + 10×test_lab | 全部读 + 实跑 | 0 |
| MiniShop `server.py` / tests / `run.py` | 全文件 | 读 + pytest + HTTP 矩阵 | 0 |
| Postman collection + environment | 2 JSON | schema/脚本/对照 server | 0 |
| `jmeter/*.jmx` | 1 | XML 完好；**未装 JMeter GUI** | GUI 未跑（见矩阵） |
| OpenAPI | `docs/openapi.json` | 路径对照 server | 0 |
| 前端 `index.html` / `app.js` / `admin.html` | 3 | 读；HTTP 层对照 | 未开浏览器点击 |

围栏语言分布与 `UNIT_INVENTORY.md` 一致：text 82、python 47、bash 44、mermaid 23、markdown 19、sql 19、javascript 8、json 5、html 2、css/ini/yaml 各 1。

---

## 2. 执行矩阵

副本：`/tmp/g03-audit-ws`（`rsync`，`.venv` 符号链接到原 `project/minishop/.venv`）。解释器：Python 3.14.3；venv 内 pytest 9.1.1、requests 2.34.2、pytest-html 4.2.0；sqlite3 CLI 3.43.2；curl 系统自带。

| # | 命令 / 片段 | 结果 | 与教材声称 |
| --- | --- | --- | --- |
| E01 | `python3 practice/run.py --list` | EXIT 0，列出 1-1…19-1 + 书面 4-1/6-1 | 一致 |
| E02 | `python3 practice/run.py 4-1` | EXIT 0，「书面实操…打开 practice/04-requirement-review/README.md」 | 一致 |
| E03 | `python3 practice/run.py 99-9` | EXIT 2，「没有编号」 | 一致（失败路径） |
| E04 | `python3 practice/run.py 1-1` | EXIT 0；空白 keyword → HTTP 200、3 件；结论 BUG-001 仍开放 | 一致 |
| E05 | `1-1 --check` | 3 tests OK | 一致 |
| E06 | `5-1` / `--check` | qty=10 → 200 `qty=10`；qty=11 → 400 `qty exceeds stock`；2 tests OK | 一致 |
| E07 | `8-1` / `--check` | 下单 201；B 读 A → 403；自己 200；用户 admin 403；管理员 200 | 一致 |
| E08 | `9-1` / `--check` | POST `/api/login` 200，有 token 与 Set-Cookie | 一致 |
| E09 | `11-1` / `--check` | HTTP 400 + 日志 `inventory reject … qty=11` | 一致 |
| E10 | `12-1` / `--check` | API qty=2 且 SQL JOIN qty=2 | 一致（临时库，退出即删） |
| E11 | `13-1` / `--check` | missing/null/empty/wrong_type 全 400，error 字符串与 `server.py` 一致 | 一致 |
| E12 | `15-1` / `--check` | 3 件，鼠标 stock=10 | 一致 |
| E13 | `16-1` / `--check` | `37 passed, 1 xfailed`；xfail = `test_empty_keyword_should_not_return_all` | 一致 |
| E14 | `19-1` / `--check` | PRD/BUG-001/OpenAPI/Postman 文件 OK；pytest 仍 37/1 | 一致 |
| E15 | `project/minishop/.venv/bin/python -m pytest -q` | **38 collected；37 passed, 1 xfailed**；EXIT 0 | 与第 16/19 章、`evidence/pytest-output.txt` 一致 |
| E16 | 仓库根 `python3 -m pytest --collect-only -q` | **9 errors**：`practice/*/tests/test_lab.py` 模块同名 `import file mismatch` | 教材 16.10 未写 cwd；与声称「pytest 一打就绿」不一致（见 G03-0007） |
| E17 | 第 15A 全部 python 围栏 | compile OK；有 print 的声称输出 **全部 MATCH**（含 `qty_allowed` 四行、可变默认参数、`set_not_json`） | 一致 |
| E18 | 第 18.4 `samples_ms` | 打印 `266.0` / `120` / `800` | 与正文数字一致；**没有算出 P95**（章标题概念，见 G03-0012） |
| E19 | 15.10 `open("cart_cases.json")` 单独跑 | `FileNotFoundError` | 正文把输出写成 `list 8 合法数量`，文件在 15.12 才给（G03-0010） |
| E20 | 15.12 `check_minishop_data.py` + 同目录 `cart_cases.json` | EXIT 0：`token_ok` / `over SKU-DEMO-002` / `cases_ok 8` | **一致** |
| E21 | 16A `tests/test_qty_allowed.py` 两断言 | `2 passed` | 一致 |
| E22 | 16A `test_fail_demo` | FAILED `assert 11 <= 10` | 与声称失败信息一致 |
| E23 | 16A `requests.get(127.0.0.1:8765/…)` 服务未启动 | `ConnectionError` | 正文已警告，不是断言失败 |
| E24 | 12.4 教学库 + 全部 SELECT/JOIN/NULL（sqlite3 CLI） | user_count=3；named_count=2；qty_sum=4；AVG=6.0；MIN/MAX=3/10；`= NULL` 0 行；`IS NULL` 用户 3；BETWEEN 键盘+耳机；LIMIT2 鼠标再键盘；JOIN 两行；LEFT JOIN 耳机 qty 空；qty>stock 0 行 | **与「审查结果」数字一致** |
| E25 | 12.13 `BEGIN…ROLLBACK` 库存 10→9→10 | CLI 一致 | 一致 |
| E26 | 12.13 DELETE ROLLBACK | id=2 qty=2 仍在 | 一致 |
| E27 | 12.16 事务内 qty=11 再 ROLLBACK | 事务内 11/10，回滚后 1 | 一致 |
| E28 | `TRUNCATE TABLE products` | `near "TRUNCATE": syntax error` | 与 12.14「SQLite 没有 TRUNCATE」一致 |
| E29 | `PRAGMA foreign_keys=ON` 后 `user_id=99` INSERT | `FOREIGN KEY constraint failed` | 与 12.12 审查句一致 |
| E30 | 12.12 INSERT 耳机 **无 ROLLBACK** | 提交后多一行 id=4 | 散文要求放进事务，**可复制 SQL 会永久留下**（G03-0009） |
| E31 | MiniShopLab `GET /api/products` | HTTP **1.0** 200；`Content-Type: application/json; charset=utf-8`；3 件 | 课文写 HTTP/1.1、无 charset（G03-0003） |
| E32 | `?keyword=mouse` | 200 `{"items":[]}` | 第 11 章「最小读取」未声明空列表（G03-0002） |
| E33 | `?keyword=SKU-DEMO-001` / 百分号编码「鼠标」 | 200，1 件 | 搜索实现正确 |
| E34 | 请求行未编码 `keyword=鼠标` | `HTTP/1.0 400 Bad request syntax` | 与 CH11 描述同向 |
| E35 | 裸 socket 登录 **无 Content-Length** | HTTP/1.0 400 | 第 13 章可抄报文缺该头（G03-0003） |
| E36 | 同样 Body **有 Content-Length** | HTTP/1.0 200，Body 含 `result/token/role`，Set-Cookie `HttpOnly; Path=/` | curl 能过是因为 curl 自动加长度 |
| E37 | `POST /login`（无 `/api`） | 404 `not found` | 与「不要抄 /login」一致 |
| E38 | 错误密码 | 401 `{"result":"fail"}` | 一致 |
| E39 | 仅 Cookie、无 Bearer：`GET /api/cart` | **200** | R-AUTH「Cookie 可并存」成立 |
| E40 | 仅 Cookie、无 Bearer：`POST /api/orders` | **201** 有 id | Postman「无凭证创建」默认 Runner 会绿不了 401（G03-0001） |
| E41 | 无任何凭证下单 | 401 `unauthorized` | 一致 |
| E42 | qty=10 / 11 | 200 / 400 `qty exceeds stock` | 一致 |
| E43 | 四态 + 无 sku | missing qty / null qty / wrong type / wrong type / **missing sku** | 13-1 带 sku 的四态对；图若缺 sku 则对不上（同意 CH13-0001） |
| E44 | 未知 sku | 404 `unknown sku` | OpenAPI `/api/cart/items` 未列 404（P3） |
| E45 | 错误 `Content-Type` + JSON 字节 | 购物车 **仍 200** | MiniShop 不读 Content-Type（同意 CH13-0005） |
| E46 | 连续两单 | 两个 201、不同 `id`、无 `status` | 一致 |
| E47 | `GET /api/orders/`（空 id，模拟未写入的 `{{lastOrderId}}`） | 404 | 同意 CH14-0002 |
| E48 | 第 13 章 `TOKEN=$(curl … \| python json.load)`（**无 -D**） | 下单 201 | 该块本身可跑 |
| E49 | 把上一例的 `-D -` 拼进 TOKEN 管道 | `json.JSONDecodeError`（stdin 先是 HTTP 头） | 相邻示例陷阱（G03-0005） |
| E50 | `curl -sS -D - …/api/login` | 首行 `HTTP/1.0 200 OK`，有 HttpOnly | 证据文件同形态 |
| E51 | `ls --help`（macOS BSD） | `unrecognized option '--help'` | 11.1 已声明，不单开 ISSUE |
| E52 | 仓库根 `grep … evidence/logs/app-sample.log` | 文件不存在 | 11.6 未给 cwd（G03-0008） |
| E53 | `cd project/minishop && grep -n "inventory reject" evidence/logs/app-sample.log` | 命中 INFO 行，含 qty=11 | 一致 |
| E54 | 第 2 章 git 最小流（`/tmp` 独立目录） | init/add/commit 成功 | 一致（课程仓库内应按正文跳过 init） |
| E55 | Postman / OpenAPI / 环境 JSON | `json.loads` OK；集合 **15** 条；环境 `lastOrderId`；`password` 当前值为空 | JSON 合法 |
| E56 | `node --check` 全部 JS 围栏 | 全 0 | 语法合法（`pm` 是沙箱全局，静态检查不执行） |
| E57 | YAML CI 示例 | PyYAML 解析 name=`minishop-api-tests` | 语法合法；变量名/目录不对（G03-0013） |
| E58 | `pytest.ini` | 与 16B 围栏逐字相同：`testpaths=tests` `addopts=-ra` | 一致 |
| E59 | `.jmx` `ElementTree` | XML 完好；`functional_mode=true`；**无 `ResponseAssertion` 元件**（仅 saveConfig 里有 `<assertions>`） | 结构问题见 G03-0011；**未装 jmeter，GUI 未跑** |
| E60 | Playwright `Page` 内省 | `get_by_role/label/test_id=True`；`getByRole/Label/TestId=False` | 同意 CH17-0004 |
| E61 | `token` 登录后 `reset_db` 再打购物车 | **401** | 同意 CH16-0004（session-scoped token 不能和 autouse 清库共存） |
| E62 | `server.qty_allowed` / `valid_phone` / `valid_password` | 与 15A/注册测试同向 | 一致 |
| E63 | 未跑 | `python3 run.py evidence`（会写 `evidence/` 与 `chapters/assets/`）；JMeter GUI；Postman Runner GUI；`ssh tester@192.0.2.10`；`kill 12345` | 故意跳过 |

practice `--check` 全部 EXIT 0。MiniShop 基线锁仍然是 **37 passed, 1 xfailed（BUG-001，`strict=True`）**。

---

## 3. P0

无。

未发现把 GET/POST 安全神话、Cookie/Session/Token 三选一、P0 全球统一、没找到 Bug 就没有 Bug、测试必须等开发写完、接口 ROI 永远最高写成正说。未把 `/login`、支付、订单状态机写成 v1.0 可抄契约。`server.py` 写操作使用绑定变量。practice 用临时库，不改 `project/minishop/data/`。

---

## 4. P1

下列四条都会让「按教材复制」得到与课文 oracle 不同的观察。独立复现；与对应 Chapter Agent **同向**，不是新发明的假冲突。

### ISSUE
ID：G03-0001  
文件：`project/minishop/postman/MiniShop.postman_collection.json`；`chapters/14-postman.md`；`project/minishop/server.py`  
章节：第 14 章 + MiniShop 资产  
小节：集合「无凭证创建」；`_token()`  
精确位置：集合约 L199–207（无 Authorization、无 `disableCookies`）；`server.py` L190–199  
原文：无凭证创建应 401；完成标准「导入并跑通仓库集合（空搜索允许红）」  
问题等级：P1  
问题类别：CODE / HTTP / TEST  
问题说明：MiniShop 无 Bearer 时仍读 Cookie `minishop_session`。登录响应带 `Set-Cookie`。Postman 默认 cookie jar 会把后续「无凭证」请求变成已登录。  
为什么有问题：本轮用 Cookie、不带 `Authorization` 打 `POST /api/orders` → **HTTP 201 + `id`**。无 Cookie 才是 401。Collection Runner 默认会多一条红（401 断言失败），正文只允许空搜索红。学生会改集合、补 Bearer，或以为服务坏了。  
依据：E39–E41；PRD R-AUTH；`test_login_ok` 用 Cookie 打 `/api/cart` 得 200。Postman 支持 `protocolProfileBehavior.disableCookies`。  
建议修改：该请求加 `"protocolProfileBehavior": {"disableCookies": true}`；14.4/14.6 写明「无凭证 = 不要 Authorization **且** 关掉 cookie jar」。  
推荐替换文本：无凭证不是「这条没填 Authorization」。Postman 默认代发 `minishop_session`。仓库「无凭证创建」必须 Disable cookie jar；MiniShop 没 Bearer 时仍认 Cookie。  
对照：【同意 CH14-0001】独立复现 201。

### ISSUE
ID：G03-0002  
文件：`chapters/11-linux.md`；`chapters/14-postman.md`；`chapters/09a-network-http-semantics.md` 配图（跨章同一错误输入）  
章节：11 / 14 / 09  
小节：11.13 最小读取；14.5 列表脚本  
精确位置：11.13 `keyword=mouse`；14.5 只断言 `items` 为数组  
原文：`curl … "/api/products?keyword=mouse"`；`pm.expect(body.items).to.be.an("array")`  
问题等级：P1  
问题类别：CODE / ACC / MiniShop  
问题说明：搜索是 `keyword.lower() in name/sku`。种子名「无线鼠标」、SKU `SKU-DEMO-001`，都不含 `mouse`。  
为什么有问题：本轮 `GET ?keyword=mouse` → `200 {"items":[]}`。第 11 章把它当「最小读取」；第 14 章刚警告「只断言数组会绿」然后示例自己只断言数组。仓库集合「搜索商品」已断言 `SKU-DEMO-001`，正文脚本更弱。空数组会被当成「搜索坏了」或和 BUG-001（空白 keyword 返回 3 件）搅在一起。  
依据：E32–E33；`server.py` `_get_products`。  
建议修改：最小读取改为无 query 或 `keyword=SKU-DEMO-001`；正文列表脚本与集合对齐，命中 sku。  
推荐替换文本：`curl -sS -D - -o ./minishop-curl-body.txt "http://127.0.0.1:8765/api/products"` 预期 3 件。不要用 `keyword=mouse`。  
对照：【同意 CH11-0001 / CH14-0005 / CH09-0001】同一输入，三章重复。

### ISSUE
ID：G03-0003  
文件：`chapters/13-api-testing.md`；`chapters/09b-http-message-observe.md`  
章节：13 / 09  
小节：13.12 可抄登录报文；09B 示例  
精确位置：请求无 `Content-Length`；响应写成 `HTTP/1.1 200 OK` + `Content-Type: application/json`  
原文：见 13.12 / 09B text 围栏  
问题等级：P1  
问题类别：HTTP / CODE / ACC  
问题说明：`BaseHTTPRequestHandler.protocol_version` 默认 **HTTP/1.0**。`_read_json` 用 `Content-Length or 0` 读体。RFC 9112：无 Content-Length / Transfer-Encoding 则请求无 body。  
为什么有问题：裸 socket 按课文发送 → **400**。补 `Content-Length` → 200，Body 还有课文没写的 `role`，Content-Type 带 `charset=utf-8`，状态行是 `HTTP/1.0`。curl 能过只因为 curl 自动加长度，不是报文可照抄。核心接口章给出「按 RFC 成帧会失败」的形状。  
依据：E31、E35、E36、E50；`MiniShopHandler.protocol_version == "HTTP/1.0"`。  
建议修改：可抄请求补 `Content-Length`（或标明「curl 会自动加，裸 TCP 必须写」）；响应注明实装 HTTP/1.0、charset、`role`。  
推荐替换文本：纸面可继续写 HTTP/1.1 语义。对照 MiniShop 时看 curl 第一行 `HTTP/1.0 200 OK` 和 Body 的 `role`，不要为版本号开缺陷。  
对照：【同意 CH13-0004 / CH09-0002】。等级取 P1：这是核心章可复制报文，不是「省略头」的注释。

### ISSUE
ID：G03-0004  
文件：`chapters/14-postman.md`；`project/minishop/postman/MiniShop.postman_environment.json`；集合「创建订单」「越权-他人订单」  
章节：第 14 章  
小节：14.3 变量表；14.5 创建订单脚本  
精确位置：正文 `pm.environment.set("orderId", …)`；仓库 `lastOrderId`  
原文：表列 `orderId`；集合 `set('lastOrderId')` + `GET {{baseUrl}}/api/orders/{{lastOrderId}}`  
问题等级：P1  
问题类别：CODE / TERM  
问题说明：环境文件只有 `lastOrderId`。按正文 `set("orderId")` 后跑仓库越权请求，Path 替换为空 → 实际 `GET /api/orders/`。  
为什么有问题：本轮 `GET /api/orders/` → **404** `not found`，不是 403。越权断言整条作废。  
依据：E47；`server.py` `do_GET` 对恰好 `/api/orders/` 不进 `_get_order`。  
建议修改：正文、表、练习答案、脚本一律 `lastOrderId`。  
推荐替换文本：`pm.environment.set("lastOrderId", body.id);` 越权 URL 用 `{{baseUrl}}/api/orders/{{lastOrderId}}`。  
对照：【同意 CH14-0002】。

---

## 5. P2

### ISSUE
ID：G03-0005  
文件：`chapters/13-api-testing.md`  
章节：第 13 章  
小节：13.12 登录 curl（带 `-D -`）紧挨 13.13 `TOKEN=$(curl … | python3 json.load)`  
精确位置：L374–378 与 L391–394  
原文：登录例用 `-D -` 把头打到 stdout；TOKEN 例把 stdout 当纯 JSON  
问题等级：P2  
问题类别：CODE / PED  
问题说明：TOKEN 块本身 **无 -D，本轮可跑（E48）**。学生把「完整登录」选项拼进管道是高频动作。  
为什么有问题：本轮把 `-D -` 拼进 TOKEN 管道 → `json.JSONDecodeError`（stdin 以 `HTTP/1.0` 开头）。会误判「python 解析 token 的方法错了」。Chapter-13 审了缺 Content-Length，**没审这两块 curl 的 stdout 契约冲突**。  
依据：E48–E49。  
建议修改：TOKEN 例加一句「不要加 `-D`/`-i`；头会毁掉 json.load」。或改成 `-o body.json -D /dev/stderr`。  
推荐替换文本：取 token 时只收 Body。需要看头时另开一条带 `-D -` 的命令，不要和 `json.load(sys.stdin)` 接在同一根管道上。

### ISSUE
ID：G03-0006  
文件：`project/minishop/run.py`  
章节：第 19 章一键命令 / 工程代码  
小节：`capture_screenshots`  
精确位置：L239–241  
原文：`if assets.exists() or True:` 然后写入 `chapters/assets/<name>`  
问题等级：P2  
问题类别：CODE  
问题说明：`or True` 使条件恒真。`python3 run.py evidence` 在有 Playwright+Chrome 时会 **覆盖教材章节配图**（`01-login.png` 等），不仅写 `evidence/screenshots/`。  
为什么有问题：第 19 章把 `run.py evidence` 当取证入口。学生跑完 `git status` 会看到 `chapters/assets/*.png` 被改；也存在用一次失败截图盖掉课程配图的风险。CH19-0008 只写了 `run.py test` 覆盖 `evidence/pytest-output.txt`，**没写这条 `or True`**。本轮 **未执行 evidence**（避免改教材）。  
依据：源码 L239 `if assets.exists() or True`；`assets = ROOT.parents[1] / "chapters" / "assets"`。  
建议修改：删掉 `or True`；默认只写 `evidence/screenshots/`。同步章节配图应是作者手工步骤，不要绑在学生命令上。  
推荐替换文本：只 `page.screenshot(path=evidence/screenshots/…)`。不要写 `chapters/assets`。

### ISSUE
ID：G03-0007  
文件：`chapters/16b-pytest-fixtures.md`；`practice/*/tests/test_lab.py`  
章节：第 16 章  
小节：16.10 常用命令  
精确位置：无 `cd` 的 `python3 -m pytest`  
原文：五条 pytest 命令都不带工作目录  
问题等级：P2  
问题类别：CODE / PED  
问题说明：10 份 practice 测试模块都叫 `test_lab.py`。pytest 默认收集会 `import file mismatch`。  
为什么有问题：本轮仓库根 collect → **9 errors**（E16）。作业命令 `cd project/minishop && python3 run.py test` 是绿的。学生从仓库根模仿 16.10 会认为 pytest 坏了。  
依据：E16；practice 十份 `tests/test_lab.py`。  
建议修改：命令全部带 `cd project/minishop`，并禁止在课程根目录直接 pytest。  
推荐替换文本：见 CH16-0009。  
对照：【同意 CH16-0009 / CH17-0005】独立复现 9 errors。

### ISSUE
ID：G03-0008  
文件：`chapters/11-linux.md`  
章节：第 11 章  
小节：11.6 第一条可复制 grep  
精确位置：L235  
原文：`grep -n "inventory reject" evidence/logs/app-sample.log`  
问题等级：P2  
问题类别：CODE / PRE  
问题说明：相对路径只有在 `project/minishop` 下成立。11.6 尚未 `cd`。工作实战 L495 才 cd。  
为什么有问题：本轮在仓库根执行 → `No such file or directory`（E52）；在 minishop 目录 → 命中 INFO 行（E53）。Chapter-11 写了样本 vs `logs/app.log`（CH11-0011），**没单独标 11.6 这条相对路径的 cwd**。  
依据：E52–E53。  
建议修改：写成 `project/minishop/evidence/logs/app-sample.log`，或先 `cd project/minishop`。  
推荐替换文本：`grep -n "inventory reject" project/minishop/evidence/logs/app-sample.log`

### ISSUE
ID：G03-0009  
文件：`chapters/12b-sql-write-and-minishop.md`  
章节：第 12 章  
小节：12.12 INSERT 围栏  
精确位置：L32–38  
原文：散文「练习插入应放在事务里回滚」；可复制 SQL 是 SELECT + INSERT，无 BEGIN/ROLLBACK  
问题等级：P2  
问题类别：SQL / CODE  
问题说明：sqlite3 CLI 执行该围栏会 **提交** 一行耳机（本轮 id=4）。同一文件后续若再跑 12A 的 LEFT JOIN，「SKU-DEMO-003 的 qty 为空」不再成立。  
为什么有问题：12A 审查数字建立在三行购物车上。学生按页顺序把 12B INSERT 打进 `~/minishop-sql-lab.sqlite`，聚合/LEFT JOIN 与课文对不上，会以为自己 JOIN 写错。CH12 验证了 FK 与 ROLLBACK 示例，**未标这条已提交 INSERT 对同一库后续查询的污染**。  
依据：E30 vs E24 的 LEFT JOIN 声称。  
建议修改：INSERT 围栏包进 `BEGIN…ROLLBACK`，或明确「这是会留下的准备数据，后面 JOIN 会多一行耳机」。  
推荐替换文本：

```sql
BEGIN;
INSERT INTO cart_items (user_id, product_id, qty) VALUES (1, 3, 1);
SELECT id, user_id, product_id, qty FROM cart_items WHERE user_id = 1 AND product_id = 3;
ROLLBACK;
```

### ISSUE
ID：G03-0010  
文件：`chapters/15b-python-files-json.md`  
章节：第 15 章  
小节：15.10 读文件  
精确位置：L95–106 声称输出 `list 8 合法数量`；JSON 在 L321  
原文：先准备 cart_cases.json（见 15.12）  
问题等级：P2  
问题类别：CODE / SEQ  
问题说明：按页复制 15.10 必 `FileNotFoundError`。同目录放上 15.12 的 8 条后，完整脚本输出与课文完全一致（E20）。  
为什么有问题：正式代码块给了确定打印结果，上下文却不完整。  
依据：E19–E20。  
建议修改：15.10 用 2 条最小 JSON，或把读取示例移到 15.12 之后。  
对照：【同意 CH15-0009】独立复现。

### ISSUE
ID：G03-0011  
文件：`project/minishop/jmeter/minishop-get-products.jmx`；`chapters/18-performance-testing.md`  
章节：第 18 章  
小节：18.7 与仓库骨架  
精确位置：`TestPlan.functional_mode=true`；HTTPSampler 后无 Assertion 元件  
原文：元件表有 Assertion；纪律「先看功能断言」  
问题等级：P2  
问题类别：CODE / TEST  
问题说明：XML 完好，1 user / 1 loop / GET `127.0.0.1:8765/api/products` 与 MiniShop 默认一致。**没有 `ResponseAssertion`**。saveConfig 里的 `<assertions>true</assertions>` 只是结果保存开关，不是断言。functional mode 在加压时违反 JMeter 官方 best practices。  
为什么有问题：学生把线程改大却不关 functional mode / View Results Tree，会得到不能当 SLA 的文件，还以为已经「先看功能断言」。  
依据：E59；本机 **未装 jmeter**，GUI 勾选是否原样显示标 【External Verification Required】。  
建议修改：加 Response Code 200 或 Contains `items`；正文写明 functional mode 仅调试。  
对照：【同意 CH18-0006 实质】。用词分歧见 §7。

### ISSUE
ID：G03-0012  
文件：`chapters/18-performance-testing.md`  
章节：第 18 章  
小节：18.4 百分位  
精确位置：python 围栏只算 mean/median/max  
原文：打印 266.0 / 120 / 800  
问题等级：P2  
问题类别：CODE / TERM  
问题说明：数字算对（E18）。名为 P95 的章却不停在平均/中位/最大。  
为什么有问题：可运行代码不能支撑标题概念。不是语法错误。  
依据：E18；样本 `[100,110,120,200,800]`。  
对照：【同意 CH18-0001/0002 方向】；本 Agent 只从「代码是否实现所教指标」开单。

### ISSUE
ID：G03-0013  
文件：`chapters/17-automation-overview.md`  
章节：第 17 章  
小节：17.4 对照表；17.7 YAML  
精确位置：表写 `getByRole`；YAML `TEACH_BASE_URL` + 仓库根 `pytest`  
原文：推荐 getByRole；示例流水线 `python -m pytest -q`  
问题等级：P2  
问题类别：CODE / TERM  
问题说明：（1）本机 Playwright Python：`get_by_role` 存在，`getByRole` 不存在。同节 Python 示例已经是 snake_case，表会抄出 `AttributeError`。（2）`conftest.py` 不读 `TEACH_BASE_URL`；根目录 pytest 即 G03-0007。  
依据：E60、E16；YAML 可解析但不是 MiniShop 入口。  
对照：【同意 CH17-0004 / CH17-0005】。

### ISSUE
ID：G03-0014  
文件：`chapters/16b-pytest-fixtures.md`；`project/minishop/tests/conftest.py`  
章节：第 16 章  
小节：16.6 `base_url` 片段；「登录很慢再改 session」  
精确位置：片段读 `MINISHOP_BASE_URL` 默认 8765；仓库 fixture 起临时端口 + autouse `reset_db`  
原文：仓库套件自己起临时端口（一句话）；同时又建议 session scope  
问题等级：P2  
问题类别：CODE / ACC  
问题说明：抄片段打常驻 serve 会脏库（注册 409、库存被扣）。把 `token_a` 改成 session 后，autouse `reset_db` 会让旧 token **401**。  
为什么有问题：本轮：登录 200 → `reset_db` → 同 token 打购物车 → **401**（E61）。  
依据：E61；`conftest.py` 无 `MINISHOP_BASE_URL`。  
对照：【同意 CH16-0003 / CH16-0004】。

### ISSUE
ID：G03-0015  
文件：`project/minishop/run.py`；`chapters/19-minishop-project.md`  
章节：第 19 章  
小节：`python3 run.py test`  
精确位置：`run_pytest()` 写 `evidence/pytest-output.txt` 且跑两遍 pytest（第二次 html）  
原文：`python3 run.py test       # pytest`  
问题等级：P2  
问题类别：CODE / PED  
问题说明：会覆盖已提交的审查证据。19-1 直接 `python -m pytest` 不写该文件。本轮 pytest 走 venv，**故意不跑 `run.py test`** 以免改原仓库 evidence。  
依据：`run.py` L61–81。  
对照：【同意 CH19-0008】。

---

## 6. P3

### ISSUE
ID：G03-0016  
文件：`practice/01-observation-oracle-evidence/tests/test_lab.py` 等  
章节：实操测试  
精确位置：class `Practice11Tests`（1-1）、`Practice51Tests`（5-1）…  
原文：类名把「1-1」写成 `11`  
问题等级：P3  
问题类别：CODE  
问题说明：unittest 通过，不影响学生命令。读测试的人会以为是第 11 章。Chapter Agent 未开单。  
建议修改：`Practice1_1Tests`。

### ISSUE
ID：G03-0017  
文件：`project/minishop/frontend/app.js`；`admin.html`  
章节：工程前端  
精确位置：`innerHTML = … sku/name/id` 拼接  
问题等级：P3  
问题类别：JOB / CODE  
问题说明：教学数据可信，功能测试够用。岗位上这是 DOM XSS 面。教材不当成安全课可以，但不要在面试口播里说「我做了前端安全」。Chapter Agent 未开单。  
建议修改：一句纪律即可，不必改实现。

### ISSUE
ID：G03-0018  
文件：`practice/_minishop.py`  
章节：实操基础设施  
精确位置：给 `MiniShopHandler.db_path` 赋类属性  
问题等级：P3  
问题类别：CODE  
问题说明：并发两个 MiniShopLab 会互踩 DB 路径。课程脚本串行，pytest 一个 session server，本轮全部绿。不要并行 `--check`。  
建议修改：实例级状态或锁。非学生作业。

### ISSUE
ID：G03-0019  
文件：`project/minishop/docs/openapi.json`  
章节：第 13 章文档资产  
精确位置：`POST /api/cart/items` responses 无 404；login 无 400  
问题等级：P3  
问题类别：CODE  
问题说明：本轮未知 sku → 404 `unknown sku`；缺字段登录 → 400。薄 OpenAPI 与实现不完全同构。CH13-0008 已从「无 security/无 Swagger UI」切入；这里只补一条实现有、文档无的状态码。  
建议修改：补 404/400 或写明「错误码以 PRD+server 为准」。

### ISSUE
ID：G03-0020  
文件：`chapters/07-web-basics.md`；`chapters/assets/07-html-combo.html`  
章节：第 7 章  
小节：HTML 示例  
精确位置：价格 `¥99.00`  
问题等级：P3  
问题类别：MiniShop / CODE  
问题说明：组合页可打开，JS 语法正确，按钮会改成「已加入购物车」。v1.0 商品没有价格字段。正文已说「不代表真实 MiniShop 加购」。仍可能被抄进观察记录。  
建议修改：改成库存，或再加半句「价格是假数据」。

### ISSUE
ID：G03-0021  
文件：`project/minishop/run.py` `serve()`  
章节：工程入口  
精确位置：`os.execv(sys.executable, …)` 不用 `.venv`  
问题等级：P3  
问题类别：CODE  
问题说明：server 是标准库，能跑。`test` 优先 venv，`serve` 用当前解释器。`python3 server.py` 的 `ps` 命令行里不一定有单词 `minishop`（同意 CH11-0004）。不是功能 bug。

其它已由章节 Agent 覆盖、本轮只确认不升级的 P3：09B Body 缺 `role`；15A `from __future__`；Windows `python3` vs `py -3`；环境文件 `password` 空（必须本机填 `Test1234`）；集合 `newPhone` 跑第二次 409；`pm.expect(true)` 反例练习（14.练习 4）语法合法、断言无意义——课文当反例是对的。

---

## 7. 与 Chapter Agent 分歧

格式：【Agent Disagreement】双方证据 → 本 Agent 裁决建议（总控最终裁决）。

### D1. CH15-0017 把 `from __future__ import annotations` 当代码问题

- Chapter-15：practice 15-1 有未教的 future 注解，P3 CODE。  
- 本轮：该文件跑通（E12）；3.12+ 上这行是空操作，不影响观察 JSON。  
- **裁决建议：保留为风格/课序 P3，不要进「代码质量」主清单，更不要当成 15-1 不可运行。** 真正的 15 章代码问题是 15.10 缺文件（G03-0010）。

### D2. CH18-0006「jmx 没有 Assertion」的用词

- Chapter-18：树里没有 Assertion 节点。  
- 本轮：文件里能搜到 `<assertions>true</assertions>`，那是 **SampleSaveConfiguration**，不是 `ResponseAssertion`。  
- **裁决建议：同意实质（没有功能断言元件）。** 改稿时不要用「文件里没有 Assertion 字符串」这种检验，以免后人以为 saveConfig 算断言。G03-0011 按元件类型写。

### D3. CH12 未执行 `python3 practice/run.py 12-1`

- Chapter-12：为避免写 `validation/latest.json` 只跑了等价 Python。  
- 本轮：在 `/tmp` 副本实跑 12-1，API=SQL=2，与其结论一致。  
- **无结论分歧。** 取证方法不同。

### D4. 无「practice / pytest 基线已红」类冲突

多章声称 37 passed / 1 xfailed、5-1 切点、13-1 四态。本轮全部绿，**不支持任何「基线已经变了」的旧印象**。

### D5. P1 清单与章节 Agent

G03-0001…0004 与 CH14-0001、CH11-0001/CH14-0005、CH13-0004、CH14-0002 **同向**。不另开假冲突。总控若去重，保留跨章那条 `keyword=mouse` 和 Postman Cookie 罐即可。

### 章节 Agent 已覆盖、本轮同意且不重复长写的

| 章节 ISSUE | 本轮 |
| --- | --- |
| CH13-0001 四态图缺 sku | `{"qty":null}` → `missing sku` |
| CH13-0005 MiniShop 不校验 Content-Type | 错误 CT 仍 200 写购物车 |
| CH13-0006 「Body 只要 sku」 | OpenAPI required sku+qty；下单 qty=11 也 400 |
| CH14-0003 「第 6 步再创建订单」集合没有 | 集合 15 条，仅一条创建订单 |
| CH16-0009 根目录 pytest | E16 |
| CH17-0004 getByRole | E60 |
| CH19-0008 run.py test 覆盖 evidence | 代码确认；本轮未执行以免改仓库 |

---

## 8. 代码质量总表（实现 vs 教材）

| 资产 | 语法 | import/API | 参数/路径 | 完整性 | 可运行 | 输出 vs 声称 | 隐藏依赖 | 未教授概念 | 坏习惯 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| practice 1-1…15-1 | 通过 | stdlib + MiniShopLab | `/api/` 正确 | 完整 | 全绿 | 一致 | 无第三方 | Lab 内部有 future/线程，学生可不读 | 类名 Practice11Tests |
| practice 16-1/19-1 | 通过 | 要 pytest | cwd=minishop | 锁 37/1 | 需 setup | 一致 | `.venv` | 字符串匹配 pytest 摘要（脆弱但有意） | 两次跑 pytest（19-1 再跑一遍） |
| `server.py` | 通过 | stdlib | 与 OpenAPI 路径对齐 | 库存/权限/四态实现完整 | pytest 绿 | HTTP/1.0、charset、role 比课文多 | 无 | 类 handler、线程 | 固定盐哈希（教学，勿当生产） |
| `tests/*.py` | 通过 | pytest/requests | fixture 临时端口 | 38 条 | 37+1 xfail | 与正文基线一致 | requirements.txt | xfail strict 正文展示不足（CH16-0006） | autouse 清库正确 |
| 第 15A 片段 | 通过 | 无 | — | 有 print 的完整 | 输出 MATCH | MATCH | 无 | 15A 提前 json.dumps(set) | 可变默认参数是反例，处理正确 |
| 第 15B 完整脚本 | 通过 | json | 依赖同目录 JSON | 8 条 expect 全中 | 放一起则绿 | MATCH | 无 | — | 15.10 前移 |
| 第 16 片段 | 通过 | requests/pytest | 8765 vs 临时端口两扇门 | 片段不是完整 conftest | 对已启动服务可跑 | — | 先 serve | fixture 装饰器 | session token 建议有害 |
| 第 12 SQL | CLI 通过 | SQLite 方言已声明 | 教学库 ≠ MiniShop 全表 | 12.4 无 UNIQUE(user_id,product_id) | CLI 数字对 | MATCH | `sqlite3` | TRUNCATE 已声明没有 | 12.12 INSERT 提交 |
| 第 11 bash | 部分实跑 | macOS 差异正文有 | grep 相对路径 | curl 最小读取用错 keyword | mouse 空列表 | 不一致 | 服务须启动 | — | cwd |
| 第 13 curl | TOKEN 块可跑 | python json | `/api/login` 正确 | 报文缺 CL | curl 行可跑、裸 TCP 不行 | 状态行 1.0≠1.1 | 服务 | — | -D 与 json.load 相邻 |
| Postman JSON | 合法 | pm.test/expect 语法过关 | `/api/*` 正确 | 15 条；无 disableCookies | GUI 未跑；Cookie 行为已用 HTTP 证明 | 空搜索按设计应红 | 本机填 password | 变量 lastOrderId | 无凭证请求 |
| JMX | XML 合法 | GET products | 127.0.0.1:8765 | 无断言；functional mode | **JMeter 未装** | — | 服务 | functional mode 未解释 | 加压禁用项 |
| YAML | 可解析 | Actions v4/v5 常见 | 不读 MiniShop env | 声明「不是本仓库」 | 不能当 MiniShop CI | — | 无 .github | TEACH_* 虚构 | 根目录 pytest |
| 前端 JS | 语法可接受 | fetch + sessionStorage | `/api/login` 等正确 | 登录不传空 keyword（pytest 有锁） | 未开浏览器 | — | — | innerHTML | Number() 对 type=number 够用 |

---

## 9. 建议（只给总控，不改教材）

1. **先修学生会复制且会得到错观察的四条 P1**：mouse 空列表、HTTP 报文成帧、Postman Cookie 罐、`lastOrderId`。  
2. **再修本 Agent 新 P2**：`run.py` 的 `or True`、13.13 管道、11.6 cwd、12.12 INSERT。  
3. practice 与 pytest 基线不要动逻辑，只改类名/注释即可。  
4. JMeter / Postman GUI 本环境没有，总控不要把「作者未点 Runner」写成代码语法错误。

---

## 10. 本章（全局代码）结论

**C 明显需要修改**（对「可复制命令与资产」而言，不是对 MiniShop 能否启动而言）。

- 不是 E：实现能跑，基线 37/1 真，SQL/Python 声称输出真。  
- 不是 A/B：四条 P1 都在学生第一天会抄的 curl/Postman/HTTP 上。  
- 核心课程序列（5-1 切点、8-1 403、13-1 四态、16-1 xfail）代码是诚实的。

---

## 11. 执行记录

读过（不完全等于改过）：`GLOBAL_AGENT_BRIEF.md`、`UNIT_INVENTORY.md`、`AUDIT_AGENT_BRIEF.md`、`practice/run.py` `_http.py` `_minishop.py` 全部 `practice/*/main.py` 与 `tests/test_lab.py`、`project/minishop/server.py` `run.py` `pytest.ini` `requirements.txt` `tests/*` `postman/*` `jmeter/*.jmx` `docs/openapi.json` `frontend/index.html` `app.js` `admin.html` `run.sh` `run.bat`、相关章节围栏、CH11–19 审计中 CODE 类 ISSUE。

实跑工作目录：`/tmp/g03-audit-ws` 与 `/tmp/g03-sql`、`/tmp/g03-snip`、`/tmp/g03-runs`。原仓库 practice `validation/` **未**被本轮 1-1…19-1 覆盖（副本 mtime 更新，原文不同）。

未跑：`run.py evidence`（会写章节配图）、JMeter GUI、Postman GUI、SSH、kill 示例 PID。

本机指纹：Python 3.14.3；pytest 9.1.1；sqlite3 3.43.2；Playwright Python 已装（仅内省 API）；Selenium / jmeter / Postman CLI **无**。
