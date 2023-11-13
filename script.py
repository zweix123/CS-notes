#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import re
import string
from typing import Optional

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout
from rich.progress import track


def tree(root_path: str, filetype: Optional[str] = None):
    return [
        os.path.abspath(os.path.join(dirpath, filename))
        for dirpath, _, filenames in os.walk(root_path)
        for filename in filenames
        if (True if filetype is None else str(filename).endswith(filetype))
    ]


def get_links(text: str, image_link: bool = True, hyperlink: bool = True) -> list[str]:
    patterns: list[str] = list()
    if image_link is True:
        patterns += [
            r"!\[.*?\]\((.*?)\)",
            r"<img.*?src=[\'\"](.*?)[\'\"].*?>",
        ]
    if hyperlink is True:
        patterns += [
            r"(?<!!)\[.*?\]\((.*?)\)",
            r"<a.*?href=[\'\"](.*?)[\'\"].*?>",
        ]

    return [item for pattern in patterns for item in re.findall(pattern, text)]


def cmd_img_check():
    """
    检测项目内置图床是否有缺失或者冗余
    """
    URL_PREFIX = "https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/"
    RESOURCE_PREFIX = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "resource/"
    )
    # print(URL_PREFIX, RESOURCE_PREFIX)

    resource_set = tree("./resource")
    resource_set = {path.removeprefix(RESOURCE_PREFIX) for path in resource_set}
    filepaths = tree(".", "md")
    img_links: list[tuple[str, str]] = list()
    used_img_link_set = set()

    for filepath in filepaths:
        dummy_img_links: list[str] = list()
        with open(filepath, "r", encoding="utf-8") as f:
            dummy_img_links = get_links(f.read(), hyperlink=False)
        img_links += [(filepath, dummy_img_link) for dummy_img_link in dummy_img_links]

    external: list[tuple[str, str]] = list()
    unmanage: list[tuple[str, str]] = list()

    for filepath, img_link in img_links:
        if img_link.startswith(URL_PREFIX):
            dummy_img_link = img_link.removeprefix(URL_PREFIX)
            if dummy_img_link not in resource_set:
                unmanage.append((filepath, img_link))
            else:
                used_img_link_set.add(dummy_img_link)
        else:
            external.append((filepath, img_link))

    print("外部图片")
    for dummy in external:
        print("  " + dummy[0] + ": " + dummy[1])

    print("在md文件使用而未被resource管理的图片")
    for dummy in unmanage:
        print("  " + dummy[0] + ": " + dummy[1])

    print("在resource管理而未使用的图片")
    for dummy in list(resource_set - used_img_link_set):
        print("  ", dummy, sep="")


def cmd_link_check():
    """
    检测项目下所有Markdown文本中所有链接的有效性
    链接包括
    + MarkDown的链接和图片链接
    + HTML的跳转链接和图片链接
    """

    def check_url(url: str):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        }
        try:
            response = requests.head(url, headers=headers, timeout=5)
            response.raise_for_status()
            return True
        except Timeout:
            # print("请求超时")
            return False
        except ConnectionError:
            # print("网络连接错误")
            return False
        except HTTPError:
            # print("HTTP错误")
            return False
        except Exception as e:
            # print("其他异常:", e)
            return False

    def check_link(filepath: str, link: str) -> bool:
        rootpath = os.path.dirname(os.path.abspath(__file__))

        if link.startswith("http") or link.startswith("www"):  # URL
            if check_url(link) is False:
                print(f'[文件"{filepath}"的链接"{link}"]: 需要网络检测, 但访问链接有点问题')
                return True
            return False
        elif "md" in link or "#" in link:  # markdown本地文件
            path_link = str()
            # 1.
            if link.startswith("#"):  # 当前文件其他标题
                path_link = filepath + link
            elif link.startswith("."):  # 相对路径
                path_link = os.path.abspath(
                    os.path.join(os.path.dirname(filepath), link)
                )
            else:
                path_link = os.path.join(rootpath, link)
            # 2.
            if "#" in path_link:  # 需要检测到标题
                path_link, chapter = path_link.split("#")
                if not os.path.exists(path_link):
                    print(f'[文件"{filepath}"的链接"{link}"]: 需要检测到标题, 但文件不存在')
                    return False
                with open(path_link) as f:
                    for line in f:
                        if chapter.lower() in line.lower().replace(" ", "-"):
                            return True
                print(f'[文件"{filepath}"的链接"{link}"]: 需要检测到标题, 但标题不存在')
                return False
            else:  # 不需要检测到标题
                if not os.path.exists(path_link):
                    print(f'[文件"{filepath}"的链接"{link}"]: 检测到文件, 但文件不存在')
                    return False
                return True
        else:
            print(f'[文件"{filepath}"的链接"{link}"]: 不属于可处理范围')
            return True

    filepaths = tree(".", "md")
    links: list[tuple[str, str]] = list()
    for filepath in filepaths:
        dummy_links: list[str] = list()
        with open(filepath, "r", encoding="utf-8") as f:
            # dummy_links = get_links(f.read())
            dummy_links = get_links(f.read(), image_link=False)

        links += [(filepath, dummy_link) for dummy_link in dummy_links]

    for filepath, link in track(links):
        check_link(filepath, link)


def cmd_cnt():
    """
    统计项目下所有的Markdown文本信息
    """
    cnt_en, cnt_zh, cnt_dg, cnt_pu = (0 for _ in range(4))
    filepaths = tree(".", "md")
    for filepath in track(filepaths):
        with open(filepath, "r", encoding="utf-8") as f:
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
    print(f"总共大约:{int(cnt_zh + cnt_en//6 + cnt_dg//32):,d}字")


CMDS = {
    "cnt": cmd_cnt,
    "link": {
        ("-c", "--check"): cmd_link_check,
    },
    "img": {
        ("-c", "--check"): cmd_img_check,
    },
}

# ================================================================= #

import os
import subprocess
import sys
from typing import Any, Callable


class DryadConfig:
    SCRIPTPATH = os.path.dirname(os.path.abspath(__file__))
    CALLPATH = os.getcwd()
    OSTYPE = sys.platform


class DryadUtil:
    @staticmethod
    def config():
        if DryadConfig.OSTYPE == "win32":
            pass
        elif DryadConfig.OSTYPE == "linux":
            pass
        elif DryadConfig.OSTYPE == "darwin":
            pass
        else:
            assert False

    @staticmethod
    def run_shell_cmd(
        cmd: str,
        pre_cmd: list[str] = [],
        is_print_cmd_and_result_code: bool = True,
    ) -> None:
        assert type(cmd) is str
        if is_print_cmd_and_result_code:
            print("\033[33;1m" + cmd + "\033[0m")
        cmd = "\n".join(pre_cmd) + "\n" + cmd
        try:
            if DryadConfig.OSTYPE == "win32":
                assert False, "Not Impl"
            elif DryadConfig.OSTYPE == "linux":
                subprocess.run(["bash", "-c", cmd], check=True)
            else:
                assert False, "Not Impl"
        except Exception as e:
            if is_print_cmd_and_result_code:
                print("\033[41m\033[37m" + "Fail" + "\033[0m")
            exit(-1)
        # if is_print_cmd_and_result_code:
        #     print("\033[42m\033[37m" + "Pass" + "\033[0m")

    @staticmethod
    def right_shift(text: str | list[str], dis: int) -> str:
        if type(text) is str:
            text = [text]
        SPACE_LEN = max([len(line) for line in text]) + 42
        ss = [
            s if len(s) != 0 else " " * SPACE_LEN
            for l in [map(str.strip, line.split("\n")) for line in text]
            for s in l
        ]
        assert max([len(s) for s in ss]) <= SPACE_LEN
        while not any(len(s) == 0 or s[0] != " " for s in ss):
            ss = [s[1:] for s in ss]
        return ("\n" + " " * dis).join(map(str.strip, ss)).strip()


class Dryad:
    def __init__(self, cmd_tree: dict, cmd_prefix: list[str] = []) -> None:
        self.cmd_tree = cmd_tree
        self.cmd_prefix = cmd_prefix

        self.config()
        self.main()

    def config(self):
        self.cmd_tree[("-h", "--help")] = self.print_help

        if DryadConfig.OSTYPE == "win32":
            assert False, f"{DryadConfig.OSTYPE} not yet tested, can't be used."
        elif DryadConfig.OSTYPE == "linux":
            self.cmd_prefix = ["set -e"] + self.cmd_prefix
        else:
            assert False, f"{DryadConfig.OSTYPE} not yet tested, can't be used."

        DryadUtil.config()

    def main(self):
        self.options = sys.argv[1:]
        if len(self.options) == 0:
            self.print_help()
        else:
            self.opt_dfs(self.options, self.cmd_tree)

    def print_help(self):
        """Print commands and desciptions supported by script.py."""
        print("该脚本命令可分为两大类")
        print("  Shell Commands, help会输出命令本身")
        print("  Python Function, help会输出函数的__doc__")
        print("命令是支持前缀递归调用的, 比如./script.py test相当于调用所有以test为前缀的命令.")

        def dfs_handle_cmds_doc(cmds: dict | list | str | Callable):
            """递归处理命令树中命令的内容和文档"""
            assert (
                type(dict) is not dict
            ), "Just for mypy, should not be passed into dict"
            if type(cmds) is str:
                return cmds.strip("\n")
            elif type(cmds) is list:
                return "\n".join([dfs_handle_cmds_doc(cmd) for cmd in cmds])
            elif callable(cmds):
                return cmds.__doc__.strip("\n") if cmds.__doc__ is not None else "None"
            else:
                assert False

        def dfs_handle_opts(opt: list[str], remain_cmds: dict | Any):
            if type(remain_cmds) is not dict:  # 递归到选项边界
                opts = " ".join(opt)
                doc = DryadUtil.right_shift(
                    dfs_handle_cmds_doc(remain_cmds), len(opts + ": ")
                )
                print(f"\033[36m{opts}\033[0m: \033[33m{doc}\033[0m")
                return
            for k, v in remain_cmds.items():
                if type(k) is tuple:
                    opt.append("/".join(k))
                elif type(k) is str:
                    opt.append(k)
                else:
                    assert False
                dfs_handle_opts(opt, v)
                opt.pop()

        dfs_handle_opts([], self.cmd_tree)

    def dfs_run(self, cmds: dict | list | str | Callable):
        if callable(cmds):
            cmds()
        elif type(cmds) is str:
            DryadUtil.run_shell_cmd(cmds, self.cmd_prefix)
        elif type(cmds) is list:
            for cmd in cmds:
                self.dfs_run(cmd)
        elif type(cmds) is dict:
            for next_cmds in cmds.values():
                self.dfs_run(next_cmds)
        else:
            assert False, "Impossible the type branch: " + "cmds = " + str(cmds)

    def opt_dfs(self, opts: list[str], cmds: dict | list | str | Callable):
        if len(opts) == 0:  # 递归边界
            self.dfs_run(cmds)
            return
        if type(cmds) is not dict or not (
            any(opts[0] == ele for ele in cmds.keys() if type(ele) is not tuple)
            or any(opts[0] in ele for ele in cmds.keys() if type(ele) is tuple)
        ):
            print(f"Don't supported the options: \"{' '.join(self.options)}\"")
            print('Give it a try of option: "--help"')
            return
        # support default
        if len(opts) == 1 and opts[0] != "default" and "default" in cmds.keys():
            #  最后一个选项     这个选项不是default         “子树”命令集中有default
            self.dfs_run(cmds["default"])  # default命令不能使用()做命令重合
        next_cmds = {
            k: v
            for k, v in cmds.items()
            if (type(k) is tuple and opts[0] in k)
            or (type(k) is not tuple and opts[0] == k)
        }
        assert (
            len(next_cmds) == 1
        ), f"歧义参数: opts: {opts}, cmd.kets(): {cmds.keys()}, next_cmds.keys(): {next_cmds.keys()}"
        self.opt_dfs(opts[1:], list(next_cmds.values())[0])


# ================================================================================= #

Dryad(cmd_tree=CMDS)
