from django.db import models

class newNote(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.CharField('Описание', max_length=255)
    location = models.CharField('Местонахождение', max_length=30)

class noteDeleting(models.Model):
    eventId = models.IntegerField('Id')