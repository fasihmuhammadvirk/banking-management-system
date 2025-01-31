from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from apps.banks.models import Bank


class BankListView(LoginRequiredMixin, ListView):
    model = Bank
    template_name = 'banks/bank_list.html'
    context_object_name = 'bank_list'
    queryset = Bank.objects.all()
    login_url = 'login/'
    redirect_field_name = 'next'

class BankCreateView(LoginRequiredMixin, CreateView):
    model = Bank
    fields = ['name', 'branch', 'is_islamic']
    template_name = 'banks/create_bank.html'
    success_url = "/"
