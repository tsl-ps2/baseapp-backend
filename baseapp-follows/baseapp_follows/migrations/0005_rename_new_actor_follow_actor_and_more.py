# Generated by Django 5.0.1 on 2024-06-07 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp_follows", "0004_alter_follow_unique_together_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="follow",
            old_name="new_actor",
            new_name="actor",
        ),
        migrations.RenameField(
            model_name="follow",
            old_name="new_target",
            new_name="target",
        ),
    ]