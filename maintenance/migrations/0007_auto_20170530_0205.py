# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0006_detailperbaikan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailperbaikan',
            name='perbaikan',
            field=models.ManyToManyField(to='maintenance.RequestPerbaikan'),
        ),
    ]
