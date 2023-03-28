from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage),
    path('notes.html', views.notes),
    path('settings.html', views.settings),
    path('map.html', views.map),
    path('index.html', views.mainPage)
]
