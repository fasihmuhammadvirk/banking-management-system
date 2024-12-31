from ..bank.models import Bank
from django.db import models
from django.contrib.auth.models import User


# Account Model
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank")
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
