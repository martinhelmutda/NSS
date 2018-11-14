"""
Last modified: ANgélica Güemes
date: November 11
Time: 11:24
"""
from .models import project, projectImg, project, rolInfo, state,city, category,subcategory, project_rol, user_project, status
from .forms import CreateProjectForm, CreateRolForm, CreateGroupForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from collections import OrderedDict
from fusioncharts import FusionCharts
from project_app import templates
from django.urls import resolve
from account_app.models import Profile
from django.http import JsonResponse
# Create your views here.
#Returns a complete list of projects
class ProjectsListView(ListView):
    model = project
    paginated_by=2
    template_name = "project_app/project_list.html"
    def get_queryset(self):
        queryset =  project.objects.filter(pro_group=False, pro_user=self.request.user)
        return queryset

class GroupsListView(ListView):
    model = project
    paginated_by=2
    template_name="project_app/group_list.html"
    def get_queryset(self):
        queryset =  project.objects.filter(pro_group=True, pro_user=self.request.user)
        return queryset

##Return a pack of projects
class ProjectDetailView(DetailView):
    model = project
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['user_project'] = user_project.objects.filter(up_user= self.request.user, up_project = self.object.id)
        print(context['user_project'])
        context['owner_project'] = project.objects.filter(id=self.object.id) #print(context['user_project']) #print('id projecto', context['user_project'])
        return context

def change_user_project_status(request):
    idRol = request.GET.get('idRol', None)
    status1 = request.GET.get('status1', None)
    idUser = request.GET.get('idUser', None)
    idProject = request.GET.get('idProject', None)
    #print('id rol',idRol)
    #print('status1',status1)
    #print('idUser',idUser)
    #print('idProject',idProject)
    if status1 == 'No_enviada':
        print('status',status1)
        #get project
        pro = project.objects.get(id=idProject)
        #get rolInf
        rol = rolInfo.objects.get(id=idRol)
        print(rol)
        #get up Status
        stat = status.objects.get(status='enviada')
        up = user_project(up_project= pro,up_user=request.user, up_rolInfo=rol, up_status= stat)
        up.save()
        print('cooool')
    else:
        print('no cooool')
        #row = user_project.objects.get(up_project= idProject,up_user=request.user, up_rolInfo=idRol)
        #print(row.up_status)

    data = {
        'is_taken': rolInfo.objects.filter(id=idRol).exists()
    }
    return JsonResponse(data)

##Creates a project with the given arguments
class ProjectCreate(CreateView):
    #model = project
    form_class = CreateProjectForm
    template_name="project_app/project_form.html"
    def form_valid(self, form):
        user_form = form.save(commit=False)
        user_form.pro_user = self.request.user
        return super(ProjectCreate, self).form_valid(form)
    def get_success_url(self):
        print(self.object)
        return reverse_lazy('project_app:project', args=[self.object.id, slugify(self.object.pro_name)])
        #Te manda a project_detail.html y es el projectdetailview



class GroupCreate(CreateView):
    #model = project
    form_class = CreateGroupForm
    template_name="project_app/group_form.html"
    def form_valid(self, form):
        user_form = form.save(commit=False)
        user_form.pro_user = self.request.user
        return super(GroupCreate, self).form_valid(form)
    def get_success_url(self):
        #print(cities)
        print(self.object)
        return reverse_lazy('project_app:project', args=[self.object.id, slugify(self.object.pro_name)])
        #Te manda a project_detail.html y es el projectdetailview

def load_cities(request):
    country_id =  request.GET.get('country')
    cities = city.objects.filter(state=country_id).order_by('city')#print(cities)
    return render(request, 'project_app/city_dropdown_list_options.html', {'cities': cities})

def load_subcategories(request):
    country_id =  request.GET.get('category')
    subcategories = subcategory.objects.filter(category=country_id)#.order_by('subcategory') print(subcategories)
    return render(request, 'project_app/subcategory_dropdown_list_options.html', {'subcategories': subcategories})

##Creates a project with the given arguments
class ProjectRolCreate(CreateView):
    #model = project
    form_class = CreateRolForm
    template_name="project_app/project_rol_form.html"
    def get_success_url(self):
        pro_temp = project.objects.get(id=self.kwargs['pk'])
        project_rol.objects.create(pro =pro_temp , rol=self.object )
        return reverse_lazy('project_app:project', args=[self.kwargs['pk'], self.kwargs['slug']])
        #Te manda a project_detail.html y es el projectdetailview

class ProjectUpdate(UpdateView):
    model = project
    fields = ['pro_name','pro_description','pro_video', 'pro_about_us', 'pro_phrase', 'pro_creation_date', 'pro_category', 'pro_subcategory', 'pro_city', 'pro_state']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('project_app:update', args=[self.object.id]) + '?ok'

class ProjectDelete(DeleteView):
    model = project
    success_url = reverse_lazy('project_app:projects')

def DataRep(request):
    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Proyectos por categoría"
    chartConfig["subCaption"] = ""
    chartConfig["xAxisName"] = "Categoría"
    chartConfig["yAxisName"] = "Cantidad"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs of data
    chartData = OrderedDict()
    chartData["Música"] = 5
    chartData["Arte"] = 2
    chartData["Teatro"] = 8
    chartData["Computación"] = 6
    chartData["Literatura"] = 1
    chartData["Cocina"] = 3
    chartData["Deportes"] = 7
    chartData["Idiomas"] = 9

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)

    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
    pie2d = FusionCharts("pie2d", "ex1", '700', '400', "myFirstchart", "json", dataSource )

    return render(request,  'project_app/data.html', {'output': column2D.render(), 'output2': pie2d.render()})
    #project_dict = {'proyecto_insert': 'PAGINA DE PROYECTO'}
    #return render(request, 'project_app/data.html', context=project_dict) # app_one/proyecto.html ha ce referencia al html en templates
