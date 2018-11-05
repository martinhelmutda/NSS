#Last modified by César Buenfil on Oct 19,2018

"""nss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an imlport:  from my_app import views
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
from account_app import views
from django.conf import settings
from django.conf.urls.static import static
from project_app.urls import projects_patterns
#SOCIAL AUTH
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'), #Despliega lo de la funcion index en appOne/views.py/def index
    path('user/', include('account_app.urls')),
    path('search/', include('search_app.urls')),

    #path('crearProyecto/',include('appOne.urls')),
    #path('createProyect/',views.form_name_view,name='form_name'),
    path('admin/', admin.site.urls),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
    #path('create_profile/',views.form_profile, name='form_profile'),
    path('project_app/',include(projects_patterns)),
    path('', include('django.contrib.auth.urls')), # EMAIL RESET
    path('oauth/', include('social_django.urls', namespace="social")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#models
#Help us incorporate a database into a django project
