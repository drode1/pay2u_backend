# Generated by Django 4.2 on 2024-03-30 23:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0014_alter_clientsubscription_expiration_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientsubscription",
            name="expiration_date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 30, 2, 35, 22, 624419),
                verbose_name="expiration_date",
            ),
        ),
    ]
