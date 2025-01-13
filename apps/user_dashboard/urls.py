from django.urls import path
from apps.user_dashboard.views import user_dashboard_view, user_login_view, user_logout_view

urlpatterns = [

    path("", user_login_view, name='login'),
    path("dashboard/", user_dashboard_view, name='dashboard'),
    path('logout/', user_logout_view, name='logout'),

]
ß
