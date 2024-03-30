# Generated by Django 4.2 on 2024-03-30 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0007_alter_subscription_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="image",
        ),
        migrations.AddField(
            model_name="subscription",
            name="image_detail",
            field=models.ImageField(
                default=None, upload_to="subscriptions/", verbose_name="Detail Image"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subscription",
            name="image_preview",
            field=models.ImageField(
                default=None, upload_to="subscriptions/", verbose_name="Preview Image"
            ),
            preserve_default=False,
        ),
    ]
