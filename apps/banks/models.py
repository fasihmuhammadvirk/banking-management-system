from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    is_islamic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
