from django.urls import path
from apps.users.views import LoginPageView, DashboardView, MyLogoutView

urlpatterns = [

    path('login/', LoginPageView.as_view(), name='login'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('logout/', MyLogoutView.as_view(), name='logout'),

]
