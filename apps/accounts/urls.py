from django.urls import path
from apps.accounts.views import UserListView

urlpatterns = [

    path("", UserListView.as_view(), name='accounts-list'),

]
