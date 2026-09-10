# Repository Inventory — 2026-09-10 全量审计

扫描根目录：`/Users/plong/Desktop/学习文件夹/软件测试class`

## 规模

| 项 | 数量 |
| --- | ---: |
| 文件（排除 .git / __pycache__ / .pyc） | 403 |
| Markdown | 140 |
| PNG | 103 |
| HTML | 91 |
| Python | 29 |
| JSON | 14 |
| TXT | 16 |
| 其他（css/js/sh/bat/ini/jmx/sqlite/log） | 10 |
| 教材章节（编号 1–22） | 22 |
| 章节 Markdown 文件（含索引+上下册） | 36 |
| 章节正文行数（chapters/*.md，不含 quizzes/assets） | ~13,900 |
| 全书 Markdown 行数 | 25,929 |
| 全书 Markdown 字符 | 694,807 |
| 代码围栏（全书 md） | 818 |
| 表格块（全书 md） | 389 |
| Markdown 链接 | 515 |
| Markdown 图片引用 | 122 |
| 示意图 PNG（chapters/assets/diagrams/ch*.png） | 85 |
| MiniShop 截图 | 9×2（chapters/assets 与 evidence 各一份） |
| 可运行 practice 目录 | 10 |
| 书面 practice 目录 | 2 |
| 阶段测验 | 7 |

## 学习顺序（正式，不是文件名顺序）

`01 → 02 → 03 → 07 → 04 → 05 → 06 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20 → 21 → 22`

## 章节 ↔ 文件映射

| 章 | 正文 | 上下册 | Practice | Quiz | 示意图 PNG |
| --: | --- | --- | --- | --- | ---: |
| 1 | `chapters/01-software-testing-intro.md` | — | `practice/01-observation-oracle-evidence/` | stage-1 | 6 |
| 2 | `chapters/02-software-development-process.md` | — | 章内 2-1 | stage-1 | 3 |
| 3 | `chapters/03-software-testing-classification.md` | — | 章内 3-1 | stage-1 | 5 |
| 4 | `chapters/04-requirements-analysis-and-static-testing.md` | 04a, 04b | `practice/04-requirement-review/` | stage-2 | 5 |
| 5 | `chapters/05-test-case-design.md` | — | `practice/05-qty-boundary/` | stage-2 | 8 |
| 6 | `chapters/06-bug-and-test-management.md` | 06a, 06b | `practice/06-bug-report/` | stage-2 | 5 |
| 7 | `chapters/07-web-basics.md` | — | 章内 7-1 + `07-html-lab.html` | stage-1 | 5 |
| 8 | `chapters/08-web-functional-testing.md` | 08a, 08b | `practice/08-privilege/` | stage-3 | 5 |
| 9 | `chapters/09-computer-network-and-http.md` | 09a, 09b | `practice/09-http-observe/` | stage-3 | 6 |
| 10 | `chapters/10-chrome-devtools.md` | — | 章内 10-1 | stage-3 | 3 |
| 11 | `chapters/11-linux.md` | — | `practice/11-log-grep/` | stage-4 | 3 |
| 12 | `chapters/12-database-and-sql.md` | 12a, 12b | `practice/12-sql-cross-check/` | stage-4 | 5 |
| 13 | `chapters/13-api-testing.md` | — | `practice/13-api-shapes/` | stage-5 | 4 |
| 14 | `chapters/14-postman.md` | — | 章内 14-1 + Postman JSON | stage-5 | 2 |
| 15 | `chapters/15-python-basics.md` | 15a, 15b | `practice/15-json-check/` | stage-5 | 4 |
| 16 | `chapters/16-pytest.md` | 16a, 16b | `practice/16-pytest-regression/` | stage-5 | 4 |
| 17 | `chapters/17-automation-overview.md` | — | 章内 17-1 | stage-6 | 2 |
| 18 | `chapters/18-performance-testing.md` | — | 章内 18-1 + `.jmx` | stage-6 | 4 |
| 19 | `chapters/19-minishop-project.md` | — | `practice/19-project-pack/` + `project/minishop/` | stage-6 | 3 |
| 20 | `chapters/20-interview.md` | — | 章内 20-1 | stage-7 | 1 |
| 21 | `chapters/21-job-hunting.md` | — | 章内 21-1 | stage-7 | 1 |
| 22 | `chapters/22-learning-path.md` | — | 章内 22-1 | stage-7 | 1 |

索引页（仅目录，约 15 行）：04 / 06 / 08 / 09 / 12 / 15 / 16。

## 全局文件（所有 Agent 必读）

- `README.md`
- `docs/COURSE_CONTROL.md`
- `docs/COURSE_OUTLINE_v1.2.md`
- `docs/LEARNING.md`
- `standards/QUALITY_STANDARD_v1.0.md`
- `practice/README.md`
- `practice/STATUS.md`
- `exercises/README.md`
- `project/minishop/README.md`
- `project/minishop/docs/PRD.md`

## MiniShop 关键路径

- 服务：`project/minishop/server.py`、`run.py`、`run.sh`、`frontend/`
- 文档：`docs/PRD.md`、`openapi.json`、`test-plan.md`、`test-cases.md`、`test-report.md`、`requirement-review.md`
- 测试：`tests/test_api.py`、`test_qty_rule.py`、`test_register.py`、`conftest.py`
- 缺陷：`bugs/BUG-001.md`
- Postman：`postman/MiniShop.postman_collection.json`
- JMeter：`jmeter/minishop-get-products.jmx`
- 证据：`evidence/`

## 已有审查（线索，不替代本次独立审计）

- `reviews/chapter-01-review.md` … `chapter-22-review.md`
- `reviews/_pedagogy-2026-09-10/`
- `reviews/_rereview-2026-09-09/`
- `reviews/full-course-audit-v1.2.md`
- `reviews/v1.2.1-rescore.md`
