# Generated by Django 5.0.7 on 2024-07-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="feedback",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
