from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.ShowTransaction.as_view(), name='transactions'),
    path('make/transaction/', views.MakeTransaction.as_view(), name='make/transaction'),
]
