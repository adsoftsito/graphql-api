# Generated by Django 3.1.3 on 2022-01-07 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receptor', '0001_initial'),
        ('sales', '0004_detail_importe'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='receptor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to='receptor.receptor'),
        ),
    ]
