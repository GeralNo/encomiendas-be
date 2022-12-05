from django.db import models
from .user import User
 
class Transportadores(models.Model):

    idTransportador = models.AutoField(primary_key=True)
    nombreTransportador = models.CharField('Nombre Trabajador', max_length = 45)
    tipoTransporte = models.CharField('cargo', max_length = 45)