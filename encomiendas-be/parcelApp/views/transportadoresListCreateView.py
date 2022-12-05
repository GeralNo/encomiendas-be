from asyncio import transports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
 
from parcelApp.models.transportadores import Transportadores
from parcelApp.serializers.transportadoresSerializer import TransportadoresSerializer
 
class TransportadoresListCreateView(APIView):
    permission_classes = (IsAuthenticated,)
   
    queryset = Transportadores.objects.all()
    serializer_class = TransportadoresSerializer
   
    def get(self, request, *args, **kwargs):
        '''
        List all the transportadores for given requested user
        '''
        transportadores = Transportadores.objects.all()
        serializer = TransportadoresSerializer(transportadores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def post(self, request, *args, **kwargs):
        serializer = TransportadoresSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)