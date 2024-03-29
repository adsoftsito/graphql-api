# Generated by Django 3.1.3 on 2022-01-20 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('precios', '0006_lista_tipolista'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.TextField(blank=True)),
                ('nombre', models.TextField(blank=True)),
                ('direccion', models.TextField(blank=True)),
                ('cp', models.IntegerField()),
                ('usocfdi', models.TextField(default='G03')),
                ('metododepago', models.TextField(default='PUE')),
                ('formadepago', models.TextField(default='01')),
                ('tipocomprobante', models.TextField(default='E')),
                ('listacompra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proveedor', to='precios.lista')),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
