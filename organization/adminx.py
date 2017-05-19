# -*- coding:utf-8 -*-
import xadmin

from models import City,Teacher,CourseOrg


class CityAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', ]


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years','work_compay','points','click_num','fav_num','add_time']
    list_filter = ['org__name', 'name', 'work_years','work_compay','points','click_num','fav_num','add_time']
    search_fields = ['org', 'name', 'work_years','work_compay','points','click_num','fav_num']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num','fav_num','image','address','city','add_time']
    list_filter = ['name', 'desc', 'click_num','fav_num','image','address','city','add_time']
    search_fields = ['name', 'desc', 'click_num','fav_num','image','address','city']


xadmin.site.register(City,CityAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)