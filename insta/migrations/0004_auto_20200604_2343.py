# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-04 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_image_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='likes',
            new_name='uplikes',
        ),
    ]
