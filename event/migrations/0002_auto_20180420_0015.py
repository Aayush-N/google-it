# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-19 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ManyToManyField(to='event.ImageModel'),
        ),
    ]