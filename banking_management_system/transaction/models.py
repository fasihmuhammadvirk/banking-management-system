from django.db import models
from ..account.models import Account

# Transaction Model (Optional for Future Development)
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
    ]

    account = models.ForeignKey(Account , on_delete=models.CASCADE, related_name="account")  # Link to Account
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Positive for deposit, negative for withdrawal
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)  # Transaction type
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for the transaction
