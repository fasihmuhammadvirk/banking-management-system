from django.db import models
from django.contrib.auth.models import User

# Bank Model
class Bank(models.Model):
    name = models.CharField(max_length=100)  # Bank name
    branch = models.CharField(max_length=100)  # Branch name
    is_islamic = models.BooleanField(default=False)  # Flag for Islamic bank
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when bank was added


