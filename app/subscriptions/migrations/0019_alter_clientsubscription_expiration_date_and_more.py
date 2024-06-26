# Generated by Django 4.2 on 2024-03-31 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0018_alter_clientsubscription_expiration_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientsubscription",
            name="expiration_date",
            field=models.DateField(
                default=datetime.datetime(2024, 4, 30, 4, 4, 10, 824725),
                verbose_name="expiration_date",
            ),
        ),
        migrations.AlterField(
            model_name="tariff",
            name="name",
            field=models.CharField(
                choices=[
                    ("30", "1 месяц"),
                    ("90", "3 месяца"),
                    ("180", "6 месяцев"),
                    ("360", "12 месяцев"),
                ],
                verbose_name="Name",
            ),
        ),
    ]
