# FIX RECORD
Audit ID：M-P1-14
原问题：Preserve log / Timing 文案 / localhost 限速（CH10-0001–0004）。MiniShop 登录是 hidden 切换；Timing 应对齐 Chrome 现行 UI。
修改文件：
- chapters/10-chrome-devtools.md
- chapters/quizzes/stage-3-web.md
- chapters/assets/diagrams/ch10-ttfb.html
- chapters/assets/diagrams/ch10-two-switches.html
- chapters/assets/diagrams/ch10-ttfb.png
- chapters/assets/diagrams/ch10-two-switches.png
修改位置：见 FIX_CH10-0001.md、FIX_CH10-0002.md、FIX_CH10-0003.md、FIX_CH10-0004.md
原内容：（摘录）登录会清空 POST；面板名 Waiting (TTFB)；caption 串台；localhost 限速无预期。
修复后内容：（摘录）
- Preserve log 对象改为文档跳转（「后台」`/admin.html`）；登录是 hidden 切换。
- Timing 主名 Waiting for server response，旧 Waiting (TTFB) 作对照；≠ web.dev TTFB。
- caption 改回本题；概念图按 README 重截（非 DevTools 面板假图）。
- 本机 127.0.0.1 接口 Waiting 常仍短；禁止编造数据库慢。
- 测验 3 Q6：有文档跳转时才需要 Preserve log。
为什么这样修：四个 P1 都是零基础会在 Chrome 152 / MiniShop 上操作学错的点，按段修补，未整章重写。
依据：CHAPTER_10_AUDIT CH10-0001–0004；Chromium RequestTimingView.ts；MiniShop `app.js` / `index.html`。
是否影响其他章节：阶段测验 3 Q6/Q8。P2（第一眼线框、Elements 微操作、Command Menu 文案）本轮不修。
验证结果：LOCAL REGRESSION——前后文 Preserve log 不再要求登录必勾；Timing 面板标签均带现行名；两张图 caption 与命题一致；10.15 有 localhost 预期。未补假 Chrome 面板截图。
状态：FIXED
