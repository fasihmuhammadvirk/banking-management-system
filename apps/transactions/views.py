from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from apps.transactions.forms import MakeTransactionForm

from apps.accounts.models import Account
from apps.transactions.models import Transaction
from apps.transactions.utils import get_create_transaction_context


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


class TransactionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'transactions/make_transaction.html'
    form_class = MakeTransactionForm
    login_url = 'login/'
    redirect_field_name = 'next'

    def post(self, request):
        account_number_from_query = request.GET.get('account_number')

        if request.method == "POST" and account_number_from_query:
            amount_user_entered = int(request.POST.get('amount'))
            transaction_type_user_select = request.POST.get('transaction_type')
            context = get_create_transaction_context(amount_user_entered, transaction_type_user_select)

        return render(request, self.template_name, context)
