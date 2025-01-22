from django.urls import path
<<<<<<< HEAD:apps/user_dashboard/urls.py
from apps.user_dashboard.views import LoginPageView, DashboardView, MyLogoutView
=======
from apps.users.views import user_dashboard_view, user_login_view, user_logout_view
>>>>>>> origin/views-and-templates:apps/users/urls.py

urlpatterns = [

    path('login/', LoginPageView.as_view(), name='login'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('logout/', MyLogoutView.as_view(), name='logout'),

]
