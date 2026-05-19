---
layout: default
title: About
permalink: /about/
---

<div class="px-6 pt-6 select-none flex items-center text-xs text-stone-400 font-sans tracking-wide">
  <svg class="w-3.5 h-3.5 mr-1.5 text-stone-300" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/>
  </svg>
  <span>此页面更新于：{{ site.time | date: "%Y年%m月%d日" }}</span>
</div>

<div class="prose prose-stone max-w-none px-6 py-6 text-stone-800 text-sm leading-relaxed">
  {% include_relative README.md %}
</div>