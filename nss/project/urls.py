from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_id>/<slug:project_slug>/', views.project, name='project'),
]
