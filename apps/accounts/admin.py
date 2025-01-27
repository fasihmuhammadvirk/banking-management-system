from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.accounts.models import Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ('user', 'bank', 'account_number', 'balance', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'bank__name', 'account_number')
