# Generated by Django 3.1.3 on 2022-01-12 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat40', '0002_claveprodserv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claveprodserv',
            old_name='similar',
            new_name='sinonimos',
        ),
    ]
