from django.urls import path
from . import views

urlpatterns = [

    path( "", views.login_view , name = 'login'),
    path("accounts/", views.account_view , name = 'accounts'),
    path("greet/", views.greet, name = 'greet'),
    path('logout/', views.logout_view , name = 'logout')
]
