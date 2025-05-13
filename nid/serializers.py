from rest_framework import serializers
from .models import NID, NIDUser




class NIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = NID
        fields = '__all__'


class NIDUserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = NIDUser
        fields = '__all__'
