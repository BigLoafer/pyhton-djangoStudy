# -*- coding:utf-8 -*-

import xadmin

from models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):

    list_display = ['name', 'desc', 'detail', 'degree','learn_time','students','fav_nums','image','click_nums','add_time']
    list_filter = ['name', 'desc', 'detail', 'degree','learn_time','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree','learn_time','students','fav_nums','image','click_nums']
    style_fields={'detail':'ueditor'}


class LessonAdmin(object):
    list_display = ['course','name', 'add_time']
    list_filter = ['course__name','name', 'add_time']
    search_fields = ['name', 'course']


class VideoAdmin(object):
    list_display=['lesson','name','add_time']
    list_filter=['lesson__name','name','add_time']
    search_fields=['lesson','name']


class CourseResourceAdmin(object):
    list_display=['course','name','add_time','download']
    list_filter=['course__name','name','add_time','download']
    search_fields=['course','name','download']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
