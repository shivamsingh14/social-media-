# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-30 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20190430_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_token',
            field=models.CharField(default=b'73252', max_length=64),
        ),
    ]
