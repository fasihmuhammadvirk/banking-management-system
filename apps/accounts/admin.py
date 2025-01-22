from django.contrib import admin
from apps.accounts.models import Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank', 'account_number', 'balance')
    list_filter = ('user', 'bank')
    search_fields = ('user__username', 'bank__name')
