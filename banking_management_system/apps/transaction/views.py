from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..account.models import Account
from .models import Transaction


# Create your views here.

@login_required
def show_all_transaction(request):
    context = dict()
    account_number_from_query = request.GET.get('q')

    if account_number_from_query:
        user_information = Account.objects.filter(account_number=account_number_from_query).first()
        all_user_transaction = Transaction.objects.filter(account=user_information)
        context['all_user_transaction'] = all_user_transaction

    return render(request, 'transaction/transaction_history.html', context)
