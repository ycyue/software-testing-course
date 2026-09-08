# 《软件测试从零基础到初级测试工程师》课程主控大纲 v1.2

## 定位

零基础 → 初级软件测试工程师 → 能独立完成基础测试项目 → 面试与求职准备。

学习方式：理论学习 + MiniShop 贯穿项目 + 工具实操 + 练习 + 项目作品。  
建议周期：全职 8～12 周；兼职 20～28 周。  
唯一主案例：MiniShop 电商系统。只能作为个人软件测试实践项目，不得伪造成企业工作经历。

## 最终能力链

理解软件与测试 → 理解研发流程和测试生命周期 → 阅读需求并参与评审 → 拆解功能和设计用例 → 执行 Web 功能测试 → 提交和验证 Bug → 回归测试 → 理解 HTTP 和认证状态 → 使用 DevTools → Linux 日志排障 → SQL 数据验证 → 阅读 OpenAPI → 使用 Postman → Python 数据处理 → requests + pytest 接口自动化 → 完成 MiniShop 测试项目 → 形成简历和面试材料。

## 22 章范围

### 第 1 章：软件测试入门

软件测试、测试价值、QA/QC/Testing、软件质量、七大测试原则、测试工程师日常工作、开发与测试的关系、岗位和职业发展。

### 第 2 章：软件研发流程与测试的位置

需求到上线、团队角色、SDLC、STLC、瀑布、V 模型、Agile/Scrum、测试左移和右移、Git 基础。传统阶段式流程中动态测试往往集中在编码后的测试阶段，但需求和设计工作产品可以更早接受评审。

### 第 3 章：软件测试分类体系

功能/非功能、黑盒/白盒/灰盒、单元/集成/系统/验收、手工/自动化、回归、冒烟、探索性、兼容性、性能和安全基础。安全内容只用于自有或明确授权环境。

### 第 4 章：测试需求分析与静态测试

测试需求分析、静态/动态测试、测试提前介入、需求评审、PRD 阅读、可测试性、歧义/遗漏/矛盾、功能/异常/边界/用户/数据/权限场景，以及 MiniShop 注册、登录、购物车需求评审。

### 第 5 章：测试用例设计

测试点、用例组成、优先级、等价类、边界值、判定表、因果图、场景法、状态迁移、错误推测、综合设计、用例评审。P0/P1/P2/P3 仅为课程项目约定，真实组织标准优先。

### 第 6 章：Bug、缺陷管理与测试管理基础

Bug 生命周期、状态、Severity/Priority、Bug 报告、无法复现、争议 Bug、偶现 Bug、Jira/禅道/TAPD、测试计划、范围、策略、入口/出口标准、进度、指标、风险、环境和配置管理。状态和等级均为常见示例，不是全球统一标准。

### 第 7 章：Web 基础

浏览器访问流程、URL、域名、DNS、客户端/服务器、前端/后端、HTML/CSS/JavaScript、浏览器渲染基础。

### 第 8 章：Web 功能测试

页面元素、表单、输入框、链接、搜索、分页、上传、下载、注册、登录、Cookie、Session、Session ID、Token、Bearer Token、权限、兼容性、响应式和 MiniShop Web 测试。Cookie/Session/Token 属于不同层次概念，不描述为互相替代技术。

### 第 9 章：计算机网络与 HTTP

IP/Port、TCP/UDP、三次握手、HTTP、HTTPS/TLS、请求/响应、Method、GET/POST、状态码、Headers、Body 和登录请求。GET/POST 按 HTTP 语义、safe、idempotent、query、body 和 cache 解释，不使用错误的安全性和长度绝对化规则。

### 第 10 章：Chrome DevTools

Elements、Console、Network、请求定位、Request/Response、前后端问题、Preserve Log、Disable Cache、Copy as cURL、网络限速、Timing/TTFB、MiniShop 登录和慢加载定位。

### 第 11 章：Linux

终端、文件系统、pwd/ls/cd、mkdir/touch/cp/mv/rm、cat/less/head/tail、grep/find、ps/top/kill、chmod、curl、管道重定向、ssh/scp、df/du/free/which/echo/history、日志定位和 curl 接口测试。

### 第 12 章：数据库与 SQL

数据库、主键/外键、关系型/非关系型、CRUD、SELECT、WHERE、逻辑运算、排序、限制、去重、聚合、GROUP BY/HAVING、JOIN、NULL、INSERT/UPDATE/DELETE、事务、COMMIT/ROLLBACK、MiniShop 数据验证。修改数据只在授权测试库执行，先 SELECT 验证范围。

### 第 13 章：接口测试

接口、API、REST、JSON、接口与 UI 测试差异、接口文档、OpenAPI/Swagger、Path/Query/Header/Body、缺失/空值/null/错误类型/边界、权限、幂等、一致性、登录和订单 API。

### 第 14 章：Postman

Workspace、Collection、Request、GET/POST、参数、Body、Headers、Response、Environment、Variables、Token、pm.test、pm.expect、Collection Runner 和 MiniShop 全流程。

### 第 15 章：Python 测试基础

变量、数据类型、字符串、list/dict/tuple/set、条件、循环、函数、模块、import、pip、文件、异常、JSON 和 MiniShop 数据实战。不追求成为 Python 开发工程师，重点服务测试自动化。

### 第 16 章：pytest 自动化

自动化适用场景和 ROI、pytest、测试函数、assert、fixture、scope、conftest、parametrize、requests、登录 API、Token fixture、数据驱动、目录结构和基础配置。

### 第 17 章：自动化测试进阶概览

测试分层、测试金字塔、接口自动化、Playwright/Selenium、UI 维护、Allure/pytest-html、CI/CD 和初级工程师能力边界。接口自动化优势必须结合场景说明，不能绝对化。

### 第 18 章：性能测试基础

性能测试、响应时间、吞吐量、TPS/QPS、并发、CPU/内存/磁盘/网络、负载/压力/耐久、JMeter 和初级岗位要求。

### 第 19 章：MiniShop 完整测试项目

真实可运行的 frontend、backend、database、docs、postman、tests、automation、logs、bugs 和 README。完成 PRD、需求评审、测试计划、风险、测试点、用例、功能测试、Bug、Postman、SQL、DevTools、Linux、接口、pytest、回归、报告、后台管理、项目总结和简历证据。

### 第 20 章：软件测试面试

自我介绍、项目介绍、测试理论、需求分析、测试方法、Bug、Web、HTTP、接口、SQL、Linux、Python、pytest、项目深挖和行为面试。所有答案采用“结论 → 原理 → 场景 → 示例 → 边界”。

### 第 21 章：软件测试求职

简历结构、技能清单、MiniShop 项目、项目描述、投递、面试复盘、薪资沟通和简历真实性原则。

### 第 22 章：学习路线总结

完整路线、必须掌握、高频使用、了解即可、入职后学习、官方资料和后续发展方向。

## 正式学习顺序

01 → 02 → 03 → 07 → 04 → 05 → 06 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20 → 21 → 22

Linux 与 SQL 是并列基础能力，不互相作为硬前置。

## 优先级

第一梯队：需求分析、测试用例、功能测试、Bug、Web、HTTP、DevTools、SQL、Linux、接口、Postman、MiniShop、面试。

第二梯队：Python、pytest、基础接口自动化。

第三梯队：性能、UI 自动化、CI/CD、高级安全和高级测试开发。

## 版本冻结

v1.2 后原则上停止新增大型基础章节。只有初级岗位高频、现有章节无法容纳、对项目能力有明显帮助且不会显著拖慢求职主线的内容，才允许加入；其他内容进入入职后进阶学习。
