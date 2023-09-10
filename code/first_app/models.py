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
