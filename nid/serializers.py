from rest_framework import serializers
from .models import NID

class NIDSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = NID
        fields = ['id', 'user', 'nid', 'photo']
        read_only_fields = ['user']
    
    def validate_nid(self, value):
        if len(value) != 16:
            raise serializers.ValidationError("NID must be exactly 16 digits long.")
        
        if not value.isdigit():
            raise serializers.ValidationError("NID must contain only numeric digits.")
        
        user = self.context['request'].user
        if NID.objects.filter(user=user).exists():
            raise serializers.ValidationError("NID has already been registered for this user.")
        
        return value
