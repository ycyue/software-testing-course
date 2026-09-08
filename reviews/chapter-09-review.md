# 第 9 章《计算机网络与 HTTP》质量审查记录

## 审查信息

- 审查对象：`chapters/09-computer-network-and-http.md`
- 质量标准：Quality Standard v1.0
- 流程：初稿 → 初审 → 修正 → 发布前复审
- 主要依据：RFC 9110 HTTP Semantics、RFC 9111 HTTP Caching、RFC 5789 PATCH、MDN HTTP 方法/状态码/HTTPS
- 核验日期：2026-09-08

## 初审结论

初稿覆盖大纲全部主题：IP/Port、TCP/UDP、三次握手、HTTP、HTTPS/TLS、请求/响应、Method、GET/POST、状态码、Headers、Body 和登录请求。GET/POST 已按 safe、幂等、query、body、缓存解释，并明确禁止“GET 不安全、POST 安全”和长度绝对化。

初审评分：**96/100。** PATCH 被误列入 RFC 9110 方法表，属于术语/知识性错误，Definition of Done 未通过，暂不发布。

## 问题清单

| ID | 级别 | 问题 | 修正要求 |
| --- | --- | --- | --- |
| CH09-01 | 中 | 方法对照表把 PATCH 写进 RFC 9110 成员 | PATCH 改为 RFC 5789 附注；RFC 9110 表只保留规范内方法 |
| CH09-02 | 低 | 参考资料使用 MDN 中文路径，可能与英文规范页不一致 | 与第 7、8 章一致，改为英文官方路径 |
| CH09-03 | 低 | 未说明 HTTP 后续还有 QUERY 等带 Body 的安全方法，初学者可能把“查询只能 GET”绝对化 | 用一句话标明 QUERY 存在，初级岗位仍以 GET/POST 为主 |

## 专项审查

### 技术准确性

- safe / idempotent 定义与 RFC 9110 §9.2 一致；GET/HEAD/OPTIONS/TRACE 为安全方法；PUT/DELETE 及安全方法为幂等；POST 既不安全也不幂等；
- 已区分 HTTP 的 safe 与 TLS 机密性；
- URL 长度限制被正确描述为实现限制而非 HTTP 硬性规则；
- 401/403 按认证与拒绝授权解释，并允许项目约定覆盖；
- 200 与业务成功解耦；
- TCP 三次握手未与 HTTP 三次请求混淆；
- Cookie / Authorization 层次与第 8 章一致；
- 初稿误将 PATCH 列入 RFC 9110 方法表，必须修正。

### 时效性

- 语义依据 RFC 9110（2022，现行 HTTP 语义标准）；
- 缓存原则指向 RFC 9111；
- HTTP/2、HTTP/3/QUIC 仅作边界，不把 HTTP/1.1 文本格式说成唯一传输形式。

### MiniShop 一致性

- 沿用 `shop.example.test`、`8443`、教学手机号；
- 登录路径、Cookie 名、Token 字段均标明教学示例，未冻结正式接口；
- 未引入订单状态或未基线化的业务字段。

### 代码、curl 与安全

- 正文报文为示例结构，密码使用 `<redacted>`；
- 审查阶段在 `127.0.0.1` 启动教学 HTTP 服务，用 curl 验证：
  - `GET /products?keyword=mouse` → `200`、`Content-Type: application/json`、Body 含 `mouse`；
  - `POST /login` JSON → `200`、`Set-Cookie: session_demo=abc; HttpOnly; Path=/`；
- 该服务由 Python `BaseHTTPRequestHandler` 提供，响应行为 HTTP/1.0，只验证状态行、头字段和 Body 可读，不冒充 MiniShop，也不要求学习者启动；
- 禁止未授权重放 Cookie/Token 和明文密码进入命令历史。

### 初学者友好性

- 用“登录失败在哪一层”导入；
- 用表格拆开 safe、幂等、query、缓存；
- 网络地图明确不要求先背 OSI 七层。

## 初稿 20 项 Definition of Done

| # | 检查项 | 初审结果 | 说明 |
| --- | --- | --- | --- |
| 1 | 目标明确 | 通过 | 读懂报文并正确比较 GET/POST |
| 2 | 前置知识正确 | 通过 | 顺序接第 8 章 |
| 3 | 无知识性错误 | 待修正 | PATCH 归属 |
| 4 | 重要信息未过时 | 通过 | RFC 9110/9111 |
| 5 | 无错误绝对化 | 通过 | 专节打破 GET/POST 神话 |
| 6 | 术语准确 | 待修正 | PATCH 不应算 RFC 9110 方法表成员 |
| 7 | 零基础能理解 | 通过 | 楼/门、握手与业务分开 |
| 8 | 示例具体 | 通过 | 登录报文 A/B |
| 9 | 有实际工作场景 | 通过 | HTTP 观察记录 |
| 10 | MiniShop 一致 | 通过 | 教学路径未冻结 |
| 11 | 代码经过验证 | 通过 | curl 教学服务已跑通 |
| 12 | SQL 操作安全 | 不适用，满足 | 无 SQL |
| 13 | 图表帮助理解 | 通过 | 分层、握手、请求响应 |
| 14 | 重要级别明确 | 通过 | 核心节 ⭐⭐⭐ |
| 15 | 常见错误有价值 | 通过 | 覆盖十类高频误解 |
| 16 | 面试题非死记硬背 | 通过 | 含边界 |
| 17 | 练习覆盖目标 | 通过 | 10 题覆盖握手、GET/POST、状态码、Cookie |
| 18 | 答案对应练习 | 通过 | 10 题对应 |
| 19 | 检查清单可验证 | 通过 | 含自测门槛 |
| 20 | 衔接下一章 | 通过 | 预告 DevTools |

初审结果：**18 项直接通过，2 项待修正，1 项不适用但满足。**

## 初稿评分

| 项目 | 满分 | 得分 |
| --- | ---: | ---: |
| 技术准确性 | 25 | 23 |
| 知识完整性 | 15 | 14 |
| 初学者友好 | 15 | 15 |
| 实战价值 | 15 | 15 |
| 示例质量 | 10 | 10 |
| 项目一致性 | 5 | 5 |
| 面试价值 | 5 | 5 |
| 练习质量 | 5 | 5 |
| 结构与表达 | 5 | 4 |
| **总分** | **100** | **96** |

## 修正清单

- [x] RFC 9110 方法表移除 PATCH，改为 RFC 5789 附注；
- [x] 补充 TRACE、CONNECT 以与 RFC 9110 方法表对齐，并标明少见；
- [x] 说明 QUERY 等方法存在，初级仍以 GET/POST 为主；
- [x] MDN 链接改为英文官方路径；
- [x] 完成 curl 验证并写入可运行性说明；
- [x] 完成最终复审。

## 发布前复审

### 修正验证

- RFC 9110 对照表现为 GET/HEAD/POST/PUT/DELETE/OPTIONS/TRACE/CONNECT；
- PATCH 与 QUERY 仅作为边界，未冒充 RFC 9110 核心方法表；
- 参考资料与第 8 章同样指向 MDN 英文页；
- GET/POST 硬约束保持：无“POST 更安全”“GET 一定更短”。

### curl 验证记录

```text
GET /products?keyword=mouse
HTTP/1.0 200 OK
Content-Type: application/json; charset=utf-8
{"items": [{"name": "mouse"}], "keyword": "mouse"}

POST /login
HTTP/1.0 200 OK
Content-Type: application/json; charset=utf-8
Set-Cookie: session_demo=abc; HttpOnly; Path=/
{"result": "ok", "note": "teaching only"}
```

### 最终 20 项 Definition of Done

| # | 检查项 | 复审结果 |
| --- | --- | --- |
| 1 | 目标明确 | 通过 |
| 2 | 前置知识正确 | 通过 |
| 3 | 无知识性错误 | 通过 |
| 4 | 重要信息未过时 | 通过 |
| 5 | 无错误绝对化 | 通过 |
| 6 | 术语准确 | 通过 |
| 7 | 零基础能理解 | 通过 |
| 8 | 示例具体 | 通过 |
| 9 | 有工作场景 | 通过 |
| 10 | MiniShop 一致 | 通过 |
| 11 | 代码经过验证 | 通过 |
| 12 | SQL 操作安全 | 不适用，满足 |
| 13 | 图表帮助理解 | 通过 |
| 14 | 重要级别明确 | 通过 |
| 15 | 常见错误有价值 | 通过 |
| 16 | 面试题非死记硬背 | 通过 |
| 17 | 练习覆盖目标 | 通过 |
| 18 | 答案对应练习 | 通过 |
| 19 | 检查清单可验证 | 通过 |
| 20 | 衔接下一章 | 通过 |

复审结果：**20/20，通过。**

### 最终评分

| 项目 | 满分 | 最终得分 |
| --- | ---: | ---: |
| 技术准确性 | 25 | 25 |
| 知识完整性 | 15 | 15 |
| 初学者友好 | 15 | 15 |
| 实战价值 | 15 | 15 |
| 示例质量 | 10 | 10 |
| 项目一致性 | 5 | 5 |
| 面试价值 | 5 | 5 |
| 练习质量 | 5 | 5 |
| 结构与表达 | 5 | 4 |
| **总分** | **100** | **99** |

结构与表达扣 1 分：方法表对 TRACE/CONNECT 的说明对零基础略超纲，但有助于与 RFC 9110 对齐，故保留并标明少见。

## 剩余风险

- 学习者尚未在 DevTools 里亲手看报文，第 10 章必须把本章字段对应到 Network 面板；
- Python 教学服务响应 HTTP/1.0，不能用来演示 HTTP/2 帧；
- MiniShop 正式登录是表单、JSON 还是两者，仍待项目基线。

## 最终结论

- Definition of Done：**20/20**；
- 最终评分：**99/100**；
- 发布标准：最低 90/100，**达到**；
- 发布结论：**可以正式发布**；
- 下一章：第 10 章《Chrome DevTools》。
