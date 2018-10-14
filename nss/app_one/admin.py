#Last modified by César Buenfil on Oct 14,2018

from django.contrib import admin

# Register your models here.
#Importamos todas las clases (tablas) de las apps.
from .models import project, category, location, rol, rolInfo, projectImg

#Anotamos las clases (tablas) para poder verlas en la pagina de admin.
admin.site.register(project)
admin.site.register(category)
admin.site.register(location)
admin.site.register(rol)
admin.site.register(rolInfo)
admin.site.register(projectImg)
