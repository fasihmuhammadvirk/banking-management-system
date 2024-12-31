from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Bank


@login_required
def get_bank_list(request):
    bank_object_list = Bank.objects.all()
    context = {
        'bank_list': bank_object_list
    }

    return render(request, 'banks/bank_list.html', context)
