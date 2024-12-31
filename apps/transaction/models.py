from datetime import timezone

from django.db import models
from ..account.models import Account
from django.utils.timezone import now

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account")
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Positive for deposit, negative for withdrawal
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
