# Generated by Django 4.2 on 2024-03-27 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0002_alter_category_table_alter_invoice_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Promocode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="deleted at"
                    ),
                ),
                ("name", models.CharField(verbose_name="Name")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is active"),
                ),
                ("amount", models.FloatField(verbose_name="Amount")),
            ],
            options={
                "verbose_name": "Promocode",
                "verbose_name_plural": "Promocodes",
                "db_table": "promocodes",
                "ordering": ("id", "name", "is_active", "amount"),
            },
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="deleted at"
                    ),
                ),
                ("name", models.CharField(verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "is_recommended",
                    models.BooleanField(default=False, verbose_name="Is recommended"),
                ),
                (
                    "image",
                    models.ImageField(upload_to="subscriptions/", verbose_name="Image"),
                ),
                (
                    "cashback",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subscription_cashback",
                        to="subscriptions.cashback",
                        verbose_name="Cashback id",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription_category",
                        to="subscriptions.category",
                        verbose_name="Category id",
                    ),
                ),
            ],
            options={
                "verbose_name": "Subscription",
                "verbose_name_plural": "Subscriptions",
                "db_table": "subscriptions",
                "ordering": ("id", "name", "category", "is_recommended"),
            },
        ),
        migrations.CreateModel(
            name="Tariff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="deleted at"
                    ),
                ),
                ("name", models.CharField(verbose_name="Name")),
                ("amount", models.FloatField(verbose_name="Amount")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "promocode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="promocode_tariff",
                        to="subscriptions.promocode",
                        verbose_name="Promocode id",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="promocode_subscription",
                        to="subscriptions.subscription",
                        verbose_name="Subscription id",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
