# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
import forms
from django.http import HttpResponse
import json
import models
# Create your views here.


class UserAskView(View):

    def post(self,request):
        userask_form=forms.AnotherUserForm(request.POST)
        if userask_form.is_valid():
            user_ask=userask_form.save(commit=True)

            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}',content_type='application/json')



