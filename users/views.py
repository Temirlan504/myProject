from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    # Take all user data from the login.html form
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # If there is a user inside the database, login him/her
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials"
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out"
    })

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save() # Add new user to the database
            # login(request, form)
            return HttpResponseRedirect(reverse("tasks:index"))
    else:
        form = UserCreationForm()

    return render(request, "users/register.html",{
        "form": form
    })