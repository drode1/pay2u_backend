from rest_framework import serializers


class TokenInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        label='user_id',
        required=True,
        min_value=1
    )


class TokenOutputSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    access_token = serializers.CharField()
