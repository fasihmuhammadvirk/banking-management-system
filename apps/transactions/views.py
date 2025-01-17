from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.transactions.utils import get_create_transaction_context
from apps.transactions.models import Transaction
from apps.accounts.models import Account


@login_required
def transactions_list_view(request):
    context = dict()
    account_number_from_query = request.GET.get('account_number')

    if account_number_from_query:
        user_information = Account.objects.filter(account_number=account_number_from_query).first()
        all_user_transaction = Transaction.objects.filter(account=user_information)
        context['all_user_transaction'] = all_user_transaction

    return render(request, 'transactions/transaction_history.html', context)


@login_required
def transaction_create_view(request):
    account_number_from_query = request.GET.get('account_number')

    if request.method == "POST" and account_number_from_query:
        amount_user_entered = int(request.POST.get('amount'))
        transaction_type_user_select = request.POST.get('transaction_type')

        context = get_create_transaction_context(amount_user_entered, transaction_type_user_select)

    return render(request, 'transactions/create_transaction.html', context)


