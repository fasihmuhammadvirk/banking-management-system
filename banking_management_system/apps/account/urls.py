from django.urls import path
from . import views

urlpatterns = [
path("all_accounts_list/", views.account_view, name='all_accounts_list'),
]

