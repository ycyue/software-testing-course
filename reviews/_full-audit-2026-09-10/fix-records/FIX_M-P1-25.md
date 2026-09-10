# FIX RECORD
Audit ID：M-P1-25
原问题：面试可背范文 + 测验 Q8 结构互斥（CH20-0001–0004、G04-0004、G08-0002）。
修改文件：`chapters/20-interview.md`；`chapters/quizzes/stage-7-career.md`
修改位置：20.3 计时自组句；20.4–20.14 提纲；20.16 STAR 映射；工作实战反抄/现场测；测验 7 Q8 答案
原内容：见 `FIX_CH20-0001.md`～`FIX_CH20-0004.md`、`FIX_G04-0004.md`、`FIX_G08-0002.md`。
修复后内容：范文改提纲；Q8 改回五段并一句映射 STAR；加 90 秒非 MiniShop 登录测试点（无范文）；20.3 不加可背口播。
为什么这样修：总控 D10：删可背满分段，加非 MiniShop 现场测，不因「像面试」再堆范文。
依据：MASTER_AUDIT M-P1-25 / D10；FIX_AGENT_BRIEF 硬约束 1–2。
是否影响其他章节：测验 7 Q8 与第 20 章对齐。未改第 21 章。
验证结果：LOCAL REGRESSION——五段名称与 Q1 一致；Q8 独立作答与新答案同构；qty=10/11、`/api/`、BUG-001、37/1 未改口径；无新增成段口播。
状态：FIXED
