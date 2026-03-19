// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	site: 'https://unclejoeyao666.github.io',
	base: '/cashcow-seo-site',
	integrations: [mdx(), sitemap()],
});
