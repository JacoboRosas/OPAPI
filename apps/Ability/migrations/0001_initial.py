# Generated by Django 5.1.1 on 2024-09-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability_name', models.CharField(max_length=40)),
                ('ability_type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
            ],
        ),
    ]
