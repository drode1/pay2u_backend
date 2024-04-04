from django.db import models


class SubscriptionPeriod(models.IntegerChoices):
    ONE_MONTH = 30, '1 месяц'
    THREE_MONTH = 90, '3 месяца'
    SIX_MONTH = 180, '6 месяцев'
    TWELVE_MONTH = 360, '12 месяцев'


class CashbackHistoryStatus(models.TextChoices):
    CANCELLED = 'cancelled', 'Отменен'
    PENDING = 'pending', 'Ожидание'
    CREDITED = 'credited', 'Начислен'
