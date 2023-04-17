from django.shortcuts import render

from .Database import main
from .forms import *

userId = 1

noteIds = []
noteNames = []
noteDescriptions = []
noteLocations = []

def mainPage(request):
    data = {
        'name': 'Карта Школы МОБУ СОШ ЦО "Кудрово"',
        'darkTheme': 0
    }
    return render(request, "main/index.html", data)

def deleteNote(request):

    if request.method == 'POST':
        form = noteDeletingForm(request.POST)
        if form.is_valid():
            EventId = request.POST.get('value')
            main.deleteEvent(EventId)

    noteNames = []
    noteDescriptions = []
    noteLocations = []
    noteIds = []

    notes = main.eventList(userId)
    for i in range(len(notes)):
        noteNames.append(notes[i][3])
        noteDescriptions.append(notes[i][4])
        noteLocations.append(notes[i][5])
        noteIds.append(notes[i][2])

    data = {
        'form': newNoteForm,
        'noteNames': noteNames,
        'noteDescriptions': noteDescriptions,
        'noteLocations': noteLocations,
        'noteIds': noteIds,
        'darkTheme': 0
    }

    return render(request, "main/notes.html", data)

def notes(request):
    if request.method == 'POST':
        form = newNoteForm(request.POST)
        if form.is_valid():
            main.createEvent(userId, request.POST['name'], request.POST['description'], request.POST['location'])

    noteNames = []
    noteDescriptions = []
    noteLocations = []
    noteIds = []

    notes = main.eventList(userId)
    for i in range(len(notes)):
        noteNames.append(notes[i][3])
        noteDescriptions.append(notes[i][4])
        noteLocations.append(notes[i][5])
        noteIds.append(notes[i][2])

    data = {
        'form': newNoteForm,
        'noteNames': noteNames,
        'noteDescriptions': noteDescriptions,
        'noteLocations': noteLocations,
        'noteIds': noteIds,
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