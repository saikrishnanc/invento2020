# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('gen', 'General'), ('cse', 'CSE'), ('it', 'IT'), ('me', 'ME'), ('ec', 'ECE'), ('eee', 'EEE')], default='gen', max_length=3),
        ),
    ]
