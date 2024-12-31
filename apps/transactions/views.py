from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..accounts.models import Account
from .models import Transaction


@login_required
def show_all_transactions(request):
    context = dict()
    account_number_from_query = request.GET.get('account_number')

    if account_number_from_query:
        user_information = Account.objects.filter(account_number=account_number_from_query).first()
        all_user_transaction = Transaction.objects.filter(account=user_information)
        context['all_user_transaction'] = all_user_transaction

    return render(request, 'transactions/transaction_history.html', context)


@login_required
def make_transaction(request):
    context = dict()
    account_number_from_query = request.GET.get('account_number')

    if request.method == "POST" and account_number_from_query:
        amount_user_entered = int(request.POST.get('amount'))
        transaction_type_user_select = request.POST.get('transaction_type')
        user_information = Account.objects.filter(account_number=account_number_from_query).first()

        Transaction.objects.create(
            account=user_information,
            amount=amount_user_entered,
            transaction_type=transaction_type_user_select,
        )

        if transaction_type_user_select == "Withdrawal" and amount_user_entered <= user_information.balance:
            user_information.balance -= amount_user_entered
            context['messages'] = [f"You have Withdrawal {amount_user_entered} "
                                   f"your current balance is {user_information.balance}"]

        elif transaction_type_user_select == "Deposit":
            user_information.balance += amount_user_entered
            context['messages'] = [f"You have Deposit {amount_user_entered} "
                                   f"your current balance is {user_information.balance}"]

        else:
            context['messages'] = ["Please enter a correct amount"]

        user_information.save()

    return render(request, 'transactions/do_transaction.html', context)
