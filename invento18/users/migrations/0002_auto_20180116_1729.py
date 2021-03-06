# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-16 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='pkd', max_length=100, verbose_name='Name of city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='college',
            field=models.CharField(default='gec pkd', max_length=255, verbose_name='Name of college'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name of User'),
        ),
    ]
