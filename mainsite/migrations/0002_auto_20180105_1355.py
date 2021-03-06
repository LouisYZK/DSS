# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='仰卧起坐',
            new_name='fhl',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='体重',
            new_name='height',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='坐位体前屈',
            new_name='ldty',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='姓名',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='立定跳远',
            new_name='r1000',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='跑_1000米',
            new_name='r50',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='跑_50米',
            new_name='r800',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='学院',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='性别',
            new_name='sex',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='跑_800米',
            new_name='weight',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='学号',
            new_name='xh',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='引体向上',
            new_name='ytxs',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='肺活量',
            new_name='ywqz',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='身高',
            new_name='zwtqq',
        ),
    ]
