都说Windows上的命令行功能比较差劲，其实我觉得和Unix相比各有千秋，毕竟可以相互借鉴嘛。我个人感觉是因为更多的人在初次接触Windows使用的是图形化，而在接触Linux则是先使用命令行，有先入为主的问题。如果非要说的话就是兼容了，cmd和pwsh(或者powershell)命令的差异可比bash和zsh的差异大多了。我在这里记录下用cmd或者pwsh的比较有意思的操作。

# 在脚本中新开一个窗口运行其他命令

+ 在cmd中
	+ 新开一个窗口运行：`start cmd ./c ping localhost`：这个命令会开一个cmd运行ping，并且完成关闭窗口
		+ `start cmd ./c ping localhost`：这个和上面很类似，但是不会关闭新的窗口
		+ 这个命令直接运行无论是在cmd里还是在pwsh都是可行的，但是放在bat中在cmd则会报错

	+ 在一个脚本中调用另一个脚本：`call file.bat`
+ 在pwsh中
	+ `Start-Process cmd -ArgumentList '/c ping localhost`：效果同上，参数效果同上
	+ 我们通过修改这里的`cmd`即可改变打开的shell类型

+ 既然是开新窗口，可能是需要并行操作  
	在pwsh中
	+ 添加参数`-Wait`，效果等同系统调用`wait`
	+ 还有一个玩法是`Start-Process cmd -ArgumentList '/c ping localhost' -NoNewWindow`，在一个窗口并行的运行两个进程
	+ 既然想到多进程了就没必要在窗口这里纠结了`Invoke-Expression 'ping localhost`后台执行命令

