from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.transactions.utils import validate_and_process_transaction
from apps.transactions.models import Transaction


@login_required
def transactions_list_view(request, account_number):
    all_user_transaction = Transaction.objects.filter(account__account_number=account_number)

    context = {
        'all_user_transaction': all_user_transaction
    }
    return render(request, 'transactions/transaction_history.html', context)


@login_required
def transaction_create_view(request, account_number):
    context = dict()
    if request.method == "POST" and account_number:
        entered_amount = int(request.POST.get('amount'))
        selected_transaction_type = str(request.POST.get('transaction_type'))

        is_transaction_successful = validate_and_process_transaction(
            selected_transaction_type,
            entered_amount,
            account_number
        )

        if is_transaction_successful:
            context['messages'] = ['Transaction Successful']
        else:
            context['messages'] = ['Please try again something went wrong']
    else:
        context['messages'] = ['Invalid Request']

    return render(request, 'transactions/create_transaction.html', context)
