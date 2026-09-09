# 实操 19-1 ★★：能指给人看的项目包

> 配套第 19 章。完整项目不是「我测过」，而是仓库里有契约、缺陷、自动化和证据。

← [实操目录](../README.md) · 📖 [读第 19 章](../../chapters/19-minishop-project.md)

## 这次实操要练什么

检查这些东西都在，并且 pytest 基线没被改掉：

- `docs/PRD.md` 含 `R-SEARCH` 与 `R-CART-10`
- `bugs/BUG-001.md` 仍按开放缺陷写
- OpenAPI 与 Postman 集合文件存在
- `37 passed, 1 xfailed`

需要先：

```bash
python3 project/minishop/run.py setup
```

## 最小命令

```bash
python3 practice/run.py 19-1
```

也可以直接：

```bash
cd project/minishop
python3 run.py test
```

## 验收条件

- 上列检查全 OK
- 你能用自己的话解释那 1 条 xfail 是 BUG-001，不是「测试挂了」
