from rest_framework.views import APIView
from rest_framework import status
from .serializers import Myuserserializers, Userloginserializers, ChangeUserSerializers,GetallUserserilaizers,CreateGroupForUserserializer, Addadminuserserializers, Addemployeeuserserializers, Employeeuserserializers, Allusertaskserializer, Addadningroupserializers, Adminuserserializer, SpecificUserserializers
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth import authenticate
from .renenders import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from CustomerDetails.models import Adminassigment, Userassigment
from django.contrib.auth.models import Group, User

from django.db import connection
from django.http import JsonResponse



"""this is code to get the token for the requested user """

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    """this is the code to assign the task to the group by admin himself"""
class AddGroupAdminUser(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request,format=None):
       
        serializers = CreateGroupForUserserializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response('the user was added to the given group')
"""this is code to get all the information about the user a group done by admin himself"""
class ViewAllUserinsideGroup(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request,format=None):
        serializers = GetallUserserilaizers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        group_name_insert = serializers.data.get('group_name')
        print(group_name_insert)
        group_exit=Group.objects.filter(name=group_name_insert).first()
        all_user = User.objects.filter(groups=group_exit)
        serializer = SpecificUserserializers(all_user,many=True)
        return Response(serializer.data)


"""this is the code to register new user"""
class userregistrationView(APIView):
    renender_classes = [UserRenderer]

    def post(self, request, format=None):
        serializers = Myuserserializers(data=request.data)

        if serializers.is_valid(raise_exception=True):
            user = serializers.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'the user was sucessfully created'}, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

"""this is the code to login the resgistered user """
class UserLoginView(APIView):

    def post(self, request, format=None):
        serializers = Userloginserializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            username = serializers.data.get('username')
            password = serializers.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'the user login was sucessfull'}, status=status.HTTP_200_OK)

            else:
                return Response({'errors': {'non_field_errors': 'the username or password is incorrect'}}, status=status.HTTP_404_NOT_FOUND)
"""this is code to change the password of registered user """

class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        print(request.user)
        serializers = ChangeUserSerializers(
            data=request.data, context={'user': request.user})
        if serializers.is_valid(raise_exception=True):
            return Response({'msg': 'the password is changed sucessfully'}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

"""this is code to get and post the user task by admin"""
class AddallAdminuser(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        alluser_task = Userassigment.objects.all()
        serializers = Allusertaskserializer(alluser_task, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = Addadminuserserializers(data=request.data)
           
        serializer.is_valid(raise_exception=True)
    
        serializer.save()
        return Response('The user was submitted with the given task', status=status.HTTP_201_CREATED)

        

"""this is code to get the particular use,update the user task by admin,delete the user task by admin"""
class AddAdminUser(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, id, format=None):
        try:

            particular_user = Userassigment.objects.get(id=id)
            serializers = Allusertaskserializer(particular_user)
            return Response(serializers.data)

        except Userassigment.DoesNotExist:
            return Response('the user is not under your control')

    def put(self, request, id, format=None):
        instance = Userassigment.objects.filter(id=id).first()
        if not instance:
            return Response({'deatils':'assignment doesnot exit'},status=status.HTTP_400_BAD_REQUEST)
        serializers = Adminuserserializer(instance, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

       

    def delete(self, request, id, format=None):
        instance = Userassigment.objects.get(id=id).delete()

        return Response('the user instance is deleted', status=status.HTTP_201_CREATED)

"""this is code to assign task to a particular user if the tasking doing user and task giving user are same group"""

class addemployeeuser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        currentuser_task = Userassigment.objects.filter(user=request.user)
        serializer = Employeeuserserializers(currentuser_task, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Addemployeeuserserializers(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response('the task has been assinged with the user inside your group', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""the is code to assign the task and get to the request group by admin"""
class AddGroupAdmin(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        group_data = Adminassigment.objects.all()
        serializers = Addadningroupserializers(group_data,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = Addadningroupserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response('The group has assigned with the task', status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class GetEmployeeuser(APIView):
    """this is the code to update and get the particular user task by user"""
    permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        user = request.user

        try:
            Emplooyee_user = Userassigment.objects.get(id=id, created_by=user)
            print(Emplooyee_user)
            serializers = Adminuserserializer(Emplooyee_user)
            return Response(serializers.data)
        except Userassigment.DoesNotExist:
            return Response('The requested user task is not available')

    def put(self, request, id, format=None):
        try:
            instance = Userassigment.objects.get(
                id=id, created_by=request.user)
            serializers = Adminuserserializer(instance, data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)

            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Userassigment.DoesNotExist:
            return Response('The user task  is not available for update')

    def delete(self, request, id, format=None):
        try:
            instance = Userassigment.objects.get(
                id=id, created_by=request.user).delete()
            return Response('the user has been sucessfully deleted')
        except userassigment.DoesNotExist:
            return Response('The user is not available to delete')

"""this is the code to to get all the user inside group user """ 
class RequestGroupUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        current_user = self.request.user
        current_group = Group.objects.get(user=current_user)
        user_inside_group = User.objects.filter(groups=current_group)
        serializers = SpecificUser(user_inside_group, many=True)
        return Response(serializers.data)
"""the is the code to get the schema of request.user """
