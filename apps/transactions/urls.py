from django.urls import path
from apps.transactions.views import TransactionListView, TransactionCreateView
urlpatterns = [

    path('history/<str:account_number>', TransactionListView.as_view(), name='transactions-list'),
    path('make/<str:account_number>', TransactionCreateView.as_view(), name='make-transaction'),

]
