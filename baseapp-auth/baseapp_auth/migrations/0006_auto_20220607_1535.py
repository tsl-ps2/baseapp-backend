# Generated by Django 3.2.12 on 2022-06-07 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permissions", "0001_initial"),
        ("users", "0005_passwordvalidation"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="permission_groups",
            field=models.ManyToManyField(
                blank=True, related_name="users", to="permissions.PermissionGroup"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="users",
                to="permissions.role",
            ),
        ),
    ]
