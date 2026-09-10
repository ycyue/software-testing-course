# 实操 4-1 📖：写一页 MiniShop 需求评审

> 配套第 4 章（下）。判定标准来自需求；需求不清，后面的用例都会漂。

← [实操目录](../README.md) · 📖 [读 04B](../../chapters/04b-minishop-requirement-review.md)

这是**书面实操**。`python3 practice/run.py 4-1` 只会指出这份说明，不能代替你写评审。把产出存到：

```text
exercises/chapter-04-minishop-requirement-review.md
```

可先复制 [template.md](template.md)。

## 这次实操要练什么

选注册、登录或购物车之一。必须分清：

- 04B 里的**教学草案**（验证码、8～20 位密码）不是 v1.0
- 项目契约以 `project/minishop/docs/PRD.md` 为准

## 验收条件

1. 写明评审对象和版本（教学草案 or PRD v1.0）
2. 至少 5 条问题，每条能标成歧义 / 遗漏 / 矛盾 / 不可测试
3. 七类场景里至少覆盖功能、异常、边界、权限四类测试点
4. 有需求 ID → 测试点 ID 的追踪表
5. **没有**把验证码、优惠券、订单状态机、8～20 位密码写进 v1.0 已确认规则

评 v1.0 时，模板「已确认规则」只许抄 `project/minishop/docs/PRD.md` 已有句。覆盖矩阵里的「不落库」、HTTP 400、失败保持原值都不是 PRD 原文，不要抄进该表。评教学草案则该表可空。
