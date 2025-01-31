from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView

from apps.accounts.models import Account
from apps.transactions.forms import MakeTransactionForm

from apps.transactions.utils import validate_and_process_transaction
from apps.transactions.models import Transaction


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_history.html'
    context_object_name = 'all_user_transaction'
    login_url = 'login/'
    redirect_field_name = 'next'

    def get_queryset(self, **kwargs):
        account_number = self.kwargs.get('account_number')
        user_account_data = Account.objects.get(account_number=account_number)
        all_user_transaction = Transaction.objects.filter(account=user_account_data)
        return all_user_transaction


class TransactionCreateView(LoginRequiredMixin, FormView):
    template_name = 'transactions/make_transaction.html'
    form_class = MakeTransactionForm
    login_url = 'login/'
    redirect_field_name = 'next'

    def form_valid(self, form):
        context = dict()
        account_number = self.kwargs.get('account_number')

        amount_user_entered = int(form.cleaned_data['amount'])
        transaction_type_user_select = form.cleaned_data['transaction_type']

        is_transaction_successful = validate_and_process_transaction(
            transaction_type_user_select,
            amount_user_entered,
            account_number)

        if is_transaction_successful:
            context['messages'] = ['Transaction Successful']
        else:
            context['messages'] = ['Please try again something went wrong']

        return render(form, self.template_name, context)
