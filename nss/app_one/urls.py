from django.urls import path, include
from app_one import views
from .views import MyProjectsView

app_name = 'app_one'
urlpatterns=[

    path('', views.see_project, name = 'see_project'),
    path('crearProyecto', views.form_project, name = 'form_project'),
    path('altCrearProyecto', views.form_project2, name = 'form_project'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('create_profile/',views.form_profile, name='form_profile'),

    path('my_projects/', MyProjectsView.as_view(), name='my_projects'),
]
