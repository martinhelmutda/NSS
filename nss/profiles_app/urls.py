from django.urls import path
from .views import ProfileList, ProfileDetail

profiles_patterns= ([
    path('', ProfileList.as_view(), name='list'),
    path('<username>/', ProfileDetail.as_view(), name='detail'),
], 'profiles_app')
