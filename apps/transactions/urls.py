from django.urls import path
from . import views

urlpatterns = [

    path('transactions/', views.show_all_transaction, name='transactions'),
    path('make/transaction/', views.make_transaction, name='make/transaction'),

]
