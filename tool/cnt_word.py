"""
统计博客目录字数脚本
"""
import os
import sys
import string
from tqdm import tqdm
from zib import *


def count_content(content):
    # English, Chinese, Digit, Punctuation
    cnt_en, cnt_zh, cnt_dg, cnt_pu = [0] * 4

    for c in content:
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

    return cnt_en, cnt_zh, cnt_dg, cnt_pu


if __name__ == "__main__":
    filenames = get_filenames(get_parent_abspath(os.getcwd()), "md", sys.argv[1:])

    count_en, count_zh, count_dg, count_pu = 0, 0, 0, 0

    for file in tqdm(filenames):
        with open(file, encoding=get_file_code(file)) as f:
            for line in f:
                t = count_content(line)
                count_en += t[0]
                count_zh += t[1]
                count_dg += t[2]
                count_pu += t[3]

    print("英文: ", count_en)
    print("中文: ", count_zh)
    print("数字: ", count_dg)
    print("标点符号: ", count_pu)
    print("汇总", count_zh + count_en // 6 + count_dg // 32)