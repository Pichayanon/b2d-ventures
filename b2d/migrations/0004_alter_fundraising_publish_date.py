# Generated by Django 5.1 on 2024-09-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2d', '0003_alter_fundraising_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundraising',
            name='publish_date',
            field=models.DateField(),
        ),
    ]
