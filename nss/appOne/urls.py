from django.urls import path
from appOne import views
from appOne import forms

urlpatterns=[
    path('', views.proyecto, name = 'proyecto'),
    path('crearProyecto', views.FormProyecto, name = 'FormProyecto'),
]
