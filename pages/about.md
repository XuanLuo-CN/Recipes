---
layout: about
title: About
permalink: /about/
---

{::nomarkdown}
<style>
  .total-badge { background: #F53200; color: white; font-size: 13px; padding: 3px 8px; border-radius: 6px; font-weight: bold; }
  .section-num  { background: #e7e5e4; color: #78716c; font-size: 11px; padding: 2px 7px; border-radius: 5px; font-weight: bold; letter-spacing: 0.05em; }
</style>

<!-- INTRO CARD -->
<div class="bg-stone-50/60 border border-stone-200/80 rounded-2xl pt-5 pb-5 px-5 shadow-sm w-full mb-6">
  <div class="flex items-start space-x-3 w-full">
    <div class="flex-shrink-0 mt-0.5"><span class="total-badge">INTRO</span></div>
    <div class="flex-1 w-full flex flex-col items-start justify-start">
      <div class="flex flex-col md:flex-row md:items-baseline w-full gap-y-1">
        <span class="text-stone-800 text-xl sm:text-2xl font-bold tracking-wider flex-shrink-0">介绍</span>
        <span class="text-primary/40 text-xs hidden md:block select-none px-4">/</span>
        <span class="text-stone-400 text-xs italic font-serif tracking-wide">Intro</span>
      </div>
      <div class="flex items-center w-full mt-2 mb-4 px-1">
        <span class="rounded-full bg-stone-300 flex-shrink-0" style="width:3px;height:3px;"></span>
        <div class="flex-grow h-px bg-stone-200/80 mx-3"></div>
        <span class="rounded-full bg-stone-300 flex-shrink-0" style="width:3px;height:3px;"></span>
      </div>
      <p class="text-stone-700 text-sm leading-relaxed pl-1">
        欢迎来到Xuan的数字菜谱！这是一个高效录入、自动化设计和补全的个人菜谱网页。
      </p>
    </div>
  </div>
</div>

<!-- SECTION 01 · 自定义增强功能 -->
<div class="mb-8 mt-2">
  <div class="flex flex-col md:flex-row md:items-baseline gap-y-0.5 mb-3">
    <span class="section-num mr-3">01</span>
    <span class="text-stone-800 text-base font-bold tracking-wide">自定义增强功能</span>
    <span class="text-primary/40 text-xs hidden md:block select-none px-3">/</span>
    <span class="text-stone-400 text-xs italic font-serif tracking-wide">Enhanced Features</span>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8">
    <ul class="space-y-2 text-stone-700 text-sm leading-relaxed">
      <li><span class="text-primary/60 mr-2 font-mono text-xs">/</span><strong>自动计数</strong>：全站菜谱数量、分类标签实时统计一目了然。</li>
      <li><span class="text-primary/60 mr-2 font-mono text-xs">/</span><strong>智能排序</strong>：支持多维度排序，快速找到你想做的那道菜。</li>
      <li><span class="text-primary/60 mr-2 font-mono text-xs">/</span><strong>精致排版</strong>：针对中文字体与中英混排进行了深度视觉优化。</li>
      <li><span class="text-primary/60 mr-2 font-mono text-xs">/</span><strong>便捷浮窗</strong>：点击菜品直接弹出详细信息，无需切换页面。</li>
    </ul>
    <ul class="space-y-2 text-stone-400 text-sm leading-relaxed italic font-serif border-l border-stone-200 pl-6 mt-4 md:mt-0">
      <li>/ <strong>Live Count</strong>: Recipe and tag totals computed and displayed in real time.</li>
      <li>/ <strong>Smart Sort</strong>: Sort by date, Chinese title, or English title in one click.</li>
      <li>/ <strong>Fine Typography</strong>: Deep visual tuning for Chinese fonts and bilingual layout.</li>
      <li>/ <strong>Quick Preview</strong>: Click any recipe to open a modal — no page reload needed.</li>
    </ul>
  </div>
</div>

<!-- SECTION 02 · 怎么加一道新菜 -->
<div class="mb-8">
  <div class="flex flex-col md:flex-row md:items-baseline gap-y-0.5 mb-3">
    <span class="section-num mr-3">02</span>
    <span class="text-stone-800 text-base font-bold tracking-wide">怎么加一道新菜</span>
    <span class="text-primary/40 text-xs hidden md:block select-none px-3">/</span>
    <span class="text-stone-400 text-xs italic font-serif tracking-wide">Adding a Recipe</span>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8">
    <div class="text-stone-700 text-sm leading-relaxed space-y-2">
      <p>本站最大的特色在于其<strong>近乎零成本的录入体验</strong>。当我想记录一道新菜时：</p>
      <ol class="list-none space-y-1 pl-1">
        <li><span class="text-primary/60 mr-2 font-mono text-xs">1.</span>我只需输入<strong>菜品做法步骤</strong>。</li>
        <li><span class="text-primary/60 mr-2 font-mono text-xs">2.</span>系统自动调用 <strong>Google Gemini</strong> 补全原料表、分类标签和配图。</li>
      </ol>
      <p class="text-stone-400 italic">「我只管做菜，剩下的全部交给 AI。」</p>
    </div>
    <div class="text-stone-400 text-sm leading-relaxed italic font-serif border-l border-stone-200 pl-6 mt-4 md:mt-0 space-y-2">
      <p>The standout feature is its <strong>near-zero-effort entry workflow</strong>. When I want to record a new dish:</p>
      <ol class="list-none space-y-1 pl-1">
        <li>/ I only type the <strong>cooking steps</strong>.</li>
        <li>/ <strong>Google Gemini</strong> auto-fills ingredients, tags, and a generated image.</li>
      </ol>
      <p>"I just cook and write — the AI handles the rest."</p>
    </div>
  </div>
</div>

<!-- SECTION 03 · 技术栈 -->
<div class="mb-10">
  <div class="flex flex-col md:flex-row md:items-baseline gap-y-0.5 mb-3">
    <span class="section-num mr-3">03</span>
    <span class="text-stone-800 text-base font-bold tracking-wide">技术栈</span>
    <span class="text-primary/40 text-xs hidden md:block select-none px-3">/</span>
    <span class="text-stone-400 text-xs italic font-serif tracking-wide">Tech Stack</span>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8">
    <div class="text-stone-700 text-sm leading-relaxed space-y-3">
      <div>
        <p class="text-xs font-bold uppercase tracking-wider text-stone-400 mb-1">框架与主题</p>
        <p>Jekyll (Ruby) &nbsp;·&nbsp; Chowdown（深度魔改）</p>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-wider text-stone-400 mb-1">AI 引擎</p>
        <p>Google Gemini Flash / Pro</p>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-wider text-stone-400 mb-1">本地编译</p>
        <code class="text-xs bg-stone-100 px-1.5 py-0.5 rounded text-stone-600">bundle exec jekyll serve --livereload</code>
      </div>
    </div>
    <div class="text-stone-400 text-sm leading-relaxed italic font-serif border-l border-stone-200 pl-6 mt-4 md:mt-0 space-y-3">
      <div>
        <p class="text-xs font-bold uppercase tracking-wider text-stone-400 mb-1 not-italic">Framework & Theme</p>
        <p>Jekyll (Ruby) &nbsp;·&nbsp; Chowdown (Modified)</p>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-wider text-stone-400 mb-1 not-italic">AI Engine</p>
        <p>Google Gemini Flash / Pro</p>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-wider text-stone-400 mb-1 not-italic">Local Build</p>
        <code class="text-xs bg-stone-100 px-1.5 py-0.5 rounded text-stone-600 not-italic">bundle exec jekyll serve --livereload</code>
      </div>
    </div>
  </div>
</div>

{:/nomarkdown}

{::nomarkdown}

  <div class="mb-8 mt-4 w-full">
    <div class="bg-stone-50/60 border border-stone-200/80 rounded-2xl pt-5 pb-5 px-5 shadow-sm w-full">
      <div class="flex items-start space-x-3 w-full">
        <div class="flex-shrink-0 mt-0.5">
          <span class="total-badge">LOG</span>
        </div>
        <div class="flex-1 w-full flex flex-col items-start justify-start">
          <div class="flex flex-col md:flex-row md:items-baseline w-full gap-y-1">
            <span class="text-stone-800 text-xl sm:text-2xl font-bold tracking-wider text-left flex-shrink-0">
              更新日志
            </span>
            <span class="text-primary/40 text-xs hidden md:block select-none text-center px-4">/</span>
            <span class="text-stone-400 text-xs italic font-serif tracking-wide block text-left">
              Changelog & History
            </span>
          </div>
          <div class="flex items-center w-full mt-2 mb-2 px-1">
            <span class="rounded-full bg-stone-300 flex-shrink-0" style="width: 3px; height: 3px;"></span>
            <div class="flex-grow h-px bg-stone-200/80 mx-3"></div>
            <span class="rounded-full bg-stone-300 flex-shrink-0" style="width: 3px; height: 3px;"></span>
          </div>
          <p class="text-xs text-stone-500 leading-relaxed pl-1 font-medium">
            记录 <span class="italic font-bold text-primary font-serif">Xuan's Recipes</span> 从零到一的进化轨迹：精进烹饪，沉淀代码。
          </p>
        </div>
      </div>
    </div>
  </div>
  
  <div class="relative pl-6 border-l-2 border-stone-200/60 space-y-10 ml-4 mt-8">

    <div class="relative">
      <span class="absolute -left-[31px] top-1.5 bg-primary animate-pulse w-3 h-3 rounded-full border-2 border-white shadow-sm"></span>
      <div class="flex flex-col gap-1.5">
        <div class="flex items-baseline gap-2">
          <h3 class="text-lg font-bold text-stone-800">2026-05-20</h3>
          <span class="text-xs text-stone-400 italic font-serif">Latest</span>
        </div>
        <ul class="list-none pl-0 space-y-2 text-stone-600 text-sm">
          <li class="flex items-start gap-2">
            <span class="text-primary font-bold flex-shrink-0">Added:</span>
            <span>Multi-dimensional sorting (Date/ZH/EN) for the main recipe index.</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="relative">
      <span class="absolute -left-[31px] top-1.5 bg-stone-400 w-3 h-3 rounded-full border-2 border-white shadow-sm"></span>
      <div class="flex flex-col gap-1.5">
        <div class="flex items-baseline gap-2">
          <h3 class="text-lg font-bold text-stone-800">2026-05-19</h3>
          
        </div>
        <ul class="list-none pl-0 space-y-2 text-stone-600 text-sm">
          <li class="flex items-start gap-2">
            <span class="text-primary font-bold flex-shrink-0">Added:</span>
            <span>Global Tags page for dynamic recipe filtering.</span>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-purple-600 font-bold flex-shrink-0">Changed:</span>
            <span>Optimized local build pipeline with Jekyll LiveReload and Tailwind CLI.</span>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-amber-600 font-bold flex-shrink-0">Fixed:</span>
            <span>Sidebar routing bug that incorrectly redirected to the root domain.</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="relative">
      <span class="absolute -left-[31px] top-1.5 bg-stone-400 w-3 h-3 rounded-full border-2 border-white shadow-sm"></span>
      <div class="flex flex-col gap-1.5">
        <div class="flex items-baseline gap-2">
          <h3 class="text-lg font-bold text-stone-800">2026-05-18</h3>
          
        </div>
        <ul class="list-none pl-0 space-y-2 text-stone-600 text-sm">
          <li class="flex items-start gap-2">
            <span class="text-purple-600 font-bold flex-shrink-0">Changed:</span>
            <span>Applied comprehensive bilingual (EN/ZH) localization across all Markdown files.</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="relative">
      <span class="absolute -left-[31px] top-1.5 bg-stone-400 w-3 h-3 rounded-full border-2 border-white shadow-sm"></span>
      <div class="flex flex-col gap-1.5">
        <div class="flex items-baseline gap-2">
          <h3 class="text-lg font-bold text-stone-800">2026-05-17</h3>
          
        </div>
        <ul class="list-none pl-0 space-y-2 text-stone-600 text-sm">
          <li class="flex items-start gap-2">
            <span class="text-purple-600 font-bold flex-shrink-0">Refactored:</span>
            <span>Replaced traditional sub-page routing with modal UI for recipe displays.</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="relative">
      <span class="absolute -left-[31px] top-1.5 bg-stone-400 w-3 h-3 rounded-full border-2 border-white shadow-sm"></span>
      <div class="flex flex-col gap-1.5">
        <div class="flex items-baseline gap-2">
          <h3 class="text-lg font-bold text-stone-800">2026-05-16</h3>
          
        </div>
        <ul class="list-none pl-0 space-y-2 text-stone-600 text-sm">
          <li class="flex items-start gap-2">
            <span class="text-purple-600 font-bold flex-shrink-0">Changed:</span>
            <span>Refined global typography, font scaling, and UI borders.</span>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-primary font-bold flex-shrink-0">Added:</span>
            <span>Roman numeral date parser and recipe creation dates in Front Matter.</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="relative">
      <span class="absolute -left-[31px] top-1.5 bg-stone-400 w-3 h-3 rounded-full border-2 border-white shadow-sm"></span>
      <div class="flex flex-col gap-1.5">
        <div class="flex items-baseline gap-2">
          <h3 class="text-lg font-bold text-stone-800">2026-03-10</h3>
          
        </div>
        <ul class="list-none pl-0 space-y-2 text-stone-600 text-sm">
          <li class="flex items-start gap-2">
            <span class="text-primary font-bold flex-shrink-0">Added:</span>
            <span>Automated script for dynamic tag generation.</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="relative">
      <span class="absolute -left-[31px] top-1.5 bg-stone-400 w-3 h-3 rounded-full border-2 border-white shadow-sm"></span>
      <div class="flex flex-col gap-1.5">
        <div class="flex items-baseline gap-2">
          <h3 class="text-lg font-bold text-stone-800">2026-03-02</h3>
          
        </div>
        <ul class="list-none pl-0 space-y-2 text-stone-600 text-sm">
          <li class="flex items-start gap-2">
            <span class="text-primary font-bold flex-shrink-0">Added:</span>
            <span>AI-driven workflow for automated recipe image generation.</span>
          </li>
          <li class="flex items-start gap-2">
            <span class="text-primary font-bold flex-shrink-0">Added:</span>
            <span>Global About page to present README and CHANGELOG</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="relative">
      <span class="absolute -left-[31px] top-1.5 bg-stone-800 w-3 h-3 rounded-full border-2 border-white shadow-sm"></span>
      <div class="flex flex-col gap-1.5">
        <div class="flex items-baseline gap-2">
          <h3 class="text-lg font-bold text-stone-800">2025-09-01</h3>
          
        </div>
        <ul class="list-none pl-0 space-y-2 text-stone-600 text-sm">
          <li class="flex items-start gap-2">
            <span class="text-primary font-bold flex-shrink-0">Added:</span>
            <span>Initial project repository and core Jekyll architecture.</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
{:/nomarkdown}
