# OPERATIONS DASHBOARD — CashCow SEO Site

## 主目标
在 2026-03-20 09:00 Berlin 前，完成网站高价值内容扩张 + P0 可视化补图收口，确保站点可发布、可抓取、可转化。

## 当前状态（2026-03-20 03:10 Berlin）
- Deadline 剩余：约 5 小时 50 分
- Queue：40 active（P0=8 / P1=31 / P2=1），Archive DONE=23
- Queue health：PENDING=37，`QUEUE_EMPTY=false`
- Blockers：0
- Build 最近状态：152 pages OK
- 新任务生成：本轮未触发（现有 PENDING 充足，>15）
- 话题审计子 agent：本轮未触发（仅在新增 batch 时执行）

## 当前优先级
1. **P0 收口补图批次 9A-12B**：优先清空剩余 hero 图 / 占位内容 / 最终 build+push
2. **P1 正在执行的高 intent 对比内容**：T015 / T016 / T017
3. **P1 新内容队列**：优先横向对比类（X vs Y vs Z），再做 buyer-intent supporting article
4. **P2 优化**：内链结构增强（等 P0/P1 主路径稳定后再做）

## 执行策略（Joe 指定）
- ⭐ **最大并行**：尽量调动多的子 agent 并行完成任务，不要串行等待
- Exec 层：每轮 spawn 3 个子 agent 各写 1 篇文章
- Deep 层：补图任务按 5 篇一组并行，降低单任务超时风险
- 所有可拆分任务都应并行化

## 本轮规划动作
- 已将 4 个 >10 分钟的补图大任务拆成 8 个更小子任务（T059A-T062B）
- 已删除明显重复 / 占位任务：T020 / T021 / T022
- 已将 DONE 任务归档到底部，Active Queue 只保留可执行项
- 已按 P0 修复 > P1 新内容 > P2 优化完成重排

## 文章质量硬性要求（Joe 指定）
- ⭐ 每篇 review 必须配 HTML hero 图（inline CSS 渐变+标题+icon）
- ⭐ 优先写横向对比文章（X vs Y），对比用 HTML 图表展示
- ⭐ 所有付费工具必须详列价格套餐（全 tier），用 HTML pricing table

## 状态标志
- QUEUE_EMPTY=false
- URGENT=true
- DEADLINE=2026-03-20T09:00:00+01:00

## 约束
- 不得依赖 Anthropic API Key
- Git remote: git@github-tokenminer:unclejoeyao666/cashcow-seo-site.git
- Git user: unclejoe / 269553286+unclejoeyao666@users.noreply.github.com
