from django.urls import path
from app_one import views

app_name = 'app_one'
urlpatterns=[
    path('', views.see_project, name = 'see_project'),
    path('crearProyecto', views.form_project, name = 'form_project'),
    path('altCrearProyecto', views.form_project2, name = 'form_project'),
]
