# Django 页面路由
# 2020/11/19 18：16
# by admin@musp.cn

from django.urls import path, re_path
from . import views
from . import admin

urlpatterns = [
    path(r"", views.home),
    re_path("^docs/$", views.docs),
    re_path('^join/$', views.join),
    re_path('^diy-api/$', views.diyapi),
    re_path('^runtest/$', views.runtest),
    re_path('^admin.+?', admin.admin),
    re_path('^login/$', views.login),
    re_path('^api-sever.+', views.apisever)
]
