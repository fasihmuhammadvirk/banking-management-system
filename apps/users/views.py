from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import View, RedirectView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


<<<<<<< HEAD:apps/user_dashboard/views.py
class LoginPageView(LoginView):
    template_name = 'user_dashboard/login_page.html'
    redirect_authenticated_user = True
    next_page = '/'
=======
@login_required
def user_dashboard_view(request):
    current_user = request.user
    context = {
        'username': current_user.username.upper()
    }

    return render(request, 'user/dashboard.html', context)
>>>>>>> origin/views-and-templates:apps/users/views.py


class MyLogoutView(RedirectView):

<<<<<<< HEAD:apps/user_dashboard/views.py
    def get(self, request):
        logout(request)
        return redirect('login')
=======
    if request.method == 'POST':

        entered_username = request.POST.get('username')
        entered_password = request.POST.get('password')
        is_user_authenticated = authenticate(request, username=entered_username, password=entered_password)

        if is_user_authenticated:
            login(request, is_user_authenticated)
            return redirect('dashboard')
        else:
            messages.error(request, 'Please Try Again there something went wrong with you login')

    return render(request, 'user/login_page.html')
>>>>>>> origin/views-and-templates:apps/users/views.py


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
