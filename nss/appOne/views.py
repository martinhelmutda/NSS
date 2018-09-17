from django.shortcuts import render
from django.http import HttpResponse
#Importo mis tablas
from appOne.models import area, proyecto

# Create your views here.
def index(request):
    areas_list = area.objects.order_by('area')
    area_dict= {'access_records': areas_list}
    return render(request, 'appOne/index.html', context=area_dict)
    #return HttpResponse("Main page")



def proyecto(request):
    proyectodict = {'proyecto_insert': 'PAGINA DE PROYECTO'}
    return render(request, 'appOne/proyecto.html', context=proyectodict) # appOne/proyecto.html ha ce referencia al html en templates
