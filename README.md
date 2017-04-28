# Hexo-Template-Generator
A little script to generator template for my blog based on Hexo.

一个生成 Hexo 模板的小工具。

如果第一个参数输入一个网址（包括 `http://` or `https://`），预设用户输入了 LertCode 题目页面的网址，默认抓取 LeetCode 题目详情；此时第二个参数为储存位置，`p` 为`_posts`即发布文件夹，`d`为`_drafts`即草稿文件夹。

若第一个参数非网址，则生成简单模板，以第一个参数为标题，可随意大写加空格，建议使用引号包裹，目前最好仅输入中文；文件名会自动根据标题生成。第二个参数为标签，不输入则默认为空。