# Generated by Django 4.2 on 2024-04-04 19:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0032_alter_clientsubscription_expiration_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientcashbackhistory",
            name="client_subscription",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="client_subscription_cashback_history",
                to="subscriptions.clientsubscription",
                verbose_name="Client subscription",
            ),
        ),
        migrations.AlterField(
            model_name="clientsubscription",
            name="expiration_date",
            field=models.DateField(
                default=datetime.datetime(2024, 5, 4, 22, 3, 20, 80428),
                verbose_name="expiration_date",
            ),
        ),
    ]