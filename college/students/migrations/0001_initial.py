# Generated by Django 5.0.7 on 2024-08-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=250, unique=True)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
