# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarperUser', '0030_auto_20170723_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='patient_email_notifications',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=120, verbose_name='Would you like your patients using harper to be able to find you account?'),
        ),
    ]
