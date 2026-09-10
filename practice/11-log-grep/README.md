# 实操 11-1 ★：页面失败之后去 grep 日志

> 配套第 11 章。日志是页面上看不到的观察通道。

← [实操目录](../README.md) · 📖 [读第 11 章](../../chapters/11-linux.md)

## 这次实操要练什么

把购物车改成 `qty=11`（应当被拒），然后在应用日志里找 `inventory reject`。

仓库里已有对照摘录：`project/minishop/evidence/linux/grep-app-log.txt`。本次脚本在**临时日志**上再跑一遍，不改教学库。

## 最小命令

```bash
python3 practice/run.py 11-1
```

自己在本机对照时：

```bash
cd project/minishop
grep -E "login ok|inventory reject" evidence/logs/app-sample.log
```

## 验收条件

- HTTP 400（不是 500）
- 日志至少一行含 `inventory reject` 和 `qty=11`（仓库样本级别是 INFO，不要默认 grep ERROR）
- 写出 `validation/latest.json`
