import os
import re
import string
from typing import Optional

import requests  # type: ignore
from dryads import Dryads  # type: ignore
from requests.exceptions import ConnectionError, HTTPError, Timeout  # type: ignore
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


def word_count():
    """
    统计项目下Markdown文本的字数信息
    """
    cnt_en, cnt_zh, cnt_dg, cnt_pu = (0 for _ in range(4))
    filepaths = [
        os.path.join(root, f)
        for root, dirs, files in os.walk(".")
        for f in files
        if f.endswith("md")
    ]

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

    print(f"总共  {len(filepaths)} 篇文章")
    print(f"字母: {int(cnt_en):,d} 个")
    print(f"汉字: {int(cnt_zh):,d} 字")
    print(f"数字: {int(cnt_dg):,d} 位")
    print(f"标点: {int(cnt_pu):,d} 个")
    print(f"共约  {int(cnt_zh + cnt_en//6 + cnt_dg//32):,d} 字")


def image_check():
    """
    笔记图床相关检测
    """
    # 笔记的图床直接放在项目下, 即目录resource
    # 其目录结构一一对应, 一个目录下的md使用的图片放在图床下的一个目录中
    # 由于互联网的不稳定性, 任何图片都应该放在图床中
    markdown_dirpaths: list[str] | set[str] = [
        root
        for root, dirs, files in os.walk(".")
        if root != "."
        and not any(d.startswith(".") for d in root.split(os.sep)[1:])
        and root.split(os.sep)[1] != "resource"
    ]
    image_dirpaths = [
        os.sep.join([".", *root.split(os.sep)[2:]])
        for root, dirs, files in os.walk(os.path.join(".", "resource"))
        if root != os.path.join(".", "resource")
        if not any(d.startswith(".") for d in root.split(os.sep)[1:])
    ]
    markdown_dirpaths = set(markdown_dirpaths)
    assert all(image_dirpath in markdown_dirpaths for image_dirpath in image_dirpaths)

    for markdown_dirpath in markdown_dirpaths:
        for root, dirs, files in os.walk(markdown_dirpath):
            dirs[:] = []
            for f in files:
                filepath = os.path.join(root, f)
                links = []
                with open(filepath, "r", encoding="utf-8") as file:
                    content = str(file)
                    links = get_links(content, True, False)
                print(links)
                if len(links) != 0:
                    exit()


CMDS = {
    "cnt": word_count,
    "link": {
        ("-c", "--check"): cmd_link_check,
    },
    "img": {
        ("-c", "--check"): image_check,
    },
}

Dryads(CMDS)
