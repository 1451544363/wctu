"""
1、删除数据库对应的数据表
注意：在这里可以不用暴力删除数据表，可以利用django的migrations进行，操作如下：
1.1、首先将自己需要重构的数据表类的models注释掉，然后输入命令python manage.py makemigrations，这个时候migration会自动记录删除数据表的操作
1.2、然后在输入命令python manage.py migrate，Django会自动将本地对应的数据库进行删除

1.python manage.py makemigrations --empty wctu
2.python manage.py makemigrations
3.python manage.py migrate

"""
from django.db import models


# 创建数据库表名格式为，项目名_类名（类名统一转换成小写生成）
# 2020/11/18 23点04分
# by admin@musp.cn

# 创建Api信息表数据库表
class HomeApi(models.Model):
    Id = models.AutoField(primary_key=True)
    ApiName = models.TextField()
    ApiUrl = models.URLField()
    ApiData = models.TextField()

    class Meta:
        db_table = 'wctu_homeapi'


# 创建管理员表
class AdminUser(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.CharField(max_length=20)
    Pwd = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)
    Pid = models.ImageField(max_length=1)
    Token = models.TextField(max_length=30)
    Token_out = models.TextField(max_length=20)


# 创建用户表
class Users(models.Model):
    Username = models.CharField(max_length=15)
    UserPsaaword = models.CharField(max_length=100)
    UserEmail = models.EmailField(max_length=20)
    UserTel = models.CharField(max_length=11, blank=True)
    UserKey = models.CharField(max_length=15)


# 创建用户调用Api次数表
class UserApi(models.Model):
    Id = models.AutoField(primary_key=True)
    Pid = models.UUIDField(blank=False)
    AApi = models.ImageField(max_length=10)
    ATime = models.TextField(max_length=65535)
    BApi = models.ImageField(max_length=10)
    BTime = models.TextField(max_length=65535)


# 创建网页配置数据库表
class HomeData(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Keywords = models.CharField(max_length=20)
    Description = models.CharField(max_length=200)
    Record = models.CharField(max_length=20)
    ConInfo = models.CharField(max_length=20)
