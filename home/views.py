from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, "index.html")


def loginuser(request):
    if request.method == "POST":
        # check the credential that user input in sign in form
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return render(request, "login.html")
    return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return redirect("login")
