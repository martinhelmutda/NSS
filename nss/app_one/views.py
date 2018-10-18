#Last modified by César Buenfil on Oct 14,2018

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from app_one.models import category, project, rolInfo, rol, location, projectImg
from . import forms
from app_one.forms import formProject, rol_formset
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.
def index(request): #index(request, nombre):
    categories_list = category.objects.order_by('category')
    #category_dict= {'access_records': categorys_list, 'nombre':nombre}
    category_dict= {'access_records': categories_list}
    return render(request, 'app_one/index.html', context=category_dict)
    #return HttpResponse("Main page")

def see_project(request):
    project_dict = {'proyecto_insert': 'PAGINA DE PROYECTO'}
    return render(request, 'app_one/project.html', context=project_dict) # app_one/proyecto.html ha ce referencia al html en templates

def see_project(request, p_db, r_db, img_url_db):
    pro_db = p_db
    rol_db = r_db
    img_url_db=img_url_db
    project_dict = {'proyecto_insert': 'PAGINA ','pro_db':pro_db,'rol_db':rol_db, 'img_url_db':img_url_db}
    return render(request, 'app_one/project.html', context=project_dict) # app_one/proyecto.html ha ce referencia al html en templates


def form_project(request):
    form_pro = formProject()
    form_rol = rol_formset()

    if request.method == 'POST':
        form_pro=formProject(request.POST,request.FILES)
        form_rol=rol_formset(request.POST,request.FILES)


        if form_pro.is_valid() and form_rol.is_valid():
            pro_db={"pro_name": str(form_pro.cleaned_data['pro_name']),"pro_description": str(form_pro.cleaned_data['pro_description']),
                    "pro_video": str(form_pro.cleaned_data['pro_video']),"pro_about_us": str(form_pro.cleaned_data['pro_about_us']),
                    "pro_phrase": str(form_pro.cleaned_data['pro_phrase']),"pro_creation_date": str(form_pro.cleaned_data['pro_creation_date']),
                    "pro_category": str(form_pro.cleaned_data['pro_category']),"pro_img": str(form_pro.cleaned_data['pro_img'])}
            rol_db=[]
            print("VALIDATION SUCCESS!")
            print(form_pro.cleaned_data)
            print(form_rol.cleaned_data)
            for form in form_rol:
                print(form.cleaned_data)
            p = project(pro_name=form_pro.cleaned_data['pro_name'],pro_description=form_pro.cleaned_data['pro_description'],
                        pro_video=form_pro.cleaned_data['pro_video'],pro_about_us=form_pro.cleaned_data['pro_about_us'],
                        pro_phrase=form_pro.cleaned_data['pro_phrase'],pro_creation_date=form_pro.cleaned_data['pro_creation_date'],
                        pro_category=form_pro.cleaned_data['pro_category'],pro_location=form_pro.cleaned_data['pro_location'])
            p.save()
            i = projectImg(pro_img=form_pro.cleaned_data['pro_img'], pro = p)
            img_url="../media/pro_img/"+str(form_pro.cleaned_data['pro_img'])
            print(img_url)
            i.save()
            for form in form_rol:
                x={"rol_name": str(form.cleaned_data['rol_name']),"rol_due_date": str(form.cleaned_data['rol_due_date']),
                   "rol_amount": str(form.cleaned_data['rol_amount']),"rol_description": str(form.cleaned_data['rol_description']),
                   "rol_location": str(form.cleaned_data['rol_location'])}
                rol_db.append(x)
                r = rolInfo(rol_name=form.cleaned_data['rol_name'],rol_due_date=form.cleaned_data['rol_due_date'],
                            rol_amount=form.cleaned_data['rol_amount'],rol_description=form.cleaned_data['rol_description'],
                            rol_location=form.cleaned_data['rol_location'])

                r.save()
                p.pro_roles.add(r)
            #return index(request)
            return see_project(request, pro_db, rol_db, img_url)
        else:
            print('ERROR EN EL FORM')
    return render(request,'app_one/create_project.html',{'form_rol':form_rol, 'form_pro':form_pro})

# destruir después de usar
#
def form_project2(request):
    form_pro = formProject()
    form_rol = rol_formset()

    if request.method == 'POST':
        form_pro=formProject(request.POST,request.FILES)
        form_rol=rol_formset(request.POST,request.FILES)


        if form_pro.is_valid() and form_rol.is_valid():
            pro_db={"pro_name": str(form_pro.cleaned_data['pro_name']),"pro_description": str(form_pro.cleaned_data['pro_description']),
                    "pro_video": str(form_pro.cleaned_data['pro_video']),"pro_about_us": str(form_pro.cleaned_data['pro_about_us']),
                    "pro_phrase": str(form_pro.cleaned_data['pro_phrase']),"pro_creation_date": str(form_pro.cleaned_data['pro_creation_date']),
                    "pro_category": str(form_pro.cleaned_data['pro_category']),"pro_img": str(form_pro.cleaned_data['pro_img'])}
            rol_db=[]
            print("VALIDATION SUCCESS!")
            print(form_pro.cleaned_data)
            print(form_rol.cleaned_data)
            for form in form_rol:
                print(form.cleaned_data)
            p = project(pro_name=form_pro.cleaned_data['pro_name'],pro_description=form_pro.cleaned_data['pro_description'],
                        pro_video=form_pro.cleaned_data['pro_video'],pro_about_us=form_pro.cleaned_data['pro_about_us'],
                        pro_phrase=form_pro.cleaned_data['pro_phrase'],pro_creation_date=form_pro.cleaned_data['pro_creation_date'],
                        pro_category=form_pro.cleaned_data['pro_category'],pro_location=form_pro.cleaned_data['pro_location'])
            p.save()
            i = projectImg(pro_img=form_pro.cleaned_data['pro_img'], pro = p)
            img_url="../media/pro_img/"+str(form_pro.cleaned_data['pro_img'])
            print(img_url)
            i.save()
            for form in form_rol:
                x={"rol_name": str(form.cleaned_data['rol_name']),"rol_due_date": str(form.cleaned_data['rol_due_date']),
                   "rol_amount": str(form.cleaned_data['rol_amount']),"rol_description": str(form.cleaned_data['rol_description']),
                   "rol_location": str(form.cleaned_data['rol_location'])}
                rol_db.append(x)
                r = rolInfo(rol_name=form.cleaned_data['rol_name'],rol_due_date=form.cleaned_data['rol_due_date'],
                            rol_amount=form.cleaned_data['rol_amount'],rol_description=form.cleaned_data['rol_description'],
                            rol_location=form.cleaned_data['rol_location'])

                r.save()
                p.pro_roles.add(r)
            #return index(request)
            return see_project(request, pro_db, rol_db, img_url)
        else:
            print('ERROR EN EL FORM')
    return render(request,'app_one/alt_create_project.html',{'form_rol':form_rol, 'form_pro':form_pro})

#
# destruir después de usar

"""
def form_project(request):
    form = forms.formProject()

    if request.method == 'POST':
        form = forms.formProject(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            #print("NAME: "+form.cleaned_data['name'])
            #recipients=[]
            #if ProConfirmation:
                #print("Enviar email!")
            #    send_mail('subject', 'message', 'A01421467@itesm.mx', 'angieguemes@gmail.com')
            #    return HttpResponseRedirect('/thanks/')

    return render(request,'app_one/createPro.html',{'form':form})
"""
