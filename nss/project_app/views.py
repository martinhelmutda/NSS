"""
Last modified: ANgélica Güemes
date: November 11
Time: 11:24
"""
from .models import project, projectImg, project, rolInfo, state,city, category,subcategory, project_rol, user_project, status
from .forms import CreateProjectForm, CreateRolForm, CreateGroupForm
from django.utils import timezone
from django.contrib.auth.models import User
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
from django.template.loader import render_to_string

# Create your views here.
#Returns a complete list of projects
class ProjectsListView(ListView):
    model = project
    paginated_by=2
    template_name = "project_app/project_list.html"
    def get_context_data(self, **kwargs):
        context = super(ProjectsListView, self).get_context_data(**kwargs)
        context['integrantes'] = user_project.objects.filter(up_user=self.request.user) #print(context['user_project']) #print('id projecto', context['user_project'])
        print(context['integrantes'])
        context['project_list'] = project.objects.filter( pro_user=self.request.user)
        return context


##Return a pack of projects
class ProjectDetailView(DetailView):
    model = project
"""
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        id_Project= self.kwargs['pk']

        if self.request.user.is_anonymous:
            print("BUUU")
        else:
            context['user_project'] = user_project.objects.filter(up_user= self.request.user, up_project = self.object.id)
            print(context['user_project'])
            # total_likes = project.objects.filter(likes=self.request.user).count()
        context['owner_project'] = project.objects.filter(id=self.object.id) #print(context['user_project']) #print('id projecto', context['user_project'])
        aceptada = status.objects.get(status='aceptada')
        context['integrantes']= user_project.objects.filter(up_project=id_Project, up_status=aceptada)
        is_liked = True
        context['is_liked']= is_liked
        # context['total_likes']= total_likes
        #    if post.likes.filter(id=request.user.id).exists():
            #    is_liked = True

        return context
"""
class ApplicationsDetailView(DetailView):
    model = project
    paginated_by=2
    template_name="project_app/application_list.html"
    def get_context_data(self, **kwargs):
        context = super(ApplicationsDetailView, self).get_context_data(**kwargs)
        id_Project= self.kwargs['pk']
        context['applications'] =  user_project.objects.filter(up_project=id_Project)#filter(up_project=self.object.id)
        context['applications_rols'] =  project_rol.objects.filter(pro=id_Project)#filter(up_project=self.object.id)
        aceptada = status.objects.get(status='aceptada')
        context['integrantes']= user_project.objects.filter(up_project=id_Project, up_status=aceptada).order_by('up_rolInfo', 'up_user')
        for rol in context['applications_rols']:
            if rol.rol.rol_name == 'Otro':
                context[rol.rol.rol_name_other]= user_project.objects.filter(up_project=id_Project, up_rolInfo= rol.rol)
            else:
                context[rol.rol.rol_name_other]= user_project.objects.filter(up_project=id_Project, up_rolInfo= rol.rol)
        context['project_name'] =  project.objects.get(id=id_Project)#filter(up_project=self.object.id)
        return context


def change_user_project_status(request):
    idRol = request.GET.get('idRol', None)
    status1 = request.GET.get('status1', None)
    print("STATUS!........", status1)
    idUser = request.GET.get('idUser', None)
    idProject = request.GET.get('idProject', None)#print('id rol',idRol)#print('status1',status1)#print('idUser',idUser)#print('idProject',idProject)
    pro = project.objects.get(id=idProject)#get project
    rol = rolInfo.objects.get(id=idRol)#get rolInf
    if status1 == 'No_enviada':
        stat = status.objects.get(status='enviada')#get up Status
        up = user_project(up_project= pro,up_user=request.user, up_rolInfo=rol, up_status= stat)
        up.save()#print('cooool')
    else:
        print('no cooool')
        stat = status.objects.get(status=status1)#get up Status
        up = user_project.objects.get(up_project= pro ,up_user=request.user, up_rolInfo=rol, up_status=stat)
        #print(up.up_status)
        if up.up_status.status == 'aceptada':
            stat = status.objects.get(status='cancelada')
        elif up.up_status.status == 'cancelada':
            stat = status.objects.get(status='enviada')
        elif up.up_status.status == 'enviada':
            stat = status.objects.get(status='cancelada')
        elif up.up_status.status == 'rechazada':
            stat = status.objects.get(status='enviada')
        elif up.up_status.status == 'renuncia':
            stat = status.objects.get(status='enviada')
        up.up_status= stat
        up.save()
    data = {
        'is_taken': rolInfo.objects.filter(id=idRol).exists()
    }
    return JsonResponse(data)

def button_text(request):
    print("ENTRO")
    idProject = request.GET.get('idProject', None)
    pro_object = project.objects.get(id=idProject)
    roles = user_project.objects.filter(up_project=pro_object, up_user=request.user)
    roles_todos = user_project.objects.filter(up_project=pro_object)
    status1 = status.objects.get(status='aceptada')
    dict =	{}
    dictStatus={}
    dictRestantes={}

    for x in roles: #print(x.up_rolInfo.id)#print(x.up_rolInfo)#print(x.up_status.status_text)
        dict[x.up_rolInfo.id] = x.up_status.status_text
        dictStatus[x.up_rolInfo.id] = x.up_status.status
    for x in roles_todos:
        dictRestantes[x.up_rolInfo.id] = x.up_rolInfo.rol_amount - user_project.objects.filter(up_project= pro_object, up_status=status1, up_rolInfo=x.up_rolInfo).count()
    print(dictRestantes)
    data = {
        'dict': dict,
        'dictStatus': dictStatus,
        'dictRestantes': dictRestantes,
    }
    return JsonResponse(data)


##Creates a project with the given arguments
@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class GroupCreate(CreateView):
    #model = project
    form_class = CreateGroupForm
    template_name="project_app/group_form.html"
    def form_valid(self, form):
        user_form = form.save(commit=False)
        user_form.pro_user = self.request.user
        user_form.pro_group=True
        return super(GroupCreate, self).form_valid(form)
    def get_success_url(self):
        #print(cities)
        print(self.object)
        return reverse_lazy('project_app:project', args=[self.object.id, slugify(self.object.pro_name)])
        #Te manda a project_detail.html y es el projectdetailview

@method_decorator(login_required, name='dispatch')
def like_post(request):
    post = get_object_or_404(project, id= request.POST.get('post_id'))
    #post = get_object_or_404(project, id= request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked= True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def load_cities(request):
    country_id =  request.GET.get('country')
    cities = city.objects.filter(state=country_id).order_by('city')#print(cities)
    return render(request, 'project_app/city_dropdown_list_options.html', {'cities': cities})

def load_subcategories(request):
    country_id =  request.GET.get('category')
    subcategories = subcategory.objects.filter(category=country_id)#.order_by('subcategory') print(subcategories)
    return render(request, 'project_app/subcategory_dropdown_list_options.html', {'subcategories': subcategories})

def accept(request):
    #Get de la funcion de AJAX
    idUser = request.GET.get('idUser', None)
    idProject = request.GET.get('idProject', None)
    idRol = request.GET.get('idRol', None)
    #Get de la base de datos
    user1 = User.objects.get(id=idUser)
    rol1= rolInfo.objects.get(id=idRol)
    status1 = status.objects.get(status='aceptada')
    #Cambio su estado a ACEPTADO
    application = user_project.objects.get(up_project= idProject, up_user=user1, up_rolInfo=rol1)
    application.up_status = status1
    application.save()
    #Resto uno a rol_amount
    x = rol1.rol_amount - user_project.objects.filter(up_project= idProject, up_status=status1, up_rolInfo=rol1).count()
    print(x)
    data = {
        'cantidad': x,
    }
    return JsonResponse(data)

def delete(request):
    idUser = request.GET.get('idUser', None)
    idProject = request.GET.get('idProject', None)
    idRol = request.GET.get('idRol', None)
    user1 = User.objects.get(id=idUser)
    rol1= rolInfo.objects.get(id=idRol)
    application = user_project.objects.get(up_project= idProject, up_user=user1, up_rolInfo=rol1)
    status1 = status.objects.get(status='rechazada')
    application.up_status = status1
    application.save()
    data = {
        'is_taken': 'application'
    }
    return JsonResponse(data)

##Creates a project with the given arguments
class ProjectRolCreate(CreateView):
    #model = project
    form_class = CreateRolForm
    template_name="project_app/project_rol_form.html"
    def get_success_url(self):
        pro_temp = project.objects.get(id=self.kwargs['pk'])
        if pro_temp.pro_group == False:
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

def DataRepGoogle(request):
    idProject = request.GET.get('idProject', None)
    print("id Pro ",idProject)
    pieData=[]
    pro1 = project.objects.get(id=idProject)
    rols = project_rol.objects.filter(pro=pro1)
    for rol in rols: ##Por cada rol que haya en el proyecto
        #Busco los integrantes que ya estan aceptados en el proyecto con este rol1
        r = rolInfo.objects.get(rol_name=rol.rol.rol_name)
        s= status.objects.get(status='aceptada')
        cantidad = user_project.objects.filter(up_rolInfo=r,up_project=pro1, up_status=s).count()
        pieData.append([rol.rol.rol_name, cantidad])
        print("1: ",rol.rol.rol_name)
        print("2: ", cantidad)

    data = {
        'pieData': pieData,
    }
    return JsonResponse(data)

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
