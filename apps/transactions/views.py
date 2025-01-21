from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from apps.transactions.forms import MakeTransactionForm

from apps.accounts.models import Account
from apps.transactions.models import Transaction
from apps.transactions.utils import update_user_balance_and_create_transaction_history


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_history.html'
    context_object_name = 'all_user_transaction'
    login_url = 'login/'
    redirect_field_name = 'next'

    def get_queryset(self):
        account_number_from_query = self.request.GET.get('account_number')
        user_account_data = Account.objects.filter(account_number=account_number_from_query).first()
        all_user_transaction = Transaction.objects.filter(account=user_account_data)
        return all_user_transaction


class TransactionCreateView(LoginRequiredMixin, FormView):
    template_name = 'transactions/make_transaction.html'
    form_class = MakeTransactionForm
    login_url = 'login/'
    redirect_field_name = 'next'

    def form_valid(self, form):
        context = dict()
        account_number_from_query = self.request.GET.get('account_number')

        if account_number_from_query:
            amount_user_entered = int(form.cleaned_data['amount'])
            transaction_type_user_select = form.cleaned_data['transaction_type']

            is_transaction_successful = update_user_balance_and_create_transaction_history(
                transaction_type_user_select,
                amount_user_entered,
                account_number_from_query)

            if is_transaction_successful:
                context = ['Transaction Successful']
            else:
                context = ['Please try again something went wrong']
        return render(form, self.template_name, context)
