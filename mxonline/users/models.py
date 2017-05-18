# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfo(AbstractUser):
    nick_name=models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birday=models.DateField(verbose_name=u'生日', null=True,blank=True)
    gender=models.CharField(choices=(('male', u'男'), ('female', u'女')), default='female', max_length=10)
    address=models.CharField(max_length=100, default='')
    mobile=models.CharField(max_length=11, null=True, blank=True)
    image=models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name=u'验证码')
    send_type=models.CharField(max_length=20,choices=(('register' , u'注册'),('forget',u'找回密码')))
    email=models.EmailField(max_length=50,verbose_name=u'邮箱')
    send_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u'邮箱验证码'
        verbose_name_plural=verbose_name


class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name='标题')
    image=models.ImageField(upload_to='banner/%Y/%m',verbose_name='轮播图' ,max_length=200)
    url=models.URLField(max_length=200, verbose_name='访问地址')
    index=models.IntegerField(default=100,verbose_name='顺序')
    addTime=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name='轮播图'
        verbose_name_plural=verbose_name


class Test(models.Model):
    name=models.CharField(max_length=30,verbose_name='测试')