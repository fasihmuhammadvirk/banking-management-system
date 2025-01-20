from django.contrib import admin
from apps.banks.models import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'is_islamic', 'created_at', 'updated_at')
    list_filter = ('is_islamic', 'created_at', 'updated_at')
    search_fields = ('name', 'branch', 'is_islamic')
