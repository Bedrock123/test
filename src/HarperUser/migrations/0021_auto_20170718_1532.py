# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-18 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarperUser', '0020_auto_20170718_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.CharField(max_length=60, null=True, verbose_name='Date of Birth'),
        ),
    ]
