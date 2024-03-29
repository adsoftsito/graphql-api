# Generated by Django 3.1.3 on 2022-01-16 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('links', '0007_auto_20220113_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(default='')),
                ('descuento', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField(default=0)),
                ('lista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lista', to='precios.lista')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='links.link')),
            ],
        ),
    ]
