# Generated by Django 3.1.3 on 2021-07-29 22:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='iva',
            new_name='descuento',
        ),
        migrations.AddField(
            model_name='sale',
            name='condicionesdepago',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sale',
            name='fecha',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sale',
            name='folio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sale',
            name='formapago',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sale',
            name='lugarexpedicion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sale',
            name='metodopago',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sale',
            name='moneda',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sale',
            name='serie',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sale',
            name='tipodecomprobante',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sale',
            name='totalimpuestosretenidos',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sale',
            name='totalimpuestostrasladados',
            field=models.FloatField(default=0),
        ),
    ]
