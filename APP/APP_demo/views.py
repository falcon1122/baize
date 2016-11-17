#!/usr/bin/env python
#coding:utf-8

# (c) 2016 , Tianbiao Zu <zutianbian@qq.com>
#
# 该文件是白泽自动化管理系统的一部分,是白泽系统APP_demo应用的视图处理文件


###################################################################################################
from django.shortcuts import render_to_response


def index(request):
    """ 示例应用主页 """
    return render_to_response('index.html')
