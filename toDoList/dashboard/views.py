from django.shortcuts import render, redirect
from .models import List
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="login")
def deleteList(request, id):
    lists = List.objects.get(id = id)
    lists.delete()
    # parameters = {
    #     "lists" : lists,
    # }
    return redirect("dashboard")

@login_required(login_url="login")
def editList(request, id):
    lists = List.objects.get(id = id)

    if request.method == "POST":
        todo = request.POST.get("todo")

        lists.todo = todo
        lists.save()

        return redirect("dashboard")

    parameters = {
        "lists" : lists
    }

    return render(request, "edit.html", parameters)

@login_required(login_url="login")
def dashboard(request):

    #read starts
    user = request.user
    lists = List.objects.filter(user = user)

    parameters = {
        "list" : lists,
    }
    #read ends

    # create starts
    if request.method == "POST":
        todo = request.POST.get("todo")
        date = request.POST.get("date")

        new_todo = List.objects.create(
            user = user,
            todo = todo,
            date = date
        )
        new_todo.save()

        return redirect("dashboard")
    #create ends

    return render(request, "index.html", parameters)