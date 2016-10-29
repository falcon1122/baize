#!/usr/bin/env python
#coding:utf-8

# (c) 2016 , Tianbiao Zu <zutianbian@qq.com>
#
# 该文件是白泽自动化管理系统的一部分,是白泽系统APP_demo应用的url路由文件


###################################################################################################
from django.conf.urls import patterns, url
from APP.APP_demo.views import index

urlpatterns = patterns('',
    url(r'^$', index),
)