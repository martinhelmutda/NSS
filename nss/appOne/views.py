from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
#Importo mis tablas
from appOne.models import area, proyecto
from . import forms

# Create your views here.
def index(request):
    areas_list = area.objects.order_by('area')
    area_dict= {'access_records': areas_list}
    return render(request, 'appOne/index.html', context=area_dict)
    #return HttpResponse("Main page")

def proyecto(request):
    proyectodict = {'proyecto_insert': 'PAGINA DE PROYECTO'}
    return render(request, 'appOne/proyecto.html', context=proyectodict) # appOne/proyecto.html ha ce referencia al html en templates

def FormProyecto(request):
    form = forms.FormProyecto()

    if request.method == 'POST':
        form = forms.FormProyecto(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            #print("NAME: "+form.cleaned_data['name'])
            #print("EMAIL: "+form.cleaned_data['email'])
            #print("TEXT: "+form.cleaned_data['text'])
            recipients=[]
            if ProConfirmation:
                send_mail('subject', 'message', 'A01421467@itesm.mx', 'angieguemes@gmail.com')
                return HttpResponseRedirect('/thanks/')

    return render(request,'appOne/createPro.html',{'form':form})
