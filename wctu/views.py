from django.shortcuts import render, redirect, HttpResponse
from . import system
from . import admin
import json
import time


# Python 页面渲染
# 2020/11/18 23点16分
# by admin@musp.cn


def home(request):
    webdata = system.webinfo()
    apidata = system.apidata()
    return render(request, 'index.html', {'lt': apidata, 'st': webdata})


def docs(request):
    webdata = system.webinfo()
    return render(request, 'docs.html', {'st': webdata})


def diyapi(request):
    webdata = system.webinfo()
    return render(request, 'diy-api.html', {'st': webdata})


def join(request):
    webdata = system.webinfo()
    return render(request, 'join.html', {'st': webdata})


def runtest(request):
    webdata = system.webinfo()
    return render(request, 'runtest.html', {'st': webdata})


def login(request):
    name = request.POST.get('name', '')
    pwd = request.POST.get('password', '')
    if name:
        data = admin.login_accept(name, pwd)
        if data:
            response = redirect("/admin/index")
            response.set_cookie('token', data,  18000)
            return response
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



def apisever(request):
    print('n1',time.time())
    url = request.GET.get('url', '')
    pt = int(request.GET.get('id', '0'))
    if pt == 1:
        data = NewSever(url).kuaishou()
    elif pt == 2:
        data = NewSever(url).douyin()
    else:
        data = NewSever().returns()
    return HttpResponse(json.dumps(data),'application/json; charset=UTF-8')