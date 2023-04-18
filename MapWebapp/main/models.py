from django.db import models

class newNote(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.CharField('Описание', max_length=255)
    location = models.CharField('Местонахождение', max_length=30)

class newUser(models.Model):
    name = models.CharField('Ваш ник', max_length=30)
    password = models.CharField('Пароль', max_length=30)
    passwordConfirm = models.CharField('Подтвердите пароль', max_length=30)