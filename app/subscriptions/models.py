import secrets
import string
from datetime import datetime, timedelta

from django.conf import settings as s
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from django.db.models import CheckConstraint, Q

from app.core.models import BaseModel
from app.subscriptions.enums import CashbackHistoryStatus, SubscriptionPeriod
from app.users.models import User


class Category(BaseModel):
    name = models.TextField(
        'Name',
        unique=True,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'
        ordering = (
            'id',
            'name',
        )

    def __repr__(self):
        return f'Category {self.id}'

    def __str__(self):
        return self.name


class Cashback(BaseModel):
    amount = models.PositiveSmallIntegerField(
        'Amount',
        null=False,
        blank=False,
        validators=[
            MinValueValidator(s.MIN_CASHBACK_VALUE),
            MaxValueValidator(s.MAX_CASHBACK_VALUE)
        ],
    )

    class Meta:
        verbose_name = 'Cashback'
        verbose_name_plural = 'Cashback'
        db_table = 'cashback'
        ordering = (
            'id',
            'amount',
        )

        constraints = (
            CheckConstraint(
                check=Q(amount__gte=s.MIN_CASHBACK_VALUE) & Q(
                    amount__lte=s.MAX_CASHBACK_VALUE),
                name='min_max_range'),
        )

    def __repr__(self):
        return f'Cashback {self.id}'

    def __str__(self):
        return str(self.amount)


class Invoice(BaseModel):
    amount = models.PositiveIntegerField(
        'Amount',
        null=False,
        blank=False,
        validators=[
            MinValueValidator(s.MIN_AMOUNT_VALUE),
        ],
    )
    date = models.DateTimeField(
        'Date',
        auto_now=True,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        db_table = 'invoices'
        ordering = (
            'id',
            'date',
        )

    def __repr__(self):
        return f'Invoice {self.id}'

    def __str__(self):
        return f'{self.id}'


class Promocode(BaseModel):
    """Activation subscription code model"""
    name = models.CharField(
        'Name',
        blank=False,
        null=False,
        unique=True,
    )
    is_active = models.BooleanField(
        'Is active',
        blank=False,
        null=False,
        default=True,
    )

    class Meta:
        verbose_name = 'Promocode'
        verbose_name_plural = 'Promocodes'
        db_table = 'promocodes'
        ordering = (
            'id',
            'name',
            'is_active',
        )

    def __repr__(self):
        return f'Promocode {self.id}'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            # Generate random activate code with 6 symbols
            code_length = 6
            while True:
                code = ''.join(
                    secrets.choice(string.ascii_uppercase + string.digits)
                    for _ in range(code_length)
                )
                if not Promocode.objects.filter(name=code).exists():
                    self.name = code
                    break
        super().save(*args, **kwargs)

    def activate(self):
        """
        Activate subscription promocode and deactivate if for further
        activation possibilities
        """
        self.is_active = False
        self.soft_delete()
        self.save()


class SubscriptionBenefits(BaseModel):
    subscription = models.ForeignKey(
        'Subscription',
        verbose_name='Subscription',
        related_name='subscription_benefit',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    icon = models.FileField(
        'Icon',
        upload_to='subscriptions/benefits',
        blank=False,
        null=False,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png', 'svg'])
        ]
    )
    benefit = models.TextField(
        'Benefit',
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Subscription benefit'
        verbose_name_plural = 'Subscription benefits'
        db_table = 'subscription_benefits'
        ordering = (
            'id',
        )

    def __repr__(self):
        return f'Subscription benefit {self.id}'

    def __str__(self):
        return str(self.id)


class Subscription(BaseModel):
    name = models.CharField(
        'Name',
        blank=False,
        null=False,
    )
    description = models.TextField(
        'Description',
        null=False,
        blank=False,
    )
    cashback = models.ForeignKey(
        Cashback,
        verbose_name='Cashback',
        related_name='subscription_cashback',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Category',
        related_name='subscription_category',
        on_delete=models.RESTRICT,
        null=True,
        blank=False,
    )
    is_recommended = models.BooleanField(
        'Is recommended',
        blank=False,
        null=False,
        default=False,
    )
    image_preview = models.ImageField(
        'Preview Image',
        upload_to='subscriptions/',
        blank=False,
        null=False,
    )
    image_detail = models.ImageField(
        'Detail Image',
        upload_to='subscriptions/',
        blank=False,
        null=False,
    )
    popularity = models.PositiveIntegerField(
        'Popularity',
        blank=False,
        null=False,
        default=0
    )

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        db_table = 'subscriptions'
        ordering = (
            'id',
            'name',
            'category',
            'is_recommended',
        )

    def __repr__(self):
        return f'Subscription {self.id}'

    def __str__(self):
        return self.name

    def calculate_popularity(self):
        count = self.subscription_client_subscription.count()
        if count > 0:
            self.popularity = count * self.id * 10
        else:
            self.popularity = self.id


class Favourite(BaseModel):
    client = models.ForeignKey(
        User,
        verbose_name='Client',
        related_name='client_favourite',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    subscription = models.ForeignKey(
        Subscription,
        verbose_name='Subscription',
        related_name='subscription_favourite',
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'
        db_table = 'favourites'
        ordering = (
            'id',
        )
        constraints = (
            models.UniqueConstraint(
                fields=['client', 'subscription'],
                name='unique_favourite'
            ),
        )

    def __repr__(self):
        return f'Favourite {self.id}'

    def __str__(self):
        return str(self.id)


class Tariff(BaseModel):
    days_amount = models.PositiveIntegerField(
        'Days amount',
        blank=False,
        null=False,
        choices=SubscriptionPeriod.choices,
        default=SubscriptionPeriod.ONE_MONTH.value,
    )
    subscription = models.ForeignKey(
        Subscription,
        verbose_name='Subscription',
        related_name='subscription_tariff',
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
    )
    amount = models.PositiveIntegerField(
        'Amount',
        null=False,
        blank=False,
        validators=[
            MinValueValidator(s.MIN_AMOUNT_VALUE),
        ],
    )
    description = models.TextField(
        'Description',
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Tariff'
        verbose_name_plural = 'Tariffs'
        db_table = 'tariffs'
        ordering = (
            'id',
            'subscription',
            'amount',
        )

    def __repr__(self):
        return f'Tariff {self.id}'

    def __str__(self):
        return str(self.id)

    @property
    def name(self):
        return SubscriptionPeriod(self.days_amount).label


class ClientSubscription(BaseModel):
    client = models.ForeignKey(
        User,
        verbose_name='Client',
        related_name='user_client_subscription',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    subscription = models.ForeignKey(
        Subscription,
        verbose_name='Subscription',
        related_name='subscription_client_subscription',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    tariff = models.ForeignKey(
        Tariff,
        verbose_name='Tariff',
        related_name='tariff_client_subscription',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    promocode = models.ForeignKey(
        Promocode,
        verbose_name='Promocode',
        related_name='promocode_client_subscription',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    expiration_date = models.DateField(
        'expiration_date',
        null=False,
        blank=False,
        default=datetime.now() + timedelta(
            days=int(SubscriptionPeriod.ONE_MONTH)
        )
    )
    invoice = models.ForeignKey(
        Invoice,
        verbose_name='Invoice',
        related_name='invoice_client_subscription',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        'Is active',
        blank=False,
        null=False,
        default=True,
    )
    is_auto_pay = models.BooleanField(
        'Is auto-renewal',
        blank=False,
        null=False,
        default=False,
    )

    class Meta:
        verbose_name = 'Client subscription'
        verbose_name_plural = 'Client Subscriptions'
        db_table = 'clients_subscriptions'
        ordering = (
            'id',
            'client',
            'subscription',
            'tariff',
            'promocode',
            'expiration_date',
            'is_active',
        )

    def __repr__(self):
        return f'Client subscription {self.id}'

    def __str__(self):
        return str(self.id)

    def check_subscription_period(self):
        from app.subscriptions.services import (
            inactivate_or_renew_user_subscription,
        )
        inactivate_or_renew_user_subscription(self)

    def clean(self):
        super().clean()

        """
        Check that tariff is linked to concrete subscription,
        but we don`t check that the tariff is deleted,
        because archive tariffs may exist
        """
        from app.subscriptions.services import (
            validate_tariff_subscription,
        )
        validate_tariff_subscription(
            self.tariff.id,
            self.subscription.id,
            False
        )
        self.check_subscription_period()


class ClientCashbackHistory(BaseModel):
    client = models.ForeignKey(
        User,
        verbose_name='Client',
        related_name='client_cashback_history',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    amount = models.PositiveIntegerField(
        'Amount',
        null=False,
        blank=False,
        validators=[
            MinValueValidator(s.MIN_AMOUNT_VALUE),
        ],
    )
    status = models.CharField(
        'Cashback status',
        blank=False,
        null=False,
        choices=CashbackHistoryStatus.choices,
        default=CashbackHistoryStatus.PENDING.value
    )
    client_subscription = models.ForeignKey(
        ClientSubscription,
        verbose_name='Client subscription',
        related_name='client_subscription_cashback_history',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )

    class Meta:
        verbose_name = 'Client cashback history'
        verbose_name_plural = 'Client cashback histories'
        db_table = 'client_cashback_history'
        ordering = (
            'id',
            'amount',
            'client',
            'status',
        )

    def __repr__(self):
        return f'Client cashback {self.id}'

    def __str__(self):
        return str(self.id)
