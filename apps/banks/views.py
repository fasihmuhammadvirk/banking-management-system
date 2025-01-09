from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Bank


class BankView(LoginRequiredMixin, ListView):
    model = Bank
    template_name = 'banks/bank_list.html'
    context_object_name = 'bank_list'
    queryset = Bank.objects.all()
