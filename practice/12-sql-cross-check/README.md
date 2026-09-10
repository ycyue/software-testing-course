# 实操 12-1 ★：API 数量和 SQL 必须对上

> 配套第 12 章。数据库是最终状态；只看页面等于少了一条观察通道。

← [实操目录](../README.md) · 📖 [读第 12 章上](../../chapters/12a-sql-query.md) · [第 12 章下](../../chapters/12b-sql-write-and-minishop.md)

## Code map

- **Run first:** `python3 practice/run.py 12-1`
- **Core behavior:** 登录后把购物车改为 2，再用 `JOIN` 读库
- **Verifier:** `python3 practice/run.py 12-1 --check`
- **Skip on first pass:** 临时 SQLite 文件在哪

## 这次实操要练什么

同一条业务规则要用**两条观察通道**核对：

- API：`POST /api/cart/items` 返回 `"qty": 2`
- SQL：`cart_items JOIN users JOIN products` 同一用户同一 SKU 也是 2

对不上就是缺陷。这次实操在**临时教学库**里写入，退出即删除，不是生产库。

## 最小命令

```bash
python3 practice/run.py 12-1
```

## 验收条件

- API 与 SQL 的 `qty` 均为 2（合法改数，不是 qty=11）
- 打印了 JOIN 语句
- 写出 `validation/latest.json`
