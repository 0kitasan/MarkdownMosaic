# MarkdownMosaic

The project helps merge multiple Markdown files into a single document, based on python.

MarkdownMosaic 是一个 Python 编写的项目，旨在帮助将多个 Markdown 文件合并为一个单一文件。

## 项目文件结构

```
.
├── TocBuilder.py
├── TocFiller.py
├── toc.md
├── output.md
└── docs
    ├── chapter1.md
    ├── chapter2.md
    └── chapter2.md
```

## TocBuilder.py
用于生成带有占位符的文件目录，即toc.md，作为中间件，同时也可以作为目录使用。

## TocFiller.py
用于替换占位符，并生成最后的文件。

## 使用方式
修改配置文件`config.json`，`docs_path`是用于存放你的md源文件的文件夹

``` json
{
  "docs_path": "test1",
  "output_filename": "output.md",
  "toc_filename": "toc.md"
}
```

## 未来计划
- [ ] 添加更多可选项：文件排序方式/目标层级对齐方式
- [ ] GUI界面

## 项目参考/灵感来源
https://github.com/jiang-taibai/docsify-merger

https://github.com/mgmeyers/obsidian-easy-bake
