from django.contrib import admin

# Register your models here.
#Importamos todas las clases (tablas) de las apps.
from .models import proyecto, area, location, rol, rolInfo, proyectoImagen

#Anotamos las clases (tablas) para poder verlas en la pagina de admin.
admin.site.register(proyecto)
admin.site.register(area)
admin.site.register(location)
admin.site.register(rol)
admin.site.register(rolInfo)
admin.site.register(proyectoImagen)
