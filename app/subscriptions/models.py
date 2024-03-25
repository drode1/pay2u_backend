from django.db import models


class Category(BaseModel):

    name = models.TextField(
        'category name',
        null=False
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
        'cashback amount',
        null=False
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


class Invoice(models.Model):

    amount = models.FloatField(
        'invoice amount',
        null=False
    )
    date = models.DateTimeField(
        'invoice date',
        auto_now=True,
        null=True,
        blank=True,
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
