from django.urls import path
from . import views

urlpatterns = [

    path('banks/', views.get_bank_list, name='banks'),

]
