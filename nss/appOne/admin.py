from django.contrib import admin

# Register your models here.
#Importamos todas las clases (tablas) de las apps.
from .models import proyecto, area, location

#Anotamos las clases (tablas) para poder verlas en la pagina de admin.
admin.site.register(proyecto)
admin.site.register(area)
admin.site.register(location)
