from django.core.validators import MinLengthValidator
from django.db import models


class Facultad(models.Model):
    nombre = models.CharField(max_length=100,
                              help_text='Nombre de la facultad',
                              validators= [MinLengthValidator(3)])
    siglas = models.CharField(max_length=10,
                              blank=True,
                              help_text='Siglas de la facultad')

    def __str__(self):
        return self.nombre


class Modalidad(models.Choices):
    PRESENCIAL = 'PRESENCIAL'
    SEMIPRESENCIAL = 'SEMIPRESENCIAL'
    DISTANCIA = 'DISTANCIA'


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    titulo = models.CharField(max_length=100)
    facultad = models.ForeignKey(Facultad,
                                 on_delete=models.CASCADE,
                                 related_name='carrera_list')
    modalidad = models.CharField(max_length=50,  # PRE, SEM, DIS
                                 choices=Modalidad.choices,
                                 default=Modalidad.PRESENCIAL)

    def __str__(self):
        return self.nombre


class Ciclo(models.Model):
    numero = models.PositiveIntegerField()
    carrera = models.ForeignKey(Carrera,
                                on_delete=models.CASCADE,
                                related_name='ciclo_list')

    def __str__(self):
        return f'{self.numero} - {self.carrera.nombre}'


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    aa = models.PositiveIntegerField()
    acd = models.PositiveIntegerField()
    ape = models.PositiveIntegerField()
    ciclo = models.ForeignKey(Ciclo,
                              on_delete=models.CASCADE,
                              related_name='asignatura_list')

    def __str__(self):
        return self.nombre
