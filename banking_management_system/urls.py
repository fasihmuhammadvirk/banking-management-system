from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/', include('apps.users.urls')),
    path('', RedirectView.as_view(url='user/', permanent=True)),  # Redirect root URL to /user/
    path('banks/', include('apps.banks.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('transactions/', include('apps.transactions.urls')),

]
