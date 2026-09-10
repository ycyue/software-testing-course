# 实操 9-1 ★：登录请求的四格

> 配套第 9 章。HTTP 观察不是「看一下 Network」，而是能说出方法、路径、头、体。

← [实操目录](../README.md) · 📖 [读 09B](../../chapters/09b-http-message-observe.md)

## Code map

- **Run first:** `python3 practice/run.py 9-1`
- **Core behavior:** `POST /api/login` 打印请求四格和响应状态/头/体
- **Verifier:** `python3 practice/run.py 9-1 --check`
- **Skip on first pass:** urllib 如何拼 JSON

## 这次实操要练什么

点登录按钮时，浏览器发出的是一条 HTTP 报文。测试工程师要能指出：

1. 方法是不是 POST
2. 路径是不是 `/api/login`（v1.0 前缀是 `/api/`）
3. 头里有没有 `Content-Type`
4. 体里是手机号和密码，而不是把密码放进 URL

响应里同时出现 `token` 和 `Set-Cookie`，对应 PRD `R-AUTH`：它们不是三选一的登录产品。

动手前先在纸上填四格（不要先看脚本输出）：

| 格 | 你猜 MiniShop 登录是什么 |
| --- | --- |
| 方法 |  |
| 路径 | （不要写 `/login`） |
| 头 |  |
| 体 | 密码在哪一格？ |

跑完再核对。对着 MiniShop 把路径写成 `/login` 会 404，那不是密码错。

## 最小命令

```bash
python3 practice/run.py 9-1
```

## 验收条件

- 打印请求的方法、路径、头、体四格
- HTTP 200，响应 JSON 含 `token`，响应头含 `Set-Cookie`
- 写出 `validation/latest.json`

教学密码只出现在本机请求体里，证据文件不得写入明文密码。
