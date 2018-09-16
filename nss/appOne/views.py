from django.shortcuts import render
from django.http import HttpResponse
#Importo mis tablas
#from django.models import area, proyecto
# Create your views here.
def index(request):
    return HttpResponse("Main page")



def proyecto(request):
    proyectodict = {'proyecto_insert': 'PAGINA DE PROYECTO'}
    return render(request, 'appOne/proyecto.html', context=proyectodict) # appOne/proyecto.html ha ce referencia al html en templates
