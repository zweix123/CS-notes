学习资料是[Acwing工程课之Django](https://www.acwing.com/activity/content/72/)
+ 学习提示：
	+ y总的工程课以实用为主，对原理性的解释不多，要多总结思考
	+ y总强行用终端开发，是个很好的练习机会，不过VSCode的remoting SSH也挺香。

# misc

+ Django提供一个ipython：`python3 manage.py shell`

# INIT

## 搭建环境

1. 购买云服务器、配置服务器（[linux云服务器配置指南](https://github.com/zweix123/blog/blob/master/Linux%E6%9C%BA%E5%99%A8%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97.md)）、配置堡垒机（AC Terminal和本地）的SSH。
2. 在服务器上安装docker（[教程](https://yeasy.gitbook.io/docker_practice/install/ubuntu)）。
3. 将Acwing的Django课程Docker镜像scp到云服务器上：
	```bash
	scp /var/lib/acwing/docker/images/django_lesson_1_0.tar 云服务器别名:~/
	```
4. 将镜像导出：
	```bash
	docker load -i django_lesson_1_0.tar 
	```
5. 利用镜像生成容器（并运行）：
	```bash
	docker run -p 20000:22 -p 8000:8000 --name django_server --hostname django_server -itd django_lesson:1.0  # 这里的命令和课程内不同的(我指定了hosttname)
	```
	+ 20000端口用于ssh登录
	+ 8000端口用于调试  

	去服务器官网开启对应端口
6. 进入容器：
	```bash
	docker attach django_server
	```
	配置这个Linux（像配置云服务那样）

	+ 挂起容器：`(Ctrl + p) -> (Ctrl + q)`

## 创建项目

1. 创建项目：
	```bash
	django-admin startproject moba
	```
	+ 初始文件结构：
		```
		.
		\`-- 项目根目录
		    |-- 与项目同名的子目录
		    |   |-- __init__.py
		    |   |-- asgi.py
		    |   |-- settings.py
		    |   |-- urls.py
		    |   \`-- wsgi.py
		    \`-- manage.py
		```

2. 配置Git并上云

## 初步配置

+ 打开`项目根目录/和项目同名的目录/settings`
	```python
	import os  # 下面要用到
	...
	# 修改
	ALLOWED_HOSTS = ['服务器IPv4地址']  # 项目允许访问的URL, `'*'`表示通配
	...
	# 修改
	TIME_ZONE = 'Asia/Shanghai'  # 修改时区
	...
	# 修改和添加静态资源路径和位置
	STATIC_URL = '/static/'  # 文件本来就有: 使用的URL
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # 添加: 上面的URL对应的路径
	MEDIR_URL = '/media/'  # 添加: 原理同上
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 添加
	# 这样可以通过`url/static/...`访问项目静态资源, 结合下面项目文件结构可以猜测Django是统一整个项目的静态资源
	# 初步测试, 在app下的static可以找到, 但是在任意位置的static就不可以
	```
+ 同步数据：
	```bash
	python3 manage.py migrate
		```

## 运行体验

```bash
python3 manage.py runserver 0.0.0.0:8000
```

通过网址`服务器IPv4地址:8000`即可访问

+ 运行后文件结构`tree`：
	```
	|-- 与项目同名目录
	|   |-- __init__.py
	|   |-- __pycache__
	|   |   |-- __init__.cpython-38.pyc
	|   |   |-- settings.cpython-38.pyc
	|   |   |-- urls.cpython-38.pyc
	|   |   \`-- wsgi.cpython-38.pyc
	|   |-- asgi.py
	|   |-- settings.py
	|   |-- urls.py
	|   \`-- wsgi.py
	|-- db.sqlite3
	\`-- manage.py
	```


## 创建admin

```bash
python3 manage.py createsuperuser
# 输入管理员用户名
# 输入管理员邮箱，回车跳过
# 输入管理员密码
# 重复密码
```
通过网址`服务器IPv4地址:8000/admin`即可登录查看


## 创建app
习惯上通常不直接在`和项目同名`的子目录下开发，而是再创建一个`app`。

1. 创建app：
	```bash
	python3 manage.py startapp app名称
	```
	+ 位置：`项目根目录/app名目录/`下

2. 配置：打开`项目根目录/项目同名子目录/setting.py`
	```python
	...
	INSTALLED_APPS = [
		[app名].apps.[App名]Config  # 是一个函数在`app子目录/apps.py`中
		...
	]
	...
	```

下面是一个简单的例子
```python
# vim ./game/views.py  # 已有
# 键入
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world!")

#---

# vim ./game/urls.py  # 没有
# 键入
from django.urls import path
from game.views import index

urlpatterns = [
	path("", index, name="index"), 
]

#---

# cd ./moba/urls.py
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

## 文件系统

### 项目系统设计

+ 方法论：将一个大项目分成多个小部件，每个部件同样可以再细分
+ 在Acwing的项目中：
	```
	acapp
	  |---menu
	  |---playground
	  \`--settings
	```


### 项目文件结构

+ 项目文件结构：Djang框架文件结构：  
	
	下面的管理方式将默认的单文件换成目录管理，而Python的文件互通是通过`import`，所以每个管理python代码的目录下都应该有名为的`__init__.py`的文件
	
	+ `templates`目录：管理HTML
	+ `urls`目录：替换`urls.py`文件，管理URL
	+ `consumers`目录：管理HTTP
	+ `views`目录：替换`views.py`文件，管理函数
	+ `models`目录：替换`models.py`文件，管理数据库
	+ `static`目录：管理静态文件（CSS、JS）
		+ `image`目录：存储图片
		+ `audio`目录：存储音频
		+ `css`目录：存储CSS文件
		+ `js`目录：存储JavaScript文件
			+ `src`目录：分部件管理
			+ `dist`目录：将各部件js源码拼接放在该目录下

			 说明见下

### Sum

+ 系统架构和文件结构的关系：在不再拆分app的情况下，在每个项目文件结构的”终端“，都有一个系统架构的目录树
	+ 图片音频类资源：如上
	+ CSS类资源：一个大部件基本就一个，比如只有一个`menu.css`
	+ JavaScript类资源：
		>如果Js资源同样细分成小文件，在引用时由于并行读取太多文件会太慢
		
		所以src目录中仍然如上，所以将每个部件的Js文件拼接成一个文件到dist中
		+ 脚本如下：

			```bash
			#! /bin/bash
			
			JS_PATH=拼接Js文件的根目录
			JS_PATH_DIST=${JS_PATH}dist/
			JS_PATH_SRC=${JS_PATH}src/
			
			find $JS_PATH_SRC -type f -name '*.js' | sort | xargs cat > ${JS_PATH_DIST}game.js
			```
	+ template资源：如上
		>本项目还支持多终端，故还多一个目录`multiends`

---

## 上线
>处理到上面的步骤，对运行的项目，我们可以通过`IP地址:端口号`的方式访问，但是浏览器会认为这样的url是不安全的

1. 将URL对接安全协议（https协议）
	>需要申请https协议证书
2. 将域名和证书挂钩
	>域名需要备案

---



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

```
      
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


# Doc



## 数据库

### Sqlite

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

### Redis

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


1. 用户在网站点击第三方授权登录

2. 网站向对应第三方上报`Appid`（由第三方规定，携带对应信息），通过OAuth2获得`code`授权码

   + AcWing的API：

     ```
     AcWingOS.api.oauth2.authorize(appid, redirect_uri, scope, state, callback);
     ```


     | 参数           | 是否必须 | 说明                                                         |
     | ------------ | -------- | ------------------------------------------------------------ |
     | appid          | 是       | 应用的唯一id，可以在AcWing编辑AcApp的界面里看到              |
     | redirect_uri | 是       | 接收授权码的地址。需要用urllib.parse.quote对链接进行处理     |
     | scope          | 是       | 申请授权的范围。目前只需填userinfo                           |
     | state           | 是       | 用于判断请求和回调的一致性，授权成功后后原样返回。该参数可用于防止csrf攻击（跨站请求伪造攻击），建议第三方带上该参数，可设置为简单的随机数（如果是将第三方授权登录绑定到现有账号上，那么推荐用随机数 + user_id作为state的值，可以有效防止CSRF攻击）  |
     | callback      | 是       | redirect_uri返回后的回调函数                                 |

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
