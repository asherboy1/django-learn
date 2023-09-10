# 用户管理项目

## 1.欢迎页面

**django默认加载配置**

需在setting中进行配置

![image-20230304105150302](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230304105150302.png)

![image-20230304105205351](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230304105205351.png)



在该app层级中根目录下 新建static  映射 builtins路径



在html中 先装载静态文件

{% load static%}

之后按目录层级进行引用

注：利用vscode-prettier 格式化html文档



**url跳转的坑**

1.redirect方法：要么整体跳转，要么在原有request上进行拼接

2.在html form 标签属性中 action字段以拼接方式 进行动作跳转(以拼接发送请求) 也可以与redirect一致 以整体跳转链接进行请求





## 2.登录

**数据库信息初始化**

![image-20230304114442000](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230304114442000.png)

数据库表中设置自增初始化键



在setting中注册app

然后 进行迁移

https://blog.csdn.net/Dropall/article/details/83629652

在对应的app models中进行配置



**迁移命令**

manage.py makemigrations

manage.py migrate

注意：迁移默认为全局迁移，也就是如果以前有 该配置的表 会在makemigrations检测出来

默认会以当此变更未做迁移的数据进行操作



**高级迁移命令**

manage.py makemigrations appname

仅对指定app修改的model进行迁移



如果在数据库中 数据库设计与model中(实际为该app下migrations最新不对应，会出现错误)

解决方案：

1.备份当前数据

2.删除该app下migrations 中除了__init___.py文件(初始化)

3.在数据库django_migrations表中，删除与该表相关信息

重新迁移即可



**用户登录逻辑**

1.orm查询要点

在views层中导入

以models的object(对象)来进行操作

https://blog.csdn.net/DAO_HUNG/article/details/120636209



注意操作分清维度

以数据表为对象(table_name) 还是以数据表中数据为对象(table_name.object)







# 3.用户管理

## 1.userinfo列表查询 

两种形式：

1.html django形式

2.前后端分离 vue



2.不同app之间调用model时，可以在view层直接引用



## 2.添加用户

函数：

get请求 看到页面 输入内容

post 提交-》写入数据库

注意点：

1.注意 添加用户的页面，与表单提交

![image-20230308205823890](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230308205823890.png)

2.注意关联url，跳转链接或者如果添加页面与提交表单页面相同，可以对于form表单不设置action

3.插入数据 代码

```python
UserInfo.objects.create(name=_name, password=_password)
```

create “插入”

4.跳转 可以直接redirect  默认以当前host进行拼接跳转

![image-20230308210555145](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230308210555145.png)

添加用户的url 注意  最后没有/  --- 表单提交

![image-20230308214159953](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230308214159953.png)

提交数据 form报表或者ajax



## 3.删除用户

get请求 看到页面 输入内容

post 提交-》写入数据库

注意点：

1.需判断删除的用户是否存在

2.删除需关注语句是否正确(判断、过滤条件)

3.删除语句

```python
UserInfo.objects.filter(name=_name).delete()
```

通过name进行删除

4.优化点 可以加一列 操作列，利用id对其该行数据进行 操作

在html中拿到id，obj.id  通过id进行 get 删除

![image-20230308214322243](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230308214322243.png)

![image-20230308214359058](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230308214359058.png)

4.get请求可直接用/?xxx=yyy来进行发送，并获取xxx对应的value



#### 注：所以orm对object进行操作，对应在pythno中的操作会映射“影响”到 该models！！！！





## 表结构设计：

```
title = models.CharField(verbose_name="标题", max_length=32)
```

verbose_name  注释，最好写上 清晰

#### django 会自己创建一个主键，自增的id

如需自己创建：

```
id = models.BigAutoField(verbose_name="id", primary_key=True)
```

```
id = models.AutoField(verbose_name="id", primary_key=True)
```

auto与bigauto区别为，int与bigint



#### 对于精度较高的数值

```
account = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=3, default=0)
```

max_digits 字符长度

decimal_places 小数位数

default 初始值



### 创建时间

```
creat_time = models.DateTimeField(verbose_name="入职时间")
```



### 外键

根据数据库设计 范式，外键关联 id  太过于固定的 不需要考虑 设计另一张表

关联表数据固定，去拿取id，节省存储开销 ，但是这样的代价如果查询次数多，多表联查时会有时间额外开销

```python
department = models.ForeignKey(verbose_name="部分表id", to="Department", to_field="id")
```

to 关联那张表

to_field关联表中那个字段

注意：

当使用ForeignKey时 django建表时会自动创建以_id为结尾的列名

如上代码最后结果为列名为： department_id



特殊场景：

如果department中删除了部分，那么已经创建的用户表中数据如何处理？一般两种处理方式

1.级联删除  department表被删除了，直接删除用户表中 所关联的数据

```
department = models.ForeignKey(verbose_name="部分表id", to="Department", to_field="id", on_delete=models.CASCADE)
```

on_delete=models.CASCADE

2.置空操作(关联操作不会出问题)

需先将这一列设置为可以为空

再将其设置处理为空

```
department = models.ForeignKey(verbose_name="部分表id", to="Department", to_field="id", blank=True ,on_delete=models.SET_NULL)

```



不同app间调用

![image-20230311153513075](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311153513075.png)



### 二项选择

*在django中做约束*

```
gender_choices = (
        (1, "male"),
        (2, "female")
    )

    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
```

在django中形成约束，存在于内存中；；；

再传值时，仅能传入choices中的那一个值



# 4.静态文件管理

bootstrap--前端框架

需引入jQuery

![image-20230311113019909](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311113019909.png)

学会在bootstrap中寻找所需组件  个性化自己所需的



注意Form与ModelForm组件！！！！



# 5.部门管理

原型图：

![image-20230311113440979](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311113440979.png)

## 1.html引入静态文件

![image-20230311114114113](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311114114113.png)

min：压缩版







## 2.导入script

![image-20230311121348636](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311121348636.png)



## 3.构建html

利用bootstrap组件进行构建

**技巧：利用F12 去快速拿到想要的模板**



**图标**样式：

![image-20230311123511206](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311123511206.png)

![image-20230311123528765](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311123528765.png)



**模板组件：**

![image-20230311123607663](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311123607663.png)



小技巧：

下边距设置：

![image-20230311123705913](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311123705913.png)

按钮设置：

btn-xs 小按钮

![image-20230311125437949](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230311125437949.png)



autocomplete  不带入历史值

required 必填项校验

![image-20230318185314519](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318185314519.png)



### 展示所有部分列表信息

![image-20230318135640203](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318135640203.png)

![image-20230318135659637](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318135659637.png)





以字典方式传入

以循环方式解析



技巧 存在可将models对象转换为 dict 对象 函数

![image-20230318141948672](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318141948672.png)

![image-20230318141957727](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318141957727.png)



vscode设置 ：同时有html与django  语法提示

https://blog.csdn.net/gandongusa/article/details/123049993



如果需要进行排序

![image-20230318214448118](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318214448118.png)

目前解决办法是 给objects返回的对象添加默认序列参数 进行排序 html拿取该参数进行展示

![image-20230318214538241](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318214538241.png)

![image-20230318214554906](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318214554906.png)



之后可用到js动态进行实现



### 添加部门

![image-20230318185844512](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318185844512.png)





### 删除部门

![image-20230318190749112](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318190749112.png)

{{%for obj in ***%}}

已经在该请求体中引用 之后引用直接obj.**即可



![image-20230318193040398](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318193040398.png)



路由匹配 path re_path

https://docs.djangoproject.com/zh-hans/3.2/topics/http/urls/#example

注意，无论什么请求get post put，只要路由能匹配，即可进行views层逻辑操作



```
<div class="panel panel-default">
  <!-- Default panel contents -->
  <div class="panel-heading">Panel heading</div>
  <div class="panel-body">
    <p>...</p>
  </div>

  <!-- Table -->
  <table class="table">
    ...
  </table>
</div>
```





### 编辑部门

![image-20230318215303532](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230318215303532.png)

注意点：

重新渲染时报错信息，回填



注意 如果传参数 以get方式传参，，可以直接设置接收参数

如：xxx/?nid=yyy

而是 xxx/num/edit

可以在view利用 另外参数进行接收 get请求

![image-20230319113822216](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319113822216.png)

此处nid为传参接收 

在html中设置传参

![image-20230319114312742](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319114312742.png)

此处id为传入参数，views层可接受



需设置路由规则匹配

![image-20230319114344136](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319114344136.png)



**orm规则**

orm中为filter、all等 返回为[obj,]既是一个也为列表加上queryset形式

如果为first、last、lastest等 直接返回queryset对象 利用属性访问即可 .id 

**列表+queryset  传入context后 需 for循环解析**

**queryset、dict传入后 可以指访问 即可**

**注意当model-queryset转为dict后 其内联将会失效！！** 如外键关联取值  django 内部默认规则取值



设计方式：

![image-20230319115704752](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319115704752.png)

同一个views层的函数可利用请求方式不同 对实际逻辑进行区分





### 模板继承

目的：对重复性的html进行操作，而导致如果其中一个公有html变更，那么所对应的html都得变更

如：导航栏设置为多个html都是相同的，其中主要变了，其他都得变，所以引入模板继承



html继承模板

![image-20230319145903372](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319145903372.png)

继承后，只需在该处加入模板即可

![image-20230319150634178](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319150634178.png)

extends 加入所需继承模板

block 所覆盖填写的块



技巧：

不想都加入一些资源  多写block css js

![image-20230319153238808](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319153238808.png)

![image-20230319153336489](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319153336489.png)





# 6.用户管理

## 1.用户列表展示

**注意点：**

1.在django里设置固定的映射关系  利用 get_xxx_display()  即可 拿到实际值

![image-20230319162230641](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319162230641.png)

![image-20230319162243783](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319162243783.png)



2.在django中设置了外键关联 关系，因为设置外键时，会自动在外键名称后加上_id进行存储

我们可以 直接利用属性获取该级联的关联对象，相当于直接获取关联后的那一行数据(关联查询 类似于join)，再进行属性 获取--view层

![image-20230319163953274](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319163953274.png)

![image-20230319164013092](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319164013092.png)

此方法为内部提供方法，，也可以单独写对其进行关联查询



注意此处写法：：

如果还需保持queryset对象 (可使用其内联关系，并且 对其进行排序)

![image-20230319173652282](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319173652282.png)

在html中 利用对象 属性 一级一级进行访问

![image-20230319173744289](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230319173744289.png)



因为在html5中不可以带有（）

```
{% for obj in xxx.item %}
```

所以当有函数需要进行传参数时 如上图  create_time

这里用到了django中的“管道”与内置过滤器 详情

https://docs.djangoproject.com/zh-hans/4.1/ref/templates/builtins/#built-in-filter-reference



## 2.用户添加

- 原始方式思路：本质 通用  【较麻烦】

- ```
  -用户提交数据无校验
  -出现错误，页面上应该有错误提示
  -页面上每一个字段都需要重写一遍 提交 关联
  -关联的数据，手动去获取并展示在页面
  ```

  

- Django组件

  - Form组件   原始前三条 包含 最后关联数据需要自己加

  - ModelForm组件   简单易用，但对于django 耦合度较高  直接关联model



-- 原始：

在html中建立多个input等

html中radio、select option选择后，实际传向后台为value值

![image-20230320224310008](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230320224310008.png)



在html中可以使用位置参数获取值



**用户部门下拉框选择**

![image-20230320224945667](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230320224945667.png)

注意引用后的数据类型 此处id 为str类型



-- Form组件

**view.py**

```python
class MyForm(Form):
	user = forms.CharField()
	pwd = form.CharField()
	email = form.CharFiled(widget=forms.Input) # 属于view层 与model无关；显示一个input框
def user_add(request):
	xxx
    form = MyForm()	# 实例化组件
    return render(request, "render.html", {"form":form})
```

**user_add.html**

```
<form method="post">
{{form.user}}   不用自己写html标签 坏处 无法控制样式css
{{form.pwd}} 
{{form.email}}
</form>
```



--ModelForm

**model.py**

```python
from django.db import models
from datetime import datetime
from mainapp.models import Department
# Create your models here.

class UserInfo(models.Model):
    '''员工表'''
    name = models.CharField(verbose_name="姓名" ,max_length=32)
    password = models.CharField(verbose_name="密码", max_length=32, default="123")  # 修改表中列的时候 1 手动填充 2 添加default
    age = models.IntegerField(verbose_name="年龄", default=18)

    # decimal 可以更加精确设计数值 长度 精度等
    account = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=3, default=0)
    
    # 创建时间
    create_time = models.DateTimeField(verbose_name="入职时间", default=datetime.now())

    # 外键 to那张表 to_field 表中那一列进行关联  会自动加上_id,以其命名
    # blank 允许为空
    # on_delete 外键关联数据被删除后 操作
    department = models.ForeignKey(verbose_name="部分表id", to=Department, to_field="id", blank=True ,on_delete=models.CASCADE, default=1)

    # 二项选择 在django中做约束
    gender_choices = (
        (1, "male"),
        (2, "female")
    )

    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, default=1)

```



**view.py**

```
class MyForm(forms.ModelForm):
	class Meta:   # 内部类
		model = UserInfo
		fields = ["name","password","age","account","create_time","department","gender"]
```

定义拉取form



![image-20230327211350157](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230327211350157.png)



直接获取内部字段

![image-20230327211405210](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230327211405210.png)



该输入框直接关联对应字段

![image-20230327211413512](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230327211413512.png)

form.label可展示 models中编写字段的verbose_name

![image-20230327212347800](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230327212347800.png)

问题：

django 直接内部通过all函数 返回；如果为对象 则以对象显示 如下

![image-20230327213102842](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230327213102842.png)

解决：

当返回对象时 实际为对象的地址，可以对象的内部函数 重写__str__  java中为toString

https://blog.csdn.net/weixin_42011794/article/details/115938912

该函数写什么就返回什么  面向对象

```
class foo(object):
	def __str__(self):
		return "ok"

obj = foo()
print(obj) -> ok
```

![image-20230327214637661](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230327214637661.png)



使用FormModel时加入样式

插件widgets

![image-20230327220739862](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230327220739862.png)



设置模型全局  调用全局 设置 更改 全局属性

此方法适合该部分都适用此样式

![image-20230327221112260](C:\Users\Asherboy\AppData\Roaming\Typora\typora-user-images\image-20230327221112260.png)
