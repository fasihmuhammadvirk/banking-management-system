from django.contrib import admin
from .models import Bank, Account, Transaction

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'is_islamic', 'created_at')
    search_fields = ('name', 'branch')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank', 'account_number', 'balance')
    search_fields = ('user__username', 'account_number', 'bank__name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'transaction_type', 'timestamp')
    list_filter = ('transaction_type',)
    search_fields = ('account__account_number',)
