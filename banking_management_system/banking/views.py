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
    context = dict()

    if request.user.is_authenticated:
        return redirect('accounts')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            mymessage = ["User doesnot exit"]
            context['messages'] = mymessage
            return render(request, 'banking/loginpage.html', context)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts')
        else:
            messages.error(request, 'Incorrect Email or Password')

    return render(request, 'banking/loginpage.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def bank_view(request):
    pass

@login_required
def account_view(request):
    return render(request, 'banking/greet.html')