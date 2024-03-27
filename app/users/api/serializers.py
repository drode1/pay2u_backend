from rest_framework import serializers

from app.users.models import User


class UserReadOutputSerializer(serializers.ModelSerializer):
    subscriptions_count = serializers.SerializerMethodField(
        method_name='get_subscriptions_count'
    )
    month_cashback = serializers.SerializerMethodField(
        method_name='get_month_cashback'
    )

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'phone',
            'subscriptions_count',
            'month_cashback',
        )

    def get_subscriptions_count(self, obj):
        raise NotImplementedError

    def get_month_cashback(self, obj):
        raise NotImplementedError
