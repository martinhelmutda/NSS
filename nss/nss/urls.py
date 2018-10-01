
"""nss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appOne import views

urlpatterns = [
    path('', views.index, name='index'), #Despliega lo de la funcion index en appOne/views.py/def index
    path('proyecto/', include('appOne.urls')),
    #path('crearProyecto/',include('appOne.urls')),
    #path('createProyect/',views.form_name_view,name='form_name'),
    path('admin/', admin.site.urls),
]


#models
#Help us incorporate a database into a django project

