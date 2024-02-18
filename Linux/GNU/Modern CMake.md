file(GLOB_RECURSE srcs CONFIGURE_DEPENDS *.cpp)
foreach(v ${srcs})
    string(REGEX MATCH "pingpong/.*" relative_path ${v})
    string(REGEX REPLACE "pingpong/" "" target_name ${relative_path})
    string(REGEX REPLACE ".cpp" "" target_name ${target_name})

    add_executable(${target_name} ${v})
endforeach()


foreach(file ${files})
    # message(${file})
    string(REGEX MATCH "low-latency-insert/.*" relative_path ${file})

    # message(${relative_path})
    string(REGEX REPLACE "low-latency-insert/" "" target_name ${relative_path})
    string(REGEX REPLACE ".cpp" "" target_name ${target_name})

    # message(${target_name})
    add_executable(${target_name} ${file})
    target_link_libraries(${target_name} ${LINK_LIBS})
endforeach()

include_directories(${PROJECT_SOURCE_DIR}/include)

add_subdirectory(./tinydb)

# add_subdirectory(./pingpong)

# CONFIGURE_DEPENDS  在make时自动寻找文件的变化
# GLOB与GLOB_RECURSE 是否递归




> 相信你已经掌握了Makefile

> CMake较于Makefile解决什么问题
>
> 1.  Makefile的语法还是相当复杂的，对于大型项目来说，即使有一定的推导仍然相当繁琐
> 2.  在不同的操作系统、编译器下编译流程是不同的，每在一个环境下需要重新编写Makefile
>
> *   另外CMake不仅可以处理C/C++系列的代码

*   类似Makefile，CMake的源代码存在一个名为`CMakeLists.txt`的文件中

*   使用逻辑和部分命令：
    通过`cmake`命令在某个目录中找到CMakeLists.txt文件并据此生成Makefile和其他相关文件，继而可以通过`make`命令完成编译
    1.  `cmake -B build`：生成构建目录并将生成的Makefile放在`./build`目录下（`-B`参数的作用）
        > manual中使用这样的写法
        >
        > ```bash
        > mkdir build
        > cd build
        > cmake ..
        > ```
    2.  `cmake --build build`：执行构建
        或者`cd ./build/ && make`（当然如果生成的不是makefile就是其他事情了）
        可执行文件在运行了make的目录中

## 语法

*   对于关键字CMake不区分大小，建议小写

```CMake
cmake_minimum_required(VERSION 3.9)  # 指定最小CMake版本要求
#  官方文档有更鲁棒的写法

project(项目名)  # 设置项目名称
#  当然也能设置其他项目属性

add_executable(可执行文件 xx1.cpp xx2.cpp ...)  # 生成可执行文件
# 后面是其依赖，只需要.cpp，CMake会自动寻找其依赖

add_library(库名 库类型 库依赖.cpp ...)  # 生成库
```

*   生成库
    *   库类型
        *   `STATIC`静态库

    *   生成库的作用：重构代码，将一个局部的代码放在同一个子目录下而只暴露接口（库）

*   子目录：含义同上，一个子目录也有一个CMakefile.txt，其管理其目录下的编译流程和依赖关系
    *   添加子目录：
        ```CMake
        ...
        add_subdirectory(子目录名)
        ```
    *   重构：
        1.  子目录：
            ```CMake
            target_include_directories(库名 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/...)
            ```
            *   其中的变量为CMake的内置变量，表示项目根目录路径
            *   `PUBLIC`
                `PRIVATE`
        2.  根目录：
            ```CMake
            target_link_libraries(当前项目结果可执行文件 库名)
            ```

*   第三方库：
    ```CMake
    find_package(引入后的名 在第三方库的README里找一下)  # 用于在系统中寻找安装的第三方库的头文件和库文件的位置
    ```
    之后第三方库内的库可以通过`引入后的名::库名`使用

### 语句

```CMake
    # message(类型 内容)
    message(SEND_ERROR "error!")  # 打印一个错误
```

### 变量

*   创建变量：
    ```CMake
    set(变量名 默认值 类型 描述)
    ```

*   场景
    1.  库中的某些值需要调用该库的代码在编译时确定
        ```CMake
        target_include_directories(库名 一个宏变量名称=$(上层的一个变量))
        ```
        *   如果上层变量是字符串，定义的宏也是字符串，则需要`"$(...)"`这样子用
        ```bash
        cmake -B build -D变量名=值  # 参数之间没有空格
        ```
        > 或者将`cmake`换成`ccmake`，它会提供一个命令行的UI，在里面手动的去改

### 分支

```CMake
if (...)
    ...
else()  # 可省略
    ...
endif()
```



