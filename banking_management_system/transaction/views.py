from django.shortcuts import render
from ..account.models import Account
from .models import Transaction
# Create your views here.

def transcation(request):

    context = dict()
    q = request.GET.get('q')

    if q:
        user_to_transact = Account.objects.filter(account_number = q).first()
        transaction = Transaction.objects.filter(account = user_to_transact)
        context['transaction'] = transaction

    return render(request, 'bank/transaction.html',context)
