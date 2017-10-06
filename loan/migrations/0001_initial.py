# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 08:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barang', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AsetBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaBarang', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('satuan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.Satuan')),
            ],
        ),
        migrations.CreateModel(
            name='PinjamBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peminjam', models.CharField(max_length=100)),
                ('keterangan', models.TextField(null=True)),
                ('return_plan', models.CharField(max_length=15)),
                ('return_date', models.DateField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.AsetBarang')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]