from django.contrib.auth.models import User
from rest_framework import viewsets
from myproject.api.serializers import UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(User, many=True)
        return Response(serializer.data)
