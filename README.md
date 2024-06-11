# MarkdownMosaic
MarkdownMosaic 是一个 Python 编写的项目，旨在帮助将多个 Markdown 文件合并为一个单一文件。

The project helps merge multiple Markdown files into a single document, based on python.

在写作过程中，将各个章节或模块分开编写有利于专注于内容创作。然而，最后需要将这些分开的文件合并成一个完整的 Markdown 文档。
使用 pandoc ，或者 obsidian 的 bake 插件进行转换时，可能会遇到一些困难，并且不如期望中那样方便。本项目旨在解决这些问题。

而且 Joplin 也只能批量转换，并不支持直接生成一个总的 md 文档。而本人又希望上传至个人博客（hexo依赖md），还是单一文件的形式更好。

不得不说 gpt 是真厉害，本项目的源码基本都由 gpt-4o 生成，

## 项目结构
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

## 源码解释

`TocBuilder.py` ：用于生成带有占位符的文件目录，即 `toc.md` 。它作为项目的中间件，同时也可以作为目录使用。

`TocBuilder.py` ：用于替换占位符，并生成最后的文件。


## 使用方式
修改配置文件 `config.json`，`docs_path` 是用于存放你的md源文件的文件夹

``` json
{
  "docs_path": "test1",
  "output_filename": "output.md",
  "toc_filename": "toc.md"
}
```

先后运行 `TocBuilder.py` 与 `TocFiller.py` 这两个脚本即可。
好处是如果你对 `toc.md` 不满意，你可以手动修改后，再使用 `TocFiller.py` 生成最后的文件。


## 未来计划
- [ ] 添加更多可选项：文件排序方式/目标层级对齐方式
- [ ] 添加GUI界面，从而可以更方便地修改路径选取、层级对齐方式


## 项目参考/灵感来源
https://github.com/jiang-taibai/docsify-merger

https://github.com/mgmeyers/obsidian-easy-bake



