# Generated by Django 5.1.6 on 2025-04-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artsapp', '0008_auction_start_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='start_amount',
        ),
        migrations.AddField(
            model_name='post',
            name='start_amount',
            field=models.FloatField(null=True),
        ),
    ]
