from .models import project, projectImg, project, rolInfo, location, category
from .forms import CreateProjectForm
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from project_app.forms import formImg, formProject, formProjectAddRol, baseProjectAddRol, rol_formset
from django.shortcuts import render, redirect

# Create your views here.

#Returns a complete list of projects
class ProjectsListView(ListView):
    model = project

##Return a pack of projects
class ProjectDetailView(DetailView):
    model = project

##Creates a project with the given arguments
class ProjectCreate(CreateView):
    model = project
    form_class = CreateProjectForm
    # success_url=reverse_lazy('project_app:project_app')
    def get_success_url(self):
        return reverse_lazy('project_app:project', args=[self.object.id, slugify(self.object.pro_name)])

class ProjectUpdate(UpdateView):
    model = project
    fields = ['pro_name','pro_description','pro_video', 'pro_about_us', 'pro_phrase', 'pro_creation_date', 'pro_category', 'pro_location', 'pro_roles']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('project_app:update', args=[self.object.id]) + '?ok'

class ProjectDelete(DeleteView):
    model = project
    success_url = reverse_lazy('project_app:project_app')


def see_project(request):
    project_dict = {'proyecto_insert': 'PAGINA DE PROYECTO'}
    return render(request, 'project_app/project.html', context=project_dict) # app_one/proyecto.html ha ce referencia al html en templates

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
                    "rol_description":description, "rol_location": location}
                rol_db.append(y)
                r = rolInfo(rol_name=name,rol_due_date=due_date,rol_amount=amount,
                            rol_description=description,rol_location= location.objects.get(location=loc))

                r.save()
                p.pro_roles.add(r)
                print(name)

            return see_project(request, pro_db, rol_db, img_db)
        else:
            print('ERROR EN EL FORM')
    return render(request,'project_app/create_project.html',{'form_rol':form_rol, 'form_pro':form_pro, 'form_img':form_img})
