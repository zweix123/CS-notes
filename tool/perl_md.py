# 以jsdelivr作为cdn的url格式: https://cdn.jsdelivr.net/gh/"github用户名"/"project名"@"分支名"/"在project下的路径"

import os
import re
import chardet

# 该脚本用来批量修改md中的图片链接
# 该脚本要求博客文件和图床文件的相对路径对应, 即笔记路径为notes/A/B/note.md, 则其中链接的图片路径为notes-img/A/B/img.jpg, 这里不要求项目名, 但是在项目下的相对路径要一致
# prefix按照代码头的cdn的格式修改到分支名部分, 另外两个变量依照变量名填写
prefix = "https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/"
project_md_name = "CS-notes"
project_img_name = "CS-notes-img"


def get_file_list(root, suffix):
    # 取出root路径下所有后缀名为suffix的文件名组成列表并返回
    return [
        os.path.join(root, _,  file)
        for _, dirs, files in os.walk(root)
        for file in files
        if str(file).endswith("." + suffix)
    ]


def get_file_code(file_path):  # 辅助函数, 检测文件编码格式
    res = str()
    with open(file_path, 'rb') as f:
        res = chardet.detect(f.read())['encoding']
    return res


def get_path_list(path):
    # 把一个文件的路径按照分隔符分割返回列表(这里区分win的文件路径和url)
    if "/" in path:
        return path.split("/")
    else:
        return path.split("\\")


def process(file_path):
    print("处理文件为 : " + file_path)
    # file_path为要处理的文件

    paths = get_path_list(file_path)  # 分割文件路径
    # 从项目开始(开区间)到最后的文件名以前(开区间)
    paths = paths[paths.index(project_md_name) + 1: -1]
    infix = "/".join(paths) + "/"  # 拼接好项目路径到文件名前

    with open(file_path, "r", encoding=get_file_code(file_path)) as f:
        context = f.read()

    def modify(match):
        # 该函数用于正则表达式匹配图片链接部分, 将其中的地址修改为"代码开头设计的url前缀 + 按照代码规定的图片和笔记在项目下一致的相对路径 + 文件名"
        tar = match.group()
        print("处理图片链接 " + tar)

        pre, mid, suf = "", "", ""  # 链接图片的代码, pre和suf是其他部分, mid是路径部分
        if tar[-1] == ")":
            pre = tar[: tar.index("(") + 1]
            mid = tar[tar.index("(") + 1: tar.index(")")]
            suf = tar[-1]
        else:
            pre = tar[: tar.index("\"") + 1]
            tar = tar[tar.index("\"") + 1:]  # 转换一下, 不是要使用
            mid = tar[: tar.index("\"")]
            suf = tar[tar.index("\""):]

        img_name = get_path_list(mid)[-1]
        res = pre + (prefix + infix + img_name) + suf
        print("修改图片链接 " + res)
        return res
    # Markdown中图片语法 ![](url) 或者 <img src='' />
    patten = r"!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"].*?>"
    # 匹配所有图片链接并修改
    context = re.sub(patten, modify, context)

    # 写回
    with open(file_path, "w", encoding=get_file_code(file_path)) as f:
        f.write(context)


if __name__ == "__main__":
    files = get_file_list(os.getcwd(), "md")
    for file in files:
        process(file)
