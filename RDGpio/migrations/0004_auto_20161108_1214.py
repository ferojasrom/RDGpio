# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RDGpio', '0003_auto_20161108_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpios',
            name='pin',
            field=models.IntegerField(null=True),
        ),
    ]