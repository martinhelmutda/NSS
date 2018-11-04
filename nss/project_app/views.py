from .models import project, projectImg, project, rolInfo, location, category
from .forms import CreateProjectForm, CreateRolForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from project_app.forms import formImg, formProject, formProjectAddRol, baseProjectAddRol, rol_formset
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from collections import OrderedDict
from fusioncharts import FusionCharts
from project_app import templates
from django.urls import resolve

# Create your views here.

#Returns a complete list of projects
class ProjectsListView(ListView):
    model = project


##Return a pack of projects
class ProjectDetailView(DetailView):
    model = project
    #form_class = CreateRolForm
##Creates a project with the given arguments
class ProjectCreate(CreateView):
    #model = project
    form_class = CreateProjectForm
    template_name="project_app/project_form.html"
    # success_url=reverse_lazy('project_app:project_app')
    def get_success_url(self):
        return reverse_lazy('project_app:project', args=[self.object.id, slugify(self.object.pro_name)])
        #Te manda a project_detail.html y es el projectdetailview

##Creates a project with the given arguments
class ProjectRolCreate(CreateView):
    #model = project
    form_class = CreateRolForm
    template_name="project_app/project_rol_form.html"
    #def form_valid():

    def get_success_url(self):
        print(self.kwargs['pk'])
        print(self.kwargs['slug'])
        return reverse_lazy('project_app:project', args=[self.kwargs['pk'], self.kwargs['slug']])
        #Te manda a project_detail.html y es el projectdetailview

class ProjectUpdate(UpdateView):
    model = project
    fields = ['pro_name','pro_description','pro_video', 'pro_about_us', 'pro_phrase', 'pro_creation_date', 'pro_category', 'pro_location', 'pro_roles']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('project_app:update', args=[self.object.id]) + '?ok'

class ProjectDelete(DeleteView):
    model = project
    success_url = reverse_lazy('project_app:projects')


def see_project(request):
    project_dict = {'proyecto_insert': 'PAGINA DE PROYECTO'}
    return render(request, 'project_app/project.html', context=project_dict) # app_one/proyecto.html ha ce referencia al html en templates

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


def see_project(request, p_db, r_db, i_db):
    pro_db = p_db
    rol_db = r_db
    img_db=i_db
    project_dict = {'pro_db':pro_db,'rol_db':rol_db, 'img_db':img_db}
    return render(request, 'project_app/project.html', context=project_dict) # app_one/proyecto.html ha ce referencia al html en templates

def form_project(request):
    form_pro = formProject()
    form_rol = rol_formset()
    form_img = formImg()

    if request.method == 'POST':
        form_pro=formProject(request.POST,request.FILES)
        form_rol=rol_formset(request.POST,request.FILES)
        form_img=formImg(request.POST,request.FILES)

        cantidad= request.POST.get("cantidad", "")
        if cantidad=='':
            cantidad=1
        else:
            cantidad=int(cantidad)

        if form_pro.is_valid() and form_rol.is_valid():
            #Las variables con terminacion _db son lstas que se iran al view see_project para mostrar la info de este proyecto.
            pro_db={"pro_name": str(form_pro.cleaned_data['pro_name']),"pro_description": str(form_pro.cleaned_data['pro_description']),
                    "pro_video": str(form_pro.cleaned_data['pro_video']),"pro_about_us": str(form_pro.cleaned_data['pro_about_us']),
                    "pro_phrase": str(form_pro.cleaned_data['pro_phrase']),"pro_creation_date": str(form_pro.cleaned_data['pro_creation_date']),
                    "pro_category": str(form_pro.cleaned_data['pro_category'])}
            rol_db=[]
            img_db=[]
            print("VALIDATION SUCCESS!")
            print(request.POST)
            p = project(pro_name=form_pro.cleaned_data['pro_name'],pro_description=form_pro.cleaned_data['pro_description'],
                        pro_video=form_pro.cleaned_data['pro_video'],pro_about_us=form_pro.cleaned_data['pro_about_us'],
                        pro_phrase=form_pro.cleaned_data['pro_phrase'],pro_creation_date=form_pro.cleaned_data['pro_creation_date'],
                        pro_category=form_pro.cleaned_data['pro_category'],pro_location=form_pro.cleaned_data['pro_location'])
            p.save()
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    i = projectImg(pro_img=formfile, pro = p)
                    img_url="../media/pro_img/"+str(formfile)
                    img_db.append(img_url)
                    i.save()
            for x in range(0, cantidad):
                txt='form-'+str(x)+'-rol_dropdown_name'
                name= request.POST.get(txt, "")
                if name == 'Otro':
                    txt='form-'+str(x)+'-rol_alternative_name'
                    name = request.POST.get(txt, "")
                txt='form-'+str(x)+'-rol_due_date'
                due_date= request.POST.get(txt, "")
                txt='form-'+str(x)+'-rol_amount'
                amount= request.POST.get(txt, "")
                txt='form-'+str(x)+'-rol_description'
                description= request.POST.get(txt, "")
                txt='form-'+str(x)+'-rol_location'
                loc= request.POST.get(txt, "")
                y={"rol_name": name,"rol_due_date": due_date,"rol_amount": amount,
                    "rol_description":description, "rol_location": loc}
                rol_db.append(y)
                r = rolInfo(rol_name=name,rol_due_date=due_date,rol_amount=amount,
                            rol_description=description,rol_location= location.objects.get(location=loc))

                r.save()
                p.pro_r
