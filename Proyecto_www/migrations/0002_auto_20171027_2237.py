# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_www', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=50, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=20, null=True, verbose_name='Password'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(max_length=15, null=True, verbose_name='Tipo'),
        ),
    ]
