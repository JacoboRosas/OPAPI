# Generated by Django 5.1.1 on 2024-10-04 00:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pirate', '0002_remove_pirate_faction_remove_pirate_ship_name_and_more'),
        ('Ship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pirate',
            name='ship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ship.ship'),
        ),
    ]
