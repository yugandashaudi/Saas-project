from rest_framework.views import APIView
from rest_framework import status
from .serializers import Myuser,userlogin,ChangeUserSerializers
from rest_framework.response import Response
from django.shortcuts import render 
from django.contrib.auth import authenticate
from .renenders import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class userregistrationView(APIView):
    renender_classes = [UserRenderer]
    

    def post(self,request,format=None):
        serializers=Myuser(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user = serializers.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'the user was sucessfully created'},status=status.HTTP_201_CREATED)

        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)    

class UserLoginView(APIView):
    
    def post(self,request,format=None):
        serializers = userlogin(data=request.data)
        if serializers.is_valid(raise_exception=True):
            username = serializers.data.get('username')
            password = serializers.data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'the user login was sucessfull'},status = status.HTTP_200_OK)

            else:
                return Response({'errors':{'non_field_errors':'the username or password is incorrect'}},status= status.HTTP_404_NOT_FOUND)    

class UserChangePasswordView(APIView):
    permission_classes =[IsAuthenticated]
    def post(self,request,format=None):
        serializers = ChangeUserSerializers(data=request.data,context={'user':request.user})
        if serializers.is_valid(raise_exception=True):
            return Response({'msg':'the password is changed sucessfully'},status = status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)        



