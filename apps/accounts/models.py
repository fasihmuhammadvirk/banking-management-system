from apps.banks.models import Bank
from django.db import models
from apps.users.models import User
from banking_management_system.models import BaseModel


class Account(BaseModel):
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = models.CharField(max_length=32, unique=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    class Meta:
        unique_together = ['bank', 'user']

    def __str__(self):
        return f"{self.user} | {self.account_number} | {self.bank}"
