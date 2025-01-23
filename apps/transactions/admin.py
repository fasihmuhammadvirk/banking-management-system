from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.transactions.models import Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = ('account', 'amount', 'transaction_type', 'created_at', 'updated_at')
    list_filter = ('transaction_type', 'created_at', 'updated_at')
    search_fields = ('=amount', 'account__user__username')
