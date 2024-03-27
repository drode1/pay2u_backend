from rest_framework import serializers


class TokenInputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(
        label='user_id',
        required=True,
        min_value=1
    )
