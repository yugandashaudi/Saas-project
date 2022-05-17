from rest_framework import serializers 
from .models import Client,Domain

class ClientTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields='__all__'       