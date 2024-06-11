import os
import re
import json


def natural_sort_key(s):
    """生成自然排序的键"""
    return [
        int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", s)
    ]


def load_config():
    """加载配置文件"""
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


def generate_toc(docs_dir, toc_file):
    """生成目录文件"""
    # 获取docs目录下的所有Markdown文件并自然排序
    markdown_files = sorted(
        [f for f in os.listdir(docs_dir) if f.endswith(".md")], key=natural_sort_key
    )

    with open(toc_file, "w", encoding="utf-8") as f:
        for md_file in markdown_files:
            chapter_name = os.path.splitext(md_file)[0]
            f.write(f"## {chapter_name}\n")
            f.write(f"[[{md_file}]]\n\n")


if __name__ == "__main__":
    config = load_config()
    docs_dir = config["docs_path"]
    toc_file = config["toc_filename"]

    generate_toc(docs_dir, toc_file)
    print(f"Table of contents has been generated in {toc_file}")
