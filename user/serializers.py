from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password", "is_staff")
        read_only_fields = ("id", "is_staff")
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 7}
        }

    def create(self, validated_data):
        """create user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)