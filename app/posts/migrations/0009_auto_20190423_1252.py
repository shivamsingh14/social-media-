# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-23 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20190423_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postvisibility',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
