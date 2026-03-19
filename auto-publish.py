#!/usr/bin/env python3
"""
SEO联盟站 — 全自动发文脚本
Shell 每天自动运行，生成+发布一篇AI工具评测文章
无需 Joe 介入

运行：python3 auto-publish.py
或通过 Cron 定时运行
"""

import anthropic
import httpx
import re
import json
import subprocess
import sys
from datetime import datetime, date
from pathlib import Path

# ── 配置 ────────────────────────────────────────────────
SITE_DIR = Path(__file__).parent / "site"
CONTENT_DIR = SITE_DIR / "src" / "content" / "blog"
AFFILIATE_LINKS = {
    "ElevenLabs": "https://elevenlabs.io/?via=YOUR_AFFILIATE_ID",  # 22% recurring
    "Jasper AI": "https://www.jasper.ai/?fpr=YOUR_ID",             # 25% recurring
    "Copy.ai": "https://www.copy.ai/?via=YOUR_ID",                  # 45% recurring
    "Cursor": "https://cursor.sh",
    "Claude": "https://claude.ai",
    "Perplexity": "https://www.perplexity.ai",
}

# 关键词列表（SEO目标）
KEYWORD_TOPICS = [
    "best AI writing tools 2026",
    "AI tools for developers",
    "Claude vs ChatGPT comparison",
    "ElevenLabs alternatives",
    "best AI voice generator",
    "AI automation tools for business",
    "AI newsletter tools",
    "best AI coding assistants",
    "Cursor IDE review",
    "AI tools for content creators",
    "Jasper AI alternatives",
    "Copy.ai review 2026",
    "AI tools for freelancers",
    "best AI summarizer tools",
    "how to use Claude API",
]

def get_unused_topic() -> str:
    """选择还没写过的主题"""
    published_file = SITE_DIR / "published_topics.json"
    
    if published_file.exists():
        with open(published_file) as f:
            published = set(json.load(f))
    else:
        published = set()
    
    unused = [t for t in KEYWORD_TOPICS if t not in published]
    if not unused:
        # 所有主题用完，从头开始（但保持随机性）
        unused = KEYWORD_TOPICS
        published = set()
    
    topic = unused[0]
    published.add(topic)
    
    with open(published_file, "w") as f:
        json.dump(list(published), f, indent=2)
    
    return topic


def generate_article(topic: str) -> dict:
    """用 Claude 生成 SEO 优化文章"""
    client = anthropic.Anthropic()
    
    # 生成文章
    prompt = f"""Write a comprehensive, SEO-optimized blog article about: "{topic}"

Requirements:
1. Title: Compelling, includes the main keyword
2. Length: 1500-2000 words
3. Structure: H2/H3 headers, bullet points where appropriate
4. SEO: Natural keyword usage, semantic keywords included
5. Tone: Expert but accessible, helpful and honest
6. Include: Specific tool comparisons, pros/cons, pricing info
7. CTA: End with actionable recommendation

Format as Markdown with frontmatter:
---
title: "YOUR TITLE"
description: "SEO meta description (150 chars max)"
pubDate: "{date.today().isoformat()}"
tags: ["ai-tools", "review", "automation"]
---

[article content here]

Important: Where relevant, naturally mention and link to:
- ElevenLabs (for voice/audio AI)
- Jasper AI (for writing AI)  
- Copy.ai (for marketing copy)
- Claude (for general AI assistant)
- Cursor (for coding AI)"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=3000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    content = message.content[0].text
    
    # 提取 frontmatter 和内容
    fm_match = re.search(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if fm_match:
        frontmatter = fm_match.group(1)
        article_body = fm_match.group(2)
    else:
        frontmatter = f'title: "AI Tools Guide: {topic.title()}"\ndescription: "Comprehensive guide to {topic}"\npubDate: "{date.today().isoformat()}"\ntags: ["ai-tools"]'
        article_body = content
    
    # 注入联盟链接
    for tool, link in AFFILIATE_LINKS.items():
        # 替换第一次出现的工具名为带链接的版本
        article_body = re.sub(
            rf'\b({re.escape(tool)})\b',
            rf'[\1]({link})',
            article_body,
            count=1
        )
    
    # 生成 slug
    title_match = re.search(r'title:\s*["\']?([^"\'\n]+)["\']?', frontmatter)
    title = title_match.group(1) if title_match else topic
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:60]
    
    return {
        "slug": slug,
        "frontmatter": frontmatter,
        "body": article_body,
        "topic": topic,
        "tokens": message.usage.input_tokens + message.usage.output_tokens,
    }


def save_article(article: dict) -> Path:
    """保存文章到内容目录"""
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    
    file_path = CONTENT_DIR / f"{article['slug']}.md"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"---\n{article['frontmatter']}\n---\n\n{article['body']}")
    
    return file_path


def publish_to_github(article_path: Path, article: dict):
    """git commit + push，触发 GitHub Pages 自动部署"""
    try:
        subprocess.run(["git", "-C", str(SITE_DIR), "add", str(article_path)], check=True)
        commit_msg = f"📝 Auto-publish: {article['topic'][:60]}"
        subprocess.run(["git", "-C", str(SITE_DIR), "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "-C", str(SITE_DIR), "push"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")
        return False


def log_result(article: dict, file_path: Path, published: bool):
    """记录运行日志"""
    log_file = Path(__file__).parent / "auto-publish.log"
    log_entry = {
        "date": datetime.now().isoformat(),
        "topic": article["topic"],
        "slug": article["slug"],
        "file": str(file_path),
        "tokens_used": article["tokens"],
        "published": published,
    }
    
    logs = []
    if log_file.exists():
        with open(log_file) as f:
            logs = json.load(f)
    
    logs.append(log_entry)
    
    with open(log_file, "w") as f:
        json.dump(logs[-30:], f, indent=2)  # 只保留最近30条
    
    print(f"{'✅' if published else '⚠️'} {article['topic']}")
    print(f"   File: {file_path.name}")
    print(f"   Tokens: {article['tokens']:,}")
    print(f"   Published: {published}")


def main():
    print(f"🚀 Auto-publish starting — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    # 1. 选题
    topic = get_unused_topic()
    print(f"📝 Topic: {topic}")
    
    # 2. 生成文章
    print("🤖 Generating article with Claude...")
    article = generate_article(topic)
    print(f"   Generated {len(article['body'])} chars, {article['tokens']} tokens")
    
    # 3. 保存文件
    file_path = save_article(article)
    print(f"   Saved: {file_path.name}")
    
    # 4. 发布（git push）
    print("📤 Publishing to GitHub Pages...")
    published = publish_to_github(file_path, article)
    
    # 5. 记录
    log_result(article, file_path, published)
    
    print("\n✅ Done!")
    return 0 if published else 1


if __name__ == "__main__":
    sys.exit(main())
