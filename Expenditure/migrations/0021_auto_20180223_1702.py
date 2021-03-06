# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-23 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expenditure', '0020_auto_20180222_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='user_info',
            name='phone_number',
            field=models.CharField(max_length=16),
        ),
    ]
