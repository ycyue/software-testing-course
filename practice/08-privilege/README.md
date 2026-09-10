# 实操 8-1 ★：别人的订单和后台接口

> 配套第 8 章（下）。权限测的是**服务器判定**，不是页面上藏没藏按钮。

← [实操目录](../README.md) · 📖 [读第 8 章下](../../chapters/08b-web-auth-permission.md)

## 这次实操要练什么

PRD `R-PERM`：用户不得读写他人订单；非管理员不得访问 `/api/admin/*`。

| 谁 | 做什么 | 预期 |
| --- | --- | --- |
| A | 下一单 | 201，得到 `id` |
| B | 用 A 的 `id` 去读 | **403**，不是 404 也不是 200 |
| A | 读自己的订单 | 200 |
| A | `GET /api/admin/orders` | 403 |
| 管理员 | `GET /api/admin/orders` | 200 |

脚本替你带的是 **Bearer**。分层观察（Cookie / Session / Token 不是三选一）对照 `project/minishop/evidence/http/01-login-ok.txt`：同一份成功登录里既有 `Set-Cookie` 也有 JSON `token`。未认证 401 不在上表五格里，可自己对 `/api/orders/{id}` **同时去掉** Bearer 和 Cookie `minishop_session` 看一眼；只去掉 Bearer、Cookie 还在，会仍是 200。

## 最小命令

```bash
python3 practice/run.py 8-1
```

## 验收条件

- 上表五格状态码都对
- 写出 `validation/latest.json`
- `--check` 通过
