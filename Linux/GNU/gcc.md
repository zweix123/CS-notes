
## gcc

```bash
gcc code.c  # complie
gcc code.c -o code.out  # 指定可执行文件名称的complie
gcc -E code.c  # 只做预处理, 结果标准输出
gcc -E -I目录名 code.c  # include "在同目录下找", 该命令指定目录
```

## clang

> k lang

1. 词法分析，得到token

```bash
clang -fsyntax-only -Xclang -dump-tokens code.c
```

2. 语法分析，得到语法树AST Abstract Syntax Tree

3. 语义分析，按照标准确定AST每个表达式类型（编译器并未将上述阶段进行严格划分）

```bash
clang -fsyntax-only -Xclang -ast-dump code.c
```
4. 中间代码生成

+ 中间代码（clang叫LLVM IR，gcc叫GIMPLE）生成

  + `clang -S -emit-llvm code.c`

  是一种抽象层，从多种语言到多种指令集之间的抽象

  即将编译器分出前端和后端

  + 前端：将各种语言变成中间层
  + 后端：将中间层变成各种指令集

5. 优化

   + 满足 observable behavior of the program 程序的可观测行为的一致性

   + ```bash
     clang -S -foptimization-record-file=- code.c
     ```

     优化(常数传播)

     ```bash
     clang -S -foptimization-record-file=- code.c -O1
     ```

   + 查看clang进行的优化

     ```bash
     clang -S -emit-llvm -mllvm -debug-pass=Arguments code.c -O3
     ```

6. 目标代码生成

   ```bash
   clang -S a.c  # 结果a.s
   clang -S a.c --target=riscv64 -march=rv64g
   ```

   + 观察clang尝试哪些优化

     ```bash
     clang -S code.c -ftime-report
     ```

至此我们得到了对应指令集的汇编代码

+ 汇编：根据指令集手册，把汇编代码（指令的符号化表示）翻译成二进制目标文件（指令的编码表示）

  ```bash
  clang -S a.c  # a.o  不可阅读
  clang -S a.c --target=riscv64 -march=rv64g
  ```

  + 使用binutils(Binary Utilities)或者llvm的工具链

    ```bash
    objdump -d a.o
    riscv6
    -linux-gnu-objdump -d a.o
    llvm-objdump -d a.o  # llvm的工具链可以自动识别目标文件的架构
    ```

1. 汇编
2. 链接：
3. 执行

---

+ 未指定行为Unspecified Behavior：标准没有明说，文档也没有说
+ 实现定义行为Implementation-definded Behavior：用户自定义。文档写明
+ 未定义行为Undefined Behavior：不符合标准的行为。但是没说违反了会发生什么

上面的文档，就是ABI Application Binary Interface，计算机系统软硬件协同的重要体现