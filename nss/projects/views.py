from .models import Project
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

#Returns a complete list of projects
class ProjectsListView(ListView):
    model = Project

##Return a pack of projects
class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(CreateView):
    model = Project
    fields = ['pro_name','pro_description','pro_video', 'pro_about_us', 'pro_phrase', 'pro_creation_date', 'pro_category', 'pro_location', 'pro_roles']
