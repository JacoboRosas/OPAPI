# Generated by Django 5.1.1 on 2024-10-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DevilFruit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devilfruit',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='devilfruit',
            name='df_jp_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='devilfruit',
            name='df_name',
            field=models.CharField(max_length=50),
        ),
    ]