# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-22 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarperUser', '0022_auto_20170722_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, max_length=60, verbose_name='Middle Name'),
        ),
    ]
