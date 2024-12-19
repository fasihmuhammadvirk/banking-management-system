from django.db import models
from django.contrib.auth.models import User

# Bank Model
class Bank(models.Model):
    name = models.CharField(max_length=100)  # Bank name
    branch = models.CharField(max_length=100)  # Branch name
    is_islamic = models.BooleanField(default=False)  # Flag for Islamic banking
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when bank was added

# Account Model
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")  # Link to User model
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank")  # Link to Bank model
    account_number = models.CharField(max_length=20, unique=True)  # Unique account number
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Account balance

# Transaction Model (Optional for Future Development)
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account")  # Link to Account
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Positive for deposit, negative for withdrawal
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)  # Transaction type
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for the transaction
