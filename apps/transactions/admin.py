from django.contrib import admin
from apps.transactions.models import Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account__account_number', 'account__user__username', 'amount', 'transaction_type', 'created_at')
    list_filter = ('transaction_type', 'amount', 'account__user__username')
    search_fields = ('transaction_type', 'amount', 'account__user__username')
