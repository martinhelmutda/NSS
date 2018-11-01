from django.contrib import admin
from .models import project, category, location, rolInfo, projectImg

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pro_name','order')

admin.site.register(project)
admin.site.register(category)
admin.site.register(location)
admin.site.register(rolInfo)
admin.site.register(projectImg)
