from .models import *
from django.forms import ModelForm, TextInput, forms

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
                'placeholder': 'Ваш ник',

            }),
            'password': TextInput(attrs={
                'placeholder': 'Пароль'
            }),
            'passwordConfirm': TextInput(attrs={
                'placeholder': 'Подтверждение пароля'
            })
        }

class loginUserForm(ModelForm):
    class Meta:
        model = loginUser
        fields = ['name', 'password']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Ваш ник'
            }),
            'password': TextInput(attrs={
                'placeholder': 'Пароль'
            })
        }

class floorChangeForm(forms.Form):
    pass

class loginForm(forms.Form):
    pass