# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expenditure', '0002_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='debits',
            name='category',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='debits',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='debits',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='debits',
            name='system',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='debits',
            name='tax',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='debits',
            name='unit',
            field=models.CharField(default=b'kg', max_length=10),
        ),
        migrations.AlterField(
            model_name='credits',
            name='description',
            field=models.TextField(),
        ),
    ]