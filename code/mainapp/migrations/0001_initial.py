# Generated by Django 4.0.5 on 2023-03-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_name', models.CharField(max_length=32, verbose_name='部门名称')),
                ('create_time', models.DateTimeField(verbose_name='创立时间')),
            ],
        ),
    ]