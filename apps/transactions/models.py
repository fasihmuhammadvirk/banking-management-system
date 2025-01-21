from django.db import models
from apps.accounts.models import Account
from banking_management_system.models import BaseModel


class Transaction(BaseModel):
    TRANSACTION_TYPES = [
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account")

    class Meta:
        ordering = ['-created_at']
