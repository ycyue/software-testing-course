# 实操 13-1 ★：缺字段、null、空字符串、错误类型

> 配套第 13 章。接口观察要看 Body 的**形状**，不能把所有异常捏成一条。

← [实操目录](../README.md) · 📖 [读第 13 章](../../chapters/13-api-testing.md)

## 这次实操要练什么

已登录后，对 `POST /api/cart/items` 分别发送：

| 形状 | Body | 预期 |
| --- | --- | --- |
| 缺字段 | `{"sku":"..."}` | 400 `missing qty` |
| null | `{"sku":"...","qty":null}` | 400 `null qty` |
| 空字符串 | `{"sku":"...","qty":""}` | 400 `wrong type qty` |
| 错误类型 | `{"sku":"...","qty":"1"}` | 400 `wrong type qty` |

本实现里后两种都是 wrong type——这也是观察：服务端把「不是 int」归成一类。测试记录里仍要分开写，因为别的系统可能把 `""` 当成缺省。

`qty=11` 的边界已在 [实操 5-1](../05-qty-boundary/) 测过，这里不重复当主目标。

## 最小命令

```bash
python3 practice/run.py 13-1
```

## 验收条件

- 四行都是 400，错误信息与上表一致
- 写出 `validation/latest.json`
