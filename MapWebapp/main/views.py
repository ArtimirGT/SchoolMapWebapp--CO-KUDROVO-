from django.shortcuts import render

from .Database import main

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
    data = {
        'noteNames': noteNames,
        'noteDescriptions': noteDescriptions,
        'noteLocations': noteLocations,
        'darkTheme': 0
    }
    return render(request, "main/notes.html", data)

'''def settings(request):
    data = {
        'darkTheme': 0
    }
    return render(request, 'main/settings.html', data)'''

def map(request):
    data = {
        'darkTheme': 0
    }
    return render(request, 'main/map.html', data)

def settings(request):
    # Проверяем состояние (включено/выключено)
    is_on = False
    if request.method == 'POST':
        on_off = request.POST.get('on_off', None)
        if on_off:
            is_on = (on_off == 'on')

    # Определяем текст на кнопке в соответствии с текущим состоянием
    if is_on:
        button_text = 'Выключить'
    else:
        button_text = 'Включить'

    # Отображаем кнопку и текущее состояние
    context = {
        'is_on': is_on,
        'on_off': 'on' if not is_on else 'off',
        'button_text': button_text
    }
    return render(request, 'main/settings.html', context=context)