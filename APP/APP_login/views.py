#!/usr/bin/env python
#coding:utf-8

# (c) 2016 , Xianglong Meng <falcon1122@163.com>
#
# 该文件是白泽自动化管理系统的一部分,是白泽系统login的视图文件


###################################################################################################
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
import json
import config as C
import constant as D

@csrf_exempt
def user_login(request):
    '''
    用户登录视图，实现登录验证，登出，以及记住密码
    '''
    result = {}
    if request.method == 'POST':
        data = request.POST
        action = data.get('action')
        username = data.get('username','')
        request.session['username'] = username
        if action == 'login':
            password = data.get('password','')
            remember_me = data.get('remeber_me',C.REMEBER_ME)
            redirect = data.get('redirect',C.REDIRECT)
            user = auth.authenticate(username=username,password=password)
            expity_time = int(remember_me) * 3600
            request.session.set_expiry(expity_time)
            if user is not None and user.is_active:
                auth.login(request,user)
                result['success'] = True
                result['msg'] = D.MSG_SUCCESS
                result['redirect'] = redirect
            else:
                result['success'] = False
                result['msg'] = D.MSG_FAILED
            response = json.dumps(result)
            return HttpResponse(response)
        elif action == 'logout':
            auth.logout(request)
            return HttpResponse("LOGOUT NOW")
           # return HttpResponseRedirect("/login")




