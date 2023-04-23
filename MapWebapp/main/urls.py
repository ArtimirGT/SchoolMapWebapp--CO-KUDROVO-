from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
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
    path('userRegister', views.userRegister, name='userRegister'),
    path('login', views.login, name='login'),
    path('Floor1', views.Floor1, name='Floor1'),
    path('Floor2', views.Floor2, name='Floor2'),
    path('Floor3', views.Floor3, name='Floor3'),
    path('Floor4', views.Floor4, name='Floor4'),
    #3 этаж
    path('Mediateka', views.Mediateka, name='Mediateka'),
    path('cab4201', views.cab4201, name='cab4201')
]

urlpatterns += staticfiles_urlpatterns()