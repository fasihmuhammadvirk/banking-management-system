from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Account


@login_required
def get_user_account_list(request):
    context = dict()
    user_account_list = Account.objects.filter(user=request.user)  # because we need all user information
    context['user_account_list'] = user_account_list

    return render(request, 'accounts/user_account_list.html', context)
