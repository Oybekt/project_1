from django.shortcuts import render

# Create your views here.


def sign_up(request):
    return render(request, 'regitration/signup.html')


def sign_in(request):
    return render(request, 'regitration/signin.html')