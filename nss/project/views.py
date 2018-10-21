from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project

# Create your views here.
def projects(request):
    projects = get_list_or_404(Project)
    return render(request, 'projects/projects.html', {'projects':projects})

def project(request, project_id, project_slug):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project.html', {'project':project})
