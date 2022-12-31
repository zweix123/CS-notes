# 检测当前目录下的所有makedown文件中各种字符的数量
import os
import chardet
import string
from tqdm import tqdm


def get_file_code(file_path):  # 检测文件编码格式
    res = str()
    with open(file_path, 'rb') as f:
        res = chardet.detect(f.read())['encoding']
    return res


def get_files(root=os.getcwd()):  # 获得root目录下的所有makedown文件路径名
    return [
        os.path.join(pre, file)
        for pre, dirs, files in os.walk(root)
        for file in files
        if str(file).endswith(".md")
    ]


def str_count(s):
    # English, Chinese, digit, punctuation
    cnt_en, cnt_zh, cnt_dg, cnt_pu = [0] * 4

    for c in s:
        if c in string.ascii_letters:  # 英文
            cnt_en += 1
        elif c.isalpha():  # 中文, isalpha()会得到英文和中文, 但是英文已经在上面的if筛选了
            cnt_zh += 1
        elif c.isdigit():  # 数字
            cnt_dg += 1
        elif c.isspace():  # 空格
            pass
        else:              # 标点符号
            cnt_pu += 1

    return cnt_en, cnt_zh, cnt_dg, cnt_pu

if __name__ == "__main__":
    count_en, count_zh, count_dg, count_pu = 0, 0, 0, 0
    files = get_files(os.getcwd())
    for file in tqdm(files):
        # print(file)
        with open(file, encoding=get_file_code(file)) as f:
            for line in f:
                t = str_count(line)
                count_en += t[0]
                count_zh += t[1]
                count_dg += t[2]
                count_pu += t[3]
    
    print('英文: ', count_en)
    print('中文: ', count_zh)
    print('数字: ', count_dg)
    print('标点符号: ', count_pu)
    print("汇总", count_zh + count_en // 6 + count_dg // 32)