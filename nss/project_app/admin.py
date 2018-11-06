from django.contrib import admin
from .models import project, category, state, city, rolInfo, projectImg, project_rol

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pro_name','order')

admin.site.register(project, ProjectAdmin)
admin.site.register(category)
admin.site.register(state)
admin.site.register(city)
admin.site.register(rolInfo)
admin.site.register(projectImg)
admin.site.register(project_rol)
