from django.urls import path
from apps.banks.views import bank_list_view

urlpatterns = [

    path('banks/', bank_list_view, name='banks'),

]
