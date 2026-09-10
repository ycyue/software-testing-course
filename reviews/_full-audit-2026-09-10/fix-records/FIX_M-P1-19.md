# FIX RECORD
Audit ID：M-P1-19
原问题：正文、14.3 变量表、14.5 创建订单脚本、练习 8 答案、Path 示例写 `orderId`。仓库环境 JSON 与越权 URL 是 `lastOrderId`。按正文 set 后再跑集合越权请求，Path 为空 → 实际 `GET /api/orders/` → 404 而不是 403。
修改文件：`chapters/14-postman.md`（环境 JSON 已是 `lastOrderId`，未改）
修改位置：14.2 Path 示例；14.3 变量表；14.5 创建订单脚本；14.7 越权 Path；练习 8 答案
原内容：（摘录）

> 例如 Path `/api/orders/:orderId` 与 `{{orderId}}`。
> | `orderId` | 运行中由脚本写入 | 创建订单后保存 |
> `pm.environment.set("orderId", body.id);`
> 保存第一次 `orderId`，第二次 `pm.expect(body.id).to.not.eql(pm.environment.get("orderId"))`。

修复后内容：（摘录）

> 仓库越权请求的 URL 是 `{{baseUrl}}/api/orders/{{lastOrderId}}`
> | `lastOrderId` | 运行中由脚本写入 | 创建订单后保存；越权请求的 Path 引用它 |
> `pm.environment.set("lastOrderId", body.id);`
> 保存第一次 `lastOrderId`，第二次（复制「创建订单」再跑）`pm.expect(body.id).to.not.eql(pm.environment.get("lastOrderId"))`。
> 14.7：`GET /api/orders/{{lastOrderId}}`

为什么这样修：线性读者必须用和环境文件、越权 URL 同一个名字，否则 403 用例打成 404。Path `:id` 与环境变量 `{{lastOrderId}}` 不是同一层，正文改用仓库真实写法。
依据：`MiniShop.postman_environment.json` 仅有 `lastOrderId`；集合「创建订单」`set('lastOrderId')`；「越权-他人订单」`GET {{baseUrl}}/api/orders/{{lastOrderId}}`；`server.py` 对 `/api/orders/` 不进 `_get_order`。
是否影响其他章节：第 19 章导入同一集合，变量名现已一致。未改环境 JSON。
验证结果：`chapters/14-postman.md` 已无 `orderId` 作为环境变量名。环境 keys 含 `lastOrderId` 不含 `orderId`。集合越权 URL 为 `{{baseUrl}}/api/orders/{{lastOrderId}}`。
状态：FIXED
