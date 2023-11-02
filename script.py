#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import string
import sys
from typing import Callable, Optional

filepaths = [
    os.path.abspath(os.path.join(dirpath, filename))
    for dirpath, dirnames, filenames in os.walk(".")
    for filename in filenames
    if str(filename).endswith(".md")
]

rootpath = os.getcwd()


def get_link(content: str):
    # ref = img + link
    img_patterns = [
        r"!\[.*?\]\((.*?)\)",
        r"<img.*?src=[\'\"](.*?)[\'\"].*?>",
    ]
    link_patterns = [
        r"(?<!!)\[.*?\]\((.*?)\)",
        r"<a.*?href=[\'\"](.*?)[\'\"].*?>",
    ]
    patterns = img_patterns + link_patterns
    all_links = [item for pattern in patterns for item in re.findall(pattern, content)]
    return all_links


def check_md_ref(filepath: str, ref: str) -> bool:
    if ref.startswith("http") or ref.startswith("www"):  # 网络通信
        return True
    elif "md" in ref or "#" in ref:  # 网链已排除, 该分支只有本地相对md文件
        relative_filepath = str()
        if ref.startswith("#"):  # 当前文件其他标题
            relative_filepath = filepath + ref
        elif ref.startswith("."):  # 相对路径
            relative_filepath = os.path.join(os.path.dirname(filepath), ref)
        else:  # 项目下相对路径
            relative_filepath = os.path.join(rootpath, ref)
        ###################################################
        if "#" in relative_filepath:  # 需要检测到标题
            relative_filepath, chapter = relative_filepath.split("#")

            if not os.path.exists(relative_filepath):
                print(f"[文件 {filepath} 的链接 {ref}]: 检测到标题, 文件 {relative_filepath} 不存在")
                return False

            def check(target: str, text: str):
                return target.lower() in text.lower().replace(" ", "-")

            with open(relative_filepath) as f:
                for line in f:
                    if check(chapter, line):
                        return True

            print(f"[文件 {filepath} 的链接 {ref}]: 检测到标题, 标题 {chapter} 不存在")
            return False
        else:
            if not os.path.exists(relative_filepath):
                print(f"[文件 {filepath} 的链接 {ref}]: 检测文件, 文件 {relative_filepath}")
                return False
            return True
    else:
        print(f'[文件 {filepath} 的链接 "{ref}"]: 不属于可处理范畴')
        return True


def cmd_link_check():
    """\
    检测项目下所有Markdown文本中所有链接的有效性
    链接包括MarkDown语法的链接和图片链接, HTML的图片链接和跳转链接
    """
    print("外部网络链接并未处理, 仅仅处理本地相对路径")
    for filepath in filepaths:
        links = list()
        with open(filepath) as f:
            for line in f:
                links += get_link(line)

        for link in links:
            check_md_ref(filepath, link)


def cmd_cnt():
    """\
    统计项目下所有的Markdown文本信息
    """
    cnt_en, cnt_zh, cnt_dg, cnt_pu = [0] * 4
    filepaths = [
        os.path.abspath(os.path.join(dirpath, filename))
        for dirpath, dirnames, filenames in os.walk(".")
        for filename in filenames
        if str(filename).endswith(".md")
    ]
    for filepath in filepaths:
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                for c in line:
                    if c in string.ascii_letters:  # 英文
                        cnt_en += 1
                    elif c.isalpha():  # 中文, isalpha()会得到英文和中文, 但是英文已经在上面的if筛选了
                        cnt_zh += 1
                    elif c.isdigit():  # 数字
                        cnt_dg += 1
                    elif c.isspace():  # 空格
                        pass
                    else:  # 标点符号
                        cnt_pu += 1

    print(f"总共{len(filepaths)}篇文章")
    print(f"字母:{int(cnt_en):,d}个")
    print(f"汉字:{int(cnt_zh):,d}字")
    print(f"数字:{int(cnt_dg):,d}位")
    print(f"标点:{int(cnt_pu):,d}个")
    print(f"总共大约:{int(cnt_zh + cnt_en//6 + cnt_dg//32):,d}字")  # fmt: skip


def replace_prefix(string, new_prefix):
    def get_space_prefix(strs: list[str]):
        prefix = " " * min([len(s) for s in strs])
        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if len(prefix) == 0:
                    break
        return prefix

    prefix = get_space_prefix([line for line in string.split("\n")])
    return ("\n" + string).replace("\n" + prefix, new_prefix).strip()


def cmd_help():
    """\
    打印脚本支持的命令及其说明
    """
    context = dict()

    def cmd_capture(cmds: dict | Callable, pre_cmd: str = ""):
        if callable(cmds):
            context.setdefault(cmds, []).append(pre_cmd)
            return
        for cmd_name, next_dict in cmds.items():
            cmd_capture(next_dict, pre_cmd + " " + cmd_name)

    cmd_capture(CMDS)
    for cmd_func, args in context.items():
        output_text = "\n".join(args) + ": "
        prefix = "\n" + (max([len(arg) for arg in args]) + 2) * " "
        output_text += replace_prefix(cmd_func.__doc__, prefix)
        print(output_text)


CMDS = {
    "help": cmd_help,
    "cnt": cmd_cnt,
    "link": {
        "-c": cmd_link_check,
        "--check": cmd_link_check,
    },
}


def arg_dfs(args=["help"], cmds=CMDS):
    if len(args) == 0:
        if not callable(cmds):
            cmd_help()
            return
        cmds()
        return
    if type(cmds) is not dict or args[0] not in cmds.keys():
        print(f'Argument: {sys.argv[1:]} not have function. Give it a try of "help"?')
        return
    arg_dfs(args[1:], cmds[args[0]])


arg_dfs(sys.argv[1:])
