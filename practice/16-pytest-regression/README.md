# 实操 16-1 ★★：37 绿、1 条 xfail 是什么意思？

> 配套第 16 章。自动化不是「让条变绿」，而是把已经明确的判定变成可回归的证据。

← [实操目录](../README.md) · 📖 [读第 16 章上](../../chapters/16a-pytest-basics.md) · [第 16 章下](../../chapters/16b-pytest-fixtures.md)

## Code map

- **Run first:** `python3 practice/run.py 16-1`（需先 `python3 project/minishop/run.py setup`）
- **Core behavior:** 在 `project/minishop` 跑 pytest
- **Verifier:** 输出含 `37 passed` 与 `1 xfailed`
- **Skip on first pass:** fixture 怎么起临时端口

## 这次实操要练什么

- **passed**：你写过的断言在这次运行里成立。
- **xfailed**：已知 BUG-001，用例按预期失败并被标记。这是诚实记录，不是「测试写错了」，也不是「缺陷已修复」。

pytest 绿了，只证明脚本覆盖到的判定成立。库存有没有真改，仍要像实操 12-1 那样在库里看。

## 最小命令

```bash
python3 project/minishop/run.py setup   # 只需一次
python3 practice/run.py 16-1
```

也可以：

```bash
cd project/minishop
python3 run.py test
```

## 验收条件

- 输出含 `37 passed` 和 `1 xfailed`
- 你能指着 `bugs/BUG-001.md` 说出那 1 条 xfail 是什么
- 写出 `validation/latest.json`
