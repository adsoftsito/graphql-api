# Generated by Django 3.1.3 on 2021-08-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20210805_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='importe',
            field=models.FloatField(default=0),
        ),
    ]
