from django.shortcuts import render

from .Database import main
from .forms import *

userId = 1

noteIds = []
noteNames = []
noteDescriptions = []
noteLocations = []

def userRegister(request):

    if request.method == 'POST':
        form = creatingUserForm(request.POST)
        if form.is_valid() and request.POST['password'] == request.POST['passwordConfirm']:
            main.createUser(request.POST['name'], request.POST['password'])

            data = {
                'name': 'Карта Школы МОБУ СОШ ЦО "Кудрово"',
                'darkTheme': 0
            }

            return render(request, "main/mainPage.html", data)

        else:
            data = {
                'form': creatingUserForm,
                'name': 'Карта Школы МОБУ СОШ ЦО "Кудрово"'
            }
            return render(request, "main/index.html", data)

def registerPage(request):
    data = {
        'form': creatingUserForm,
        'name': 'Карта Школы МОБУ СОШ ЦО "Кудрово"'
    }

    return render(request, "main/index.html", data)

def mainPage(request):
    data = {
        'name': 'Карта Школы МОБУ СОШ ЦО "Кудрово"',
        'darkTheme': 0
    }
    return render(request, "main/mainPage.html", data)

def createNote(request):

    if request.method == 'POST':
        form = newNoteForm(request.POST)
        if form.is_valid():
            main.createEvent(userId, request.POST['name'], request.POST['description'], request.POST['location'])

    data = notesData()

    return render(request, "main/notes.html", data)

def deleteNote(request):

    if request.method == 'POST':
        form = noteDeletingForm(request.POST)
        if form.is_valid():
            EventId = request.POST.get('value')
            main.deleteEvent(EventId)

    data = notesData()

    return render(request, "main/notes.html", data)

def notesData():
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
    return data

def notes(request):

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