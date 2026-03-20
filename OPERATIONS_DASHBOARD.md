# OPERATIONS DASHBOARD — CashCow SEO Site

## 主目标
在 2026-03-20 09:00 Berlin 前，完成网站高价值内容扩张，确保站点可发布、可抓取、可转化。

## 当前状态（2026-03-20 08:47 Berlin）
- Deadline 剩余：约 13 分
- Queue：39 active（P1=38 / P2=1），已完成批次持续增长
- Queue health：PENDING=16，`QUEUE_EMPTY=false`
- Blockers：0
- Build 最近状态：164 pages OK
- 新任务生成：本轮未触发（PENDING=16 ≥ 15 阈值）
- 话题审计子 agent：本轮未触发（无新增 batch）
- 上轮完成：T016A/B/C（Automation 3篇）、T027（Avatar Video 3篇）、T013A/T013B/T013C/T013D/T013E/T013F/T013G（内链补强与结构修复前七批）

## 当前优先级（按 SEO 价值 / 商业意图 / 自主可行性排序）
1. **P1 高商业价值对比类**（优先执行）：
   - T045：Ahrefs AI vs SEMrush AI vs Moz + AI SEO Suites + AI Keyword Research
   - T046：HubSpot AI vs Salesforce Einstein vs Zoho AI + AI CRM + AI Lead Scoring
   - T028：Writesonic vs Rytr vs Anyword + AI Blog Writers + AI Content Generation
   - T034：Jasper vs Copy.ai vs Writesonic (Deep Dive) + AI Copywriting + AI Sales Copy
2. **P1 中等商业价值对比类**：
   - T030：Tidio vs Intercom vs Drift AI + AI Chatbots + AI Customer Service
   - T032：Mailchimp AI vs Klaviyo vs ActiveCampaign + AI Email + AI Subject Lines
   - T040：Shopify AI vs BigCommerce vs WooCommerce AI + AI Ecommerce + AI Product Descriptions
   - T042：Codeium vs Tabnine vs CodeWhisperer + AI Coding + AI Code Completion
3. **P1 增长型内容**：
   - T029：Pictory vs InVideo vs Lumen5 + AI Video Creators + Automated Video
   - T033：Murf vs Play.ht vs WellSaid Labs + AI Voice + TTS
   - T035：Stockimg.ai vs NightCafe vs Leonardo AI + AI Art + AI Image for Marketing
   - T037：Fireflies vs Grain vs Avoma + AI Sales Call + Revenue Intelligence
   - T044：Perplexity vs Google AI vs You.com + AI Search Engines + AI Research
   - T047：Tableau AI vs Power BI Copilot vs Looker + AI Analytics + AI Data Viz
   - T049：Gemini vs Claude vs ChatGPT (2026 Update) + AI for Students + AI Study Tools
4. **P2 优化**：T013 内链结构增强（待高价值新内容扩张完成后再做）

## 执行策略（Joe 指定）
- ⭐ **最大并行**：尽量调动多的子 agent 并行完成任务，不要串行等待
- Exec 层：每轮 spawn 3 个子 agent 各写 1 篇文章
- Deep 层：复杂内容 batch 拆成文章级子任务，降低单轮超时风险
- 所有可拆分任务都应并行化

## EXECUTION_LOG 最近20条概览（05:35 更新）
- shell 内容/校正层：12 success / 0 fail
- seo-sprint / sprint heartbeat：7 success / 0 fail（均为无 [QUICK] 任务可领）
- seo-watchdog：1 success / 0 fail
- `duration_s` 字段仍不稳定缺失；按完成时间戳粗估，内容 batch 节奏约 15-30 分钟/批，heartbeat 约 3-13 分钟/次

## 文章质量硬性要求（Joe 指定）
- ⭐ 每篇 review 必须配 HTML hero 图（inline CSS 渐变+标题+icon）
- ⭐ 优先写横向对比文章（X vs Y / X vs Y vs Z），对比用 HTML 图表展示
- ⭐ 所有付费工具必须详列价格套餐（全 tier），用 HTML pricing table

## 状态标志
- PROJECT_STATUS=PAUSED
- QUEUE_EMPTY=false
- URGENT=false
- DEADLINE=2026-03-20T09:00:00+01:00

## 约束
- 不得依赖 Anthropic API Key
- Git remote: git@github-t