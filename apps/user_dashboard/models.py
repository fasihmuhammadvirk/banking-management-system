from django.db import models


# Create your models here.
class MyUser(models.Model):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
