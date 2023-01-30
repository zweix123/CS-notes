import os
import chardet


def get_file_code(file_path):  # 检测文件编码格式, 效率较低
    res = str()
    with open(file_path, "rb") as f:
        res = chardet.detect(f.read())["encoding"]
    return res


def get_parent_abspath(path):
    return os.path.abspath(os.path.dirname(path))


def get_filenames(top, suffix, contrabands=None):
    # 获得top目录下的所有后缀名为suffix的文件路径列表
    # contrabands是一个字符串列表, 表示一些目录, 如果文件路径列表包含某个目的, 则将其排除
    # 这里的方案有不完全的地方, 比如两个同样的目录一个要保留一个不要, 可以通过使用更长的路径子串
    res = [
        os.path.join(dirpath, filename)
        for dirpath, dirnames, filenames in os.walk(top)
        for filename in filenames
        if str(filename).endswith("." + suffix)
    ]

    def check(filename):
        for contraband in contrabands:
            if contraband in filename:
                return False
        return True

    res = filter(lambda filename: check(filename), res)

    return list(res)