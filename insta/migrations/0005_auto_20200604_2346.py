# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-04 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_auto_20200604_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='uplikes',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
