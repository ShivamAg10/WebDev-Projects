from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user = request.user
    parameters = {
        user : user,
    }
    return render(request, "index.html", parameters)