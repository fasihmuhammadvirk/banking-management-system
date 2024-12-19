from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from .models import User, Account, Bank, Transaction

@login_required
def bank_view(request):

    context = dict()
    user_account = Bank.objects.all()
    context['all_banks'] = user_account

    return render(request, 'bank/banks.html',context)
