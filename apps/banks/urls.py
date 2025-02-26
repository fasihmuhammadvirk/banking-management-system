from django.urls import path
from apps.banks.views import BankListView, BankCreateView

urlpatterns = [

    path('', BankListView.as_view(), name='banks-list'),
    path('create', BankCreateView.as_view(), name='create-bank' )

]
