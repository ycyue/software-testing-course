# 实操 5-1 ★：库存边界切在哪？

> 配套第 5 章。边界值不是「再测一个奇怪数字」，而是**切点两侧都要看到**。

← [实操目录](../README.md) · 📖 [读第 5 章](../../chapters/05-test-case-design.md)

## Code map

- **Run first:** `python3 practice/run.py 5-1`
- **Core behavior:** 已登录用户把 `SKU-DEMO-001` 设为 `qty=10` 再设为 `qty=11`
- **Verifier:** `python3 practice/run.py 5-1 --check`
- **Skip on first pass:** token 怎么从登录响应里取出来

## 这次实操要练什么

PRD `R-CART-10`：教学库存为 10 时，**等于 10 允许，超过 10 拒绝**。

只测 `qty=2`（正常值）通过，不能说明最大值在哪。只测 `qty=11` 被拒，也不能说明 `qty=10` 是否被误伤。

## 最小命令

```bash
python3 practice/run.py 5-1
```

## 验收条件

- `qty=10` → HTTP 200，响应含 `"qty": 10`
- `qty=11` → HTTP 400
- 写出 `validation/latest.json`
- `--check` 通过

## 读完请回答

等价类告诉你「有效/无效各测一个代表」；边界值告诉你「切点两侧各取一个」。这两条分别覆盖了什么风险？
