from django.db import models

from app.core.models import BaseModel


class Category(BaseModel):

    name = models.TextField(
        'Name',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'
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
        return f'Cashback {self.amount}'


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
        db_table = 'invoice'
        ordering = (
            'id',
            'date',
        )

    def __repr__(self):
        return f'Invoice {self.id}'

    def __str__(self):
        return f'Invoice {self.amount}'
