from rest_framework import serializers
from .models import NID, NIDUser




class NIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = NID
        fields = '__all__'


class NIDUserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nid_data = NIDSerializer(source='nid')
    user_data = serializers.StringRelatedField(source='user')
    
    class Meta:
        model = NIDUser
        fields = '__all__'
        extra_kwargs = {
            'nid': {'write_only': True}
        }
