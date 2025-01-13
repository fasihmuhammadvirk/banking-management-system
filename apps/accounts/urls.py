from django.urls import path
from apps.accounts.views import UserListView

urlpatterns = [

    path("accounts/", UserListView.as_view(), name='accounts-list'),

]
