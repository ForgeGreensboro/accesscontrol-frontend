# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20160812_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]