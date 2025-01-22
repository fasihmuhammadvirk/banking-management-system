from apps.accounts.models import Account
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def user_account_list_view(request):
    user_account_list = Account.objects.filter(user=request.user)
    context = {
        'user_account_list': user_account_list,
    }

    return render(request, 'accounts/user_account_list.html', context)
