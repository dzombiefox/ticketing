# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 02:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0008_auto_20170530_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailperbaikan',
            name='keterangan',
        ),
    ]
