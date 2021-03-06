# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-06 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='defen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('xh', models.CharField(max_length=20)),
                ('grade', models.FloatField(max_length=20)),
                ('ytxs', models.FloatField(max_length=10)),
                ('sex', models.IntegerField(max_length=10)),
                ('ldty', models.FloatField(max_length=10)),
                ('fhl', models.FloatField(max_length=10)),
                ('r50', models.FloatField(max_length=10)),
                ('r800', models.FloatField(max_length=10)),
                ('r1000', models.FloatField(max_length=10)),
                ('add', models.FloatField(max_length=10)),
                ('bmi', models.FloatField(max_length=10)),
                ('zwtqq', models.FloatField(max_length=10)),
                ('total', models.FloatField(max_length=10)),
            ],
        ),
    ]
