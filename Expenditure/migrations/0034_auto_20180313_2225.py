# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-13 16:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Expenditure', '0033_auto_20180313_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credits',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 13, 16, 55, 42, 996592, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='debits',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 13, 16, 55, 42, 995194, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 13, 16, 55, 42, 993538, tzinfo=utc)),
        ),
    ]
