from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerPage),
    path('notes.html', views.notes),
    path('settings.html', views.settings),
    path('map.html', views.map),
    path('mainPage.html', views.mainPage),
    path('index.html', views.mainPage),
    path('newNote', views.createNote, name='newNote'),
    path('deleteNote', views.deleteNote, name='deleteNote'),
    path('userRegister', views.userRegister, name='userRegister')
]
