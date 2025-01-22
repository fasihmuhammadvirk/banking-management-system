from django.urls import path
from apps.transactions.views import transactions_list_view, transaction_create_view

urlpatterns = [

    path('history/', transactions_list_view, name='transactions-list'),
    path('make/', transaction_create_view, name='make-transaction'),

]
