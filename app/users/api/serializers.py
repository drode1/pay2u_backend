from rest_framework import serializers

from app.users.models import User


class UserReadOutputSerializer(serializers.ModelSerializer):
    count_sub = serializers.SerializerMethodField()
    cashback_month = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'notification_date',
            'phone',
            'count_sub',
            'cashback_mounth',
        )

    def get_count_sub(self, obj):
        # Пока не знаю, что это за поля
        raise NotImplemented

    def get_cashback_month(self, obj):
        # Пока не знаю, что это за поля
        raise NotImplemented
