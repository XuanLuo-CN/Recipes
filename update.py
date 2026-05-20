import os
import re

# ================= 配置路径 =================
RECIPES_DIR = './_recipes'
IMAGES_DIR = './images'
CHANGELOG_PATH = './CHANGELOG.md'
README_PATH = './README.md'
ABOUT_PATH = './about.md'

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg')


def check_missing_images():
    print(" 1. 开始检查菜谱图片...")
    recipes = set()
    if os.path.exists(RECIPES_DIR):
        for f in os.listdir(RECIPES_DIR):
            if f.endswith('.md'):
                recipes.add(os.path.splitext(f)[0])
    else:
        print(f"❌ 错误：未找到菜谱目录 {RECIPES_DIR}")
        return

    images = set()
    if os.path.exists(IMAGES_DIR):
        for f in os.listdir(IMAGES_DIR):
            if f.lower().endswith(IMAGE_EXTENSIONS):
                images.add(os.path.splitext(f)[0])

    missing = recipes - images
    if missing:
        print("❌ 以下菜谱在 ./images 中没有找到同名图片：")
        for r in sorted(missing):
            print(f"   - {r}.md")
    else:
        print("✅ 完美！所有菜谱均已配备对应图片。")


def generate_html_from_changelog():
    """解析极简的 CHANGELOG.md 并生成华丽的 Tailwind HTML 时间轴"""
    if not os.path.exists(CHANGELOG_PATH):
        return ""

    with open(CHANGELOG_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    entries = []
    current_date = None
    current_items = []

    for line in lines:
        line = line.strip()
        if line.startswith('## '):
            if current_date:
                entries.append((current_date, current_items))
            current_date = line[3:].strip()
            current_items = []
        elif line.startswith('- ') and current_date:
            item_text = line[2:].strip()
            if ':' in item_text or '：' in item_text:
                separator = ':' if ':' in item_text else '：'
                tag, desc = item_text.split(separator, 1)
                current_items.append((tag.strip(), desc.strip()))
            else:
                current_items.append(("Updated", item_text))
    
    if current_date:
        entries.append((current_date, current_items))

    if not entries:
        return ""

    html_parts = []
    html_parts.append('''
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
''')

    for index, (date_str, items) in enumerate(entries):
        is_latest = (index == 0)
        is_oldest = (index == len(entries) - 1)
        
        if is_latest:
            dot_style = "bg-primary animate-pulse"
        elif is_oldest:
            dot_style = "bg-stone-800"
        else:
            dot_style = "bg-stone-400"

        html_parts.append(f'''
    <div class="relative">
      <span class="absolute -left-[31px] top-1.5 {dot_style} w-3 h-3 rounded-full border-2 border-white shadow-sm"></span>
      <div class="flex flex-col gap-1.5">
        <div class="flex items-baseline gap-2">
          <h3 class="text-lg font-bold text-stone-800">{date_str}</h3>
          { '<span class="text-xs text-stone-400 italic font-serif">Latest</span>' if is_latest else '' }
        </div>
        <ul class="list-none pl-0 space-y-2 text-stone-600 text-sm">''')
        
        for tag, desc in items:
            tag_color = "text-stone-600"
            if tag in ["Added", "✨ 新增"]: 
                tag_color = "text-primary"
            elif tag in ["Fixed", "🐛 修复"]: 
                tag_color = "text-amber-600"
            elif tag in ["Infrastructure", "⚙️ 环境"]: 
                tag_color = "text-emerald-600"
            elif tag in ["Localization", "🌐 翻译"]: 
                tag_color = "text-blue-600"
            elif tag in ["Refactored", "Changed", "🎨 重构", "🎨 优化"]: 
                tag_color = "text-purple-600"
            elif tag in ["Automation", "🤖 智能"]: 
                tag_color = "text-indigo-600"

            html_parts.append(f'''
          <li class="flex items-start gap-2">
            <span class="{tag_color} font-bold flex-shrink-0">{tag}:</span>
            <span>{desc}</span>
          </li>''')
            
        html_parts.append('''
        </ul>
      </div>
    </div>''')

    html_parts.append('\n  </div>')
    return "".join(html_parts)


def sync_to_about():
    print("\n 2. 开始整合 README 和 CHANGELOG 并同步到 about.md...")
    
    if not os.path.exists(ABOUT_PATH):
        print(f"❌ 错误：未找到 {ABOUT_PATH}")
        return

    # 获取 README 内容并包裹 HTML 样式
    readme_content = ""
    if os.path.exists(README_PATH):
        with open(README_PATH, 'r', encoding='utf-8') as f:
            raw_readme = f.read().strip()
            readme_content = f'  \n  <div class="prose max-w-3xl mx-auto mb-16" markdown="1">\n\n{raw_readme}\n\n  </div>\n'
    else:
        print(f"⚠️ 警告：未找到 {README_PATH}")

    # 获取 CHANGELOG HTML
    changelog_html = generate_html_from_changelog()

    # 将两部分内容无缝拼接
    final_content = f"\n{readme_content}\n{changelog_html}\n"

    # 读取 about.md
    with open(ABOUT_PATH, 'r', encoding='utf-8') as f:
        about_text = f.read()

# 寻找匹配锚点
    # 💡【在这里修改】：把空字符串改成明确的 html 标签标记
    start_pattern = r'<div id="about-content-start"></div>'
    end_pattern = r'<div id="about-content-end"></div>'

    match_start = re.search(start_pattern, about_text, re.IGNORECASE)
    match_end = re.search(end_pattern, about_text, re.IGNORECASE)

    match_start = re.search(start_pattern, about_text, re.IGNORECASE)
    match_end = re.search(end_pattern, about_text, re.IGNORECASE)

    if match_start and match_end and match_start.end() <= match_end.start():
        header = about_text[:match_start.end()]
        footer = about_text[match_end.start():]
        new_about_text = f"{header}{final_content}{footer}"

        if about_text.strip() != new_about_text.strip():
            with open(ABOUT_PATH, 'w', encoding='utf-8') as f:
                f.write(new_about_text)
            print("⚡ 检测到内容更新，已成功将 README 和 CHANGELOG 联合注入到 about.md！")
        else:
            print("✅ 检查完毕：about.md 内容已是最新，无需同步。")
    else:
        print("⚠️ 警告：在 about.md 中未找到标准的 ABOUT_CONTENT_START 和 END 锚点标记，注入终止。")


if __name__ == '__main__':
    print("=== Xuan's Recipes 自动化维护助手 ===")
    check_missing_images()
    sync_to_about()
    print("====================================")
