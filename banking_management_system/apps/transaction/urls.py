from django.urls import path
from . import views

urlpatterns = [

    path('user_transactions/', views.show_all_transaction, name='user_transactions'),
    path('make_transaction/', views.make_transaction, name='make_transaction'),

]
