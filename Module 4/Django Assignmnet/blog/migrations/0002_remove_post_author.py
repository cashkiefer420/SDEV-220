# Generated by Django 5.1.8 on 2025-04-29 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
    ]
