# Generated by Django 5.1.1 on 2024-10-09 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_injurykick', '0013_teamseasonstatistics_played_away_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamseasonstatistics',
            name='api_id',
        ),
    ]