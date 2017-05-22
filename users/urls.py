# -*- coding:utf-8 -*-
from django.conf.urls import url,include
import xadmin
import views

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/$',views.IndexView.as_view(), name='index'),
    url(r'^register/$',views.RegistView.as_view(), name='register'),
    url(r'^login/$',views.LoginView.as_view(), name='login'),
    url(r'^forget/$',views.ForgetPwdView.as_view(), name='forget'),
]