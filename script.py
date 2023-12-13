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
#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from enum import Enum, auto
from typing import Any, Callable

# TODO: --help无法区分脚本是使用[]包括还是一个完成的脚本文本字符串

DryadArg: Any = None


class DryadFlag(Enum):
    PrefixCmd = auto()  # 作为某个节点的键, 其值对应的脚本为子树中所有脚本的前置脚本
    # AcceptArg = auto()  # 作为叶子的值, 表示该选项还接收一个可选参数, 并将参数放在变量DryadArg中
    InVisible = auto()  # 作为叶子的值, 表示执行的脚本是否打印, 默认打印, 使用该标志表示不打印
    IgnoreErr = auto()  # 作为叶子的值, 表示命令执行出错后是否停止, 默认停止, 使用该标志表示不停止


class DryadEnv:
    SCRIPTPATH = os.path.dirname(os.path.abspath(__file__))
    CALLPATH = os.getcwd()
    OSTYPE = sys.platform

    @staticmethod
    def println():
        """Print Dryad env."""
        print("SCRIPTPATH", "=", DryadEnv.SCRIPTPATH)
        print("CALLPATH  ", "=", DryadEnv.CALLPATH)
        print("OSTYPE    ", "=", DryadEnv.OSTYPE)


class DryadUtil:
    ErrStopCmd = "set -eu"
    PrefixCmds: list[str] = []
    DryadFlags: list[DryadFlag] = []

    @staticmethod
    def flag_push(flag: DryadFlag, data: Any):
        assert type(flag) is DryadFlag
        if flag == DryadFlag.PrefixCmd:
            if type(data) is str:
                DryadUtil.PrefixCmds.append(data)
            elif type(data) is list:
                for ele in data:
                    DryadUtil.PrefixCmds.append(ele)
            else:
                assert False
        elif flag == DryadFlag.InVisible:
            DryadUtil.DryadFlags.append(flag)
        elif flag == DryadFlag.IgnoreErr:
            DryadUtil.DryadFlags.append(flag)
        else:
            assert False

    @staticmethod
    def flag_pop(flag: DryadFlag, data: Any):
        assert type(flag) is DryadFlag
        if flag == DryadFlag.PrefixCmd:
            if type(data) is str:
                DryadUtil.PrefixCmds.pop()
            elif type(data) is list:
                for ele in data:
                    DryadUtil.PrefixCmds.pop()
            else:
                assert False
        elif flag == DryadFlag.InVisible:
            DryadUtil.DryadFlags.pop()
        elif flag == DryadFlag.IgnoreErr:
            DryadUtil.DryadFlags.pop()
        else:
            assert False

    @staticmethod
    def _run(cmd: str):
        assert type(cmd) is str, f"arg cmd = {cmd} is not str."

        if DryadEnv.OSTYPE == "win32":
            assert False, "Not supported"
        elif DryadEnv.OSTYPE == "linux":
            subprocess.run(["bash", "-c", cmd], check=True)
        else:
            assert False, "Not supported"

    @staticmethod
    def run(cmd: str) -> None:
        assert type(cmd) is str, f"arg cmd = {cmd} is not str."

        if DryadFlag.InVisible not in DryadUtil.DryadFlags:
            print("\033[33;1m" + cmd + "\033[0m")
        pre_cmd = DryadUtil.PrefixCmds
        if DryadFlag.IgnoreErr not in DryadUtil.DryadFlags:
            pre_cmd = [DryadUtil.ErrStopCmd] + pre_cmd

        cmd = "\n".join(pre_cmd) + "\n" + cmd

        try:
            DryadUtil._run(cmd)
        except Exception as e:
            if DryadFlag.IgnoreErr not in DryadUtil.DryadFlags:
                if DryadFlag.InVisible not in DryadUtil.DryadFlags:
                    print("\033[41m\033[37m" + "Fail" + "\033[0m")
                exit(-1)
        # print("\033[42m\033[37m" + "Pass" + "\033[0m")

    @staticmethod
    def strip_line(text: str) -> str:
        """去除首尾空行"""
        assert type(text) is str
        while len(text) > 0 and text[0] == "\n":
            text = text[1:]
        while len(text) > 0 and text[-1] == "\n":
            text = text[:-1]
        return text

    @staticmethod
    def left_tab(text: str) -> str:
        """去除文本左空列"""
        assert type(text) is str
        text = DryadUtil.strip_line(text)
        lines = text.split("\n")
        # 文本内部可能有空行, 其会影响对左空列的判断, 同时其本身还要保留, 这里暂时将其填充极大, 最后用rstrip(注意有r)消除
        for i in range(len(lines)):
            if len(lines[i].strip()) == 0:
                lines[i] = " " * len(text)

        def space_prefix_len(s: str) -> int:
            # 暴力拿到一行文本左边的空格个数
            assert "\n" not in s, "only support a line."
            ans = 0
            while ans + 1 < len(s) and s[: ans + 1] == " " * (ans + 1):
                ans = ans + 1
            return ans

        max_space_prefix_len: int = min([space_prefix_len(line) for line in lines])
        lines = [line[max_space_prefix_len:] for line in lines]
        return "\n".join([line.rstrip() for line in lines])

    @staticmethod
    def right_shift(text: str, dist: int) -> str:
        """整个文本右移(在左边填充空列对齐), 不会处理首行"""
        assert type(text) is str and type(dist) is int
        text = DryadUtil.left_tab(text)
        lines = text.split("\n")
        for i in range(1, len(lines)):
            lines[i] = (" " * dist) + lines[i]
        return "\n".join(lines)


class Dryad:
    def __init__(self, cmd_tree: dict) -> None:
        self.cmd_tree = cmd_tree
        self.options: list[str] = []

        def check_cmd_tree(cmd_tree_node: dict | list | str | Callable):
            if callable(cmd_tree_node):
                return
            elif type(cmd_tree_node) is str:
                return
            elif type(cmd_tree_node) is list:
                [check_cmd_tree(ele) for ele in cmd_tree_node]
            elif type(cmd_tree_node) is dict:
                keys = []
                for key in cmd_tree_node.keys():
                    if type(key) is str:
                        keys.append(key)
                    elif type(key) is tuple:
                        for ele in key:
                            keys.append(ele)
                    elif type(key) is DryadFlag:
                        pass
                    else:
                        assert False
                if len(keys) != len(set(keys)):
                    # dict本身不会有冲突的键, 但是因为tuple支持多重选项, 就可能出现冲突了
                    print("Commands dict has conflicting options.")
                    exit(-1)
            else:
                assert False

        check_cmd_tree(self.cmd_tree)

        if DryadEnv.OSTYPE == "win32":

            def dfs(cmds: dict | list | str | Callable | DryadFlag):
                if type(cmds) is str:
                    print("run commands in win is banned.")
                    exit(0)
                elif type(cmds) is list:
                    for ele in cmds:
                        dfs(ele)
                elif type(cmds) is dict:
                    for son in cmds.values():
                        dfs(son)
                else:
                    assert callable(cmds) or type(cmds) is DryadFlag, cmds

            dfs(cmd_tree)

        elif DryadEnv.OSTYPE == "linux":
            pass
        else:
            assert False, f"{DryadEnv.OSTYPE} not yet tested, can't be used."

        self.cmd_tree[("-h", "--help")] = self.print_help
        self.cmd_tree["env"] = DryadEnv.println

        self.main()

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
        # "支持前缀递归调用, 如果有选项test collector, test planer, test executor三个选项, 则./script.py test则会调用三个, 注意./script te是一个错误命令, 这里的前缀指的是前缀选项"

        def bfs(cmds: list | str | Callable | DryadFlag | dict) -> str:
            assert type(cmds) is not dict  # for mypy
            if type(cmds) is DryadFlag:
                return str(cmds)
            elif type(cmds) is str:
                return cmds
            elif callable(cmds):
                return cmds.__doc__ if cmds.__doc__ is not None else "no doc str"
            elif type(cmds) is list:
                return "\n".join([bfs(cmd) for cmd in cmds])
            else:
                assert False

        def dfs(opts: list[str], cmds: dict | Any):
            if type(cmds) is not dict:
                opt = " ".join(opts)
                doc = DryadUtil.right_shift(bfs(cmds), len(opt + ": "))
                print(f"\033[36m{opt}\033[0m: \033[33m{doc}\033[0m")
                return
            for k, v in cmds.items():
                if type(k) is tuple:
                    opts.append("/".join(k))
                elif type(k) is str:
                    opts.append(k)
                elif type(k) is DryadFlag:
                    opts.append(str(k))
                else:
                    assert False
                dfs(opts, v)
                opts.pop()

        dfs([], self.cmd_tree)

    def dfs_run(self, cmds: dict | list | str | Callable):
        if callable(cmds):
            cmds()
        elif type(cmds) is str:
            DryadUtil.run(cmds)
        elif type(cmds) is list:
            # 必须放在两个循环, 即保证所有的标记都收集完毕, 影响所有的命令执行, 相当于允许标志乱序
            [DryadUtil.flag_push(ele, None) for ele in cmds if type(ele) is DryadFlag]
            [self.dfs_run(ele) for ele in cmds if type(ele) is not DryadFlag]
            [DryadUtil.flag_pop(ele, None) for ele in cmds if type(ele) is DryadFlag]
        elif type(cmds) is dict:
            [DryadUtil.flag_push(k, v) for k, v in cmds.items() if type(k) is DryadFlag]
            [self.dfs_run(v) for k, v in cmds.items() if type(k) is not DryadFlag]
            [DryadUtil.flag_pop(k, v) for k, v in cmds.items() if type(k) is DryadFlag]
        else:
            assert False

    def opt_dfs(self, opts: list[str], cmds: dict | Any):
        def match(cmd_dict: dict, opt: str) -> Any | None:
            assert type(cmd_dict) is dict and type(opt) is str
            item: Any = None
            for k, v in cmd_dict.items():
                if (type(k) is str and opt == k) or (type(k) is tuple and opt in k):
                    assert item is None, "键应该是唯一的, 构造函数中未成功检测出."
                    item = v
            return item

        if len(opts) == 0:
            self.dfs_run(cmds)
            return

        if type(cmds) is not dict or match(cmds, opts[0]) is None:
            # 如果当前的节点已经是叶子(而选项仍然没匹配完), 或者虽然是中间节点但是并没有匹配的键
            print(f"Options \"{' '.join(self.options)}\" error", end=", ")
            print(f"unsupported or spelled incorrectly", end=", ")
            print(f'give it a try of option "--help"', end=".\n")
            return

        if DryadFlag.PrefixCmd in cmds:
            DryadUtil.flag_push(DryadFlag.PrefixCmd, cmds[DryadFlag.PrefixCmd])
        self.opt_dfs(opts[1:], match(cmds, opts[0]))
        if DryadFlag.PrefixCmd in cmds:
            DryadUtil.flag_pop(DryadFlag.PrefixCmd, cmds[DryadFlag.PrefixCmd])


def example_func():
    print("Call example_func")


def simple_func():
    """This is a simple function."""
    print("Call simple_func")


def complex_func():
    """
         Complex Func
    ========================
       args   ||  none
     ability  ||  print

    不需要参数, 功能仅打印。
    """
    print("Call complex_func")


def input_func():
    """Output DryadArg"""
    assert DryadArg is not None
    print(DryadArg)


EXAMPLE_CMDS = {
    "func": {
        "example": example_func,
        "simple": simple_func,
        "complex": complex_func,
    },
    "bash": {
        "common": ["echo 1", "echo 2", "echo 3"],
        "un-vis": [DryadFlag.InVisible, "echo This is in-visible test cmd."],
        "prefix": {
            DryadFlag.PrefixCmd: ["cd ~", "mkdir -p .dryad_test", "cd .dryad_test"],
            "exe1": "mkdir -p dir1 && cd dir1 && pwd",
            "exe2": [
                DryadFlag.IgnoreErr,
                "mkdir dir2",
                "cd dir2 && pwd",
            ],
            "exe3": [
                DryadFlag.IgnoreErr,
                "mkdir dir3",
                """
                cd dir3
                pwd
                """,
            ],
        },
    },
    "put": [
        # DryadFlag.AcceptArg,
        input_func,
    ],
}

# Dryad(EXAMPLE_CMDS)
Dryad(CMDS)