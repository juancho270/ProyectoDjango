# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_www', '0002_auto_20171027_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='1234', max_length=20, verbose_name='Password'),
        ),
    ]
