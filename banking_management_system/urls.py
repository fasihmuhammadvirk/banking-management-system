from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/', include('apps.users.urls')),
    path('banks/', include('apps.banks.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('transactions/', include('apps.transactions.urls')),

]
