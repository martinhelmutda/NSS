###Last modified by Martín Helmut on Oct 20,2018
from django.urls import path, include
from search_app import views
from project_app.urls import projects_patterns

app_name = 'search_app'
urlpatterns=[
    path('',views.SearchView.as_view(),name='search'),
    path('ajax/load_info/', views.load_info, name='load_info'),
]
