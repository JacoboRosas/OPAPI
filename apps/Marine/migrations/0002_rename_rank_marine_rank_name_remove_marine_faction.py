# Generated by Django 5.1.1 on 2024-10-04 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Marine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marine',
            old_name='rank',
            new_name='rank_name',
        ),
        migrations.RemoveField(
            model_name='marine',
            name='faction',
        ),
    ]
