from django.urls import path
from appOne import views

urlpatterns=[
    path('', views.proyecto, name = 'proyecto'),
]
