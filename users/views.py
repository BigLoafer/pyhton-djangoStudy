# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic.base import View
import forms
from models import UserInfo
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_eamil

# Create your views here.


class IndexView(View):

    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        pass


class LoginView(View):

    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        login_form=forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', None)
            pwd = request.POST.get('password', None)
            user = authenticate(username=username, password=pwd)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request,'login.html',{'err_msg': '用户没有激活'})
            else:
                return render(request, 'login.html', {'err_msg': '用户名或密码错误'})
        else:
            return  render(request,'login.html',{'login_forms':login_form})


class RegistView(View):

    def get(self,request):

        register_form = forms.RegisterForm()
        return render(request, 'register.html',{'regist_form':register_form})

    def post(self,request):
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', None).strip()

            if UserInfo.objects.filter(email=email):
                return render(request,'register.html',{'err_msg':'用户已经呗注册了','regist_form' : register_form})

            pwd = request.POST.get('password', None)
            user_info=UserInfo()
            user_info.email=email
            user_info.username=email
            user_info.password=make_password(pwd)
            user_info.is_active=False
            user_info.save()

            send_register_eamil(email,'register')
            return redirect('/home/login')

        else:
            return render(request,'register.html',{'regist_form':register_form})


class ForgetPwdView(View):

    def get(self,request):
        forget_form=forms.ForgetForm();

        return render(request,'forgetpwd.html',{'forget_form':forget_form})


