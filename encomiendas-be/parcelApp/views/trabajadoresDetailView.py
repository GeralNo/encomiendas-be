from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from parcelApp.models.trabajadores import Trabajadores
from parcelApp.serializers.trabajadoresSerializer import TrabajadoresSerializer
 
class TrabajadoresDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
   
    def get_object(self, id):
       
        try:
            return Trabajadores.objects.get(id=id)
        except Trabajadores.DoesNotExist:
            return None
       
    def get(self, request, *args, **kwargs):
       
        trabajadores_instance = self.get_object(kwargs['pk'])
        if not trabajadores_instance:
            return Response(
                {"res": "Object with trabajadores id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TrabajadoresSerializer(trabajadores_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def put(self, request, *args, **kwargs):
        
        trabajadores_instance = self.get_object(kwargs['pk'])
        if not trabajadores_instance:
            return Response(
                {"res": "Object with trabajadores id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = TrabajadoresSerializer(instance =trabajadores_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the trabajadores item with given branch id if exists
        '''
        trabajadores_instance = self.get_object(kwargs['pk'])
        if not trabajadores_instance:
            return Response(
                {"res": "Object with trabajadores id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        trabajadores_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
