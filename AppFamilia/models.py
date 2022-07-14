from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_de_nacimiento= models.DateField()

    def __str__(self):
        return self.nombre+" "+ str(self.apellido)

class Mascotas(models.Model):
    apodo = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.apodo+" "+ str(self.raza)

class Vecinos(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+ str(self.direccion)