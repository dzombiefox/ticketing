# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0006_pinjambarang_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengembalianbarang',
            name='barang',
        ),
        migrations.AddField(
            model_name='pengembalianbarang',
            name='pinjam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='loan.PinjamBarang'),
            preserve_default=False,
        ),
    ]