# django asigna un campo ID autoincrementable automaticamente 
# a menos que nosotros creemos un campo con clave primaria.

from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido) 
        

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=False , blank=True, on_delete=models.CASCADE)
    numero_mascota = models.IntegerField()
    razones = models.TextField()
