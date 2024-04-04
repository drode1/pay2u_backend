from rest_framework import serializers

from app.subscriptions.models import ClientCashbackHistory
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

    def get_subscriptions_count(self, obj: User):
        return obj.get_active_subscriptions_count

    def get_month_cashback(self, obj: User):
        return obj.get_month_cashback


class UserCashbackHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCashbackHistory
        fields = (
            'id',
            'client',
            'amount',
            'status',
            'created_at',
        )
