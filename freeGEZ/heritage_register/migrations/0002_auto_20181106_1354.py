# Generated by Django 2.1.2 on 2018-11-06 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heritage_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relic',
            name='address',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='relic',
            name='date_from',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='relic',
            name='date_to',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='relic',
            name='description',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='relic',
            name='forms_of_protection',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='relic',
            name='place',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='relic',
            name='time_of_creation',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
