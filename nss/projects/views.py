from .models import Project
from .forms import CreateProjectForm
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify

# Create your views here.

#Returns a complete list of projects
class ProjectsListView(ListView):
    model = Project

##Return a pack of projects
class ProjectDetailView(DetailView):
    model = Project

##Creates a project with the given arguments
class ProjectCreate(CreateView):
    model = Project
    form_class = CreateProjectForm
    # success_url=reverse_lazy('projects:projects')
    def get_success_url(self):
        return reverse_lazy('projects:project', args=[self.object.id, slugify(self.object.pro_name)])

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['pro_name','pro_description','pro_video', 'pro_about_us', 'pro_phrase', 'pro_creation_date', 'pro_category', 'pro_location', 'pro_roles']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('projects:update', args=[self.object.id]) + '?ok'

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:projects')
