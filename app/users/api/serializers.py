from rest_framework import serializers

from app.users.models import User


class UserReadOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            ...  # TODO дозаполнить полями
        )
