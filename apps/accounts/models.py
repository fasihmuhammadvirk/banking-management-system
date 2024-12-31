from ..banks.models import Bank
from django.db import models
from django.contrib.auth.models import User


# Account Model
class Account(models.Model):
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = models.CharField(max_length=20, unique=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
