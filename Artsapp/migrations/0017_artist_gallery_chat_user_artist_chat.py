# Generated by Django 5.1.6 on 2025-04-02 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artsapp', '0016_alter_bookslot_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist_Gallery_Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artsapp.artist_tbl')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artsapp.gallery_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='User_Artist_Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artsapp.artist_tbl')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artsapp.user_tbl')),
            ],
        ),
    ]
