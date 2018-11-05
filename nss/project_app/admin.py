from django.contrib import admin
from .models import project, category, location, rolInfo, projectImg, project_rol

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pro_name','order')

admin.site.register(project, ProjectAdmin)
admin.site.register(category)
admin.site.register(location)
admin.site.register(rolInfo)
admin.site.register(projectImg)
admin.site.register(project_rol)
