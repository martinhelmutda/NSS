from django.contrib import admin
from .models import Project, category, location, rol, rolInfo

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pro_name','order')

admin.site.register(Project, ProjectAdmin)
admin.site.register(category)
admin.site.register(location)
admin.site.register(rol)
admin.site.register(rolInfo)
