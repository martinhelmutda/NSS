from django.urls import path
from .views import ProjectsListView,GroupCreate,GroupsListView, change_user_project_status ,ProjectDetailView, ProjectCreate, ProjectUpdate, ProjectDelete, DataRep, ProjectRolCreate
from project_app import views
app_name="project_app"
projects_patterns = ([
    path('p/', ProjectsListView.as_view(), name='projects'),
    path('g/', GroupsListView.as_view(), name='groups'),
    path('<int:pk>/<slug:slug>/', ProjectDetailView.as_view(), name='project'),
    path('ajax/change_user_project_status/', views.change_user_project_status, name='change_user_project_status'),
    path('create/', ProjectCreate.as_view(), name='create'),
    path('createGroup/', GroupCreate.as_view(), name='create_group'),
    path('DataRep/', views.DataRep, name='DataRep'),
    path('update/<int:pk>/', ProjectUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProjectDelete.as_view(), name='delete'),
    path('createRolProyecto/<int:pk>/<slug:slug>/', ProjectRolCreate.as_view(), name = 'form_rol_project'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),

], 'project_app')
