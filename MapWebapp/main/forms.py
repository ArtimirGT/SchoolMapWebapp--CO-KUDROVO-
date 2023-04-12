from .models import *
from django.forms import ModelForm, TextInput

class newNoteForm(ModelForm):
    class Meta:
        model = newNote
        fields = ['name', 'description', 'location']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'description': TextInput(attrs={
                'placeholder': 'Описание'
            }),
            'location': TextInput(attrs={
                'placeholder': 'Местоположение'
            })
        }