from django.shortcuts import render
from .models import Account
# Create your views here.

def account_view(request):

    context = dict()
    user_account = Account.objects.filter(user = request.user)
    context['all_accounts'] = user_account

    return render(request, 'account/accounts.html',context)
