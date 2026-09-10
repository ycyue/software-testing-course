# FIX RECORD
Audit ID：M-P1-36
原问题：16.6 写「登录很慢时再改为 `scope="session"`」。仓库 `token_a` 是 function；`reset_seed_db` 是 autouse，每测 `unlink` 数据库并重种，`sessions` 表里的旧 token 失效。按教材把 `token_a` 改成 session 后，认证用例会 401，看起来像 pytest 坏了。CH16-0004 / G03 E61。
修改文件：
- `chapters/16b-pytest-fixtures.md`
- `project/minishop/tests/conftest.py`（核对，未改）
修改位置：16.6 scope 表 `session` 行；紧随其后的 `token_a` 段；练习 5 标准答案。
原内容：（摘录）
```
| `session` | 整次 pytest | 登录贵、启动服务 |

`token_a` 用默认 `function` 最稳：每个需要它的测试自己登录一次。登录很慢时再改为 `scope="session"`。不要把 `token_a` 设成 `autouse=True`：…

5. `function`。`autouse` 会让无凭证测试先多登录一次；…
```
修复后内容：（摘录）
```
| `session` | 整次 pytest | 启动服务、只读配置；不要给会随清库失效的 token |

`token_a` 必须保持默认 `function`：每个需要它的测试在 `reset_seed_db` 之后自己登录一次。只要 autouse 的 `reset_seed_db` 还在每测清库，就不要改成 `scope="session"`——仓库会把 `sessions` 表打回种子，旧 token 立刻失效（本课程已复现为 401）。登录成本用 session 去摊，只适用于**不**每测清库的项目。不要把 `token_a` 设成 `autouse=True`：…

5. `function`。只要 `reset_seed_db` 还在每测清库，就不要改成 `scope="session"`，否则旧 token 会 401。`autouse` 会让无凭证测试先多登录一次；…
```
为什么这样修：删掉「慢了再改 session」这条可复制错误；明确禁令绑定 autouse 清库，而不是禁止一切 session fixture。`base_url` 仍可以 session（启动服务）。仓库 `token_a` 保持 `@pytest.fixture` 默认 function，不改测试代码。
依据：pytest fixture 更高 scope 先创建、更低 scope 后创建；`server.reset_db` 会 `unlink` 再重建 `sessions`；CH16-0004 本机：登录 200 → reset_db → 同 Bearer 打购物车 → 401。
是否影响其他章节：第 20 章已写 `token_a` 不是 autouse；未改。16.8 片段本身无 session。16.10 未动。
验证结果：`conftest.py` 中 `token_a` / `token_b` / `token_admin` 均无 `scope="session"`；`reset_seed_db` 仍 `autouse=True`。正文与练习 5 不再建议改 session。未跑 `run.py test`（会覆盖 `evidence/pytest-output.txt`）。
状态：FIXED
