from parcelApp.models.trabajadores import Trabajadores
from rest_framework import serializers

class TrabajadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajadores
        fields = ['idTrabajador', 'nombreTrabajador', 'fechaIngreso', 'cargo', 'salario', 'isActive']

        