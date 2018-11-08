from django.urls import path
from .views import ThreadList, ThreadDetail, add_message

messages_app_patterns = ([
    path('', ThreadList.as_view(), name="list"),
    path('thread/<int:pk>/',ThreadDetail.as_view(), name="detail"),
    path('thread/<int:pk>/add/',add_message, name="add"),
], "messages_app")
