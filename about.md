---
layout: default
title: About
permalink: /about/
---

<div class="prose max-w-3xl mx-auto px-6 py-12" markdown="1">


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

</div>