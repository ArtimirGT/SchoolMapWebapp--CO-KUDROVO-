from django.shortcuts import render

from .Database import main
from .forms import *

noteNames = []
noteDescriptions = []
noteLocations = []

notes = main.eventList(1)
for i in range(len(notes)):
    noteNames.append(notes[i][3])
    noteDescriptions.append(notes[i][5])
    noteLocations.append(notes[i][4])

def mainPage(request):
    data = {
        'name': 'Карта Школы МОБУ СОШ ЦО "Кудрово"',
        'darkTheme': 0
    }
    return render(request, "main/index.html", data)

def notes(request):

    if request.method == 'POST':
        form = newNoteForm(request.POST)
        noteNames.append(request.POST['name'])
        noteDescriptions.append(request.POST['description'])
        noteLocations.append(request.POST['location'])


    data = {
        'form': newNoteForm,
        'noteNames': noteNames,
        'noteDescriptions': noteDescriptions,
        'noteLocations': noteLocations,
        'darkTheme': 0
    }
    return render(request, "main/notes.html", data)

def map(request):
    data = {
        'darkTheme': 0
    }
    return render(request, 'main/map.html', data)

def settings(request):
    data = {
        'darkTheme': 0
    }
    return render(request, 'main/settings.html')