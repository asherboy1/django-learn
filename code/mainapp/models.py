from django.db import models
from datetime import datetime
# Create your models here.
class Department(models.Model):
    '''部门表'''
    # django 会自己创建一个主键，自增的id
    # id = models.BigAutoField(verbose_name="id", primary_key=True)

    depart_name = models.CharField(verbose_name="部门名称", max_length=32)
    # 创建时间
    create_time = models.DateTimeField(verbose_name="创立时间", default=datetime.now())


    def __str__(self):
        return self.depart_name
