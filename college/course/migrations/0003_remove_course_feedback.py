# Generated by Django 5.0.7 on 2024-07-26 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_course_feedback"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="feedback",
        ),
    ]
