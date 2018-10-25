from django.urls import path
from .views import ProjectsListView, ProjectDetailView, ProjectCreate, ProjectUpdate, ProjectDelete


projects_patterns = ([
    path('', ProjectsListView.as_view(), name='projects'),
    path('<int:pk>/<slug:slug>/', ProjectDetailView.as_view(), name='project'),
    path('create/', ProjectCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProjectUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProjectDelete.as_view(), name='delete'),
], 'projects')
