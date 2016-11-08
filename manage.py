#!/usr/bin/env python
#coding:utf-8

# (c) 2016 , Tianbiao Zu <zutianbian@qq.com>
#
# 该文件是白泽自动化管理系统的一部分,是白泽系统的django工程管理文件


###################################################################################################
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baize.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
