# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-07 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarperUser', '0006_auto_20170210_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_icon',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Avatar Icon'),
        ),
    ]
