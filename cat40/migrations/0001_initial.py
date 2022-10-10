# Generated by Django 3.1.3 on 2022-01-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClaveUnidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claveunidad', models.TextField(blank=True, default='', null=True)),
                ('nombre', models.TextField(blank=True, default='', null=True)),
                ('descripcion', models.TextField(blank=True, default='', null=True)),
                ('simbolo', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
