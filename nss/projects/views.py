from .models import Project
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

#Returns a complete list of projects
class ProjectsListView(ListView):
    model = Project
##Return a pack of projects
class ProjectDetailView(DetailView):
    model = Project
