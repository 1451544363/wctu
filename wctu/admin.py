"""
    后台视图
    2020/11/22 13点59分
    by admin@musp.cn
"""
from django.shortcuts import render, redirect
from . import models
from . import system
import random
import string
import time
import re


# 后台token过期验证
def token_verification(token):
    data = models.AdminUser.objects.get(Id=1)
    newtime = int(time.time())
    if data.Token == token and int(data.Token_out) > newtime:
        return True
    else:
        return False


def login_accept(name, pwd):
    data = models.AdminUser.objects.get(Id=1)
    if data.User == name and data.Pwd == pwd:
        new_time = str(int(time.time()) + 18000)
        token = tokens(data.Id, new_time)
        models.AdminUser.objects.filter(Id=1).update(Token=token, Token_out=new_time)
        return token
    else:
        return False


def tokens(uid, times):
    md_list = ['Z', 'N', 'M', 'A', 'F', 'G', 'K', 'L', 'R', 'T']
    pod = ''
    timeuid = str(times) + str(uid)
    for n in timeuid:
        pod = pod + md_list[int(n)]
    data = pod + '-' + ''.join(random.sample(string.ascii_letters + string.digits, 18))
    return data


# 后台路由正则表达式匹配
def re_url(url, reurl):
    if re.search(url, reurl, re.I):
        return True
    else:
        return False


def admin(request):
    token = request.COOKIES.get('token', '')
    if token_verification(token):
        url = request.path_info
        if re_url("/admin/index", url):
            return render(request, 'adminhome.html', )
        elif re_url("/admin/apiinfo", url, ):
            return render(request, 'apiinfo.html', )
        elif re_url("/admin/user", url):
            return render(request, 'user.html', )
        elif re_url("/admin/webinfo", url):
            data = system.webinfo()
            return render(request, 'webinfo.html', {'vo': data})
        elif re_url("/admin/webadmin", url):
            data = system.getadmin()
            return render(request, 'webadmin.html',{'vo': data})
        elif re_url("/admin/request", url):
            return render(request, 'request.html', )
        elif re_url("/admin/login_out", url):
            resp = redirect('/login/')
            resp.delete_cookie('token')
            return resp

        else:
            return render(request, '404.html')
    else:
        return redirect('/login/')

