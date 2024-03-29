# Generated by Django 3.1.3 on 2022-01-03 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_colonia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidad', models.TextField(blank=True, null=True)),
                ('estado', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.TextField(blank=True, null=True)),
                ('estado', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
