# Generated by Django 5.1.1 on 2024-09-28 20:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Faction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=20)),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Faction.faction')),
            ],
        ),
    ]
