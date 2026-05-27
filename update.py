import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

# ================= 配置路径 =================
RECIPES_DIR = './_recipes'
IMAGES_DIR = './images'


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




def get_new_recipes():
    result = subprocess.run(
        ["git", "status", "--porcelain", RECIPES_DIR],
        capture_output=True, text=True, encoding="utf-8"
    )
    files = []
    for line in result.stdout.strip().splitlines():
        if not line.strip():
            continue
        status = line[:2].strip()
        path = line[3:].strip().strip('"')
        if path.endswith(".md") and status in ("??", "A"):
            files.append(path)
    return files


def complete_new_recipes():
    new_files = get_new_recipes()
    if not new_files:
        print("\n 3. 没有新菜谱需要补全。")
        return False

    print(f"\n 3. 发现 {len(new_files)} 个新菜谱，开始调用 complete_recipes.py 补全...")
    sys.stdout.flush()
    result = subprocess.run(
        [sys.executable, "complete_recipes.py"],
        capture_output=False
    )
    if result.returncode != 0:
        print("❌ complete_recipes.py 执行失败，终止 push。")
        return False
    return True


def git_push():
    print("\n 4. 开始自动 git add / commit / push...")
    sys.stdout.flush()

    new_files = get_new_recipes()
    if not new_files:
        print("   没有需要提交的新菜谱。")
        return

    for f in new_files:
        subprocess.run(["git", "add", f], check=True)
        print(f"   git add: {f}")

    titles = []
    for f in new_files:
        name = os.path.splitext(os.path.basename(f))[0]
        titles.append(name)
    commit_msg = "Add recipes: " + ", ".join(titles)

    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push"], check=True)
    print("   Push 完成！")


if __name__ == '__main__':
    print("=== Xuan's Recipes 自动化维护助手 ===")
    check_missing_images()
    has_new = complete_new_recipes()
    if has_new:
        git_push()
    print("====================================")
