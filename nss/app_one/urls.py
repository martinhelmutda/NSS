from django.urls import path
from app_one import views

app_name = 'app_one'
urlpatterns=[
    path('', views.see_project, name = 'see_project'),
    path('crearProyecto', views.form_project, name = 'form_project'),
    path('altCrearProyecto', views.form_project2, name = 'form_project'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('create_pofile',views.form_profile, name='form_profile'),
]
