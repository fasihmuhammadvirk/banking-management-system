from django.shortcuts import render
from .models import Account
# Create your views here.

@login_required
def account_view(request):

    context = dict()
    user_account = Account.objects.filter(user = request.user)
    context['all_accounts'] = user_account

    return render(request, 'bank/accounts.html',context)
