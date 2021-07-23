# Generated by Django 2.2.24 on 2021-07-09 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("djstripe", "0008_2_5"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "price",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="djstripe.Price"
                    ),
                ),
            ],
            options={"swappable": "APPS.PAYMENTS_PLAN_MODEL",},
        ),
    ]
