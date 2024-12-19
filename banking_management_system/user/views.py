from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
@login_required()
def home(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'bank/home.html' )

# Create your views here.
def login_view(request):

    # if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        is_user_autheticated = authenticate(request, username=username, password=password)

        if is_user_autheticated is not None:
            login(request, is_user_autheticated)
            return redirect('home')

        else:
            messages.error(request, 'Please Try Again there something went wrong with you login')

    return render(request, 'bank/loginpage.html')

def logout_view(request):
    logout(request)
    return redirect('login')
