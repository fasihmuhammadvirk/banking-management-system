from django.db import models

from apps.accounts.models import Account
from banking_management_system.models import BaseModel
from apps.transactions.choices import TRANSACTION_TYPES


class Transaction(BaseModel):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    transaction_type = models.CharField(max_length=16, choices=TRANSACTION_TYPES)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.account} | {self.amount}"
