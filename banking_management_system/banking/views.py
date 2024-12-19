from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def greet(request):
    context = dict()
    users = User.objects.all()

    context['users'] = users

    return render(request, 'banking/greet.html' , context)


def login_view(request):

    # if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('accounts')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        is_user_autheticated = authenticate(request, username=username, password=password)

        if is_user_autheticated is not None:
            login(request, is_user_autheticated)
            return redirect('accounts')

        else:
            messages.error(request, 'Please Try Again there something went wrong with you login')

    return render(request, 'banking/loginpage.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def bank_view(request):
    pass

@login_required
def account_view(request):
    return render(request, 'banking/greet.html')