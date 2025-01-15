from django.urls import path
from apps.banks.views import BankListView

urlpatterns = [

    path('banks/', BankListView.as_view(), name='banks-list'),

]
