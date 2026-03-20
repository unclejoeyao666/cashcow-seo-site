# OPERATIONS DASHBOARD — CashCow SEO Site

## 主目标
在 2026-03-20 09:00 Berlin 前，完成网站全面修复 + 持续增加高质量内容

## 当前优先级
1. ✅ 修复所有断链/404（3227→0，已完成）
2. ✅ 修复静态资源路径（已完成）
3. 持续新增高质量 AI 工具评测文章
4. 确保 build 零错误、内链测试通过

## 执行策略（Joe 指定）
- ⭐ **最大并行**：尽量调动多的子 agent 并行完成任务，不要串行等待
- Exec 层：每轮 spawn 3 个子 agent 各写 1 篇文章
- Deep 层：补图任务每批 spawn 10 个子 agent 各补 1 篇
- 所有可拆分任务都应并行化

## 文章质量硬性要求（Joe 指定）
- ⭐ 每篇 review 必须配 HTML hero 图（inline CSS 渐变+标题+icon）
- ⭐ 优先写横向对比文章（X vs Y），对比用 HTML 图表展示
- ⭐ 所有付费工具必须详列价格套餐（全 tier），用 HTML pricing table

## 状态标志
- QUEUE_EMPTY=false
- URGENT=true
- DEADLINE=2026-03-20T08:00:00+01:00

## 约束
- 不得依赖 Anthropic API Key
- Git remote: git@github-tokenminer:unclejoeyao666/cashcow-seo-site.git
- Git user: unclejoe / 269553286+unclejoeyao666@users.noreply.github.com
