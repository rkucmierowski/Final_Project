# Generated by Django 2.1.2 on 2018-11-06 13:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heritage_register', '0002_auto_20181106_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relic',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='relics', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='relic',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]