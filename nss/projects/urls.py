from django.urls import path
from .views import ProjectsListView, ProjectDetailView


urlpatterns = [
    path('', ProjectsListView.as_view(), name='projects'),
    path('<int:pk>/<slug:slug>/', ProjectDetailView.as_view(), name='project'),
]
