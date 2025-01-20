from django.contrib import admin
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'address')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('username', 'address')
