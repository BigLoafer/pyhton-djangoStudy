# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  datetime import datetime

from django.db import models

# Create your models here.


class City(models.Model):
    name=models.CharField(max_length=50,verbose_name='城市名 ')
    desc=models.CharField(max_length=200,verbose_name='描述 ')
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name='城市'
        verbose_name_plural=verbose_name


class CourseOrg(models.Model):
    name=models.CharField(max_length=50,verbose_name='机构')
    desc=models.TextField(verbose_name='机构描述')
    click_num=models.IntegerField(default=0,verbose_name='点击数')
    fav_num=models.IntegerField(default=0,verbose_name='收藏数')
    image=models.ImageField(upload_to='org/%Y/%m',verbose_name='封面图',max_length=100)
    address=models.CharField(max_length=200,verbose_name='机构地址')
    city=models.ForeignKey(City,verbose_name='所在城市')
    add_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name='课程机构'
        verbose_name_plural=verbose_name


class Teacher(models.Model):
    org=models.ForeignKey(CourseOrg,verbose_name='所属机构')
    name=models.CharField(max_length=20,verbose_name='教师名字')
    work_years=models.IntegerField(default=0,verbose_name='就职年限')
    work_compay=models.CharField(max_length=50,verbose_name='就职公司')
    work_position=models.CharField(max_length=50,verbose_name='就职职位')
    points=models.CharField(max_length=100,verbose_name='教师特点')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name='教师'
        verbose_name_plural=verbose_name



