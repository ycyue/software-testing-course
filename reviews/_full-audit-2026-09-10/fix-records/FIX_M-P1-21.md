# FIX RECORD
Audit ID：M-P1-21（CH15-0001 / G05-0006 caption / G05-0007）
原问题：`ch15-venv` 把本章练习画成立刻 `pip install -r requirements.txt` 并 `cd project/minishop && python3 run.py setup`；caption 残留「审查未点击」。与 15B「只建 venv、看 pip list，本章不装 requests/pytest、不拿课程仓库当安装场」互殴。
修改文件：
- `chapters/assets/diagrams/ch15-venv.html`
- `chapters/assets/diagrams/ch15-venv.png`
修改位置：三列卡片正文；caption。标题、lead、结构未改。
原内容：（摘录）
```
中列：python3 -m venv .venv 后 pip install -r requirements.txt
右列标题：第 19 章已备好
右列：cd project/minishop && python3 run.py setup
caption：示意图：.venv 不要进 Git。Windows 激活脚本见第 15 章，审查未点击。
```
修复后内容：（摘录）
```
左列：不要 sudo pip，也不要 --break-system-packages。
中列：python3 -m venv .venv 后 python3 -m pip list，本章只该看到 pip
右列标题：第 19 章再装
右列：本章不要在仓库里装包。
caption：示意图：.venv 不要进 Git。Windows 激活脚本见第 15 章。
```
为什么这样修：本章步骤只建练习目录 `.venv` 并用 `python3 -m pip list` 确认环境；装包不是本章动作。右列保留「第 19 章再装」作后置指针，但不画 `pip install -r` 或 `run.py setup`，避免学生按图提前装 pytest/requests 或把课程仓库当安装场。caption 删作者备忘「审查未点击」。
依据：15b §15.9（venv + `python3 -m pip list`、本章不装 requests/pytest）；Packaging User Guide / PEP 668（venv，不用 `--break-system-packages` / `sudo pip`）；FIX_PLAN M-P1-21；任务允许右列「第 19 章再装」。
是否影响其他章节：否。第 16 章练习目录装 pytest/requests、第 19 章 `run.py setup` 仍按原章。正文 `15b-python-files-json.md` 未改。
验证结果：HTML 已无 `pip install -r`、`run.py setup`、「审查未点击」。PNG 已按 `chapters/assets/diagrams/README.md` 用 Chrome headless `--window-size=1320,780` 重截（1320×780）；画面三列与 caption 与 HTML 一致。需重截 PNG：已重截，Coordinator 清单中的 `ch15-venv` 可复核。LOCAL REGRESSION：15.9 图注、术语 `python3 -m pip` / `.venv`、Markdown `![]` 路径均对齐。
状态：FIXED
