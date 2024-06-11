import os
import re
import json


def find_max_heading_level(content):
    """
    找到 Markdown 内容中的最大标题级别。

    参数:
    content (str): Markdown 文件内容

    返回:
    int: 最大标题级别
    """
    headings = re.findall(r"^(#{1,6})\s", content, flags=re.MULTILINE)
    if not headings:
        return 0  # 如果没有标题，则返回 0
    return min(len(heading) for heading in headings)


def adjust_heading_levels(content, current_max_level, target_level):
    """
    调整 Markdown 内容中的标题层级。

    参数:
    content (str): Markdown 文件内容
    current_max_level (int): 当前文档中的最大标题级别
    target_level (int): 目标标题级别

    返回:
    str: 调整后的 Markdown 内容
    """
    level_offset = target_level - current_max_level

    def replace_heading(match):
        heading = match.group(1)
        return "#" * (len(heading) + level_offset) + match.group(2)

    adjusted_content = re.sub(
        r"^(#{1,6})(.*)$", replace_heading, content, flags=re.MULTILINE
    )
    return adjusted_content


def load_config():
    """加载配置文件"""
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


def replace_placeholders(toc_file, docs_dir, output_file, target_level):
    # 读取 toc.md 的内容
    with open(toc_file, "r", encoding="utf-8") as f:
        toc_content = f.read()

    # 提取占位符并替换为对应文件的内容
    placeholders = re.findall(r"\[\[(.*?)\]\]", toc_content)
    for placeholder in placeholders:
        md_file_path = os.path.join(docs_dir, placeholder)
        if os.path.exists(md_file_path):
            with open(md_file_path, "r", encoding="utf-8") as md:
                md_content = md.read()
                max_heading_level = find_max_heading_level(md_content)
                if max_heading_level > 0:
                    adjusted_content = adjust_heading_levels(
                        md_content, max_heading_level, target_level
                    )
                    toc_content = toc_content.replace(
                        f"[[{placeholder}]]", adjusted_content
                    )
                else:
                    toc_content = toc_content.replace(f"[[{placeholder}]]", md_content)

    # 写回 output.md 文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(toc_content)


if __name__ == "__main__":
    config = load_config()
    toc_file = config["toc_filename"]
    docs_dir = config["docs_path"]
    output_file = config["output_filename"]
    target_level = config.get("target_level", 3)  # 默认目标标题级别为3

    replace_placeholders(toc_file, docs_dir, output_file, target_level)
    print(
        f"Placeholders in {output_file} have been replaced with the content of respective Markdown files."
    )
