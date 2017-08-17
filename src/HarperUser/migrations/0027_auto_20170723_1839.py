# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-23 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarperUser', '0026_auto_20170723_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='what_health_care_type',
            field=models.CharField(default='', max_length=120, verbose_name='What medical field are you in?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='what_medical_type_are_you',
            field=models.CharField(choices=[('Nurse', 'Nurse'), ('Doctor', 'Doctor'), ('Physicians Assistant', 'Physicians Assistant'), ('Dentist', 'Dentist'), ('Other', 'Other')], default='Doctor', max_length=120, verbose_name='What kind of medical professional are you?'),
        ),
    ]
