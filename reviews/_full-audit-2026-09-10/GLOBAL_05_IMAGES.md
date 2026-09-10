# Global-05 Image Audit

审计员：Global-Agent-05（Image Audit Agent）  
日期：2026-09-10  
范围：`chapters/assets/**`、`project/minishop/evidence/screenshots/**`、全书 Markdown 图片引用  
方法：独立 `read_file` 打开全部 PNG；对照同名 HTML 源；对照 `server.py` schema / 校验顺序 / 种子数据；像素 diff 截图；对照 22 份 `CHAPTER_XX_AUDIT.md`。  
禁止改教材。本文件只写审计结论。

---

## 1. Coverage

| 资产类 | 数量 | 已打开 | 未打开 |
| --- | ---: | ---: | ---: |
| 示意图 PNG `chapters/assets/diagrams/ch*.png` | 85 | 85 | 0 |
| 示意图 HTML `chapters/assets/diagrams/ch*.html` | 85 | 85（全文抽取标题/lead/caption；点名串台图全文） | 0 |
| MiniShop 运行截图 `chapters/assets/*.png` | 9 | 9 | 0 |
| 证据副本 `project/minishop/evidence/screenshots/*.png` | 9 | 9（sha256 与 assets 逐文件相同） | 0 |
| 练习 HTML `07-html-lab.html` / `07-html-combo.html` | 2 | 2 | 0 |
| 章节 `![...](...)` 引用 | 102 | 102 | 0 |
| 断链（引用了但不存在） | 0 | — | — |

示意图全部 1320×780；运行截图 1280×900（`08-network-log.png` 为 1280×720）。HTML 与 PNG 文案一致，未发现「改了 HTML 忘重截」。

---

## 2. 特别核对（章节 Agent 已报串台 / 错图）

独立复审，不照抄。

| 点名资产 | 章节 Agent | 本轮独立证据 | 本轮裁决 |
| --- | --- | --- | --- |
| `ch18-p95` | CH18 MODIFY / P1 caption 串台 | 柱子与 H1 讲 100/110/120/200/800、平均 266；caption 整段是「并发人数 ≠ TPS。50 线程共用一个教学账号」——与 `ch18-tps-concurrency` 同题。柱高也不按比例（100 画成约 28% 高，800 为 100%）。 | **同意 MODIFY**。caption 必须换；建议柱上标 P50/尾部。 |
| `ch09-get-post` | CH09 MODIFY：`keyword=mouse` 在 MiniShop 空列表 | 图：`GET /api/products?keyword=mouse`。`server.py` 商品名是「无线鼠标/键盘/耳机」。第 13 章正文已写「搜 `mouse` 会空」。方法语义（safe/幂等、加密看 TLS）正确，MiniShop 例子会把学生带到空货架。 | **同意 MODIFY**。命题 KEEP，例子改 `keyword=鼠标` 或教学 URL。 |
| `ch12-tables` | CH12 REPLACE：自称种子但不完整 | 图写「MiniShop 种子数据如下」。实种：users 3 行（含 admin 13800138099）、products 3 行（含 SKU-DEMO-003 耳机 stock=3）、cart_items 3 行（含 user 2）。图只有 users×2、products×2、cart×2，无 `id` 列。caption 在讲主键/先 SELECT（邻图内容）。 | **同意 REPLACE**。 |
| `ch12-pk-fk` | CH12 REPLACE：`products.sku` 当主键 | 主键卡写「users.id、products.sku（唯一）」。DDL：`products.id INTEGER PRIMARY KEY`，`sku TEXT NOT NULL UNIQUE`；`cart_items.id` 也是主键。外键只画了 `user_id→users.id`，缺 `product_id→products.id`。正文 ASCII 图是对的，图是错的。 | **同意 REPLACE**。 |
| `ch13-four-shapes` | CH13 REPLACE：缺 sku，oracle 错 | 2–4 格 Body 为 `{"qty":null}` / `{""}` / `{"qty":"1"}`。`server.py` 先查 `"sku" not in data` → **400 `missing sku`**，不会走到图上的 `null qty` / `wrong type qty`。13.8 表每行都带 sku。 | **同意 REPLACE。本轮升为 P0**（会把接口 oracle 教错）。 |
| `ch15-venv` | CH15 MODIFY | 中列 `pip install -r requirements.txt`（正文教 `python3 -m pip`，本章明确不装包）；右列「第 19 章已备好」+ `run.py setup`；caption「审查未点击」。 | **同意 MODIFY**。 |
| `ch01-formula` | CH01 MODIFY：OpenAPI/pytest/SQL 超纲 | 观察卡堆 HTTP/SQL/JSON；判定卡 OpenAPI；证据卡 pytest。第 1 章正文表已收到「步骤+屏幕+BUG-001」。HTML=PNG。 | **同意 MODIFY**。公式句可留。 |
| `04-search-empty-bug001.png` | CH08 REPLACE / CH10 MODIFY-or-REPLACE / CH19 MODIFY | 与 `03-shop.png` 同为 1280×900；像素差 1595/1,152,000，bbox 仅搜索框边框（约 538,264–591,295）。两图关键字都空、都「共 3 件」、都已登录。默认 `refreshProducts()` 不带 keyword 也是三件。截图证明不了提交了空关键字。 | **同意 REPLACE**。HTTP 证据 `keyword=` / `keyword=%20` 才能当 BUG-001。 |
| `ch05-decision-table` | CH05 MODIFY：caption「超库存」 | 表是注册 201/400/409；caption「不要把『否』和『超库存』叠在同一条里」。正文紧接着是优惠券判定表，图是注册表。列 1 因「201 有 phone、无 token」把 2–4 挤没。注册 201 无 token 与 `server.py:332` 一致。 | **同意 MODIFY**。caption 串台属实；表本身可用。 |

---

## 3. 图片总表

结论列是本轮独立裁决。ID 沿用章节 `IMG-CHxx`；全局新项用 `IMG-G05`。

### 3.1 示意图（85）

| ID | 文件 | 引用 | 结论 | 一句话 |
| --- | --- | --- | --- | --- |
| IMG-CH01-001 | `ch01-formula` | 01 L52 | **MODIFY** | 脊柱对；通道超纲。 |
| IMG-CH01-002 | `ch01-static-dynamic` | 01 L105 | **MODIFY** | 「还没有页面」与「仓库 BUG-001」打架。 |
| IMG-CH01-003 | `ch01-qa-qc-testing` | 01 L166 | **KEEP** | QA/QC/Testing 分层正确。 |
| IMG-CH01-004 | `ch01-quality` | 01 L176 | **KEEP** | 未用 2011 旧名；可靠/安全合并可接受。 |
| IMG-CH01-005 | `ch01-net-holes` | 01 L214 | **MODIFY** | 渔网对；「错误密码 401」第 1 章超纲；BUG-001 不该在网外。 |
| IMG-CH01-006 | `ch01-tester-dev` | 01 L306 | **KEEP** | 开发/测试问句互补。 |
| IMG-CH02-001 | `ch02-where-test-sits` | 02 L64 | **MODIFY** | 五盒与 2.1 表不完全对齐；底栏抢讲 V 模型。 |
| IMG-CH02-002 | `ch02-vmodel` | 02 L143 | **MODIFY** | 配对表正确；不是 V 形——alt 已声明「不是字母形状」，不必整张 REPLACE。 |
| IMG-CH02-003 | `ch02-smoke-confirm` | 02 L252 | **MODIFY** | 三分法对；冒烟「接口能通」对第 2 章偏早。 |
| IMG-CH03-001 | `ch03-six-axes` | 03 L63 | **KEEP** | 六轴同时成立，打掉互斥标签。 |
| IMG-CH03-002 | `ch03-func-nonfunc` | 03 L97 | **KEEP** | 「订单有没有 status」是 v1.0 负向检查，可留。 |
| IMG-CH03-003 | `ch03-black-white` | 03 L135 | **KEEP** | 依据不是蒙眼。 |
| IMG-CH03-004 | `ch03-levels` | 03 L162 | **KEEP** | 四级对象变大；无支付 caption 正确。 |
| IMG-CH03-005 | `ch03-exploratory` | 03 L236 | **KEEP** | 时间盒+目标 vs 瞎点。 |
| IMG-CH04-001 | `ch04-four-terms` | 04a L49 | **MODIFY** | 分层可用；末卡折行。 |
| IMG-CH04-002 | `ch04-testable` | 04a L204 | **MODIFY** | 本章最有用；第 4 条把 10 过/11 拒挤一句。 |
| IMG-CH04-003 | `ch04-three-problems` | 04a L229 | **MODIFY** | 三类对；矛盾数字未标「虚构」。 |
| IMG-CH04-004 | `ch04-seven-scenes` | 04a L296 | **MODIFY** | 七抽屉有用；11 同时占异常和边界。 |
| IMG-CH04-005 | `ch04-trace` | 04a L345；04b L84 | **MODIFY** | 04B 可用；04A 画到 pytest 过早。 |
| IMG-CH05-001 | `ch05-point-case-data` | 05 L78 | **KEEP** | 点/用例/数据；10 位计数对。 |
| IMG-CH05-002 | `ch05-testcase-card` | 05 L112 | **MODIFY** | 任务卡好；ID 体系与章内不完全统一。 |
| IMG-CH05-003 | `ch05-priority` | 05 L136 | **MODIFY** | 反绝对化对；P1「四态」超前。 |
| IMG-CH05-004 | `ch05-equivalence` | 05 L156 | **MODIFY** | 四箱清楚；有效类脚注折行；缺「不以 1 开头」。 |
| IMG-CH05-005 | `ch05-boundary` | 05 L215 | **KEEP** | 8～16 尺正确；不要 8～20。 |
| IMG-CH05-006 | `ch05-decision-table` | 05 L264 | **MODIFY** | 注册表对；caption 超库存串台。 |
| IMG-CH05-007 | `ch05-scenario` | 05 L342 | **MODIFY** | 基本路径对；备选把管理员看库存塞进下单。 |
| IMG-CH05-008 | `ch05-state-door` | 05 L375 | **KEEP** | 标明教学模型 / v1.0 无状态机。 |
| IMG-CH06-001 | `ch06-error-defect-failure` | 06a L35 | **KEEP** | Error/Defect/Failure 链正确。 |
| IMG-CH06-002 | `ch06-severity-priority` | 06a L144 | **KEEP** | 两把尺子；反 S1=P0。 |
| IMG-CH06-003 | `ch06-bug-report` | 06a L210 | **MODIFY** | 示范写法已声明「不是现在超卖」；仍建议改用开放的 BUG-001。 |
| IMG-CH06-004 | `ch06-pass-rate` | 06b L26 | **KEEP** | 100% 盖不住范围遗漏。 |
| IMG-CH06-005 | `ch06-entry-exit` | 06b L95 | **KEEP** | 入口/出口；上线≠零缺陷。 |
| IMG-CH07-001 | `ch07-url` | 07 L126 | **MODIFY** | 拆分正确；教学 URL 与冻结 8765 并存需 caption 更醒目（已有一句）。 |
| IMG-CH07-002 | `ch07-dns` | 07 L192 | **KEEP** | 203.0.113.10 文档网段；解析≠店开着。 |
| IMG-CH07-003 | `ch07-client-server` | 07 L218 | **MODIFY** | 命题对；caption 抢讲前端/后端（邻图）。 |
| IMG-CH07-004 | `ch07-frontend-backend` | 07 L253 | **KEEP** | 摆盘/炒菜。 |
| IMG-CH07-005 | `ch07-html-css-js` | 07 L297 | **KEEP** | 指向 combo 页正确。 |
| IMG-CH08-001 | `ch08-browser-vs-server` | 08a L77 | **MODIFY** | 命题对；第二盒写死注册 400，08A 未教状态码。 |
| IMG-CH08-002 | `ch08-search` | 08a L193 | **MODIFY** | 缺陷判断对；R-SEARCH 盒把 400 写成预期过早；并指向弱截图 04。 |
| IMG-CH08-003 | `ch08-auth-layers` | 08b L35 | **KEEP** | Cookie/Session/Token 分层，打掉三选一。脚注「三层」vs 四条带可 P3。 |
| IMG-CH08-004 | `ch08-privilege` | 08b L168 | **MODIFY** | 401/横 403/纵 403 对；401 盒只写 Bearer。 |
| IMG-CH08-005 | `ch08-compat-responsive` | 08b L204 | **KEEP** | 换环境 ≠ 换宽度。 |
| IMG-CH09-001 | `ch09-ip-port` | 09a L104 | **KEEP** | 8765 门牌；ping ≠ 业务。 |
| IMG-CH09-002 | `ch09-tcp-knock` | 09a L139 | **KEEP** | SYN/SYN-ACK/ACK；握手 ≠ 登录。 |
| IMG-CH09-003 | `ch09-https-wrap` | 09a L212 | **MODIFY** | 分层对；「先握手」易与 TCP 撞词，改「TLS 握手」。 |
| IMG-CH09-004 | `ch09-get-post` | 09a L275 | **MODIFY** | 语义对；`keyword=mouse` 在 MiniShop 空。 |
| IMG-CH09-005 | `ch09-http-letter` | 09b L42 | **KEEP** | 401+脱敏密码；反 GET 不安全神话。 |
| IMG-CH09-006 | `ch09-status` | 09b L77 | **KEEP** | 2xx 仍看 Body；401≠403。 |
| IMG-CH10-001 | `ch10-three-panels` | 10 L79 | **KEEP** | 三抽屉取证。 |
| IMG-CH10-002 | `ch10-two-switches` | 10 L239 | **MODIFY** | 卡片对；caption 去讲 Copy as cURL。 |
| IMG-CH10-003 | `ch10-ttfb` | 10 L326 | **MODIFY** | 两段拆分对；caption 整段是 Preserve log（串台）。 |
| IMG-CH11-001 | `ch11-path` | 11 L127 | **MODIFY** | 当前目录对；`ls` 省略 frontend/data 等。 |
| IMG-CH11-002 | `ch11-grep-find` | 11 L228 | **KEEP** | grep 内容 / find 文件名。 |
| IMG-CH11-003 | `ch11-pipe` | 11 L271 | **KEEP** | `tail \| grep`。 |
| IMG-CH12-001 | `ch12-pk-fk` | 12a L62 | **REPLACE** | sku 不是主键。 |
| IMG-CH12-002 | `ch12-tables` | 12a L82 | **REPLACE** | 假种子 + caption 串台。 |
| IMG-CH12-003 | `ch12-join` | 12a L295 | **MODIFY** | INNER JOIN 这一行对；缺 LEFT JOIN。 |
| IMG-CH12-004 | `ch12-null` | 12a L334 | **MODIFY** | SQL NULL vs 空串对；caption 提前第 13 章四态。不升 REPLACE。 |
| IMG-CH12-005 | `ch12-select-first` | 12b L49 | **MODIFY** | 三步结构对；第三步跑到 qty=11。 |
| IMG-CH13-001 | `ch13-ui-vs-api` | 13 L153 | **MODIFY** | 分工对；后厨 Body 缺 sku。 |
| IMG-CH13-002 | `ch13-four-slots` | 13 L226 | **MODIFY** | 四格对；Body 把四态和 0/11 边界混写。 |
| IMG-CH13-003 | `ch13-four-shapes` | 13 L250 | **REPLACE** | MiniShop oracle 错（P0）。 |
| IMG-CH13-004 | `ch13-401-403` | 13 L275 | **KEEP** | `/api/admin/products` 403 路径真实存在。 |
| IMG-CH14-001 | `ch14-workspace` | 14 L67 | **MODIFY** | 三层对；caption「审查未点 Postman GUI」。 |
| IMG-CH14-002 | `ch14-token-relay` | 14 L270 | **MODIFY** | 接力对；caption「审查未点 GUI」。 |
| IMG-CH15-001 | `ch15-truthy` | 15a L163 | **MODIFY** | if qty 陷阱对；标题讲库存、卡片讲 qty。 |
| IMG-CH15-002 | `ch15-list-dict` | 15a L321 | **MODIFY** | JSON 形状对；caption 跑到 get/可变默认。 |
| IMG-CH15-003 | `ch15-venv` | 15b L30 | **MODIFY** | 命题对；步骤和「审查未点击」错。 |
| IMG-CH15-004 | `ch15-four-json` | 15b L211 | **MODIFY** | 四态对；caption 跑到 eval。 |
| IMG-CH16-001 | `ch16-roi` | 16a L31 | **KEEP** | 未说接口永远最高 ROI。 |
| IMG-CH16-002 | `ch16-collect` | 16a L91 | **MODIFY** | 收集规则对；caption 去讲 autouse（邻图）。 |
| IMG-CH16-003 | `ch16-fixture` | 16b L30 | **KEEP** | fixture vs parametrize。 |
| IMG-CH16-004 | `ch16-no-autouse` | 16b L80 | **MODIFY** | 命题对；caption「第 16 章强调过这件事」元叙述。 |
| IMG-CH17-001 | `ch17-pyramid` | 17 L78 | **KEEP** | 非 70/20/10；反接口永远最高。 |
| IMG-CH17-002 | `ch17-ui-cost` | 17 L176 | **KEEP** | 定位/等待/`time.sleep`。 |
| IMG-CH18-001 | `ch18-p95` | 18 L112 | **MODIFY** | 平均藏 800 对；caption 串台；柱不按比例。 |
| IMG-CH18-002 | `ch18-tps-concurrency` | 18 L137 | **KEEP** | 并发 ≠ TPS。 |
| IMG-CH18-003 | `ch18-load-stress` | 18 L174 | **KEEP** | Load/Stress/Soak 问句不同。 |
| IMG-CH18-004 | `ch18-jmeter-parts` | 18 L195 | **MODIFY** | 零件对；lead「审查未安装 JMeter」。 |
| IMG-CH19-001 | `ch19-workbench` | 19 L64 | **KEEP** | 能跑+契约+证据；37/1+BUG-001。 |
| IMG-CH19-002 | `ch19-qty-rule` | 19 L124 | **MODIFY** | 10/11 对；「教学服务只让 qty=1」现在时不稳。 |
| IMG-CH19-003 | `ch19-cross-check` | 19 L193 | **KEEP** | 四通道对 qty=11。 |
| IMG-CH20-001 | `ch20-five-beats` | 20 L65 | **MODIFY** | 五段骨架对；卡片过空。 |
| IMG-CH21-001 | `ch21-resume` | 21 L58 | **KEEP** | 个人项目 ≠ 任职；留白可裁。 |
| IMG-CH22-001 | `ch22-tiers` | 22 L76 | **MODIFY** | 三梯队有用；第一梯队已含「接口」，第二梯队又「基础接口自动化」。 |

### 3.2 运行截图（9 唯一文件 × 2 目录）

`chapters/assets/` 与 `evidence/screenshots/` **sha256 全等**。

| ID | 文件 | 章节引用 | 结论 | 一句话 |
| --- | --- | --- | --- | --- |
| IMG-CH10-004 / CH19-004 | `01-login.png` | 10 L396；19 L173；07/08 另有链接 | **KEEP** | 登录+注册同屏；个人实践声明可见。 |
| IMG-CH10-005 / CH19-005 | `02-login-fail.png` | 10 L400；19 L175；08 链接 | **KEEP** | 「登录失败」+密码圆点，未泄密。 |
| IMG-CH10-006 / CH19-006 | `03-shop.png` | 10 L404；19 L177 | **KEEP** | 登录后三件商品+购物车 qty=1。 |
| IMG-CH08-008 / CH10-007 / CH19-007 | `04-search-empty-bug001.png` | 10 L408；19 L179；08 链接 | **REPLACE** | 与 03 肉眼不可分，不能当 BUG-001。 |
| IMG-CH10-008 / CH19-008 | `05-cart-qty-11.png` | 10 L412；19 L181；08 链接 | **KEEP** | 框内 11 + `qty exceeds stock` + 列表仍 qty=1。 |
| IMG-G05-001 / CH19-009 | `06-register.png` | **章节 `![]` 未引用** | **DELETE** | 与 `01-login.png` 字节相同（37737，`910f31b0b0de…`）。覆盖矩阵把它当独立证据是错的。 |
| IMG-CH19-010 | `07-admin.png` | 19 L183 | **MODIFY** | 后台结构对（只列 id、无状态）；画面是「已加载 / 订单暂无」，alt「只列出订单 id」略满。 |
| IMG-CH10-009 / CH14-003 / CH19-011 | `08-network-log.png` | 10 L416；14 L291 | **KEEP** | 自题「不是 DevTools 面板」；路径/状态与实现一致。 |
| IMG-CH14-004 / CH16-005 / CH19-012 | `09-pytest-report.png` | 14 L293；16a L268；19 L248 | **KEEP** | 37 Passed / 1 Expected failure / 38 tests，对基线。明细折叠，教学价值中。 |

### 3.3 练习 HTML（非 PNG，但在 assets 根目录）

| ID | 文件 | 引用 | 结论 |
| --- | --- | --- | --- |
| IMG-CH07-006 / CH08-010 | `07-html-lab.html` | 07 L349/385；08a；practice 7-1 | **MODIFY**：密码无 8～16，与正文代码块/PRD `R-PASS` 不一致。提交文案诚实。 |
| IMG-G05-002 | `07-html-combo.html` | 07 L349 | **KEEP**：标明不连服务器；有价格 ¥99 不是 v1.0 字段，正文已声明验证只证明示例。 |

---

## 4. 漏图（引用了但不存在）

**零。** 102 条 `![...](assets/...)` 全部命中文件。

教学审查草稿里的 `ch04-two-rulers.png` **从未写入章节正文**，不是断链。若 04B 要钉「草案 vs PRD」两把尺子，这是建议新增，不是现行错误。

---

## 5. 未引用资产

| 文件 | 状态 |
| --- | --- |
| `chapters/assets/06-register.png` | 章节无 `![]`。`prd-coverage-matrix.md` 把它和 `01-login.png` 并列当两条证据。字节相同，文件名谎称「注册」。**DELETE 或改成 01 的别名说明。** |
| `project/minishop/evidence/screenshots/06-register.png` | 同上，证据目录副本。 |
| `evidence/screenshots/01–05,07–09` | 不是漏挂：它们是项目证据包，章节从 `chapters/assets/` 引用。与 assets 哈希一致，无双版本漂移。 |
| `diagrams/_theme.css` / `diagrams/README.md` | 源与说明，不应进正文。 |
| 全部 85 张 `ch*.png` | **均被章节引用**（`ch04-trace` 引用 2 次）。无「画了从未挂」的示意图。 |

章节**故意未挂**、但文件存在：

- 第 19 章未挂 `06-register.png`：合理（与 01 相同）。
- 第 19 章未挂 `08-network-log.png`：可挂进 19.6 作非 DevTools 旁证，不是错误。

---

## 6. HTML ↔ PNG 一致性

抽检原则：每张 PNG 的 H1 / 卡片 / caption 与 HTML 对照。

**结论：85/85 文案一致。** 未发现修源忘截图。

系统性问题不在漂移，在**源本身**：

1. caption 从邻图复制（见 G05-0004）。
2. 编辑备忘写进学生可见 caption/lead：「审查未点击 / 审查未点 GUI / 审查未安装 JMeter」（见 G05-0006）。
3. 画布统一 1320×780，内容往往只占上半，下半大片留白（P3，不单开 ISSUE）。

---

## 7. 【Agent Disagreement】

| 项 | 章节 Agent | 本轮 | 证据 | 建议总控 |
| --- | --- | --- | --- | --- |
| `ch02-vmodel` | REPLACE 成 V 形 | **MODIFY** | alt 与 lead 明确「价值不在字母 V」。表配对（需求↔验收、系统需求↔系统测试、设计↔集成、详细设计↔单元）正确。画 V 可能反而让学生记形状。 | 留表；可选角落加极简 V 轮廓，不要整张重画。 |
| `ch12-null` | REPLACE | **MODIFY** | SQL `IS NULL` vs `=''` vs 缺字段本身对。问题是 caption 把第 13 章 JSON 四态拽进来，不是图内 SQL 事实错误。 | 改 caption / 例子回到 users.display_name NULL，不必新图。 |
| `ch14-workspace` / `ch14-token-relay` | KEEP | **MODIFY** | caption 含「审查未点 Postman GUI」。CH14 写「未点 GUI，均正确」把编辑残留当成诚实声明。学生会读成课程未完成。 | 删「审查未…」，改成「本仓库不提供 GUI 截图，以 JSON 集合为准」。 |
| `ch18-jmeter-parts` | KEEP | **MODIFY** | lead：「审查未安装 JMeter。」与上条同类。零件内容可 KEEP。 | 删该句。 |
| `ch13-four-shapes` 等级 | CH13 作 REPLACE，放在图片节未单列 P0 | **P0** | `server.py` 先 `missing sku`。学生按图写 `{"qty":null}` 期望 `null qty`，实测 400 `missing sku`。13.8 表是对的，图会覆盖表。 | 按 13.8 表逐字节改 JSON 后重截。 |
| 缺 DevTools 真面板 | CH10 KEEP 诚实边界 | **同意 KEEP** | 作者用 `08-network-log.png` 自证不是面板。伪造 Chrome 皮肤更糟。 | 不要为分数补假面板。空搜索应补 **Network 或 URL** 证据，不是假 DevTools。 |

其余点名串台图：与章节 Agent **同向**，见 §2。

---

## 8. P0

```
## ISSUE
ID：G05-0001
文件：chapters/assets/diagrams/ch13-four-shapes.html ；ch13-four-shapes.png
章节：第 13 章
小节：13.8
精确位置：四张卡片的 JSON；插入 chapters/13-api-testing.md L250
原文：{"qty":null} → 400 null qty ；{"qty":""} / {"qty":"1"} → 400 wrong type qty
问题等级：P0
问题类别：IMG / ACC / HTTP
问题说明：图自称「MiniShop 购物车 Body」。校验顺序是 sku 先于 qty。缺 sku 的 Body 一律 400 missing sku，到不了图上的 qty 错误串。
为什么有问题：这是接口测试的 oracle。学生会按图写用例和断言，和实操 13-1、server.py、13.8 表三处打架。表是对的，图更大、更像标准答案。
依据：server.py L366–382（"sku" not in data → missing sku；其后才 missing qty / null qty / wrong type qty）；13.8 表每行都有 "sku":"SKU-DEMO-001"。本轮打开 PNG+HTML。
建议修改：四格都带 sku，与 13.8 表逐字节相同后重截。
推荐替换：
  {"sku":"SKU-DEMO-001"} → 400 missing qty
  {"sku":"SKU-DEMO-001","qty":null} → 400 null qty
  {"sku":"SKU-DEMO-001","qty":""} → 400 wrong type qty
  {"sku":"SKU-DEMO-001","qty":"1"} → 400 wrong type qty
```

---

## 9. P1

```
## ISSUE
ID：G05-0002
文件：chapters/assets/diagrams/ch12-pk-fk.html / .png
章节：第 12 章 12.3
精确位置：主键卡片
原文：users.id、products.sku（唯一）。没有它，两行鼠标会分不清。
问题等级：P1
问题类别：IMG / SQL
问题说明：把 UNIQUE sku 写成主键。cart_items 主键 id 只在 lead 出现，卡片没有。外键只画 user_id。
为什么有问题：12.3 正文 ASCII 是 users.id / products.id。图是学生第一眼。JOIN 会按 id 连，按 sku 当 PK 会写错 SQL。
依据：server.py L49–62；12a L69–71、L87–103。
建议修改：三表主键都是 id；sku 标 UNIQUE；外键两条都画。
```

```
## ISSUE
ID：G05-0003
文件：chapters/assets/diagrams/ch12-tables.html / .png
章节：第 12 章 12.4
精确位置：lead「MiniShop 种子数据如下」+ 三张表
原文：users 两行、products 两行（无 003）、cart_items 两行且无 id
问题等级：P1
问题类别：IMG / SQL
问题说明：自称种子，却少 admin、少耳机、少 Tester B 的车、少主键列。紧随其后的 12.4 DDL/正文是全量。caption 在讲主键和先 SELECT。
为什么有问题：学生 COUNT(*) / JOIN 会对不上库。这张图本该是全章最有用的库貌。
依据：server.py seed() L90–111。
建议修改：按 seed 全量重画；caption 只讲「页面一行来自三表」。
```

```
## ISSUE
ID：G05-0004
文件：ch18-p95、ch10-ttfb、ch10-two-switches、ch05-decision-table、ch12-tables、ch16-collect 的 html/png
章节：5 / 10 / 12 / 16 / 18
问题等级：P1
问题类别：IMG
问题说明：示意图 footer 出现系统性复制邻图命题：
  - ch18-p95 caption = 并发≠TPS（ch18-tps 的题）
  - ch10-ttfb caption = Preserve log / Disable cache（ch10-two-switches 的 H1）
  - ch10-two-switches caption = Copy as cURL
  - ch05-decision-table caption = 「否」和「超库存」（表是注册）
  - ch12-tables caption = 主键/先 SELECT（邻两张图）
  - ch16-collect caption = autouse / 401（ch16-no-autouse 的题）
为什么有问题：图注是零基础读图的第一句。文件名、alt、画面、图注四套口径时，图在帮倒忙。质量标准「图表确实帮助理解」。
依据：本轮抽取全部 85 条 caption，并逐张打开 PNG。
建议修改：caption 只复述本图 H1；按 diagrams/README 重截这 6 张。
```

```
## ISSUE
ID：G05-0005
文件：chapters/assets/04-search-empty-bug001.png （及 evidence 副本）
章节：08A 工作实战 3；10 逐步操作 6；19.5
精确位置：alt「空白搜索仍返回三件商品」/「空搜索 BUG-001」
问题等级：P1
问题类别：IMG / TEST
问题说明：与 03-shop.png 构图相同。像素 diff 只在搜索框边框（疑似焦点），关键字都空。登录后默认列表也是三件。
为什么有问题：BUG-001 的观察是「提交了空/空白 keyword 仍全量」。这张图观察不到提交，也不能看 URL/Network。三章都把它当缺陷证据。
依据：本机 PIL diff bbox (538,264)-(591,295)，1595 像素；app.js 默认 refreshProducts 不带 keyword。
建议修改：重拍：地址栏或 Network 可见 `keyword=` 或 `keyword=%20`，再配「共 3 件」。过渡期改挂 evidence/http/03-products-empty-keyword.txt。
```

```
## ISSUE
ID：G05-0006
文件：ch14-workspace.html/png；ch14-token-relay.html/png；ch15-venv.html/png；ch18-jmeter-parts.html/png
章节：14 / 15 / 18
问题等级：P1
问题类别：IMG / PED
问题说明：学生可见文案残留审计备忘：「审查未点 Postman GUI」「审查未点 GUI」「审查未点击」「审查未安装 JMeter」。
为什么有问题：教材口吻变成「我们还没点过」。第 15 章 Windows 激活正文已经写了，图注却说审查未点击。
依据：grep「审查未」仅这 4 个 html，PNG 已带出。
建议修改：删除四句；重截。不要用「审查未」代替「仓库不提供 GUI 截图」。
```

```
## ISSUE
ID：G05-0007
文件：chapters/assets/diagrams/ch15-venv.html / .png
章节：15.9
问题等级：P1
问题类别：IMG / SEQ
问题说明：中列 `pip install -r requirements.txt`；右列第 19 章 `run.py setup`。正文：本章不要装 requests/pytest，用 `python3 -m pip`，不要拿课程仓库当安装场。
为什么有问题：学生按图在仓库里 setup/装包，和第 15、16、19 章步骤冲突。叠加 G05-0006。
依据：15b L54–79；图中三列。
建议修改：三列改为 系统 pip 危险 / venv+python3 -m pip list / .venv 不进 Git。setup 留给第 16/19 章。
```

---

## 10. P2

```
## ISSUE
ID：G05-0008
文件：chapters/assets/06-register.png ；evidence/screenshots/06-register.png
章节：未挂入 ![] ；覆盖矩阵引用文件名
问题等级：P2
问题类别：IMG
问题说明：与 01-login.png 字节级相同。文件名表示「注册成功/注册页」，实际是登录+注册空白表单。
建议修改：DELETE 双份副本；覆盖矩阵只留 01-login.png。若要注册成功证据，需另拍 201 之后仍停在首页、无 token 的画面。
```

```
## ISSUE
ID：G05-0009
文件：ch09-get-post ；ch13-ui-vs-api
章节：09.8 / 13.4
问题等级：P2
问题类别：IMG / HTTP
问题说明：GET 例 keyword=mouse（MiniShop 空列表）；UI vs API 后厨例 `{"qty":11}` 缺 sku（会 missing sku，不是超库存 400）。
建议修改：GET 改 keyword=鼠标；后厨 Body 写成完整 sku+qty=11 并注明 Bearer。
```

```
## ISSUE
ID：G05-0010
文件：ch01-formula ；ch01-static-dynamic ；ch01-net-holes
章节：第 1 章
问题等级：P2
问题类别：IMG / PRE
问题说明：第 1 章图堆 OpenAPI、pytest、401、R-SEARCH 仓库对照。正文表已收敛，图未跟。
建议修改：第 1 章例子只留空白搜索 3 件 + 步骤/屏幕/缺陷单。通道名写「后面章节会加」。
```

```
## ISSUE
ID：G05-0011
文件：07-html-lab.html
章节：7 / 8
问题等级：P2
问题类别：IMG / PRE
问题说明：密码框只有 required，无 minlength/maxlength 8～16。08A 代码块和 PRD 是 8～16。
建议修改：lab 补 8～16，或正文一句「练习页只练 required，尺在项目页」。
```

```
## ISSUE
ID：G05-0012
文件：ch18-p95.png 柱高
章节：18.2
问题等级：P2
问题类别：IMG
问题说明：100 ms 柱约 28% 高、800 ms 100% 高，视觉比约 3.5×，真实 8×。文件名 p95，画面只标平均/中间/最慢，没有百分位刻度。
建议修改：按数值比例重画；在 120 与红柱侧标注「P50 / 尾部（教学上理解 P95）」。
```

```
## ISSUE
ID：G05-0013
文件：ch19-qty-rule ；07-admin.png
章节：19
问题等级：P2
问题类别：IMG
问题说明：qty-rule 标题「教学服务可能只让 qty=1」与第 13–16 章已打 v1.0 尺子的现在时冲突。07-admin 是空订单「暂无」，alt 说「只列出订单 id」（结构对，实例弱）。
建议修改：qty-rule 标题改「v1.0：等于库存 10 允许 / 11 拒绝」。admin 图补一笔真实订单 id，或改 alt「空库时订单区为暂无」。
```

---

## 11. P3

```
## ISSUE
ID：G05-0014
文件：全部 diagrams/ch*.png
问题等级：P3
问题类别：IMG
问题说明：统一 1320×780 导出，多数图内容在上 40–55%，下半空白。ch21-resume、ch11-pipe、ch03-exploratory 尤甚。
建议修改：按内容裁 canvas 或减小 window-size 后重截。不改文案。
```

```
## ISSUE
ID：G05-0015
文件：09-pytest-report.png
问题等级：P3
问题类别：IMG
问题说明：Summary 数字正确，测试明细全折叠，看不出 xfail 是哪条（BUG-001）。
建议修改：展开 xfailed 那一行再截，或正文指向 pytest-output.txt。
```

```
## ISSUE
ID：G05-0016
文件：无（缺图，不是断链）
问题等级：P3
问题类别：IMG
问题说明：建议新增而非现行错误：① 04B 草案 vs PRD 两把尺子（pedagogy 的 ch04-two-rulers）；② 12.10 LEFT JOIN 行复制；③ 空搜索的 URL/Network 帧（替代 04 弱截图）。不要补假 Chrome 面板。
```

---

## 12. 章节 Agent 漏报（本轮新发现或升级）

章节 Agent 已抓住绝大多数错图。全局增量：

1. **P0 升级**：`ch13-four-shapes` 不只是「和表不完全一样」，按 `server.py` 校验顺序会给出错误错误串。
2. **编辑残留「审查未…」四连**（14×2 + 15 + 18）：CH14/CH18 写成 KEEP，把备忘当诚实。
3. **caption 串台是跨章系统 bug**，不止 ch18-p95：至少再加 ch10-ttfb、ch05-decision-table、ch12-tables、ch16-collect。
4. **`06-register.png` 双重身份**：章节未挂是对的；覆盖矩阵仍当独立证据。
5. **ch13-ui-vs-api 缺 sku**：CH13 已报 MODIFY，与四态图同源偷懒，全局应一次修。
6. **柱状图比例**：CH18 报了 caption，未报柱高失真。

未漏的重要 KEEP（防止总控误杀）：`ch08-auth-layers`、`ch09-http-letter`、`ch09-status`、`ch13-401-403`、`ch17-pyramid`、`08-network-log.png`（诚实非面板）、`05-cart-qty-11.png`、`09-pytest-report.png` 数字。

---

## 13. 结论

| 统计 | 数量 |
| --- | ---: |
| 示意图 KEEP | 37 |
| 示意图 MODIFY | 45 |
| 示意图 REPLACE | 3（`ch12-pk-fk`、`ch12-tables`、`ch13-four-shapes`） |
| 截图 KEEP | 6（01/02/03/05/08/09） |
| 截图 MODIFY | 1（07-admin） |
| 截图 REPLACE | 1（04-search-empty） |
| 截图 DELETE | 1（06-register，assets+evidence 两份字节相同的副本） |
| 断链 | 0 |
| 未引用示意图 | 0 |
| P0 | 1 |
| P1 | 6 |
| P2 | 6 |
| P3 | 3 |

发布阻塞：**G05-0001（四态 oracle）必须改。** 其次同一批改主键图、假种子表、空搜索证据、caption 串台和「审查未」四句。概念图整体教学方向正确（反绝对化、分层、MiniShop 尺子），问题是复制图注和个别事实写错，不是缺图。

优先补丁顺序：

1. `ch13-four-shapes` JSON 与 13.8 对齐，重截。  
2. `ch12-pk-fk` + `ch12-tables` 按 DDL/seed 重画。  
3. 重拍 `04-search-empty-bug001.png`（URL 或 Network 可见 keyword）。  
4. 六张串台 caption + 四句「审查未」改源重截。  
5. 删除 `06-register.png` 两份副本。  

---

## 14. 执行记录

读过：

- `reviews/_full-audit-2026-09-10/GLOBAL_AGENT_BRIEF.md`、`AUDIT_AGENT_BRIEF.md`、`REPOSITORY_INVENTORY.md`、`UNIT_INVENTORY.md`、`AGENT_MAP.md`
- 22 份 `CHAPTER_XX_AUDIT.md` 图片节（对照，不替代取证）
- `chapters/assets/diagrams/` 全部 85 png + 85 html + README + `_theme.css`
- `chapters/assets/01–09` png、`07-html-lab.html`、`07-html-combo.html`
- `project/minishop/evidence/screenshots/` 9 png
- `project/minishop/server.py` schema / seed / cart 校验 / register 201 / admin 路径
- 各插入点章节 Markdown（alt 与上下文）

跑过：

- 全库 PNG sha256；assets 与 evidence 9 对 9 全等
- `01-login` == `06-register`（`910f31b0b0de`）
- `03-shop` vs `04-search-empty` 像素 diff（1595 px，仅搜索框边框）
- 全部 diagram 尺寸 1320×780
- 85 条 HTML caption 交叉匹配（检出 ch10-ttfb 引用 ch10-two-switches H1 等）
- grep「审查未」仅 4 个 html

外部核查：无（MiniShop 事实以仓库 `server.py` 为准；HTTP 方法语义与章节 Agent 引用的 RFC 9110 同向，本轮未再联网）。

未改任何教材文件。
