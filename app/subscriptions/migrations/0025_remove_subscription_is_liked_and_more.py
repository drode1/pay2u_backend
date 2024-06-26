# Generated by Django 4.2 on 2024-04-01 11:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("subscriptions", "0024_remove_clientsubscription_is_liked_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="is_liked",
        ),
        migrations.AlterField(
            model_name="clientsubscription",
            name="expiration_date",
            field=models.DateField(
                default=datetime.datetime(2024, 5, 1, 14, 29, 24, 94259),
                verbose_name="expiration_date",
            ),
        ),
        migrations.CreateModel(
            name="Favourite",
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
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_favourite",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Client",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="subscription_favourite",
                        to="subscriptions.subscription",
                        verbose_name="Subscription",
                    ),
                ),
            ],
            options={
                "verbose_name": "Favourite",
                "verbose_name_plural": "Favourites",
                "db_table": "favourites",
                "ordering": ("id",),
            },
        ),
        migrations.AddConstraint(
            model_name="favourite",
            constraint=models.UniqueConstraint(
                fields=("client", "subscription"), name="unique_favourite"
            ),
        ),
    ]
