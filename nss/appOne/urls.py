from django.urls import path
from appOne import views
from appOne import forms

urlpatterns=[
    path('', views.verProyecto, name = 'verProyecto'),
    path('crearProyecto', views.FormProyecto, name = 'FormProyecto'),
]
