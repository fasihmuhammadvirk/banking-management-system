from apps.transactions.models import Transaction
from django.forms import ModelForm


class MakeTransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type']
