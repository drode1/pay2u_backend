from rest_framework import serializers

from app.subscriptions.api.serializers import SubscriptionBaseReadOutputSerializer
from app.subscriptions.models import ClientCashbackHistory
from app.subscriptions.services import update_cashback_history_status
from app.users.models import User


class UserBankAccountSerializer(serializers.Serializer):
    name = serializers.CharField()
    number = serializers.CharField()
    balance = serializers.IntegerField()


class UserReadOutputSerializer(serializers.ModelSerializer):
    subscriptions_count = serializers.SerializerMethodField(
        method_name='get_subscriptions_count'
    )
    month_cashback = serializers.SerializerMethodField(
        method_name='get_month_cashback'
    )
    bank_accounts = serializers.SerializerMethodField(
        method_name='get_user_bank_accounts'
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
            'bank_accounts',
        )

    def get_subscriptions_count(self, obj: User):
        return obj.get_active_subscriptions_count

    def get_month_cashback(self, obj: User):
        return obj.get_month_cashback

    def get_user_bank_accounts(self, obj) -> list[dict[str, str]]:
        # It`s mock function, not for production
        return UserBankAccountSerializer(
            obj.get_user_bank_accounts,
            many=True
        ).data


class UserCashbackHistoryInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCashbackHistory
        fields = (
            'status',
        )

    def update(self, instance, validated_data):
        update_cashback_history_status(instance, validated_data.get('status'))
        return instance


class UserCashbackHistoryOutputSerializer(serializers.ModelSerializer):
    invoice_id = serializers.SerializerMethodField(
        method_name='get_invoice_id'
    )
    subscription = serializers.SerializerMethodField(
        method_name='get_subscription'
    )

    class Meta:
        model = ClientCashbackHistory
        fields = (
            'id',
            'client',
            'amount',
            'status',
            'subscription',
            'invoice_id',
            'created_at',
        )

    def get_invoice_id(self, obj):
        return obj.client_subscription.invoice.id

    def get_subscription(self, obj):
        return SubscriptionBaseReadOutputSerializer(
            obj.client_subscription.subscription, many=False
        ).data
