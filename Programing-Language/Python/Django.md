学习资料是[Acwing工程课之Django](https://www.acwing.com/activity/content/72/)
+ 学习提示：
	+ y总的工程课以实用为主，对原理性的解释不多，要多总结思考
	+ y总强行用终端开发，是个很好的练习机会，不过VSCode的remoting SSH也挺香。
# misc
+ Django提供一个ipython：`python3 manage.py shell`
# INIT

## 搭建环境

1. 购买云服务器、配置服务器（[linux云服务器配置指南](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/LinuxConfigGuide.md)）、配置堡垒机（AC Terminal和本地）的SSH。
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
		    | -- 与项目同名的子目录 |                |
		    | --------------------- | -------------- |
		    |                       | -- __init__.py |
		    |                       | -- asgi.py     |
		    |                       | -- settings.py |
		    |                       | -- urls.py     |
		    | \`-- wsgi.py          |                |
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
	| -- 与项目同名目录 |                          |                            |
	| ----------------- | ------------------------ | -------------------------- |
	|                   | -- __init__.py           |                            |
	|                   | -- __pycache__           |                            |
	|                   |                          | -- __init__.cpython-38.pyc |
	|                   |                          | -- settings.cpython-38.pyc |
	|                   |                          | -- urls.cpython-38.pyc     |
	|                   | \`-- wsgi.cpython-38.pyc |                            |
	|                   | -- asgi.py               |                            |
	|                   | -- settings.py           |                            |
	|                   | -- urls.py               |                            |
	| \`-- wsgi.py      |                          |                            |
	| -- db.sqlite3     |                          |                            |
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

## 系统架构

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

### 项目系统设计

+ 方法论：将一个大项目分成多个小部件，每个部件同样可以再细分
+ 在Acwing的项目中：
	```
	acapp
	  | ---menu       |
	  | ------------- |
	  | ---playground |
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

# 发布上线

HTTP2协议、域名与nginx
+ 关于HTTP2协议问题：上面的处理我们可以通过`服务器IP地址:端口号`的方式访问，浏览器认为这样的URL是不安全的
	+ 需要申请HTTP2安全协议证书对接URL
+ 关于域名问题：上面的访问当时并不优雅
	+ 需要购买并备案域名
+ nginx的作用：一方面用于对接域名和对应运行的程序，另一方面nginx让我们的web更有利于扩展和负载均衡
Acwing提供学习用HTTP2协议证书、域名以及配套的nginx配置

1. HTTP协议端口是80，HTTPS协议端口是443端口，要开放对应端口
	1. 硬件：服务器开放端口，去官网
	2. 软件：系统开发端口
		```bash
		# 关闭容器所有任务
		docker commit django_server django_lesson:1.1  # 将容器保存成镜像
		# docker images  # 查看生成的镜像

		# 关闭并删除旧的容器
		# docker stop django_server
		# docker rm django_server
		
		# 使用保存的镜像重新创建容器
		docker run -p 20000:22 -p 8000:8000 -p 80:80 -p 443:443 --name django_server --hostname django_server -itd django_lesson:1.1
		# docker ps  # 查看生成的容器
		```

Acwing的[讲义](https://www.acwing.com/file_system/file/content/whole/index/content/3257028/)  

2. 将Acwing提供的nginx配置HTTP2协议证书放到对应位置

3. 启动nginx服务
>+ 会提示OK
>+ 重新加载：
>	```bash
>	sudo nginx -s reload
>	```  
>+ log: `/var/log/ngnix/`

 4. 修改项目（debug和allow_url）和归档
 5. 配置uwsgi
 6. 通过uwsgi启动项目


# 数据库

## Sqlite
>Django自带数据库Sqlite
>Django自带账号系统

Django账号系统的扩充
1. 在`~/app/models`目录下创建表`表名/表名.py`
	```python
	from django.db import models                                                         
	from django.contrib.auth.models import User
	
	class Player(models.Model):
		user = models.OneToOneField(User, on_delete=models.CASCADE)
		photo = models.URLField(max_length=256, blank=True)
	
	def __str__(self):
		return str(self.user)
	```
	+ 一个表对应一个Class  
		一条数据对应一个对象

1. 在`~/game/admin.py`写入：
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
4. 重启项目即可在`url/admin`下查看
## Redis
1. 安装`django_redis`
	```bash
	pip install django_redis
	```
2. 配置`settings.py`：将下面的代码复制到文件末尾
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
	
	cache.keys("*")  # 按关键字查找，支持正则表达式，这样为查找所有关键字
	cache.set(key, value, time)  # time单位是秒，设为None为不过期
	cache.has_key(key)
	cache,get(key)
	cache.delete(key)
	```

# QAuth2第三方授权

1. Client向Web请求使用AcWing账号登录
2. Web向AcWing请求OAuth2授权登录，上报信息（），这个过程使用AcWing的API
	```
	https://www.acwing.com/third_party/api/oauth2/web/authorize/?appid=APPID&redirect_uri=REDIRECT_URI&scope=SCOPE&state=STATE
	```
	
    | 参数         | 是否必须 | 说明                 |
    | ------------ | -------- | -------------------- |
    | appid        | 是       | acapp唯一ID          |
    | redirect_uri | 是       | 接收授权的范围       |
    | scope        | 是       | 申请授权的范围       |
    | state        | 否       | 建议带上作为请求的ID |


QAuth2开始
3. AcWing询问Client是否确认授权
4. Client确认授权
保证Client安全
+ Clinet确认后，AcWing对第二步的询问给出返回
	```
	redirect_uri?code=CODE&state=STATE  # code为授权码，state同上
	```
5. AcWing将授权码发送到Web
6. Web向AcWing再次报送一些信息（之前的必要信息和独属于Web的密钥）
	```
	https://www.acwing.com/third_party/api/oauth2/access_token/?appid=APPID&secret=APPSECRET&code=CODE
	```
	appid和code即为之前的信息，secret即为acapp应用密钥
7. AcWing向Web返回“令牌”
保护Web安全
+ 具体的：
	+ 申请成功示例：
		```
		{
			"access_token": "ACCESS_TOKEN", 
			 "expires_in": 7200, 
			 "refresh_token": "REFRESH_TOKEN",
			  "openid": "OPENID", 
			  "scope": "SCOPE",
		}
		```
	+ 申请失败示例：
		```
		{
			 "errcode": 40001,
			 "errmsg": "code expired",  # 授权码过期
		}
		```

	| 参数          | 说明                                                                       |
	| ------------- | -------------------------------------------------------------------------- |
	| access_token  | 授权令牌，有效期2小时                                                      |
	| expires_in    | 授权令牌还有多久过期，单位（秒）                                           |
	| refresh_token | 用于刷新access_token的令牌，有效期30天                                     |
	| openid        | 用户的id。每个AcWing用户在每个acapp中授权的openid是唯一的,可用于识别用户。 |
	| scope         | 用户授权的范围。目前范围为userinfo，包括用户名、头像                       |


1. 用户在网站点击第三方授权登录
2. 网站向对应第三方上报`Appid`（由第三方规定，携带对应信息），通过OAuth2获得`code`授权码
   + AcWing的API：
     ```
     AcWingOS.api.oauth2.authorize(appid, redirect_uri, scope, state, callback);
     ```

     | 参数         | 是否必须 | 说明                                                                                                                                                                                                                                                |
     | ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | appid        | 是       | 应用的唯一id，可以在AcWing编辑AcApp的界面里看到                                                                                                                                                                                                     |
     | redirect_uri | 是       | 接收授权码的地址。需要用urllib.parse.quote对链接进行处理                                                                                                                                                                                            |
     | scope        | 是       | 申请授权的范围。目前只需填userinfo                                                                                                                                                                                                                  |
     | state        | 是       | 用于判断请求和回调的一致性，授权成功后后原样返回。该参数可用于防止csrf攻击（跨站请求伪造攻击），建议第三方带上该参数，可设置为简单的随机数（如果是将第三方授权登录绑定到现有账号上，那么推荐用随机数 + user_id作为state的值，可以有效防止CSRF攻击） |
     | callback     | 是       | redirect_uri返回后的回调函数                                                                                                                                                                                                                        |

     + 返回：
       + 用户同意授权后，会将code和state传递给redirect_uri。
       + 如果用户拒绝授权，则将会收到如下错误码：
         {
             errcode: "40010"
             errmsg: "user reject"
         }
至此达成Client和Web都安全的局面  
Web可以利用令牌获得在权限内的信息，同时有两个令牌，一个用来获得信息，时效短；另一个用来刷新令牌，失效长  
这里无论是获得信息还是刷新令牌都有对应的API

# 联机

## 画面同步
