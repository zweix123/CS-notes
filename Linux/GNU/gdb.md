GDB, GNU Debugger可以调试很多语言
>   zweix的gdb版本：`GNU gdb (Ubuntu 12.0.90-0ubuntu1) 12.0.90`

+   gdb调试的是可执行程序，加入这个程序名为`exe`，则命令为`gdb exe`进入调试
+   gdb调试的是一个可执行程序，那么在编译这些程序时需要添加特殊指令
    +   C/C++：`-g`
        错误提示：
        ```
        Reading symbols from exe...
        (no debugging symbols found in exe)
        ```
        正确提示：
        ```
        Reading symbols from exe...
        ```
    +   Golang：我没有用特殊指令也能正常调试
        >   需要配置：
        >   1.  vim ~/.gdbinit
        >   2.  添加`add-auto-load-safe-path /usr/local/go/src/runtime/runtime-gdb.py`