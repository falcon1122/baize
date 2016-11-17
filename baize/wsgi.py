#!/usr/bin/env python
#coding:utf-8

# (c) 2016 , Tianbiao Zu <zutianbian@qq.com>
#
# 该文件是白泽自动化管理系统的一部分,是白泽系统的wsgi文件


###################################################################################################

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baize.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
