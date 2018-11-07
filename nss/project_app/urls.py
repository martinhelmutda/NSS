from django.urls import path
from .views import ProjectsListView, ProjectDetailView, ProjectCreate, ProjectUpdate, ProjectDelete, DataRep, ProjectRolCreate
from project_app import views

projects_patterns = ([
    path('', ProjectsListView.as_view(), name='projects'),
    path('<int:pk>/<slug:slug>/', ProjectDetailView.as_view(), name='project'),
    path('create/', ProjectCreate.as_view(), name='create'),
    path('DataRep/', views.DataRep, name='DataRep'),
    path('update/<int:pk>/', ProjectUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProjectDelete.as_view(), name='delete'),
    path('createRolProyecto/<int:pk>/<slug:slug>/', ProjectRolCreate.as_view(), name = 'form_rol_project'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
], 'project_app')
