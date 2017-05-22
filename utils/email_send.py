# -*- coding:utf-8 -*-

from users.models import EmailVerifyRecord
from random import Random
from  django.core.mail import send_mail
from mxonline.settings import EMAIL_FROM


def send_register_eamil(enail,type='register'):
    email_record=EmailVerifyRecord()
    code=generate_str(16)
    email_record.code=code
    email_record.email=enail
    email_record.send_type=type
    email_record.save()

    if type=='register':
        email_title='慕学在线网注册激活链接'
        email_body='请点击下面的链接激活你的账号:127.0.0.1:8000/active/{0}'.format(code)
        send_status=send_mail(email_title,email_body,EMAIL_FROM,[enail])
        if send_status:
            pass


def generate_str(randomlength=8):
    str=''
    chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRESTUVWXYZ0123456789'
    length=len(chars)-1
    random=Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str