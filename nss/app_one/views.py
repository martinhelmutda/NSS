#Last modified by César Buenfil on Oct 14,2018

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from app_one.models import category, project, rolInfo, rol, location, projectImg
from . import forms
from app_one.forms import formProject, rol_formset, UserForm, UserProfileInfoForm
from django.urls import reverse
from urllib.parse import urlencode

#login
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): #index(request, nombre):
    categories_list = category.objects.order_by('category')
    #category_dict= {'access_records': categorys_list, 'nombre':nombre}
    category_dict= {'access_records': categories_list}
    return render(request, 'app_one/index.html', context=category_dict)
    #return HttpResponse("Main page")

@login_required
def special(request):
    return HttpResponse("You are logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'app_one/registration.html',{'user_form':user_form,
                                                       'profile_form':profile_form,
                                                       'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not Active")

        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request,'app_one/login.html',{})

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
    #form_rol=rol_formset()
    context={
        'form_pro':form_pro,
        #'form_rol':form_rol,
    }

    if request.method == 'POST':
        form_pro=formProject(request.POST)
        #form_rol=rol_formset(request.POST,request.FILES)

        if form_pro.is_valid() and form_rol.is_valid():
            print("VALIDATION SUCCESS!")
            print(form_pro.cleaned_data)
            #print(form_rol.cleaned_data)
            #for form in form_rol:
                #print(form.cleaned_data)
            p = project(pro_name=form_pro.cleaned_data['pro_name'],pro_description=form_pro.cleaned_data['pro_description'],
                        pro_video=form_pro.cleaned_data['pro_video'],pro_about_us=form_pro.cleaned_data['pro_about_us'],
                        pro_phrase=form_pro.cleaned_data['pro_phrase'],pro_creation_date=form_pro.cleaned_data['pro_creation_date'],
                        pro_category=form_pro.cleaned_data['pro_category'],pro_location=form_pro.cleaned_data['pro_location'],
                        pro_img=form_pro.cleaned_data['pro_category'])
            p.save()
            #for form in form_rol:
                #r = rolInfo(rol=form.cleaned_data['rolNombre'],fechaLimite=form.cleaned_data['rolFechaLimite'],
                        #    rolcantidad=form.cleaned_data['rolCantidad'],rolDescripcion=form.cleaned_data['rolDescripcion'],
                        #    rolLocation=form.cleaned_data['rolLocation'])
                #r.save()
                #p.proRoles.add(r)
            return index(request)
        else:
            print('ERROR EN EL FORM')
    return render(request,'app_one/alt_create_project.html',context)

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
