from .models import *
from django.forms import ModelForm, TextInput, forms, HiddenInput

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

class noteDeletingForm(forms.Form):
    pass

class creatingUserForm(ModelForm):
    class Meta:
        model = newUser
        fields = ['name', 'password', 'passwordConfirm']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Ваш ник'
            }),
            'password': TextInput(attrs={
                'placeholder': 'Пароль',
                'tag': HiddenInput
            }),
            'passwordConfirm': TextInput(attrs={
                'placeholder': 'Подтверждение пароля',
                'tag': HiddenInput
            })
        }

class floorChangeForm(forms.Form):
    pass