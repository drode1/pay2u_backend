# Generated by Django 4.2 on 2024-03-31 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0019_alter_clientsubscription_expiration_date_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tariff",
            options={
                "ordering": ("id", "subscription", "amount"),
                "verbose_name": "Tariff",
                "verbose_name_plural": "Tariffs",
            },
        ),
        migrations.RemoveField(
            model_name="tariff",
            name="name",
        ),
        migrations.AlterField(
            model_name="clientsubscription",
            name="expiration_date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 30, 4, 7, 8, 558179),
                verbose_name="expiration_date",
            ),
        ),
    ]
