from django.urls import path
from apps.transactions.views import TransactionListView, TransactionCreateView
urlpatterns = [

    path('history/', TransactionListView.as_view(), name='transactions-list'),
    path('make/', TransactionCreateView.as_view(), name='make-transaction'),

]
