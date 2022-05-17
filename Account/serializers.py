from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group 
from CustomerDetails.models import Adminassigment,Userassigment
class GetallUserserilaizers(serializers.ModelSerializer):
   
    class Meta:
        model = Group
        fields=['id']
   
    def create(self,validate_data):
        
        
        
        
        return validate_data

class CreateGroupForUserserializer(serializers.Serializer):
    group_name = serializers.CharField()
    user = serializers.CharField()

    def create(self,validate_data):
        group_name_insert = validate_data['group_name']
        instance = User.objects.filter(id=validate_data['user']).first()
        group_created,created = Group.objects.get_or_create(name=group_name_insert)
        print(group_created)
        user_group_created = group_created.user_set.add(instance)
        print(group_created)
        return group_created

class SpecificUserserializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields =['id','username']


class Allusertaskserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Userassigment
        fields=['id','user','work_Description','metting_description','metting_scheldule','completed']
class Myuserserializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
  
    class Meta:
        model=User
        fields=['username','password','password2','email']
        extra_kwargs={
      'password':{'write_only':True}
    }


    def validate(self,attrs):
        password=attrs.get('password') 
        password2=attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError('confirm password and password doesnot match')

        return attrs


    def create(self, validated_data):
        validated_data.pop('password2')
        
       

        user = User.objects.create_user(**validated_data)     


        return user
class Userloginserializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields=['username','password']


class ChangeUserSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100,style={'input_type':'password'},write_only=True)
    password2 =serializers.CharField(max_length=100,style={'input_type':'password'},write_only=True)
    class Meta:
        fields =['password','passsword2']

    def validate(self,attrs):
        password = attrs.get('password')    
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError('New password and Confirm password deesnot match')

        user.set_password(password)    
        user.save()
        return attrs


class Adminuserserializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Userassigment 
        fields =['work_Description','metting_description','metting_scheldule','completed','image','created_by']
    def update(self,instance,validate_data):
        print(validate_data.get('work_Description'))
        print(instance.work_Description)
        instance.work_Description =validate_data.get('work_Description', instance.work_Description) 
        print(instance.work_Description)
        instance.metting_description = validate_data.get('metting_description',instance.metting_description)    
        instance.metting_scheldule = validate_data.get('metting_scheldule',instance.metting_scheldule)   
        instance.completed = validate_data.get('completed',instance.completed)
        instance.image = validate_data.get('image',instance.image)
        instance.save()
        return instance


class Addadminuserserializers(serializers.ModelSerializer):
    
    class Meta:
        model =Userassigment
        fields =['user','work_Description','metting_description','metting_scheldule','completed','created_by','image']

    def create(self,validate):
        
        try:
           
            Name = User.objects.get(username=validate['user'])  
            admin_user = Userassigment.objects.create(
                user=Name,
                work_Description=validate['work_Description'],
                metting_description=validate['metting_description'],
                metting_scheldule=validate['metting_scheldule'],
                completed=validate['completed'],
                created_by=self.context.get('request').user,
                image=validate['image']
            )

        except User.DoesNotExist:
            raise serializers.ValidationError('The user does not exit ')

        return admin_user 

    


class Employeeuserserializers(serializers.ModelSerializer):
    class Meta:
        model = Userassigment
        fields= ['work_Description','metting_description','metting_scheldule','completed','created_by']  

class Addemployeeuserserializers(serializers.ModelSerializer):
   
    class Meta:
        model = Userassigment
        fields = ['user','work_Description','metting_description','metting_scheldule','completed','created_by','image']

    def validate(self,attrs):
        
        current_user = self.context.get('request').user
        name=attrs['user']
        print(name)
        
        print(current_user)
        try:
            current_group = Group.objects.get(user= current_user)
            print(current_group)
            try:
                user_insert = User.objects.get(username=attrs['user'],groups=current_group)

            except User.DoesNotExist:   
                raise serializers.ValidationError('The user does not exit or not in group ')  

            
        except Group.DoesNotExist:
            raise serializers.ValidationError('The user is  not associated with your group')  

        return attrs      


    def create(self,validate):
        

        current_user = self.context.get('request').user
        try:
            print(validate['user'])
            current_group = Group.objects.get(user= current_user)
            user_insert = User.objects.get(username=validate['user'],groups=current_group)
            employee_user = Userassigment.objects.create(user=user_insert,work_Description=validate['work_Description'],metting_description=validate['metting_description'],metting_scheldule=validate['metting_scheldule'],completed=validate['completed'],created_by=current_user,image=validate['image'])
        except User.DoesNotExist:
            raise serializers.ValidationError('The user does not exit ')

        return employee_user    
    



class Addadningroupserializers(serializers.ModelSerializer):

   
    class Meta:
        model = Adminassigment
        fields = ['assigned_group','work_Description','metting_description','metting_scheldule','completed','image']


   



    
    def create(self,validate_data):
        
        try:
        
            group_name = Group.objects.get(name = validate_data['assigned_group'])
            admin_group_works = Adminassigment.objects.create(assigned_group=group_name,metting_scheldule=validate_data['metting_scheldule'],work_Description=validate_data['work_Description'],metting_description=validate_data['metting_description'],image=validate_data['image'])
            return admin_group_works

        except Group.DoesNotExist:
            raise serializers.ValidationError('the request group is not available')    

            

            


