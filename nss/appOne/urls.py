from django.urls import path
from appOne import views

app_name = 'appOne'
urlpatterns=[
    path('', views.verProyecto, name = 'verProyecto'),
    path('crearProyecto', views.FormProyecto, name = 'FormProyecto'),
    path('altCrearProyecto', views.FormProyecto2, name = 'FormProyecto2'),
]
