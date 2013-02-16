from django.db import models

SUCCESS = 1
ERR_BAD_CREDENTIALS = -1
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4

# Create your models here.
class UserModel(models.Model):
    user = models.CharField(primary_key=True, max_length=128)
    password = models.CharField(blank=True, max_length=128)
    count = models.IntegerField()
    
def login(userField, passwordField):
    if UserModel.objects.filter(user__exact=userField) and passwordField == UserModel.objects.filter(user__exact=userField)[0].password:
        u = UserModel.objects.filter(user__exact=userField)[0]
        u.count += 1
        u.save()
        return UserModel.objects.filter(user__exact=userField)[0].count
    else:
        return ERR_BAD_CREDENTIALS
        
def add(userField, passwordField):
    if userField=='' or len(userField) > 128:
        return ERR_BAD_USERNAME
    elif UserModel.objects.filter(user__exact=userField):
        return ERR_USER_EXISTS
    elif len(passwordField) > 128:
        return ERR_BAD_PASSWORD
    else:
        u = UserModel(user=userField, password=passwordField, count=1)
        u.save()
        return UserModel.objects.filter(user__exact=userField)[0].count
        
def TESTAPI_resetFixture():
    UserModel.objects.all().delete()
    return SUCCESS