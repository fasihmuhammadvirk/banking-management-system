from django.contrib.auth.models import AbstractUser
from django.db import models

from banking_management_system.models import BaseModel


class User(AbstractUser, BaseModel):
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16, default=00000000000)

    def __str__(self):
        return f'{self.username}'
