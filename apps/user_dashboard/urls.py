from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPageView.as_view(), name='login'),
    path("dashboard/", views.DashboardView.as_view(), name='dashboard'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
]
