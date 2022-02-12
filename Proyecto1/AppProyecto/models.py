from django.db import models

# Create your models here.

class Entrenadores (models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email = models.EmailField()

class Clientes (models.Model):
    nombre= models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()

class Actividades (models.Model):
    nombre= models.CharField(max_length=40)
    intensidad = models.CharField(max_length=10)