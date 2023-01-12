from django.db import models

class Peliculas(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.CharField(max_length=50)
    año_de_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=50)
    

class Directores(models.Model):

    ESTADO_CHOICES = (
        ("activo", "activo"),
        ("inactivo", "inactivo"),
    )

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    estado= models.CharField(max_length=10, choices=ESTADO_CHOICES)


class Generos(models.Model):
    nombre = models. CharField(max_length=100)
    
