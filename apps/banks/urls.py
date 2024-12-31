from django.urls import path
from . import views

urlpatterns = [

    path('bank_list/', views.get_bank_list, name='bank_list'),

]
