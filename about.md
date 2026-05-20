

欢迎来到Xuan的数字菜谱！这是一个专为高效录入、精致展示而设计的现代化个人菜谱微型系统。


---

### 自定义增强功能
在原本极简的 Chowdown 模板基础上，我深度定制了以下功能：

*   **自动计数**：全站菜谱数量、分类标签实时统计一目了然。
*   **智能排序**：支持多维度排序，快速捞出你想做的那道菜。
*   **精致排版**：针对中文字体、中英文混排以及烹饪步骤的间距进行了深度视觉优化。
*   **便捷浮窗**：在主页点击菜品直接弹出精致的高性能浮窗展示详细信息，无需频繁切换和刷新页面。

---
###  怎么加一道新菜
本站最大的特色在于其**近乎零成本的录入体验**。当我想记录一道新菜时：
1. 我只需输入**菜品做法步骤**。
2. 系统会自动调用 **Google Gemini** 进行全自动填充以下内容：
	1. **原料提取**：自动规范化生成精确的原料表。
	2. **自动归类**：智能分析并打上跨维度的标签。
	3. **视觉生成**：自动为这道菜量身定制并渲染出一张精美的插图。

真正实现了“我只管做菜和记录，剩下的排版和设计全部交给 AI”。

----

###  技术栈
Framework: Jekyll (Ruby)

Theme: Chowdown (Modified)

AI Engine: Google Gemini (Flash / Pro)

本地编译工具
* Environment: `Ruby & Bundler`
* CSS Compiler: `Tailwind CSS CLI`

编译流程与命令
1. 启动本地监听与热更新编译：
```bash
bundle exec jekyll serve --livereload
npx tailwindcss -i ./css/main.css -o ./css/compiled.css --watch

  <div class="mb-8 mt-4 w-full">
    <div class="bg-stone-50/60 border border-stone-200/80 rounded-2xl pt-5 pb-5 px-5 shadow-sm w-full">
      <div class="flex items-start space-x-3 w-full">
        <div class="flex-shrink-0 mt-0.5">
            <span class="total-badge" style="background-color: #f97316; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 0.75rem;">LOG</span>
          </div>
        <div class="flex-1 w-full flex flex-col items-start justify-start">
          <div class="flex flex-col md:flex-row md:items-baseline w-full gap-y-1">
            <span class="text-stone-800 text-xl sm:text-2xl font-bold tracking-wider text-left flex-shrink-0">
              更新日志
            </span>
            <span class="text-primary/40 text-xs hidden md:block select-none text-center px-4">/</span>
            <span class="text-stone-400 text-xs italic font-serif tracking-wide block text-left">
              Changelog
            </span>
          </div>
          <div class="flex items-center w-full mt-2 mb-2 px-1">
            <span class="rounded-full bg-stone-300 flex-shrink-0" style="width: 3px; height: 3px;"></span>
            <div class="flex-grow h-px bg-stone-200/80 mx-3"></div>
            <span class="rounded-full bg-stone-300 flex-shrink-0" style="width: 3px; height: 3px;"></span>
          </div>
          <div class="flex flex-col md:flex-row md:items-baseline w-full gap-y-1">
            <span class="text-xs text-stone-500 leading-relaxed pl-1 font-medium">
                精进烹饪，沉淀代码
            </span>
            <span class="text-primary/40 text-xs hidden md:block select-none text-center px-4">/</span>
            <span class="text-stone-400 text-xs italic font-serif tracking-wide block text-left">
              Cooking My Code...
            </span>
          </div>
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
---
layout: default
title: About
permalink: /about/
---

{::nomarkdown}

<div class="prose max-w-3xl mx-auto mb-16">
  </div>

<div class="mb-8 mt-4 w-full">
  </div>

<div class="relative pl-6 border-l-2 border-stone-200/60 space-y-10 ml-4 mt-8">
  </div>

{:/nomarkdown}
