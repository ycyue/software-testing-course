# 实操 15-1 ★：把商品列表当成 JSON 来读

> 配套第 15 章（下）。Python 在本课程里是为了处理观察结果。

← [实操目录](../README.md) · 📖 [读第 15 章下](../../chapters/15b-python-files-json.md)

## 这次实操要练什么

1. 请求 `GET /api/products`
2. 把 Body 写成文件再 `json.loads` 读回来
3. 确认 `items` 是列表，找出 `SKU-DEMO-001` 库存为 10

章内「教学数据检查脚本」仍要你自己写 `cart_cases.json`。这次实操只保证你会读接口 JSON。

## 最小命令

```bash
python3 practice/run.py 15-1
```

## 验收条件

- HTTP 200，3 件商品，鼠标 `stock=10`
- 写出 `validation/products.json` 与 `validation/latest.json`
