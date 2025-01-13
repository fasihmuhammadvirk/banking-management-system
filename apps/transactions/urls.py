from django.urls import path
from apps.transactions.views import transactions_list_view, transaction_create_view

urlpatterns = [

    path('transactions/', transactions_list_view, name='transactions-list'),
    path('create/transaction/', transaction_create_view, name='create-transaction'),

]
