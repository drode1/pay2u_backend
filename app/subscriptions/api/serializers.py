from rest_framework import serializers

from app.subscriptions.models import Cashback, Category, Subscription, Tariff


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
            'amount',
            'description',
        )


class SubscriptionReadOutputSerializer(serializers.ModelSerializer):
    category = CategoryReadOutputSerializer()
    cashback = CashbackReadOutputSerializer()
    tariffs = serializers.SerializerMethodField(
        method_name='get_tariffs'
    )

    class Meta:
        model = Subscription
        fields = (
            'id',
            'name',
            'image',
            'description',
            'is_recommended',
            'category',
            'cashback',
            'tariffs',
        )

    @staticmethod
    def get_tariffs(obj):
        tarrifs = Tariff.objects.filter(subscription_id=obj.id)
        return TariffReadOutputSerializer(tarrifs, many=True).data
