# Generated by Django 5.1.1 on 2024-12-08 15:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("b2d", "0010_alter_business_options_alter_investor_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="investor",
            options={
                "permissions": [
                    ("view_portfolio", "Can view portfolio"),
                    ("make_investment", "Can make investment"),
                    ("update_investor_profile", "Can update investor profile"),
                ],
                "verbose_name": "Investor Registration",
                "verbose_name_plural": "Investor Registrations",
            },
        ),
    ]
