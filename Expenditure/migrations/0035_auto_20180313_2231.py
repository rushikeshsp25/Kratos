# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-13 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Expenditure', '0034_auto_20180313_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credits',
            name='date_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='debits',
            name='date_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
