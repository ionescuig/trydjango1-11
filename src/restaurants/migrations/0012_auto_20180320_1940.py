# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_auto_20180314_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='location',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
