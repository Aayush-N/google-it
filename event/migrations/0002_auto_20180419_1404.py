# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-19 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswers',
            old_name='uid',
            new_name='user',
        ),
    ]
