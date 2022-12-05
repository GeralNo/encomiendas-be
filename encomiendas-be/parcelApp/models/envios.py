from django.db import models
from .user import User

class Envios(models.Model):
    
    idEnvio = models.AutoField(primary_key=True)
    remitente = models.CharField('Remitente', max_length = 45)
    destinatario = models.CharField('Destinatario', max_length = 45)
    fechaEnvio = models.DateTimeField()
    fechaEntrega = models.DateTimeField()
    tipoPaquete = models.CharField('Paquete', max_length = 45)
    valorDeclarado = models.IntegerField(default=0)
    fueEntregado = models.BooleanField(default=False)