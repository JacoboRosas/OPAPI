# Generated by Django 5.1.1 on 2024-10-04 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Character', '0002_remove_character_bountys'),
        ('Marine', '0002_rename_rank_marine_rank_name_remove_marine_faction'),
        ('Pirate', '0002_remove_pirate_faction_remove_pirate_ship_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='abilitys',
            new_name='ability',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='arcs',
            new_name='arc',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='devil_fruits',
            new_name='devil_fruit',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='factions',
            new_name='faction',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='hakis',
            new_name='haki',
        ),
        migrations.AddField(
            model_name='character',
            name='marine',
            field=models.ManyToManyField(to='Marine.marine'),
        ),
        migrations.AddField(
            model_name='character',
            name='pirate',
            field=models.ManyToManyField(to='Pirate.pirate'),
        ),
    ]
