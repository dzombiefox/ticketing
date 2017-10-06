# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 04:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0001_initial'),
        ('maintenance', '0002_requestperbaikan'),
    ]

    operations = [
        migrations.CreateModel(
            name='PemakaianBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('keterangan', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.Barang')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.RequestPerbaikan')),
                ('satuan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.Satuan')),
            ],
        ),
    ]
