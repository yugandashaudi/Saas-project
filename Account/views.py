from rest_framework.views import APIView
from rest_framework import status
from .serializers import Myuser
from rest_framework.response import Response



class userregistrationView(APIView):
    def post(self,request,format=None):
        serializers=Myuser(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user = serializers.save()
            return Response('The user resgistration was sucessfull',status=status.HTTP_201_CREATED)

        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)    