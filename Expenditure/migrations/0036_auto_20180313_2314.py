# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-13 17:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Expenditure', '0035_auto_20180313_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debits',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='debits',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='debits',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
