from django.contrib.auth.models import AbstractUser
from django.db import models

from banking_management_system.models import BaseModel


class User(AbstractUser, BaseModel):
    address = models.CharField(max_length=200)
    phone_number = models.DecimalField(max_digits=11, default=00000000000, decimal_places=0)

    def __str__(self):
        return self.username
