from .models import Account
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserList(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'accounts/user_account_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_account_list'] = Account.objects.filter(user=self.request.user)

        return context
