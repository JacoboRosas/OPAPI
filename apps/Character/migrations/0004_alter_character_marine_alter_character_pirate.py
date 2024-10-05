# Generated by Django 5.1.1 on 2024-10-04 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Character', '0003_rename_abilitys_character_ability_and_more'),
        ('Marine', '0002_rename_rank_marine_rank_name_remove_marine_faction'),
        ('Pirate', '0003_alter_pirate_ship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='marine',
            field=models.ManyToManyField(blank=True, to='Marine.marine'),
        ),
        migrations.AlterField(
            model_name='character',
            name='pirate',
            field=models.ManyToManyField(blank=True, to='Pirate.pirate'),
        ),
    ]
