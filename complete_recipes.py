# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
complete_recipes.py — 自动补全未 push 的菜谱文件

用法：
  python complete_recipes.py

依赖：
  pip install anthropic pyyaml

环境变量：
  ANTHROPIC_API_KEY — Anthropic API 密钥
"""

import os
import re
import sys
import subprocess
import json
from pathlib import Path


def load_env():
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

load_env()

sys.stdout.reconfigure(encoding="utf-8")

try:
    import anthropic
except ImportError:
    print("[ERROR] Missing dependency: pip install anthropic")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("[ERROR] Missing dependency: pip install pyyaml")
    sys.exit(1)

RECIPES_DIR = "_recipes"
MODEL = "claude-haiku-4-5-20251001"


def get_new_recipes():
    """找出 git 未追踪（??）或新增（A）的 _recipes/*.md 文件"""
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


def parse_frontmatter(content):
    """解析 YAML frontmatter，返回 (data_dict, raw_fm_str)"""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None, None
    fm_str = match.group(1)
    data = yaml.safe_load(fm_str)
    return data, fm_str


def is_incomplete(data):
    """返回缺失的字段列表"""
    missing = []
    if not data.get("tags"):
        missing.append("tags")
    if not data.get("ingredients"):
        missing.append("ingredients")
    dirs = data.get("directions", [])
    if not dirs or isinstance(dirs[0], str):
        missing.append("directions bilingual")
    return missing


def build_prompt(data):
    title_zh = data.get("title_zh", "")
    title_en_raw = data.get("title_en", "")
    directions_raw = data.get("directions", [])
    directions_str = "\n".join(f"- {d}" for d in directions_raw)

    return f"""你是中英双语菜谱助手。根据以下信息补全菜谱的缺失字段。

菜名（中文）：{title_zh}
菜名（英文，可能需要修正）：{title_en_raw}
烹饪步骤（中文原版）：
{directions_str}

严格返回如下 JSON，不要任何额外说明：
{{
  "title_en": "地道英文菜名（首字母大写，不用下划线）",
  "tags": [
    {{"zh": "标签中文", "en": "Tag English"}}
  ],
  "ingredients": [
    {{"zh": "食材中文", "en": "Ingredient English"}}
  ],
  "directions": [
    {{"zh": "步骤中文原文", "en": "Step English translation"}}
  ]
}}

规则：
1. title_en 必须是正规英文菜名（例如 "Beef Short Ribs with Peppers"，不要 "beef_short_ribs_with_pepper"）
2. tags 选 1-2 个，只能从以下选择，不得使用其他值：
   {"zh": "牛肉", "en": "Beef"}
   {"zh": "鸡肉", "en": "Chicken"}
   {"zh": "甜点", "en": "Dessert"}
   {"zh": "羊肉", "en": "Lamb"}
   {"zh": "猪肉", "en": "Pork"}
   {"zh": "海鲜", "en": "Seafood"}
   {"zh": "素菜", "en": "Vege"}
3. ingredients 从步骤里提取全部食材和调料，去重
4. directions 保留中文原文，英文要地道（不要逐字直译）
5. 所有 JSON 字符串用双引号"""


def serialize_frontmatter(data):
    """将数据序列化为与现有菜谱格式一致的 frontmatter 字符串"""
    lines = ["---"]

    def q(s):
        return f'"{s}"'

    for key in ["layout", "title_zh", "title_en", "date", "image"]:
        val = data.get(key)
        if val is None:
            continue
        if key in ("layout", "date"):
            lines.append(f"{key}: {val}")
        else:
            lines.append(f"{key}: {q(val)}")

    for section in ["tags", "ingredients", "directions"]:
        items = data.get(section)
        if not items:
            continue
        lines.append("")
        lines.append(f"{section}:")
        for item in items:
            if isinstance(item, dict):
                first = True
                for k, v in item.items():
                    prefix = "- " if first else "  "
                    lines.append(f"{prefix}{k}: {q(v)}")
                    first = False
            else:
                lines.append(f"- {item}")

    lines.append("---")
    return "\n".join(lines) + "\n"


def complete_recipe(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    data, _ = parse_frontmatter(content)
    if data is None:
        print(f"  [WARN] 无法解析 frontmatter: {filepath}")
        return False

    missing = is_incomplete(data)
    if not missing:
        print(f"  [OK] 已完整，跳过: {filepath}")
        return False

    print(f"  [..] 补全中: {filepath}（缺少: {', '.join(missing)}）")

    client = anthropic.Anthropic()
    message = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": build_prompt(data)}]
    )

    response_text = message.content[0].text.strip()

    json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
    if not json_match:
        print(f"  [ERROR] Claude 返回格式有误:\n{response_text}")
        return False

    try:
        result = json.loads(json_match.group(0))
    except json.JSONDecodeError as e:
        print(f"  [ERROR] JSON 解析失败: {e}")
        return False

    data["title_en"] = result.get("title_en", data.get("title_en", ""))
    data["tags"] = result.get("tags", [])
    data["ingredients"] = result.get("ingredients", [])
    data["directions"] = result.get("directions", [])

    new_content = serialize_frontmatter(data)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  [OK] 已补全并写入: {filepath}")
    return True


if __name__ == "__main__":
    print("=== 菜谱自动补全 ===")

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("[ERROR] 请先在 .env 中设置 ANTHROPIC_API_KEY")
        sys.exit(1)

    new_files = get_new_recipes()
    if not new_files:
        print("[OK] 没有发现未 push 的新菜谱")
        sys.exit(0)

    print(f"发现 {len(new_files)} 个新菜谱：")
    for f in new_files:
        print(f"  - {f}")
    print()

    updated = 0
    for filepath in new_files:
        updated += complete_recipe(filepath)

    print(f"\n完成！共补全 {updated} 个菜谱。")
