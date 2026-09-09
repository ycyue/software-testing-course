# 实操 6-1 📖：按模板写 BUG-001

> 配套第 6 章（上）。缺陷报告是给别人复核的证据，不是情绪宣泄。

← [实操目录](../README.md) · 📖 [读 06A](../../chapters/06a-bug-management.md)

这是**书面实操**。先跑 [实操 1-1](../01-observation-oracle-evidence/) 复现空搜索，再自己写一份报告（不要抄仓库那份当「我写的」）。

```text
exercises/chapter-06-bug-001.md
```

可先复制 [template.md](template.md)。对照：`project/minishop/bugs/BUG-001.md`。

## 这次实操要练什么

报告里必须能单独站住：环境、步骤、预期、实际、证据路径。标题要写出对象、条件和结果。

## 验收条件

1. 标题不是「搜索有问题」
2. 预期能追溯到 PRD `R-SEARCH`
3. 实际结果有 HTTP 或页面现象，不是「不对」
4. 证据能指到文件（自己跑的 `practice/01-.../validation/latest.json` 或仓库 `evidence/`）
5. **没有**写成已修复；严重程度与优先级分开写
