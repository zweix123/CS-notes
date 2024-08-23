# amazing

```bash
# 查询项目贡献者数量
git log --pretty='%aN' | sort -u | wc -l
# 查询项目commit数量
git log --oneline | wc -l
# 查询项目规模
cloc --git $(git branch --show-current)  # 依赖非原生命令的
find . -name *\.后缀名 -exec wc -l  {} \; | awk '{s+=$1}END{print s}'  # 不依赖非原生命令的

# 开始内卷!
# 查询每个项目贡献者的commit数量并排名
git log --pretty='%aN' | sort | uniq -c | sort -k1 -n -r
# 查询每个项目贡献者的实际代码修改量
git log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
# 升级版:
# - 指定时间范围, 通过git log参数: --since=2020-01-01 --until=2025-01-04
git log --since=2020-01-01 --until=2025-01-04 --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
# - 指定文件夹(包括或排除)
# 排除
git log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat -- . ":(exclude)要排除的目录" | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
# 包括
git log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | grep 要包含的目录 | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done

# 你可能没那么内卷, 只关注自己的, 主要还是引入另一种命令的格式
git log --author="用户名" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -;
# 接时间范围、排除路径、指定路径参数如上
```
