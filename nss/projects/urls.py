from django.urls import path
from .views import ProjectsListView, ProjectDetailView, ProjectCreateView


projects_patterns = ([
    path('', ProjectsListView.as_view(), name='projects'),
    path('<int:pk>/<slug:slug>/', ProjectDetailView.as_view(), name='project'),
    path('create/', ProjectCreateView.as_view(), name='create'),
], 'projects')
