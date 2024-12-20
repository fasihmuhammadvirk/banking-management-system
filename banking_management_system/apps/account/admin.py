from django.contrib import admin
from .models import Account

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank', 'account_number', 'balance')
    search_fields = ('user__username', 'account_number', 'bank__name')
