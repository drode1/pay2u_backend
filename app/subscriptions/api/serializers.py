from typing import Any

from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from app.subscriptions.api.exceptions import CurrentUserSubscriptionExists
from app.subscriptions.models import (
    Cashback,
    Category,
    ClientSubscription,
    Favourite,
    Invoice,
    Subscription,
    SubscriptionBenefits,
    Tariff,
)
from app.subscriptions.services import (
    calculate_cashback_amount,
    create_new_user_subscription,
    is_current_user_subscription_exists,
    validate_tariff_subscription,
)
from app.users.models import User


class CategoryReadOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class CashbackReadOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashback
        fields = (
            'id',
            'amount',
        )


class TariffReadOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = (
            'id',
            'name',
            'days_amount',
            'amount',
            'description',
        )


class SubscriptionBenefitsReadOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionBenefits
        fields = (
            'id',
            'icon',
            'benefit',
        )


class UserSubscriptionCreteInputSerializer(serializers.ModelSerializer):
    subscription = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.without_trashed(),
    )
    tariff = serializers.PrimaryKeyRelatedField(
        queryset=Tariff.objects.without_trashed()
    )
    charge_account = serializers.CharField()
    client = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        write_only=True
    )

    class Meta:
        model = ClientSubscription
        fields = (
            'subscription',
            'tariff',
            'charge_account',
            'is_auto_pay',
            'client',
        )

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        subscription: Subscription = attrs.get('subscription')
        tariff: Tariff = attrs.get('tariff')
        client: User = attrs.get('client')

        validate_tariff_subscription(
            tariff.id,
            subscription.id,
            True,
        )
        if is_current_user_subscription_exists(client, subscription):
            raise CurrentUserSubscriptionExists

        return attrs

    def create(self, validated_data: dict[str, Any]) -> dict[str, Any]:
        create_new_user_subscription(validated_data)
        return validated_data


class UserSubscriptionUpdateInputSerializer(serializers.ModelSerializer):
    client = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        write_only=True
    )

    class Meta:
        model = ClientSubscription
        fields = (
            'is_auto_pay',
            'client',
        )


class SubscriptionBaseReadOutputSerializer(serializers.ModelSerializer):
    cashback = CashbackReadOutputSerializer()
    category = CategoryReadOutputSerializer()
    subscription_benefits = serializers.SerializerMethodField(
        method_name='get_subscription_benefits'
    )
    is_liked = serializers.SerializerMethodField(
        method_name='get_is_liked'
    )

    class Meta:
        model = Subscription
        fields = (
            'id',
            'popularity',
            'name',
            'image_preview',
            'image_detail',
            'description',
            'conditions',
            'is_recommended',
            'category',
            'cashback',
            'subscription_benefits',
            'is_liked',
        )

    @extend_schema_field(SubscriptionBenefitsReadOutputSerializer(many=True))
    def get_subscription_benefits(self, obj: Subscription) -> dict:
        benefits = SubscriptionBenefits.objects.filter(subscription_id=obj.id)
        return SubscriptionBenefitsReadOutputSerializer(
            benefits,
            many=True
        ).data

    def get_is_liked(self, obj: Subscription) -> bool:
        request = self.context.get('request')
        return (obj.subscription_favourite.filter(
            client=request.user
        ).exists() if request else True)


class SubscriptionReadOutputSerializer(SubscriptionBaseReadOutputSerializer):
    tariffs = serializers.SerializerMethodField(
        method_name='get_tariffs'
    )

    class Meta:
        model = Subscription
        fields = (
            'id',
            'popularity',
            'name',
            'image_preview',
            'image_detail',
            'description',
            'conditions',
            'is_recommended',
            'category',
            'cashback',
            'tariffs',
            'subscription_benefits',
            'is_liked',
        )

    @extend_schema_field(TariffReadOutputSerializer(many=True))
    def get_tariffs(self, obj: Subscription) -> dict:
        tarrifs = Tariff.objects.filter(subscription_id=obj.id)
        return TariffReadOutputSerializer(tarrifs, many=True).data


class InvoiceReadOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'id',
            'amount',
            'date',
        )


class UserSubscriptionOutputSerializer(serializers.ModelSerializer):
    subscription = SubscriptionBaseReadOutputSerializer()
    tariff = TariffReadOutputSerializer()
    invoice = InvoiceReadOutputSerializer()
    cashback_amount = serializers.SerializerMethodField(
        method_name='get_cashback_amount'
    )

    class Meta:
        model = ClientSubscription
        fields = (
            'id',
            'subscription',
            'tariff',
            'invoice',
            'expiration_date',
            'is_active',
            'is_auto_pay',
            'cashback_amount',
            'deleted_at',
        )

    def get_cashback_amount(self, obj: ClientSubscription) -> int:
        return calculate_cashback_amount(
            obj.tariff.amount,
            obj.subscription.cashback.amount
        )


class FavouriteInputSerializer(serializers.ModelSerializer):
    subscription = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.without_trashed()
    )
    client = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favourite
        fields = (
            'subscription',
            'client',
        )


class FavouriteOutputSerializer(serializers.ModelSerializer):
    subscription = SubscriptionReadOutputSerializer()

    class Meta:
        model = Favourite
        fields = (
            'id',
            'subscription',
            'client',
        )
