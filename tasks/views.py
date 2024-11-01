from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import TaskForm
from .models import Task


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    return render(request, "tasks/task_create.html", {"form": form})


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    return render(request, "tasks/my_tasks.html", {"tasks": tasks})

@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, assignee=request.user)
    if request.method == "POST":
        task.is_completed = not task.is_completed
        task.save()
        return redirect("show_my_tasks")
    return HttpResponseForbidden("You are not allowed to edit tasks")
