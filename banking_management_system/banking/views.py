from django.shortcuts import render

# Create your views here.
def greet(request):
    return render(request, 'banking/greet.html')