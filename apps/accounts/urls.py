from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.UserList.as_view(), name='accounts'),
]
