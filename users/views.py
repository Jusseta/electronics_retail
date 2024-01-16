from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Set user password"""
        new_user = serializer.save()
        new_user.set_password(new_user.password)
        new_user.save()
