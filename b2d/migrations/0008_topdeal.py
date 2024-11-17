# Generated by Django 5.1.1 on 2024-11-16 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("b2d", "0007_investment_shares"),
    ]

    operations = [
        migrations.CreateModel(
            name="TopDeal",
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
                ("display_order", models.PositiveIntegerField()),
                (
                    "fundraising",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="b2d.fundraising",
                    ),
                ),
            ],
        ),
    ]
