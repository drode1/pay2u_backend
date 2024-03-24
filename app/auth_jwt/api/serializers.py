from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class TokenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('id',)
