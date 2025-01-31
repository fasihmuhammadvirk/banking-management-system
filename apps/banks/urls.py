from django.urls import path
from apps.banks.views import BankListView

urlpatterns = [

    path('', BankListView.as_view(), name='banks-list'),

]
