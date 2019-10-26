from rest_framework import viewsets, permissions
from users.models import CustomUser
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer

