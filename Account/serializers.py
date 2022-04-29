from rest_framework import serializers
from django.contrib.auth.models import User

class Myuser(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','password','password2']
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
class userlogin(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields=['username','password']
class ChangeUserSerializers(serializers.Serializer):
    password = serializers.CharField(max_length=100,style={'input_type':'password'},write_only=True)
    password2 =serializers.CharField(max_length=100,style={'input_type':'password'},write_only=True)
    class Meta:
        fields =['password','passsword2']

    def validate(self,attrs):
        password = attrs.get('password')    
        password = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError('New password and Confirm password deesnot match')

        user.set_password(password)    
        user.save()
        return attrs


