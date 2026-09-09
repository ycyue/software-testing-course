# 实操 1-1 ★：去掉观察 / 判定 / 证据，还叫测试吗？

> 配套第 1 章。证明公式 **测试 = 观察 + 判定 + 证据** 不是口号。

← [实操目录](../README.md) · 📖 [读第 1 章](../../chapters/01-software-testing-intro.md)

## Code map

- **Run first:** `python3 practice/run.py 1-1`
- **Start here:** 屏幕上的三段输出（臂 A / B / C）
- **Core behavior:** 空白关键字搜商品；对照 PRD `R-SEARCH`
- **Verifier:** `python3 practice/run.py 1-1 --check`
- **可改的输入:** `--arm observe|oracle|full|all`
- **Skip on first pass:** `_minishop.py` 如何起服务

你不需要会 Python。把命令跑完，对着三段输出回答 README 末尾的问题即可。

## 这次实操要练什么

同一件 MiniShop 的事，三种做法：

| 臂 | 你做了什么 | 缺了什么 | 结果 |
| --- | --- | --- | --- |
| A 只有观察 | 调用 `GET /api/products?keyword=   ` | 判定 | 看到 3 件商品，说不清算不算 Bug |
| B 只有判定 | 读 PRD `R-SEARCH` | 观察 | 知道需求，不知道实现违不违反 |
| C 三者齐全 | 观察 + 对照需求 + 写下 JSON | — | 结论是 BUG-001，证据可复核 |

第 19 章仓库里这条缺陷是**故意开放**的。这次实操成功的标志是**复现它**，不是把它修掉。

## 最小命令

在仓库根目录：

```bash
python3 practice/run.py 1-1
```

等价于：

```bash
python3 practice/01-observation-oracle-evidence/main.py
```

脚本会在临时目录自己启动 MiniShop，不占用 `8765`，也不改 `project/minishop/data/`。

只看某一臂：

```bash
python3 practice/run.py 1-1 -- --arm observe
python3 practice/run.py 1-1 -- --arm oracle
python3 practice/run.py 1-1 -- --arm full
```

## 验收条件

- 臂 A 打印了 HTTP 状态和商品数量，且**没有**下「通过/失败」的结论。
- 臂 B 引用了 `R-SEARCH`，且**没有**发 HTTP。
- 臂 C 写明不符合 `R-SEARCH`，并写出 `practice/01-observation-oracle-evidence/validation/latest.json`。
- `python3 practice/run.py 1-1 --check` 通过。

## 读完请回答

1. 为什么「系统返回了 3 件商品」单独不能叫做测试结论？
2. 为什么只读 PRD 也不能说「已经测过搜索」？
3. 如果你发现了问题却不写证据，明天开发说「我这边是好的」，你怎么证明？

## 和仓库其他材料的关系

- 判定原文：[PRD R-SEARCH](../../project/minishop/docs/PRD.md)
- 缺陷单：[BUG-001](../../project/minishop/bugs/BUG-001.md)
- 已保存的 HTTP 摘录：[evidence/http/03-products-empty-keyword.txt](../../project/minishop/evidence/http/03-products-empty-keyword.txt)
