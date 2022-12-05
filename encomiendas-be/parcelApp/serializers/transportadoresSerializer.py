from parcelApp.models.transportadores import Transportadores
from rest_framework import serializers

class TransportadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportadores
        fields = ['idTransportador', 'nombreTransportador', 'tipoTransporte']