from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.banks.models import Bank


@login_required
def bank_list_view(request):
    bank_object_list = Bank.objects.all()
    context = {
        'bank_list': bank_object_list
    }

    return render(request, 'banks/bank_list.html', context)
