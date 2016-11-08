#!/usr/bin/env python
#coding:utf-8

# (c) 2016 , Xianglong Meng <falcon1122@163.com>
#

# 该文件是白泽自动化管理系统的一部分,是白泽系统的配置文件，配置常量定义


###################################################################################################
import os


####################################################################################################
# web界面的配置管理列表
##########################
# 示例:跳转页面的默认参数
#   REDIRECT = '/asset_manage'
REDIRECT = '/asset_manage'
# 示例:记住密码的默认参数，单位：小时
#   REMEBER_ME = 1
REMEBER_ME = 1


####################################################################################################
# 日志相关配置
# 调用示例:
#        errInfo = u'我要报警了!'
#        logger = logging.getLogger('log_file')
#        logger.error(errInfo.encode('utf8'))
#        if C.LOG_SCREEN == 'ON':
#            logger = logging.getLogger('log_screen')
#            logger.error(errInfo.encode('utf8'))
##########################
# 是否开启日志
#   示例:LOG_OPEN=['ON'|'OFF']
LOG_OPEN = 'ON'
# 日志级别
#    示例:LOG_LEVEL=['DEBUG'|'INFO'|'WARNING'|'ERROR'|'CRITICAL']
LOG_LEVEL = 'DEBUG'
# 日志文件路径
#   默认:LOG_FILE=os.path.join(os.path.dirname(__file__),'log/%s.log' % LOG_LEVEL.lower())
#   示例:LOG_FILE='/var/run/log/access.log'
LOG_FILE = os.path.join(os.path.dirname(__file__), 'log/%s.log' % LOG_LEVEL.lower())
# 是否向标准输出打印日志
#   示例:LOG_SCREEN=['ON'|'OFF']
LOG_SCREEN = 'OFF'
# 日志格式
# 示例:LOG_FORMAT = '"[%(asctime)s]" "%(pathname)s[line:%(lineno)d]" "[%(levelname)s]" "%(message)s"'
#   %(name)s	                      日志记录器名称
#   %(levelno)s	                      日志级别编号
#   %(levelname)s	                  日志级别名称('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
#   %(pathname)s	                  打印日志的代码文件路径
#   %(filename)s	                  打印日志的代码文件名称
#   %(module)s	                      打印日志的代码模块名称
#   %(funcName)s	                  打印日志的代码函数名称
#   %(lineno)d	                      打印日志的代码行号
#   %(created)f	                      日志记录器产生的时间戳
#   %(relativeCreated)d	              日志打印时间(毫秒)
#   %(asctime)s	                      日志打印时间(可读性强例如'2016-10-11 16:00:00')
#   %(msecs)d	                      日志打印时间的毫秒值
#   %(thread)d	                      线程id
#   %(threadName)s	                  线程名称
#   %(process)d	                      进程id
#   %(message)s	                      日志消息主体
LOG_FORMAT = '"[%(asctime)s]" "%(pathname)s[line:%(lineno)d]" "[%(levelname)s]" "%(message)s"'


####################################################################################################
# 文件上传的相关配置
##########################
# 文件上传的路径
UPLOAD_ROOT = os.path.join(os.path.join(os.path.dirname(__file__), 'static'), 'upload')
