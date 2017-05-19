# -*- coding:utf-8 -*-
from django.conf.urls import url,include
import xadmin
import views

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/$',views.index,name='index'),
    url(r'^register/$',views.user_register,name='register'),
    url(r'^login/$',views.user_login,name='login'),
]