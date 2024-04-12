# Generated by Django 4.2 on 2024-04-12 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0034_subscription_conditions_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientsubscription",
            name="expiration_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 5, 12, 14, 55, 50, 8129, tzinfo=datetime.timezone.utc
                ),
                verbose_name="expiration_date",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="conditions",
            field=models.TextField(blank=True, verbose_name="Conditions"),
        ),
    ]
