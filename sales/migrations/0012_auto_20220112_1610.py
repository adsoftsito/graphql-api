# Generated by Django 3.1.3 on 2022-01-12 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0005_auto_20220112_1603'),
        ('sales', '0011_auto_20220109_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='claveunidad',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='codigosat',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='noidentificacion',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='url',
        ),
        migrations.AlterField(
            model_name='detail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='links.link'),
        ),
    ]
