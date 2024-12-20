from django.urls import path
from . import views

urlpatterns = [

    path('user_transactions/', views.show_all_transaction, name='user_transactions'),

]
