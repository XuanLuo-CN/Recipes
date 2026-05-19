import os

# ================= 配置路径 =================
RECIPES_DIR = './_recipes'
IMAGES_DIR = './images'
README_PATH = './README.md'
ABOUT_PATH = './about.md'

# 常见图片格式后缀
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg')


def check_missing_images():
    print(" 1. 开始检查菜谱图片...")
    
    # 1. 获取所有菜谱的文件名（不含后缀）
    recipes = set()
    if os.path.exists(RECIPES_DIR):
        for f in os.listdir(RECIPES_DIR):
            if f.endswith('.md'):
                # 比如 'basil_beef.md' -> 'basil_beef'
                recipes.add(os.path.splitext(f)[0])
    else:
        print(f"❌ 错误：未找到菜谱目录 {RECIPES_DIR}")
        return

    # 2. 获取所有图片的文件名（不含后缀）
    images = set()
    if os.path.exists(IMAGES_DIR):
        for f in os.listdir(IMAGES_DIR):
            if f.lower().endswith(IMAGE_EXTENSIONS):
                # 比如 'basil_beef.jpg' -> 'basil_beef'
                images.add(os.path.splitext(f)[0])
    else:
        print(f"⚠️ 提示：未找到图片目录 {IMAGES_DIR}，将视所有菜谱为缺少图片。")

    # 3. 对比找出没有图片的菜谱
    missing = recipes - images

    if missing:
        print("❌ 以下菜谱在 ./images 中没有找到同名图片：")
        for r in sorted(missing):
            print(f"   - {r}.md")
    else:
        print("✅ 完美！所有菜谱均已配备对应图片。")


def sync_readme_to_about():
    print("\n 2. 开始检查 About 和 README 同步状态...")
    
    if not os.path.exists(README_PATH):
        print(f"❌ 错误：未找到根目录下的 {README_PATH}")
        return

    # 读取 README 内容
    with open(README_PATH, 'r', encoding='utf-8') as f:
        readme_content = f.read().strip()

    # 如果 about.md 还不存在，直接新建一个默认模版
    if not os.path.exists(ABOUT_PATH):
        print(f"📝 未找到 about.md，正在自动创建...")
        default_about = f'---\nlayout: default\ntitle: About\npermalink: /about/\n---\n\n<div class="prose max-w-3xl mx-auto px-6 py-12" markdown="1">\n\n{readme_content}\n\n</div>\n'
        with open(ABOUT_PATH, 'w', encoding='utf-8') as f:
            f.write(default_about)
        print("✅ about.md 已创建并同步了 README 内容！")
        return

    # 读取现有的 about.md
    with open(ABOUT_PATH, 'r', encoding='utf-8') as f:
        about_lines = f.readlines()

    # 寻找 <div> 的开头和 </div> 的结尾
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(about_lines):
        if '<div' in line and 'markdown="1"' in line:
            start_idx = i
        if '</div>' in line:
            end_idx = i

    # 如果找到了合法的 HTML 标签包裹圈
    if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
        # 提取保留的头部（Front Matter 和 <div> 标签行）
        header = "".join(about_lines[:start_idx + 1])
        # 提取保留的尾部（</div> 标签及之后的内容）
        footer = "".join(about_lines[end_idx:])

        # 拼接出期望的新文件内容
        new_about_content = f"{header}\n{readme_content}\n\n{footer}"

        # 读取当前完整的 about.md 做对比
        with open(ABOUT_PATH, 'r', encoding='utf-8') as f:
            current_about_content = f.read()

        # 检查是否一致
        if current_about_content.strip() != new_about_content.strip():
            with open(ABOUT_PATH, 'w', encoding='utf-8') as f:
                f.write(new_about_content)
            print("⚡ 检测到内容有差异，已成功把 README 更新到 about.md 的容器中！")
        else:
            print("✅ 检查完毕：about.md 的内容与 README 完全一致，无需更新。")
    else:
        print("⚠️ 警告：在 about.md 中没找到标准的 <div ... markdown=\"1\"> 或 </div> 标签结构！")
        print("为了安全起见，本次未覆盖。请确保 about.md 里包含这两行标签。")


if __name__ == '__main__':
    print("=== Chowdown 菜谱主页维护助手 ===")
    check_missing_images()
    sync_readme_to_about()
    print("=================================")
