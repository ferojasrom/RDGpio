# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RDGpio', '0002_auto_20161108_0955'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GPIO',
            new_name='GPIOs',
        ),
    ]
