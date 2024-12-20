from django.urls import path
from . import views

urlpatterns = [

    path('all_banks_list/', views.bank_view, name='all_banks_list'),

]
