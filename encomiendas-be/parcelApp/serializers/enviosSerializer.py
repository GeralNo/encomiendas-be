from parcelApp.models.envios import Envios
from rest_framework import serializers

class EnviosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envios
        fields = ['idEnvio', 'remitente', 'destinatario', 'fechaEnvio', 'fechaEntrega', 'tipoPaquete', 'valorDeclarado', 'fueEntregado']
