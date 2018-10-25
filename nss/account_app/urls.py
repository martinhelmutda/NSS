###Last modified by Martín Helmut on Oct 20,2018
from django.urls import path, include
from account_app import views
from project_app.urls import projects_patterns

app_name = 'account_app'
urlpatterns=[

    #path('', views.see_project, name = 'see_project'),
    path('registrar/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    #path('create_profile/',views.form_profile, name='form_profile'),

    # path('my_projects/', MyProjectsView.as_view(), name='my_projects'),
    # path('projects/',include(projects_patterns)),
]
