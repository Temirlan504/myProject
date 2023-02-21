from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import NewTaskForm
from django.views.generic.edit import UpdateView

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    tasks = Task.objects.filter(user=request.user.id) # User-specific tasks

    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                user_id = request.user.id,
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description']
            )
            form = NewTaskForm()

    else:
        form = NewTaskForm()

    return render(request, "tasks/add.html", {
        "form": form
    })

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return HttpResponseRedirect(reverse("tasks:index"))

class UpdateTaskView(UpdateView):
    model = Task
    fields = ["title", "description"]
    template_name = 'tasks/update.html'
    success_url = reverse_lazy("tasks:index")