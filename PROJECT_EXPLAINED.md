# CashCow SEO Site — 项目完整说明

_写于：2026-03-19 | 作者：Shell 🐚_

---

## 一、这个项目是干什么的？

一句话：**做一个AI工具评测网站，靠联盟营销（Affiliate Marketing）挣钱。**

用户搜索"best AI tools 2026"这类关键词 → 找到你的网站 → 读文章 → 点击文章里的推荐链接 → 去那些AI工具的官网注册/付费 → **你拿佣金**。

整个过程不需要你自己卖任何东西，不需要客服，不需要库存。

---

## 二、钱从哪里来？

**联盟营销佣金（Affiliate Commission）**

比如：
- 用户通过你网站的链接注册了 Jasper AI（$49/月）
- Jasper 付给你 **25% 递归佣金** = 每月 $12.25，只要用户续订就一直给
- 100个用户这样做 → 每月 $1225 被动收入

类似的联盟项目：

| 工具 | 佣金比例 | 类型 |
|---|---|---|
| Jasper AI | 25% | 递归月佣 |
| Copy.ai | 45% | 递归月佣 |
| ElevenLabs | 22% | 递归月佣 |

"递归"的意思是：用户只要不取消订阅，你每个月都收钱。这就是 **被动收入**。

---

## 三、SEO 是什么意思，为什么要这样建站？

**SEO = Search Engine Optimization（搜索引擎优化）**

核心逻辑：
1. 谷歌每天有数百万次"AI tools"相关搜索
2. 谷歌会把写得好、内容多、结构规范的网页排在前面
3. 如果你的文章出现在第1页 → 免费流量 → 免费点击 → 免费佣金

**为什么要创建这么多页面（80篇）？**

因为每一篇文章都是一个"入口"，针对不同的搜索词：
- "best AI coding assistants" → 一篇
- "ahrefs vs semrush" → 一篇
- "ai passive income ideas" → 一篇

每篇文章都可以独立排名，独立带来流量。**页面越多，被谷歌收录的机会越多，流量越大。**

---

## 四、技术框架是什么？为什么选它？

**框架：Astro（静态站点生成器）**

- 用 Markdown 写文章（`.md` 文件）
- `astro build` 命令把所有文章编译成纯 HTML/CSS
- 静态文件托管到 GitHub Pages（完全免费）

**为什么选 Astro？**
1. **免费托管** — GitHub Pages 零成本
2. **极快速度** — 纯静态页面，Lighthouse 性能100分，谷歌喜欢快的网站
3. **SEO友好** — 自动生成 sitemap（告诉谷歌有哪些页面）、canonical URLs、Open Graph
4. **无服务器** — 没有数据库、没有后端，出不了问题，零维护成本

**部署地址：** `https://joevonlong.github.io/ai-tools-hub`

**仓库：** `git@github-tokenminer:unclejoeyao666/cashcow-seo-site.git`

---

## 五、自动化在哪里？

项目里有个 `auto-publish.py` 脚本，设计逻辑是：

1. 从关键词列表里挑一个还没写过的主题
2. 调用 Claude API 生成一篇 SEO 文章
3. 保存为 `.md` 文件到 `src/content/blog/`
4. git commit + push → GitHub Actions 自动 build + deploy

**⚠️ 当前问题**：脚本依赖 `anthropic.Anthropic()` 直接调 Claude API Key，而 Joe 没有单独的 API Key（用的是订阅制）。需要改造为不依赖 Claude API 的内容生成方式（比如用本地模型、免费 API 或手动生成）。

---

## 六、整体赚钱路径总结

```
谷歌搜索
    ↓
用户找到 AIToolsHub 文章
    ↓
读文章（"Best AI Tools 2026"）
    ↓
点击文章里的联盟链接（带推荐ID）
    ↓
在 Jasper/Copy.ai/ElevenLabs 注册付费
    ↓
你每月收佣金（22%~45%，递归）
    ↓
被动收入 💰
```

**关键成功要素：**
1. 内容质量高 → 谷歌给排名
2. 文章数量多 → 覆盖更多搜索词
3. 联盟链接真实有效 → 点击能转化为佣金
4. 持续更新 → 谷歌喜欢活跃的网站

---

## 七、当前项目状态

| 项目 | 状态 | 说明 |
|---|---|---|
| 框架搭建 | ✅ 完成 | Astro + GitHub Pages |
| 文章数量 | ✅ 80篇 | 涵盖各类 AI 工具关键词 |
| GitHub Pages 部署 | ✅ 配置完成 | 待确认是否正常上线 |
| 联盟链接注册 | ❌ 占位符 | **需要去各平台注册拿真实ID** |
| 自动发文脚本 | ⚠️ 有但受阻 | 依赖 Claude API Key，需改造 |
| 谷歌收录/流量 | ❓ 未知 | 需提交 sitemap 到 Google Search Console |

---

## 八、下一步行动（优先级排序）

### 🔴 高优先级（直接影响能否赚钱）

1. **注册联盟账号，替换占位符链接**
   - Jasper AI: https://www.jasper.ai/affiliate
   - Copy.ai: https://www.copy.ai/affiliate
   - ElevenLabs: https://elevenlabs.io/affiliate
   - 拿到真实链接后替换 `YOUR_AFFILIATE_ID`

2. **提交 sitemap 到 Google Search Console**
   - Sitemap URL: `https://joevonlong.github.io/ai-tools-hub/sitemap-index.xml`
   - 这步做完谷歌才会开始收录你的文章

### 🟡 中优先级（提升效果）

3. **验证网站是否正常在线**
   - 访问 `https://joevonlong.github.io/ai-tools-hub` 检查

4. **改造自动发文脚本**
   - 移除 Claude API 依赖
   - 改用 Shell 直接写文章内容，或用免费模型

### 🟢 低优先级（长期优化）

5. 增加文章数量（目标 200+）
6. 添加内部链接结构
7. 建立外链（其他网站引用你）

---

## 九、预期收益时间线

| 阶段 | 时间 | 里程碑 |
|---|---|---|
| 起步 | 0-3个月 | 谷歌开始收录，流量 0→几百/月 |
| 成长 | 3-6个月 | 部分文章上首页，流量破千/月 |
| 变现 | 6-12个月 | 首笔联盟佣金到账 |
| 规模化 | 12个月+ | 月收入 $500-$2000（如果排名好） |

---

_此文档由 Shell 生成并维护。如有更新请同步修改。_
