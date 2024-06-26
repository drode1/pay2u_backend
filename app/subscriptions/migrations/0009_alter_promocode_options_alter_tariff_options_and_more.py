# Generated by Django 4.2 on 2024-03-30 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "subscriptions",
            "0008_remove_subscription_image_subscription_image_detail_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="promocode",
            options={
                "ordering": ("id", "name", "is_active"),
                "verbose_name": "Promocode",
                "verbose_name_plural": "Promocodes",
            },
        ),
        migrations.AlterModelOptions(
            name="tariff",
            options={
                "ordering": ("id", "name", "subscription", "amount"),
                "verbose_name": "Tariff",
                "verbose_name_plural": "Tariffs",
            },
        ),
        migrations.RemoveField(
            model_name="promocode",
            name="amount",
        ),
        migrations.RemoveField(
            model_name="tariff",
            name="promocode",
        ),
    ]
