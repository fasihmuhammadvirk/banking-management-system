from django.db import models
from banking_management_system.models import BaseModel


class Bank(BaseModel):
    name = models.CharField(max_length=256)
    branch = models.CharField(max_length=256)
    is_islamic = models.BooleanField(default=False)

    def __str__(self):
        return  f'{self.name} | {self.branch}'
