# Init

+ 图片下载：

  ```bash
  wget --output-document=自定义图片名称 图片地址
  ```

+ Django的ipython：`pyhton3 manage.py shell`

## 配置docker环境

0. 1. 购买云服务器
   2. 创建用户并分配`sudo`权限
   3. 为用户配置别名和免密登录
   4. `scp`祖传配置
   5. 安装`docker`

1. 将Acwing的docker镜像传到云服务器上：

   ```bash
   cd /var/lib/acwing/docker/images/
   scp django_lesson_1_0.tar 云服务器别名:
   ```

ssh到云服务器上

2. 将镜像导出：

   ```bash
   docker load -i django_lesson_1_0.tar``
   ```

3. 利用镜像生成容器：

   ```bash
   docker run -p 20000:22 -p 8000:8000 --name django_server -itd django_lesson:1.0
   ```

   + 两万端口用于ssh登录
   + 八千端口用于调试

   > 对应端口的开放需要到云服务官网上打开

4. 进入容器：

   ```bash
   docker attack django_server
   ```

5. 像配置云服务器一样配置容器：

   1. 添加用户，配置sudo
   
   2. 为该用户在本地配置别名和免密登录
   
   3. 传入祖传配置
   
      > 在每次进入tmux时会有关于sudo的提示，在tmux外利用sudu执行任意命令即可之后不再提示

## 创建项目

1. 创建项目：

   ```bash
   django-admin startproject 项目名称
   ```

   + `和项目同名的目录`
     + `和项目同名的目录`
       + `__init__.py`
       + `asgi.py`
       + `settings.py`
       + `urls.py`
       + `wsgi.py`
     + `manage.py`

## 配置git环境

0. 将该镜像和代码托管平台建立连接
   1. 生成密钥：`ssh-keygen`
   2. 将公钥配置到平台上

进入项目目录

1. 初始化`git init`

   ```bash
   git add .
   git commit -m "start project"
   ```

2. 在代码托管平台创建项目

   + 项目名称尽量一样
   + 不使用`Initialize repository with a README`

   创建后平台进入一个引导界面

   1. 输入`Git global setup`的命令

   2. 输入`Push an existing Git repository`的命令

      1. `git remote add origin git@git.acwing.com:zweix/acapp.git`

      2. `git push`

         按照报错提示输入命令

   ```bash
   git push
   ```

+ ```bash
  vim readme.md
  # 输入 A great epic masterpiece !!!
  # git add . \ git commit -m "add readme" \ git push三件套
  ```

+ 后续会有预编译的文件和开发过程中的`swp`文件，我们不希望将其维护在云端

  ```bash
  # 在仓库根目录下
  vim .gitignore
  
  # 写入
  */__pycache__  # 后续发现各个子目录下仍有，将此改为 **/__pycache__
  *.swp
  ```

## 项目初步配置

1. 运行项目：

   ```bash
   python3 manage.py runserver 0.0.0.0:8000
   ```

2. 查看项目：

   ```bash
   # 浏览器网址输入
   云服务器平台分配的IP地址:8000
   ```

此时弹出的网页报错，查看提示：将本地IP地址加入源代码中的`ALLOWED_HOSTS`列表中

+ `tree`后发现变化：
  + `项目根目录/项目同名目录/__pycache__/`：预编译的文件
  + `项目根目录/db.sqlite3`：数据库文件

```bash
ag ALLOWED_HOSTS # 查找列表在源代码位置
```

以字符串的形式将本地IP地址加入在列表中

3. 同步数据库：在退出项目后

   ```bash
   python3 manage.py migrate
   ```

4. 创建`admin`用户：

   ```bash
   python3 manage.py createsuperuser
   # 输入管理员用户名
   # 输入管理员邮箱 # 直接回车跳过设置
   # 输入密码
   # 重复密码
   ```

   + 即可在`项目地址/admin`进入

5. 创建app：

   ```bash
   python3 manage.py startapp app名称
   ```

   + `/项目根目录下/game`

+ 配置：

  ```bash
  vim ./acapp/setting.py
  ```

  + 时区

    ```python
    TIME_ZONE = 'Asia/Shanghai'
    ```

  + 将game app添加到配置文件：

    ```python
    # 找到INSTALLED_APPS列表
    # 将字符串‘game.apps.GameConfig’放在其首
    ```

  + 静态文件：

    ```python
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 这里两个文件目前还没有创建
    MEDIR_URL = '/media/'
    ```

+ Hello world

  1. ```python
     # vim ./game/views/py  # 已有
     # 键入
     from django.shortcuts import render
     from django.http import HttpResponse
     
     def index(request):
         return HttpResponse("Hello world!")
     ```

  2. ```python
     # vim ./game/urls.py  # 没有，需创建
     # 键入
     from django.urls import path
     from game.views import index
     
     urlpatterns = [
     	path("", index, name="index"), 
     ]
     ```

  3. ```python
     # cd ./acapp/urls.py
     # 键入
     from django.contrib import admin
     from django.urls import path, include
     
     urlpatterns = [
         path('game/', include('game.urls')), 
         # 此时"IP地址:端口号"为一个不可访问地址
         # 但是"IP地址:端口号/game"即为game app的主页面
         # 如果第一个参数字符串为空，则网址直接为game的主页面
         path('admin/', admin.site.urls),
     ]
     ```

# 项目文件结构

+ 分而治之：将一个项目分成各个更容易实现的小部分
  + `acapp`：
    + `menu`
    + `playground`
    + `settings`

+ Django文件结构：

  + `templates`目录：管理`.html`文件，负责前端展示，按终端管理

  + `urls`目录：管理`.py`文件，负责链接和函数的对应关系、即网址的去处，按部件管理

  + `views`目录：管理`.py`文件，负责`http`函数、即短链接，按部件管理

  + `comsumers`目录：管理`.py`文件，负责`websocket`函数、即长链接，按部件管理

  + `models`目录：管理`.py`文件，负责数据库

  + `static`目录：存储静态文件，按部件管理

    + `image`：存储图片文件

    + `audio`：存储音频文件

    + `css`：存储`.css`文件，负责格式，通常整个项目只有一个，由`.html`文件引入
    
  + `js`：存储`,js`文件，负责逻辑，通常要承担更多责任，由`.html`文件引入
    
      + `src`：分部件管理，为各个部件的`.js`源码
      + `dist`：为方便管理，将源码连在一起放在同一个文件在此管理
      
      > 合并用脚本
      >
      > ```bash
      > #! /bin/bash
      > 
      > JS_PATH=/home/acs/acapp/game/static/js/
      > JS_PATH_DIST=${JS_PATH}dist/
      > JS_PATH_SRC=${JS_PATH}src/
      > 
      > find $JS_PATH_SRC -type f -name '*.js' | sort | xargs cat > ${JS_PATH_DIST}game.js
    > ```

> 对于上面的`.py`的文件夹，Django之间的文件互通是通过`import`，所以这些目录下需要有`__init__.py`文件

+ 项目运转流程：

  浏览器只是想要一个html文件来渲染一下

  1. 找到对应函数：浏览器通过地址递归询问各层"`urls`"：在`和项目同名`目录的`urls.py`$\rightarrow$各个app下的`urls`目录$\rightarrow$各个部件的"`urls`"：这个跳转方式是指向对应的文件地址，能指向下一层"`urls`"，也能指向要执行的函数
  2. 运行函数：函数通常按部件管理在`views`目录中，"`urls`"直接指向对应的函数名
  3. 函数返回`.html`：函数返回一个`.html`供浏览器渲染，一个静态的页面

  ---

  4. `.html`引入`.css`文件和`.js`文件

     > html给的是一个静态的页面，通常不能满足需求，而js里也可执行html语句，所以通常的模式是主体在`.js`文件中

     + `.js`：js可以实现复杂的逻辑，比如生成一些html代码，以及一些交互方面的设计，通常是面向对象
     + `.css`：css可以以特定的语法，针对js中的类，**使其变得更好看**，同时也能在特定的位置引入静态文件

## url

+ `和项目同名`目录下的`urls.py`

  ```python
  from django.urls import path, include
  
  urlpatterns = [
  		path('', include('game.urls.index')), # 末尾的,是需要的
  		]
  ```

  核心在于`path`函数的两个参数

  1. 代表解析到当前的下一”位“的文件层次名称，这里为空表示这一位为空，而只是起始的点，之前的部分是网址，相当于网址就是
  2. `include`函数里的字符串是文件引用格式，是从项目根目录开始的`game/urls/index`，这里的`index`是一个`/py`文件

+ app下的`urls`目录下的`index.py`

  ```python
  from django.urls import path, include
  from game.views.index import index
  
  urlpatterns = [
  	    path("", index, name="index"),
     		path("menu/", include("game.urls.menu.index")),
      	path("playground/", include("game.urls.playground.index")),
      	path("settings/", include("game.urls.settings.index")),
  		]
  ```

  + 这里展示了`path`函数的另一个用法：

    + `import`的格式也是文件结构下的对应函数名

    1. 第一个参数同上，即如果只有解析到此前的部分（地址本身）则是这里
    2. 第二第三个参数则是调用了`index`这个函数

    + 之后的`path`则是该app下各个组件的地址，格式和方式同上

+ 组件内的`index.py`不再展示

## view

+ app内的`views`目录下的`index.py`文件：

  ```python
  from django.shortcuts import render
  
  def index(request):
      return render(request, "multiends/web.html")
  ```

  要求返回一个`.html`文件

  ==怎么感觉文件路径缺了呢==

## html js css

+ html做基本框架
+ js和css相互呼应
  + css唯一，即js类为线索
  + js多

# 上线

> 目前项目只能通过`IP地址:端口号`的方式访问，且浏览器认为该`url`是不安全的

+ 将链接对接安全协议/https协议
+ 需要申请https协议证书
+ 证书和域名挂钩
+ 域名需要备案

---

+ https协议对应443端口、http协议对应80端口

1. 开放端口：

   1. 登录容器，关闭所有运行中的任务

   2. 登录运行容器的服务器，然后执行

      ```bash
      docker commit CONTAINER_NAME django_lesson:1.1  # 将容器保存成镜像，将CONTAINER_NAME替换成容器名称
      docker stop CONTAINER_NAME  # 关闭容器
      docker rm CONTAINER_NAME # 删除容器
      
      # 使用保存的镜像重新创建容器
      docker run -p 20000:22 -p 8000:8000 -p 80:80 -p 443:443 --name CONTAINER_NAME -itd django_lesson:1.1
      ```

   3. 去云平台打开80和443端口

2. 配置nginx

   + 配置文件`/etc/nginx/nginx.conf`

   + 配置文件`/etc/nginx/cert/acapp.key`

   + 配置文件`/etc/nginx/cert/acapp.pem`

   > 要使用`sudo`，根目录可能没有祖传配置，注意不要传bash部分

   + 启动nginx服务：

     ```bash
     sudo /etc/init.d/nginx start
     ```

     > 如果没有提示OK
     >
     > + 重新加载nginx配置：
     >
     >   ```bash
     >   sudo nginx -s reload
     >   ```
     >
     >   之后会有报错提示
     >
     > + 文件`/var/log/ngnix/error.log`会有报错信息

3. 修改django配置：

   1. 将域名（`https://`后面的部分）放在`settings.py`的`ALLOWED_HOSTS`列表中

   2. 令`srttings.py`中的`DEBUG = False`

   3. 归档`static`文件：

      ```bash
      python3 manage.py collectstatic
      ```

4. 配置`uwsgi`：是nginx和django的桥梁

   1. 在django项目添加配置文件：`scripts/uwsgi.ini`

      ```ini
      [uwsgi]
      socket          = 127.0.0.1:8000
      chdir           = /home/acs/acapp
      wsgi-file       = acapp/wsgi.py
      master          = true
      processes       = 2
      threads         = 5
      vacuum          = true
      ```

   2. 启动uwsgi服务：

      ```bash
      uwsgi --ini scripts/uwsgi.ini
      ```

5. 配置acapp：

# 数据库

> Django自带的数据库Sqlite

+ Django有自带的账号系统`Users`，但是不能满足头像这种需求，需要扩充（`app/model/`）

+ 如何扩充

  1. 在`~/app/models`目录下创建表`表名目录/表名.py`

     ```python
     from django.db import models                                                         
     from django.contrib.auth.models import User
     
     
     class Player(models.Model):
         user = models.OneToOneField(User, on_delete=models.CASCADE)
         photo = models.URLField(max_length=256, blank=True)
     
         def __str__(self):
             return str(self.user)
     ```

  2. 在`~/game/admin.py`写入：

     ```python
     from django.contrib import admin                                                     
     from game.models.player.player import Player
     
     # Register your models here.
     
     admin.site.register(Player)
     ```

  3. 运行命令：更新数据库

     ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     ```

  4. 重启项目

     在`IP/admin`下即有，可图形化操作

+ 一个表对应一个Class

  每条数据对应一个对象

## Redis

+ 特点：
  + 内存的，快
  + 存储方式是`key-value`对
  + 单线程

1. 安装`django_redis`

   ```bash
   pip install django_redis
   ```

2. 配置`settings.py`：将下列代码复制到末尾

   ```python
   CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
   }
   USER_AGENTS_CACHE = 'default'
   ```

3. 启动`redis-server`：

   ```bash
   sudo redis-server /etc/redis/redis.conf
   ```

+ 常用用法：

  ```python
  from django.core.cache import cache
  
  cache.keys("*")  # 查找关键字 # 支持正则表达式
  cache.set("key名", 值, 存在时间（单位是秒）设置过 None 就是不过期)
  
  cache.has_key("key")
  
  
  cache,get("key")  //获得值
  cache.delete("key") 删掉
  ```

## QAuth2第三方授权

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/Python/1_1ddf070e4d-weboauth2.png)

1. 用户在网站点击第三方授权登录

2. 网站向对应第三方上报`Appid`（由第三方规定，携带对应信息），通过OAuth2获得`code`授权码

   + AcWing的API：

     ```
     AcWingOS.api.oauth2.authorize(appid, redirect_uri, scope, state, callback);
     ```

     | 参数         | 是否必须 | 说明                                                         |
     | ------------ | -------- | ------------------------------------------------------------ |
     | appid        | 是       | 应用的唯一id，可以在AcWing编辑AcApp的界面里看到              |
     | redirect_uri | 是       | 接收授权码的地址。需要用urllib.parse.quote对链接进行处理     |
     | scope        | 是       | 申请授权的范围。目前只需填userinfo                           |
     | state        | 是       | 用于判断请求和回调的一致性，授权成功后后原样返回。该参数可用于防止csrf攻击（跨站请求伪造攻击），建议第三方带上该参数，可设置为简单的随机数（如果是将第三方授权登录绑定到现有账号上，那么推荐用随机数 + user_id作为state的值，可以有效防止CSRF攻击） |
     | callback     | 是       | redirect_uri返回后的回调函数                                 |

     + 返回：

       + 用户同意授权后，会将code和state传递给redirect_uri。

       + 如果用户拒绝授权，则将会收到如下错误码：

         {
             errcode: "40010"
             errmsg: "user reject"
         }

3. 第三方向用户返回页面，询问是否授权：规定时间内同意

4. 用户同意授权

5. 第三方给网站一个`code`授权码说明同一授权

6. 网站将`code`授权码、`Appid`、`Appsecret`（和第三方规定的密钥）发送给第三方申请授权

7. 第三方返回`access_token`授权令牌和`openid`（第三方识别网站的ID）

8. 网站通过授权令牌和`openid`申请一些第三方像公开的信息

9. 第三方返回对应信息
