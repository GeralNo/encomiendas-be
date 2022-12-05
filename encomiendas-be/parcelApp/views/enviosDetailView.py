from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from parcelApp.models.envios import Envios
from parcelApp.serializers.enviosSerializer import EnviosSerializer
 
class EnviosDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
   
    def get_object(self, id):
       
        try:
            return Envios.objects.get(id=id)
        except Envios.DoesNotExist:
            return None
       
    def get(self, request, *args, **kwargs):
       
        envios_instance = self.get_object(kwargs['pk'])
        if not envios_instance:
            return Response(
                {"res": "Object with envios id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = EnviosSerializer(envios_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def put(self, request, *args, **kwargs):
        
        envios_instance = self.get_object(kwargs['pk'])
        if not envios_instance:
            return Response(
                {"res": "Object with envios id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = EnviosSerializer(instance =envios_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the envios item with given branch id if exists
        '''
        envios_instance = self.get_object(kwargs['pk'])
        if not envios_instance:
            return Response(
                {"res": "Object with envios id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        envios_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
