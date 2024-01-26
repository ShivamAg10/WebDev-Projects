from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("login")

def invalid(request):
    return render(request, "accounts/invalid.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("psw")

        user = auth.authenticate(
            username = username,
            password = password 
        )

        if user is None:
            return redirect("invalid")
        else:
            auth.login(request, user)
            return redirect("dashboard")

    return render(request, "accounts/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pswd")

        new_user = User.objects.create(
            username = username,
        )
        new_user.set_password(password)
        new_user.save()

        return redirect("login")

    return render(request, "accounts/signup.html")