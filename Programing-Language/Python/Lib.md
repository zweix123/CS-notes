```python
help(模块名)
```

# 标准库

## sys

```python
'''
一个与python解释器进行交互的module
'''
import sys

#参数列表
args = sys.argv

args[0] -> 程序名（包含绝对路径）

else -> 参数
```

## os

```python
'''
一个与操作系统交互的module
'''
import os

#通过python运行cmd
os.system('cmd指令')
#此方法会阻塞当前程序运行
#以此解决
os.system('start cmd指令')

#判断文件存在否
os.path.exists('文件名') #绝对路径和相对路径都可以

#获得程序当前路径
os.getcwd()
os.path.abspath(os.curdir)  # os.curdir返回'.'
# 同理可获得父目录路径 os.path.abspath('..')

#组合路径
os.path.join('D:\\', 'Users', '郑尉欣', 'Desktop')

### 分隔符

#遍历目录
os.work('目录') #返回三元组，目录路径，目录下的目录，目录下的文件

#获得目录下所有的文件和文件夹
os.listdir('目录') #返回这个目录下所有目录和文件的名字（文件类）

# 结合os.path.isdir()来dfs可有后者实现前者

#os.path.splitext
```

### json

> json(JavaScript Object Notation)格式：文件以`.json`结尾

+ 将数据结构转存到文件中，然后运输该文件，其他程序在加载该文件来使用数据

+ 函数`dump(数据, json文件)`：将数据加载到文件中
+ 函数`load(json文件)`：返回。。。：将json加载出来

### unittest

+ 单元测试：用于核实函数的某个方面没有问题

  测试用例：一组单元测试 -> 符合核实函数的符合要求

  全覆盖式测试样例包含一整套单元测试，涵盖各种可能的函数使用方式

+ 测试流程：导入模块unittest和要测试的函数，创建一个继承`unittest.TestCase`的类，并编写一系列方法的函数行为的不同方面进行测试。

  ```python
  import unittest
  
  class MyTestCase(unittest.TestCase):
      def test_oabaoaba(self):  #所有test_打头的方法都自动进行
          ...
  
  unittest.main()
  ```

+ 断言方法：

  | 方法                      | 用途                   |
  | ------------------------- | ---------------------- |
  | `assertEqual(a, b)`       | 核实`a == b`           |
  | `assertnotEqual(a, b)`    | 核实`a != b`           |
  | `assertTrue(x)`           | 核实`x`为`True`        |
  | `assertFalse(x)`          | 核实`x`为`False`       |
  | `assertIn(item, list)`    | 核实`item`在`list`中   |
  | `assertNotIn(item, list)` | 核实`item`不在`list`中 |

+ 测试类：

  + 方法：`setUp(self)`：测试程序先进行该方法，在运行其他test_开头方法：在此创建对象和答案列表


# 图形化

## Pygame

+ surface：在Pygame种是屏幕的一部分，用于显示游戏元素

+ 事件：用户执行的操作：按键和移动鼠标

+ 颜色：以RGB值指定：颜色由红色、绿色和蓝色值组成，每个值可取范围是0 ~ 255；

  ​            255, 0, 0是red、0, 255, 0是green、0, 0, 255是blue。

+ 设计：

  + 设置类：将需要设置的常量放在一个类中，然后主函数调用里面的类

    ```python
    class Setting():
        def __init__(self):
            self.screen_width = 1200
            self.screen_height = 800
            self.bg_color = (230, 230, 230)
    ```

    ```python
    from settings import Settings
    
    oabaoab_settings = Settings()
    ```

---

+ 框架：整个游戏又一个while控制，里面的一个for监控事件

  ```python
  while True:
      
  ```

+ 主类`pygame`：

  ```python
  pygame.init() #初始化pygame
  ```

+ 窗口类：`display`

  ```python
  screen = pygame.display.set_mode((长, 宽)) #传递信息元组，创造并返回一个窗口类
  pygame.display.set_caption("oabaoaba") #改变窗口标题
  
  pygame.display.flip() #刷新屏幕
  
  screen.fill((RGB元组)) #填充颜色
  ```

+ 事件类：`event`

  ```python
  for event in pygame.event.get(): #侦听事件 get()可检测所有键盘和鼠标的事件 在for中用一系列if来响应
      ...
      # 每次响应用flip()刷新屏幕
      if event.type == pygame.什么
  ```

  + 键盘
  + 鼠标：
    + `QUIT`：退出
    + `KEYDOWN`：点击：进一步比对`event.key == ...`
      + `K_RIGHT`：右键点击

+ 图片类：`image`

  ```python
  image = pygame.image.load('图片路径') # 获取图片，返回的也是一种surface
  ```

  + 图片属性类：rect：通过`get_rect()`获取：
    + 属性值：`centerx`：类成员
    + 属性值：`bottom：类成员`

# MISC

## 图像识别pytesseract

```python
import os
import sys

file = sys.argv[1]

if not os.path.exists(file):
    print(file + " is not exists")
    quit()

op = ''
if len(sys.argv) == 3:
    op = sys.argv[2]


from PIL import Image
import pytesseract


image = Image.open(file)

if op == 'chi_sim':
    res = pytesseract.image_to_string(image, lang='chi_sim')
else :
    res = pytesseract.image_to_string(image)

print(res)
```