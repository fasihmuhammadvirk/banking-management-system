from django.urls import path
from . import views
from ..transaction.urls import urlpatterns

urlpatterns = [

    path("", views.login_view, name='login'),
    path("home/", views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),

]