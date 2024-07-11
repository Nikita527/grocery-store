# Generated by Django 5.0.7 on 2024-07-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=150,
                unique=True,
                verbose_name="Адрес электроной почты",
            ),
        ),
    ]