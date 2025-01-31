from django.urls import path
from apps.accounts.views import UserListView, UserCreateView

urlpatterns = [

    path("", UserListView.as_view(), name='accounts-list'),
    path("create/", UserCreateView.as_view(), name='create-account')
]
