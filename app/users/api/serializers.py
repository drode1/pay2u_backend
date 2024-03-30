from rest_framework import serializers

from app.users.models import User


class UserReadOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'phone',
        )
