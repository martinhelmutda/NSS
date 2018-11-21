#Last modified by César Buenfil on Oct 19,2018

from django.contrib import admin

# Register your models here.
#Importamos todas las clases (tablas) de las apps.
from .models import *

admin.site.register(UserProfileInfo)
admin.site.register(Profile) 

#Anotamos las clases (tablas) para poder verlas en la pagina de admin.
