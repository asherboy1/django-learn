# python环境配置

Python 虚拟化环境--目的 达到环境隔离

不同环境所用到的包、库不一致 隔离后能更加容易配置，并且对于不同的数据库表 管理更容易



cmd：python -m venv myvenv     (myvenv为虚拟环境名称)

在当前路径下生成一个python虚拟环境  全新环境



**启动虚拟环境**

macOs:

source myvenv/bin/activate 

Windows:

start myvenv\Scripts\activate.bat

vscode:

powershell 中 .\Activate.ps1 然后选择编译器



# Django 命令

django-admin 作为启动程序 

**创建django项目**

django-admin startproject first_project  



将虚拟环境移动至项目内

mv myvenv\ .\first_project



**创建app**

django-admin startapp first_app

记住 需要在setting中进行关联



python manage.py runserver 启动服务





## project目录关注

- settings 全局配置文件 数据库、模板等

- urls 会到该urls中 寻找链接  路由层  总的urls 可以将app得路径与总的路径进行拼接跳转
- asgi 接收网络请求
- wsgi 接收网络请求



## app目录关注

* apps 

* models 对数据库进行操作 ORM

* views  视图函数
* migrations 用于做数据库操作记录 数据库变更记录
* admin 后台管理功能



设计逻辑：app可”插拔“   应用

每个app设计为单独设计，相互之前隔离-最好

多app设置路由跳转

一级url最好设计为不直接关联view层，最好设计为去做跳转，本层进绑定该层的路由



第三方库-网上找、 venv\Lib\site-packages\django\contrib

channel库 协程



可以关注Flask FastApi 的学习



# Django设计模式

MTV+urls

| MVT       |                           |
| --------- | ------------------------- |
| Models    | 模型-数据库管理员(非必须) |
| Templates | 模板-模板引擎渲染(非必须) |
| Views     | 视图-接口引擎(必须)       |



### Models--定义数据库语句 执行；django 开放的功能 Orm设计 一切对象化

注：

ORM 是个啥？

在python中的一个默认的编写规范是一切皆对象，这样做使得代码简洁，结构清晰，便于维护和重用代码，同时极大的提升开发效率。

同样在操作数据库时，一般我们用[SQL语句](https://so.csdn.net/so/search?q=SQL语句&spm=1001.2101.3001.7020)来实现操作，但是放在Python中是一串冗长的字符串，不利于调试和修改，更不符合上面提到的规范。

所以，有大佬就提出ORM来替代原生的SQL语句，说白了**ORM** 就是要给缩写，代表着 **对象-关系-映射**  重点！

| 简写 | 全称       | 中文 |
| ---- | ---------- | ---- |
| O    | Object     | 对象 |
| R    | Relational | 关系 |
| M    | Mapping    | 映射 |

https://blog.csdn.net/u011262253/article/details/107605500

1.类：对应数据库表 

2.字段：对应数据库里的字段  

3.方法：对应数据库里的操作

对数据库表进行操作  ，如果仅为显示  可以不使用该模块



## Templates--模板印象 接受http请求，返回资源

render默认会到app目录templates去寻找html文件 （底层：根据注册顺序 在所有app中去寻找html文件）

返回的资源转换为html，资源转换器

如果前后端分离，前端进行处理，那么后端仅仅传输数据即可，不用考虑前端设计

所以模块为非必要



静态文件：

- 图片
- css
- js

统一放在app中static 自建

分别创建目录

引入静态文件 load static

在setting中 STATIC_URL = "/static/"



## Views--一个接口对应一个视图、一种响应、响应请求



整体流程：**请求**--->**urls**（path）对应地址进行匹配--->**views**-->接口处理、业务逻辑--->models（如果需要对数据库进行操作）--->数据库--->**views**--->templates---**>respones**（字节码bytes）--->**浏览器**

注：加粗代表比经过项



HttpResponse 返回字节码 此项返回内容形式很多text json html 

如果返回内容就为html，那么直接显示；也可以返回内容 由前端进行处理

前端渲染与后端渲染区别





# 实操

+ request--->urls(path)
+ response--->views(HttpResponse,TemplateResponse)



**urls中path**

```python
urlpatterns = [ 
    # 其中admin/全路径为 127.0.0.1:8000/admin/
    **path**('admin/', **admin**.site.urls),
    #
]
```

**settings**

选在settings中注册app

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'first_app.apps.FirstAppConfig'  #注册app
]
```



路由跳转：

from **django**.**urls** import **path**, **include**

在app目录中新建urls，结构与project层一致

相当于发送请求 通过主urls跳转至app-urls路由跳转

```python
from first_app import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path("first_app/", include(urls), name="zanding"), #include导入
]
```

注意里面的name为命名空间 在某些情况下（html 指引链接等..暂未全面了解）可以区分



**url**跳转的坑

1.redirect方法：要么整体跳转，要么在原有request上进行拼接

2.在html form 标签属性中 action字段以拼接方式 进行动作跳转(以拼接发送请求)



进阶：

在path中设置 RoutePattern  

如：path('test/《int:num》/', views, name="aa")

当test请求地址后面为数字也会自动跳转至该对应的view



常见的请求/响应

![image-20230226165726657](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230226165726657.png)





## ORM

models.xxx.all() --> 翻译 select * from xxx

- 创建、修改、删除数据库中表。【无法创建数据库！】
- 操作表中的数据。



流程：

### 1.创建数据库

### 2.连接数据库

在setting文件中，配置修改  不使用sqlite

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

### 3.关联models

![](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230226193859083.png)

python manage.py makemigrations  #

python manage.py migrate

执行命令时，会检索所有注册的app里的models 自动建表



如果需要在原有基础上增加字段

可以在增加的对应字段上加入default 或者 置为null

```python
 size = models.IntegerField(null=True, blank=True) *# 可为空 添加在已有的表中不会报错*
 size2 = models.CharField(default="默认")
```



注意 需将models中的models 导入

操作表中数据

- 增  

- ```
  models.object.create(title="aa") 等同 models.object.create(title).value("aa")
  ```

  

- 删

- ```
  models.object.filter().delete()  models.object.all().delete()    filter加入条件
  ```

  

- 改

- ```
  models.object.filter().update() 某些进行更改
  ```

  

- 查

- ```
  models.object.filter()  models.object.all()  返回queryset类型 列表 对象；[obj1, obj2]  单个 直接返回对象
  可利用循环 取出值
  for obj in data:
       print(obj.name, obj.password, obj.size)
  
  models.object.all().first() 第一条数据
  ```

  