import os

from dryads import Dryads  # type: ignore
from rich.progress import track


def print_execel():
    raise Exception("not imple")


def print_table(data: list[tuple[str, ...]]) -> None:
    assert all(len(line) == len(data[0]) for line in data)
    pass


def cnt_impl():
    import string

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

    print_table(
        [
            ("总共", str(len(filepaths)), "文章"),
            ("字母: ", str(cnt_en), "个"),
            ("汉字: ", str(cnt_zh), "字"),
            ("数字: ", str(cnt_dg), "位"),
            ("标点: ", str(cnt_pu), "个"),
            ("共约", str(int(cnt_zh + cnt_en // 6 + cnt_dg // 32)), "字"),
        ]
    )


CMDS = {
    "cnt": cnt_impl,
}

Dryads(CMDS)
