# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_auto_20170529_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pemakaianbarang',
            old_name='requestid',
            new_name='request',
        ),
    ]
