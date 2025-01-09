from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, View
from .forms import MakeTransactionForm

from ..accounts.models import Account
from .models import Transaction


class ShowTransaction(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_history.html'
    context_object_name = 'all_user_transaction'

    def get_queryset(self):
        account_number_from_query = self.request.GET.get('account_number')
        user_information = Account.objects.filter(account_number=account_number_from_query).first()
        all_user_transaction = Transaction.objects.filter(account=user_information)
        return all_user_transaction


class MakeTransaction(LoginRequiredMixin, View):
    template_name = 'transactions/do_transaction.html'
    form_class = MakeTransactionForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):

        context = dict()

        account_number_from_query = request.GET.get('account_number')

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
            context['messages'] = [f'Transaction Successful Current Balance: {user_information.balance}']

        elif transaction_type_user_select == "Deposit":
            user_information.balance += amount_user_entered
            context['messages'] = [f'Transaction Successful Current Balance: {user_information.balance}']

        else:
            context['messages'] = ["Please enter a correct amount"]

        user_information.save()

        return render(request, self.template_name, context)
