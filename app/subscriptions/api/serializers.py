from rest_framework import serializers

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


class SubscriptionReadOutputSerializer(serializers.ModelSerializer):
    category = CategoryReadOutputSerializer()
    cashback = CashbackReadOutputSerializer()
    tariffs = serializers.SerializerMethodField(
        method_name='get_tariffs'
    )
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
            'is_recommended',
            'category',
            'cashback',
            'tariffs',
            'subscription_benefits',
            'is_liked',
        )

    @staticmethod
    def get_tariffs(obj):
        tarrifs = Tariff.objects.filter(subscription_id=obj.id)
        return TariffReadOutputSerializer(tarrifs, many=True).data

    @staticmethod
    def get_subscription_benefits(obj):
        benefits = SubscriptionBenefits.objects.filter(subscription_id=obj.id)
        return SubscriptionBenefitsReadOutputSerializer(
            benefits,
            many=True
        ).data

    def get_is_liked(self, obj: Subscription):
        return obj.subscription_favourite.filter(
            client=self.context['request'].user,
        ).exists()



class InvoiceReadOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'id',
            'amount',
            'date',
        )


class UserSubscriptionOutputSerializer(serializers.ModelSerializer):
    subscription = SubscriptionReadOutputSerializer()
    tariff = TariffReadOutputSerializer()
    invoice = InvoiceReadOutputSerializer()

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
