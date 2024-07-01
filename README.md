<!-- https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/ -->
<!--
<span id="锚点">内容内容内容</span>
<a href="#锚点">链接</a>
-->


## 声明

+ 该项目是我个人的笔记，部分会刻意制作成Blog，但大部分仍然是我个人的Note，除非特殊声明，否则不建议作为学习资料。
+ 该笔记部分插图来自各种书籍、课程或其他资料，若涉及任何版权行为，请联系我，我将删除内容。
+ 对于课程笔记，我严格遵循[Academic Integrity](http://integrity.mit.edu/)，虽然在笔记中可能记录思路，但是代码肯定是Private的，如果有不合适的地方，请提醒我。
+ 文中所有内容，与本人现在，之前或者将来的雇佣公司或组织无关。
+ 本人保留自省的权力，即你看到的内容不一定代表本人最新的认知和观点。
+ 项目下所有文章除特别声明外，均采用[CC BY-NC-SA 协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)，转载请严格准守。

## 链接

+ [CSRankings: Computer Science Rankings](https://csrankings.org/#/fromyear/2016/toyear/2024/index?arch&mod&world)

+ 个人常用的稳定信息源推荐：
    + [阮一峰的网络日志](https://www.ruanyifeng.com/blog/)：每周五更新，自上而下分别是封面图，博客，科技动态，文章，软件，工具，资源，图片，文摘，言论。部分内容由用户投稿，时常能出现让人眼前一亮的玩意。
    + [潘乱的乱翻书](https://www.xiaoyuzhoufm.com/podcast/61358d971c5d56efe5bcb5d2)：不定期更新，大部分内容为针对一个互联网问题或产品要求互联网从业者进行讨论，相当于是业务方面的学习。
    + [数据库内核月报](http://mysql.taobao.org/monthly/)：阿里某团队维护，每月更新。
    + [美团技术团队](https://tech.meituan.com/)：美团维护，不定期更新。
    + [RustTalk](https://rusttalk.github.io/)：R！

+ CS RoadMap：
    >仅作记录，不作推荐

    + [CS DIY](https://csdiy.wiki/)
    + [Teach Yourself Computer Science](https://teachyourselfcs.com/)
    + [PingCAP Awesome Database Learning](https://github.com/pingcap/awesome-database-learning)

+ 有启发性的文章：
    + [1%慢请求优化](https://drmingdrmer.github.io/math/engineering/2014/07/24/slow-request.html)
    + [互联网中对象访问频率的91分布](https://drmingdrmer.github.io/tech/2019/10/30/zipf.html)

+ Tools：
    + `https://ipinfo.io/$ip/loc`：获取公网IP的坐标

## 输出

+ [博客](./blog/README.md)：只赠有缘人
+ [面经](./recruit/README.md)：只赠有缘人
+ 开发机配置指南：正所谓工欲善其事必先利其器，这真不是差生文具多，是实打实的生产力提升。

    + [Windows开发机配置指南](./Missing-Semester/WindowsConfigGuide.md)：如题
    + [Linux开发机配置指南](./Missing-Semester/LinuxConfigGuide.md)：如题
    + Apple系：
        + [IPad学习机配置指南](Missing-Semester/iPadConfigGuide.md)：如题
        + [Mac开发机配置指南](Missing-Semester/macConfigGuide.md)：如题

    和平台无关的：[SSH](Missing-Semester/SSH.md) | [Git](Missing-Semester/Git.md) | [Markdown](Missing-Semester/Markdown.md) | [VSCode](Missing-Semester/VSCode.md) | [LaTeX](Missing-Semester/LaTeX.md)

+ [侵入式数据结构和非侵入式数据结构的区别](./Algorithm/Junior-Data-Structure/侵入式和非侵入式数据结构.md)
+ [不同编程范式的量化交易回测系统](Interdisciplinary/Quant/Survey-BackTest.md)
+ 软件推荐：
    + 命令`neofetch`：现代风格地查看机器信息
    + [命令`fd`](https://github.com/sharkdp/fd#installation)（好用！）：按文件名递归查找
    + 命令`rg`（好用！），特别的`alias rg='rg --hidden --no-follow --max-columns 255 --no-heading --column -F'`：按文本内容递归查找
        >`ag`已经是历史的眼泪了

    + `ranger`，当然，它同样有了新的实现，比如用Golang实现的`lf`，用Rust实现的`Yazi`
    + [noti](https://github.com/variadico/noti)：在终端使用的命令完成时弹窗提示的工具

+ Tips：
    + PDF文件下载：zlibrary+谷歌搜索关键字末尾添加`filetype:pdf`

## 笔记意义

### 来自大学三年

1. 在初学时
     + 在学习时记下笔记有助于记忆  
     + 在整理时重构笔记有助于搭建知识体系  
         随着进一步学习，我们对同一知识的理解发生变化，会动态的调整笔记（重构知识体系的过程）

2. 在实践时  
     通过笔记快速的回忆起学习时的理解或者查找对应的知识点

但随着时间的推移，笔记的作用减少了

+ 常用的 、 重要的知识点内化于心
+ 零碎的 、 细节性的知识现用现查

此时笔记更像是 ” 当年攻城略地时的纪念品 “。

### 来自实习一年

+ 现在(初次实习)看来笔记不是一个结果，而是一个过程。工作之后，少有整块时间学习，又通勤时间过长，故基本是在地铁上学的，读资料的时候确实感觉学到了东西但是很快忘记。不能即时记笔记意味着不能很好的构建（并重构）知识框架，也不能通过整理进行反复记忆。这就是导致学完之后对知识的吸收很少，如果能充分记笔记可能会有更好的学习效果。花有重开日人无再少年呀。

+ 在最开始刚接触一个领域时，任何知识对我都是新的，于是笔记是非常详细的。  
    随着我对这个领域的深入和实践，对最基本的概念已经有了自己的理解，此时再事无巨细的记录只会徒增复杂性，此时的笔记侧重重点难点或者整体框架。

# RoadMap

>我认为计算机最有普遍意义的天赋只有一种 —— 行动力
>+ 立刻去做的行动力
>+ 坚持去做的行动力

>>好吧，当然还需要独立思考和深度思考

>顺便讨论下完美和完成哪个更重要，仅讨论在计算机相关知识学习方面的，我表达下个人的看法。我认为完美比完成更重要，因为我做事的发念是好奇心，如果第一次做不好很可能就没有下次了。

+ 发心：
    + 自用：我个人有强迫症，想让自己在计算机领域的知识体系很系统，但熵增定理告诉我们这样阻力很大，我希望通过笔记去对抗它
    + 费曼学习法：我会设想有一个人在看这篇记录，用词尽可能有易读性，比如简介下资料内容 、 推荐程度~~和适合人群~~

+ 说明：我本科的学习方法论是理论结合实践螺旋上升
    + 理论结合实践：Donald Knuth曾经说过"If you find that you’re spending almost all your time on theory, start turning some attention to practical things; it will improve your theories. If you find that you’re spending almost all your time on practice, start turning some attention to theoretical things; it will improve your practice."，我这里也提供一个工程类的视角理解这句话，如果我们要写一本教材，我们要选择一个主题，我们希望可以写出这个主题的方方面面，各个层次 、 各个细分以及它们的发展和现状。但我们发现如果一本教材想要实现理论和实践相结合是要做取舍的。如果想概念方面面面俱到，很难辅以实践，各个概念分别给出实践很零散，而且并不是所有的概念都有适合学习的实践。目前对这个问题的一种解决方案就是开发相对独立的配套实验嘛。还有一个方案就是专门写实践的书籍，这本书就是主要讲怎么实现某个东西，然后在这个过程中讲这个领域的相关概念，那么我们发现这样组织就很难展示尽可能全面的概念。所以我在资料的选择方面就涉及上面说的几种类型的资料。
    + 螺旋上升：这个是理论结合实践在时序上必然体现的结果，我们可能对某个领域的某个概念以不同的视角 “ 重新 ” 学习。

+ 下面的文字无形中成为学习资料的推荐，但是这里有一个问题，比如我对一个领域是入门，此时我选择一份资料，即使它客观上很差甚至有错误，我也能学到东西，同时无法识别出中间的错误。比如 《C++ Primer Plus》，这是我的第一本 C++语法书，后面再提到它我只评价是语言版本落后，但是实际上其中有很多知识是错误的，这是别人识别出来的，在我看的过程中是没有能力辨别的，这就导致我无法对学习资料做出正确的判断。

+ 对于涉及项目（实践结果是一个项目）的部分，我会在下面使用这个🤏emoji进行标注，表示相关项目体量比较小，适合作为练手项目，但不足以写在（本科校招）简历上。定量的说，我希望代码行数在3k行以下的使用该符号标记；值得讨论的是，比如《Crafting interpreters》中涉及的Lox的C语言解释器，其代码行数虽然在3k行，但是由于是C语言实现的且麻雀虽小五脏俱全，其实思维难度不小，但是由于其代码全部开源且相当于有逐行解释的手册，所以认为其是练手项目；而xv6 lab中虽然学生添加的代码比较少，但是由于整个xv6项目规模不小且整个lab思维难度较大，所以认为是可以写在简历上的。而诸如B站小彭老师的一些课程，实现Vector或者实现Json，则毋庸置疑是练手项目，而像BusTub lab这种整个项目在3w行左右，学生添加的行数在4k行左右的则毋庸置疑是可以写在简历上的项目。

+ 大学基础：
    + [How to ask questions the smart way](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)：
    + [x] 上海交通大学生存手册：[我的书评](https://www.zhihu.com/question/23633140/answer/2247825107)
    + 杭州电子科技大学CS指南：个人没有看完，但是可可佬说很好，这里也推荐下。

## 数理基础

+ 数学基础：
    + 微积分：
        + [x] 宋浩：应付期末 、 草草看完，早忘光了。
    + 线性代数：
        + [x] 宋浩：应付期末 、 草草看完，早忘光了。
    + 概率论：
        + [x] 宋浩：应付期末 、 草草看完，早忘光了。
    + 信息安全：
        + [x] 《 深入浅出密码学 》：比较推荐，我目前需要的绝大部分密码学知识都来自这里，在做Web3或者其他东西时对这方面不犯怵了

+ 物理基础：上课（很少听讲），学校老师讲的应该算挺好的。
+ 电子基础：
    + 数字电路
        + [x] 上课（草草看完录播），学校老师讲的确实挺好的。
        + [x] 《编码 · 隐匿在计算机软硬件背后的语言》：这本书的范围比数电这个科目要大，是从最基本的逻辑门开始直接干到概念性的计算机，但是偏简单，为了平缓的学习曲线放弃了深度，~~适合高三~~。

## 专业知识

+ 信息学导论：
    + [x] [csdiy.wiki](https://csdiy.wiki/)：我没开玩笑，我在刚上大学时看了无数人的学习路线规划，感觉抄来抄去，但是csdiy属实是有世界观刷新感觉，强烈推荐。~~不过可能过几年 Lab 也是人均了（~~
    + [x] Crash Course Computer Science：神奇的网课，语速极快的overview了CS的各种topic，比较推荐~~高中毕业~~。

+ 编程入门：
    >我有点遗忘在第一次接触编程的感觉了，不太能换位到一个初学者的视角；不同人进入编程世界的入口是不一样的，这个阶段可能会花一些时间找找感觉。

    + [ ] CS61A（SICP, Structure and Interpretation of Computer Programs）： CS-DIY的第一门课，还没看过， SCIP也被称为是一个常看常新的书，比较向往，先Mark下。
    + [x] Acwing Linux 基础课/Missing-Semester：这两门课有一小部分重叠，主要讲 Linux 的操作和工具，我觉得非常实用，前者内容更少，所以讲的更细致（给了很多演示），但是它是服务于它自己后面的课程的，够细但不够多，所以需要后者作为补充；后者非常的全面，会讲到我们在实际开发中会遇到但是不会有人系统讲的东西。强烈推荐。

+ 计算机系统基础：
	+ [ ] CSAPP/CMU15-213：纯纯看书，没有做课后作业 、 没有看课程录像。先鸽了。

### 编程语言

>语言是互通的，一个新语言的诞生必然要考虑用户教育成本，一个显而易见的方案就是和之前的语言更像。  
>所以我在编程语言的学习方案从开始是系统的看大部头的书籍到后是面看 Quick Start 文档然后直接上手。

+ C：
	+ [x] 《C Primer Plus》：C 语言学习的不二之选，我当时有 C 语言基础，但是不够系统，于是看的这本书，用了五天五夜，看完后可以在小范围当语言律师了。

+ C++：

    >[StackOver 上的 C++书籍推荐](https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list)


    + [x] 《C++ Primer Plus》：不评价，不推荐。

            下面的几本书真是值得反复刷呀。

        + [x] 《C++ Primer》（以下简称 c3p）：毫无疑问的成为C++初学者的第一本书，比较推荐，但我个人认为它还是有股 C++98 味儿。

            下面的几本书必须要二刷，因为c3p毫无疑问是给新手准备的，但是C++太深奥了，刚看完 c3p肯定要继续看下面来学习更Modern的特性和最佳实践，但是在没有足够实践的基础上绝对是理解不到位的，在充分实践后再来看会有崭新的体验。

        + [x] 现代 C++30讲/32讲：一个课程的文字记录，是《C++ Primer》必要补充。本身更多是提纲挈领的说明一些要点，对细节想要更深刻的理解肯定要看更多的资料。或者它本来就是一个提纲，为我们打开Modern C++的大门。
        + [x] 《Effective Modern C++》：本来想看《Effective C++》的，它被称为 Effective 类书籍的鼻祖，但看评价觉得它不够Modern，而这本书是它的continuation和correction。强烈推荐！惊叹于 C++的博大精深，这本书对我个人而言说清了很多我过去模棱两可的事情，看完之后越发感觉自己还是 C++的初学者。

        我也想大言不惭的表达下该如何学习 C++，推荐叔叔的[博客](https://zclll.com/index.php/cpp/get_started_cpp.html)。好吧我写不出比叔叔更好的，"眼前有景道不得，崔颢题诗在上头"，算了算了。
    
        + [ ] 《C++ Templates The Complete Guide》
        + [ ] 《C++函数式编程》\[塞尔维亚\]伊凡·库奇

+ Python：
	+ Manual：Python这种语言看Manual就行啦
	+ B站码农高天，他是CPython的Contributor，Python相关教程很不错，适合想精深Python的。
+ Golang：
	+ Manual，Golang官方的Tour of Go就非常好呀。
	+ https://github.com/golang/groupcache
	+ [Go语言设计与实现](https://draveness.me/golang/)：从名字也能管中窥豹，这不是讲Golang语法和项目的书籍，而是讲它是怎么实现的
+ Rust：
	+ [ ] 《The Rust Programming Language》 | 中文出版书《Rust权威指南》 | 中文在线版《Rust程序设计语言》 | Rust Book：
	+ [x] [rustlings](https://github.com/rust-lang/rustlings)：真的不由得感叹一句 “ 太现代了！”，它的思路是提供很多无法编译的Rust代码，然后供我们修改，在实践中理解Rust的各种语法（显然这些 Bug 涉及的语法特性应该是难度递增的）。它的特色是提供了全自动交互环境，就像玩游戏闯关一样。具体的，我以我的流程为例，将项目Fork到自己的github中，然后clone下来，在本地搭建好Rust相关环境后，编译`rustlings`。然后在项目目录下打开VSCode，不需要Explorer，整个屏幕就有一个编辑区和终端，然后让他们左右放置（以往我都是上下放置），然后在终端启动 `rustlings watch`，就会自动找到最近的需要修改的代码，VSCode的终端是可以点击链接打开，自然就拿到了需要修改的文件，然后保存，终端自动重新测试，错了给出编译报错，成了给出下一个需要修改的 Bug。这就很像游戏呀。然后`rustlings watch`是有`hint`的，因为我没有学过Rust，直接以练代学，所以基本每个我都`hint`一下，它会给出Rust Book的链接，这个时候我再去看书。整个学习体验棒极了。
	+ [ ] 《Rust By Practice》：
	+ [ ] 《Programming Rust - Fast, Safe Systems Development》：
	+ [ ] 《Hands-On Concurrency With Rust》：
	+ [ ] [《Learn Rust the Dangerous Way》](https://cliffle.com/p/dangerust/)

### 数据结构

+ [x] Acwing算法全家桶，我不想评价Acwing和yxc，但结合性价比，这个可能是国内最适合初学者的一套教程了。

### 编译原理

>编译原理在整体计算机知识体系中似乎是一个比较独立的部分，但是我个人感觉非常有学习的必要
>+ 它为我们展示了计算机看待程序的视角
>+ 它为我们展示设计编程语言的方方面面

+ [x] 《Crafting interpreters》【🤏】：这本书自底向上手把手的带读者使用C语言实现一个有闭包、类、垃圾回收的动态类型语言。是我2023年看到的最好的技术书（这个受到了 《Effective Modern C++》的冲击），总之非常推荐。
+ [ ] 华盛顿大学课程《Programming Languages》：
+ [ ] 《Essential of compilation》

### 体系结构

>个人感觉计算机组成原理 、 体系结构 、 操作系统（的一部分）并不能泾渭分明的划分，这里以体系结构统称

+ [x] 王道考研的计组课：应付期末，草草看完。

+ [ ] 南大ICS PA：只看了余子豪的课，还没来得及做实验，应该也鸽了。
	+ 让我对计算机底层有了全新的理解
	+ 学到了很多对 Coder 来说很珍贵的的品质：Unix 哲学 、 如何提问 、STFW/STFM/RTFSC 等等
	+ 相信机器是永远正确的，相信 Bugs 一定是能观测，可复现，你能够解决的。如果不是，那一定是没有找对合适的工具，没掌握正确的调试手法。
+ 《计算机组成与设计：软件/硬件接口》
+ 《Computer Architecture A Quantitaive Approach》（又称《量化方法》）
+ [ ] [CS152](https://inst.eecs.berkeley.edu/~cs152/sp24/)：[videos](https://www.bilibili.com/video/BV1yP411U7xh/?buvid=YD4427D0E2F425F24DC3B3E141423100995B&from_spmid=search.search-result.0.0&is_story_h5=false&mid=GEs0LBvW7TE0b7OO54MY4A%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=iphone&share_plat=ios&share_session_id=B1036BC8-7F30-4F71-97DB-0D6EC7ED0B04&share_source=QQ&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1706339671&unique_k=Vv6ultm&up_id=7006687&vd_source=4ee99d4ebd507c7277fa312ed28dbdda)，川流严选，先mark下。

### 操作系统

+ [x] 王道考研的操统课：应付期末，草草看完。
+ [x] MIT6.S081：资料方面只看了xv6 Manual和野生课程内容翻译，然后直接啃实验，以实践为主，缺乏理论由OSTEP补充。
+ [x] 南大蒋炎岩操作系统/OSTEP：蒋老师说他的课是OSTEP导读，但蒋老师的课很有个人风格，推荐课程；蒋老师评价OSTEP为最好的自学OS的资料，我的第一本英文书，全程在地铁上看完的，没有课后作业，没有记笔记，非常推荐（其实中文版就翻译的挺好，没必要硬啃英文版）

### 计算机网络

+ [x] 谢希仁的《计算机网络》（第七版）：教材
+ [x] Stanford CS144（2023）：使用C++20实现了字节流、重组器、TCP的两端、数据链路层和网络层的接口、IP的路由选择。其中的项目结构（包括CMake相关代码）和几个Util类（地址的封装、文件描述符的封装、Socket的封装）都挺值得学习的。做完才意识到删除了往年最难的部分，难度低了很多，应该适合新手。遗憾的是这就导致后几个实验比较零碎，未能得到一个完整可用的TCP协议实现。

### 广义下的存储

```
MapReduce                     ┌──────►Codis               
     │                        │                           
     │                      Redis                           
     ▼                        │ │                           
    GFS                       │ └──►Redis-Cluster           
     │                        │           │                 
     │                        │           ├─────────►KVRocks
     ▼                        │           │                 
BigTable────►LSM Tree───►LevelDB────►RocksDB              
     │                                    │                 
     │                       ┌────────────┴───────►TiKV     
     ▼                       │                              
 Raft───────────────────► etcd                            
     │                                                      
     │                                                      
     ▼                                                      
 Paxos                                                    
```

#### 数据库

+ [x] 王珊、萨师煊的《数据库系统概念》（第五版）：教材
>萨师煊先生是我国数据库的奠基人。
+ [x] 《Build Your Own Redis with C/C++》和《Build Your Own Database From Scratch》【🤏】：分别用C with STL实现mini Redis和Go实现mini关系型数据库，我个人完成了第一个和第二个的 B+Tree 部分（有bug），第一本中我将作者的 C 实现改成Modern C++实现，但是对于侵入式数据结构还是一股C味儿，后面有机会可能结合CRTP重写。对于第二本，写出的 B+Tree不符合预期，而且作者使用的B+Tree是比较特殊的变种，作者没有好好描述、网上也没有很好的描述，于是作罢，以后有机会写15445吧。嘻嘻，写完15445的B+Tree了，果然要科学的多（拉踩一波）。

+ [x] <span id="CMU15445">CMU 15445 Lab 2023 Spring：在23年春季版本中，我们首先实现一个面向磁盘的内存管理器作为整个数据库的基础，然后实现一个很有意思的数据结构B+Tree来实现数据库索引，这也是我选择23春季版本而不是秋季版本的原因。之后则是深入到数据库的相关概念中，火山模型和事务系统。还有其他的涉及优化的可选作业，我是最小实现，没有做任何优化。首先要感谢老师 、 助教和其他为该项目贡献的人，是你们的付出才有了如此精致的课程。其次是十分感谢群友，没有群友前辈的点拨我是万万不能完成的。我在这个过程中，也遇到一些坑，收集整理一些资料，在[这里](./Database-System/CMU15445.md)，我过了一遍，保证符合学术诚信，这里包括我遇到的坑点，还有对相关知识的整理，比如 B+Tree 伪代码里面的数值逻辑和模糊概念的梳理，还有关于事务系统这个名词之间的关系和限制（Project4 的 Handout 有点离谱）。这个过程中，特别是 P3 和 P4，看来很多前辈的文章攻略，我个人觉得这是不违反学术诚信的，因为客观开发项目也是需要文档手册的，而 Handout 真的不是一个好手册；当然，jyy 老师也说过，在工业场景，并不是所有问题都有答案和指导，在没有指导的情况下完成也是需要训练的。但是这里过于离谱，没有说明算法流程可以接受，但是相关概念也没有说清，是甚至需要对照野生样例反推语义；当然这又涉及另一个话题，“ 共享测试样例 ” 是不是不违反学术诚信，见仁见智吧，没这个我真过不了了呀，太菜了。然后是这个[bustub_2023spring_backup](https://github.com/zweix123/bustub_2023spring_backup)，这是 23 春季起始代码的副本，当然正常途径是 reset 或者找 release，但是我当时并不知道这样的方法，不管怎么这个可以给您节省一些时间。除此之外，这里添加了两个部分，一个 `script.py` 的脚本，这个本身也是我常用的一个命令行工具框架。一方面，这里收纳整理实现所需要的命令，`--help` 即可查看，这个存在的必要是什么？命令还需要整理？实际上，15445 的每个测试（或者 format 或者 submit），都需要两个命令以上，当然可以通过`&&`和历史命令补全来实现，但是终究是麻烦，该脚本提供了简写，除此之外，这样也让可以 “ 记住 ” 所有命令成为可能，我个人的调试方法几乎只有一种方法，那就是打日志，我需要高频的重复运行测试代码，所以对我个人很有用。另一个方面，这里有三个有意思的命令，`viz` 是按照代码中持久的命令生成 B+Tree 可视化，`viz-repr` 是以交互的形式生成 B+Tree 可视化，使用的都是 15445 提供给我们的工具，前者帮助我们快速的复现错误的 B+Tree 形态，后者的使用体验我相信和 15445 提供给的 Web 的体验一样。它帮助我在 P2 非常快速的发现了出现错误的样例。还有一个是 `terier-debug`，这里借用 6.824 中的工具中的一些技巧，将多个线程的日志并排的按时间输出（不过我用的并不多）。所以这个脚本极大的提高了我的开发和排查效率。另一个是更多的测试，它和前面的脚本是对应的，收集了一些我使用的民间测试样例（还有一些纠错）。希望可以给大家帮助，祝各位武运昌隆。</span>
+ [ ] CMU 15-721

#### 分布式系统

+ [ ] MIT6.824：看完了部分课程的讲义和完整的课程字幕翻译记录，主要以了解知识点为主，因为我的实习项目就是分布式存储，工业界的实践就在眼前，所以课程实现没有做。
	+ [x] [MapReduce](./Distributed-System/MapReduce.md)
    + [ ] GFS
    + [ ] BigTable
    + [x] [Raft](./Distributed-System/Raft.md)
    + [ ] Zookeeper
    + [ ] Spanner
    + [ ] Ceph

#### 存储

+ [ ] 《Direct Data-independent acquisition》（简称DDIA）
+ [ ] 《数据存储-架构与技术》舒继武：海舟哥严选，先mark下

### 高性能和并行计算

+ [ ] MIT 6.172 Performance Engineering Of Software Systems
+ [ ] 《Programming Massively Parallel Processors： A Hands-on Approach》4th Edition

### 图形学

+ GAMES系列

### 人工智能

+ dlsys, [Deep Learning Systems](https://dlsyscourse.org/)：
+ [动手实战人工智能](https://aibydoing.com/intro)
+ [llya Sutskever 30u30](https://www.reddit.com/r/ArtificialInteligence/comments/1cpbh1s/ilya_sutskever_if_you_really_learn_all_of_these/?rdt=49832&onetap_auto=true&one_tap=true)

### 业务开发

+ [x] Acwing工程课的Django和前端：优势的很简单，缺点是太简单；低年级可以看看，否则没必要了。

## 人文学科

+ 文学：
    + 理论：
        + [ ] 《文学讲稿三种》美国的弗拉基米尔·纳博科夫
        + [ ] 《给青年人的十二封信》 朱光潜

    + 科幻文学：这部分的书评比较尴尬，我不能剧透，但是也无力提供深刻的解读。
        + 刘慈欣：

            +  
                + [x] 短篇小说《赡养上帝》：假如上帝是一个客观存在的、创造人类的种族。
                + [x] 短篇小说《赡养人类》：人类发展的一种终极情况。

            + [ ] 短篇小说《乡村教师》：老师和孩子们无意中拯救了整个地球。
            + [ ] 短篇小说《中国太阳》：双线叙事，一个人从农村的无知状态，到整个人类最激进的宇宙开发者。
            + [ ] 《超新星纪元》

        + 阿西莫夫
            + [x] 短篇小说《最后的问题》：超级AI与人类发展到整个宇宙最广泛物种。

+ 人际关系理解力：正如张作霖所说 “ 江湖不是打打杀杀，江湖是人情世故 ”（自动配音李雪健老师）

    + [x] <span id="吴思">吴思的《潜规则》和《血酬定律》</span>：这两本书的性质更像是文摘，它们组合起来通过较多的事例让读者明白某种道理。“潜规则”和“血酬定律”是分别对官与官、官与民之间的这种道理的比较好的概括，所以才选择这两个名字。那么作者想表达的道理究竟是什么？我是这样理解的，从人的本质出发，人首先是动物，有趋利避害的本能，然后再是人，在人类社会中的不同位置。相互之间有**损害**或者**使获益**的能力。这种相互的力推动人们进入新的位置，并不是由于个人品质才导致某个位置的人变到另一个位置，而是由于利害计算。书中以此视角解释了诸如贪官、造反等等话题。抛开其表达的思想，书本身很好读，在读之前以为会很晦涩，但读起来发现可以理解为一个个历史故事组成的，作者以他的视角对历史事件做出新的解读，让人眼前一亮，可读性不错。
    + [ ] 小说《沧浪之水》

+ 中国：
    + [ ] 《乡土中国》-费孝通
    + [ ] 《毛泽东选集》
    + [ ] 《中国式管理》 曾仕强
    + [ ] 蒙克MK
    + [ ] 《中国历代政治得失》
    + [ ] 《参谋助手论》

+ 心理学：
    + 对死亡的思考：
        + [ ] 《末日船票》 罗小茗

    + 人的成长：这也是我最近的体会，至少在年轻的时候，人的观念变化是比较剧烈且频繁的，这种变化是通过一个个事件、一次次谈话中发生的。这样的变化发生在每个人的成长过程中，如果TA们将其总结成书，读这样的书就像和一个前辈说话，会有所思考。

        + [x] 《优秀的绵羊》：作者是耶鲁大学招生相关的工作人员，本身的教育经历也非常丰富，他观察并和很多同学交流意识到，排名很高的院校的学生简历非常漂亮，但是普遍缺乏我理解为做事的发心和真挚的人际关系感情，这要么已经在他们中暴露出心理问题，要么他们职业中后期出现迷失；后面讲了现在整个美国高等院校招生现状的历史由来，其实这里有很多我国高效的影子。后面讲了作为学生怎么避免这种情况，即博雅教育+尽可能多的接触不同圈层的人（无论向上还是向下）。最后更进一步批判精英阶层的一些问题（可是又有什么用呢？）
        + [ ] 《被讨厌的勇气》

    + 网红书：
        + [ ] 《刻意练习》
        + [ ] 《思考，快与慢》
        + [ ] 金一南《胜者思维》
        + [ ] 《为什么我们总是在防御》
        + 吴军：
            + [ ] 文明之光
            + [ ] 大学之路
            + [ ] 浪潮之巅
            + [ ] 数学之美

+ 历史学：
    + 尤瓦尔·诺亚·赫拉利的简史三部曲
        + [ ] 《人类简史》
        + [ ] 《今日简史》
        + [ ] 《未来简史》
    + [ ] 《枪炮、病菌与钢铁：人类社会的命运》-贾德·戴蒙
    + [ ] 王晓的世界电子地图册

+ 经济学/金融学：
    + Bilibili 小德 MOMO
    + Bilibili 翟东升
    + [ ] 《棉花帝国》
    + 基金或者证券从业资格证
    + [ ] 《金钱心理学》
    + 金融科技：
        + [ ] Max Dama《Max Dama on Trade》：Max Dama 的博客汇总

+ 工商业
    + [ ] 瑞·达利欧的《原则》
    + 软件工程：
        + [ ] 《黑客与画家》
        + [ ] 《复盘网飞》美国的马克 · 伦道夫
    + 电子信息：
        + [ ] 《我在硅谷管芯片：芯片产品线经理生存指南》
    + 产品经理：
        + [ ] 《超级转化率》
        + [ ] 《增长黑客》
    + 创业：
        + [ ] 埃隆马斯克自传
        + [ ] 《精益创业》
        + [ ] 《创业维艰》
        + [ ] 《低成本创业》 樊登
        + [ ] 《重新理解创业》 周航
        + [ ] 得到的《详谈》 系列

+ 广告学：
    + [ ] Bilibili王政东

+ 自然科学：
    + [ ] 瑞安·诺思的 《万物发明指南：时间旅行者的生存手册》
    + [ ] 美国史蒂文·约翰逊的 《我们如何走到今天：重塑时间的六项创新》
    + [ ] 哈福德的《塑造世界经济的五十项伟大发明》
    + [ ] 马克·米奥多的《迷人的材料：10 种改变世界的神奇物质和它们背后的科学故事》
    + [ ] 卡尔·奇默的《病毒星球》

### 个人成长

+ 《做时间的朋友》李笑来
	+ 行为：
		+ 组织中：
		+ 独处中：趋利避害
			+ 弊害：阻碍做出弊害行为的是拖延
				+ 原因：恐惧错误和评价
				+ 认知与方法：
					+ 面对恐惧，要知道完美是不存在的
					+ 面对评价，要过滤它人非建设性负面评价
					+ 要考虑到意外的出现以及计划时间估算的不准确，所以，**面对Deadline，应该从“在ddl之前能不能做完”变成“在ddl之前能做多好做多好“**。
					+ 拖延除了拖延行动的开始，还有逃避行动中困难的部分。
			+ 趋利：阻碍做出趋利行为的是低欲望
	+ 实事求是：
		+ 速成不存在，但是人的基因倾向尽量快的看到结果
		+ 完美不存在，所以要学会接受不完美
		+ 未知永远存在，这也是焦虑的来源，只能尽量克制，否则焦虑会让动作变形
		+ 现状永远不满，同样是人性导致的，需要戒骄戒躁
		+ 资源永远稀缺，**降低欲望**是逃避现实

	+ misc：
		+ 经验主义的局限性与科学方法论
			+ 科学方法论的互通性，比如三段论、面向对象、双盲测试
		+ 法律思维：谁主张谁举证
