## Intro

在1976年没有Linux操作系统时(1991)，就已经有了编辑器vi，现在几乎大部分Linux操作系统都默认安装vi，而vim即为`vi improved` — vi的增强版，neovim则是它们的一个分支，意在重构和重写vim的核心部分来实现更好的性能、可扩展性和可定制性，随着两者的发展，已经越来越不兼容，希望下面的命令在两边都能用吧。

+ Reference：
	+ [vim awesome](https://vimawesome.com/)
	+ [阮一峰](https://www.ruanyifeng.com/blog/2018/09/vimrc.html)
	+ [陈皓](https://coolshell.cn/articles/5426.html)
	+ [vim tutor](https://github.com/HanielF/VimTutor)

## Install

|         | vim   | neovim                                                                   |
| ------- | ----- | ------------------------------------------------------------------------ |
| windows | scoop | [scoop](https://github.com/neovim/neovim/wiki/Installing-Neovim#scoop)   |
| linux   |       | [Manual](https://github.com/neovim/neovim/wiki/Installing-Neovim#ubuntu) |

## Config
>Config分成配置文件和插件

### Vim

+ 配置文件位置可通过`:version`查看
+ 插件位置可通过`:set rtp`查看
+ 配色：使用命令`colorscheme 配色名`来设置，其中配色名来自插件目录下的`colors`下的`.vim`文件  
	比如：  
	```vim
	colorscheme gruvbox
	set background=dark  
	```

+ 插件：在vim 8提供官方的插件管理方式/内置包管理器，可通过`:help packages`查看manual
	+ Reference：
		+ [这里提供了一个配置上云的方案](https://blog.hulifa.cn/2019-10-20-Vim-8%E5%86%85%E7%BD%AE%E5%8C%85%E7%AE%A1%E7%90%86%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97/)

## Use

+ nvim按空格（leader）会有提示，一个一个尝试

  14. `:set paste`设置成粘贴模式，取消代码自动缩进
      `:set nopaste`取消粘贴模式，开启代码自动缩进
      `:set nu`显示行号
      `:set nonu`隐藏行号

  15. 连招`gg=G`：将全文代码格式化
  16. `Ctrl + q`：当vim卡死时，可以取消当前正在执行的命令
+ `set nowrap`取消折行

+ 常见异常/异常处理：
  >  每次用vim编辑文件时，会自动创建一个.filename.swp的临时文件。

  + 如果打开某个文件时，该文件的swp文件已存在，则会报错。此时解决办法有两种
    1. 找到正在打开该文件的程序，并退出
    2. 直接删掉该swp文件即可

---

+ 打开目录：
	+ `enter`下一级目录或者进入，`-`上一级目录
	+ `:Ex`从文件中退出到文件的目录中

+ Tab：
	+ `vim -p file1 file2`
	+ 命令模式`gt`一次切换
	+ `tabnew filename`新建tab

+ 在命令模式前缀`!`可以使用Shell命令，其中`%`表示现在vim中的内容