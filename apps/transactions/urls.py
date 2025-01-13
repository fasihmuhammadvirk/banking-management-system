from django.urls import path
from apps.transactions.views import TransactionListView, TransactionCreateView

urlpatterns = [

    path('transactions/', TransactionListView.as_view(), name='transactions-list'),
    path('make/transaction/', TransactionCreateView.as_view(), name='make-transaction'),

]
