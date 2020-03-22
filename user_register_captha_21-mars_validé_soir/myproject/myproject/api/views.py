from rest_framework import viewsets
from .serializers import UserSerializer, UserMiniSerializer
from .models import User
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    def list(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserMiniSerializer(users, many=True)
        return Response(serializer.data)

