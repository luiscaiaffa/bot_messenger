# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-18 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_auto_20170617_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebook',
            name='recipient',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Recipient ID'),
        ),
    ]
