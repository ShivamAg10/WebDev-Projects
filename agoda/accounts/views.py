from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def createAccount(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if password == cpassword:
            new_user = User.objects.create(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email
            )

            new_user.set_password(password)
            new_user.save()

            return redirect("/accounts/signin")

        else:
            messages.error(request, "Maybe Password and Confirm Password is not same")

    return render(request, "accounts/createAccount.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(
            username = username,
            password = password
        )

        if user is None:
            messages.error(request, "Maybe you have not created account....")
        else:
            auth.login(request, user)
            return redirect("/")

    return render(request, "accounts/signin.html")

def logout(request):
    auth.logout(request)
    return redirect("signin")