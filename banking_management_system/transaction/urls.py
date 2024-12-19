from django.urls import path
from . import views

urlpatterns = [

    path('transaction/', views.transcation, name='transaction'),

]