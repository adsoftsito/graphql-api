# Generated by Django 3.1.3 on 2022-01-02 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estacion',
            old_name='description',
            new_name='descripcion',
        ),
    ]
