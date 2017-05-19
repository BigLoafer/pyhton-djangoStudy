# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate,login

# Create your views here.


def index(request):

    if request.method =="POST":
        pass
    else:
       return render(request,'index.html')


def user_register(request):
    if request.method=="POST":
        pass
    else:
        return render(request,'register.html')


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username',None)
        pwd=request.POST.get('password',None)
        user=authenticate(username=username,password=pwd)
        if user:
            login(request,user)
            return render(request,'index.html')
        else:
            return render(request,'login.html',{'err_msg': '用户名或密码错误'})

    else:
       return render(request,'login.html')