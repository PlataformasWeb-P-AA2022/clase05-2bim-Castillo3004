# Generated by Django 4.0.5 on 2022-07-05 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Autos',
            new_name='Auto',
        ),
        migrations.RenameModel(
            old_name='Motos',
            new_name='Moto',
        ),
    ]