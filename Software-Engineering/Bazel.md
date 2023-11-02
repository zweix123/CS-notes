## Install

+ Reference：[Manual](https://bazel.build/install/ubuntu?hl=zh-cn)

Manual推荐Bazellisk，但是我使用的方式是“使用 Bazel 的 apt 代码库”

>在服务器下载时出现这样的问题：第一步这句话会卡住
>```
>curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor >bazel-archive-keyring.gpg
>```
>先STFW下curl的参数，发现基本都是报错性信息，至少没有对下载的东西进行处理的。  
>再运行下后半句，发现它再等待我们的输入。  
>在本地下载网址内容后发现里面时类似密钥的东西  
>于是尝试将里面的内容放入这句话的管道中，即  
>```
>cat bazel-release.pub.gpg | gpg --dearmor >bazel-archive-keyring.gpg  # 本机下载然后scp到服务器上
>```
>即可运行后面的命令

## QuickStart

+ `WORKSPACE` file，主要其定位作用，一般位于项目目录结构的根目录下
+ `BUILD` files，告知Bazel如何
