# Generated by Django 5.1 on 2024-11-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2d', '0006_alter_fundraising_shares'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='shares',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
    ]
