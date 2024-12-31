from django.contrib import admin
from .models import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'is_islamic', 'created_at')
    list_filter = ('name', 'branch')
    search_fields = ('name', 'branch')
