from django.contrib import admin
from apps.accounts.models import Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'bank__name', 'account_number', 'balance')
    list_filter = ('user__username', 'bank__name', 'created_at')
    search_fields = ('user__username', 'bank__name')
