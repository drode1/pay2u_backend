from django.db import models

from app.core.models import BaseModel


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
    amount = models.FloatField(
        'Amount',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Cashback'
        verbose_name_plural = 'Cashback'
        db_table = 'cashback'
        ordering = (
            'id',
            'amount',
        )

    def __repr__(self):
        return f'Cashback {self.id}'

    def __str__(self):
        return str(self.amount)


class Invoice(BaseModel):
    amount = models.FloatField(
        'Amount',
        null=False,
        blank=False
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
    name = models.CharField(
        'Name',
        blank=False,
        null=False,
    )
    is_active = models.BooleanField(
        'Is active',
        blank=False,
        null=False,
        default=True,
    )
    amount = models.FloatField(
        'Amount',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Promocode'
        verbose_name_plural = 'Promocodes'
        db_table = 'promocodes'
        ordering = (
            'id',
            'name',
            'is_active',
            'amount',
        )

    def __repr__(self):
        return f'Promocode {self.id}'

    def __str__(self):
        return self.name


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


class Tariff(BaseModel):
    name = models.CharField(
        'Name',
        blank=False,
        null=False,
    )
    subscription = models.ForeignKey(
        Subscription,
        verbose_name='Subscription',
        related_name='subscription_tariff',
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
    )
    promocode = models.ForeignKey(
        Promocode,
        verbose_name='Promocode',
        related_name='promocode_tariff',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    amount = models.FloatField(
        'Amount',
        null=False,
        blank=False
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
            'name',
            'subscription',
            'amount',
            'promocode',
        )

    def __repr__(self):
        return f'Tariff {self.id}'

    def __str__(self):
        return self.name
