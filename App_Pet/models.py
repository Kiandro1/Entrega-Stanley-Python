from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    movil = models.IntegerField()
    email = models.EmailField(null=True)

    def __str__(self):
        return f'{self.nombre} {self.movil}'

class Mascota(models.Model):

    nombre = models.CharField(max_length=50)
    nombre_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    raza = models.CharField(max_length=30)
    peso = models.FloatField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre, self.nombre_cliente
    
    class Meta():
        ordering = ('nombre', 'raza')


class Alimento_Pet(models.Model):

    marca = models.CharField(max_length=30)
    raza_pet = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.marca} {self.raza_pet}'


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
# Create your models here.
