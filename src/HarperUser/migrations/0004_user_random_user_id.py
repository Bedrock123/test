# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-11 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarperUser', '0003_auto_20170120_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='random_user_id',
            field=models.CharField(default='17gh3-dbqaz9', max_length=120, verbose_name='Random User Id'),
        ),
    ]
