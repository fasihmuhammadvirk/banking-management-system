from django.urls import path
from . import views

urlpatterns = [

    path("", views.user_login_view, name='login'),
    path("dashboard/", views.user_dashboard, name='dashboard'),
    path('logout/', views.user_logout_view, name='logout'),

]
