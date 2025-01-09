from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View, RedirectView
from .forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginPageView(View):
    template_name = 'user_dashboard/login_page.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                context = {
                    'username': user.username
                }
                return redirect('dashboard')

        messages.error(request, 'Please Try Again there something went wrong with you login')

        return render(request, self.template_name)


class MyLogoutView(RedirectView):

    def get(self, request):
        logout(request)
        return redirect('login')


class DashboardView(LoginRequiredMixin, View):
    template_name = 'user_dashboard/dashboard.html'

    def get(self, request):
        current_user = request.user
        context = {
            'username': current_user.username.upper()
        }

        return render(request, self.template_name, context)
