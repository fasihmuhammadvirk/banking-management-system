from django.contrib import admin
from apps.transactions.models import Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'transaction_type', 'created_at')
    list_filter = ('transaction_type', 'account__account_number')
    search_fields = ('account__account_number',)
