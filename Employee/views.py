from rest_framework.response import Response 
from .serializers import *
from rest_framework.views import APIView


class CreateTenant(APIView):
    def post(self,request,format=None):
        serializers = ClientTenantSerializer(data= request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
class CreateDomain(APIView):
  
    def post(self,request,format=None):
        serializers = DomainSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response('The domain was created ')