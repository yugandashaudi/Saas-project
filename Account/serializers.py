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
