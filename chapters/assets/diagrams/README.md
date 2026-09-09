# 概念示意图

这些图是教材里的**讲解示意图**，不是流程图，也不是 MiniShop 运行截图。第 1～22 章每章至少有一张，嵌在对应概念旁边。全书脊柱图：`ch01-formula`（测试 = 观察 + 判定 + 证据）。

- 源文件：同名 `.html` + `_theme.css`（中文和数字按正文排版）
- 插入章节的是 `.png`，由本机 Chrome 无头截图生成
- 运行截图仍在上级目录：`01-login.png` 等

重新截图：

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in ch*.html; do
  "$CHROME" --headless --disable-gpu --hide-scrollbars --window-size=1320,780 \
    --screenshot="${f%.html}.png" "file://$PWD/$f"
done
```
