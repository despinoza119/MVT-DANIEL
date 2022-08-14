from django.db import models

# Create your models here.

class Tio(models.Model):
    nombre=models.CharField(max_length=30) #Nombre del familiar (tio)
    edad=models.IntegerField()             #Edad del familiar (tio)
    fechaRegistro=models.DateField()       #Fecha en la que se registró

class Primo(models.Model):
    nombre=models.CharField(max_length=30) #Nombre del familiar (tio)
    edad=models.IntegerField()             #Edad del familiar (tio)
    deportePreferido=models.CharField(max_length=30)    #Deporte preferido
