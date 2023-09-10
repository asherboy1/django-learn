# Generated by Django 4.0.5 on 2023-03-11 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('password', models.CharField(default='123', max_length=32, verbose_name='密码')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('account', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='余额')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2023, 3, 11, 15, 20, 13, 426626), verbose_name='入职时间')),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1, verbose_name='性别')),
            ],
        ),
    ]
