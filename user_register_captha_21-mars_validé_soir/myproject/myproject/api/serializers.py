from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username','firstName','lastName','email','password')
        extra_kwargs = {'password': {'required': True}}

class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','firstName','lastName','email','password')
    # def create(self,validated_data) :
    #     user= User.objects.create_user(**validated_data)
    #     return user


