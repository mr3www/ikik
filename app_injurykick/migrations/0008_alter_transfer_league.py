# Generated by Django 5.1.1 on 2024-10-18 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_injurykick', '0007_transfer_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_injurykick.league', to_field='api_id'),
        ),
    ]
