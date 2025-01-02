from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('apps.user_dashboard.urls')),
    path('', include('apps.banks.urls')),
    path('', include('apps.accounts.urls')),
    path('', include('apps.transactions.urls')),

]
