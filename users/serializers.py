from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=40, min_length=6)

    class Meta:
        model = User
        fields = '__all__'
