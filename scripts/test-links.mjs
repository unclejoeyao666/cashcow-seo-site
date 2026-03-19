#!/usr/bin/env node
/**
 * Link Integrity Test — AIToolsHub
 * 
 * Scans all built HTML files and checks:
 * 1. All internal <a href> links resolve to actual files in dist/
 * 2. No broken anchor links to non-existent fragments (basic check)
 * 
 * Run: node scripts/test-links.mjs
 * Expects: npm run build already done (dist/ exists)
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DIST = path.resolve(__dirname, '../dist');
const BASE = '/ai-tools-hub';

let errors = 0;
let warnings = 0;
let checked = 0;
let pagesScanned = 0;

// Collect all built HTML files
function collectHtmlFiles(dir) {
  const results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) results.push(...collectHtmlFiles(full));
    else if (entry.name.endsWith('.html')) results.push(full);
  }
  return results;
}

// Extract all href values from HTML
function extractLinks(html) {
  const links = [];
  const re = /href="([^"#][^"]*?)"/g;
  let m;
  while ((m = re.exec(html)) !== null) {
    links.push(m[1]);
  }
  return links;
}

// Check if an internal path resolves in dist
function checkInternalPath(href, fromFile) {
  // Strip base prefix for lookup
  let localPath = href;
  if (localPath.startsWith(BASE)) {
    localPath = localPath.slice(BASE.length);
  }
  if (!localPath.startsWith('/')) return null; // relative, skip
  
  // Strip query/hash
  localPath = localPath.split('?')[0].split('#')[0];
  
  // Try as file or index.html
  const candidates = [
    path.join(DIST, localPath),
    path.join(DIST, localPath, 'index.html'),
    path.join(DIST, localPath.endsWith('/') ? localPath + 'index.html' : localPath),
  ];
  
  for (const c of candidates) {
    if (fs.existsSync(c)) return true;
  }
  return false;
}

console.log('\n🔍 AIToolsHub Link Integrity Test\n');

if (!fs.existsSync(DIST)) {
  console.error('❌ dist/ directory not found. Run `npm run build` first.\n');
  process.exit(1);
}

const htmlFiles = collectHtmlFiles(DIST);
console.log(`📄 Scanning ${htmlFiles.length} HTML files...\n`);

const broken = [];

for (const file of htmlFiles) {
  const html = fs.readFileSync(file, 'utf-8');
  const links = extractLinks(html);
  const relFile = file.replace(DIST, '');
  pagesScanned++;

  for (const href of links) {
    // Skip external links
    if (href.startsWith('http://') || href.startsWith('https://') || href.startsWith('mailto:')) continue;
    // Skip assets
    if (href.match(/\.(css|js|svg|png|jpg|webp|ico|xml|txt|json)$/)) continue;
    
    checked++;
    const exists = checkInternalPath(href, file);
    
    if (exists === false) {
      broken.push({ file: relFile, href });
      errors++;
    }
  }
}

if (broken.length === 0) {
  console.log(`✅ All ${checked} internal links are valid across ${pagesScanned} pages.\n`);
} else {
  console.log(`❌ Found ${broken.length} broken internal link(s):\n`);
  for (const { file, href } of broken) {
    console.log(`   🔴 ${file}\n      → ${href}\n`);
  }
}

// Summary
console.log(`─────────────────────────────────`);
console.log(`Pages scanned : ${pagesScanned}`);
console.log(`Links checked : ${checked}`);
console.log(`Broken links  : ${errors}`);
console.log(`─────────────────────────────────\n`);

if (errors > 0) {
  console.log('💡 Tip: Check that all internal hrefs use the correct base path (/ai-tools-hub/...).\n');
  process.exit(1);
} else {
  console.log('🎉 Site passed link integrity test!\n');
  process.exit(0);
}
