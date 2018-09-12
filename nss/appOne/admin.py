from django.contrib import admin

# Register your models here.
from .models import proyecto, area

admin.site.register(proyecto)
admin.site.register(area)
