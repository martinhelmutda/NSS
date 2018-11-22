from django.urls import path
from .views import ProjectsListView,GroupCreate,ApplicationsDetailView,delete,accept,button_text, change_user_project_status ,ProjectDetailView, ProjectCreate, ProjectUpdate, ProjectDelete, DataRep, ProjectRolCreate
from project_app import views
app_name="project_app"
projects_patterns = ([
    path('p/', ProjectsListView.as_view(), name='projects'),
    path('<int:pk>/a/', ApplicationsDetailView.as_view(), name='applications'),
    path('<int:pk>/<slug:slug>/', ProjectDetailView.as_view(), name='project'),
    path('ajax/change_user_project_status/', views.change_user_project_status, name='change_user_project_status'),
    path('ajax/button_text/', views.button_text, name='button_text'),
    path('ajax/accept/', views.accept, name='accept'),
    path('ajax/delete/', views.delete, name='delete'),
    path('create/', ProjectCreate.as_view(), name='create'),
    path('createGroup/', GroupCreate.as_view(), name='create_group'),
    path('DataRep/', views.DataRep, name='DataRep'),
    path('update/<int:pk>/', ProjectUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProjectDelete.as_view(), name='delete'),
    path('createRolProyecto/<int:pk>/<slug:slug>/', ProjectRolCreate.as_view(), name = 'form_rol_project'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    path('like/',views.like_post, name ="like_post"),

], 'project_app')
