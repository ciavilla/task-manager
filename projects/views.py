from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm


# Create your views here.
@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    return render(
        request, "projects/project_list.html", {"projects": projects}
    )


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = project.tasks.all()
    return render(
        request,
        "projects/project_detail.html",
        {"project": project, "tasks": tasks},
    )


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    return render(request, "projects/project_create.html", {"form": form})
