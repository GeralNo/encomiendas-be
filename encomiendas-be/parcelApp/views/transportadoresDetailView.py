from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from parcelApp.models.transportadores import Transportadores
from parcelApp.serializers.transportadoresSerializer import TransportadoresSerializer
 
class TransportadoresDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
   
    def get_object(self, id):
       
        try:
            return Transportadores.objects.get(id=id)
        except Transportadores.DoesNotExist:
            return None
       
    def get(self, request, *args, **kwargs):
       
        transportadores_instance = self.get_object(kwargs['pk'])
        if not transportadores_instance:
            return Response(
                {"res": "Object with transportadores id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TransportadoresSerializer(transportadores_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def put(self, request, *args, **kwargs):
        
        transportadores_instance = self.get_object(kwargs['pk'])
        if not transportadores_instance:
            return Response(
                {"res": "Object with transportadores id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = TransportadoresSerializer(instance =transportadores_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the transportadores item with given branch id if exists
        '''
        transportadores_instance = self.get_object(kwargs['pk'])
        if not transportadores_instance:
            return Response(
                {"res": "Object with transportadores id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        transportadores_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
