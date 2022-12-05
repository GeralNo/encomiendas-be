from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
 
from parcelApp.models.trabajadores import Trabajadores
from parcelApp.serializers.trabajadoresSerializer import TrabajadoresSerializer
 
class TrabajadoresListCreateView(APIView):
    permission_classes = (IsAuthenticated,)
   
    queryset = Trabajadores.objects.all()
    serializer_class = TrabajadoresSerializer
   
    def get(self, request, *args, **kwargs):
        '''
        List all the trabajadores for given requested user
        '''
        trabajadores = Trabajadores.objects.all()
        serializer = TrabajadoresSerializer(trabajadores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def post(self, request, *args, **kwargs):
        serializer = TrabajadoresSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)