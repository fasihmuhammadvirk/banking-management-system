from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import View, RedirectView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class LoginPageView(LoginView):
    template_name = 'user_dashboard/login_page.html'
    redirect_authenticated_user = True
    next_page = '/'

class MyLogoutView(RedirectView):
    def get(self, request):
        logout(request)
        return redirect('login')


class DashboardView(LoginRequiredMixin, View):
    template_name = 'user_dashboard/dashboard.html'
    login_url = 'login/'
    redirect_field_name = 'next'

    def get(self, request):
        current_user = request.user
        context = {
            'username': current_user.username.upper()
        }

        return render(request, self.template_name, context)
