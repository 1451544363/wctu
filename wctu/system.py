from . import models


def webinfo():
    data = models.HomeData.objects.get(Id=1)
    return data

def modweb(data):
    mod = models.HomeData.objects.filter(Id=1)
    mod.update(data)

def apidata():
    data = models.HomeApi.objects.all()
    return data

def getadmin():
    data = models.AdminUser.objects.get(Id=1)
    return data


