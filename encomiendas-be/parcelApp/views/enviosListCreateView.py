from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
 
from parcelApp.models.envios import Envios
from parcelApp.serializers.enviosSerializer import EnviosSerializer
 
class EnviosListCreateView(APIView):
    permission_classes = (IsAuthenticated,)
   
    queryset = Envios.objects.all()
    serializer_class = EnviosSerializer
   
    def get(self, request, *args, **kwargs):
        '''
        List all the envios for given requested user
        '''
        envios = Envios.objects.all()
        serializer = EnviosSerializer(envios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def post(self, request, *args, **kwargs):
        serializer = EnviosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)