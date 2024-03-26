from rest_framework import serializers


class TokenOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
