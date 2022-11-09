# 概述

[常识](https://linux.cn/article-6160-1.html)

+ 根目录`\`
  + `home`：所有用户”家“目录
  + `bin`：常用可执行文件命令
  + `lib`：安装包和头文件
  + `etc`：配置文件
    + `nginx`：阿帕奇的配置文件
  + `var`：
    + `log`：日志
  + `proc`：硬件配置信息
+ 文件路径：
  + 绝对路径：从根目录开始描述，以`/`分隔
    + `~/`：家目录（区别根目录）
  + 相对路径：
    + `.`表示当前目录
    + `..`表示当前目录的上一个目录

## 环境变量

记录配置信息，可被各个进程访问到

+ 查看方法：

  1. `env`：显示当前用户的变量
  2. `set`：显示当前shell的变量，包含当前用户的变量
  3. `export`：显示当前导出成用户环境变量的shell变量

  + 输出某环境变量的值：`echo $PATH`

+ 修改：将对环境变量的修改放在`~/.bashrc`文件中（末尾），然后执行`source ~/.bashrc`

+ 常用环境变量：

  + `HOME`：用户的家目录。

  + `PATH`：可执行文件（命令）的存储路径。路径与路径之间用`:`分隔。当某个可执行文件同时出现在多个路径中时，会选择从左到右数第一个路径中的执行。下列所有存储路径的环境变量，均采用从左到右的优先顺序。

    + 如果想让自己的命令可以在任何一个目录下直接类似普通命令那样运行

      在`~/.bashrc`中末尾添加`export PATH=命令目录（从根目录开始：/home...）:$PATH`：相当于将PATH本来的字符串前接一个新的串然后保存在PATH中

  + `LD_LIBRARY_PATH`：用于指定动态链接库(`.so`文件)的路径，其内容是以冒号分隔的路径列表。

  ---

  + `C_INCLUDE_PATH`：C语言的头文件路径，内容是以冒号分隔的路径列表。
    `CPLUS_INCLUDE_PATH`：CPP的头文件路径，内容是以冒号分隔的路径列表。
  + `PYTHONPATH`：Python导入包的路径，内容是以冒号分隔的路径列表。
  + `JAVA_HOME`：jdk的安装目录。
    `CLASSPATH`：存放Java导入类的路径，内容是以冒号分隔的路径列表。

# 命令

+ 命令格式：`命令 [选项] [参数]`
  + 选项：`-`加什么，顺序不关键
    + `-help/--help/-h/--h`：提供该命令手册
  + 参数：部分命令对参数个数不强制，支持正则表达式，对于参数名称中的空格使用转移字符`'\ '`

## 最基本命令

0. `man -ls`：提供命令手册

1. `ctrl c`：取消命令，并且换行：向当前进程传递终止信号

2. `ctrl u`：清空本行命令

3. `tab`键：可以补全命令或文件名，如果补全不了快速按两下tab键，可以显示备选选项

4. 方向键上键：上一条命令

5. `ls`：列出当前目录下所有文件，（ac terminal中）蓝色的是文件夹，白色的是普通文件，绿色的是可执行文件

   + `ls -l`：提供详细信息

     > 每个文明名前是二进制表示的文件权限：分别是作者的权限、同组的权限、其他用户权限。每个权限占三位，分别是读`r`、写`w`、执行`x`

   + `ls -a`：显示隐藏文件

     > 如果一个文件名以`.`开头，则其是一个隐藏文件

   + `ls -h`：”人性化“（也使用于其他命令）

   + `ll`：相当于`ls -al`

6. `pwd`：显示当前路径

7. `cd XXX`：进入XXX目录下，`cd ..`返回上层目录，`cd -`返回上一个所在的目录，只有`cd`返回家目录

8. `cp XXX YYY`：将XXX文件复制成YYY，相当于复制+粘贴+（重命名），如果是移动文件夹则是`cp 文件夹 路径 -r`

9. `mkdir XXX`：创建目录XXX，`mkdir 参数 -p`：如果一系列路径有部分目录没有，则递归创建

10. `rm XXX`：删除普通文件；

    `rm XXX -r`：删除文件夹

    + 支持正则表达式：`rm a\*`：删除文件夹a下的所有文件而不删除文件夹

11. `mv XXX YYY`：将XXX文件移动到YYY，和`cp`命令一样，XXX和YYY可以是一个路径，相当于拖拽

12. `touch XXX`：创建一个文件

13. `cat XXX`：展示文件XXX中的内容

14. 虚拟机和主体机器之间的信息交换

    复制文本：windows/Linux下，`Ctrl + insert`，Mac下，`command + c`

    粘贴文本：windows/Linux下，`Shift + insert`，Mac下，`command + v`

15. `history`查看历史命令

15. `clear`和`Ctrl + l`：终端显示页后翻=刷新屏幕$\approx$清屏

+ `type 其他命令`：查看命令类型

## 重定向和管道

+ 每个进程默认打开3个文件描述符：

  + `stdin`标准输入，从命令行读取数据，文件描述符为`0`
  + `stdout`标准输出，向命令行输出数据，文件描述符为`1`
  + `stderr`标准错误输出，向命令行输出数据，文件描述符为`2`

  可以用文件重定向将这三个文件重定向到其他文件中。

+ 重定向命令列表

  | 命令               | 说明                                  |
  | ------------------ | ------------------------------------- |
  | `command > file`   | 将stdout重定向到file中                |
  | `command < file`   | 将stdin重定向到file中                 |
  | `command >> file`  | 将stdout以追加方式重定向到file中      |
  | `command n> file`  | 将文件描述符n重定向到file中           |
  | `command n>> file` | 将文件描述符n以追加方式重定向到file中 |

+ 管道：将前一个命令的`stdout`重定向给下一个命令的`stdin`
  + 只能处理`stdout`，会忽略`stderr`
  + 要求管道右边的命令必须能接受`stdin`
  + 可串联
+ `xargs`命令：将stdin中的数据用空格或回车分割成命令行参数：因为有的参数不从stdin读入，不能用管道

## 其他常用命令

+ 系统状况

  + `top`：查看所有进程的信息（Linux的任务管理器）

    + 打开后，输入`M`：按使用内存排序
    + 打开后，输入`P`：按使用CPU排序
    + 打开后，输入`q`：退出

  + `df -h`：查看硬盘使用情况

    `free -h`：查看内存使用情况

    `du -sh`：查看当前目录占用的硬盘空间

  + `ps aux`：查看所有进程

  + `kill -9 pid`：杀死编号为pid的进程

    > 其中9是一个kill设定的参数，还有其他参数，用数字表示

    + 传递某个具体的信号：`kill -s SIGTERM pid`

      > 9就是其中一个信号

  + `netstat -nt`：查看所有网络连接

  + `w`：列出当前登陆的用户

  + `ping`：

+ 文件权限：`chmod`：修改文件权限

  每个文件由10个二进制表示文件权限：其中分成四组，分别是1、3、3、3，其中第一个表示文件类型（是文件还是目录），后面三个表示权限，每组都是同样的三位，分别表示是否可读、是否可写、是否可执行，由数字0~7表示，而这三组分别表示自己权限、同组权限和。。。权限。

  + `chmod +x XXX`：给XXX添加可执行权限
  + `chmod -x XXX`：去掉XXX的可执行权限
  + `chmod 777 XXX`：将XXX的权限改成777
  + `chmod 777 XXX -R`：递归修改整个文件夹的权限

+ 文件检索：

  + `find 路径 -name "正则表达式"`：搜索路径下是否有名称符合正则表达式的文件
  + `grep xxx`：从`stdin`中读入若干行数据，如果某行中包含`xxx`，则输入该行；否则忽略
  + `wc`：统计行数、单词书、字节数：既可以从`stdin中`直接读入内容；也可以在命令行参数中传入文件名列表
    + 参数：`-l`：统计行数；`-w`：统计单词数；`-c`：统计字节数

  ```bash
  find 文件目录/ -name "要查的文件或文件名正则表达式" | xargs cat | grep "要查的内容"
  # 找到这些文件                      # 输入内容（cat应该是参数而不是stdin，用xargs转换）
  find 文件目录/ -name "要查的文件或文件名正则表达式" | xargs cat | wc
  # 确定这些文件的内容的多少信息
  ```

  + `ag "要查的内容"`：在当前目录下的文件中查找内容（较于grep输入更人性化）
  + `tree`：展示当前目录的文件结构：可添加参数展示某个目录的文件结果
    + `-a`：显示隐藏文件
  + cut：
    从stdin中读入多行数据
    echo \$PATH | cut -d ':' -f 3,5：输出PATH用:分割后第3、5列数据
    echo \$PATH | cut -d ':' -f 3-5：输出PATH用:分割后第3-5列数据
    echo \$PATH | cut -c 3,5：输出PATH的第3、5个字符
    echo \$PATH | cut -c 3-5：输出PATH的第3-5个字符
  + `sort`：将每行内容按字典序排序，可从`stdin`内读取多行，可从参数读取文件名列表

+ 查看文件内容：
  + `more`：浏览文件内容：
    + `回车`：下一行
    + `空格`：下一页
    + `b`：上一页
    + `q`：退出
  + `less`：与more类似，功能更全
    + `回车`：下一行
    + `y`：上一行
    + `Page Down`：下一页
      `Page Up`：上一页
    + `q`：退出
  + head -3 xxx：展示xxx的前3行内容
    同时支持从stdin读入内容
    tail -3 xxx：展示xxx末尾3行内容
    同时支持从stdin读入内容

+ 用户相关
  + `history`：展示当前用户的历史操作。内容存放在`~/.bash_history`中

+ 工具：
  + `md5sum`：计算md5哈希值：
    + 可从`stdin`读入内容：执行命令 -> 输入内容 -> `Ctrl + z`
    + 可从命令行参数传入文件名列表
  + `time command`：统计`command`命令的执行时间
  + `ipython`：ipython的相关特点
  + `watch -n 0.1 command`：每0.1秒执行一次`command`命令
    + 怎么关：`Ctrl + c`
  + `tar`：压缩文件
    + `tar -zcvf xxx.tar.gz /path/to/file/*`：压缩
      `tar -zxvf xxx.tar.gz`：解压缩
  + `diff XXX YYY`： 查找文件XXX与YYY的不同点

+ 安装软件
  + `sudo command`：以`root`身份执行`command`命令
  + `apt-get install xxx`：安装软件
  + `pip install xxx --user --upgrade`：安装python包

## Shell编程

> 关于空格，如果表达式加上”美观“的空格，可能导致这样的问题，空格在linux中有含义，分隔参数

> linux下的Shell语言种类很多，一般默认bash

+ 文件后缀名：`.sh`

  脚本需要在文件开头`#! /bin/bash`来指明bash为脚本解释器

+ 运行方式：

  1. `chmod +x test.sh`：把脚本`test.sh`具有可执行权限

     可以把`test.sh`作为可执行文件运行（当前路径、绝对路径、家目录路径）

  2. 解释器运行：`bash test.sh`

+ 注释：

  1. 单行注释：`#`：注释每行之后的内容

  2. 多行注释：

     ```bash
     :<<EOF
     这里面是一个注释
     EOF
     ```

     这里的`EOF`可以换成其他任意字符串

+ 引入外部脚本：

  ```bash
  . filename  # 空格隔开
  
  #或者
  
  source filename
  ```

### 变量

+ 定义变量：

  ```bash
  sam='string'
  sam="string"
  sam=string
  ```

  上面这三种方法都是定义字符串

  + 字符串：

    + 单引号：内容原样输出、不会执行、不会取变量——真文本
    + 双引号：内容                   可以执行、可以去变量——代码

    > ssh中的`ssh ... commond`相反

  + 获取字符串长度：`${#字符串变量名}`

  + 提取子串：`${字符串变量名:第一个索引（从0开始）:子串长度}`

+ 使用变量：在变量名前加上`$`或者使用`${}`符号

  + 在后续的使用中，可能还要把取变量后的结果在用引号括起来，因为比如变量是字符串变量且中间有空格，同时取变量后作为参数，这时空格导致这是多个参数

+ 只读变量：

  ```bash
  sam=string
  readonly sam
  declare -r name
  ```

  以上两种方式均可

+ 删除变量：

  ```bash
  sam=string
  unset sam
  ```

  删除之后其内容为一个空字符串

+ 变量类型：

  > 子进程：命令bash会开一个新进程，原进程睡眠，exit/Ctrl + d退出当前bash

  1. 自定义变量/局部变量：子进程不能访问的变量
  2. 环境变量/全局变量：子进程可以访问的变量

  + 自定义变量改成环境变量：

    ```bash
    sam=string  # 定义自定义变量
    export name
    declare -x name
    ```

    以上两种方法均可

  + 环境变量改为自定义变量：

    ```bash
    export sam=string  # 定义环境变量
    declare +x name
    ```

+ 文件参数变量（默认变量）：执行shell脚本时，可向脚本传递参数

  | 参数         | 说明                                                         |
  | ------------ | ------------------------------------------------------------ |
  | `$数字`      | `$0`是文件名<br>对应参数从1开始                              |
  | `$#`         | 代表文件传入的参数个数                                       |
  | `$*`         | 由所有参数构成的用空格隔开的字符串                           |
  | `$@`         | 每个参数分别用双引号括起来的字符串                           |
  | `$$`         | 脚本当前运行的进程ID                                         |
  | `$?`         | 上一条命令的退出状态（注意不是stdout，而是exit code）。0表示正常退出，其他值表示错误 |
  | `$(command)` | 返回command这条命令的stdout（可嵌套）                        |
  | \`command\`  | 返回command这条命令的stdout（不可嵌套）这里的点是有效的      |

  + 后两个比如：

    ```bash
    #! /bin/bash
    echo $(ls)
    echo 'ls'
    ```


### 数组

shell的数组可以存放**不同类型的值**，只支持一维数组，**下标从0开始**

+ 定义：

  1. 用小括号表示，元素用空格隔开：`array=(sam1 sam2 sam3...)`

  2. 直接定义数组中某个元素的值：`array[索引]=值`

     > 这里显然可以在一个较大的位置赋值，但是其中没有用到的索引是空的，没有空间

+ 读取：

  + 某个元素：`${array[index]}`
  + 整个数组：
    1. `${array[@]}`
    2. `${array[*]}`
  + 取数组长度：`${#array}`

### 命令

#### `expr`

用于求表达式的值：`expr 表达式`

+ 表达式说明：

  + 用空格隔开每一项

  + 用反斜杠放在shell特定的字符前面

  + 对于包含空格和其他特殊字符的字符串要用引号括起来

  + `stdout`      ：expr的返回值，则需要文件参数变量获得结果

    `exit code`：如果表达式是逻辑表达式则和其统一：0/1

+ 字符串表达式：

  + `length STRING`：返回STRING的长度
  + `index STRING CHARSET`：返回set中任意单个字符在string中最前面的字符的位置，**索引从1开始**，如果set中一个都不存在则返回0
  + `substr STRING POSITION LENGTH`：同上，如果后两个参数不合法则返回空字符串

+ 整数表达式：算术表达式优先级低于字符串表达式，高于逻辑表达式

  + `+ - * / % ( )`：参数会转换成整数
    + `* ( )`需要转义，除了转义之外还可以用单引号把特殊符号括起来
    + 只能处理整数

+ 逻辑关系表达式：下列符号都需要转义

  + `| &`：是关系不是位运算：返回对应的值（非空且非0） + 短路原则
  + `< <= = == != >= >`：返回真假，`=`和`==`同义，优先转换成整数，不能则转换成字符集
    + `( )`：改变优先级，需要反斜杠转义

#### `read`

+ 用于从标准输入中读取单行数据

  当读到文件结束符时，`exit code`为1，否则为0

+ 参数：

  + `read 变量名`：向变量名读入
  + `-p`：后接提示信息
  + `-t`：后接秒数：输入字符的等待时间，超过则忽略该命令

#### `echo`

标准输出stdout

+ 用于输出字符串。命令格式：`echo STRING`

+ 显示普通字符串：`echo "普通字符串"`其中引号可以省略

+ 显示转义字符：只能使用双引号或者不使用引号

+ 显示变量：

+ 显示换行    ：`echo -e "字符串\n"  # -e 开启转义`

  显示不换行：`echo -e "字符串\c"  # -e 开启转义`

+ 显示结果定向至文件：`>`

+ 不进行转义或取变量：用单引号

+ 显示命令执行的结果： 用波浪线下边的点

#### `printf`

格式化输出

格式：`printf format-string [arrguments...]`

#### `test`和`[]`

+ 逻辑运算符：`&& ||`：具有短路原则：`exit code`为0是真，非0是假

  > 之前的单与单或是expr内部的，这里的双与和双或是Shell内的

  + 短路原则可用于分支：`判断的语句 && 如果是真要运行的 || 否则要运行的`：如果是假则 &&后边的没有必要运行了，但是还要看看||后的，而如果是真的则相反

+ `test`：用于判断文件类型和文件比较

  + 用`exit code`返回结果，而不使用`stdout`：0真、非0假

    `echo $?`：来得到上条语句的`exit code`

+ 文件类型判断：`test -e filename`

  | 测试参数 | 含义                               |
  | -------- | ---------------------------------- |
  | `-e`     | 文件是否存在                       |
  | `-f`     | 是否为文件                         |
  | `-d`     | 是否为目录，也能判断文件夹是否存在 |

+ 文件权限判断：`test -r filename`

  | 测试参数 | 含义           |
  | -------- | -------------- |
  | `-r`     | 文件是否可读   |
  | `-w`     | 文件是否可写   |
  | `-x`     | 文件是否可执行 |
  | `-s`     | 是否为非空文件 |

+ 整数间的比较：`test 操作数1 操作符参数 操作数2`

  | 测试参数 | 代表意义                 |
  | -------- | ------------------------ |
  | `-eq`    | 是否等于                 |
  | `-ne`    | 不等于                   |
  | `-gt`    | 左操作数是否大于右操作数 |
  | `-lt`    | 小于                     |
  | `-ge`    | 大于等于                 |
  | `le`     | 小于等于                 |

+ 字符串比较：

  | 测试参数            | 代表意义                         |
  | ------------------- | -------------------------------- |
  | `test -z STRING`    | 判断是否为空，空为真             |
  | `test -n STRING`    | 是否为非空，非空为真，`-n`可省略 |
  | `test str1 == str2` |                                  |
  | `test str1 != str2` |                                  |

+ 多重条件判定：和逻辑运算符等效：`test -r filename -a -x filename`

  | 测试参数 | 代表意义           |
  | -------- | ------------------ |
  | `-a`     | 同时               |
  | `-o`     | 至少一             |
  | `!`      | 取反（后面的结果） |

---

+ 判断符号`[]`：`[]`与test用法几乎一模一样，更常用于`if`语句中。另外`[[]]`是`[]`的加强版，支持的特性更多。
  + `[]`内的每一项都要用空格隔开
  + 中括号内的变量，最好用双引号括起来
  + 中括号内的常数，最好用单或双引号括起来

#### `exit`

exit命令用来退出当前shell进程，并返回一个退出状态；使用$?可以接收这个退出状态。

exit命令可以接受一个整数值作为参数，代表退出状态。如果不指定，默认状态值是 0。

exit退出状态只能是一个介于 0~255 之间的整数，其中只有 0 表示成功，其它值都表示失败。

### 循环分支

+ `if`

  1. ```bash
     if codition
     then
     	语句
     fi
     ```

  2. ```bash
     if condtion
     then
     	语句
     else
     	语句
     fi
     ```

  3. ```bash
     if codition
     then
     	语句
     elif condition
     then
     	语句
     elif condition
     then
     	语句
     else
     	语句
     fi
     ```

+ `case`

  ```bash
  case ${变量名称} in
  	值1)
  		语句
  		...
  		;;  # 类似break
  	值2)
  		...
  		;;
  	*)  # 其他情况
  		...
  		;;  # 可选
  esac
  ```

  +  `;;`除了最后一个是必须的，一般建议都不删

+ `for each`

  ```bash
  for var in val1 val2 val3...
  do
  	语句
  done
  ```

  + 参数：
    1. 一系列值
    2. 其他命令结果
    3. `$(sep 起 止)`：输出一系列数
    4. `{起..止}`：其中`...`是关键字，可以是数字或者是字母

+ `for()`

  ```bash
  for ((expression; condition; expression))
  do
  	语句
  done
  ```

+ `while`：为假弹出

  ```bash
  while condition
  do
  	语句
  done
  ```

+ `until`：为真结束

  ```bash
  until condition
  do
  	语句
  done
  ```

+ `break`：跳出当层循环，不能跳出case

+ `continue`：跳过当前循环

+ 对于死循环的处理方法：

  1. `Ctrl + c`
  2. 1. `top`找到进程PID
     2. `kill -9 对应的id`关掉进程

### 函数

+ 函数的return是exit code：0-255的值，0表示正常结束

  > 不写return，默认`return 0`

  1. `$(function_name)`/使用单引号：获得stdout
  2. `$?`：获得return的exit code

+ 格式：

  ```bash
  [function] func_name() {
  	语句
  	...
  }
  ```

+ 函数参数：不需要在格式中的括号中写，在函数内直接通过`$数字`对应使用

  > 注意`$0`仍是文件名，不是函数名

+ 局部变量：`local 变量名=变量值`

# 终端复用器tmux

+ 功能：

  1. 分屏

  2. 允许断开Terminal连接后，继续运行进程

     > `top`：查看进程（任务管理器）

     服务器中的进程如果断开连接则停止

+ 结构：树形：一个tmux可包含多个session，每个session可包含多个window，每个window可包含多个pane

  其中pane是最小单位，每个pane都会打开一个shell对话框

1. `tmux`：新建一个session，包含一个window，window中包含一个pane，pane里打开了一个shell对话框

2. `按下Ctrl + a后手指松开，然后按%`：将当前pane左右平分成带个pane

   `按下Ctrl + a后手指松开，然后按"`：将当前pane左右平分成带个pane

   + `鼠标点击`选择pane/`按下Ctrl + a后手指松开，使用方向键`选择pane
   + 鼠标拖动pane之间的分割线，可以调整分割线的位置/`按下Ctrl + a的同时使用方向键`调整分割线。
   + `按下Ctrl + a后手指松开，然后按z`：将当前pane全屏/取消全屏

3. `Ctrl + d`：关闭当前pane，如果当前window的所有pane均已关闭，则自动关闭window，如果当前session的所有window均已关闭，则自动关闭session

4. `按下Ctrl + a后手指松开，然后按d`：挂起当前session

   `tmux a`/`tmux attch`：返回挂起的session

5. `按下Ctrl + a后手指松开，然后按s`：选择其他session

   + 方向键——上，选择上一项 session/window/pane
   + 方向键——下，选择下一项 session/window/pane
   + 方向键——右，展开当前项 session/window
   + 方向键——做，闭合当前项 session/window

6. `按下Ctrl + a后手指松开，然后按c`：在当前session中创建一个新的window

7. `按下Ctrl + a后手指松开，然后按w`：选择其他window

   + 方向键——上，选择上一项 session/window/pane
   + 方向键——下，选择下一项 session/window/pane
   + 方向键——右，展开当前项 session/window
   + 方向键——做，闭合当前项 session/window

8. 复制粘贴：tmux中的选择需要按住`shift键`

   1. 按下Ctrl + a后松开手指，然后按`[`
   2. 用鼠标选中文本，被选中的文本会被自动复制到tmux的剪切板
   3. 按下Ctrl + a后松开手指，然后按]，会将剪切板中的内容粘贴到光标处

# 文本编辑器vim

每次用vim编辑文件时，会自动创建一个`.filename.swp`的临时文件，此时如果打开某个文件时，该文件的swp文件已存在，则会报错，可以找到正在打开该文件的程序，并退出或者直接删掉该swp文件即可。

+ 功能：

  1. 命令行模式下的文本编辑器
  2. 根据文本扩展名自动判别编程语言。支持代码缩进、代码高亮等功能
  3. 使用方式：`vim filename`
     + 如果已有该文件，则打开它
     + 如果没有该文件，则打开一个新的文件，并命名为`filename`

+ 模式：

  1. 一般命令模式（默认）：可进行复制、粘贴、删除。

  2. 编辑模式：

     在一般命令模式里按`i`，进入编辑模式

     `按下ESC`退出编辑模式，返回到编辑模式

  3. 命令行模式：在一般命令模式按下`:`、`/`、`?`三个字母中的任意一个，进入命令行模式，命令行在最下面，

     ​                       可进行查找、替换、保存、退出、配置编辑器等

+ 命令：

  1. `i`：进入编辑模式

  2. `ESC`：进入一般命令模式

  3. `h`或`左箭头键`：光标向左移动一个字符

     `j`或`向下箭头`：光标向下移动一个字符

     `k`或`向上箭头`：光标向上移动一个字符

     `l`或`向右箭头`：光标向右移动一个字符

  4. `数字+空格`：光标向右移动数字大小个字母

     `数字+回车`：光标向下移动数字大小个行

  5. `0`或`功能键[Home]`：光标移动到本行开头

  6. `$`或`功能键[End]`：光标移动到本行末尾

  7. `G`：光标移动到最后一行

     `:数字`/`数字G`：光标移动到第n行

     `gg`：光标移动到第一行，相当于`1G`

  8. 查找：

     + `/word`：向光标之下寻找第一个值为word的字符串
     + `?word`：向光标之上寻找第一个值为word的字符串
     + `n`：重复前一个查找操作
     + `N`：反向重复前一个查找操作

  9. 替换：

     + `:数字1,数字2s/word1/word2/g`：在数字1和数字2行之间的word1替换成word2

       `:1,$s/word1/word2/g`：全文替换

       `:1,$s/word1/word2/gc`：全文替换，并且在替换前询问用户

  + `:noh`：取消高亮

  10. `v`：选中文本

      `d`（剪切）：删除选中的文本

      `dd`（剪切）：删除当前行

      `y`：复制选中的文本

      `yy`：复制当前行

      `p`：将复制的数据在光标的下一位置粘贴

  11. `u`：撤销

      `Ctrl + r`：取消撤销

  12. `shift + >`：将选中的文本整体向右缩进一次

      `shift + <`：将选中的文本整体向左缩进一次

  13. `:w`保存（`:w 文件名`）

      `:w!`强制保存

      `:q`退出

      `:q!`：强制退出

      `:wq`保存并退出

  14. `:set paste`设置成粘贴模式，取消代码自动缩进

      `:set nopaste`取消粘贴模式，开启代码自动缩进

      `:set nu`显示行号

      `:set nonu`隐藏行号

  15. 连招`gg=G`：将全文代码格式化

  16. `Ctrl + q`：当vim卡死时，可以取消当前正在执行的命令

+ 常见异常：

  异常处理：
      每次用vim编辑文件时，会自动创建一个.filename.swp的临时文件。
      如果打开某个文件时，该文件的swp文件已存在，则会报错。此时解决办法有两种：
          (1) 找到正在打开该文件的程序，并退出
          (2) 直接删掉该swp文件即可

# ssh

+ 登录过程：

  + 登录格式：`ssh user@pastname`
    + `user`：用户名
    + `hostname`：IP地址或域名

  0. 第一次登录会有提示，忽略即可

     > 之后服务器信息记录本机在`~/.ssh/known_hosts`

  1. 输入密码

  2. 默认登陆端口号为22

     登录特定端口：`ssh user@hostname -p 端口号`

+ 本机配置文件：

  + 创建文件：`~/.ssh/config`

  + 文件输入：

    ```bash
    Host 别名
    	HostName IP地址或域名
    	User 用户名
    ```

    > 在该文件下维护多个云服务器

  + 之后即可直接通过别名`ssh 别名`直接登入

  + 密钥登录：

    1. 创建密钥：命令`ssh-keygen`，之后一路回车

       结果：`~/.ssh/`目录下多两个文件

       + `id_rsa`私钥
       + `id_rsa.pub`公钥

    2. 将公钥传给服务器

       1. 将公钥中的内容复制到对应服务器中的`~/.ssh/authorized_keys`文件中

          > 服务器多个公钥回车隔开

       2. 本机使用命令添加公钥：`ssh-copy-id 服务器别名`

+ 本地在服务器执行命令（自动登录、执行、退出）：`ssh user@hostname commad`/`ssh 服务器别名 commad`

## scp传文件

命令格式：`scp source destination`：将`source`路径下的文件复制到`destination`中

+ 多文件：`scp source1 source2 destination`
+ 复制文件夹：`scp -r ... ...`
+ 指定端口：`scp -P 端口号 ... ...`

> 其中参数`-r`和`-P`尽可能放在两组地址之前

+ source和destination是逻辑关系，不是本机和服务器的关系

  + 本机：正常使用
  + 服务器：`服务器别名:...`
    + `服务器别名:/home/acs/...`
    + `服务器别名:家目录下的文件`：服务器的家目录不用起始`~`

+ 配置`tmux`和`vim`

  ```bash
  scp ~/.vimrc ~/.tmux.conf myserver:
  ```

## 云服务器租赁

+ 创建用户：

  ```bash
  adduser acs  # 创建用户acs
  usermod -aG sudo acs  # 给用户acs分配sudo权限
  ```

+ 为用户创建别名和免密登录

+ 装修：

  ```bash
  sudo apt-get update
  sudo apt-get install tmux
  
  # 回到acwing的服务器
  scp .bashrc .vimrc .tmux.conf server_name:  # server_name需要换成自己配置的别名
  ```

  + 只需tmux即可，因为主要开发平台是服务器中的docker

# git

> git是版本管理工具，github是代码托管平台。

+ 工作区：仓库的目录。工作区是独立于各个分支的。
+ 暂存区：数据暂时存放的区域，类似于工作区写入版本库前的缓存区。暂存区是独立于各个分支的。
+ 版本库：存放所有已经提交到本地仓库的代码版本
+ 版本结构：树结构，树中每个节点代表一个代码版本。

1. 初始化：

   ```bash
   git config --global user.name xxx  # 设置全局用户名
   git config --global user.email xxx@xxx  # 设置全局邮箱地址
   ```

   信息记录在`~/.gitconfig`文件中

   > 这部通常是在github上创建好项目后，它会知道具体参数
   >
   
2. 把文件夹创建成一个仓库：进入目录，然后`git init`即把当前目录配置成git仓库，信息记录在隐藏`.git`文件夹中

   > 其中有个HEAD为版本树上的一个结点指针

+ 通过`get status`：查看仓库当前状态

1. 当前本地目录相当于工作区

2. `git add XXX`：将XXX文件添加到暂存区（也是加到仓库索引目录）

   + `git add .`：将所有待加入暂存区的文件加入暂存区
   + 对于”删除文件“这种操作，同样可以将”对应“文件再加入缓存区，此时加入的是对这个文件的删除操作
   + `git reset .`：撤销上一次提交暂存区的操作
   
   + `git resotore --stated <file>`：将暂存区的文件从暂存区撤出：还要管理
   
   + `git rm --cached XX`：将文件从仓库索引目录中删除——不再管理
   
   + `git restore <file>`：将文件的修改撤回到暂存区的版本
   + `git diff XX`：查看XX文件相对于缓存区修改了哪些内容
   
3. `git commit -m "备注信息或者说节点名"`：将暂存区的内容提交到当前分支（情况暂存区）
   + 如果暂存区只有部分仓库所有目录中的部分文件，commit后就只修改这部分

+ `git log`：查看当前分支的所有版本
  + 参数`--pretty=online`一行显示

+ `git reflog`：查看HEAD指针的移动历史（包括被回滚的版本）

1. `git reset --hard HEAD^`或`git reset --hard HEAD~`：将代码库（工作区）回滚到上一个版本

   + `git reset --hard HEAD^^`：往上回滚两次，以此类推

   + `git reset --hard HEAD~100`：往上回滚100个版本

   + `git reset --hard 版本号`：回滚到某一特定版本

     > 版本号：`git log`和`git reflog`均可查看版本的版本号：哈希值的前六位

+ 上云origin：

  > 平台基本回给出提示命令

  0. 在托管平台上的偏好设置中添加SSH密钥为自己的ssh公钥

  1. `git remote add origin git@git.acwing.com:zweix/homework.git`：将本地仓库关联到远程仓库

  2. `git push`：将当前分支推送到远程仓库

     `git push origin branch_name`：将本地的某个分支推送到远程仓库

     > 如果是第一次push需要添加`-u`参数

  3. 克隆：`git clone 在托管平台上找到clone按钮`

+ 分支：默认创建主分支`master`

  + `git branch branch_name`：创建新分支
  + `git checkout branch_name`：切换到`branch_name`分支
    + `git checkout -b branch_name`：创建并切换到`branch_name`这个分支
  + `git branch`：查看所有分支和当前所处分支
  + `git merge branch_name`：将分支`branch_name`合并到当前分支上

  ---

  + `git push --set-upstream origin branch_name`：设置本地的`branch_name`分支对应远程仓库的`branch_name`分支

    > `--set-upstream`参数可不需要

  + `git branch --set-upstream-to=origin/branch_name1 branch_name2`：将远程的`branch_name1`分支与本地的`branch_name2`分支对应

  ---

  + `git branch -d branch_name`：删除本地仓库的`branch_name`分支
  + `git push -d origin branch_name`：删除远程仓库的`branch_name`分支

  ---

  + `git pull`：将远程仓库的当前分支与本地仓库的当前分支合并
  + `git pull origin branch_name`：将远程仓库的`branch_name`分支与本地仓库的当前分支合并

  ---

  + `git checkout -t origin/branch_name`：将远程的`branch_name`分支拉取到本地

+ `stash`：存储没有持久化的修改
  
  + `git stash`：将工作区和暂存区中尚未提交的修改存入栈中
  + `git stash apply`：将栈顶存储的修改恢复到当前分支，但不删除栈顶元素
  + `git stash drop`：删除栈顶存储的修改
  + `git stash pop`：将栈顶存储的修改恢复到当前分支，同时删除栈顶元素
  + `git stash list`：查看栈中所有

# docker

+ 安装：[docker官网](https://docs.docker.com/desktop/)和[acwing所用Ubuntu版本下的docker安装网址]((https://docs.docker.com/engine/install/ubuntu/))

  > 在tmux中安装——防止闪退

  所需执行命令：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Linux/Docker下载.jpg)

  > Tip：如果apt-get下载软件速度较慢，可以参考[清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)中的内容，修改软件源。
  >
  > 1. `vim /etc/apt/sources.list`：把软件园首页的代码copy进去
  > 2. 然后`apt-get update`即可
  > 3. 之后的下载自动利用镜像站中的软件源

+ 将当前用户添加到docker用户组，为了避免每次使用docker命令都需要加上sudo权限，可以将当前用户加入安装中自动创建的docker用户组(可以参考官方文档)：`sudo usermod -aG docker $USER`执行完此操作后，需要退出服务器，再重新登录回来，才可以省去sudo权限。

  > docker很多命令需要sudo

+ 每个docker可以管理多个image镜像，每个image都可以生成多个container容器（这些容器里的环境都是一样的），每个容器都相当于一个完整的云服务器

+ 镜像（images）：

  + `docker images`：列出本地所有镜像

  + 从docker官网拉去一个镜像：`docker pull ubuntu:20.04`：拉取一个镜像

    > 镜像有两部分构成：`type:version`

  + `docker image rm ubuntu:20.04` \ `docker rmi ubuntu:20.04`：删除镜像ubuntu:20.04

  + 迁移镜像：

    1. 压缩：`docker save -o ubuntu_20_04.tar ubuntu:20.04`：将镜像ubuntu:20.04导出到本地文件ubuntu_20_04.tar中

       > 该文件通常权限是不可读，要手动加一个可读权限`chmod +r ubuntu_20_04`

    2. 迁移到其他服务器：`docker load -i ubuntu_20_04.tar`：将镜像ubuntu:20.04从本地文件ubuntu_20_04.tar中加载出来

       将该压缩文件传到对应的服务器即可下载

+ 容器（container）：

  + `docker ps -a`：查看本地的所有容器

    + `docker ps`：查看各容器状态

  + `docker [container] create -it ubuntu:20.04`：利用镜像ubuntu:20.04创建一个容器。

    `docker [container] commit CONTAINER IMAGE_NAME:TAG`：创建某个`container`的镜像

  + `docker [container] start CONTAINER`：启动容器
    `docker [container] stop CONTAINER`：停止容器
    `docker [container] restart CONTAINER`：重启容器
    `docker [contaienr] run -itd ubuntu:20.04`：创建并启动一个容器

    > 这里的参数`-itd`：如果没有d是创建、启动并进入

    `docker [container] attach CONTAINER`：进入容器

    + 先按`Ctrl-p`，再按`Ctrl-q`可以挂起容器

      > `Ctrl + d`是直接关掉容器

    `docker [container] rm CONTAINER`：删除容器（需要容器停止）

    + `docker container prune`：删除所有已停止的容器

  + `docker [container] exec CONTAINER COMMAND`：在容器中执行命令

  + 迁移容器：并没有迁移容器，而是浅出容器的镜像

    + `docker export -o xxx.tar CONTAINER`：将容器CONTAINER导出到本地文件xxx.tar中

    + `docker import xxx.tar image_name:tag`：将本地文件xxx.tar导入成镜像，并将镜像命名为image_name:tag

    > docker export/import与docker save/load的区别：
    >
    > + export/import会丢弃历史记录和元数据信息，仅保存容器当时的快照状态
    > + save/load会保存完整记录，体积更大

  + `docker top CONTAINER`：查看某个容器内的所有进程
    `docker stats`：查看所有容器的统计信息，包括CPU、内存、存储、网络等信息
    `docker cp xxx CONTAINER:xxx` 或 `docker cp CONTAINER:xxx xxx`：在本地和容器间复制文件
    `docker rename CONTAINER1 CONTAINER2`：重命名容器
    `docker update CONTAINER --memory 500MB`：修改容器限制

+ 利用acwing的资源搭建docker：

  1. 在本地将镜像上传到自己租的云端服务器：`scp /var/lib/acwing/docker/images/docker_lesson_1_0.tar server_name:`

  2. 在云服务器将镜像加载到本地：`docker load -i docker_lesson_1_0.tar`

     创建并运行docker_lesson:1.0镜像：`docker run -p 20000:22 --name my_docker_server -itd docker_lesson:1.0 `

  3. 进入创建的docker容器：`docker attach my_docker_server`

     设置密码：`passwd`

  4. 去云平台控制台中修改安全组配置，放行端口20000

  + 则可以通过`ssh root@xxx.xxx.xxx.xxx -p 20000`指定端口ssh
  + 此时配置的docker容器相当于一个完整的云服务器，可以配置其免密登录，注意此时本地的`~/.ssh/config`中要在多加一行`Port 20000`

# thrift

> [thrift官网](https://thrift.apache.org/)

+ rpc模式：srever端提供服务，client通过两方设定好的接口享受服务，thrift则是实现这个目的的工具
+ 上述的c/s的交流本质是信息的交换，所以通信双方必须要知道通信的数据格式和通信的接口，thrift就以这样的方式发挥作用
+ 我们可以在`.thrift`文件中规则一系列的数据格式和通信接口，然后thrift通过这些规定好的规则生成一系列的代码，用户（即程序员）即可在生成的代码中确定交互中的逻辑。
+ 而且thrift还更进一步，它可以让通信双方是任意的语言，而具体的通信的细节有thrift完成

0. 编写`.thrift`文件
1. 编译`.thrift`文件（到特定语言）
2. 在生成的一系列文件中完成自己作为微服务的内部的逻辑

+ 建议版本：`0.16.0`
