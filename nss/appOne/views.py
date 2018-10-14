from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from appOne.models import area, proyecto, rolInfo, rol, location, proyectoImagen
from . import forms
from appOne.forms import formProyecto, rolesFormset
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.
def index(request): #index(request, nombre):
    areas_list = area.objects.order_by('area')
    #area_dict= {'access_records': areas_list, 'nombre':nombre}
    area_dict= {'access_records': areas_list}
    return render(request, 'appOne/index.html', context=area_dict)
    #return HttpResponse("Main page")

def verProyecto(request):
    proyectodict = {'proyecto_insert': 'PAGINA DE PROYECTO'}
    return render(request, 'appOne/proyecto.html', context=proyectodict) # appOne/proyecto.html ha ce referencia al html en templates

def ver_proyecto(request, p_db, r_db):
    pro_db = p_db
    rol_db=r_db
    proyectodict = {'proyecto_insert': 'PAGINA ','pro_db':pro_db,'rol_db':rol_db}
    return render(request, 'appOne/proyecto.html', context=proyectodict) # appOne/proyecto.html ha ce referencia al html en templates


def FormProyecto(request):
    formPro = formProyecto()
    formRol=rolesFormset()

    if request.method == 'POST':
        formPro=formProyecto(request.POST,request.FILES)
        formRol=rolesFormset(request.POST,request.FILES)

        if formPro.is_valid() and formRol.is_valid():
            pro_db={ "pro_nombre": str(formPro.cleaned_data['proName']),"pro_descripcion": str(formPro.cleaned_data['proDescription']),
                    "pro_video": str(formPro.cleaned_data['proVideo']),"pro_nosotros": str(formPro.cleaned_data['proAboutUs']),
                    "pro_frase": str(formPro.cleaned_data['proFrase']),"pro_fecha_creacion": str(formPro.cleaned_data['proCreationDate']),
                    "pro_categoria": str(formPro.cleaned_data['proArea']),"pro_imagen": str(formPro.cleaned_data['proImage'])}
            rol_db=[]
            print("VALIDATION SUCCESS!")
            print(formPro.cleaned_data)
            print(formRol.cleaned_data)
            for form in formRol:
                print(form.cleaned_data)
            p = proyecto(proName=formPro.cleaned_data['proName'],proDescription=formPro.cleaned_data['proDescription'],
                        proVideo=formPro.cleaned_data['proVideo'],proAboutUs=formPro.cleaned_data['proAboutUs'],
                        proFrase=formPro.cleaned_data['proFrase'],proCreationDate=formPro.cleaned_data['proCreationDate'],
                        proArea=formPro.cleaned_data['proArea'],proLocation=formPro.cleaned_data['proLocation'])
            p.save()
            i = proyectoImagen(proImage=formPro.cleaned_data['proImage'], proyecto=p)
            i.save()
            for form in formRol:
                x={"rol_nombre": str(form.cleaned_data['rolNombre']),"rol_fecha_limite": str(form.cleaned_data['rolFechaLimite']),
                        "rol_cantidad": str(form.cleaned_data['rolCantidad']),"rol_descripcion": str(form.cleaned_data['rolDescripcion']),
                        "rol_ubicacion": str(form.cleaned_data['rolLocation'])}
                rol_db.append(x)
                r = rolInfo(rol=form.cleaned_data['rolNombre'],fechaLimite=form.cleaned_data['rolFechaLimite'],
                            rolcantidad=form.cleaned_data['rolCantidad'],rolDescripcion=form.cleaned_data['rolDescripcion'],
                            rolLocation=form.cleaned_data['rolLocation'])

                r.save()
                p.proRoles.add(r)
            #return index(request)
            return ver_proyecto(request, pro_db, rol_db)
        else:
            print('ERROR EN EL FORM')
    return render(request,'appOne/createPro.html',{'formRol':formRol, 'formProyecto':formPro})

# destruir después de usar
#
def FormProyecto2(request):
    formPro = formProyecto()
    #formRol=rolesFormset()
    context={
        'formPro':formPro,
        #'formRol':formRol,
    }

    if request.method == 'POST':
        formPro=formProyecto(request.POST)
        #formRol=rolesFormset(request.POST,request.FILES)

        if formPro.is_valid() and formRol.is_valid():
            print("VALIDATION SUCCESS!")
            print(formPro.cleaned_data)
            #print(formRol.cleaned_data)
            #for form in formRol:
                #print(form.cleaned_data)
            p = proyecto(proName=formPro.cleaned_data['proName'],proDescription=formPro.cleaned_data['proDescription'],
                        proVideo=formPro.cleaned_data['proVideo'],proAboutUs=formPro.cleaned_data['proAboutUs'],
                        proFrase=formPro.cleaned_data['proFrase'],proCreationDate=formPro.cleaned_data['proCreationDate'],
                        proArea=formPro.cleaned_data['proArea'],proLocation=formPro.cleaned_data['proLocation'],
                        proImagen=formPro.cleaned_data['proArea'])
            p.save()
            #for form in formRol:
                #r = rolInfo(rol=form.cleaned_data['rolNombre'],fechaLimite=form.cleaned_data['rolFechaLimite'],
                        #    rolcantidad=form.cleaned_data['rolCantidad'],rolDescripcion=form.cleaned_data['rolDescripcion'],
                        #    rolLocation=form.cleaned_data['rolLocation'])
                #r.save()
                #p.proRoles.add(r)
            return index(request)
        else:
            print('ERROR EN EL FORM')
    return render(request,'appOne/altCreaPro.html',context)

#
# destruir después de usar

"""
def FormProyecto(request):
    form = forms.FormProyecto()

    if request.method == 'POST':
        form = forms.FormProyecto(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            #print("NAME: "+form.cleaned_data['name'])
            #recipients=[]
            #if ProConfirmation:
                #print("Enviar email!")
            #    send_mail('subject', 'message', 'A01421467@itesm.mx', 'angieguemes@gmail.com')
            #    return HttpResponseRedirect('/thanks/')

    return render(request,'appOne/createPro.html',{'form':form})
"""
