# 实操状态

本文件记录仓库里**已经留下的证据**，不记录你本机还没做的那一次。

克隆、安装依赖、冒烟通过，都不等于实操完成。

| 状态 | 含义 |
| --- | --- |
| **Complete** | 有可复核证据。允许结论是「复现了缺陷」或「假设未成立」 |
| **Reader exercise** | 完成取决于你写出的评审/缺陷单/口述 |
| **Incomplete** | 骨架或步骤在，作者未留下 GUI/压测等证据 |

## 已留下证据的实操

| 实操 | 状态 |
| --- | --- |
| 1-1 观察/判定/证据 | **Complete**（跑完会在本机写出 `validation/latest.json`，该文件不入库；预期复现 BUG-001） |
| 4-1 需求评审 | **Reader exercise**（模板在 `04-requirement-review/`） |
| 5-1 库存边界 | **Complete**（qty=10 通过、qty=11 拒绝） |
| 6-1 缺陷报告 | **Reader exercise**（模板在 `06-bug-report/`） |
| 8-1 权限 | **Complete**（他人订单 403，非管理员 403） |
| 9-1 HTTP 四格 | **Complete**（登录 200 + token + Set-Cookie） |
| 11-1 日志 grep | **Complete**（临时日志出现 inventory reject） |
| 12-1 SQL 交叉验证 | **Complete**（临时库，退出即删） |
| 13-1 接口形状 | **Complete**（missing / null / empty / wrong type） |
| 15-1 JSON | **Complete**（读回 3 件商品，鼠标库存 10） |
| 16-1 pytest 基线 | **Complete**（需 `run.py setup`；37 passed / 1 xfailed） |
| 19-1 MiniShop 项目包 | **Complete**（文件检查 + pytest；无 Postman GUI、无性能结论） |

## 明确未完成

| 实操 | 状态 |
| --- | --- |
| 10-1 DevTools 面板 | **Incomplete**：有页面截图和步骤，没有 DevTools 面板本身的截图 |
| 14-1 Postman Runner | **Incomplete**：集合可导入，作者未点 GUI Runner |
| 18-1 JMeter | **Incomplete**：有 `jmeter/minishop-get-products.jmx`，未安装、未跑 GUI |

17-1 是 **Reader exercise**（画分层地图），不是缺一套 Playwright 回归。Playwright 只用于 `run.py evidence` 取证。

其余书面实操（2-1、3-1、7-1、17-1、20-1、21-1、22-1）默认是 **Reader exercise**，入口在对应章的「MiniShop 工作实战」（根 README 实操列已链过去）。`practice/run.py` 不认这些编号。
