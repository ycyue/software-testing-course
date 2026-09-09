# MiniShop v1.0 执行证据

本目录保存**本机真实跑出来的**输出，不是手写示例。采集命令：

```bash
cd project/minishop
python3 run.py setup
python3 run.py evidence
```

| 路径 | 内容 |
| --- | --- |
| `pytest-output.txt` | pytest 摘要 |
| `pytest-report.html` | 可选 HTML 报告（需 pytest-html） |
| `http/` | curl 等价的登录/注册/购物车/搜索响应（token 已打码） |
| `sql/seed-join.txt` | Tester A 购物车 JOIN（第一节种子 qty=1；第二节为 qty=10/11 之后） |
| `logs/app-sample.log` | 应用日志摘录（无完整 token） |
| `linux/` | pwd/ls/df/grep/curl 头 |
| `screenshots/` | 本机 Chrome（Playwright channel=chrome）页面截图 |

不要把这里的密码用于真实系统。截图中的教学账号仅限本机。
