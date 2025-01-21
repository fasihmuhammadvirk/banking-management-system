from django.contrib import admin
from apps.transactions.models import Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'account__bank','amount', 'transaction_type', 'created_at', 'updated_at')
    list_filter = ('transaction_type', 'created_at', 'updated_at')
    search_fields = ('=amount', '=account' , 'account__bank')
