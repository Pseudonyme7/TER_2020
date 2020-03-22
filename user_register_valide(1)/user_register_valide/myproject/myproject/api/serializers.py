from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'firstName','lastName','username','password','email')
        extra_kwargs = {'password': {'required': True}}

   


