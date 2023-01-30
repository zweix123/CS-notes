import os, sys, re
from tqdm import tqdm
from zib import *

projectname = os.getcwd().split(os.sep)[-2]
CDN_PREFIX, MODE = str(), str()


def process(filepath):
    # print(filepath)
    if "+" in filepath or "《" in filepath or "&" in filepath:
        print(filepath)
        return
    _, filename = os.path.split(filepath)  # 获得文件名
    t = '(?<=({}))(.*?)(?=({}))'.format(projectname, filename)
    # print(t)
    _, midpath, _ = re.findall(
        '(?<=({}))(.*?)(?=({}))'.format(projectname, filename),
        filepath)[0]  # 获得从项目到文件之间的路径
    # 将路径转换成对应模式的网址路径
    if MODE == "note":
        midpath = "/".join(midpath.split(os.sep))
        pass
    elif MODE == "blog":
        midpath = "/"

    context = str()

    with open(filepath, "r", encoding=get_file_code(filepath)) as f:
        context = f.read()

    def modify(match):
        tar = match.group()
        # print("#", tar)
        pre, mid, suf = str(), str(), str()  # 链接图片的代码, pre和suf是其他部分, mid是路径部分
        if tar[-1] == ")":
            pre = tar[:tar.index("(") + 1]
            mid = tar[tar.index("(") + 1:tar.index(")")]
            suf = tar[-1]
        else:
            pre = tar[:tar.index('"') + 1]
            tar = tar[tar.index('"') + 1:]  # 转换一下, 不是要使用
            mid = tar[:tar.index('"')]
            suf = tar[tar.index('"'):]
        
        _, photoname = os.path.split(mid)
        res = pre + (CDN_PREFIX + midpath + photoname) + suf
        
        # print("%", res)
        return res
    
    patten = r"!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"].*?>"
    # 匹配所有图片链接并修改
    context = re.sub(patten, modify, context)


    # 写回
    with open(filepath, "w", encoding=get_file_code(filepath)) as f:
        f.write(context)
    pass


if __name__ == "__main__":
    _, CDN_PREFIX, MODE = sys.argv
    
    # if CDN_PREFIX[-1] != '/':
    #     CDN_PREFIX += '/'
    filenames = get_filenames(get_parent_abspath(os.getcwd()), "md", [])

    if MODE != "note" and MODE != "blog":
        print("mode is wrong!")

    # for filename in tqdm(filenames):
    for filename in filenames:
        process(filename)