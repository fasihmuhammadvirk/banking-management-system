from django.urls import path
from . import views

urlpatterns = [

    path('user_transactions/', views.transcation, name='user_transactions'),

]