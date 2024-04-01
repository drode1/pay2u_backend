# Generated by Django 4.2 on 2024-04-01 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0026_alter_clientsubscription_expiration_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='popularity',
            field=models.PositiveIntegerField(default=0, verbose_name='Popularity'),
        ),
        migrations.AlterField(
            model_name='clientsubscription',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 1, 22, 41, 43, 649569), verbose_name='expiration_date'),
        ),
    ]
