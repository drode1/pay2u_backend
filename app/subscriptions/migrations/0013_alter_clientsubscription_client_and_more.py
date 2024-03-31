# Generated by Django 4.2 on 2024-03-30 22:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("subscriptions", "0012_alter_clientsubscription_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientsubscription",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_client_subscription",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Client",
            ),
        ),
        migrations.AlterField(
            model_name="clientsubscription",
            name="expiration_date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 30, 1, 20, 29, 361267),
                verbose_name="expiration_date",
            ),
        ),
        migrations.AlterField(
            model_name="clientsubscription",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invoice_client_subscription",
                to="subscriptions.invoice",
                verbose_name="Invoice",
            ),
        ),
        migrations.AlterField(
            model_name="clientsubscription",
            name="promocode",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="promocode_client_subscription",
                to="subscriptions.promocode",
                verbose_name="Promocode",
            ),
        ),
        migrations.AlterField(
            model_name="clientsubscription",
            name="subscription",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscription_client_subscription",
                to="subscriptions.subscription",
                verbose_name="Subscription",
            ),
        ),
        migrations.AlterField(
            model_name="clientsubscription",
            name="tariff",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tariff_client_subscription",
                to="subscriptions.tariff",
                verbose_name="Tariff",
            ),
        ),
    ]
