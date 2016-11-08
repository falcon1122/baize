#!/usr/bin/env python
#coding:utf-8

# (c) 2016 , Xianglong Meng <falcon1122@163.com>
#
# 该文件是白泽自动化管理系统的一部分,是白泽系统login的url路由文件


###################################################################################################
from django.conf.urls import patterns,url
from APP.APP_login.views import user_login,index

urlpatterns = patterns('',
    url(r'^$', user_login),
)
