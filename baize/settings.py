#!/usr/bin/env python
#coding:utf-8

# (c) 2016 , Tianbiao Zu <zutianbian@qq.com>
#
# 该文件是白泽自动化管理系统的一部分,是白泽系统的django环境配置文件


###################################################################################################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p#ls2t*^h6t+0!3uyaj3*&5%7%p))=fge7-z09@c9q6^snpuu_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'APP.APP_demo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'baize.urls'

WSGI_APPLICATION = 'baize.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
DEFAULT_CHARSET = 'utf-8'
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_PASSWORD = 'baize1234'
EMAIL_HOST_USER = 'baize@163.com'
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = True
EMAIL_PORT = 25
ADMINS = (('zutianbiao@qq.com', 'zutianbiao@163.com'),)
import config as C
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': C.LOG_FORMAT,
        },
    },
    'filters': {
        'require_debug_true': {
        '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'mail_handler': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter':'standard',
        },
        'screen_handler': {
            'level': C.LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'standard',
        },
        'file_handler': {
            'level': C.LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': C.LOG_FILE,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'log_mail': {
            'handlers': ['mail_handler'],
            'level': 'ERROR',
            'propagate': True,
        },
        'log_screen': {
            'handlers': ['screen_handler'],
            'level': C.LOG_LEVEL,
            'propagate': False
        },
        'log_file': {
            'handlers': ['file_handler'],
            'level': C.LOG_LEVEL,
            'propagate': False
        },
    }
}

