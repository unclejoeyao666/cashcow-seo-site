# OPERATIONS DASHBOARD — CashCow SEO Site

## 主目标
在 2026-03-20 09:00 Berlin 前，完成网站高价值内容扩张 + P0 可视化补图收口，确保站点可发布、可抓取、可转化。

## 当前状态（2026-03-20 04:27 Berlin）
- Deadline 剩余：约 4 小时 33 分
- Queue：26 active（P0=0 / P1=25 / P2=1），Archive DONE=41
- Queue health：PENDING=26，`QUEUE_EMPTY=false`
- Blockers：0
- Build 最近状态：152 pages OK
- 新任务生成：本轮未触发（现有 PENDING 充足，>15）
- 话题审计子 agent：本轮未触发（无新增 batch）

## 当前优先级
1. **P1 高 intent 对比内容第一梯队**：T016A
2. **P1 buyer-intent supporting 内容第二梯队**：T016B / T016C
3. **P1 新内容储备队列**：优先横向对比类（T045 / T046 / T040 / T030 / T044 / T049），其后再做 supporting article
4. **P2 优化**：T013 内链结构增强（待高价值新内容扩张完成后再做）

## 执行策略（Joe 指定）
- ⭐ **最大并行**：尽量调动多的子 agent 并行完成任务，不要串行等待
- Exec 层：每轮 spawn 3 个子 agent 各写 1 篇文章
- Deep 层：复杂内容 batch 拆成文章级子任务，降低单轮超时风险
- 所有可拆分任务都应并行化

## 本轮规划动作
- 已读取 TASK_QUEUE / BLOCKERS / OPERATIONS_DASHBOARD / PROGRESS，并检查 EXECUTION_LOG 最近20条
- 已确认队列充足：无需新增 batch，避免无意义扩容
- 已将 3 个 >10 分钟的新内容 batch（T015 / T016 / T017）拆成 9 个文章级子任务（T015A-T017C）
- 已把 Active Queue 中残留的 DONE 子任务 T059A-T062B 移入 Archive
- 已删除明显重复的 PENDING batch：T023 / T024 / T025 / T026 / T031 / T036 / T038 / T039 / T041 / T043 / T048 / T050
- 已按收益接近度 / SEO 价值 / 自主可行性完成重排，优先对比类 buyer-intent 文章

## EXECUTION_LOG 最近20条概览
- `shell`：12 success / 0 fail
- `seo-sprint`：7 success / 0 fail
- `heartbeat`：1 success / 0 fail
- `duration_s` 字段在最近20条中基本缺失，无法稳定统计平均耗时
- 按时间戳粗估，最近完成节奏维持在约 1-5 分钟/项（补图 / 清理 / 核验类任务）

## 文章质量硬性要求（Joe 指定）
- ⭐ 每篇 review 必须配 HTML hero 图（inline CSS 渐变+标题+icon）
- ⭐ 优先写横向对比文章（X vs Y / X vs Y vs Z），对比用 HTML 图表展示
- ⭐ 所有付费工具必须详列价格套餐（全 tier），用 HTML pricing table

## 状态标志
- QUEUE_EMPTY=false
- URGENT=true
- DEADLINE=2026-03-20T09:00:00+01:00

## 约束
- 不得依赖 Anthropic API Key
- Git remote: git@github-tokenminer:unclejoeyao666/cashcow-seo-site.git
- Git user: unclejoe / 269553286+unclejoeyao666@users.noreply.github.com
