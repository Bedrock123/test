# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-16 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarperUser', '0017_auto_20170716_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='patient_email_notifications',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=120, verbose_name='Would you like to notify your patients using harper that you have signed up?'),
        ),
    ]
