from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    tasks = Task.objects.filter(user=request.user.id) # User-specific tasks

    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        Task.objects.create(
            user_id = request.user.id,
            title = request.POST["title"],
            description = request.POST["description"]
        )
    return render(request, "tasks/add.html")

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return HttpResponseRedirect(reverse("tasks:index"))