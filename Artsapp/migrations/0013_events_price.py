# Generated by Django 5.1.6 on 2025-04-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artsapp', '0012_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
