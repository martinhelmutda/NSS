from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from appOne.models import area, proyecto, rolInfo, rol, location
from . import forms
from appOne.forms import formProyecto
from django.urls import reverse
from urllib.parse import urlencode
from flask import Flask, render_template, request, redirect

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


def FormProyecto(request):
    form = formProyecto()

    if request.method == 'POST':
        form=formProyecto(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print(form.cleaned_data['proName'])
            r = rolInfo(rol=form.cleaned_data['rolNombre'],fechaLimite=form.cleaned_data['rolFechaLimite'],
                        rolcantidad=form.cleaned_data['rolCantidad'],rolDescripcion=form.cleaned_data['rolDescripcion'],
                        rolLocation=form.cleaned_data['rolLocation'])
            r.save()
            p = proyecto(proName=form.cleaned_data['proName'],proDescription=form.cleaned_data['proDescription'],
                        proVideo=form.cleaned_data['proVideo'],proAboutUs=form.cleaned_data['proAboutUs'],
                        proFrase=form.cleaned_data['proFrase'],proCreationDate=form.cleaned_data['proCreationDate'],
                        proArea=form.cleaned_data['proArea'],proLocation=form.cleaned_data['proLocation'])
            p.save()
            p.proRoles.add(r)
            return index(request)
        else:
            print('ERROR EN EL FORM')
    return render(request,'appOne/createPro.html',{'form':form})

# destruir después de usar
#
def FormProyecto2(request):
    form = NewProjectForm()
    if request.method == 'POST':
        form = NewProjectForm(request.POST)

        if form.is_valid:
            print("LISTO")
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR EN EL FORM")
    return render(request,'appOne/altCreaPro.html',{'form':form})
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
