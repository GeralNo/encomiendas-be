from django.db import models
from .user import User
 
class Trabajadores(models.Model):
    
    idTrabajador = models.AutoField(primary_key=True)
    nombreTrabajador = models.CharField('Nombre Trabajador', max_length = 45)
    fechaIngreso = models.DateTimeField()
    cargo = models.CharField('cargo', max_length = 45)
    salario = models.IntegerField(default=0)
    isActive = models.BooleanField(default=True)