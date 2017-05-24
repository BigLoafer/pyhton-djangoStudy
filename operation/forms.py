# -*- coding:utf-8 -*-
from django import forms
import models
import re


class UserAskForms(forms.Form):
    name=forms.CharField(required=True,min_length=2,max_length=20)
    phone=forms.CharField(required=True,min_length=11,max_length=11)
    course_name=forms.CharField(required=True,min_length=5,max_length=100)


class AnotherUserForm(forms.ModelForm):

    class Meta:
        model=models.UserAsk
        fields=['name','mobile','course_name']

    def clean_mobile(self):
        mobile=self.cleaned_data['mobile']
        REGEX_MOBILE='^1[3458]\\d{9}$'
        p=re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法',code='mobile_invalid')
