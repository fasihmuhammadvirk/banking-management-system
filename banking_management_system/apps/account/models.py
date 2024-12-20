from ..bank.models import Bank
from django.db import models
from django.contrib.auth.models import User

# Account Model
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")  # Link to User model
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank")  # Link to Bank model
    account_number = models.CharField(max_length=20, unique=True)  # Unique account number
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Account balance
