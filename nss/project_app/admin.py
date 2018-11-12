from django.contrib import admin
from .models import project, category,subcategory, state, city, rolInfo, projectImg, project_rol, user_project, status

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pro_name','order')

admin.site.register(project)
admin.site.register(category)
admin.site.register(subcategory)
admin.site.register(state)
admin.site.register(city)
admin.site.register(rolInfo)
admin.site.register(projectImg)
admin.site.register(project_rol)
admin.site.register(user_project)
admin.site.register(status)
