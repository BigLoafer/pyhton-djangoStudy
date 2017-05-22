# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
import models
# Create your views here.


class OrgListView(View):

    def get(self,request):
        all_citys=models.City.objects.all()

        return render(request,'org-list.html',{'all_citys':all_citys})
