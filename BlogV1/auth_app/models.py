from django.db import models




class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.IntegerField()
    email=models.CharField(max_length=20)
    telephone=models.CharField(max_length=15)
    status=models.IntegerField()