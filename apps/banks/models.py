from django.db import models
from banking_management_system.models import BaseModel


class Bank(BaseModel):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    is_islamic = models.BooleanField(default=False)
