# -*- coding:utf-8 -*-
import xadmin
from xadmin import views
from models import EmailVerifyRecord,Banner


class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True


class GlobalSettings(object):
    site_title='慕学后台管理系统'
    site_footer='慕学在线网'
    #menu_style='accordion'


class EmailVerifyRecordAdmin(object):

    list_display=['code','send_type','email','send_time']
    list_filter=['code','send_type','email','send_time']
    search_fields=['code','send_type','email']
    model_icon='fa fa-user'
    list_editable=['code','send_type']


class BannerAdmin(object):

    list_display = ['title', 'image', 'url', 'index','addTime']
    list_filter = ['title', 'image', 'url', 'index','addTime']
    search_fields = ['title', 'image', 'url', 'index']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)