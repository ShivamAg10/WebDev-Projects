from django.shortcuts import render

# Create your views here.
def createAccount(request):
    return render(request, "accounts/createAccount.html")

def signin(request):
    return render(request, "accounts/signin.html")