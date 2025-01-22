from django.urls import path
from apps.accounts.views import user_account_list_view

urlpatterns = [

    path("", user_account_list_view, name='accounts-list'),

]
