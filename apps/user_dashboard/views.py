from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


@login_required
def user_dashboard(request):
    current_user = request.user
    context = {
        'username': current_user.username.upper()
    }
    return render(request, 'user_dashboard/dashboard.html', context)


# Create your views here.
def user_login_view(request):
    # checking if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        entered_username = request.POST.get('username')
        entered_password = request.POST.get('password')
        is_user_authenticated = authenticate(request, username=entered_username, password=entered_password)

        if is_user_authenticated:
            login(request, is_user_authenticated)
            return redirect('dashboard')
        else:
            messages.error(request, 'Please Try Again there something went wrong with you login')

    return render(request, 'user_dashboard/login_page.html')


def user_logout_view(request):
    logout(request)
    return redirect('login')
